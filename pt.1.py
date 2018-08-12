import numpy as np
import matplotlib.pyplot as plt
import h5py
data=np.loadtxt('C:/Users/Yilver Garcia/Desktop/B-Skeleton/xyz.dat')
x=data[0]
y=data[1]
z=data[2]
M_x=[np.max(x),np.min(x)]
M_y=[np.max(y),np.min(y)]
M_z=[np.max(z),np.min(z)]
datos=[data[:,i] for i in range(len(data[0]))]
data_graph=[]

for z in range(len(datos)):
    if(datos[z][2]>500 and datos[z][2]<550):
       data_graph.append(datos[z])
   
#plt.plot(data_graph[:,1],data_graph[:,2])
"""
¿Cómo se llegó al nuevo archivo de texto?

complete=np.loadtxt('C:/Users/Yilver Garcia/Desktop/B-Skeleton/CatshortW.0088.04.DAT') 
x=complete[:,0]
y=complete[:,1]
z=complete[:,2]
data=np.array([x,y,z])
np.savetxt('C:/Users/Yilver Garcia/Desktop/B-Skeleton/xyz.dat',data)
"""



