

import sys
import os
import pickle
BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录

class Student:
    operate_lst = [('查看可选课程', 'show_courses'), ('选择课程', 'select_course'), ('查看所选课程', 'show_selected_course'),
                   ('退出', 'exit')]
    def __init__(self, name):
        self.name = name
        self.courses = []
    def show_courses(self):
        '''查看可选课程'''
        print('课程信息如下 ： ')
        course_obj_lst = []
        with open(os.path.join(BASE_DIR, 'db', 'course_info'), 'rb') as f:
            num = 0
            while True:
                try:
                    num += 1
                    course_obj = pickle.load(f)
                    course_obj_lst.append(course_obj)
                    print('\t', num, course_obj.name, course_obj.price, course_obj.period)
                except EOFError:
                    break
        print('')
        return course_obj_lst
    def select_course(self):
        '''选择课程'''
        print('选择课程')
        course_obj_lst = self.show_courses()
        course_num = input('输入选择课程的序号： ').strip()
        if course_num.isdigit():
            course_num = int(course_num)
            if course_num in range(len(course_obj_lst) + 1):
                choose_num = course_obj_lst.pop(course_num - 1)
                self.courses.append(choose_num)
            print('%s 课程选择成功' % choose_num.name)
        with open(os.path.join(BASE_DIR, 'db', 'student_info'), 'rb') as f, \
            open(os.path.join(BASE_DIR, 'db', 'student_info_new'), 'wb') as f2:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if stu_obj.name == self.name:
                        pickle.dump(self, f2)
                    else:
                        pickle.dump(stu_obj, f2)
                except EOFError:
                    break
        os.remove(os.path.join(BASE_DIR, 'db', 'student_info'))
        os.rename(os.path.join(BASE_DIR, 'db', 'student_info_new'), os.path.join(BASE_DIR, 'db', 'student_info'))

    def show_selected_course(self):
        '''查看选择的课程'''
        # with open(os.path.join(BASE_DIR, 'db', 'student_info'), 'rb') as f:
        #     while True:
        #         try:
        #             stu_obj = pickle.load(f)
        #             if self.name == stu_obj.name:
        #                 for index, item in enumerate(stu_obj.courses, 1):
        #                     print(index, item.name, item.price, item.period)
        #         except EOFError:
        #             break
        # print()

        print('选课情况如下 ： ')
        for num, course_obj in enumerate(self.courses, 1):
            print('\t', num, course_obj.name, course_obj.price, course_obj.period)
        print()

    def exit(self):
        '''退出'''
        sys.exit('拜拜了您嘞！')

    @classmethod
    def get_obj(cls, name):
        with open(os.path.join(BASE_DIR, 'db', 'student_info'), 'rb') as f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if stu_obj.name == name:
                        return stu_obj
                except EOFError:
                    break

class Manager:
    operate_lst = [('创建课程', 'create_course'), ('创建学生', 'create_student'), ('查看可选课程', 'show_courses'),
                ('查看所有学生', 'show_students'), ('查看所有学生选课情况', 'show_students_courses'),
                ('退出', 'exit')]
    def __init__(self, name):
        self.name = name
    def create_course(self):
        '''创建课程'''
        course_name = input('课程名 ：')
        course_price = int(input('课程价格 ：'))
        course_period = input('课程周期：')
        course_obj = Course(course_name, course_price, course_period)
        with open(os.path.join(BASE_DIR, 'db', 'course_info'), 'ab') as f:
            pickle.dump(course_obj, f)
        print('\033[0;32m课程创建成功：%s %s %s \033[0m' % (course_obj.name, course_obj.price, course_obj.period))
    def create_student(self):
        '''创建学生'''
        stu_name = input('学生姓名 ： ')
        stu_pwd = input('学生密码 ： ')
        with open(os.path.join(BASE_DIR, 'db', 'userinfo'), 'a') as f:
            f.write('%s|%s|%s\n' % (stu_name, stu_pwd, 'Student'))
        stu_obj = Student(stu_name)
        with open(os.path.join(BASE_DIR, 'db', 'student_info'), 'ab') as f:
            pickle.dump(stu_obj, f)
        print('\033[0;32m学员账号创建成功：%s 初始密码 ：%s\033[0m' % (stu_obj.name, stu_pwd))
    def show_courses(self):
        '''查看可选课程'''
        print('可选课程如下:')
        with open(os.path.join(BASE_DIR, 'db', 'course_info'), 'rb') as f:
            num = 0
            while True:
                try:
                    num += 1
                    course_obj = pickle.load(f)
                    print('\t', num, course_obj.name, course_obj.price, course_obj.period)
                except EOFError:
                    break
        print('')
    def show_students(self):
        '''查看所有学生'''
        print('学生如下 ： ')
        with open(os.path.join(BASE_DIR, 'db', 'student_info'), 'rb') as f:
            num = 0
            while True:
                try:
                    num += 1
                    stu_obj = pickle.load(f)
                    print(num, stu_obj.name)
                except EOFError:
                    break
            print('')

    def show_students_courses(self):
        '''查看所有学生选课情况'''
        with open(os.path.join(BASE_DIR, 'db', 'student_info'), 'rb') as f:
            num = 0
            while True:
                try:
                    num += 1
                    stu_obj = pickle.load(f)
                    print(num, stu_obj.name, stu_obj.courses)
                except EOFError:
                    break
        print()
    def exit(self):
        '''退出'''
        sys.exit('拜拜了您嘞！')

    @classmethod
    def get_obj(cls, name):
        return Manager(name)

class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period
    def __repr__(self):
        return self.name
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
            obj = cls.get_obj(ret['name'])  # 调用类方法返回文件中已存在的对象
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

