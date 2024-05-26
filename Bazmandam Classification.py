import numpy as np
import matplotlib.pyplot as plt
def swap_z_values(points):
    swapped_points = []
    for x, y, z in points:
        if z == -1:
            swapped_points.append((x, y, 1))
        elif z == 1:
            swapped_points.append((x, y, -1))
        else:
            swapped_points.append((x, y, z))
    return swapped_points

def group_x(points):
    grouped_points = {}
    for point in points:
        x_value = point[0]
        if x_value not in grouped_points:
            grouped_points[x_value] = []
        grouped_points[x_value].append(point)
    return grouped_points

def is_ok(points):
    grouped_by_x = group_x(points)
    for x_group in grouped_by_x.values():
        minus = []
        plus = []
        for point in x_group:
            x_value, y_value, z_value = point
            if z_value == -1:
                minus.append(point)
            elif z_value == 1:
                plus.append(point)
        if(len(minus) > 0 and len(plus) > 0):        
            min_minus = min(minus, key=lambda x: x[1], default=None)
            max_plus = max(plus, key=lambda x: x[1], default=None)
            if(min_minus < max_plus):
                return False
    return True
def gen_y(points):
    if(is_ok(points) == False):
        points = swap_z_values(points)
    grouped_by_x = group_x(points)
    new_y=[]
    for x_group in grouped_by_x.values():
        minus = []
        plus = []
        for point in x_group:
            x_value, y_value, z_value = point
            if z_value == -1:
                minus.append(point)
            elif z_value == 1:
                plus.append(point)
        if(len(minus) > 0 and len(plus) > 0):        
            min_minus = min(minus, key=lambda x: x[1], default=None)
            max_plus = max(plus, key=lambda x: x[1], default=None)
            new_y.append((min_minus[1]+max_plus[1])/2)
        elif(len(minus) > 0):
            min_minus = min(minus, key=lambda x: x[1], default=None)
            new_y.append(min_minus[1]-0.5)
        else:
            max_plus = max(plus, key=lambda x: x[1], default=None)
            new_y.append(max_plus[1] + 0.5)
            
    return new_y    
def lagrange_interpolation(x_values, y_values, x):
    M = len(x_values)
    result = 0.0
    for i in range(M):
        term = y_values[i]
        for j in range(M):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result     
def plot_lagrange_interpolation(x_values, y_values, x_range):
    y_interpolated = [lagrange_interpolation(x_values, y_values, x) for x in x_range]
    plt.plot(x_range, y_interpolated)
    plt.xlabel('x')
    plt.ylabel('y')
        
n = int(input("Enter the number of points: "))
points = []
for i in range(n):
    x, y, z = map(int, input(f"Enter the point {i + 1} (x, y, nshich): ").split())
    points.append((x, y, z))
new_y = gen_y(points)   
points_x = np.array([point[0] for point in points])
points_y = np.array([point[1] for point in points])
points_z = np.array([point[2] for point in points])
plot_lagrange_interpolation(np.unique(np.array([point[0] for point in points])),new_y, np.linspace(min(points_x)-0.5, max(points_x)+0.5, 1000))
plt.scatter(points_x[points_z == 1], points_y[points_z == 1] , color='red') 
plt.scatter(points_x[points_z == -1], points_y[points_z == -1] , color='blue')
plt.show()    