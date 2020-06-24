class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    def __init__(self,fisrtName,lastName,idNum,scores):
        self.avg = (scores[0] + scores[1])/2
        Person.__init__(self,firstName,lastName,idNum)
    def calculate(self):
        if(90 <= self.avg <= 100): return 'O'
        elif(80 <= self.avg < 90): return 'E'
        elif(70 <= self.avg < 80): return 'A'
        elif(55 <= self.avg < 70): return 'P'            
        elif(40 <= self.avg < 55): return 'D'
        else: return 'T'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
