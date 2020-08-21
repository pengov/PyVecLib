from .vec import Vec
from collections.abc import Iterable
import math as m

class Vec2d(Vec):
    def __init__(self, x_or_pair=None, y=None):
        if y is None:
            if issubclass(type(x_or_pair), Iterable):
                if len(x_or_pair) == 2:
                    if all([issubclass(type(i, (int, float, complex))) for i in x_or_pair]):
                        super().__init__(*x_or_pair)
                        self.x, self.y = x_or_pair
                    else:
                        raise TypeError("x_or_pair need to contain olny int, float, or complex number")
                else:
                    raise TypeError(f"x_or_pair need to have 2 dim not {len(x_or_pair)}")
            elif x is None:
                super().__init__(0, 0)
                self.x, self.y = 0, 0
            else:
                raise TypeError(f"if y=None so x_or_pair need to be an Iterable not {type(x_or_pair)}")
        else:
            if issubclass(type(x_or_pair), (int, float, complex)):
                if issubclass(type(y), (int, float, complex)):
                    super().__init__(x_or_pair, y)
                    self.x, self.y = x_or_pair, y
                else:
                    raise TypeError(f"y must be None, int, float or complex type not {type(y)}")
            else:
                raise TypeError(f"x_or_pair must be int, float, complex type not {type(x_or_pair)}")
    
    def __repr__(self):
        return f"Vec2d: {[self[0], self[1]]}"
        
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
        else:
            raise AttributeError(f"Cannot set {name} attribute")
    
    def rotate(self, alpha):
        if issubclass(alpha, (int, float)):
            c, s = m.cos(alpha), m.sin(alpha)
            return Vec2d(c * self.x - s * self.y, s * self.x + c * self.y)
        else:
            raise TypeError(f"alpha must be int or float type not {type(alpha)}")
        
    def cross(self, vec):
        if issubclass(type(vec), (Vec, Vec2d)):
            if self._dim == vec._dim:
                return self.x * vec.y - self.y * vec.x
            else:
                raise TypeError(f"vec must have 2 dimensions not {vec._dim}")
        else:
            raise TypeError(f"vec must be Vec or Vec2d type not {type(vec)}")
    