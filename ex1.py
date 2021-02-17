import numpy as np

#Ex a
null = np.zeros(10)
null[4] = 1

print(null)

#Ex b
vector = np.arange(10,50)

print(vector)

#Ex c
#Priting null and vector reverted
print(null[::-1])
print(vector[::-1])

#Ex d
mat = np.arange(0,9).reshape(3,3)
print(mat)

#Ex e
array = np.array([1,2,0,0,4,0])
#loc = array!=0 #this gives an array of booleans
loc = np.where(array!=0)
print(loc[0])
