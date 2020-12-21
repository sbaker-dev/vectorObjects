from vectorObjects.DefinedVectors import Vector2D, Vector3D, VectorRGB
from vectorObjects.VectorMaster import VectorMaster
import operator
from random import randint


example_vector = Vector3D(4.5, 3.2, 5.6)
tuple_vector = Vector3D((3, 5, 10), ex=True)
list_vector = Vector3D([5, 2, 5], ex=True)

example_vector + tuple_vector
print(f"Vector3D after addition of b array: {example_vector}\n")

example_vector + 5
print(f"Vector3D after constant addition: {example_vector}\n")

dot_product = example_vector.dot_product(tuple_vector)
print(f"Dot product of a and b: {dot_product}\n")

list_vector.normalise()
print(f"Vector3D after normalisation: {list_vector}\n")

example_vector.cross_product(tuple_vector)
print(f"Vector3D after cross product: {example_vector}\n")


# Custom Vector based with VectorMaster inheritance
class Vector5D(VectorMaster):
    __slots__ = ["a", "b", "c", "d", "e"]

    def __init__(self, *args):
        super().__init__()
        # Load via inherited self._load so that your custom vector can load all valid int float combinations
        self.a, self.b, self.c, self.d, self.e = self._load(args)

    # Basic dunder have there vector information set within VectorMaster so they can just inherit it
    def __sub__(self, other):
        self._mathematical_operator(self, other, operator.sub)

    # If you want the majority of the information in VectorMaster or want to add new options based on a different type
    # you can add or change that functionality via isinstance
    # by isinstance
    def __add__(self, other):
        if isinstance(other, type(self)):
            print("Do some custom code here")
        else:
            self._mathematical_operator(self, other, operator.add)


width = 3
height = 3

# This shows a random row
for i in range(width):
    print(VectorRGB(randint(0, 255), randint(0, 255), randint(0, 255)))

# This is our matrix of our 10 by 10 image
matrix = [[VectorRGB(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(width)] for _ in range(height)]
print(matrix)

# For 2D vectors we can also subdivide
point1 = Vector2D(5, 10)
point2 = Vector2D(10, 20)
print(f"Sub divided points is {point1.sub_divide(point2, 4)}")
