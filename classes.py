class point():
    def __init__(self,a,b): # called everytime when class objects are created
        self.x = a   # creating instances x and y for point class
        self.y = b
p = point(3,4)
print(p.x)
print(p.y)