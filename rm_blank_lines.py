# -*- coding: utf-8 -*-
# @Time   : 2021/6/21 16:27
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : rm_blank_lines.py

txt = '/Users/Beyoung/Library/Mobile Documents/com~apple~CloudDocs/电子藏书/第二性（合卷本）【三秋书屋www.d4j.cn】/第二性合卷本2-迅捷PDF转换器.txt'

content = []
with open(txt, 'r') as f:
    lines = f.readlines()
    f.close()

for line in lines:
    if line != '\n':
        if not line.startswith('('):
            content.append(line)

with open(txt[:-4] + '_min.txt', 'w') as of:
    of.writelines(content)
    of.close()
