import numpy as np
import matplotlib.pyplot as plt

#iniit des donnees
def init():
    global data
    
    f=np.loadtxt("data/taillepoids_f.txt")
    h=np.loadtxt("data/taillepoids_h.txt")
    Nf=f.size
    Nh=h.size

    f=np.vstack((np.ones((1,Nf/2)),f.T))
    h=np.vstack(((np.ones((1,Nh/2))*0),h.T))

    data=np.concatenate((f,h),axis=1)
    
# function qui pour un x donne retourne la valeur y
# x appartient au donnees
def oracle(x):
    global data
    return data[0,x]
    
# def pasT(pas):
#    return 0.5/(0.5+pas)

# def nextTheta(theta, pas):
#     print "not yet"

# def erreurLogis(theta):
#     print "not yet"

# def descenteGrad():


if __name__ == '__main__':
    global data
    
    init()
    
    print data.shape
    print data
    #plt.show()
