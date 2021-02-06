class Manager(): 
    def __init__(self, Name, Age, Language):
        Employee.__init__(self, Name, Age, Language) 
       
    def name(self):
        return self.Name
    def age(self): 
        return self.Age
    def language(self):
        return self.Language
    
class Employee():
    
    def __init__(self, Name, Age, Language): 
        self.name = Name
        self.age = Age
        self.language= Language
            
    def Name(self):
        return self.Name
   
    def Age(self):
        return self.Age
   
    def Language(self):
        return self.Language
 


 

manager = Manager("Michael", 35,"Japanese ")
manager2 = Manager("Margaret",32,"French")
staff = []

staff.append(manager)
staff.append(manager2)
staff.append(Employee("Jack", 25,"Italian"))
staff.append(Employee("Britney", 22, "German"))
staff.append(Employee("Kevin",  27, "Chinese"))

for e in staff:
        print(e.language)
