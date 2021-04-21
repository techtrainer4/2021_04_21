#user defined functions
#What is the area of triangle
b = 5
h = 10
A = b * h / 2 

def Area_of_Tri(base,height):
  Area = base * height / 2 
  return Area
print(Area_of_Tri(10,12))

def Gmail():
  name = input("Type your first name ")
  surname = input("Type your last name ")
  address = f"{name}.{surname}@gmail.com"
  return address

print(Gmail())

def Intro():
  name = input("What is your name? ")
  where = input("Where are you from?")
  intro = f"My name is {name} and I am from {where}."
  return intro 

def area_circle(r): #pi = 3.14159
  pi = 3.14159
  A = pi * r ** 2 
  return A 


















