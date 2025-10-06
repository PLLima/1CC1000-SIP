import numpy as np

l = [0, 1, 2, 3, 4, 5]
print("Id of l  : ", id(l))
l[:3] = [2, 1, 0]
print("l :  ", l)
 
l2 = l[:4]
print("Id of l2 : ", id(l2))  #Two python objects with the same id are physically the same
l2[:] = [0, 0, 0, 0]          #Warning do not confuse with "l2 = [0, 0, 0]" which is used to change the reference l2
print("Id of l2 : ", id(l2))
 
print("l :  ", l)
print("l2 : ", l2)

L = np.array([0, 1, 2, 3, 4, 5])
print("Id of L  : ", id(L))
L[:3] = [2, 1, 0]
print("L :  ", L)
 
L2 = L[:4]
print("Id of L2 : ", id(L2))  #Two python objects with the same id are physically the same
L2[:] = [0, 0, 0, 0]          #Warning do not confuse with "L2 = [0, 0, 0]" which is used  to change reference L2
print("Id of L2 : ", id(L2))
 
print("L :  ", L)
print("L2 : ", L2)

print("Base of L :  ", L.base)
print("Base of L2 : ", L2.base)
 
print("Id of L : ", id(L))
print("Id of the base of L2 : ", id(L2.base))

L3 = np.reshape(L2, (2, 2))
L3[1, 0] = 9
print("L3 :\n", L3)
print("L :\n", L)

A = np.ones((3, 4))
print("Array A :\n", A)
 
A[::2, :] = 2
print("Array A: modified with a scalar\n", A)
 
B = np.zeros((3, 4))
A[:,:] = B[:,:]
print("Array A: modified with a view\n", A)
