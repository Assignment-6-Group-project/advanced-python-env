class Person:
    def __init__(self, name):
        self._name = name          

    def introduce(self):
        return f"My name is {self._name}"

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def introduce(self):
        return f"I am student {self._name}, ID: {self.student_id}"

def demo():
    p = Person("Anna")
    s = Student("John", "S123")

    people = [p, s]

    for person in people:
        print(person.introduce())  

if __name__ == "__main__":
    demo()



