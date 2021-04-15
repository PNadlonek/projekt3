import numpy as np 
import matplotlib.pyplot as plt
###### 2 #######
c=0
f=0
#geometria
x_0=0
x_p=1

wezly = np.array([[1,0],
                 [2,1],
                 [3,0.5], 
                 [4,0.75]])

elementy = np. array([[1, 1, 1],
                      [2, 4, 2], 
                      [3, 3, 4]])

twb_L ='D'
twb_R ='D'

wwb_L = 0 
wwb_R = 1 

##### Zadanie 3 

def GenerujTabliceGeometrii(x_0,x_p,n):
    template = (x_p-x_0)/(n-1)
    wezly = np.array([x_p,x_0])
    
    for i in range(1, n-1, 1):
        wezly = np.block([wezly, i * template + x_p])
    
    return wezly
print(GenerujTabliceGeometrii(0,1,100),"węzły")

######## Zadanie 4

def RysujGeometrie(wezly, elementy):
    li_wezlow = np.size(wezly)
    y=np.zeros((li_wezlow,1))
    plt.plot(wezly[:,1], y, 'r .')
    