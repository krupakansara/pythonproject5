🧑‍💼 OOP Wrapper — Employee Management System
<p align="center">
  <h2 align="center">🐍 OOP Wrapper</h2>
  <p align="center">Employee Management System using Python OOP</p>
</p>
---
🌟 Project Overview
OOP Wrapper is a Python project that creates an Employee Management System using Object-Oriented Programming concepts.
The program manages three types of employee objects:
👤 Employee
👨‍💼 Manager
👨‍💻 Developer
The uploaded project code implements an `Employee` base class, `Manager` and `Developer` derived classes, private employee ID and salary data, getter/setter methods, constructors, a destructor, method overriding, `super()`, `issubclass()`, and a menu-driven interface.
---
🎯 Objective
The main objective of this project is to understand and practically implement important Python OOP concepts, including:
🏗️ Classes
🎯 Objects
🧱 Constructors
🧹 Destructor
🔐 Encapsulation
🧬 Inheritance
🔄 Method Overriding
⬆️ `super()`
🔎 `issubclass()`
🔑 Getter and Setter Methods
🖥️ Menu-Driven Interface
---
🏛️ Class Structure
```text
                    Employee
                   /        \
                  /          \
             Manager       Developer
                |              |
          Department     Programming Language
```
---
👤 Employee Class
`Employee` is the base class.
It stores:
🆔 Employee ID
👤 Name
🎂 Age
💰 Salary
⚧️ Gender
The project uses private attributes for employee ID and salary:
```python
self.__employee_id
self.__salary
```
It also contains getter and setter methods for these private attributes.
---
🔐 Encapsulation
Encapsulation is implemented by making sensitive information private.
Private attributes
```python
__employee_id
__salary
```
Getter methods
```python
get_employee_id()
get_salary()
```
Setter methods
```python
set_employee_id()
set_salary()
```
This allows the program to access and update the private data through methods.
---
🧬 Inheritance
The project contains two derived classes:
```python
class Manager(Employee):
```
and
```python
class Developer(Employee):
```
Both inherit from the `Employee` class.
---
👨‍💼 Manager Class
The `Manager` class inherits the Employee features and adds:
```python
department
```
The `display()` method is overridden to display the manager's department.
---
👨‍💻 Developer Class
The `Developer` class inherits the Employee features and adds:
```python
programming_language
```
The `display()` method is overridden to display the developer's programming language.
---
🔄 Method Overriding
Both derived classes override the `display()` method.
Manager
```python
def display(self):
    super().display()
    print("Department:", self.department)
```
Developer
```python
def display(self):
    super().display()
    print("Programming language:", self.programming_language)
```
This allows each class to display its own additional information.
---
⬆️ `super()`
`super()` is used to call the parent class methods.
For example:
```python
super().__init__(employee_id, name, age, salary, gender)
```
and:
```python
super().display()
```
---
🔎 `issubclass()`
The project checks inheritance using:
```python
issubclass(Manager, Employee)
issubclass(Developer, Employee)
```
The expected result is:
```text
True
True
```
---
🖥️ Menu-Driven Interface
The program provides these options:
🔢 Option	📌 Operation
1️⃣	Add Employee
2️⃣	Add Manager
3️⃣	Add Developer
4️⃣	Display Employees
5️⃣	Update Employee
6️⃣	Remove Employee
7️⃣	Exit
---
⚙️ Main Operations
➕ Add Employee
Enter employee ID, name, age, salary, and gender.
👨‍💼 Add Manager
Enter employee information along with the department.
👨‍💻 Add Developer
Enter employee information along with the programming language.
📋 Display Employees
Displays the stored employee information.
✏️ Update Employee
Allows updating:
🆔 Employee ID
💰 Salary
🗑️ Remove Employee
Removes an employee using the employee ID.
🚪 Exit
Exits the Employee Management System.
---
📸 Screenshots
> The README is prepared for the five screenshots you provided. Place the image files in the `screenshots` folder using these exact filenames.
🏠 Main Menu
![Main Menu](screenshots/Screenshot%202026-10-04%20154119.png)
➕ Employee / Manager Entry
![Employee Entry](screenshots/Screenshot%202026-10-04%20154132.png)
📋 Employee Details
![Employee Details](screenshots/Screenshot%202026-10-04%20164536.png)
✏️ Update / Management
![Update](screenshots/Screenshot%202026-10-04%20164550.png)
🖥️ Program Output
![Program Output](screenshots/Screenshot%202026-10-04%20164559.png)
---
🎥 Project Demonstration
Place the project demonstration video in the `video` folder:
Video filename:
```text
2026-10-04 16-30-31.mp4
```
▶️ 🎬 Open Project Demonstration Video
---
🛠️ Technologies Used
🐍 Python
💻 Python IDLE / Python Editor
🧠 Object-Oriented Programming
---
🚀 How to Run
Open `oop_wrapper.py`.
Run the Python program.
The Employee Management System menu will appear.
Select an option from the menu.
Enter the required information.
Use the available options to add, display, update, or remove employees.
Select 7️⃣ Exit to close the program.
---
📚 Learning Outcomes
By completing this project, I learned how to:
Create and use classes.
Create constructors and destructors.
Use `self`.
Implement encapsulation.
Use private attributes.
Create getter and setter methods.
Implement inheritance.
Override parent class methods.
Use `super()`.
Check inheritance using `issubclass()`.
Create a menu-driven Python application.
---
👩‍💻 Project Details
📌 Detail	💡 Information
Project Name	OOP Wrapper
Application	Employee Management System
Language	Python 🐍
Main Topic	Object-Oriented Programming
Base Class	Employee
Derived Classes	Manager, Developer
---
⭐ Thank You
Thank you for checking out my Python OOP project! 🐍💙
> Made with Python, practice, and OOP concepts. 🚀
