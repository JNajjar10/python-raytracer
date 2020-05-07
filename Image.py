from Vector3 import Vector3
from Sphere import Sphere
from Camera import Camera
from math import pi
from math import tan
from math import sqrt
from Light import Light

magicNumber = "P3"
width = 1024
height = 1024
maxColor = "255"
header = magicNumber + '\n' + str(width) + " " + str(height) + '\n' + maxColor + '\n'
cam = Camera(Vector3(0.0, 0.0, 0.0), 1)
frameBuffer = []
spheres = []
lights = []
s = Sphere(Vector3(8.0, 0.0, -20.0), 1, Vector3(102, 50, 60))
s2 = Sphere(Vector3(-8.0, 0.0, -20.0), 1, Vector3(70, 50, 60))
spheres.append(s)
spheres.append(s2)


# def castRay(orig, dir, s):
#     if(not s.rayIntersect(orig, dir)):
#         return Vector3(51, 178, 204)
#     return s.material
def buildRay(i, j):
    # x = (2 * (i + 0.5) / float(width) - 1) * tan(cam.fov/2.0) * width / float(height) 
    # y = -(2 * (j + 0.5) / float(height) - 1) * tan(cam.fov / 2.0)
    #print(str(x) + " , " + str(y))
    x = (i + 0.5) - width / 2.0
    y = -(j + 0.5) + height/2.0
    z = -height/(2.0 * tan(cam.fov/2.0))
    return x, y, z

def castRay(orig, dir, s):
    #t = sys.float_info.max #distance between ray origin and point
    if(not s.rayIntersect(orig, dir)):
        return Vector3(51, 178, 204)
    return s.material

# def intersect(orig, dir, s):
#     if(s.rayIntersect(orig, dir)):
#         return True
#     return False

def intersect(orig, dir, spheres):
    for s in spheres:
        if(s.rayIntersect(orig, dir)):
            return s.material
    return Vector3(51, 178, 204)

# def castRay(orig, dir, spheres, lights):
#     i = 0
#     lightIntensity = 0.0
#     while i < len(spheres):
#         if spheres[i].rayIntersect(orig, dir):
#             for light in lights:
#                 L = spheres[i].center.Sub(orig)
#                 tca = L.DotProduct(dir)
#                 d2 = L.DotProduct(L) - tca * tca
#                 if d2 > spheres[i].radius * spheres[i].radius:
#                     break 
#                 thc = sqrt(spheres[i].radius * spheres[i].radius - d2)
#                 t0 = tca - thc
#                 t1 = tca + thc
#                 if t0 < 0:
#                     t0 = t1 
#                 hit = orig.Add(dir.Scale(t0))
                
#                 N = (hit.Sub(spheres[i].center)).Normal()
#                 lightDirection = light.position.Sub((hit)).Normal()
#                 lightIntensity += light.intensity * (max(0, lightDirection.DotProduct(N)))
#             #print("light intensity: " + str(lightIntensity))
#             return spheres[i].material.Scale(lightIntensity)
#         else:
#              i += 1
#     return Vector3(51, 178, 204)
        


def bodyFormat(s, width):
    temp = ""
    i = 0
    widthCount = 0
    while i < len(s):
        temp += "{x} {y} {z} ".format(x = s[i].x, y = s[i].y, z = s[i].z)
        if(width - 1 == widthCount):
            temp += '\n'
            widthCount = 0
        else:
            widthCount += 1
        i += 1     
    return temp


def createFile(header, body):
    with open('raytrace.ppm', 'wb') as f:
        f.write(bytearray(header, 'ascii'))
        f.write(bytearray(body, 'ascii'))

def render():
    # spheres.append(Sphere(Vector3( 7, 5, -18), 4, Vector3(80, 120, 60)))
    # lights.append(Light(Vector3(-20, 20, 20), 50))


    # for j in range(height):  
    #     for i in range(width):
    #         for k in range(len(spheres)):
    #             x, y, z = buildRay(i, j)
    #             if(intersect(cam.location, Vector3(x, y, z).Normal(), spheres[k])): #i,j,-1.0
    #                 frameBuffer.append(spheres[k].material)
    #             else:
    #                 frameBuffer.append(Vector3(51, 178, 204))
    for j in range(height):  
        for i in range(width):
            x, y, z = buildRay(i, j)
            frameBuffer.append(intersect(cam.location, Vector3(x, y, z).Normal(), spheres)) #i,j,-1.
            

    body = bodyFormat(frameBuffer, width)
    createFile(header, body)



render()