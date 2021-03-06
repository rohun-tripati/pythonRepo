#Author : @Rohun
#Found in BanData, For the data which has not ".PEN_DOWN" 
#and which had 1 for pendowm and 0 start of new stroke

from matplotlib import pyplot as plt
import random, time, os, sys
from os import walk

def processPath(pathname):
	dirs = []
	for (r,d,f) in walk(pathname):
		dirs.extend(d)
		break
	for g1 in dirs:
		pathname = pathname.rstrip("/") + "/" + g1
		dirs2 = []
		for (r,d,f) in walk(pathname):
			dirs2.extend(d)
			break
		return pathname + "/" + dirs2[0] + "/"
	print "PathName processing failed for pathname == ", pathname
	sys.exit(0)

def reverselist(y):
	return [y[i] for i in range( len(y)-1, -1, -1 )]

def PenDowmOn(line,x, y,first, second,firstlinecheck):
	continueflag = 0
	if line == ".PEN_DOWN" or line == ".PEN_UP":
		#change colour
		firstlinecheck = 1
		rand = random.random()%12

		last = first[ int(rand/4) ] + second[ int(rand)%4 ]

		if len(x)>0:
			plt.plot(x,y)
		x = []
		y = []
		continueflag = 1

	return continueflag, x,y, firstlinecheck
	
def NoPenDown(flag, first,second, x, y ):
	if flag == 1:
		rand = random.random() * 100
		rand =  int(rand) % 9
		last = first[ int(rand/3) ] + second[int(rand%2)]
		newx = x.pop()
		newy = y.pop()
		if len(x)>0:
			n = reverselist(x)
			m = reverselist(y)
			plt.plot(n	,m, last)
		x = [newx]
		y = [newy]
		flag = 0
	return flag, x, y

def main(strokepath,IsPenDownAvalable):
	try:
		strokefile = open(strokepath, "r")
	except:
		print "Cudn't Open ", strokepath
	first = ["r", "g", "b"]
	second = ["--", "-"]
	
	x = []
	y = []
	flag = 0
	firstlinecheck = 0

	for line in strokefile.readlines():
		line = line.strip()
		if IsPenDownAvalable == 1:
			continueflag, x, y, firstlinecheck = PenDowmOn(line,x, y, first, second, firstlinecheck)
			if continueflag == 1:
				continue
		else:
			flag, x, y = NoPenDown(flag, first,second, x, y)
		
		if firstlinecheck == 1:
			coor = line.split()
			x.append( float(coor[0]) )
			y.append( float(coor[1]) )
			if int(coor[2]) == 0:
				flag=1

	rand = random.random() * 100
	rand =  int (rand) % 9
	last = first[ int(rand/3) ] + second[int(rand%2)]
	if len(x)>0:

		n = reverselist(x)
		m = reverselist(y)
		plt.plot(n,m, last)
	plt.show()

IsPenDownAvalable = 1
path = os.curdir
startFolder = raw_input("Enter start point of folder : ")
path = os.path.join(path,startFolder)

dirs = []
for r,d,f in os.walk(path):
	dirs.extend(d)
	break

for d in dirs:
	files = []
	print path
	pathname = processPath(path.rstrip("/") + "/" + d)
	print pathname
	for r1,d1,f in os.walk(pathname):
		files.extend(f)
		break
		print f
	for i, f in enumerate(files):
		if i > 3:
			break
		filepath = os.path.join(pathname,f)
		print "File Drawn == ", filepath
		main(filepath, IsPenDownAvalable)