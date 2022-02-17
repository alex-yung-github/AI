import sys
from queue import Queue
from heapq import heappop, heapify,heappush
from math import pi , acos , sin , cos
import time
import tkinter as alan
 
globaldict = {} #Key : [(destination, distance)]
distdict = {}
citynodedict = {}
canvasdict = {}
linedict = {}
latratio = 0
longratio = 0
root = alan.Tk()

 
def calcd(node1, node2):
#    y1 = lat1, x1 = long1
#    y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2
 
   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
 
   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
 

def createnetwork():
    nodesfile = "rrNodes.txt"
    edgesfile = "rrEdges.txt"
    nodecities = "rrNodeCity.txt"
    with open(nodecities, "r") as f:
        for line in f:
            temp = line.split()
            id = temp[0]
            string = ""
            for i in range(1, len(temp)):
                string += temp[i].strip() + " "
            citynodedict[id] = string.strip()
    with open(nodesfile, "r") as f:  
        for line in f:  
            temp = line.split()
            nameid = temp[0].strip()
            if(nameid in citynodedict):
                name = citynodedict[nameid]
            else:
                name = nameid
            lat = float(temp[1].strip())
            long = float(temp[2].strip())
            distdict[name] = [lat, long]
    with open(edgesfile, "r") as f:
        for line in f:
            temp = line.split()
            node1 = temp[0]
            if(node1 in citynodedict):
                node1 = citynodedict[node1]
            node2 = temp[1].strip()
            if(node2 in citynodedict):
                node2 = citynodedict[node2]
            d = calcd(distdict[node1], distdict[node2])
            if(node1 not in globaldict.keys()):
                globaldict[node1] = []
            globaldict[node1].append((node2, d))
            if(node2 not in globaldict.keys()):
                globaldict[node2] = []
            globaldict[node2].append((node1, d))


def djikstra(start, end):
    depth = 0
    visited = set()
    startf = (depth, start)
    fringe = []
    heappush(fringe, startf)
    while(len(fringe) > 0):
        v = heappop(fringe)
        if(end == v[1]):
            return (v)
        if(v[1] not in visited):
            visited.add(v[1])
            for i in globaldict[v[1]]:
                if i not in visited:
                    temp = finddist(v[1], i[0])
                    newdepth = v[0] + temp
                    heappush(fringe, (newdepth, i[0]))
    return None


def astar(start, end):
    depth = 0
    visited = set()
    fringe = []
    heuristic = calcd(distdict[start], distdict[end])
    startf = (heuristic + depth, depth, start)
    heappush(fringe, startf)
    while(len(fringe) > 0):
        v = heappop(fringe)
        if(end == v[2]):
            return (v)
        if(v[2] not in visited):
            visited.add(v[2])
            for i in globaldict[v[2]]:
                if i not in visited:
                    temp = finddist(v[2], i[0])
                    newdepth = v[1] + temp
                    newh = newdepth + calcd(distdict[i[0]], distdict[end])
                    heappush(fringe, (newh, newdepth, i[0]))
    return None


def finddist(start, end):
    for i in globaldict[start]:
        if(i[0] == end):
            return i[1]
    return None

    
def convertpixels(): # take screen width and height; then take the length of the longitude and latitude
    #by finding the maxlatitude, minlatitude, maxlongitude, and minlongitude. THen
    #divide the width and height of the screen by the length of the longitude and latitude
    #for the ratio of window per pixel. Then take that measurement and get the x and y coordinates of
    #all of the cities and the different ids. Then make black lines between them.
    maxlong = 0
    maxlat = 0
    btemp = distdict["1800608"]
    minlat = btemp[0]
    minlong = abs(btemp[1])
    for i in distdict:
        temp = distdict[i]
        if(temp[0] > maxlat):
            maxlat = temp[0]
        elif(temp[0] < minlat):
            minlat = temp[0]
        if(abs(temp[1]) > maxlong):
            maxlong = abs(temp[1])
        elif(abs(temp[1]) < minlong):
            minlong = abs(temp[1])
    longdist = maxlong - minlong
    latdist = maxlat - minlat
    print (latdist, longdist)
    latratio = 800/latdist
    longratio = 800/longdist
    print(latratio, longratio)
    return [latratio, longratio, minlat, minlong]


def canvasConversion():
    ratiolist = convertpixels()
    latratio = ratiolist[0]
    longratio = ratiolist[1]
    minlat = abs(ratiolist[2])
    minlong = abs(ratiolist[3])
    for i in distdict:
        temp = distdict[i]
        newlat = 800 - ((abs(temp[0]) - minlat) * latratio)
        newlong = 800 - ((abs(temp[1]) - minlong) * longratio)
        canvasdict[i] = [newlong, newlat]


def makeCanvas(canvas):
    #canvas.create_line(0, 0, 400, 400, fill='black')
    #canvas.winfo_reqheight()
    count = 0
    for i in globaldict:
        start = canvasdict[i]
        for j in globaldict[i]:
            endnode = j[0]
            end = canvasdict[endnode]
            line = canvas.create_line(start, end, fill = "black")
            linedict[(i, endnode)] = line
            linedict[(endnode, i)] = line


def setBaseLine(canvas, color):
    for node in linedict:
        line = linedict[node]
        canvas.itemconfig(line, fill = color)
        root.update()
    canvas.mainloop()

def changeColor(start, end, canvas, color):
    for i in linedict:
        if(i == (start, end)):
            line = linedict[(start, end)]
            canvas.itemconfig(line, fill = color)
# start = sys.argv[1]
# end = sys.argv[2]
# start = "Albuquerque"
# end = "Atlanta"
canvas = alan.Canvas(root, height=800, width=800, bg='white') #creates a canvas widget, which can be used for drawing lines and shapes
canvas.pack(expand=True)
createnetwork()
canvasConversion()
makeCanvas(canvas)
setBaseLine(canvas, "black")
# t1 = time.perf_counter()
# tem = djikstra(start, end)
# t2 = time.perf_counter()
# t3 = time.perf_counter()
# tem2 = astar(start, end)
# t4 = time.perf_counter()
# print("Length", tem[0], "Time", "%s" % (t2 - t1))
# print("Length", tem2[1], "Time", "%s" % (t4 - t3))
 
 
