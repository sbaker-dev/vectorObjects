# vectorObjects
#### Object approach to common dimensional vectors 

This project was create by converting and extending a small section of code within the now archived [pymeshio][pymesh], 
relating to Vectors and 3D object rotation matrices which have been extracted and generalised where possible. This was 
due to some of these objects also having the potential to be used outside of this specific use case.
 
vectorObjects also has the ability to allow you to create your own vectors, not pre defined within vectorObjects, 
quickly via inheritance from a master class of methods. All source code is available on the project [github page][pro]

## Getting Started 
vectorObjects is available as a package via Pypi so you can pip install by the following command

```shell script
python -m pip install vectorObjects
```

# Basic example
Pre definied vectors can be imported via vectorObject.DefinedVectors. In this example we are using Vector3D. You can
define a new Vector3D by assigning its x, y, and z values individually, as a tuple or a list. Defined Vectors have most
dunder methods set via VectorMaster which they inherit. So the result of adding another instance of Vector 3D is 
different that adding a constant. Most Vectors also have some custom methods. Some of these like dot_product return a 
value whilst others update the instance of the Vector like normalise

```python
from vectorObjects.DefinedVectors import Vector3D

example_vector = Vector3D(4.5, 3.2, 5.6)
tuple_vector = Vector3D((3, 5, 10))
list_vector = Vector3D([5, 2, 5])

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
```

It is also possible via inheritance to make your own custom vector array with most of the dunders sorted via 
inheritance. Just set each variable in Slots, and then have the class attributes be loaded via the inherited self._load.
The self._load, and most of the dunder methods, can be inherited from VectorMaster, so if you just define a dunder, like
sub, you can then inherit the logic from VectorMaster. To apply a certain mathematical operator you need to user the
operator library. Make sure to pass the operator.type rather than the call otherwise it will not work; for example pass
operator.sub not operator.sub().

```python
from vectorObjects.VectorMaster import VectorMaster
import operator

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
```

You can also then use these vectors to create a matrix. For example, rgb values are a vector that exists in a 
width*height matrix that cane be constructed in python via nested lists.

```python

from vectorObjects.DefinedVectors import VectorRGB
from random import randint

width = 3
height = 3

# This shows a random row
for i in range(width):
    print(VectorRGB(randint(0, 255), randint(0, 255), randint(0, 255)))

# This is our matrix of our 10 by 10 image
matrix = [[VectorRGB(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(width)] for _ in range(height)]
print(matrix)
```

This should give you access to some of the common vectors via the Defined Vectors, and if you need something custom and
you find the logic within VectorMaster to be of use then you can create your own vectors quickly. All the code from this
example can be found in the [Examples folder][docpath] on github.


## License
Distributed under the MIT License. See `LICENSE` for more information.


[mmd]: https://github.com/sbaker-dev/mmdParser
[pymesh]: https://github.com/ousttrue/pymeshio
[docpath]: https://github.com/sbaker-dev/vectorObjects/Examples
[pro]: https://github.com/sbaker-dev/vectorObjects




