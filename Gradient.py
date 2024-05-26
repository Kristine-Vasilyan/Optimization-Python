import numpy as np
import math
def grad_apriori(A, b, x0, e0):
    k = 0
    xk = x0
    df = np.dot(A,xk)+b
    while((np.linalg.norm(df) ) > e0):
        k = k + 1
        ak = 1/(k+1)
        hk = -(np.dot(A,xk)+b)
        xk = xk + ak*hk
        df = np.dot(A,xk)+b
    return (xk, k)
def grad_maxfall(A, b, x0, e0):
    k = 0
    xk = x0
    df = np.dot(A,xk)+b
    while((np.linalg.norm(df) ) > e0):
        k = k + 1
        hk = -(A.dot(xk)+b)
        ak = -((A.dot(xk)+b).dot(hk))/((A.dot(hk)).dot(hk))
        xk = xk + ak*hk
        df = np.dot(A,xk)+b
    return (xk, k)  
def f(x,A,b):
    return 1/2*np.dot(np.dot(A,x),x)+np.dot(b,x)
def df(x, A, b):
    return np.dot(A,x)+b
def grad_division(A, b, x0, e, e0):
    xk=x0
    k = 0
    while(np.linalg.norm(df(xk, A, b)) > e0):
        k = k+1
        ak = 1
        hk = -(A.dot(xk)+b)
        while((f(xk - ak*df(xk, A, b), A,b) - f(xk, A, b)) > (-e*ak*np.linalg.norm(df(xk, A, b))**2)):
            ak = ak/2
        xk = xk + ak*hk    
    return (xk,k)    
    
np.set_printoptions(precision=3)
# A = np.array([[18, 0],
#                [0, 2]])
# b = np.array([0, 0])
# x0 = np.array([1, 1])
# e0=0.05
# e = 0.05
n = int(input("Enter  n: "))
input_str = input("Enter elements of the A: ")
elements = list(map(float, input_str.split()))
A = np.array(elements).reshape(n,n)
input_str = input("Enter b: ")
elements = list(map(int, input_str.split()))
b = np.array(elements)
input_str = input("Enter x0: ")
elements = list(map(int, input_str.split()))
x0 = np.array(elements)
e0 = float(input("Enter e0: "))
e = float(input("Enter e: "))
out = grad_apriori(A, b, x0, e0)
print("grad_apriori is: ")
print(out)
print("grad_maxfall is: ")
out = grad_maxfall(A, b, x0, e0)
print(out)
print("grad_division is: ")
out = grad_division(A,b, x0, e,e0 )
print(out)