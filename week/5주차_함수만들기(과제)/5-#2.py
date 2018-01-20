import math
radius = 5
print(round(math.pi * radius ** 2,2))
radius = 9
print(round(math.pi * radius ** 2,2))
radius = 23
print(round(math.pi * radius ** 2,2))

def area_circle(radius,r):
    import math
    return round(math.pi * radius ** 2 , r)

print(area_circle(5,2))
print(area_circle(9,2))
print(area_circle(23,2))
