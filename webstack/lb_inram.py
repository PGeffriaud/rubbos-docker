#!/usr/bin/env python
# -*- coding: utf-8 -*-


# lb_inram.py
# Script python gérant la création et la suppression de containers Docker
# Dépendances : psutils (librairie Python, trouvable dans les dépôts, par exemple "python_psutil")
# Commande de lancement : python lb_inram.py

# Nouvelle stratéie initiée suite aux problèmes de montée en charge
# Principe : nous créons tous les docks au lancement du script, puis les stoppons (sauf un)
# 	     Cela permettra de lancer les docks plus rapidement

import psutil
import time
import math
from subprocess import Popen, PIPE
import signal
import sys
import os.path

###################################
#
# Pour gérer la stratégie utilisée, changer l'import ci-dessous par le nom de fichier de la stratégie (sans l'extension)
#
###################################

from strategy4stairs_static import LoadBalancer


## Constantes du script

DOCK_HOSTNAME = "localhost"
DOCK_BEGIN_PORT = 33300
NGINX_UPDATE_CMD = "./lb-setup.sh"
PHP_CREATE = "php-create.sh"
PHP_REMOVE = "php-remove.sh"
PHP_START = "php-start.sh"
PHP_STOP = "php-stop.sh"


dockList = []
port = DOCK_BEGIN_PORT
stop = False

class Dock:

	def __init__(self, dockId, port):
		self.dockId = dockId
		self.port = port

	def __str__(self):
		return "(Dock) Id: " + str(self.dockId) + " Port: " + str(self.port)

	def getDockId(self):
                return self.dockId

	def getPort(self) : 
		return self.port

def execScript(filename, args):
	scriptPath = os.path.abspath(filename)
	callCmd = [scriptPath]
	for arg in args: 
		callCmd.append(arg)
	pipe = Popen(callCmd, stdout=PIPE)
	val = str(pipe.communicate()[0]).replace("\\n'", '').replace("b'", "")
	return val

def updateNginxConf(docks) :
	scriptPath= os.path.abspath("./lb-setup.sh")
	fullCmd = [scriptPath, "80"]
	for dock in docks : 
		fullCmd.append("localhost:" + dock.getPort())
	Popen(fullCmd)

def createDock():
	global dockList
	global port
	port+=1
	dockId = execScript(PHP_CREATE, [str(port)])
	newDock = Dock(dockId,str(port))
	print("+ Running: " + str(newDock))
	dockList.append(newDock)
	return newDock

def stopDock(running):
	global dockList
	toStop = running.pop()
	stoppedResponse = execScript(PHP_STOP, [toStop.getDockId()])
	if(stoppedResponse == toStop.getDockId()):
		print("- Stopped: " + str(toStop))
		dockList.append(toStop)
		return running
	else :
		print("Stop failed: " + str(stoppedResponse))

def startDock():
	global dockList
	toStart = dockList.pop(0)
	startResponse = execScript(PHP_START, [toStart.getDockId()])
	if(startResponse == toStart.getDockId()):
		print("+ Launched: " + str(toStart))
		return toStart
	else:
		print("Launch failed: " + str(startResponse))

def deleteDock():
	global dockList
	toDelete = dockList.pop()
	deletedResponse = execScript(PHP_REMOVE, [toDelete.getDockId()])
	if(deletedResponse == toDelete.getDockId()):
		print("- Deleted: " + str(toDelete))
	else :
		print("Delete failed: " + str(deletedResponse))

def updateDockList():
	global dockList
	lbUpdateParams = ""
	for dock in dockList :
		lbUpdateParams += " " + DOCK_HOSTNAME + ":" + dock.port
	fullCmd = NGINX_UPDATE_CMD + lbUpdateParams
	subprocess.call(fullCmd, shell=True)


def getStats() :
    return {
     'cpu': 100 - psutil.cpu_times_percent(interval=1).idle,
     'mem_available': psutil.virtual_memory().available,
     'dockSize': 500 * 1000
    }


def quit(signal, frame):
	global dockList
	global stop
	stop = True
	while (len(dockList) > 0):   
		deleteDock()

def createDocks():
	global port
	for i in range(0, LoadBalancer.nbDocks):
		createDock()
		

def main() :
	global dockList
	global stop
	print("Programme de Load Balancing -- Application Rubbos")
	signal.signal(signal.SIGINT, quit)
	# All the docks are runned at the beginning, and then stored
	createDocks()
	running = list(dockList)
	dockList = []
	# We keep forever at least one dock running
	while len(running) > 1:
		running = stopDock(running)
	updateNginxConf(running)

	stats = getStats()
	loadBalancer = LoadBalancer(stats['cpu'],stats['mem_available'], stats['dockSize'], len(running))

	while (not(stop)):
		stats = getStats()
		print("\nCPU: " + str(stats['cpu']))
		print("Active: " + str(len(running)))
		loadBalancer.add(stats['cpu'], stats['mem_available'], stats['dockSize'], len(running))
		toStart = loadBalancer.judge() - len(running)
		print("To create: " + str(toStart))
		
		print("DockList " + str(len(dockList)))
		print("Running: " + str(len(running)))

		while(toStart > 0):
			running.append(startDock())
			loadBalancer.add(stats['cpu'], stats['mem_available'], stats['dockSize'], len(running))
			toStart = loadBalancer.judge() - len(running)
			updateNginxConf(running)

		while(toStart < 0):
			running = stopDock(running)
			loadBalancer.add(stats['cpu'], stats['mem_available'], stats['dockSize'], len(running))
			toStart = loadBalancer.judge() - len(running)
			updateNginxConf(running)
		time.sleep(5)
main()
