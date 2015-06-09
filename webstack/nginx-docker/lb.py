#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import time
import math
from subprocess import Popen, PIPE
from strategy4stairs import LoadBalancer
import signal
import sys
import os.path

DOCK_HOSTNAME = "localhost"
DOCK_BEGIN_PORT = 33290
NGINX_UPDATE_CMD = "./lb-setup.sh"
PHP_CREATE = "php-create.sh"
PHP_REMOVE = "php-remove.sh"


dockList = []
i = DOCK_BEGIN_PORT
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



def updateNginxConf(dockList) :
	scriptPath= os.path.abspath("./lb-setup.sh")
	fullCmd = [scriptPath, "80"]
	for dock in dockList : 
		fullCmd.append("localhost:" + dock.getPort())
	Popen(fullCmd)

def createDock(dockList, i):
	i+=1
	scriptPath = os.path.abspath(PHP_CREATE)
	pipe = Popen([scriptPath, str(i)], stdout=PIPE)
	dockId = str(pipe.communicate()[0]).replace("\\n'", '').replace("b'", "");
	newDock = Dock(dockId,str(i))
	print("Création de l'élément")
	print(newDock)
	dockList.append(newDock)
	return i

def deleteDock(dockList):
	toDelete = dockList.pop()
	print("Suppression de l'élément " + str(toDelete.getDockId()))
	scriptPath = os.path.abspath(PHP_REMOVE)
	pipe = Popen([scriptPath, toDelete.getDockId()], stdout=PIPE)
	deletedResponse = str(pipe.communicate()[0]).replace("\\n'", "").replace("b'", "")
	if(deletedResponse == toDelete.getDockId()):
		print("Succès de la suppression")
	else :
		print("Échec de la suppression: " + str(deletedResponse))
	#subprocess.call([scriptPath, toDelete.getDockId])

def updateDockList(dockList):
	lbUpdateParams = ""
	for dock in dockList :
		lbUpdateParams += " " + DOCK_HOSTNAME + ":" + dock.port
	fullCmd = NGINX_UPDATE_CMD + lbUpdateParams
	subprocess.call(fullCmd, shell=True)

def getNumberOfDocks(percents):
	if(percents < 25):
		return 1
	if(percents < 50):
		return 2
	if(percent < 75):
		return 3
	if(percent < 90):
		return 4



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
		deleteDock(dockList)


def main() :
	global i
	global dockList
	global stop
	print("Programme de Load Balancing -- Application Rubbos")
	signal.signal(signal.SIGINT, quit)
	lastPercent = 0

	stats = getStats()
	loadBalancer = LoadBalancer(stats['cpu'],stats['mem_available'], stats['dockSize'], len(dockList))

	while (not(stop)):
		stats = getStats()
		print("CPU load: " + str(stats['cpu']))
		print("Active docks: " + str(len(dockList)))
		loadBalancer.add(stats['cpu'], stats['mem_available'], stats['dockSize'], len(dockList))
		toCreate = loadBalancer.judge() - len(dockList)
		print("To create: " + str(toCreate))

		while(toCreate > 0):
			i = createDock(dockList, i)
			updateNginxConf(dockList)
			loadBalancer.add(stats['cpu'], stats['mem_available'], stats['dockSize'], len(dockList))
			toCreate = loadBalancer.judge() - len(dockList)

		while(toCreate < 0):
			deleteDock(dockList)
			updateNginxConf(dockList)
			loadBalancer.add(stats['cpu'], stats['mem_available'], stats['dockSize'], len(dockList))
			toCreate = loadBalancer.judge() - len(dockList)

		time.sleep(5)
main()
