# 1
class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        return {'first_name': self.first_name, 'last_name': self.last_name}


# 2
class Storage:
    list1 = []

    def add(self, word):
        return self.list1.append(word)

    def get(self, word1=None):
        if word1:
            list_words = [i for i in self.list1 if i.startswith(word1)]
            return sorted(list_words)[:5]
        return sorted(self.list1)[:5]


# 3
class Course:
    students = []
    name = {}

    def __init__(self, course_name):
        self.course_name = course_name


    def add_student(self, obj):
        self.name['name'] = self.course_name
        self.students.append(dict(obj.info()))


    def to_json(self):
        self.name['students'] = self.students
        return self.name
