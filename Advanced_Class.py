
class CollegeStudent:
    def __init__(self, name, age, yearsection):
        self.name = name
        self.age = age
        self.yearsection = yearsection
        
    def __str__(self):
        return f"A college student named {self.name} is {self.age} years old in {self.yearsection}"

Student1 = CollegeStudent("Jake Reyes", 17, "DHRS-1A")
print(Student1)

Student2 = CollegeStudent("John Imaculo", 18, "BTVTED-2A")
print(Student2)

Student3 = CollegeStudent("Jovan Hilan", 20, "BSPA-2B")
print(Student3)