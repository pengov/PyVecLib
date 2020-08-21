from collections.abc import Iterable
import math as m

class Vec(object):
    """A class to represent multidimensional Vector

    Attributes
    ----------
    _protection : bool
        if True block the write access to method and non writables attributes
    _dim : int
        dimension of the vector
        non writable attribute
    value : list
        value of the vector
        
    Methods
    ----------
    copy() : Vec
        return a copy of the vector
    get_dim() : int
        return the dimension of the vector
    dot(vec:Vec) : float
        return the dot product of self and vec
    norm2() : float
        return the vector norm squared
    norm() : float
        return the vector norm
    dist2(vec:Vec) : float
        return the squared distance beetween self and vec
    dist(vec:Vec) : 
        return the distance beetween self and vec
    normalize() : Vec
        return the normalized vector
    project_on(vec:Vec) : Vec
        return the vector projection on vec
    project_on_plane(plane:Vec) : Vec
        return the vector projection on the plane
    project_from(vec:Vec) : Vec
        return the inverse projection from vec
    rotate(alpha:float, axis:Vec) : Vec
        implemented only in Vec2d and Vec3d
    cross(vec:Vec) : Vec
        implemented only in Vec2d and Vec3d
    """
    
    def __init__(self, *args):
        """Object initialization for Vec class 

        Args:
            *args (list): liste of int, float or complex number who compose the vector
        
        Raises:
            TypeError: all arguments must be int, float or complex
            TypeError: vector must have less 1 dimension so the class need less 1 argument
        """
        
        if not all(map(lambda x: type(x) in (int, float, complex), args)):
            raise TypeError("Arguments must be int, float or complex")
        if len(args) == 0:
            raise TypeError("Vector must have less 1 dimension")
        
        self._protection = False
        self._dim = len(args)
        self.value = list(args)
        self._protection = True
    
    def __repr__(self):
        """Return the canonical string representation of the vector.
        repr(self) == str(self)

        Returns:
            str: vector representation
        """
        
        return f"Vec {self._dim}d: [{' '.join(map(str, self.value))}]"
    
    def __str__(self):
        """Create a new string object from the vector
        repr(self) == str(self)

        Returns:
            str: string representation of the vector
        """
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
        elif hasattr(self, name):
            raise AttributeError(f"attribute '{name}' of 'vecLib.Vec' objects is not writable")
        else:
            raise AttributeError(f"'vecLib.Vec' object has no attribute '{name}'")
    
    def __delattr__(self, name):
        raise AttributeError(f"Cannot delete {name} attribute")
    
    def __getitem__(self, index):
        """same as vec.value[index]

        Args:
            index (int): vector's value index

        Raises:
            IndexError: vector index out of range
            TypeError: index must be int

        Returns:
            (int, float or complex): vector's value on this index
        """
        if type(index) == int:
            if -self._dim <= index < self._dim:
                return self.value[index]
            else:
                raise IndexError("Vector index out of range")
        else:
            raise TypeError("Index must be int type")
    
    def __setitem__(self, index, value):
        """same as vec.value[index] = value

        Args:
            index (int): vector's value index
            value (int, float or complex): new vector's value on this index

        Raises:
            IndexError: index out of range
            TypeError: value must be int, float or complex
            TypeError: index must be int
        """
        if type(index) == int:
            if issubclass(type(value), (int, float, complex)):
                if -self._dim <= index < self._dim:
                    self.value[index] = value
                else:
                    raise IndexError("Vector index out of range")
            else:
                raise TypeError("value must be int, float or complex")
        else:
            raise TypeError("Index must be int type")
    
    def __contains__(self, value):
        return value in self.value
    
    def __len__(self):
        """vector's dimension

        Returns:
            int: vectr's dimension
        """
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
        """return a vector's copy

        Returns:
            Vec: vector's value
        """
        
        return self.__copy__()
    
    def get_dim(self):
        """return the vector's dimensions
        same as len(vec)

        Returns:
            int: vector's dimensions
        """
        return self._dim
    
    def dot(self, vec):
        """do the dot product beetween self and vec

        Args:
            vec (Vec): second vector

        Raises:
            TypeError: vectors must have the same dimensions
            TypeError: vec must be Vec type or subclass of Vec class

        Returns:
            (int, float or complex): dot product beetweenself and vec
        """
        
        if issubclass(type(vec), Vec):
            if self._dim == vec._dim:
                return sum([i*j for i, j in zip(self, vec)])
            else:
                raise TypeError(f"Vectors must have the same dimension: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or subclass of Vec class")
        
    def norm2(self):
        """squarred vector's norm
        faster than get classic vectr's norm

        Returns:
            (int, float or complex): squarred vector's norm
        """
        
        return sum([i**2 for i in self])
    
    def norm(self):
        """get the vector's norm

        Returns:
            (int, float or complex): return the vector's norm
        """
        return m.sqrt(sum([i**2 for i in self]))
    
    def dist2(self, vec):
        """get the squarred distance beetween self and vec

        Args:
            vec (Vec): second vector

        Raises:
            TypeError: vectors must have the same dimension
            TypeError: vec must be Vec type or subclass of Vec class

        Returns:
            (int, float or complex): squarred distance beetween self and vec
        """
        
        if issubclass(type(vec), Vec):
            if self._dim == vec._dim:
                return sum((self - vec)**2)
            else:
                raise TypeError(f"Vectors must have the same dimensions: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or subclass of Vec class")
    
    def dist(self, vec):
        """get the distance beetween self and vec

        Args:
            vec (Vec): second vector

        Raises:
            TypeError: vectors must have the same dimensions
            TypeError: vec must be Vec type or subclass or Vec class

        Returns:
            (int, float or complex): distance beetween self and vec
        """
        
        if issubclass(type(vec), Vec):
            if self._dim == vec._dim:
                return m.sqrt(sum((self - vec)**2))
            else:
                raise TypeError(f"Vectors must have the same dimensions: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or subclass of Vec class")
        
    def normalize(self):
        """normalize the vector

        Returns:
            Vec: vector normalized
        """
        
        return self / self.norm()
        
    def project_on(self, vec):
        """project self on a vector

        Args:
            vec (Vec): second vector

        Raises:
            TypeError: vectors must have the same dimensions
            TypeError: vec must be Vec type or subclass of Vec class

        Returns:
            Vec: vector projected
        """
        
        if issubclass(vec, Vec):
            if self._dim == vec._dim:
                s = self.dot(vec) / vec.norm()
                return self * s
            else:
                raise TypeError(f"Vectors must have the same dimensions: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or subclass of Vec class")
        
    def project_on_plane(self, plane):
        """project self on a plane

        Args:
            plane (Vec): plane where the vector will be projected

        Raises:
            TypeError: the plane and self must have the same dimensions
            TypeError: plane must be Vec type or subclass of Vec class

        Returns:
            (Vec): vector projected
        """
        
        if issubclass(plane, Vec):
            if self._dim == plane._dim:
                s = self.dot(plane) * plane / plane.norm2()
                return self - s
            else:
                raise TypeError(f"The plane and self must have the same dimensions: {self._dim}!={plane._dim}")
        else:
            raise TypeError("plane must be Vec type or subclass of Vec class")
        
    def project_from(self, vec):
        """do the reverse projection

        Args:
            vec (Vec): second vector

        Raises:
            TypeError: vectors must have the asme dimensions
            TypeError: vec must be Vec type or subclass of Vec class

        Returns:
            Vec: vector's reverse projection
        """
        
        if issubclass(vec, Vec):
            if self._dim == vec._dim:
                s = vec.norm2() / self.dot(vec)
                return self * s
            else:
                raise TypeError(f"Vectors must have the same dimensions: {self._dim}!={vec._dim}")
        else:
            raise TypeError("vec must be Vec type or subclass of Vec class")
    
    def rotate(self, alpha, axis):
        """applied a roation on the vector
        Not implemented

        Args:
            alpha (float): angle in radians
            axis (Vec): vector how defined the axis of the rotation

        Raises:
            NotImplementedError: rotate is not implemented in Vec
        """
        
        raise NotImplementedError("rotate is not implemented in Vec")
        
    def cross(self, vec):
        """do the cross operation beetween self and vec

        Args:
            vec (Vec): second vector

        Raises:
            NotImplementedError: cross is not implemented in Vec
        """
        raise NotImplementedError("cross is not implemented in Vec")