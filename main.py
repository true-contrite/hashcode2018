from vehicle import *

def parseinput(file):

	input_array = []
	ride_array = []

	with open(file) as inputfile:

		for line in inputfile:

			input_array.append(line.replace(" ","").rstrip())

	for i in range (1, len(input_array)):
		
		ride_array.append(Ride([input_array[i][0], input_array[i][1]], [input_array[i][2], input_array[i][3]], input_array[i][4], input_array[i][5],i))

	return [ride_array, input_array[0][2]] #RETURNS ARRAY OF RIDES and No. of Vehicles

def makeVehicles(num):

	vehicle_array = []

	for i in range(0, int(num)):

		vehicle_array.append(Vehicle(i))

	return vehicle_array

def sortRides(ride_array):

	return sorted(ride_array, key=Ride.get_difference)

###################################################################



parse_array = parseinput("a_example.in")

number_of_vehicles = parse_array[1]
ride_array = sortRides(parse_array[0])


inuse = []
notinuse = makeVehicles(number_of_vehicles)

for ride in ride_array:

	pass

