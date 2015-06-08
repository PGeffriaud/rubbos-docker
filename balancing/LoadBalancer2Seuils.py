import psutil
import time 

seuilUp = 80 
seuilDown = 70
seuilDock = 1.5 



class LoadBalancer:
	def __init__(self, c, m,d):
		self.ChargeProc = c
		self.MemoireLibre = m
		self.DockSize = d

	def DockMemFree(self)
		return (self.MemoireLibre < self.DockSize * seuilDock)

	def judge(self):
		if(self.ChargeProc > seuilUp && DockMemFree()):
			return 1
		elif(self.ChargeProc < seuilDown):
			return 2
		else:
			return 0
	
	def add(self, c,m,d)
		self.ChargeProc = c
		self.MemoireLibre = m
		self.DockSize = d		
		


test = LoadBalancer(50,4096,100)

print("ChargeProc : " + str(test.ChargeProc))

print("Verdict : " + str(test.judge()))

"""

Charge processeur
Memoire utilise
(Disque Dur)

0 RAS
1 Creer un Dock
2 Supprimer un Dock

"""
