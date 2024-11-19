print ("******* AREA CALCULATOR*****")
print("Enter 1 to know the area of square")
print("Enter 2 to know the area of rectangle")
print("Enter 3 to know the area of circle")
print("Enter 4 to know the area of triangle")


n = int (input("Enter any number between 1 to 4 :"))

if n == 1:
    side = float(input("enter the side of the square:"))
    area = side*side
    print("the area of the square :", area, "m2")
elif n==2:
    length = int(input("enter the length of the rectangle :"))
    breadth = int(input("enter the breadth of the rectangle :"))
    area = length * breadth
    print("the area of the rectangle :", area, "m2")


