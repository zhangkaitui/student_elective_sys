

# 7.3.1
# class Student:
#     def __init__(self, name):
#         self.name = name
#
# class Manager:
#     def __init__(self, name):
#         self.name = name
#
# class Course:
#     def __init__(self, name, price, period):
#         self.name = name
#         self.price = price
#         self.period = period


# 7.3.2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.courses = []
#     def show_courses(self):
#         '''查看所有课程'''
#         pass
#     def select_course(self):
#         '''选择课程'''
#         pass
#     def show_selected_course(self):
#         '''查看选择的课程'''
#         pass
#     def exit(self):
#         '''退出'''
#         pass
#
# class Manager:
#     def __init__(self, name):
#         self.name = name
#     def create_course(self):
#         '''创建课程'''
#         pass
#     def create_student(self):
#         '''创建学生'''
#         pass
#     def show_courses(self):
#         '''查看所有课程'''
#         pass
#     def show_students(self):
#         '''查看所有学生'''
#     def show_students_courses(self):
#         '''查看所有学生选课情况'''
#         pass
#     def exit(self):
#         '''退出'''
#         pass
#
# class Course:
#     def __init__(self, name, price, period):
#         self.name = name
#         self.price = price
#         self.period = period





# 7.3.3

# import os
# BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录
#
# def main():
#     '''程序入口'''
#     usr = input('username:').strip()
#     pwd = input('password:').strip()
#     dic = {}
#     with open(os.path.join(BASE_DIR, 'db', 'userinfo')) as f:
#         for line in f:
#             username, password, ident = line.strip().split('|')
#             if username == usr and password == pwd:
#                 dic.update({'name': usr, 'identify': ident, 'auth': True})
#                 break
#         else:
#             dic['auth'] = False
#     print(dic)
#     if dic['auth'] == True:
#         print('login successful')
#         pass  #  拿到身份之后就可以做些具体的操作了，这里稍后实现
#     else:
#         print('login error')
#
# if __name__ == '__main__':
#     main()
#
# '''
# username:alex
# password:3714
# login successful
# '''



# 7.3.3


# import os
# BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录
#
# def login():
#     '''登录逻辑,此处是用了单次登录验证，你也可以根据自己的需求改成三次登录失败才返回False'''
#     usr = input('username:').strip()
#     pwd = input('password:').strip()
#     with open(os.path.join(BASE_DIR, 'db', 'userinfo')) as f:
#         for line in f:
#             username, password, ident = line.strip().split('|')
#             if username == usr and password == pwd:
#                 return {'name': usr, 'identify': ident, 'auth': True}
#
#         else:
#             return {'name': usr, 'identify': ident, 'auth': False}
#
# def main():
#     '''程序入口'''
#
#     print('\033[0;32m欢迎使用学生选课系统\033[0m')
#     ret = login()
#     if ret['auth']:
#         print('\033[0;32m登录成功，欢迎%s，您的身份是%s\033[0m' % (ret['name'], ret['identify']))
#         pass  #  拿到身份之后就可以做些具体的操作了，这里稍后实现
#     else:
#         print('\033[0;31m%s登录失败\033[0m' % ret['name'])
#
# if __name__ == '__main__':
#     main()
# '''
# 欢迎使用学生选课系统
# username:alex
# password:3714
# 登录成功，欢迎alex，您的身份是Manager
# '''


# 7.3.4

# import os
# BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录
#
# class Student:
#     operate_lst = ['show_courses', 'select_course', 'show_selected_course', 'exit']
#     def __init__(self, name):
#         self.name = name
#         self.courses = []
#     def show_courses(self):
#         '''查看所有课程'''
#         print('查看所有课程')
#     def selected_course(self):
#         '''选择课程'''
#         print('选择课程')
#     def show_selected_course(self):
#         '''查看选择的课程'''
#         print('查看选择的课程')
#     def exit(self):
#         '''退出'''
#         print('退出')
#
# class Manager:
#     operate_lst = ['create_course', 'create_student', 'show_courses', 'show_students', 'show_students_courses', 'exit']
#     def __init__(self, name):
#         self.name = name
#     def create_course(self):
#         '''创建课程'''
#         print('创建课程')
#     def create_student(self):
#         '''创建学生'''
#         print('创建学生')
#     def show_courses(self):
#         '''查看所有课程'''
#         print('查看所有课程')
#     def show_students(self):
#         '''查看所有学生'''
#         print('查看所有学生')
#     def show_students_courses(self):
#         '''查看所有学生选课情况'''
#         print('查看所有学生选课情况')
#     def exit(self):
#         '''退出'''
#         print('退出')
#
# class Course:
#     def __init__(self, name, price, period):
#         self.name = name
#         self.price = price
#         self.period = period
#
# def login():
#     '''登录逻辑,此处是用了单次登录验证，你也可以根据自己的需求改成三次登录失败才返回False'''
#     usr = input('username:').strip()
#     pwd = input('password:').strip()
#     with open(os.path.join(BASE_DIR, 'db', 'userinfo')) as f:
#         for line in f:
#             username, password, ident = line.strip().split('|')
#             if username == usr and password == pwd:
#                 return {'name': usr, 'identify': ident, 'auth': True}
#
#         else:
#             return {'name': usr, 'identify': ident, 'auth': False}
#
# def main():
#     '''程序入口'''
#
#     print('\033[0;32m欢迎使用学生选课系统\033[0m')
#     ret = login()
#     if ret['auth']:
#         print('\033[0;32m登录成功，欢迎%s，您的身份是%s\033[0m' % (ret['name'], ret['identify']))
#         if ret['identify'] == 'Manager':
#             obj = Manager(ret['name'])
#             for num, opt in enumerate(Manager.operate_lst, 1):
#                 print(num, opt)
#             while True:
#                 inp = int(input('请选择您要做的操作: '))
#                 if inp == 1:
#                     obj.create_course()
#                 elif inp == 2:
#                     obj.create_student()
#                 elif inp == 3:
#                     obj.show_courses()
#                 elif inp == 4:
#                     obj.show_students()
#                 elif inp == 5:
#                     obj.show_students_courses()
#                 elif inp == 6:
#                     obj.exit()
#         elif ret['identify'] == 'Student':
#             stu_obj = Student(ret['name'])
#             for num, opt in enumerate(Student.operate_lst, 1):
#                 print(num, opt)
#             while True:
#                 inp = int(input('请选择您要做的操作: '))
#                 if inp == 1:
#                     stu_obj.show_courses()
#                 elif inp == 2:
#                     stu_obj.selected_course()
#                 elif inp == 3:
#                     stu_obj.show_selected_course()
#                 elif inp == 4:
#                     stu_obj.exit()
#     else:
#         print('\033[0;31m%s登录失败\033[0m' % ret['name'])
#
# if __name__ == '__main__':
#     main()


# 7.3.5
# import sys
# import os
# BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录
#
# class Student:
#     operate_lst = ['show_courses', 'select_course', 'show_selected_course', 'exit']
#     def __init__(self, name):
#         self.name = name
#         self.courses = []
#     def show_courses(self):
#         '''查看所有课程'''
#         print('查看所有课程')
#     def selected_course(self):
#         '''选择课程'''
#         print('选择课程')
#     def show_selected_course(self):
#         '''查看选择的课程'''
#         print('查看选择的课程')
#     def exit(self):
#         '''退出'''
#         print('退出')
#
# class Manager:
#     operate_lst = ['create_course', 'create_student', 'show_courses', 'show_students', 'show_students_courses', 'exit']
#     def __init__(self, name):
#         self.name = name
#     def create_course(self):
#         '''创建课程'''
#         print('创建课程')
#     def create_student(self):
#         '''创建学生'''
#         print('创建学生')
#     def show_courses(self):
#         '''查看所有课程'''
#         print('查看所有课程')
#     def show_students(self):
#         '''查看所有学生'''
#         print('查看所有学生')
#     def show_students_courses(self):
#         '''查看所有学生选课情况'''
#         print('查看所有学生选课情况')
#     def exit(self):
#         '''退出'''
#         print('退出')
#
# class Course:
#     def __init__(self, name, price, period):
#         self.name = name
#         self.price = price
#         self.period = period
#
# def login():
#     '''登录逻辑,此处是用了单次登录验证，你也可以根据自己的需求改成三次登录失败才返回False'''
#     usr = input('username:').strip()
#     pwd = input('password:').strip()
#     with open(os.path.join(BASE_DIR, 'db', 'userinfo')) as f:
#         for line in f:
#             username, password, ident = line.strip().split('|')
#             if username == usr and password == pwd:
#                 return {'name': usr, 'identify': ident, 'auth': True}
#
#         else:
#             return {'name': usr, 'identify': ident, 'auth': False}
#
# def main():
#     '''程序入口'''
#
#     print('\033[0;32m欢迎使用学生选课系统\033[0m')
#     ret = login()
#     if ret['auth']:
#         print('\033[0;32m登录成功，欢迎%s，您的身份是%s\033[0m' % (ret['name'], ret['identify']))
#         if hasattr(sys.modules[__name__], ret['identify']):
#             cls = getattr(sys.modules[__name__], ret['identify'])
#             obj = cls(ret['name'])
#             while True:
#                 for num, opt in enumerate(cls.operate_lst, 1):
#                     print(num, opt)
#                 inp = int(input('请选择您要做的操作 ： '))
#                 if inp in range(1, len(cls.operate_lst) + 1):
#                     if hasattr(obj, cls.operate_lst[inp - 1]):
#                         getattr(obj, cls.operate_lst[inp - 1])()
#                 else:
#                     print('\033[31m您选择的操作不存在\033[0m')
#     else:
#         print('\033[0;31m%s登录失败\033[0m' % ret['name'])
#
# if __name__ == '__main__':
#     main()

# 7.3.5优化

import sys
import os
BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录

class Student:
    operate_lst = [('查看可选课程', 'show_courses'), ('选择课程', 'select_course'), ('查看所选课程', 'show_selected_course'),
                   ('退出', 'exit')]
    def __init__(self, name):
        self.name = name
        self.courses = []
    def show_courses(self):
        '''查看所有课程'''
        print('查看所有课程')
    def selected_course(self):
        '''选择课程'''
        print('选择课程')
    def show_selected_course(self):
        '''查看选择的课程'''
        print('查看选择的课程')
    def exit(self):
        '''退出'''
        print('退出')

class Manager:
    operate_lst = [('创建课程', 'create_course'), ('创建学生', 'create_student'), ('查看可选课程', 'show_courses'),
                ('查看所有学生', 'show_students'), ('查看所有学生选课情况', 'show_students_courses'),
                ('退出', 'exit')]
    def __init__(self, name):
        self.name = name
    def create_course(self):
        '''创建课程'''
        print('创建课程')
    def create_student(self):
        '''创建学生'''
        print('创建学生')
    def show_courses(self):
        '''查看所有课程'''
        print('查看所有课程')
    def show_students(self):
        '''查看所有学生'''
        print('查看所有学生')
    def show_students_courses(self):
        '''查看所有学生选课情况'''
        print('查看所有学生选课情况')
    def exit(self):
        '''退出'''
        print('退出')

class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

def login():
    '''登录逻辑,此处是用了单次登录验证，你也可以根据自己的需求改成三次登录失败才返回False'''
    usr = input('username:').strip()
    pwd = input('password:').strip()
    with open(os.path.join(BASE_DIR, 'db', 'userinfo')) as f:
        for line in f:
            username, password, ident = line.strip().split('|')
            if username == usr and password == pwd:
                return {'name': usr, 'identify': ident, 'auth': True}

        else:
            return {'name': usr, 'identify': ident, 'auth': False}

def main():
    '''程序入口'''

    print('\033[0;32m欢迎使用学生选课系统\033[0m')
    ret = login()
    if ret['auth']:
        print('\033[0;32m登录成功，欢迎%s，您的身份是%s\033[0m' % (ret['name'], ret['identify']))
        if hasattr(sys.modules[__name__], ret['identify']):
            cls = getattr(sys.modules[__name__], ret['identify'])
            obj = cls(ret['name'])
            while True:
                for num, opt in enumerate(cls.operate_lst, 1):
                    print(num, opt[0])
                inp = int(input('请选择您要做的操作 ： '))
                if inp in range(1, len(cls.operate_lst) + 1):
                    if hasattr(obj, cls.operate_lst[inp - 1][1]):
                        getattr(obj, cls.operate_lst[inp - 1][1])()
                else:
                    print('\033[31m您选择的操作不存在\033[0m')
    else:
        print('\033[0;31m%s登录失败\033[0m' % ret['name'])

if __name__ == '__main__':
    main()

