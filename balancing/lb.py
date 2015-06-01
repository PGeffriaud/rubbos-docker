
import psutil
import time
import math


class Dock:

	def __init__(self, dockId, port):
		self.dockId = dockId
		self.port = port

	def __str__(self):
		return "(Dock) Id: " + str(self.dockId) + " Port: " + str(self.port)



def createDock(dockList, i):
	i+=1
	newDock = Dock("id",i)
	print("Création de l'élément")
	print(newDock)
	dockList.append(newDock)
	return i

def deleteDock(dockList):
	toDelete = dockList.pop()
	print("Suppression de l'élément")
	print(toDelete)
	dockList.remove(toDelete)

def main() :
	print("Programme de Load Balancing -- Application Rubbos")
	dockList = []
	lastPercent = 0
	i = 0

	while (True):
		percent = 100 - psutil.cpu_times_percent(interval=1).idle
		if(percent - lastPercent > 10):
			i = createDock(dockList, i)
			lastPercent = percent
			time.sleep(5)
		if(percent - lastPercent < 10 and len(dockList) > 0):
			deleteDock(dockList)
			lastPercent = percent
			time.sleep(5)

main()
