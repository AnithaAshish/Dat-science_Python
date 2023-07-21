#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Explain what inheritance is in object-oriented programming and why it is use');get_ipython().run_line_magic('pinfo', 'use')

Inheritance allows a class(child class) to access all data variables and methods from its parent class(base class).
With the help of inheritance, general/common variables and methods can be defined in parent class and can be accessed(reused) in all its child classes, instead of defining it again in the child classes.
Main advantages of inheritance is reusability of code.
    
    


# In[ ]:


Discuss the concept of single inheritance and multiple inheritance, highlighting their
differences and advantages.

Single inheritance is a concept of: a class inheriting variables and methods from a single class.
eg:
    class Person:#parent class
        def __init__(self,name):
            self.name=name
        def display(self):
            print(self.name)
            
    class Student(Person):#child class inheriting only one class(Person class)
        pass
    s1=Student("Raja")
    s1.display()
    
Multiple inheritance is concept of:a class interiting variables from multiple classes.
In the below example Teacher class is inheriting 2 classes:Person and Employee
eg:
class Person:
       
        def displayPerson(self):
            print("Able to access person class from child class")
            
class Employee:
        
        def displayEmployee(self): 
            print("Able to access employee class from child class")
        
class Teacher(Person,Employee):#inheriting Person and Employee classes
        pass
t1=Teacher()
t1.displayPerson()
t1.displayEmployee()
__________________________________________________________________________________
Advantages of single and multiple inheritance:-
    
Single inheritance:Code resuability,Less overhead and requires less execution time than multiple inheritance.  
Multple inheritance:Efficient when multiple people are working in a projectand multiple classes are written by different programmers.
The needed methods from multiple classes can be inherited in a single class by multiple inheritance rather than writing them again.


# In[ ]:


Explain the terms "base class" and "derived class" in the context of inheritance.
Base class: Base class is called the parent class which can have general methods and variables that can be used by its child/derived classes. 
Derived class: Derived class is the class which inherits the variables and methods of base class.
It is also know as child class.
 
In the below example,ElectronicDevice is the Base class and Oven is the derived class,
which inherits the variables and methods of base class.
eg:
class ElectronicDevice:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def displayinfo(self):
        print(self.name,self.brand)
        
class Oven(ElectronicDevice):
    pass
o1=Oven("Oven","L.G")
o1.displayinfo()


# In[ ]:


What is the significance of the "protected" access modifier in inheritance? How does
get_ipython().set_next_input('it differ from "private" and "public" modifiers');get_ipython().run_line_magic('pinfo', 'modifiers')

Protected Modifier:
Protected access modifier can be accessed only by derived class.
They are denoted with a '_'as a suffix to  the variable name eg:_name
    
Public variables can be accessed from anywhere.

Private variables cannot be directly accessed in any other class other than where it is defined.
It is denoted by '__'as a suffix to variable name. eg:__name.
Python allows to access private variables explicitly by <objectname>._<Class name><private variable name>eg:s1._Student__name.
Using private varibles provides security to the application.


# In[ ]:


What is the purpose of the "super" keyword in inheritance? Provide an example.

Super is used to access the variables and methods of parent class in child class.
eg:
    class Person:
        def __init__(name,gender):
            self.name=name
            self.gender=gender
    class Teacher(Person):
        def __init__(self,name,gender,school):
            self.school=school
        super().__init__(name,gender)#here super() is used to access the variables(name and gender) of Parent class Person.
    


# In[41]:


class Vehicle:#Vehicle is the base/Parent class
    
    def __init__(self,model,make,year):
        self.model=model
        self.make=make
        self.year=year
        
    def get_Vehicledetails(self):
        return self.model+" "+self.make +" "+"launched in"+" " +str(self.year)
        
class Car(Vehicle):#Car is the child class which inherits Base class Vehicle
    
    def __init__(self,model,make,year,fuel_type):
        super().__init__(model,make,year)#Super() is used to access the variables of parent class(Vehicle).
        self.fuel_type=fuel_type #This line initializes the attribute of child class
        
        
    def get_Vehicledetails(self):#overriding the 'get_Vehicledetails' method of parent class in the child class 
        print(f"{super().get_Vehicledetails()} uses {self.fuel_type}") 

        
i20=Car("i20","hyundai",2014,"diesel")
bmw=Car("7 Series","BMW",1997,"petrol")
i20.get_Vehicledetails()
bmw.get_Vehicledetails()
        


# In[42]:


class Employee:#Parent class
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def EmployeeInfo(self):
        print(f"{self.name} is a employee of our organization")
        
class Manager(Employee):#Child class inheriting the Employee class
    def __init__(self,name,salary,department):
        super().__init__(name,salary)#Accessing parent variables using super()
        self.department=department#child class instance variable
    
    def EmployeeInfo(self):#Overriding parent class EmployeeInfo method
        print(f"{self.name} is the manager of {self.department} department")
    
class Developer(Employee):#Child class inheriting the Employee class
        def __init__(self,name,salary,program_lang):
            super().__init__(name,salary)#Accessing parent variables using super()
            self.programming_language=program_lang
            
        def EmployeeInfo(self):#Overriding parent class EmployeeInfo method
            print(f"{self.name} is a developer expert in {self.programming_language}")
            
        
m1=Manager("Anitha",1000000,"CSE")
m1.EmployeeInfo()
d1=Developer("Ashish",750000,"Python")
d1.EmployeeInfo()


# In[43]:



class Shape:#Parent class
    def __init__(self,color,border_width):
        self.colour=color
        self.border_width=border_width
        
    def Fill(self):
        print(f"The color of the shape is {self.colour}")
        
class Rectangle(Shape):#child class inheriting 'Shape'(Parent class)
    def __init__(self,colour,border_width,length,width):
        super().__init__(colour,border_width)
        self.length=length
        self.width=width
        
    def Area(self):#method to find area of rectangle
        area_rectangle=self.length*self.width
        print(f"Area of a rectangle is{area_rectangle}")
        
    def Fill(self):#overriding parent class 'Fill' method
        print(f"The rectangle is filled with {self.colour} color")

class Circle(Shape):#child class inheriting 'Shape'(Parent class)
    def __init__(self,colour,border_width,radius):
        super().__init__(colour,border_width)
        self.radius=radius
              
    def Area(self):#method to find area of a circle
        area_circle=2*3.14*pow(self.radius,2)
        print(f"Area of a circle is {round(area_circle)}")
        
    def Fill(self):#overriding parent class 'Fill' method
        print(f"The circle is filled with {self.colour} color")

r1=Rectangle("Green","2mm",50,12)
r1.Area()
r1.Fill()                                     
c1=Circle("Red","3mm",5) 
c1.Area()
c1.Fill()                                     


# In[45]:


class Device:#Parent class
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
class Phone(Device):#Child class inheriting Device(Parent class)
    def __init__(self,brand,model,screen_size):
        super().__init__(brand,model)
        self.screen_size=screen_size
        
        
    def PhoneInfo(self):
        
        print(f"Details of the Phone are:-\nBrand:{self.brand}\nModel:{self.model}\nScreen size:{self.screen_size}")
        
    
 
class Tablet(Device):#child class inheriting Device(Parent class)
    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity=battery_capacity
        
        
    def TabletInfo(self):
        
        print(f"Details of the Tablet are:-\nBrand:{self.brand}\nModel:{self.model}\nBattery Capacity:{self.battery_capacity}")
        
p1=Phone("Samsung","Nseries",'6"')
p1.PhoneInfo()
t1=Tablet("Apple","Pro 12.9","9720mAh")
t1.TabletInfo()
 


# In[1]:


class BankAccount:#Parent class
    balance=2000000 #balance is a class variable shared among all the instnces of the class
    def __init__(self,acc_no):
        self.account_number=acc_no
     
        
class SavingsAccount(BankAccount):#child class inheriting Parent class(BankAccount)
      
      
    def Calculate_interest(self):
        while True:
            interest_rate=float(input("Enter the interest rate in decimals\n"))#interest_rate is a local variable
            if interest_rate<=0 or interest_rate>=1:
                print("Invalid input")
                continue
            else:
                break
        interest=BankAccount.balance*interest_rate*1 #formula to calculate the interest/per year
        BankAccount.balance=BankAccount.balance+interest#Updating class variable
        print(f"The interest of your savings account is {interest}")
        print(f"Balance after adding the interest is {BankAccount.balance}")
            
class CheckingAccount(BankAccount):
    
    def Deduct_fee(self):
        charges=int(input("Enter the charges for the checking account"))
        fee=BankAccount.balance-charges #fee is a local variable
        print(f"Balance after deducting charges are {fee}")
        
          
s1=SavingsAccount(980780680)
s1.Calculate_interest()
c1=CheckingAccount(980780680)
c1.Deduct_fee()


# In[ ]:





# In[ ]:





# In[ ]:




