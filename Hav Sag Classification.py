import numpy as np
import matplotlib.pyplot as plt
def printplot(x1, x2, y, w1, w2):
    plt.scatter(x1[y == 1], x2[y == 1] , color='red') 
    plt.scatter(x1[y == -1] , x2[y == -1], color='blue')
    x = np.linspace(0, 50, 100)
    if w1[1] != 0:
        y1 = (-w1[0] * x +w1[2] ) / w1[1]
    else:
        y1 = np.full_like(x, w2[2] / w2[0])  
    if w2[1] != 0:
        y2 = (-w2[0] * x +w2[2] ) / w2[1]
    else:
        y2 = np.full_like(x, w2[2] / w2[0])      
    plt.plot(x, y1, label=f'{w1[0]}x + {w1[1]}y + {w1[2]} = 0', color='black')
    plt.plot(x, y2, label=f'{w2[0]}x + {w2[1]}y + {w2[2]} = 0', color= 'green')
    plt.show()      
    
def rosenblatt(x1, x2, y):
    w = [0, 0, 0]
    i = 0
    while i < 10:
        i = 0
        while i < 10:
            x = np.array([x1[i], x2[i], -1])
            if(np.dot(w,x)*y[i] <= 0):
                w = x*y[i]+w 
                break
            i = i + 1
    return w        

#wt = gumar(xt*yi)*(gumarx*xt)-1 
#w = (w0, w1, w2)
# x = (x1, x2, 1)
def qar_sheghum(x1, x2, y):
    A = 0
    B = 0
    for i in range(10):
        x = np.array([x1[i], x2[i], -1])
        A = A + np.transpose(x)*y[i]
        B = B + np.outer(x, x)
    w = np.dot(A,np.linalg.inv(B))[np.newaxis]    
    return w.T
        
x1 = np.array([10, 20, 25, 20, 15, 40, 30, 20, 40, 7])
x2 = np.array([50, 30, 30, 60, 70, 40, 45, 45, 30, 35])
y = np.array([+1, -1, -1, +1, +1, -1, -1, +1, -1, +1])
printplot(x1, x2, y, rosenblatt(x1, x2, y), qar_sheghum(x1, x2, y))

