# 第7章 作业，选课系统

当你看到这的时候，恭喜你，Python重要的基础课程已经学习完毕。而面向对象部分则是基础课程中的一个重要转折点。从面向对象开始，你要试着从面向对象的思想出发，来编写程序，尤其是将来开发一些功能复杂的系统。而本章的系统则是精心设计而成的。我们学过的内容都能在该系统中体现。所以，要用心完成本系统。

在完成系统的时候，请务必回顾之前章节所学，让我们在实现系统的过程中更加得心应手。

## 7.1 功能概述

“学生选课系统”，顾名思义，本系统必须实现的需求就是选课。

## 7.2 需求分析

既然我们主要实现的功能是“选课”，那么我们要实现的核心逻辑都要围着选课展开。

### 7.2.1 角色设计

首先我们来思考：学生选课，那么学生由谁来创建？课程由谁来创建？学生能否创建课程？很明显，从我们现实角度来说，学生只能选择课程而不能创建课程！那么，课程应该由那个“谁”来创建。而学生也不能是凭空而来的。这里我们也让那个“谁”来创建学生。所以，我们在这里可以确定三个角色：

- 可以选择课程的——学生
- 可供学生选择的——课程
- 可以创建学生和课程的那个“谁”——管理员

### 7.2.2 功能设计

这里考虑到大家都是初学者，所以，尽量的选择一些简单的功能实现。

- 登录，管理员和学生都可以登录，并且登录后可以自动区分身份。
- 选课，学生可以自由的浏览课程信息，并挑选课程。
- 信息的创建，无论是学生信息还是课程信息，或是其他的信息，都由管理员创建。
- 查看选课情况，学生可以查看自己的选课情况，而管理员可以查看所有的学生信息(包括选课情况)。

### 7.2.3 流程设计

有了角色和基本的功能，那么整个系统该是怎么样的一个呈现？先干什么后干什么？就是我们要考虑的事情了。

这个系统的流程可以是这样的：

- 登录，用户输入用户名和密码。
- 判断身份，在登录成功的时候，就应该可以直接判断出登录用户的身份，是学生还是管理员。

对于学生用户来说，登录之后有四个功能选项：

- 查看可选课程
- 选择课程
- 查看所选择的课程
- 退出程序

对于管理员用户来说，管理员除了要是实现基本的查看功能，还有很多创建工作要做。

- 创建课程
- 创建学生信息(创建学生账号)
- 查看可选课程信息
- 查看所有学生
- 查看所有学生的选课情况
- 退出程序

### 7.2.4 程序设计

对于相对的复杂的功能实现，我们优先选择使用面向对象编程，而选择面向对象编程之后，就要时刻思考如何设计类和对象的关系，让程序结构更加清晰明朗。

前面的分析中，我们需要实现三个角色。那么可以对应用三个类来实现。根据角色的不同，我们有针对性的为类设计属性和方法。

- 课程类，课程类并没有什么动作，只有一些必要的属性。

  属性：课程名称、价格、周期。

  方法：暂无

- 学生，学生就要有必要的属性和方法了。

  属性：姓名、所选课程。

  方法：查看可选课程、选择课程、查看选择的课程、退出程序。

- 管理员，管理员的属性可以仅有一个姓名就好了，其他的就是方法设计了。

  属性：姓名。

  方法：创建课程、创建学生信息(创建学生账号)、查看可选课程、查看所有学生、查看所有学生的选课情况、退出程序。

这里需要说明的是，课程属性缺少一个任教老师属性，但仔细分析你会发现，老师也是一个角色，为了不增加难度，这里课程属性这里，不再添加老师属性，但你可以当成一个升级功能来拓展实现。

### 7.2.5 流程图

根据上述分析，我们将主要功能汇总成流程图。

![7.1](https://github.com/zhangkaitui/student_elective_sys/tree/master/img/7.1.bmp)

上述流程图，晰的展示了程序的执行流程及具体的功能。所以，为了更方便系统的实现，请画出你的流程图。

### 7.2.6 数据库设计

现在，不得不考虑一个尴尬的事情了，当我们创建完学生或课程信息之后，存在哪？是的，目前我们没有学习数据库。所以，暂时我们只能想办法把数据存储到普通文件中。那么该怎么构建文件呢，我们在后面会详细说明。

## 7.3 搭建框架

首先，在展开讲解之前，让我们建立这样一个目录：

```python
student_electiive_sys/
	├─ db/
	│	├─ course_info		# 存放课程信息
	│	├─ student_info		# 存放学生信息
	│	└─ user_info		# 存放用户信息
	└─ main.py				# 主逻辑文件
```

在`student_elective_sys`目录下有db目录，该目录内存放着所有的数据文件。我们只需要把db目录创建出来。然后再把`userinfo`文件创建出来即可，内容稍后填充。其他的数据文件我们无需手动创建，程序在运行中自动创建。而与db目录同级有一个main文件。该`main.py`文件为我们的主逻辑文件。

### 7.3.1 根据角色信息创建类

按照上述分析，首先我们在`main.py`中先完成三个类的创建。

```python
class Student:
    def __init__(self, name):
        self.name = name
class Manager:
    def __init__(self, name):
        self.name = name
class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period
```

上例中，我们根据角色的属性创建三个类。其中需要说明的是，学生角色的课程信息之所以定义成一个空的列表，是因为考虑到一个学生可能选择多门课程。

### 7.3.2  完善角色信息

现在，各角色已经有了属性信息，还有方法需要完善。

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    def show_courses(self):
        '''查看可选课程'''
        pass
    def select_course(self):
        '''选择课程'''
        pass
    def show_selected_course(self):
        '''查看选择的课程'''
        pass
    def exit(self):
        '''退出'''
        pass

class Manager:
    def __init__(self, name):
        self.name = name
    def create_course(self):
        '''创建课程'''
        pass
    def create_student(self):
        '''创建学生'''
        pass
    def show_courses(self):
        '''查看可选课程'''
        pass
    def show_students(self):
        '''查看所有学生'''
    def show_students_courses(self):
        '''查看所有学生选课情况'''
        pass
    def exit(self):
        '''退出'''
        pass

class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period
```

上例中，每个方法对应每个角色所要实现的方法，这样一个整体的角色的框架搭建完毕，现在角色的属性和方法已经暂时告一段落，让我们进入下一阶段的代码设计。

### 7.3.3   设计程序的入口

现在，让我们再看一眼流程图，角色框架已经搭建完毕。那么从上到下开始执行，就要着手设计程序的入口，登录功能的实现。以及如何完成登录后完成自动身份识别。

在`main.py`中，首先添加程序的入口函数。但此时要思考，这个入口函数都是要干些什么？

当入口函数开始执行后，首先要进行登录认证，认证成功后才能根据身份判断来让不同的角色执行不同的功能。

既然要实现用户认证，首先数据文件要手动填充一下(这里你后期可以写个注册函数来实现)，来两个用户名和密码。

```python
# db目录中的userinfo文件，填充内容如下  
oldboy|666|Student
alex|3714|Manager
```

如上例所示，在db目录中的`userinfo`文件中，我们手动创建两个用户`oldboy`和`alex`。然后是密码和该用户的身份，并且中间以“|”分割，需要说明的是，这个“|”可以是任意的，为了就是后面方便取值。

接下来，让我们开始在main.py中实现入口函数main函数。

```python
import os
BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录
def main():
    '''程序入口'''
    usr = input('username:').strip()
    pwd = input('password:').strip()
    dic = {}
    with open(os.path.join(BASE_DIR, 'db', 'userinfo')) as f:
        for line in f:
            username, password, ident = line.strip().split('|')
            if username == usr and password == pwd:
                dic.update({'name': usr, 'identify': ident, 'auth': True})
                break
        else:
            dic['auth'] = False
    if dic['auth'] == True:
        print('login successful')
        pass  #  拿到身份之后就可以做些具体的操作了，这里稍后实现
    else:
        print('login error')
if __name__ == '__main__':
    main()
'''
username:alex
password:3714
login successful
'''
```

上例中，第1-2行，通过使用`os`模块，来获取当前文件的上一级路径并赋值给变量`BASE_DIR`，这一步是为了下面在第8行打开`userinfo`文件时，能使用`os.path.join`方法拼接出`userinfo`文件的路径。在第3行定义的`main`函数中，首先获取用户输入的用户名和密码(第5-6行)。接下来，第7行，定义一个字典，用来存储后面“可能”用到的数据，包括身份信息，用户信息，和认证状态。第8行打开`userinfo`文件。第9行使用for循环读取文件内容，在每次的for循环中，第10行，拿到的都是一行，在手动去除换行符后，得到的是`alex|3714|Manager`这样的字符串，我们再对这个字符串以`|`分割，就得到一个有三个元素的列表，再分别赋值给左侧的三个变量。第11行的if判断中，判断从数据文件中取的用户名和密码是否与用户输入的用户名和密码一致，是的话，将必要的数据添加到第7行定义的字典中，然后退出循环。如果if条件不成立，则进入下一次循环判断。如果for循环完毕，依然没有if条件成立，那么说明用户名或者密码输入有误。程序走第16行的else语句，用户认证失败。

程序继续往下执行，来到了第18行，如果之前的用户认证成功的话，说明登录成功，这里就可以根据身份来执行具体的操作了。否则，走第21行的else语句，表示登录认证失败。程序结束。

上例的main函数，虽然完成了基本需求，但学函数时说过，我们设计的函数应该尽可能的功能简洁，很明显，这里的main函数，既要做登录，又要根据身份来执行不同的功能。这显然不符合函数设计的思想。我们来试着优化这个main函数。

```python
import os
BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录
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
        pass  # 拿到身份之后就可以做些具体的操作了，这里稍后实现
    else:
        print('\033[0;31m%s登录失败\033[0m' % ret['name'])
if __name__ == '__main__':
    main()
'''
欢迎使用学生选课系统
username:alex
password:3714
登录成功，欢迎alex，您的身份是Manager
'''
```

上例中，我们把登录逻辑从`main`函数中摘出来，并用`login`函数来完成，这样`login`函数只做登录逻辑，登录成功则把一个带有认证成功的状态字典返回，否则返回认证失败的状态字典。

而`main`函数中，在第17行打印一行欢迎语句，需要说明的是，欢迎语句两边的`\033[0;32m`和`\033[0m`是一种控制台输出着色的一种小技巧。简要来说，控制台输出着色(控制前景色、字体颜色等)是将以`\033[0;32m`开头，以`\033[0m`结尾，中间内容显示不同的颜色来增加程序的友好性。只是上例代码演示中，无法显示着色后的代码。

main函数中，第18行，首先调用login函数进行用户认证判断，返回的字典赋值给变量ret，在第18-23行，通过`ret`字典中的`auth`键对应的`value`状态来判断登录是否成功，以及要做的具体操作。

现在，我们的入口函数及登录认证不知不觉间已经完成了。

### 7.3.4 实现入口函数最重要的功能

在上一小节中，我们完成了入口函数的功能拆分，并根据login函数的认证信息来判断是否登录成功。但在登录成功部分，我们并没有往下实现，现在，是时候实现了。

这里回想login函数在用户登录成功后，返回的字典，都有什么我们需要得数据，用户名、认证状态、身份。是的这三个都是必须的，根据认证状态来判断是否登录成功；用户名暂时在输出中使用了；接下来，就来该使用这个重要的身份了。

```python
import os
BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录
class Student:
    operate_lst = ['show_courses', 'select_course', 'show_selected_course', 'exit']
    def __init__(self, name):
        self.name = name
        self.courses = []
    def show_courses(self):
        '''查看可选课程'''
        print('查看可选课程')
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
    operate_lst = ['create_course', 'create_student', 'show_courses', 'show_students', 'show_students_courses', 'exit']
    def __init__(self, name):
        self.name = name
    def create_course(self):
        '''创建课程'''
        print('创建课程')
    def create_student(self):
        '''创建学生'''
        print('创建学生')
    def show_courses(self):
        '''查看可选课程'''
        print('查看可选课程')
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
        if ret['identify'] == 'Manager':
            obj = Manager(ret['name'])
            for num, opt in enumerate(Manager.operate_lst, 1):
                print(num, opt)
            while True:
                inp = int(input('请选择您要做的操作: '))
                if inp == 1:
                    obj.create_course()
                elif inp == 2:
                    obj.create_student()
                elif inp == 3:
                    obj.show_courses()
                elif inp == 4:
                    obj.show_students()
                elif inp == 5:
                    obj.show_students_courses()
                elif inp == 6:
                    obj.exit()
        elif ret['identify'] == 'Student':
            stu_obj = Student(ret['name'])
            for num, opt in enumerate(Student.operate_lst, 1):
                print(num, opt)
            while True:
                inp = int(input('请选择您要做的操作: '))
                if inp == 1:
                    stu_obj.show_courses()
                elif inp == 2:
                    stu_obj.selected_course()
                elif inp == 3:
                    stu_obj.show_selected_course()
                elif inp == 4:
                    stu_obj.exit()
    else:
        print('\033[0;31m%s登录失败\033[0m' % ret['name'])
if __name__ == '__main__':
    main()
```

上例中，首先我们在每个类中，添加了一个静态属性，也就是建立了一个列表，列表中的元素是这个类实例化的对象所能做的操作，也就是方法名。因为不同的类所能做的操作不同，所以，每个角色类中都必须实现一个独特的列表。然后具体的操作对应一个必须实现的方法，方法中暂时只是简单的打印一行内容，表明程序可以执行到这里，具体的实现还是后面完成。

`main`函数中，第78行，在`login`函数登录认证成功返回的字典中，`auth`键对应的`value`是从用户文件取出来的身份。

第64行的if判断身份如果是`Manager`，那么对应20行的`Manager`类就会实例化一个对象，实例化过程中第22行的`__init__`方法需要一个`name`参数，我们为这个参数传递一个由`login`函数返回的字典的`name`键对应的用户名，最后返回的对象赋值给obj(第65行)。第66-67行for循环利用`enumerate`函数展示该对象所能做的操作。在第68行的while循环中，当用户看到展示的操作时，只需要输入对应的序号就行(这里为了不增加代码复杂度，没有对输入做判断，你可以当成进阶需求完善)，如果输入的是`1`，就意味着用户要做`创建课程`的操作，那么使用对象直接调用对应的方法(第70-71行所示)。后面的elif判断同理。

在`main`函数中，如果此时登录的用户身份是学生。那么在登录成功后的具体操作中，根据身份判断是`Student`。那么，就执行第82行的elif判断并执行内部的代码。逻辑同`Manager`一致。

现在，通过上例代码所示，无论登录的用户是什么身份，只要登录成功，就能看到自己所能做的操作。并只能做这些操作。

我们来看下演示效果。

```python
'''
欢迎使用学生选课系统
username:oldboy
password:666
登录成功，欢迎oldboy，您的身份是Student
1 show_courses
2 select_course
3 show_selected_course
4 exit
请选择您要做的操作: 1
查看可选课程
请选择您要做的操作: 2
选择课程
请选择您要做的操作: 3
查看选择的课程
请选择您要做的操作: 4
退出
'''
```

通过上例的演示效果来看，程序执行流畅。

### 7.3.5 优化框架

此时框架大体搭建完毕，但还不够健壮和简洁。比如说，在`main`函数登录成功后，我们根据用户的身份设计了相同的逻辑，并辅以for循环和大量的if和elif判断，那么如果我们要添加新的需求，比如添加一个老师角色，校长角色等等，是不是还是同样的逻辑？只不过增加了一堆的if判断。这明显的造轮子的行为应该是杜绝的！我们的代码还需要优化！

- 存在问题一，代码冗余，可扩展性差

怎么优化呢？来思考这样的一个场景，我们在存储用户身份的时候，是不是刻意把身份存储成了该角色的类名一致的变量。

```python
# userinfo文件 
oldboy|666|Student  
alex|3714|Manager 
wusir|888|Teacher
# main.py
class Student: pass
class Manager: pass
class Teacher: pass
```

如上例所示，在`userinfo`文件中，目前我们只有学生和管理员两个角色，那么我们对应的在`main.py`中，就定义了两个类来示例话这两个角色。如果有一天出现新的需求，比如上例中的第4行所示，新增了一个老师角色。那么该老师在登录成功之前，代码都无需改变，就足以适应这种功能扩展，但是到了实现具体的操作的时候，我们就要增加完整的逻辑，并且是重复的逻辑，那就是如实现管理具体操作的逻辑一致，这就陷入了重复造轮子阶段。

那么如何避免重复造轮子呢？仔细观察上述的代码示例，从`userinfo`取出的身份是一个字符串类型的，而且与现有的角色类名一致。那么是不是可以用到反射？在获取到用户的身份信息后，在当前脚本中判断是否存在同名的类名，是的话，则实例化，然后执行for循环，再while循环让用户循环的执行可执行的操作？否则的，给予一些提示信息。这样是不是就省下很多的重复的代码了？说干就干！

```python
import sys
import os
BASE_DIR = os.path.dirname(__name__)  # # 以当前文件为起点，获取父级目录
class Student:
    operate_lst = ['show_courses', 'select_course', 'show_selected_course', 'exit']
    def __init__(self, name):
        self.name = name
        self.courses = []
    def show_courses(self):
        '''查看可选课程'''
        print('查看可选课程')
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
    operate_lst = ['create_course', 'create_student', 'show_courses', 'show_students', 'show_students_courses', 'exit']
    def __init__(self, name):
        self.name = name
    def create_course(self):
        '''创建课程'''
        print('创建课程')
    def create_student(self):
        '''创建学生'''
        print('创建学生')
    def show_courses(self):
        '''查看可选课程'''
        print('查看可选课程')
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
                    print(num, opt)
                inp = int(input('请选择您要做的操作 ： '))
                if inp in range(1, len(cls.operate_lst) + 1):
                    if hasattr(obj, cls.operate_lst[inp - 1]):
                        getattr(obj, cls.operate_lst[inp - 1])()
                else:
                    print('\033[31m您选择的操作不存在\033[0m')
    else:
        print('\033[0;31m%s登录失败\033[0m' % ret['name'])
if __name__ == '__main__':
    main()
```

上例中，当用户登录成功后，程序来到了第65-6行，首先`hasattr`判断当前模块中是否存在跟身份同名的字符串类名。`sys.modules[__name__]`是返回当前的文件的路径(sys模块已在第1行导入)。简单来说，`hasattr`就是判断整个脚本文件中是否有个跟身份匹配的字符串类型的可执行的类(对象)。如果有，那么第66行的`getattr`就拿到该对象并赋值给`cls`变量。然后第67行`cls`加括号并传递`name`参数，等于实例化该类，并将实例化对象返回并赋值给变量`obj`。在第68行的`while`循环中，首先利用`for`循环搭配`enumerate`函数循环该对象中的`operate_lst`属性(列表)，展示可操作的序号。在第71行获取用户选择的操作序号，由字符串类型强制转换成`int`类型(这里由于篇幅限制，不做输入的判断)。在第72行，判断用户输入的数字范围是否在展示的列表索范围内。如果不在则提示选择的操作不存在；如果在，那么在通过反射，在当前类中查找是否存在索引对应的方法。如果用户的身份是Manager，并且输入的是`1`，那么就意味着，用户再执行`create_course`的操作。如何让用户的输入和列表内的实际元素对应上呢？首先通过索引查找`cls.operate_lst`中对应的元素，因为序号的起始位置使用1开始的，而列表索引是从0开始的，所以要减去1，这样就取出来了，而对象`obj`有该方法。`hasattr`返回`True`。那么 第74行的`getattr`就可以执行该方法。

通过两次反射。第一次是在当前作用域中查找跟身份对应的类名，反射成功则类名加括号实例化一个对象。第二次反射是在用户输入操作的序号后，通过序号取出列表中的对应的元素。在当前对象中查找是否存在与元素同名的方法。有则执行该方法。

经过这两次反射逻辑，我们解决代码冗余问题，并且提高了代码的可扩展性。此时如果增加一个`Teacher`角色，只需要在`main.py`中实现一个`Teacher`类，然后创建一个可供操作的属性列表，再实现对应的方法即可。

- 程序的用户体验不好

上面的例子中，我们为了解决反射问题，在类的属性列表中，都是对应的方法名称。这样在for循环的展示中，一是暴露了代码，二是展示内容体验性不好，应该循环展示中文，而不是带下划线的英文(我们的系统默认面向国内用户)。用户不管你背后做了什么，但是在乎你展示的内容和操作是否简单。这里我们修改一些代码，来解决上述问题。

```python
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
        '''查看可选课程'''
        print('查看可选课程')
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
        '''查看可选课程'''
        print('查看可选课程')
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
```

上例中，我们在每个类的属性列表中，将每个具体的方法，起一个`昵称`，也就是要显示的中文，和具体的方法封装成一个元组。这样，在第80行的for循环中展示中文，也就是元组的索引0对应的元素，而在反射时，取元组索引1对应的元素(第83-84行)。

```python
'''
欢迎使用学生选课系统
username:alex
password:3714
登录成功，欢迎alex，您的身份是Manager
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 1
创建课程
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 2
创建学生
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 3
查看可选课程
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 4
查看所有学生
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 5
查看所有学生选课情况
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 6
退出
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 7
您选择的操作不存在
'''
```

通过巧妙的利用元组，使显示更加友好，而毫不影响执行过程。结果如上例演示的一样，达到我们的预期。

经过`如此这般`的优化后，系统更显灵活、代码更加简洁、提高了扩展性。

## 7.4 细节实现

上一小节中，我们已经完成了系统的整体搭建。现在我们来为框架填充具体的逻辑代码。

接下来，所有的代码示例，都默认是对应的角色登录，并选择了对应的操作。

### 7.4.1 管理员之创建课程信息

具体的功能实现应该从哪开始入手呢？首先我们从管理员角色开始入手，因为只有管理员才有创建学生及其他的创建权限。所以应该先把课程和学生这两个对象创建出来。方便后面的功能实现。

既然是创建课程，那么就要思考，创建课程都是需要哪些信息？比如为老男孩创建一门`Python`课程。那么课程信息应该包括课程名称、价格、周期这三个必要的属性。所以，在上述的示例中，我们创建好了课程类，却暂时没有用到，这里就应该把它用上了。

```python
# Manager类中的create_course方法  
class Manager:
    def create_course(self):
        '''创建课程'''
        course_name = input('课程名 ：')
        course_price = int(input('课程价格 ：'))
        course_period = input('课程周期：')
        course_obj = Course(course_name, course_price, course_period)
```

上例中，我们在`Manger`类中，完善`create_course`方法。第5-7行首先获取管理员输入的关于课程的信息。然后在第8行中，实例化`Course`类，并传递参数，拿到课程对象。

目前一切简单而又顺利，但是问题来了？我们虽然成功的创建了课程对象，那么该如何保存创建的课程对象呢？保存到内存中吗？程序结束就没了！那么就应该保存到文件中。那么要将一个对象保存到文件中，我们应该第一反应就是使用pickle模块来将对象保存到文件中。

```python
# Manager类中的create_course方法  
class Manager:
    def create_course(self):
        '''创建课程'''
        course_name = input('课程名 ：')
        course_price = int(input('课程价格 ：'))
        course_period = input('课程周期：')
        course_obj = Course(course_name, course_price, course_period)
        with open(os.path.join(BASE_DIR, 'db', 'course_info'), 'ab') as f:
            pickle.dump(course_obj, f)
        print('\033[0;32m课程创建成功：%s %s %s \033[0m' % (course_obj.name, course_obj.price, course_obj.period))
```

 如上例所示，在第9行，已追加的方式打开一个文件(追加的方式会检测文件是否存在，存在则追加，不存在则首先创建文件)，并将文件句柄赋值给`f`，需要注意的是，必须是`ab`模式，因为`pickle`将对象序列化为字节流，所以使用`ab`模式。在第10行，通过`pickle`模块将实例化的课程对象序列化到文件中。

```python
'''
欢迎使用学生选课系统
username:alex
password:3714
登录成功，欢迎alex，您的身份是Manager
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 1
课程名 ：python
课程价格 ：15000
课程周期：6
课程创建成功：python 15000 6 
'''
```

演示过程如上例所示。可以看到已经成功的将课程对象序列化到文件中了。

### 7.4.2 管理员之查看课程信息

创建完课程后，我们就可以着手实现查看课程的功能了。

```python
# Manager类中的show_courses方法  
class Manager:
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
```

上例中，在Manager类的`show_courses`方法中，首先在第5行打印提示信息。然后第6行以二进制的方式读`course_info`文件。第8行定义一个`num`变量，用来搭配第12行展示每门课程信息的序号。第8行的`while`循环开始，紧接着使用`try`语句来捕获异常。在`try`语句中(异常处理)，使用`pickle`模块将课程对象反序列化回来。`except`语句则作为结束循环的条件。那么为什么要加`try`语句呢？是因为`while True`的条件永为真，那么开始循环取值打印。当最后一次，文件中的课程对象已经取出完毕，也就是说文件成了空文件，但是`while`循环却没有终止，就会报`EOFError`错误，这个错误被`except`语句捕获，走`except`内部的`break`语句，终止`while`循环。

经过一个while循环取值，并打印，就展示出了所有的可选课程。

```python
'''
欢迎使用学生选课系统
username:alex
password:3714
登录成功，欢迎alex，您的身份是Manager
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 3
可选课程如下:
	 1 python 15000 6
	 2 java 14000 6
	 3 python 15000 6
'''
```

演示结果如上例所示。我们在上一节创建的Python学科，已经成功展示出来。

### 7.4.3 管理员之创建学生信息

创建学生信息的逻辑与创建课程一致，首先要获取学生的姓名、密码。然后通过Student类实例化一个学生对象，通过pickle模块将对象保存到文件中。

```python
# Manager类中的create_student方法   
class Manager:
    def create_student(self):
        '''创建学生'''
        stu_name = input('学生姓名 ： ')
        stu_pwd = input('学生密码 ： ')
        stu_obj = Student(stu_name)
        with open(os.path.join(BASE_DIR, 'db', 'student_info'), 'ab') as f:
            pickle.dump(stu_obj, f)
        print('\033[0;32m学员账号创建成功：%s 初始密码 ：%s\033[0m' % (stu_obj.name, stu_pwd))
```

上例中，首先获取学生的姓名和密码(第5-6行)，在7行通过`Student`类实例化一个学生对象，通过`pickle.dump`将该对象保存到文件中(第8-9行)。第10行打印必要的提示信息。

```python
'''
欢迎使用学生选课系统
username:alex
password:3714
登录成功，欢迎alex，您的身份是Manager
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 2
学生姓名 ： egon
学生密码 ： 123
学员账号创建成功：egon 初始密码 ：123
'''
```

通过上例的演示结果来看，一切非常完美。我想你也肯定迫不及待的使用新的学生账号登录试试效果了吧。

```python
'''
欢迎使用学生选课系统  
username : egon  
password : 123  
egon登录失败  
'''
```

在我们重新运行后，出现了如上例中的提示？用户登录失败！怎么回事？之前创建学生信息时提示已经创建成功了呀？

这里我们需要做些思考，在创建学生信息的时候，我们将学生对象保存到了`student_info`中，而我们在做用户认证校验的时候，操作的是`userinfo`文件。学生信息并没有更新到`userinfo`文件中，所以，我们还在创建学生信息的时候还需要再将用户名和密码保存到`userinfo`中。

```python
# Manager类中的create_student方法   
class Manager:
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
```

上例中，我们在获取到学生的信息后，在第7-8行，按照`userinfo`文件的需要的格式，将学生信息保存到文件中。在第8行又手动的拼接一个身份信息。

至于身份信息为什么要手动添加，而不是输入获取？我们要思考，当管理员在登录并执行到创建学生的信息时，目的已经很明确了，就是在做创建学生的操作。所以身份可以写入文件的时候，手动拼接进去。

那么你可能会问为什么不将学生信息都保存到一个文件中？这里考虑到我们都是新手，所以在开始登录认证的时候，操作都是普通文件，读取文件与处理都比较简单。而`pickle`操作文件相对复杂，为了好上手，并且使用多种方式来操作文件，也是对我们之前章节知识的回顾。

让我们重新创建学生信息，并且用新的学生账号登录试试。

```python
'''
欢迎使用学生选课系统
username:egon
password:123
登录成功，欢迎egon，您的身份是Student
'''
```

通过上例的演示，并没有什么问题。已经成功的识别了身份并展示了可选操作的列表。只是暂时我们还无法选择操作，因为学生的功能还没有实现。

### 7.4.4 管理员之查看学生信息

当学生账号创建完毕，我们就可以来查看学生的信息了。

思路也很简单，创建学生信息是写文件，查看学生信息则是读文件。

```python
# Manager类中的show_students方法  
class Manager:
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
```

上例中，在`show_students`方法中，第5行打印必要的提示信息，第6行以读的方式打开文件。第8-15循环读取学生信息并展示。需要补充的是第11行，在使用`pickle.load`将学生信息反序列化回来后，`stu_obj`就是一个完整的对象，可以直接调用该对象的方法或属性(第12行)。

```python
'''
欢迎使用学生选课系统
username:alex
password:3714
登录成功，欢迎alex，您的身份是Manager
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 4
学生如下 ： 
1 oldboy
2 egon
'''
```

在上例的演示中,可以看到创建好的两个学生被展示出来了。

另外，如果你一不小心，在创建完学生信息后，把`Student`类删掉或者注释掉了，那么你在执行上例演示的时候，会报如下错误。

```python
AttributeError: Can't get attribute 'Student' on <module '__main__' from 'F:/student_elective_sys/main.py'>  
```

通过上述错误，在使用`pickle`反序列化时，在反序列化学生对象的时候，依赖实例化该对象的类。也就是说，当前名称空间内中必须存在`Student`类。序列化才能成功，否则会报错，这点是需要注意的。

### 7.4.5 管理员之退出程序

来实现本系统中最简单的一个功能——退出功能。

```python
# Manager类中的exit方法  
class Manager:
    def exit(self):
        '''退出'''
        sys.exit('拜拜了您嘞！')
```

是的，退出的主逻辑代码就一行，或者说就调用了一个`sys.exit()`方法那么`sys.exit()`方法内部做了什么呢？简单来说，当`sys.exit()`方法被执行时，会引发一个`SystemExit`异常并使解释器退出。在退出之前可以做一些如上例的提示，或者执行一些代码执行一些清理工作。

```python
import sys
def clear():
    print('我是清理程序，我被sys.exit触发执行啦！')
sys.exit(clear())  # 我是清理程序，我被sys.exit触发执行啦！  
```

如上例所示，我们在需要使解释器结束执行时，就调用`sys.exit()`方法，可以在退出之前做一些收尾工作，比如上例中的调用`clear()`函数。

### 7.4.6 问题！你，还是你吗？

是的，同志们，到目前为止，一切都很顺利，各功能实现也达到我们的预期，但是，风平浪静下难掩波涛汹涌！让我们仔细的看下列代码并思考问题——你，还是你吗？

```python
# main.py中的main函数  
def main():
    '''程序入口'''
    print('\033[0;32m欢迎使用学生选课系统\033[0m')
    ret = login()
    if ret['auth']:
        print('\033[0;32m登录成功，欢迎%s，您的身份是%s\033[0m' % (ret['name'], ret['identify']))
        if hasattr(sys.modules[__name__], ret['identify']):
            cls = getattr(sys.modules[__name__], ret['identify'])
            obj = cls(ret['name'])
```

看着上例的代码片段，我们一起让程序在我们的脑海里`运行`。当用户登录成功后，根据身份信息反射并实例化一个相应的对象。然后执行相应的代码。停，让程序倒退执行一步`，实例化一个对象`，思考`实例化……`的过程是不是再生成一个新的对象？那么问题来了，生成一个新的对象跟我登录的用户有关系吗？没有！既然没有，如果学生`oldboy`登录后，程序在执行到这一步时，就又生成了一个新的`oldboy`对象。那么如果该学生之前已经选过课程或者有其他的操作，新的`oldboy`对象都无法使用，虽然这个对象还叫`oldboy`，但是此`oldboy`(新生成的)非彼`oldboy`(文件中的)！那么，怎么解决这个你不是你的问题呢？

我们可不可以这样？在程序执行到第9行`getattr`拿到类名之后，也就是实例化的时候，不直接实例化，而是通过`类名`调用一个方法，通过这个方法去读取文件，查看文件中是否存在该对象，如果存在则把该对象返回，让接下来的程序直接使用文件中存储的对象。说干就干。

```python
# Student类中的get_obj类方法 
class Student:
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
# Manager类中的get_obj类方法  
class Manager:
	@classmethod
    def get_obj(cls, name):
        return Manager(name)
# main函数
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
```

上例中，我们在`Student`类和`Manager`类中各加一个方法`get_obj`。这个方法就是读文件，将与登录用户名一致的对象返回。那么，方法一般由对象来调用，而此时在第30行获取到的是类名。一般的，类名无法直接调用方法，因为类名调用方法时，`self`参数需要手动传递。所以，我们这里用到了一个`classmethod`装饰器(具体参见面向对象章节关于`classmethod`装饰器的介绍)。将普通的方法装饰成类方法。类方法会自动传递`cls`参数，我们就可以直接通过类调用该`get_obj`方法了。

上例中还有一个很意思的现象，就是`Student`类和`Manager`类的类方法具体实现不一样。`Student`类的类方法经过打开文件，`pickle.load`反序列化，if判断用户名和文件中存的对象名是否一致，一致就返回该对象。而Manager类则直接实例化一个对象就返回了。这又是为什么呢？因为在实际开发中，管理员的角色可能只有一个或几个，甚至是直接就在后台创建一个管理员的账号就行了，只是利用管理员的高权限来做功能。我们的系统中也是，预先在`userinfo`文件中存储一个用户密码，身份是管理员。然后利用管理员的身份来创建和查看一些功能信息。并没有像学生角色一样，创建并保存管理员对象。所以学生角色存在的问题在管理员这里不算问题，管理员只要能登录并且能实现具体的功能，我管你是不是你？！而学生角色不一样，学生对象可以有很多，并且可做的操作也不一样，我们必须保证登录的用户真实存在`student_info`文件中的对象。

通过为`Student`类和`Manager`类各增加一个`get_obj`方法，并通过`classmethod`装饰器将该方法装饰成类方法。就解决了你不是你的问题。现在我们可以继续实现具体功能了。

截止到目前，管理员的操作还只剩下一个查看学生选课信息功能没有实现，但由于学生角色的功能还没有实现，这个查看学生选课的功能也就无从谈起了。那让我们先来实现学生角色的功能吧。

### 7.4.7 学生之查看可选课程

hi，同学，当你跟随我的脚步来到这里的时候，请务必把框架搭建起来，并且管理员角色的功能也实现，并成功的创建一些必要的数据。才能学习接下来的内容。

课程信息在之前的章节中已经由管理员创建完毕了。我们这里只需要拿过来并展示就可以了。去哪拿？读取`course_info`文件。怎么展示？还记的管理员怎么查看学生或者课程吗？是的。逻辑是一样的。



```python
# Student类中的show_courses方法  
class Student:
    def show_courses(self):
        '''查看可选课程'''
        print('课程信息如下 ： ')
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
```

如上例所示，首先第5行打印必要的提示信息增加用户体验。第6行以读的方式打开`course_info`文件。然后第8-16行就是`while`循环使用`pickle`反序列化对象，并展示结果。然后`except`捕捉异常终止循环。你可能疑惑第15行为什么打印一个空字符串(暂且先这么实现)。这里是为了在交互中，循环展示的结果和操作列表中间做隔离，增加用户体验。

```python
'''
欢迎使用学生选课系统
username:oldboy
password:666
登录成功，欢迎oldboy，您的身份是Student
1 查看可选课程
2 选择课程
3 查看所选课程
4 退出
请选择您要做的操作 ： 1
课程信息如下 ： 
	 1 python 15000 6
	 2 java 14000 6
	 3 python 15000 6
'''
```

如上例演示所示，我们使用学生账号登录系统，然后选择查看可选课程，结果展示如第12-14行所示的两门课程。这两门课程我们之前用管理员的角色创建好的。这里拿来就用就可以了。

### 7.4.8 学生之选择课程

重中之重，是的，学生 选课可以说最难的一个功能了。难在哪？

- 选课前要不要展示都有哪些可选课程？
- 怎么选择课程？
- 选择的课程如何保存？

问题已经抛出来了，那么我们就来一一解决这些问题。

怎么展示哪些课程？我们在上一小节中，已经能够查看都有哪些课程了，这里只需要调用展示课程的方法就行。

怎么选择课程？当我们能看到都有哪课程后，可以使用`input`来选择课程，然后设法将对应的课程对象取出来，添加到已被我们`遗忘`了的对象的课程属性列表中。

当选择好课程后，我们可以将新的学生对象更新到`student_info`文件中。

```python
# Student类中的show_courses方法
class Student:
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

```

上例中，首先解决第一个问题。我们首先修改一下show_courses方法，第6行，首先定一个一个列表，在`while`循环中，每次循环展示的时候，都将课程对象追加到列表中，最后将列表返回。

接下来解决第二个问题。在`select_course`方法中，第21行打印提示信息。第22行调用`show_courses`方法，展示课程信息并将所有的课程对象列表返回并赋值给`course_obj_lst`变量。第23行，获取用户选择的课程序号。第24行，增加一个简单判断之后，程序执行到了25行，将输入的序号转换为`int`类型。第26行，如果用户输入的序号在课程序号的范围内，首先，`len(course_obj_lst)`获取课程列表的长度，`range`后会得到一个范围，因为`range`范围的`start`参数是从0开始，所以此时的凡物可能是这样的0-5，而用户输入的序号是从1开始的，范围是这样的1-6。所以，range时要加上1，才能跟用户输入的序号匹配。第26行，如果用户输入的序号在`range`的范围内。则表示选择课程成功。第27行将用户选定的那门课程`pop`出来(这里的减1跟上面的加1一样都是解决序号与索引位置不匹配问题)并添加到学生对象的`courses`属性列表中。第29行打印选课成功的提示。

最后在来解决怎么保存的问题。首先要思考，当一个对象的课程属性被更新了之后，要把该对象重新更新到原来的文件中，而一个文件又不能同读写文件。所以，在第30-31行，以读的方式打开`student_info`文件，和以写的方式打开一个临时文件`student_info_temp`。`while`循环的思路不变，`try/except`语句用来控制`while`循环的结束。第39行调用`pickle.load`方法将对象从`student_info`文件中一个个的反序列化回来。第35的if判断，当每次循环反序列化回来一个对象，通过对象的`name`属性和当前对象的`name`属性做判断，如果是则说明，当前文件中反序列化回来的对象就是我们要更新的对象，我们就把当前的对象(self保存当前对象的所有信息)保存到临时文件中(原来的对象直接舍弃就好)，如果不是则程序执行第37行的`else`语句，说明本次循环从文件中取回来的对象不是当前对象，就直接保存到临时文件中。当循环结束，就意味着对象更新成功。程序继续往下走来到第41行，此时的`student_info`文件中保存的是原有对象信息的旧的文件。我们把它删掉。然后第42行再把临时文件名字改成`student_info`。一招偷梁换柱解决第三个问题。

现在，让我们运行看看效果如何。

```python
'''
欢迎使用学生选课系统
username:oldboy
password:666
登录成功，欢迎oldboy，您的身份是Student
1 查看可选课程
2 选择课程
3 查看所选课程
4 退出
请选择您要做的操作 ： 2
选择课程
课程信息如下 ： 
	 1 python 15000 6
	 2 java 14000 6
	 3 python 15000 6

输入选择课程的序号： 1
python 课程选择成功
'''
```

通过上例的演示效果表明选课成功。但是，这里还有问题我们困扰着我们，比如学生`oldboy`重复选择同样的课程，依然能添加同名的课程等其他的问题。但没有学习数据库的时候，为了不增加难度，暂时只能大致的把逻辑实现就好。

### 7.4.9 学生之查看可选课程

当学生选完课程之后，就可以通`show_selected_course`过查看自己选择了什么课程。这里有两个思路，并且都相当的简单。

第一个思路是，可以读`student_info`文件，循环展示学生对象的课程属性列表内的课程信息就好。

```python
# Student类中show_selected_course方法
class Student:
        def show_selected_course(self):
        '''查看选择的课程'''
        with open(os.path.join(BASE_DIR, 'db', 'student_info'), 'rb') as f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if self.name == stu_obj.name:
                        for index, item in enumerate(stu_obj.courses, 1):
                            print(index, item.name, item.price, item.period)
                except EOFError:
                    break
        print()
```

上例中，第5行以读的方式打开文件，在第6行的while循环中，每次的反序列化出来的对象的name属性等于当期对象的name属性，就说明是我们想要的那个对象。然后我们通过for循环循环该对象的课程属性的列表。拿出一个个课程信息展示就好了。

上例中，主要是展示学生的课程属性列表。那么我们思考一个问题，当前的对象是不是从“student_info”文件中匹配并返回的(类方法get_obj实现的)。那么，我们直接从这个对象中循环课程属性列表不就好了吗？不用绕个大弯特意的再次读一遍“student_info”文件。

```python
# Student类中show_selected_course方法
class Student:
            def show_selected_course(self):
        '''查看选择的课程'''
        print('选课情况如下 ： ')
        for num, course_obj in enumerate(self.courses, 1):
            print('\t', num, course_obj.name, course_obj.price, course_obj.period)
        print()
```

上例中，我们直接使用`for`循环展示当前对象的课程属性列表。然后打印课程的属性就好了。

现在，让我们看看效果如何。

```python
'''
欢迎使用学生选课系统
username:oldboy
password:666
登录成功，欢迎oldboy，您的身份是Student
1 查看可选课程
2 选择课程
3 查看所选课程
4 退出
请选择您要做的操作 ： 3
1 python 15000 6
2 java 14000 6
3 python 15000 6
'''
```

是的。上例的演示效果表明达到预期。让我们继续完成后续的功能。

### 7.4.10 强势插入之管理员的查看学生选课信息

学生角色的选择课程信息和查看课程信息已实现完毕，是时候来完成这个“遗漏”的功能——管理员角色的查看学生的选课信息。

```python
# Manager类中show_students_courses方法  
class Manager:
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
```

上例中，第5行以读的方式打开`student_info`文件。在第7行的`while`循环中，依然是使用`pickle.load`方法将对象反序列化回来，然后在第11行打印对象的`name`属性和课程列表。

```python
'''
欢迎使用学生选课系统
username:alex
password:3714
登录成功，欢迎alex，您的身份是Manager
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 5
1 oldboy [<__main__.Course object at 0x01B74E50>, <__main__.Course object at 0x01B840F0>, <__main__.Course object at 0x01B84130>]
2 egon []
'''
```

如上例的演示可以看到，基本“没什么问题”，你要问第13行的列表中明显是两个内存地址，怎么可能没问题？但这里需要说明的是，从代码层面来说是没问题的。那么怎么解决内存地址这个“问题”呢？

还记得我们在面向对象讲的字符串格式化三剑客吗？这里我们使用三剑客之一的`__repr__`方法来解决问题。

```python
# Course类，添加__repr__方法
class Course：
	def __repr__(self):
        return self.name
```

上例中，我们在Course类中，添加一个方法`__repr__`	。并返回该对象的`name`属性。现在，让我们重新运行程序。

```python
'''
欢迎使用学生选课系统
username:alex
password:3714
登录成功，欢迎alex，您的身份是Manager
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 5
1 oldboy [python, java, python]
2 egon []
'''
```

 上例的演示中，学生`oldboy`选择了三门课程，而学生`egon`的课程列表为空。

OK，管理员查看学生的选课信息的功能完成，让我们继续开发后续功能。

### 7.4.11 学生之退出

学生角色退出，实现思路完全参照管理员的退出就好了。

```python
# Student类中exit方法
class Student:
	def exit(self):
        '''退出''' 
        sys.exit('拜拜了您嘞！')  
```

上例中，我们在实现退出功能的时候，同样调用`sys.exit()`方法就好(第5行)。

```python
'''
欢迎使用学生选课系统
username:alex
password:3714
登录成功，欢迎alex，您的身份是Manager
1 创建课程
2 创建学生
3 查看可选课程
4 查看所有学生
5 查看所有学生选课情况
6 退出
请选择您要做的操作 ： 6
拜拜了您嘞！
'''
```

如上例演示所示。学生退出功能实现完毕。

截止到目前为止，我们所有细节功能都实现完毕。

## 7.5 系统优化

现在，是时候让我们对程序做个全面的检查了。

```python
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
        # 方法一
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
        # 方法二	
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
```

上例展示了我们目前为止所有的代码。那么，让我们在整体回顾一下系统需求，就会发现，有很多地方是需要优化的。让我们一起来优化它吧。

### 7.5.1 查看课程信息功能优化

首先，看一下学生角色和管理员角色的查看课程信息的代码片段。

```python
# Manager类中的show_courses方法
class Manager:
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
# Student类中的show_courses方法
class Student:
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

```

上例中，我们仔细观察两个查看课程信息的代码，其实差别不大。整体思路一致。只是在Student类中多了一个返回课程列表的操作。但这个功能放到Manager类中也没问题因为我们可以不接受返回值嘛！那么就怎么优化呢？

让我们分析一下，管理员和学生都是人类，那能否抽象出一个父类，在父类中实现查看课程的方法呢？

```python
class Person:
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
class Student(Person): pass
class Manager(Person): pass
```

如上例所示，我们在`main.py`中实现一个`Person`类，在Person类中实现查看课程信息的方法(第2-16行)。

然后`Student`类和`Manager`类继承`Person`类就行了。当各自对象在调用`show_courses`方法时，会自动去父类中查找。

### 7.5.2 退出功能优化

相对于课程信息的优化，我想你肯定对退出功能早已虎视眈眈了。因为`Student`类和`Manager`类中的`exit`方法完全一致。所以，退出功能也需要优化。

```python
class Person:
        def exit(self):
        '''退出'''
        sys.exit('拜拜了您嘞！')   
class Student(Person): pass
class Manager(Person): pass
```

上例中，我们把退出功能在Person类中实现，然后两个子类继承Person类就可以了。

### 7.5.3 文件路径的优化

每次对文件的读写我们都利用`os.path.join`方法拼接出路径，这样很麻烦，而且，如果文件路径如果有变动，也不利于修改。我们需要对文件路径做优化。

首先更新一下目录。

```python
student_elective_sys/    
    ├─ db/   
    │   ├─ course_info           # 存放课程信息    
    │   ├─ student_info          # 存放学生信息    
    │   └─ userinfo              # 存放用户信息    
    ├─ conf/  
    │   └─ settings.py           # 配置文件  
    └─ main.py                   # 主逻辑文件   
```

上例中在与`main.py`文件同级目录中创建一个名为`conf`的目录，并在该目录内创建一个`settings.py`文件。用来存储配置信息。

`settings.py`文件中我们将文件的路径在该文件内拼接。

```python
# student_elective_sys/conf/settings.py
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STUDENT_INFO = os.path.join(BASE_DIR, 'db', 'student_info')
STUDENT_INFO_TEMP = os.path.join(BASE_DIR, 'db', 'student_info_temp')
COURSE_INFO = os.path.join(BASE_DIR, 'db', 'course_info')
USER_INFO = os.path.join(BASE_DIR, 'db', 'userinfo')
```

如上例所示，所有的文件路径都可以在配置文件拼接好并赋值给对应的常量，然后在`main.py`中可以直接调用。当有变动的时候，来配置文件中修改，`main.py`文件无需改动 就可以生效。除了文件路径之外，配置文件中还可以有其他的配置项。这里就不一一列举了。

在main.py中导入该settings.py文件。

```python
# student_elective_sys/main.py
from conf import settings 
with open(settings.COURSE_INFO, 'rb') as f: pass
with open(settings.COURSE_INFO, 'ab') as f: pass
with open(settings.STUDENT_INFO, 'rb') as f: pass
```

如上例所示，在`main.py`中，第1行，使用配置文件之前，需要导入`settings.py`文件。然后在相应的地方直接使用`settings`点对应的常量名即可(第3-5行)。

### 7.5.4 文件操作优化

既然文件路径配置完毕，我们继续把跟文件相关的操作优化完毕。现在的代码现状是这样的，很多功能都操作同一个文件。这在实际开发中并不是一个正确的编程思路，我们应该把文件处理的操作封装成方法，然后某个功能在有文件处理的需求时，直接调用该方法即可。对于本系统许多功能对于序列化的操作，我们可以做一些针对性的优化。

```python
# main.py中的Person类
class Person:
    def dump_obj(self, obj=None, file_path=None, mode=None, content=None):
        '''序列化对象到文件'''
        with open(file_path, mode) as f:
            if content:
                f.write(content)
            else:
                pickle.dump(obj, f)
    def load_obj(self, file_path=None, mode=None):
        '''反序列化对象'''
        with open(file_path, mode) as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except EOFError:
                    break
```

上例中，我们在`Person`类中，实现两个关于操作文件的方法。第3-9行，`dump_obj`方法，当具体功能模块在调用该方法时，可以传递需要序列化的对象、序列化到什么文件、`mode`模式是什么、有没有其他的操作。在第5行，比如当创建学生的功能在调用该方法时，将用户信息写入`userinfo`是普通的写入操作，而将学生对象写入`student_info`，是序列化操作，两者有本质的区别。所以利用`content`参数和`obj`参数来判断到底是什么在对文件做什么操作。普通的写入，写入的字符串传递个`content`参数；序列化的时候，就把序列化的对象传递给`obj`参数，而`content`参数则为`None`。if条件不成立，走else做序列化动作。 

第10-18行，当`load_obj`方法被调用时，只需要告诉`load_obj`方法，你要从哪个文件反序列化对象，模式是什么就可以了(甚至模式都可以写死)。然后在第16行，利用上`yield`，提高效率。

在相应的功能模块调用上例两个方法时，根据需要传递参数就可以了。

```python
# Manager类中的create_student方法
class Manager(Person):
        def create_student(self):
        '''创建学生'''
        stu_name = input('学生姓名 ： ')
        stu_pwd = input('学生密码 ： ')
        content = '%s|%s|%s\n' % (stu_name, stu_pwd, 'Student')
        self.dump_obj(obj=None, file_path=settings.USER_INFO, mode='a', content=content)
        stu_obj = Student(stu_name)
        self.dump_obj(obj=stu_obj, file_path=settings.STUDENT_INFO, mode='ab')
        print('\033[0;32m学员账号创建成功：%s 初始密码 ：%s\033[0m' % (stu_obj.name, stu_pwd))
```

如上例所示，第8-10行。我们重新设计了一下代码，在要保存学生信息时，直接调用写文件的方法。如果是普通的写入，则为`content`参数传递具体的数据；如果是序列化对象，则为`obj`参数传递要序列化的对象。这样大大的节省了代码量。

其他功能模块关于文件操作的优化会在后面展示。

### 7.5.5 交互体验的优化

在学习Python的基础阶段。

我们在代码练习时，用的最多就是输入输出的交互，为了能在千篇一律的控制台中一眼发现想看到的那条结果，可以说不太容易。针对这个情况，我们在代码通过各种手段来优化，包括控制台输出加颜色、打印一个空行做隔离等。这里我们再次增加、完善一些小技巧，让交互更加友好。让我们来看两个代码片段。

比如向用户展示可操作的列表时，在每个序号前面加上一个`*`号。

```python
# main函数内的代码片段
for num, opt in enumerate(cls.operate_lst, 1):
	print(chr(42), num, opt[0])
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
'''
```

如上例演示效果所示，在第3行的打印中特意使用`chr()`函数获取星号。在增加辨识度的情况下，又回顾了内置函数。一举两得。

在展示结果中加上`\t`来与其他的交互区分。`\t`为4个缩进。

```python
# # Manager中的show_students方法
class Manager(Person):
        def show_students(self):
        '''查看所有学生'''
        print('学生如下 ： ')
        for index, item in enumerate(self.load_obj(file_path=settings.STUDENT_INFO, mode='rb'), 1):
            print('\t', index, item.name)
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
请选择您要做的操作 ： 4
学生如下 ： 
	 1 oldboy
	 2 egon
'''
```

上例中，第7行，在展示结果之前，都加上`\t`与后续的交互区分开。

除此之外，在优化文件操作时，也删除了之前功能中的一些打印。比如打印空字符串或者打印一个空(都是为了与后续的交互区分开)。

### 7.5.6 优化后的代码示例

经过一番优化后，现在将最终的代码展示如下。

```python
# student_elective_sys/main.py
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
```

正如上例所示，这是我们最终版本的代码。此时你可以参考这个示例完善你的代码了。

让我们最后在运行测试一次，先从管理员角色开始。

```python
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
请选择您要做的操作:1
课程名 ：Go
课程价格 ：15000
课程周期：6
课程创建成功：Go 15000 6 
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作:2
学生姓名 ： 武sir
学生密码 ： 123
学员账号创建成功：武sir 初始密码 ：123
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作:3
可选课程如下 ： 
	 1 python 15000 6
	 2 java 14000 6
	 3 python 15000 6
	 4 Go 15000 6
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作:4
学生如下 ： 
	 1 oldboy
	 2 egon
	 3 武sir
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作:5
学生选课情况如下 ： 
	 1 oldboy [python, java, python]
	 2 egon []
	 3 武sir []
* 1 创建课程
* 2 创建学生
* 3 查看可选课程
* 4 查看所有学生
* 5 查看所有学生选课情况
* 6 退出
请选择您要做的操作:6
拜拜了您嘞！
'''
```

上例演示所示，每个功能都准确的达到了预期。接下来我们来测试一下学生登录。

```python
'''
欢迎使用学生选课系统
username : 武sir
password : 123
登录成功，欢迎武sir，您的身份是Student
* 1 查看可选课程
* 2 选择课程
* 3 查看所选课程
* 4 退出
请选择您要做的操作:1
可选课程如下 ： 
	 1 python 15000 6
	 2 java 14000 6
	 3 python 15000 6
	 4 Go 15000 6
* 1 查看可选课程
* 2 选择课程
* 3 查看所选课程
* 4 退出
请选择您要做的操作:2
选择课程
可选课程如下 ： 
	 1 python 15000 6
	 2 java 14000 6
	 3 python 15000 6
	 4 Go 15000 6
输入选择课程的序号： 4
Go 课程选择成功

* 1 查看可选课程
* 2 选择课程
* 3 查看所选课程
* 4 退出
请选择您要做的操作:3
选课情况如下 ： 
	 1 Go 15000 6
* 1 查看可选课程
* 2 选择课程
* 3 查看所选课程
* 4 退出
请选择您要做的操作:4
拜拜了您嘞！
'''
```

如上例所示，学生端展示也没有问题。那么本系统暂时开发至此。让我们来做一些总结。

## 7.6 总结

- 不足

本系统还有很多不足之处。 一些细节处理还不够，一些知识点的讲解还不够深入。比如说在功能的开发中，对于交互的处理，只是简单地加了一些if判断，但这还不够。

学生选课功能的开发，还有很多有待提高的地方，因为还有很多这里考虑到了却没有实现的功能，例如，用户输入超出范围的处理，重复选课的处理等等。一些功能有待完善。例如创建的学员已存在该怎么处理等。这里我们在具体的实现中并没有体现。因为暂时我们没有学习数据库，所以我们对于数据处理略显粗糙。如果使用数据库，可能解决上述问题只需要简单的两三行代码就能完成，而现在要完成却需要用20行甚至更多的代码来完善。这无疑增加难度，对我们新手来说，更加不利。

- 收获

同志们，当你学习到这里的时候，就是最大的收获！坚持学习的品质本就难能可贵。

在本系统中，我们有意无意的尽可能的多应用一些知识点。这是一次知识的回顾、串连。可能之前的有些地方看的懵懵懂懂，经过大量的练习，思考， 慢慢的就变得明朗了。这也是本书列举大量示例和讲解的原因。

Python这门语言本就是优美，简洁的，当你我们学到这里，仅是掌握了Python的基础部分。到这里并不意味着结束，而学习的步伐才刚刚开始。

------

see also： [女神的学生选课系统博客](https://www.cnblogs.com/Eva-J/articles/9235899.html)
