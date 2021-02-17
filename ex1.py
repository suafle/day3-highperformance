import numpy as np

#Ex a
null = np.zeros(10)
null[4] = 1

print('\n')
print('Output exercise 1a')
print(null)
print('\n')

#Ex b
vector = np.arange(10,50)

print('Output exercise 1b')
print(vector)
print('\n')

#Ex c
#Priting null and vector reverted
print('Output exercise 1c')
print(null[::-1])
print(vector[::-1])
print('\n')

#Ex d
mat = np.arange(0,9).reshape(3,3)
print('Output exercise 1d')
print(mat)
print('\n')

#Ex e
array = np.array([1,2,0,0,4,0])
#loc = array!=0 #this gives an array of booleans
loc = np.where(array!=0)
print('Output exercise 1e')
print(loc[0])
print('\n')

#Ex f
rand = np.random.random(30)
mean = np.mean(rand)
print('Output exercise 1f')
print(rand)
print('Mean = ',mean)
print('\n')

#Ex g
