# vectorObjects
#### Object approach to common dimensional vectors 

As part of the [mmdParser][mmd] project of converting and extending the now archived [pymeshio][pymesh], a set of common
functions programmed as part of the pymeshio relating to Vectors and 3D object rotation matrices where extracted, and 
then generalised where possible. This was due to some of these objects also having the potential to be used outside of
this specific use case.
 
vectorObjects also has the ability to allow you to create your own vectors, not pre defined within vectorObjects, 
quickly via inheritance from a master class of methods. All source code is available on the project [github page][pro]

## Getting Started 
vectorObjects is available as a package via Pypi so you can pip install by the following command

```shell script
python -m pip install vectorObjects
```

# Basic example
Pre definied vectors can be imported via vectorObject.DefinedVectors. In this example we are using Vector3D. You can
define a new Vector3D by assigning its x, y, and z values. Definded Vectors have most dunder methods set via 
VectorMaster which they inherit from with custom typeing. So the result of adding another instance of Vector 3D is 
different that adding a constant. Most Vectors also have some custom methods. Some of these like dot_product return a 
value whilst others update the instance of the Vector like normalise

```python
from vectorObject.DefinedVectors import Vector3D

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
```

It is also possible via inheritance to make your own custom vector away with most of the dunders isinstance typing 
sorted via inheritance. In this case we have an example 5D vector class called Vector5D which inherits VectorMaster.
You can then just define a dunder, like sub and inherit the logic from VectorMaster. To apply a certain mathematical
operator you need to user the operator library. Make sure to pass the operator.type rather than the call otherwise it
will not work. For example pass operator.sub not operator.sub().

```python
from vectorObject.VectorMaster import VectorMaster
import operator

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




