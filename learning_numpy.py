# from data import*
import numpy as np



# a = np.array([1,2.0,3], dtype=complex)

# b = np.array([[1.0,2.0,2.0], [3.0,4.0,2.0], [3.0,4.0,2.0]])

# print(a)
# print(b)

# #Prints the type of the array
# print(type(b))

# #Prints the data type of the array
# print(b.dtype)

# #Prints the axes of the array
# print(b.ndim)

# #Print the number of elements in the array
# print(b.size)

# #Prints dimension of the array
# print(b.shape)

# print("  ")
# #Produces an array field with zeros
# empt = np.zeros((3,3))
# print(empt)

# print("  ")
# #Produces an array field with ones
# ones = np.ones((3,3))
# print(ones)

# print("  ")
# #Creates one dimensional array between the defined range
# g = np.arange(0,12)
# print(g)

# print("  ")
# #Create an array of elements divisible by the third argument
# t = np.arange(0, 12, 3)
# print(t)

# print("  ")
# #It reshapes a prexisting array
# p = g.reshape(3, 4)
# print(p)

# print("  ")
# #Concept not really clear
# l = np.linspace(0, 10, 5)
# print(l)

# print("  ")
# # It Creates an array and fields it with random values
# r = np.random.random((3,3))
# print(r)


# # Mathematical operations
# print(" ")
# print(g)
# print("  ")
# print(g+4, g*2)


# a = np.array([1,2,3])
# print(a.shape)
# print(a.ndim)

# # Accessing the numpy array

# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# a = 1
# print(a)
# print("  ")
# print("The shape: ",a.shape)

# # To print specific data [r, c]
# print("  ")
# print(a[1,5])
# # To print a specific row  
# print(a[1, :])

# print(a[0, 2:6])

# Structured Arrays

Structured = np.array([(1, 'First', 0.5), (2, 'Second', 0.9)], dtype=('i2, a6, f4'))

# Reading and writing data in files
# Writing to a file
np.save("data", Structured)

data = np.load('data.npy')
print(data)

