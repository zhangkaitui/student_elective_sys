# -*- coding: utf-8 -*-
# Date: 2019/1/23
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STUDENT_INFO = os.path.join(BASE_DIR, 'db', 'student_info')
STUDENT_INFO_TEMP = os.path.join(BASE_DIR, 'db', 'student_info_temp')
COURSE_INFO = os.path.join(BASE_DIR, 'db', 'course_info')
USER_INFO = os.path.join(BASE_DIR, 'db', 'userinfo')


'''

# 斜杠结尾的为目录，扩展名为.py的是py文件,扩展名为.txt是数据文件  
student_elective_sys\  
    ├─ db\  
    │   ├─ course_info.txt      # 存放课程信息  
    │   ├─ student_info.txt     # 存放学生信息  
    │   └─ userinfo.txt         # 存放用户信息  
    ├─ conf\
    │   └─ settings.py          # 配置文件
    └─ main.py                  # 主逻辑文件  


'''