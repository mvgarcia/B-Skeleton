#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
entrada_10=np.loadtxt("beta_10xyz.dat")


# In[87]:


salida_int=[]
grafica=[]
def grafica(entrada,salida_double):
    salida_int=[]
    for i in range(len(salida_double)):
        salida_int.append([int(salida_double[i][0]),int(salida_double[i][1])])
    salida_int=np.array(salida_int)
    grafica=[]
    for i in range(len(salida_int)):
        m=salida_int[i][0]
        n=salida_int[i][1]
        grafica.append([entrada[m][0],entrada[n][1]])
    grafica=np.array(grafica)
    return(grafica)


# In[81]:


beta1_salida_10=np.loadtxt("b1_10_d2.dat")
grafica1=grafica(entrada_10,beta1_salida_10)
plt.xlim(0,130) 
plt.ylim(370,500)
#plt.scatter(entrada_10[:,0],entrada_10[:,1],s=0.2,alpha=1)
plt.plot(grafica[:,0],grafica[:,1],linewidth=0.50)


# In[98]:


beta2_salida_10=np.loadtxt("b2_10_d2.dat")
grafica2=grafica(entrada_10,beta2_salida_10)
plt.plot(grafica2[:,0],grafica2[:,1],linewidth=0.50)


# In[99]:


beta3_salida_10=np.loadtxt("b3_10_d2.dat")
grafica3=grafica(entrada_10,beta3_salida_10)
plt.plot(grafica3[:,0],grafica3[:,1],linewidth=0.50)


# In[100]:


beta10_salida_10=np.loadtxt("b10_10_d2.dat")
grafica10=grafica(entrada_10,beta10_salida_10)
plt.plot(grafica10[:,0],grafica10[:,1],linewidth=0.50)


# In[102]:


beta15_salida_10=np.loadtxt("b10_10_d2.dat")
grafica15=grafica(entrada_10,beta15_salida_10)
plt.xlim(0,130) 
plt.ylim(370,500)
plt.plot(grafica15[:,0],grafica15[:,1],linewidth=0.50)


# In[ ]:




