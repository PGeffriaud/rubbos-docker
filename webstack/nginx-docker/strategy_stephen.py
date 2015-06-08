
seuilUp = 80 
seuilDown = 70
seuilDock = 1.5 



class LoadBalancer:
	def __init__(self, c, m,d, dockNumber):
		self.ChargeProc = c
		self.dockNumber = dockNumber
		self.MemoireLibre = m
		self.DockSize = d

	def DockMemFree(self):
		return (self.MemoireLibre > self.DockSize * seuilDock)

	def judge(self):
		print("Mémoire " + str(self.MemoireLibre))
		print("CPU " + str(self.ChargeProc))
		print("Mémoire libre " + str(self.DockMemFree()))
		if(self.ChargeProc > seuilUp and self.DockMemFree() or self.dockNumber == 0):
			return 1
		elif(self.ChargeProc < seuilDown and self.dockNumber > 1):
			return -1
		else:
			return 0
	
	def add(self, c,m,d, dockNumber):
		self.ChargeProc = c
		self.MemoireLibre = m
		self.DockSize = d
		self.dockNumber = dockNumber
		


"""

Charge processeur
Memoire utilise
(Disque Dur)

0 RAS
1 Creer un Dock
-1 Supprimer un Dock

"""
