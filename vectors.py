import math
#simple vectors classes 
class vec2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def zero():
        return vec2(0,0)
    def one():
        return vec2(1,1)

    def Distance(self, other):
        return (self - other).magnitude()
    
    def cross(self , other):
        return (self.x * other.y )- (self.y * other.x)
    def magnitude(self):
        return math.sqrt(self.x* self.x + self.y * self.y)
    def sqrMag(self):
        return self.x* self.x + self.y * self.y
    def normalized(self):
        mag = self.magnitude()
        if mag == 0:
            return self 
        return self/ mag
    def Perpendicular(self):
        return vec2(-self.y, self.x)

    def  __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return vec2(self.x * other, self.y * other)
    def __truediv__(self, other):
        return vec2(self.x / other, self.y / other)
    def __floordiv__(self, other):
        return vec2(self.x.__floordiv__(other), self.y.__floordiv__(other))
    def __mod__(self, other):
        return vec2(self.x % other, self.y % other)
    def __neg__(self):
        return vec2( -self.x , -self.y )
    def __abs__(self):
        return vec2( abs(self.x) , abs(self.y) )
    def __str__ (self):
        return "vec2: " +  str(self.x) + " " + str(self.y)
    
class vec3:
    def __init__(self, x = 0, y = 0, z = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def zero():
        return vec3(0,0,0)
    def one():
        return vec3(1,1,1)

    def Distance(self, other):
        return (self - other).magnitude()
    
    def magnitude(self):
        return math.sqrt(self.x* self.x + self.y * self.y + self.z * self.z)
    def sqrMag(self):
        return self.x* self.x + self.y * self.y + self.z * self.z
    def normalized(self):
        mag = self.magnitude()
        if mag == 0:
            return self 
        return self/ mag

    def  __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + self.z)
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return vec3(self.x * other, self.y * other,  self.z * other)
    def __truediv__(self, other):
        return vec3(self.x / other, self.y / other ,self.z/ other)
    def __floordiv__(self, other):
        return vec3(self.x.__floordiv__(other), self.y.__floordiv__(other)
                    ,self.z.__floordiv__(other))
    def __mod__(self, other):
        return vec3(self.x % other, self.y % other, self.z % other)
    def __neg__(self):
        return vec3( -self.x , -self.y , -self.z)
    def __abs__(self):
        return vec3( abs(self.x) , abs(self.y), abs(self.z)  )
    def __str__ (self):
        return "vec3: " +  str(self.x) + " " + str(self.y) + " " + str(self.z)
    
class vec4:
    def __init__(self, x = 0, y = 0, z = 0, w = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def zero():
        return vec3(0,0,0,0)
    def one():
        return vec3(1,1,1,1)

    def Distance(self, other):
        return (self - other).magnitude()
    
    def magnitude(self):
        return math.sqrt(self.x* self.x + self.y * self.y + self.z * self.z + self.w * self.w)
    def sqrMag(self):
        return self.x* self.x + self.y * self.y + self.z * self.z + self.w * self.w
    def normalized(self):
        mag = self.magnitude()
        if mag == 0:
            return self 
        return self/ mag

    def  __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w
    def __add__(self, other):
        return vec4(self.x + other.x, self.y + other.y, self.z + self.z, self.w + self.w)
    def __sub__(self, other):
        return vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __mul__(self, other):
        return vec4(self.x * other, self.y * other,  self.z * other,  self.w * other)
    def __truediv__(self, other):
        return vec4(self.x / other, self.y / (other) ,self.z / (other), self.w / (other))
    def __floordiv__(self, other):
        return vec4(self.x.__floordiv__(other), self.y.__floordiv__(other)
                    ,self.z.__floordiv__(other), self.w.__floordiv__(other))
    def __mod__(self, other):
        return vec4(self.x % other, self.y % other, self.z % other, self.w % other)
    def __neg__(self):
        return vec4( -self.x , -self.y , -self.z, -self.w)
    def __abs__(self):
        return vec4( abs(self.x) , abs(self.y), abs(self.z), abs(self.w))
    def __str__ (self):
        return "vec4: " +  str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(self.w)
    
def test():
    print(vec2.zero().normalized())
    print(vec2(1,4).magnitude())

if __name__ == "__main__":
    test()
