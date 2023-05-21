import json


class Pagination:
    def __init__(self, data):
        self.start = 0
        self.stop = 3
        self.collection = data

    def __iter__(self):
        return iter(self.collection[self.start: self.stop])

    def next_page(self):
        if len(self.collection) / self.stop < 1:
            return []
        else:
            self.start += 3
            self.stop += 3
            return iter(self.collection[self.start: self.stop])

    def prev_page(self):
        if self.start == 0:
            return []
        else:
            self.start -= 3
            self.stop -= 3
            return iter(self.collection[self.start: self.stop])


class FileStorage:

    @staticmethod
    def load_from_file(path):
        try:
            with open(path, 'r') as opened_file:
                text = opened_file.readlines()
                return path, json.loads(text[0])
        except (FileNotFoundError, IndexError):
            return path, {}

    @staticmethod
    def list_of_courses(courses):
        res1 = []
        for key, values in courses.items():
            v = [f'Student(first_name={i["first_name"]}, last_name={i["last_name"]})' for i in values]
            res1.append(f'Course(name={key}, students={v})')
        return res1

    @staticmethod
    def save_changes(path, text):
        with open(path, 'w') as file:
            file.write(json.dumps(text))


class Courses:
    list_courses = {}

    def list_for_pagination(self, data):
        list_of_students = []
        index = 1
        for key, values in data.items():
            self.list_courses[index] = key
            v = [f'Student(first_name={i["first_name"]}, last_name={i["last_name"]})' for i in values]
            list_of_students.append(f'{index} - Course(name={key}, students={v})')
            index += 1
        return list_of_students


class App:
    menu_items = ['1 - Add course name', '2 - Show all the courses',
                  '3 - Add student to the course', '4 - Delete the course/student', '5 - Exit']

    def __init__(self, storage):
        self.path = storage[0]
        self.storage = storage[1]

    def add_course(self):
        list_course = self.storage.keys()
        print('Adding course')
        course_name = input('Enter course name: ')
        if course_name:
            if course_name not in list_course:
                self.storage[course_name] = []
                print('Course added successfully')
            else:
                print('This course already exists. You could delete the old one or write different name')
                print('1 - Delete an old one', '2 - Create a new one', sep='\n')
                s = input()
                if s == '1':
                    self.delete_course()
                elif s == '2':
                    self.add_course()
        else:
            print('Course name was not written. Try again')
        return self.run()

    def add_student(self):
        if self.storage:
            print('Choose a course to add student in ')
            menu_for_pag = Courses()
            list_menu = Pagination(menu_for_pag.list_for_pagination(self.storage))
            for i in list_menu:
                print(i)
            while True:
                s = input('Choose a course or next/prev page:\n')
                if s == 'next':
                    r = list_menu.next_page()
                    if r:
                        for i in r:
                            print(i)
                    else:
                        print('No next data')
                        break
                elif s == 'prev':
                    l = list_menu.prev_page()
                    if l:
                        for i in l:
                            print(i)
                    else:
                        print('No prev data')
                        break
                elif s.isdigit():
                    course = Courses().list_courses
                    if int(s) in course.keys():
                        student = dict()
                        student['first_name'] = input('Write first name:')
                        student['last_name'] = input('Write last name:')
                        if student in self.storage[course[int(s)]]:
                            print('This student is already on course. Please delete or add new one')
                            print('1 - Delete an old one', '2 - Create a new one', sep='\n')
                            r = input()
                            if r == '1':
                                self.delete_student()
                            elif r == '2':
                                self.add_student()
                        else:
                            self.storage[course[int(s)]].append(student)
                            print('Student was successfully added')
                    else:
                        print('There is no such course. Add please one')
                    break
                else:
                    print('No such option. Write the page or choose the course!')
                    break
        else:
            print('There are no courses. Please add at least one.')
        self.run()

    def courses_list(self):
        print('Listing courses')
        if not self.storage:
            print('There are no records. Add please one at least')
        else:
            print(*FileStorage().list_of_courses(self.storage), sep='\n')
        self.run()

    def courses_lists(self):
        c = 1
        course_list = {}
        for i in self.storage.keys():
            course_list[c] = i
            c += 1
        return course_list

    def delete_course(self):
        list1 = self.courses_lists()
        [print(f'{key} - {value}') for key, value in list1.items()]
        num_of_course = input('Choose which one of course you would like to delete:\n')
        del self.storage[list1[int(num_of_course)]]
        print('The course was deleted successfully.')
        self.run()

    def delete_student(self):
        list2 = self.courses_lists()
        [print(f'{key} - {value}') for key, value in list2.items()]
        num_of_course1 = input('Choose the course from what you would like to delete a student:\n')
        student_list1 = self.storage[list2[int(num_of_course1)]]
        c = 1
        stud_list = {}
        for i in student_list1:
            stud_list[c] = i
            c += 1
        [print(f'{key} - first_name: {value["first_name"]}, last_name: {value["last_name"]}')
         for key, value in stud_list.items()]
        stud = input('Which student you would like to delete:\n')
        try:
            student_list1.remove(stud_list[int(stud)])
            self.storage[list2[int(num_of_course1)]] = student_list1
            print('The record was deleted successfully')
        except:
            print('There is no such number of student. Try again')
        self.run()

    def __exit__(self):
        FileStorage.save_changes(self.path, self.storage)
        print('Thank you for your changes')

    def run(self):
        print(*self.menu_items, sep='\n')
        action = input('Choose menu item: ')
        if action == '1':
            self.add_course()
        elif action == '2':
            self.courses_list()
        elif action == '3':
            self.add_student()
        elif action == '4':
            print('What would you like to delete?')
            print('1 - Course', '2 - Student', sep='\n')
            choose = input()
            if choose == '1':
                self.delete_course()
            elif choose == '2':
                self.delete_student()
        elif action == '5':
            self.__exit__()
        else:
            print('No such menu item. Try again')
            self.run()


if __name__ == '__main__':
    file_path = 'file.txt'
    app = App(FileStorage.load_from_file(file_path))
    app.run()
