import numpy as np

M = np.eye(5, dtype="int")
M[0,3] = 3
M[0,4] = 3
M[1,3] = 3
M[1,4] = 3
M[3,0] = 2
M[4,0] = 2
M[3,1] = 2
M[4,1] = 2

print(M)
