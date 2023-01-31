import numpy as np

#Iván
def array1 ():
    a = np.array([88, 23, 39, 41])
    return a

def array2 ():
    b = np.array([[76.4, 21.7, 38.4], [41.2, 52.8, 68.9]])
    return b

def array3 ():
    c = np.array([[12],[4],[9],[8]])
    c.reshape(-1,1)
    return c

print (array1())
print (array2())
print (array3())