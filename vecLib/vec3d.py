from .vec import Vec
from collections.abc import Iterable
import math as m

class Vec3d(Vec):
    def __init__(self, x_or_triple=None, y=None, z=None):
        if y is None and z is None:
            if issubclass(type(x_or_triple), Iterable):
                if len(x_or_triple) == 3:
                    if all([issubclass(type(i, (int, float, complex))) for i in x_or_triple]):
                        super().__init__(*x_or_triple)
                        self.x, self.y, self.z = x_or_triple
                    else:
                        raise TypeError("x_or_triple need to contain olny int, float, or complex number")
                else:
                    raise TypeError(f"x_or_triple need to have 2 dim not {len(x_or_triple)}")
            elif x_or_triple is None:
                super().__init__(0, 0, 0)
                self.x, self.y, self.z = 0, 0, 0
            else:
                raise TypeError(f"if y=None and z=None so x_or_triple need to be an Iterable or None not {type(x_or_triple)}")
        else:
            if issubclass(type(x_or_triple), (int, float, complex)):
                if issubclass(type(y), (int, float, complex)):
                    if issubclass(type(z), (int, float, complex)):                       
                        super().__init__(x_or_triple, y, z)
                        self.x, self.y, self.z = x_or_triple, y, z
                    else:
                        raise TypeError(f"z must be None, int, float or complex type not {type(z)}")
                else:
                    raise TypeError(f"y must be None, int, float or complex type not {type(y)}")
            else:
                raise TypeError(f"x_or_triple must be int, float, complex type not {type(x_or_triple)}")
    
    def __repr__(self):
        return f"Vec3d: {[self[0], self[1], self[2]]}"
        
    def __setattr__(self, name, value):
        if name == "_protection":
            if type(value) == bool:
                return super().__setattr__(name, value)
            else:
                raise TypeError("_protection must be boolean")
        elif not self._protection:
            return super().__setattr__(name, value)
        elif name == "value":
            if issubclass(type(value), Iterable):
                if len(value) == self._dim:
                    return super().__setattr__(name, list(value))
                else:
                    raise TypeError(f"Value must have {self._dim} dimension: len(value)={len(value)}")
            else:
                raise TypeError(f"Value must be an iterable object: type(value)={type(value)}")
        elif name == "x":
            self[0] = value
        elif name == "y":
            self[1] = value
        elif name == "z":
            self[2] = value
        else:
            raise AttributeError(f"Cannot set {name} attribute")
    
    def rotate(self, alpha, axis):
        if issubclass(type(alpha), (int, float)):
            if issubclass(type(axis), (Vec, Vec3d)):
                if axis._dim == self._dim:
                    u = axis.normalize()
                    c, s = m.cos(alpha), m.sin(alpha)

                    d1 = Vec3d((c + u.x * u.x * (1-c)), (u.x * u.y * (1-c) - u.z * s), (u.x * u.z * (1-c) + u.y * s))
                    d2 = Vec3d((u.y * u.x * (1-c) + u.z * s), (c + u.y * u.y * (1-c)), (u.y * u.z * (1-c) - u.x * s))
                    d3 = Vec3d((u.z * u.x * (1-c) - u.y * s), (u.z * u.y * (1-c) + u.x * s), (c + u.z * u.z * (1-c)))

                    return Vec3d(d1.dot(self), d2.dot(self), d3.dot(self))
                else:
                    raise TypeError(f"axis must have the same dimension as the vector 3!={axis._dim}")
            else:
                raise TypeError(f"axis must be Vec or Vec3d type not {type(axis)}")
        else:
            raise TypeError(f"alpha must be int or float type not {type(alpha)}")
        
    def cross(self, vec):
        if issubclass(type(vec), (Vec, Vec3d)):
            if self._dim == vec._dim:
                return Vec3d(self.y*vec.z - self.z*vec.y, self.z*vec.x - self.x*vec.z, self.x*vec.y - self.y*vec.x)
            else:
                raise TypeError(f"vec must have 3 dimensions not {vec._dim}")
        else:
            raise TypeError(f"vec must be Vec or Vec3d type not {type(vec)}")
        
    @classmethod
    def zeros(cls):
        return Vec3d(0., 0., 0.)
    
    @classmethod
    def ones(cls):
        return Vec3d(1., 1., 1.)