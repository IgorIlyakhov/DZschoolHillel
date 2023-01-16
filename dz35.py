class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender}: {self.first_name} {self.last_name} {self.age} years old'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.gender}: {self.first_name} {self.last_name} {self.age} years old (#{self.record_book})'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) == 10:
            raise UserException('\nМаксимальна кількість студентів в кількості 10 осіб\n')
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        self.group.discard(res)

    def find_student(self, last_name):
        for st in self.group:
            if last_name in str(st):
                return st

    def __str__(self):
        all_students = ''
        for st in self.group:
            all_students += f'\n{st}'
        return f'Number:{self.number}\n {all_students}'


class UserException(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


st1 = Student('Femal', 29, 'Ilona', 'Ik', 'AN142')
st2 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st3 = Student('Female', 26, 'Rate', 'Mirror', 'AN147')
st4 = Student('Female', 36, 'JIna', 'Opytr', 'AN154')
st5 = Student('Female', 30, 'Andriy', 'Klovsky', 'AN145')
st6 = Student('Male', 20, 'Lui', 'Gtrer', 'AN151')
st7 = Student('Male', 32, 'Antony', 'Ntrew', 'AN143')
st8 = Student('Female', 36, 'Masha', 'Hoprins', 'AN154')
st9 = Student('Male', 50, 'Boris', 'Jonhson', 'AN1141')
st10 = Student('Male', 31, 'Homer', 'Simpson', 'AN150')

st11 = Student('Female', 30, 'Mari', 'An', 'AN140')

gr = Group('A1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(f'Початкова група студентів: \n{gr}')

try:
    gr.add_student(st11)
except UserException as e:
    print(e.message)

print(gr.find_student('Jobs'))
print(gr.find_student('Jobs2'))

gr.delete_student('Ilona')

try:
    gr.add_student(st11)
except UserException as e:
    print(e.message)

print(f'\nГрупа студентів після змін\n{gr}')
