import numpy as np
w12 = w34 = [[1,0.9],[0.9,1]]
w23 = w35 = [[0.1,1],[1,0.1]]
o2 = [1,0.1]
o4 = [0.1,1]
mm = lambda mat1, mat2: np.matmul(mat1,mat2)
s = lambda mat: np.sum(mat, axis=1)

print("b1:", mm(w12,mm(w23,s(w35)*mm(w34,o4))*o2))

print("b2:", b2 = mm(w23,s(w35)*mm(w34,o4))*o2*s(w12))

print("b3:", b3 = s(w35)*mm(w34,o4)*mm(w23,s(w12)*o2))

print("b4:", b4 = mm(w34,s(w35)*mm(w23,s(w12)*o2))*o4)

print("b5:", b5 = mm(w35,mm(w34,o4)*mm(w23,s(w12)*o2)))