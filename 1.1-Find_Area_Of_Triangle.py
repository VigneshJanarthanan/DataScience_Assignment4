class Triangle_inp:
    def __init__(self, side1, side2, side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        
class area(Triangle_inp):
    def __init__(self, side1, side2, side3):
        super(area, self).__init__(side1, side2, side3)
        self.semi=(self.side1+self.side2+self.side3)/2
        self.triarea=(self.semi*(self.semi-self.side1)*(self.semi-self.side2)*(self.semi-self.side3))**0.5

        
a=int(input("A Side of a triangle: "))
b=int(input("B Side of a triangle: "))
c=int(input("c Side of a triangle: "))

findarea=area(a,b,c)
print("semiperimeter is: %f " % findarea.semi)
print("Area of Triangle: %f" % findarea.triarea)