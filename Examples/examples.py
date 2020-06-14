from vectorObject.DefinedVectors import Vector3D, Vector2D
import math
import operator as op
## todo need to show how to modify based on a single vector
## todo need to show how to make your own vector based on the exisitenly logic of the master class via inheritance
# todo: IN custom, allow for individual to override a module via isinstance but then default to the standard
#  process if all other instances

a = Vector3D(4.5, 3.2, 5.6)
b = Vector3D(3, 5, 10)

print(a)
a + b
print(a)

a + 5
print(a)

print("tuple")
a + (1, 3, 5)
print(a)

print("now testing master class")
print(a)
print(b)

print("start")
a - b
print(a)

a - 5
print(a)

a - [3, 4, 5]
print(a)


e = -a
print(a)

for ee in a:
    print(ee)

print("Dot")
print(a)
print(b)
a.dot_product(b)

print("Cross")
a.cross_product(b)
print(a)

print("Norm")
a.normalise()
print(a)

print("EQ")
print(a != b)

print("2d")
f = Vector2D(5, 4)

print(f)
f.normalise()
print(f)