class FileStorage:
    courses_new = []

    @staticmethod
    def load_from_file(path):
        try:
            with open(path, 'r') as opened_file:
                text = opened_file.readlines()
                return path, text
        except:
            return path, []

    def course(self, name):
        self.courses_new.append(name)

    @staticmethod
    def list_of_courses(courses):
        res1 = [f'Course(name={i.strip()})' for i in courses]
        return res1

    @staticmethod
    def save_changes(path, text):
        with open(path, 'w') as file:
            for i in text:
                file.write(i)


class App:
    menu_items = ['1 - Add course name', '2 - Show all the courses', '3 - Exit']


    def __init__(self, storage):
        self.path = storage[0]
        self.storage = storage[1]


    def add_course(self):
        print('Adding course')
        course_name = input('Enter course name: ')
        if course_name:
            name_obj = FileStorage()
            name_obj.course(course_name)
            print('Course added successfully')
        else:
            print('Course name was not written. Tre again')
        return self.run()

    def courses_list(self):
        print('Listing courses')
        added_courses = FileStorage().courses_new + self.storage
        res1 = FileStorage()
        if not added_courses:
            print('There are no records. Added please')
        else:
            print(*res1.list_of_courses(added_courses), sep='\n')
        self.run()

    def __exit__(self):
        added_courses1 = FileStorage().courses_new
        if added_courses1:
            added_courses1 = [i + '\n' for i in added_courses1]
        text1 = added_courses1 + self.storage
        FileStorage.save_changes(self.path, text1)
        print('Thank you for your changes')

    def run(self):
        print(*self.menu_items, sep='\n')
        action = input('Choose menu item: ')
        if action == '1':
            self.add_course()
        elif action == '2':
            self.courses_list()
        elif action == '3':
            self.__exit__()
        else:
            print('No such menu item. Try again')
            self.run()


if __name__ == '__main__':
    file_path = input('Enter storage path: ')
    app = App(FileStorage.load_from_file(file_path))
    app.run()
