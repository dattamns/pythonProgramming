##################################################
# Core Python : Python Data Structures - Lists 
# Author : Shreekanta Datta
# GitHub : https://github.com/dattamns/pythonProgramming
##################################################

#########################################################################################################
# Decription: This python files demonstrates the concept of Lists in Python and its programming constructs
##########################################################################################################


#Basic constructs

print("Example1: Homogeneous list -> Collection of similar data types")
l1 = [10, 20, 30, 40, 50]
print(l1)
print()

print("Example2: Heterogenous list -> Collection of disimilar data types")
l2 = [10, 3.412, 'MNSDatta']
print(l2)
print()

print("Accessing/Iterating the elements of a List")
for i in l2:
    print(i)
print()

print("Creating an Empty-List")
l3 = []
print(l3)
print()

print("Copying one list to another")
l3 = l2
print(l3)
print()

print("Adding elements into an empty list")
l4 = []
for i in range(1,10):
    l4.append(i)
print(l4)
print()

print("Forward Indexing in List")
pos = 0
for i in l4:
    print(l4[pos]);
    pos = pos+1
print()

print("Reverse Indexing in List")
index=-1
for i in l4:
    print(l4[index])
    index = index-1
print()











