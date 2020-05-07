import math

class Vector3:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def Magnitude(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    def Normal(self):
        magnitude = self.Magnitude()
        newX = self.x / magnitude
        newY = self.y / magnitude
        newZ = self.z / magnitude
        return Vector3(newX, newY, newZ)
    
    def DotProduct(self, other):
        return ((self.x * other.x) + (self.y * other.y) + (self.z * other.z))
    
    def Add(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def Sub(self, other): #self - other
        return(Vector3(self.x - other.x, self.y - other.y, self.z - other.z))


    def Scale(self, scale):
       return(Vector3(scale * self.x, scale * self.y, scale * self.z))

    def Div(self, denom):
        return(Vector3(self.x / denom, self.y / denom, self.z / denom))

#test cases
vec = Vector3(-1, 2, -9)
print("Magnitude is " + str(vec.Magnitude()))
normal = vec.Normal()
print("Normal is " + str(normal))
dot = vec.DotProduct(Vector3(1, 2, 3))
print("Dot Product is " + str(dot))
add = vec.Add(Vector3(1,2,3))
print("add is " + str(add))
