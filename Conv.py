import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def prod(p, q, r):
    return np.cross(q - p, r - q)

def convex_hull(points):
    n = len(points)
    if n < 3:
        return "we can't do it"
    left = np.argmin(points, axis=0)[0]
    p = left
    q = None
    hull = []
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if i == p:
                continue
            if prod(points[p], points[q], points[i]) < 0:
                q = i
        p = q
        if p == left:
            break
    return hull

def plot_points(points, hull_points):
    plt.figure()
    plt.scatter(points[:,0], points[:,1])
    hull_points = np.array(hull_points + [hull_points[0]])
    plt.plot(hull_points[:,0], hull_points[:,1], 'r-')
    plt.show()

n = int(input("Enter the number of points: "))
points = []
for i in range(n):
    x, y = map(int, input(f"Enter the point {i + 1} (x, y): ").split())
    points.append((x, y))
points = np.array(points)
result = convex_hull(points)
plot_points(points, result)
