import Image, ImageSequence, math
from numpy import *
import scipy as Sci
import scipy.linalg
import scipy.sparse.linalg
import scipy.sparse.linalg.eigen
import numpy


volume = 0
s = 100
pi = 3.14159266
file = open("F:\T152_Stats_total2.txt" , 'w')	
file.write('slices, area, volume, radius, xCom, yCom, semimajor, semiminor, orientation \n')
file.close
#for slices in extras:
for slices in range(4224,6225):
	radius = 0.0
	area = 0
	ySum = 0
	xSum = 0
	yCom = 0
	xCom = 0
	x2Sum = 0
	y2Sum = 0
	xySum = 0
	y2Com = 0
	x2Com = 0
	xyCom = 0
	eArray = scipy.zeros((1650, 800), float) 
	#im = Image.open("/Users/mdgreenb/Dropbox/In Progress/T82/T82_Stats_%04i.png" % slices)
	im = Image.open("E:\Users\Stardust\Desktop\T152_zSlices2\T152_sliced_%04i.png" % slices)
	for x in range(im.size[0]-1):
		for y in range(im.size[1]-1):
			val = im.getpixel((x,y))
			if val < 100:
				area = area + 1
				xSum = xSum + x
				ySum = ySum + y
				eArray[x,y] = 1
				x2Sum = x2Sum + (x*x)
				y2Sum = y2Sum + (y*y)
				xySum = xySum + (x*y)
	volume = volume + area
	radius = math.sqrt(area/pi)
	if area > 0:
		xCom = xSum / area
		yCom = ySum / area
		x2Com = x2Sum / area
		y2Com = y2Sum / area
		xyCom = xySum / area
	arr = scipy.array([[ x2Com - (xCom * xCom), xyCom - (xCom * yCom)],[ xyCom - (xCom * yCom) , y2Com - (yCom * yCom) ]])
	vals, vecs = scipy.linalg.eigh(arr)
	#print vecs.shape
	#print vecs
  	#print vecs[0,1]

	semimajor = math.sqrt(abs(vals[0])) * 2.0
	semiminor = math.sqrt(abs(vals[1])) * 2.0
 	orientation = numpy.arccos(vecs[0,1]) * (180 / pi)

	file.write('%i, %i, %i, %.3f, %i, %i, %.3f, %.3f, %.2f' %  (slices, area, volume, radius, xCom, yCom, semimajor, semiminor, orientation))
	file.write('\n')
	file.close
	print slices, area, volume, radius, xCom, yCom, semimajor, semiminor, orientation
