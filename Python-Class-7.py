# typecasting = convert the value of one data type to another (string, integer, float, bool)
# two types: Explicit & Implicit

emp = [10,40,20,30,0]
emp1 = ["Vivek","Harry"]
emp3 = ["male",10,20]
emp4 = emp3.copy()
print(emp3)

emp4.append(25)
print(emp4)
emp2 = list(zip(emp,emp1))
print(emp2)
# 0, "", None, False

# all()  AND
# any()  OR



print(all(emp))
print(any(emp))

# enumerate

length = int(input("ENter the length:"))
width = int(input("Enter the width:"))
height = int(input("Enter the height:"))
area = length * width * height

print(f"Area of 3D Rectangle:{area}")


# calculate Ecommerce
item = input("ENter the Product:")
price = float(input("Enter the Price:"))
quantity = int(input("Enter the Quantity:"))

total = price * quantity

print(f"The total price is {round(total,2)}")

x = 3.14
y = -1
z = x + y
print(x)
print(abs(y))
print(type(x))
x = round(x)
print(type(x))

result = pow(x,2)
print(result)


list1= [10,20,"vivek",True]
tuple1= (10,20,"vivek",True,[None, 0])
print(all(tuple1))

emp_data = {"id": 101, "name": "Alice", "role": "DevOps"}
print(emp_data["name"])

print(emp_data.get('id'))
print(emp_data.get('Salary','N/A'))
emp_data['Salary']=7000
print(emp_data)
print(emp_data.keys())
print(emp_data.values())
emp_data.pop('Salary')
emp_data.update({"Salary": 7000})
print(emp_data)


emp_name = ["vivek","Sam"]
emp_age = [30,30]
employee = dict(zip(emp_name,emp_age))
print(type(employee))
print(employee)


# if-elif


x = int(input("Enter the age:"))
if x >=18:
    print("Your elegible to vote")
else:
    print("Your elegible to not vote")
print("End")

x =10
y = 5
ex = input("Enter the Expression:")


if ex == "+" or ex =="add":
    print(x+y)
elif ex == "-" or ex =="subtract":
    print(x-y)
elif ex == "*" or ex =="multiply":
    print(x*y)
elif ex == "/" or ex =="divide":
    print(x/y)
else:
    print("Please enter a valid expression")

age = int(input("Enter the age:"))
citizen = True

if age >= 18:
    if citizen:
        print("YOur elegible to vote")
    else:
        print("YOur elegible to not vote")
else:
    print("Under age")




