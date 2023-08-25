# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple
Point = collections.namedtuple("Point" , "x y")
p1 = Point(10, 20)
p2 = Point(30, 40)

print(p1, p2)

# TODO: use _replace to create a new instance
p1 = p1._replace(x=100)
p2 = p2._replace(y=400)
print(p1, p2)