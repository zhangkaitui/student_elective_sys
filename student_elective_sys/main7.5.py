import os
import sys
import pickle
from conf import settings


class Person:
    def show_courses(self):
        '''查看可选课程'''
        print('可选课程如下 ： ')
        course_obj_lst = []
        for index, item in enumerate(self.load_obj(settings.COURSE_INFO, 'rb'), 1):
            print('\t', index, item.name, item.price, item.period)
            course_obj_lst.append(item)
        return course_obj_lst

    def exit(self):
        '''退出'''
        sys.exit('拜拜了您嘞！')

    def dump_obj(self, obj=None, file_path=None, mode=None, content=None):
        '''序列化对象到文件'''
        with open(file_path, mode) as f:
            if content:
                f.write(content)
            else:
                pickle.dump(obj, f)

    def load_obj(self, file_path=None, mode=None):
        '''将对象从文件中反序列化回来'''
        with open(file_path, mode) as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except EOFError:
                    break


class Student(Person):
    operate_lst = [('查看可选课程', 'show_courses'), ('选择课程', 'select_course'), ('查看所选课程', 'show_selected_course'),
                   ('退出', 'exit')]

    def __init__(self, name):
        self.name = name
        self.courses = []

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
                print('%s 课程选择成功\n' % choose_num.name)
        with open(settings.STUDENT_INFO_TEMP, 'wb') as f:
            for item in self.load_obj(file_path=settings.STUDENT_INFO, mode='rb'):
                if item.name == self.name:
                    pickle.dump(self, f)
                else:
                    pickle.dump(item, f)
        os.remove(settings.STUDENT_INFO)
        os.rename(settings.STUDENT_INFO_TEMP, settings.STUDENT_INFO)

    def show_selected_course(self):
        '''查看所选课程'''
        print('选课情况如下 ： ')
        for num, course_obj in enumerate(self.courses, 1):
            print('\t', num, course_obj.name, course_obj.price, course_obj.period)

    @classmethod
    def get_obj(cls, name):
        for item in Person().load_obj(settings.STUDENT_INFO, 'rb'):
            if name == item.name:
                return item


class Manager(Person):
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
        self.dump_obj(obj=course_obj, file_path=settings.COURSE_INFO, mode='ab')
        print('\033[0;32m课程创建成功：%s %s %s \033[0m' % (course_obj.name, course_obj.price, course_obj.period))

    def create_student(self):
        '''创建学生'''
        stu_name = input('学生姓名 ： ')
        stu_pwd = input('学生密码 ： ')
        content = '%s|%s|%s\n' % (stu_name, stu_pwd, 'Student')
        self.dump_obj(obj=None, file_path=settings.USER_INFO, mode='a', content=content)
        stu_obj = Student(stu_name)
        self.dump_obj(obj=stu_obj, file_path=settings.STUDENT_INFO, mode='ab')
        print('\033[0;32m学员账号创建成功：%s 初始密码 ：%s\033[0m' % (stu_obj.name, stu_pwd))

    def show_students(self):
        '''查看所有学生'''
        print('学生如下 ： ')
        for index, item in enumerate(self.load_obj(file_path=settings.STUDENT_INFO, mode='rb'), 1):
            print('\t', index, item.name)

    def show_students_courses(self):
        '''查看所有学生选课情况'''
        print('学生选课情况如下 ： ')
        for index, item in enumerate(self.load_obj(file_path=settings.STUDENT_INFO, mode='rb'), 1):
            print('\t', index, item.name, item.courses)

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
    usr = input('username : ')
    pwd = input('password : ')
    with open(settings.USER_INFO) as f:
        for line in f:
            username, password, ident = line.strip().split('|')
            if username == usr and password == pwd:
                return {'name': username, 'identify': ident, 'auth': True}
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
                print(chr(42), num, opt[0])
            inp = int(input('请选择您要做的操作:'))
            if inp in range(1, len(cls.operate_lst) + 1):
                if hasattr(obj, cls.operate_lst[inp - 1][1]):
                    getattr(obj, cls.operate_lst[inp - 1][1])()
            else:
                print('\033[31m您选择的操作不存在\033[0m')
    else:
        print('\033[0;31m%s登录失败\033[0m' % ret['name'])

if __name__ == '__main__':
    main()

'''
欢迎使用学生选课系统
username : alex
password : 3714
登录成功，欢迎alex，您的身份是Manager
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作 ： 1
课程名 ：python
课程价格 ：15000
课程周期：6
课程创建成功：python 15000 6 
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作 ： 2
学生姓名 ： oldboy
学生密码 ： 666
学员账号创建成功：oldboy 初始密码 ：666
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作 ： 3
可选课程如下 ： 
	 1 python 15000 6
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作 ： 4
学生如下 ： 
	 1 oldboy
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作 ： 5
学生选课情况如下 ： 
	 1 oldboy []
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作 ： 6
拜拜了您嘞！
'''

'''
欢迎使用学生选课系统
username : oldboy
password : 666
登录成功，欢迎oldboy，您的身份是Student
* 1 查看可选课程
* 2 选择课程
* 3 查看所选课程
* 4 退出
请选择您要做的操作 ： 1
可选课程如下 ： 
	 1 python 15000 6
	 2 java 14000 6
* 1 查看可选课程
* 2 选择课程
* 3 查看所选课程
* 4 退出
请选择您要做的操作 ： 2
选择课程
可选课程如下 ： 
	 1 python 15000 6
	 2 java 14000 6
输入选择课程的序号： 2
java 课程选择成功

* 1 查看可选课程
* 2 选择课程
* 3 查看所选课程
* 4 退出
请选择您要做的操作 ： 3
选课情况如下 ： 
	 1 python 15000 6
	 2 java 14000 6
* 1 查看可选课程
* 2 选择课程
* 3 查看所选课程
* 4 退出
请选择您要做的操作 ： 4
拜拜了您嘞！
'''