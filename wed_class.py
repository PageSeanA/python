#Powerpoint 48/53 - 49/53

class Student(object):

    def __init__(self, firstName, lastName, campus):
        self.firstName = firstName
        self.lastName = lastName
        self.campus = campus

    def printStudent(self):
        print(f"{self.firstName} {self.lastName} campus: {self.campus}")


class Campus(object):

    def __init__(self):
        self.students = []

    def addStudent(self, firstName, lastName, campus):
        temp  = Student(firstName, lastName, campus)
        self.students.append(temp)

    #def

    def showCurrentStudent(self):
        for studentObject in self.students :
            print(f"{studentObject.firstName} {studentObject.lastName} campus: {studentObject.campus}")

houston = Campus()
houston.addStudent("alina", "belova", "houston") 
houston.addStudent("kazim", "sha", "houston")
houston.addStudent("alex", "fisher", "new york")
houston.addStudent("matt", "ryan", "chicago")
houston.addStudent("sean", "page", "chicago")

alina = Student("alina", "belova", "houston") 
kazim = Student("kazim", "sha", "houston")
alex = Student("alex", "fisher", "new york")
matt = Student("matt", "ryan", "chicago")
sean = Student("sean", "page", "chicago")