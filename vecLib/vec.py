from collections.abc import Iterable
import math as m

class Vec(object):
    def __init__(self, *args):
        if not all(map(lambda x: type(x) in (int, float, complex), args)):
            raise TypeError("Arguments must be int, float or complex")
        if len(args) == 0:
            raise TypeError("Vector must have less 1 dimension")
        
        self._protection = False
        self._dim = len(args)
        self.value = list(args)
        self._protection = True
    
    def __repr__(self):
        return f"Vec {self._dim}d: [{' '.join(map(str, self.value))}]"
    
    def __str__(self):
        return self.__repr__()
    
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
        else:
            raise AttributeError(f"Cannot set {name} attribute")
    
    def __delattr__(self, name):
        raise AttributeError(f"Cannot delete {name} attribute")
    
    def __getitem__(self, index):
        if type(index) == int:
            if -self._dim <= index < self._dim:
                return self.value[index]
            else:
                raise IndexError("Vector index out of range")
        else:
            raise TypeError("Index must be int type")
    
    def __setitem__(self, index, value):
        if type(index) == int:
            if -self._dim <= index < self._dim:
                self.value[index] = value
            else:
                raise IndexError("Vector index out of range")
        else:
            raise TypeError("Index must be int type")
    
    def __contains__(self, value):
        return value in self.value
    
    def __len__(self):
        return self._dim
    
    def __iadd__(self, value):
        if issubclass(type(value), (int, float, complex, Iterable)):
            if isinstance(value, (int, float, complex)):
                for i in range(self._dim):
                    self.value[i] += value
            elif len(value) == self._dim:
                for i in range(self._dim):
                    self.value[i] += value[i]
            else:
                raise IndexError(f"Value must have the same dimension of the Vec: len(value)={len(value)}")
        else:
            raise TypeError(f"Value must be int, float, complex or Iterable: type(value)={type(value)}")
        return self
    
    def __isub__(self, value):
        if issubclass(type(value), (int, float, complex, Iterable)):
            if isinstance(value, (int, float, complex)):
                for i in range(self._dim):
                    self.value[i] -= value
            elif len(value) == self._dim:
                for i in range(self._dim):
                    self.value[i] -= value[i]
            else:
                raise IndexError(f"Value must have the same dimension of the Vec: len(value)={len(value)}")
        else:
            raise TypeError(f"Value must be int, float, complex or Iterable: type(value)={type(value)}")
        return self
        
    def __imul__(self, value):
        if issubclass(type(value), (int, float, complex, Iterable)):
            if isinstance(value, (int, float, complex)):
                for i in range(self._dim):
                    self.value[i] *= value
            elif len(value) == self._dim:
                for i in range(self._dim):
                    self.value[i] *= value[i]
            else:
                raise IndexError(f"Value must have the same dimension of the Vec: len(value)={len(value)}")
        else:
            raise TypeError(f"Value must be int, float, complex or Iterable: type(value)={type(value)}")
        return self
    
    def __itruediv__(self, value):
        if issubclass(type(value), (int, float, complex, Iterable)):
            if isinstance(value, (int, float, complex)):
                for i in range(self._dim):
                    self.value[i] /= value
            elif len(value) == self._dim:
                for i in range(self._dim):
                    self.value[i] /= value[i]
            else:
                raise IndexError(f"Value must have the same dimension of the Vec: len(value)={len(value)}")
        else:
            raise TypeError(f"Value must be int, float, complex or Iterable: type(value)={type(value)}")
        return self
    
    def __ifloordiv__(self, value):
        if issubclass(type(value), (int, float, complex, Iterable)):
            if isinstance(value, (int, float, complex)):
                for i in range(self._dim):
                    self.value[i] //= value
            elif len(value) == self._dim:
                for i in range(self._dim):
                    self.value[i] //= value[i]
            else:
                raise IndexError(f"Value must have the same dimension of the Vec: len(value)={len(value)}")
        else:
            raise TypeError(f"Value must be int, float, complex or Iterable: type(value)={type(value)}")
        return self
    
    def __imod__(self, value):
        if issubclass(type(value), (int, float, complex, Iterable)):
            if isinstance(value, (int, float, complex)):
                for i in range(self._dim):
                    self.value[i] %= value
            elif len(value) == self._dim:
                for i in range(self._dim):
                    self.value[i] %= value[i]
            else:
                raise IndexError(f"Value must have the same dimension of the Vec: len(value)={len(value)}")
        else:
            raise TypeError(f"Value must be int, float, complex or Iterable: type(value)={type(value)}")
        return self
    
    def __ipow__(self, value):
        if issubclass(type(value), (int, float, complex, Iterable)):
            if isinstance(value, (int, float, complex)):
                for i in range(self._dim):
                    self.value[i] **= value
            elif len(value) == self._dim:
                for i in range(self._dim):
                    self.value[i] **= value[i]
            else:
                raise IndexError(f"Value must have the same dimension of the Vec: len(value)={len(value)}")
        else:
            raise TypeError(f"Value must be int, float, complex or Iterable: type(value)={type(value)}")
        return self
    
    def __add__(self, value):
        copy = self.copy()
        copy += value
        return copy
    
    def __sub__(self, value):
        copy = self.copy()
        copy -= value
        return copy
    
    def __mul__(self, value):
        copy = self.copy()
        copy *= value
        return copy
    
    def __truediv__(self, value):
        copy = self.copy()
        copy /= value
        return copy
    
    def __floordiv__(self, value):
        copy = self.copy()
        copy //= value
        return copy
    
    def __mod__(self, value):
        copy = self.copy()
        copy %= value
        return copy
    
    def __pow__(self, value):
        copy = self.copy()
        copy **= value
        return copy
    
    def __radd__(self, value):
        copy = self.copy()
        copy += value
        return copy
    
    def __rsub__(self, value):
        copy = self.copy()
        copy -= value
        return copy
    
    def __rmul__(self, value):
        copy = self.copy()
        copy *= value
        return copy
    
    def __rtruediv__(self, value):
        copy = self.copy()
        copy /= value
        return copy
    
    def __rfloordiv__(self, value):
        copy = self.copy()
        copy //= value
        return copy
    
    def __rmod__(self, value):
        copy = self.copy()
        copy %= value
        return copy
    
    def __rpow__(self, value):
        copy = self.copy()
        copy **= value
        return copy
    
    def __eq__(self, value):
        if issubclass(type(value), (Iterable, Vec)):
            return list(self) == list(value)
        return False
    
    def __ne__(self, value):
        if issubclass(type(value), (Iterable, Vec)):
            return list(self) != list(value)
        return False
    
    def __iter__(self):
        return iter(self.value)
    
    def __neg__(self):
        return type(self)(*map(lambda x: -x, self.value))
    
    def __pos__(self):
        return self.copy()
    
    def __abs__(self):
        return type(self)(*map(lambda x: abs(x), self.value))
    
    def __invert__(self):
        raise TypeError(f"bad operand type for unary ~: 'Vec'")
    
    def __bool__(self):
        return True if sum(abs(self)) != 0 else False
    
    def __int__(self):
        raise TypeError("int() argument must be a string, a bytes-like object or a number, not 'Vec'")
    
    def __float__(self):
        raise TypeError("float() argument must be a string or a number, not 'Vec'")
    
    def __round__(self, n=None):
        return type(self)(*map(lambda x: round(x, n), self.value))
    
    def __ceil__(self):
        return type(self)(*map(m.ceil, self.value))
    
    def __floor__(self):
        return type(self)(*map(m.floor, self.value))
    
    def __trunc__(self):
        return type(self)(*map(m.trunc, self.value))
    
    def __getstate__(self):
        return self.__dict__.copy()
        
    def __setstate__(self, state):
        self.__dict__.update(state)
    
    def __copy__(self):
        return type(self)(*self.value)
    
    def __deepcopy__(self):
        return type(self)(*self.value)
    
    def copy(self):
        return self.__copy__()
    
    def dot(self, vec):
        if issubclass(type(vec), Vec):
            if self._dim == vec._dim:
                return sum([i*j for i, j in zip(self, vec)])
            else:
                raise TypeError(f"Vectors must have the same dimension: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or subclass of Vec class")
        
    def norm2(self):
        return sum([i**2 for i in self])
    
    def norm(self):
        return m.sqrt(sum([i**2 for i in self]))
    
    def dist2(self, vec):
        if issubclass(type(vec), Vec):
            if self._dim == vec._dim:
                return (self - vec)**2
            else:
                raise TypeError(f"Vectors must have the same dimension: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or subclass of Vec class")
    
    def dist(self, vec):
        if issubclass(type(vec), Vec):
            if self._dim == vec._dim:
                return m.sqrt(sum((self - vec)**2))
            else:
                raise TypeError(f"Vectors must have the same dimension: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or object subclass of Vec class")
        
    def normalize(self):
        return self / self.norm()
        
    def project_on(self, vec):
        if issubclass(vec, Vec):
            if self._dim == vec._dim:
                s = self.dot(vec) / vec.norm()
                return self * s
            else:
                raise TypeError(f"Vectors must have the same dimension: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or object subclass of Vec class")
        
    def project_on_plane(self, plane):
        if issubclass(plane, Vec):
            if self._dim == plane._dim:
                s = self.dot(plane) * plane / plane.norm2()
                return self - s
            else:
                raise TypeError(f"Vectors must have the same dimension: {self._dim}!={plane._dim}")
        else:
            raise TypeError("vec must be Vec type or object subclass of Vec class")
        
    def project_from(self, vec):
        if issubclass(vec, Vec):
            if self._dim == vec._dim:
                s = vec.norm2() / self.dot(vec)
                return self * s
            else:
                raise TypeError(f"Vectors must have the same dimension: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or object subclass of Vec class")
        
    def mirror_on(self, vec):
        if issubclass(vec, Vec):
            if self._dim == vec._dim:
                s = 2 * self.dot(vec) / vec.norm2()
                return self * s
            else:
                raise TypeError(f"Vectors must have the same dimension: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or object subclass of Vec class")
    
    def rotate(self, alpha, axis):
        raise NotImplementedError()
        
    def cross(self, vec):
        raise NotImplementedError()