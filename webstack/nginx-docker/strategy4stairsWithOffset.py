
seuilOne = 25
seuilTwo = 50
seuilThree = 75 
offsetTreshold = 5 #offet entre les seuils up et down de chacun des seuils
offsetOverload = False # decide si l'on creee ou non des docks supplementaires si la charge CPU = 100%  


seuilDock = 1.5 
offset = 5

class LoadBalancer:
	def __init__(self, c, m,d, dockNumber):
		self.ChargeProc = c
		self.dockNumber = dockNumber
		self.MemoireLibre = m
		self.DockSize = d
		self.LastValue = 0.0 #initialisee a 0

	def DockMemFree(self):
		return (self.MemoireLibre > self.DockSize * seuilDock)

	def judge(self):
		if(self.ChargeProc == 100 and offsetOverload):
			return self.LastValue		
		elif(self.ChargeProc > seuilThree + offsetTreshold or (self.LastValue == 4 and self.ChargeProc > seuilThree - offsetTreshold)):
			self.LastValue = 4
			return 4
		elif(self.ChargeProc > seuilTwo + offsetTreshold or (self.LastValue == 3 and self.ChargeProc > seuilTwo - offsetTreshold)):
			self.LastValue = 3
			return 3
		elif(self.ChargeProc > seuilOne + offsetTreshold or (self.LastValue == 2 and self.ChargeProc > seuilOne - offsetTreshold)):
			self.LastValue = 2
			return 2
		else:
			self.LastValue = 1
			return 1
	
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
