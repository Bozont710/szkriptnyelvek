#!/usr/bin/env python3

import math

class Sphere:
    def __init__(self, r):
        self.r = r
    #END__init__

    def sphere_volume(self):
        return (4/3)*math.pi*(self.r**3)
    #ENDvolume

    def sphere_surface_area(self):
        return 4*math.pi*(self.r**2)
    #ENDsurface_area

    def __str__(self):
        return str(self.data)
    #END__str__

    def __eq__(self, other):
        return self.sphere_volume() == other.sphere_volume()
    #END__eq__

    def __ne__(self, other):
        return self.sphere_volume() != other.sphere_volume()
    #END__ne__

    def __lt__(self, other):
        return self.sphere_volume() < other.sphere_volume()
    #END__lt__

    def __gt__(self,other):
        return self.sphere_volume() > other.sphere_volume()
    
    def __le__(self,other):
        return self.sphere_volume() <= other.sphere_volume()
    
    def __ge__(self,other):
        return self.sphere_volume() >= other.sphere_volume()
#ENDSphere


class Ellipsoid:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    #END__init__

    def ellipsoid_volume(self):
        return (4/3)*math.pi*self.a*self.b*self.c
    #ENDvolume

    def ellipsoid_surface_area(self):
        one = self.a*self.b
        two = self.a*self.c
        three = self.b*self.c
        return 4*math.pi*(((one**1.6)+(two**1.6)+(three**1.6))/3)**(1/1.6)
    #ENDellipsoid_surface_area
    
    def __str__(self):
        return f"{self.a}{self.b}{self.c}"
    #END__str__
#ENDEllipse


def main():
    s1 = Sphere(5)
    print(s1.sphere_volume())
    print(s1.sphere_surface_area())
    e = Ellipsoid(1,2,3)
    print(e.ellipsoid_volume())
    print(e.ellipsoid_surface_area())

    s2 = Sphere(6)
    print(s1!=s2)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
