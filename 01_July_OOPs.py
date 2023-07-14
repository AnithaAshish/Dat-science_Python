#!/usr/bin/env python
# coding: utf-8

# In[ ]:


What is the primary goal of Object-Oriented Programming (OOP)?
The primary goal of OOP is to give a structure to the program which makes the code Robust,Resuable,Maintainable and easy debugging.
This approach is well-suited/beneficial for collaborative enviornment,where the project is divided in groups and everyone can add their modues to it.
It enables a programmer to represent every real world entity as an object by binding attributes and functions with an object


# In[ ]:


get_ipython().set_next_input('What is an object in Python');get_ipython().run_line_magic('pinfo', 'Python')
Object is an instance of a class.
Object is the actual entity while class is just a blue print/general template.
Every object has its specific data and functions.


# In[ ]:


get_ipython().set_next_input('What is a class in Python');get_ipython().run_line_magic('pinfo', 'Python')
Class is a general template/blue print of an object which has attributes and methods binded in it.


# In[ ]:


get_ipython().set_next_input('What are attributes and methods in a class');get_ipython().run_line_magic('pinfo', 'class')
Attibutes are the variables which stores data values in it.
There are two types of variables:Class variable and instance variable
    Class variabes are shared among objects of the class
    Instance variables are specific for tat instance of the class.
Methods are the functions which defines the functionality/behaviour of the object.


# In[ ]:


get_ipython().set_next_input('What is the difference between class variables and instance variables in Python');get_ipython().run_line_magic('pinfo', 'Python')
Class variable is shared by all the instances of the class while instance variable is specific to the instance.


# In[ ]:


get_ipython().set_next_input('What is the purpose of the self parameter in Python class methods');get_ipython().run_line_magic('pinfo', 'methods')
Self parameter refers to the variables and methods of an instance of the class.


# In[59]:


class Book:
    
    #This funtion is invoked when an instance/object of the class is creatd and it initializes values for that instance.
    def __init__(self,title_book,author_book,isbn_book,publi_year_book,copies_book):
        
    # Below are the attributes. 
        self.title=title_book
        self.author=author_book                           
        self.isbn=isbn_book
        self.publication_year=publi_year_book
        self.available_copies=copies_book
        
        
                
    # This function will decrement the count of available copies of the book after checking the availability of the book
    def check_out(self):
        if self.available_copies>0:
            self.available_copies-=1
        else:
            print("Book is currently not available")
            
    # This function will increment the count of available copies of the book
    def return_book(self):
        
            self.available_copies+=1
        
            
    #This function will display information of the book
    def display(self):
        
            print("Details of the book are:")
            print(f"Title:-{self.title}")
            print(f"Author:-{self.author}")
            print(f"ISBN:-{self.isbn}")
            print(f"Publication Year:-{self.publication_year}")
            print(f"Availabe copies:-{self.available_copies}\n")
        
                  
# Creating an instance named book1 of the class Book        
book1=Book("Python the complete Reference","Martin C.Brown","978-938757292",2018,20)
# Creating an instance named book2 of the class Book      
book2=Book("Pyhton for Data analysis","Wes Mckinney","978-9355421906",2022,30)
#Calling the function using dot operator (<object name>.<function name>)
book1.display()
book1.check_out()
book1.display()
book2.display()


# In[63]:


class Ticket:
    #This is a class varible.
    id=0
  
    
     #This funtion is invoked when an instance/object of the class is created and it initializes values for that instance.
        
    def __init__(self,name,date,venue,price,seat,reservation="NONE"):
        #class variable 'id' is accessed using class name 'Ticket'.This class variable is used to assign unique value to all ticket ids
        Ticket.id+=1
        self.ticket_id="IPL2023_"+str(Ticket.id)
        self.event_name=name
        self.event_date=date
        self.venue=venue
        self.price=price
        self.seat_no=seat
        self.is_reserved=reservation
        
           
            
    def reserve_ticket(self):
        if self.is_reserved!="Reserved":
            self.is_reserved="Reserved"
        print(f"After reservation:")
        self.display_ticket_info()    
        
    def cancel_ticket(self):
        if self.is_reserved=="Reserved":
            self.is_reserved="Cancelled"
            print(f"{self.ticket_id} is cancelled")
          
    
    def display_ticket_info(self):
        print("\t\tInformation about the ticket are:\t\t")
        print(f"Ticket number is {self.ticket_id}")
        print(f"Event is  {self.event_name}")
        print(f"Event is on {self.event_date}")
        print(f"Event is at {self.venue}")
        print(f"Ticket is worth {self.price} rupees")
        print(f"Seat no. is {self.seat_no}")
        print(f"Reservation status: {self.is_reserved}")
        
t1=Ticket("IPL_final2023","28th May","Ahmedabad",1000,"A-25")
t2=Ticket("IPL_Semi2023","26th May","Chennai",800,"B-50")
t1.display_ticket_info()
t1.reserve_ticket()
t1.cancel_ticket()
t2.display_ticket_info()


# In[47]:


class ShoppingCart:
    
    def __init__(self):
        self.items=[]#items is a list variable
        
    def add_item(self,item):
        self.items.append(item)#append method appends items to the list
        
    def remove_item(self,item):
        if item in self.items:
            items.remove[item]#remove method removes items from the list
            
    def view_cart(self):
        if len(self.items)==0:#len function checks the size of the list
            print("Cart is empty")
        else:
            print(f"Items in the cart are:-")
            for item in self.items:
                print(item)
            
    def clear_cart(self):
        self.items.clear()
        self.items=[]
        print("Cart is empty")
        
        
cart1=ShoppingCart()
cart1.add_item("Books")
cart1.add_item("Pens")
cart1.add_item("Bag")
cart1.add_item("Shoes")
cart1.add_item("Trousers")
cart1.add_item("T-shirt")
cart1.view_cart()
cart1.clear_cart()


# In[43]:




class Student:
    
    #id is a class variable shared among all instances of the class
    id=202301
   
    def __init__(self,name,age,grade):
        #instance variable is assigned class variable value to keep the student id unique across instances of the class
        self.student_id=Student.id
        self.name=name
        self.age=age
        self.grade=grade
        self.attendance={}#attendance is a dictionary variable with date:status as the key value pair
        Student.id+=1
        
    #Function to update/add the attendance of a student
    def update_attendance(self,date,status):
                
        if date in self.attendance.keys():
            self.attendance[date]=status
        else:
            self.attendance.update({date:status})
            
    #Function returns the attendance of a student
    def get_attendance(self):
        return self.attendance
    
    #Function calculates the average attendance of a student
    def get_avg_attendance(self):
        present=absent=0
        for key in self.attendance:
            if self.attendance[key]=='p':
                present+=1
            elif self.attendance[key]=='a':
                absent+=1
        total_days=len(self.attendance)
        percent_present=round((present/total_days)*100)
        percent_absent=round((absent/total_days)*100)
        return percent_present,percent_absent

    #Fuction displays the information of the student
    def display(self):
        print("Student informtion is as follows:\n")
        print(f" Name-\t Id \t Age\t Grade  \n")
        print(f"{self.name}\t {self.student_id}\t {self.age}\t {self.grade} \n")
        
             

s1=Student("Anitha",17,12)
s2=Student("Priya",16,11)
s3=Student("Sahil",15,10)
s4=Student("Aadhyansh",11,6)
s1.display()
s2.display()


s1.update_attendance("20-6-2023","p")
s1.update_attendance("21-6-2023","p")
s1.update_attendance("23-6-2023","p")
s1.update_attendance("20-6-2023","a")
s1.update_attendance("24-6-2023","a")

attend=s1.get_attendance()
print(f"Attendance record of {s1.name}:-{attend}")
avg_attendance=s1.get_avg_attendance()
print(f"Average attendance of {s1.name}:-Present={avg_attendance[0]}% Absent={avg_attendance[1]}%")
    
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




