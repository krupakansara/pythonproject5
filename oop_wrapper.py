#Employee Management System

#Base class

class Employee:
    #Constructor

    def __init__(self, employee_id=None, name=None, age=None, salary=None, gender=None):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary
        self.gender = gender

    #Getter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    #setter for employee_id:
    def set_employee_id(self, employee_id):
        self.__employee_id=employee_id

    #getter for salary
    def get_salary(self):
        return self.__salary

    #setter for salary
    def set_salary(self, salary):
        self.__salary=salary

    #display method
    def display(self):
        print("Employee ID: ", self.__employee_id)
        print("Name:", self.name)
        print("Age:",self.age)
        print("Gender: ", self.gender)
        print("Salary:",self.__salary)

  
    #destructor
    def __del__(self):
        print("Employee object removed.")

#derived class- manager
class Manager(Employee):

    def __init__(self, employee_id=None, name=None, age=None, salary=None, gender=None, department=None):
        super().__init__(employee_id, name, age, salary, gender)
        self.department=department

    #method overriding
    def display(self):
        super().display()
        print("Department: ",self.department)

    
#derived class- Developer
class Developer(Employee):

    def __init__(self, employee_id=None, name=None, age=None, salary=None, gender=None, programming_language=None):
        super().__init__(employee_id, name, age, salary, gender)
        self.programming_language = programming_language

    #method overriding
    def display(self):
        super().display()
        print("Programming language: ",self.programming_language)

#list to store employees
employees = []
#check inheritance using issubclass()
print("Is Manager a subclass of Employee?", issubclass(Manager,Employee))
print("Is Developer a subclass of Employee?",issubclass(Developer,Employee))
#main menu
while True:

    print("\n====Employee Management System===")
    print("1. Add Employee")
    print("2. Add Manager")
    print("3. Add Developer")
    print("4. Display Employees")
    print("5. Update Employee")
    print("6. Remove Employee")
    print("7. Exit")

    choice=input("Enter your choice: ")

    #Add employee
    if choice == "1":

        employee_id = input("Enter Employee iD: ")
        name= input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter salary: "))
        gender = input("Enter Gender: ")

        employee=Employee(employee_id, name,age,salary,gender)

        employees.append(employee)

        print("Employee added successfully!")

        #Add Manager
    elif choice == "2":

            employee_id = input("Enter Employee ID:")
            name = input("Enter Name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary:"))
            gender = input("Enter gender: ")
            department = input("Enter Department: ")

            manager = Manager(
                employee_id,
                name,
                age,
                salary,
                gender,
                department
                )

            employees.append(manager)

            print("manager added Successfully.")

    #Add Developer
    elif choice == "3":

            employee_id = input("Enter Employee ID:")
            name = input("Enter name:")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary:" ))
            gender = input("Enyter gender: ")
            programming_language = input("Enter programming language: ")

            developer = Developer(
                employee_id,
                name,
                age,
                salary,
                gender,
                programming_language
                )

            employees.append(developer)

            print("Develeopr added successfully.")

    #display Employess
    elif choice == "4":

                if len(employees) == 0:
                    print("No employee found")
                else:
                    print("\n == Employee details==")

                    for employee in employees:
                        print("---------")
                        employee.display()

     #update employee
    elif choice == "5":
            employee_id = input("Enter Employee Id to update: ")

            found = False

            for employee in employees:
               if employee.get_employee_id() == employee_id:

                 print("\n1. update employee ID")
                 print("2. update salary")

                 update_choice = input("Enter your choice: ")

                 if update_choice == "1":

                    new_id = input("Enter New Employee ID: ")
                    employee.set_employee_id(new_id)

                    print("Employee ID updated successfully")

                 elif update_choice == "2":

                    new_salary = float(input("Enter new salary"))
                    employee.set_salary(new_salary)

                    print("Salary updated successfully")

                 else:
                    print("inavlid choice")

                    found = True
                    break

            if found == False:
                print("Employee not found")
                
            
    #Remove employee
    elif choice == "6":

            employee_id = input("Enter Employee ID to remove: ")
            found = False

            for employee in employees:

                if employee.get_employee_id() == employee_id:
                    employees.remove(employee)
                    print("Employee removed successfully")
                    found = True
                    break
                
            if found == False:
                print("Employee not found")

        #Exit
    elif choice == "7":
            print("Thank you for using Employee Management system")
            break
    else:
        print("invalid choice")
        
                
                
                
                

            
            
            

        

    
            
            
        
            
    
