import numpy as np
import matplotlib.pyplot as plt

#iniit des donnees
def init():
    global data
    global Pfemme
    global Phomme
    
    
    f=np.loadtxt("data/taillepoids_f.txt")
    h=np.loadtxt("data/taillepoids_h.txt")
    Nf=f.size
    Nh=h.size

    Pfemme=(Nf)/(Nf+Nh)
    Phomme=(Nh)/(Nf+Nh)
    
    f=np.vstack((np.ones((1,Nf/2)),f.T))
    h=np.vstack(((np.ones((1,Nh/2))*0),h.T))

    data=np.concatenate((f,h),axis=1)
    
# function qui pour un x donne retourne la valeur y
# x appartient au donnees
def oracle(x):
    global data
    return data[0,x]

def sigmoide(t, A, b):
    return (1.0/(1.0+np.exp(-((A*t)+b))))

def pasT(pas):
    return 0.5/(0.5+pas)

def nextTheta(theta, pas):
    global data

    quartCal=np.dot(data,(data[0] - np.sum(np.dot(data.T, theta))))
    demiCal=(pasT(pas)/data[0].size)* quartCal
    
    return theta + demiCal

def fTheta(theta):
   global data

   return np.dot(data.T, theta)


# def erreurLogis(theta):
#     print "not yet"

# def descenteGrad():


if __name__ == '__main__':
    global data
    global Pfemme
    global Phomme

    #init
    init()
    theta=np.array([0,0,0])

    theta=nextTheta(theta, 0.5)
    print theta
       
    theta=nextTheta(theta, 0.4)
    print theta

    theta=nextTheta(theta, 0.4)
    print theta

    ftheta=fTheta(theta)

    plt.plot(ftheta, '*')

    #plt.plot(data[1], sigmoide(data[1],1,-170),'*')
    plt.show()
