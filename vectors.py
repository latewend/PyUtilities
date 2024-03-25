#simple vectors classes 
class vec2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


    def  __eq__(self, other):
        return self.x == other.x and self.y == other.x
    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return vec2(self.x * other, self.y * other)
    def __truediv__(self, other):
        return vec2(self.x.__truediv__(other), self.y.__truediv__(other))
    def __floordiv__(self, other):
        return vec2(self.x.__floordiv__(other), self.y.__floordiv__(other))
    def __mod__(self, other):
        return vec2(self.x % other, self.y % other)
    def __neg__(self):
        return vec2( -self.x , -self.y )
    def __abs__(self):
        return vec2( abs(self.x) , abs(self.y) )
# object.__invert__(self)
    def __str__ (self):
        return "vec2: " +  str(self.x) + " " + str(self.y)
    

d = vec2(1,2)
print(d)

c = vec2(1,3)
print(d * 2)