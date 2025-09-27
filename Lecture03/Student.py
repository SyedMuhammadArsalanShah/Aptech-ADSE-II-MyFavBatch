class Student :
    uname="saaria"

    @classmethod
    def username(cls, name):
       cls.uname=name
       print("student username ", cls.uname)
  


    def __init__(self,name, age, contact, salary):
        self.name=name
        self.age=age
        self.contact=contact
        self.salary=salary
        print("Student Name is ",self.name, "Age is ",self.age, "Contact ", self.contact, "and salary is ",self.salary)
        

    def speak(self,zayada):
        print("they can be speakkkkkk",zayada)

    @staticmethod
    def run():
        print("they can be run ")

    def status(self,feestatus):
        self.feestatus=feestatus
        print("Fees paid")



s1=Student("Hiba", "20","15","10000000000")

s1.speak(True)
s1.run()
print(s1.uname)
s1.uname="saaria.pk"
print(s1.uname)
s1.username("saaria.pk")

print(Student.uname)

s1.status(False)
