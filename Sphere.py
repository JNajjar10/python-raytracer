from Vector3 import Vector3
from Material import Material
from math import sqrt

class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material
    

    # def rayIntersect(self, origin, direction):
    #     oc = origin.Sub(self.center)
    #     a = direction.DotProduct(direction)
    #     b = 2.0 * oc.DotProduct(direction)
    #     c = oc.DotProduct(oc) - (self.radius * self.radius)
    #     discriminant = b * b - 4 * a * c
    #     if discriminant < 0: 
    #         return False
    #     return True


    def rayIntersect(self, origin, direction):
        l = self.center.Sub(origin)
        tca = l.DotProduct(direction)
        if tca < 0:
            return False
        d = sqrt(l.DotProduct(l) - (tca * tca))
        if d < 0 or d > self.radius:
            return False
        thc = sqrt((self.radius * self.radius) - (d * d))
        t0 = tca - thc
        t1 = tca + thc
        P1 = origin.Add(direction.Scale(t0))
        P2 = origin.Add(direction.Scale(t1))
        return True
