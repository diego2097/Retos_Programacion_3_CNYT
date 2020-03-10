import matplotlib.pyplot as plt 
import numpy as np 

def graficarProba(vector): 
    print(vector)
    x = []
    y = []
    for i in range(len(vector)): 
        x.append("Estado " + str(i+1))
    for i in range(len(vector)): 
        y.append(vector[i])
    xx = np.array(x)
    yy = np.array(y)
    plt.bar(xx,yy,align="center")
    plt.show()

