class Vehicle():

	def __init__(self,id):

		self.position = [0,0]
		self.destination = None
		self.available = True
		self._uid = id

	def __str__(self):

		return("VEHICLE: " + "position: " + str(self.position) + " destination: " + str(self.destination) + " Available: " + str(self.available))

##SETTERS
	def set_pos(self, newpos):
		self.position = newpos

	def set_dest(self, newdest):
		self.destination = newdest

	def set_available(self, available):
		self.available = bool(available)

##GETTERS
	def get_pos(self):
		return self.position

	def get_dest(self):
		return self.destination

	def get_available(self):
		return self.available

class Ride():

	def __init__(self, start, end, early, late, id):

		self.startpos = start
		self.endpos = end
		self.earlytime = early
		self.latetime = late
		self.timedif = int(late) - int(early)
		self.claimed = False
		self.id = id

	def __str__(self):

		return("RIDE: Start Position: " + str(self.startpos) + " End Position: " + str(self.endpos) + " Earlytime: " + str(self.earlytime) + " Latetime: " + str(self.latetime))

	def __repr__(self):

		return("RIDE: Start Position: " + str(self.startpos) + " End Position: " + str(self.endpos) + " Earlytime: " + str(self.earlytime) + " Latetime: " + str(self.latetime))

##GETTERS
	def get_start(self):
		return self.startpos

	def get_end(self):
		return self.endpos

	def get_earlytime(self):
		return self.earlytime

	def get_latetime(self):
		return self.latetime
 
	def get_claimed(self):
		return self.claimed

	def get_difference(self):
		return self.timedif
##SETTERS
	def set_claimed(self, boole):
		self.claimed = boole