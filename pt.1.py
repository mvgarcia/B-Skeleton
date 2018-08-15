import numpy as np
import matplotlib.pyplot as plt
import h5py
data=np.loadtxt('C:/Users/Yilver Garcia/Desktop/B-Skeleton/xyzM.dat')
x=data[0]
y=data[1]
z=data[2]
M_x=[np.max(x),np.min(x)]
M_y=[np.max(y),np.min(y)]
M_z=[np.max(z),np.min(z)]
datos=[data[:,i] for i in range(len(data[0]))]
data_graph=[]

for z in range(len(datos)):
    if(datos[z][2]>980 and datos[z][2]<1000):
       data_graph.append(datos[z])
 
data_graph=np.array(data_graph)  
plt.xlim(500,1000) 
plt.ylim(500,1000)
plt.scatter(data_graph[:,0],data_graph[:,1],s=0.1,alpha=0.4)
log_Mtot=[np.log10(data_graph[:,4])]
plt.hist(log_Mtot)
"""
¿Cómo se llegó al nuevo archivo de texto?

complete=np.loadtxt('C:/Users/Yilver Garcia/Desktop/B-Skeleton/CatshortW.0088.04.DAT') 
x=complete[:,0]
y=complete[:,1]
z=complete[:,2]
data=np.array([x,y,z])
np.savetxt('C:/Users/Yilver Garcia/Desktop/B-Skeleton/xyz.dat',data)

Mbound=complete[:,7]
M=complete[:,8]
data=np.array([M,Mbound])
np.savetxt('C:/Users/Yilver Garcia/Desktop/B-Skeleton/M.dat',data)
data=np.array([x,y,z,Mbound,M])
np.savetxt('C:/Users/Yilver Garcia/Desktop/B-Skeleton/xyzM.dat',data)
"""



