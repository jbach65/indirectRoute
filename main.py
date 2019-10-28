import random
import math

PI = 3.14159265
origin = [0,0]
destination = [10,10]
angleVariationDegrees = 340	#in degrees
angleVariationRad = math.radians(angleVariationDegrees)
maxDistance = 2
roundAngleTo = 5
roundPointTo = 2
maxPoints = 1000

points = []

def main():
	f = open("points.txt","w+")
	points.append(origin)
	while(distance(getCurrentPoint(),destination) >= maxDistance and len(points) < maxPoints):
		newPoint = generateNextPoint()
		points.append(newPoint)
	points.append(destination)
	writePoints(f)
	f.close()

#	print(angleToDestination())
#	print(angleVariationRad)
#	destAngle = angleToDestination()
#	minAngle = destAngle - (angleVariationRad/2)
#	maxAngle = destAngle + (angleVariationRad/2)
#	print(random.randint(int(round(minAngle*pow(10,roundAngleTo))),int(round(maxAngle*pow(10,roundAngleTo))))/pow(10,roundAngleTo))
#	print(random.randint(0,int(round(maxDistance*pow(10,roundPointTo))))/pow(10,roundPointTo))

def writePoints(f):
	for point in points:
		p = "{},{}\n".format(point[0],point[1])
		f.write(p)

def generateNextPoint():
	destAngle = angleToDestination()
	minAngle = destAngle - (angleVariationRad/2)
	maxAngle = destAngle + (angleVariationRad/2)
	randAngle = random.randint(int(round(minAngle*pow(10,roundAngleTo))),int(round(maxAngle*pow(10,roundAngleTo))))/pow(10,roundAngleTo)
	randDistance = random.randint(0,int(round(maxDistance*pow(10,roundPointTo))))/pow(10,roundPointTo)
	newX = round(randDistance*math.cos(randAngle),roundPointTo)
	newY = round(randDistance*math.sin(randAngle),roundPointTo)
	#print(str(len(points)) + "   (" + str(newX) + "," + str(newY) + ")")
	p = getCurrentPoint()
	newPoint = []
	newPoint.append(round(p[0] + newX,roundPointTo))
	newPoint.append(round(p[1] + newY,roundPointTo))
	return newPoint

def getCurrentPoint():
	return(points[len(points)-1])

def distance(p1,p2):
	return math.sqrt(math.pow(p2[1]-p1[1],2) + math.pow(p2[0]-p1[0],2))	#distance formula

def angleToDestination():
	p = getCurrentPoint()

	distX = destination[0]-p[0]
	distY = destination[1]-p[1]

	if(distX == 0 and distY >= 0):	#protect divide by zero, dont care about same point
		return math.radians(90.0)
	elif(distX == 0 and distY < 0):
		return math.radians(270.0)
	else:
		return math.atan2(distY,distX)

if __name__ == "__main__":
	main()
