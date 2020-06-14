from vectorObjects.DefinedVectors import Vector3D
from vectorObjects.VectorMaster import VectorMaster
import operator


example_vector = Vector3D(4.5, 3.2, 5.6)
new_vector = Vector3D(3, 5, 10)

example_vector + new_vector
print(f"Vector3D after addition of b array: {example_vector}\n")

example_vector + 5
print(f"Vector3D after constant addition: {example_vector}\n")

dot_product = example_vector.dot_product(new_vector)
print(f"Dot product of a and b: {dot_product}\n")

example_vector.normalise()
print(f"Vector3D after normalisation: {example_vector}\n")


# Custom Vector based with VectorMaster inheritance
class Vector5D(VectorMaster):
    __slots__ = ["a", "b", "c", "d", "e"]

    def __init__(self, a, b, c, d, e):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

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




