from scipy.spatial import Delaunay, QhullError
import numpy as np

def is_collinear(points_arr):
    
    if len(points_arr) < 3:
        return True
    v = points_arr[1] - points_arr[0]
    for i in range(2, len(points_arr)):
        w = points_arr[i] - points_arr[0]
        if np.abs(v[0]*w[1] - v[1]*w[0]) > 1e-10:
            return False
    return True

def triangulate_points(points):
   
    if not points or len(points) < 3:
        return [] 

   
    points = list(dict.fromkeys(points))
    points_arr = np.array(points, dtype=float)

   
    if points_arr.shape[1] == 2:
        if is_collinear(points_arr):
            return [] 
        points_arr = np.hstack([points_arr, np.zeros((len(points_arr),1))])

    
    points_arr += np.random.normal(scale=1e-10, size=points_arr.shape)

    try:
        tri = Delaunay(points_arr)
        return [tuple(simplex) for simplex in tri.simplices]
    except QhullError:
        return []

def area(triangle, points):
  
    i, j, k = triangle
    x1, y1 = points[i]
    x2, y2 = points[j]
    x3, y3 = points[k]
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
