class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks
    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False
Jan = Student("Jan", 48)
Adam = Student("Adam", 220)

print(Jan.is_passed())
print(Adam.is_passed())