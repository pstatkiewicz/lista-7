import matplotlib.pyplot as plt
from math import sqrt
import random
class Rocket:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def get_position(self):
        position="(%s,%s)"%(self.x,self.y)
        return position

    def move(self,x,y):
        self.x+=x
        self.y+=y

    def get_distance(self,rocket):
        distance=sqrt((rocket.x-self.x)**2+(rocket.y-self.y)**2)
        return distance

    def way(self,xlist=[],ylist=[]):
        plt.plot(xlist,ylist)


plt.axis([-25,25,-25,25])
plt.grid(True)
a=Rocket(0,0)
print("Starting position:",a.get_position())
plt.plot(a.x,a.y,'o')
for i in range(5):
    a.move(random.randint(-5,5),random.randint(-5,5))
    print(i+1,"position:",a.get_position())
    plt.plot(a.x,a.y,'o')
plt.title("Shifts")
plt.show()


rockets=[]
plt.axis([-25,25,-25,25])
plt.grid(True)
print("Generated points:")
for i in range(5):
    rockets.append(Rocket(random.randint(-5,5),random.randint(-5,5)))
    plt.plot(rockets[i].x,rockets[i].y,'o')
    for k in range(5):
            if i>k:
                print("Distance between",k+1,"rocket and",i+1,"rocket is",rockets[i].get_distance(rockets[k]))
plt.title("Generated rockets")
plt.xlabel("1 - blue   2 - yellow   3 - green   4 - red   5 - violet")
plt.show()
for i in range(5):
    plt.axis([-25,25,-25,25])
    plt.grid(True)
    print(i+1,"move:")
    for j in range(5):
        rockets[j].move(random.randint(-5,5),random.randint(-5,5))
        plt.plot(rockets[j].x,rockets[j].y,'o')
        for k in range(5):
            if j>k:
                print("Distance between",k+1,"rocket and",j+1,"rocket is",rockets[j].get_distance(rockets[k]))
    plt.title(str(i+1)+" move")
    plt.xlabel("1 - blue   2 - yellow   3 - green   4 - red   5 - violet")
    plt.show()


plt.axis([-25,25,-25,25])
plt.grid(True)
rockets=[]
for i in range(5):
    xlist=[]
    ylist=[]
    xlist1=[]
    ylist1=[]
    rockets.append(Rocket(random.randint(-15,15),random.randint(-15,15)))
    plt.plot(rockets[i].x,rockets[i].y,'bo')
    xlist.append(rockets[i].x)
    ylist.append(rockets[i].y)
    for j in range(5):
        rockets[i].move(random.randint(-5,5),random.randint(-5,5))
        xlist1.append(rockets[i].x)
        ylist1.append(rockets[i].y)
        if j!=5-1:
            plt.plot(rockets[i].x,rockets[i].y,'o')
        else:
            plt.plot(rockets[i].x,rockets[i].y,'ro')
    xlist.extend(xlist1)
    ylist.extend(ylist1)
    rockets[i].way(xlist,ylist)
plt.title("Rocket road")
plt.xlabel("start - blue          end - red")
plt.show()
