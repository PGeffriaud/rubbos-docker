
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
		return 4
	
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