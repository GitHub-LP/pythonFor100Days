# coding=utf-8
'''
Author: GitHub-LP
Date: 2024-09-05 17:55:19
LastEditors: LP
LastEditTime: 2024-09-13 18:01:29
FilePath: \pythonFor100Days\stage_1\01_python_basics\04_basic_operator.py
Description: 
Copyright (c) 2024 by GitHub-LP, All Rights Reserved.
'''

# 算数运算符
a = 10
b = 6

# 加法
add_result = a + b
print (add_result)

# 减法
subtract_result = a - b
print (subtract_result)

# 乘法
multiply_result = a * b
print (multiply_result)

# 除法
divide_result = a / b
print (divide_result)

# 整除
floor_div_result = a // b
print (floor_div_result)

# 取模(余数)
mod_result = a % b
print (mod_result)

# 幂
power_result = a ** b
print (power_result)

# 比较运行符
# 大于
greater_than_result = a > b # True
print (greater_than_result)

# 小于
less_than_result = a < b # False
print (less_than_result)

# 大于等于
greater_than_equal_result = a >= b # True
print (greater_than_equal_result)

# 小于等于
less_than_equal_result = a <= b # False
print (less_than_equal_result)

# 等于
equal_result = a == b # False
print (equal_result)

# 不等于
not_equal_result = a != b # True
print (not_equal_result)

# 逻辑运算符
# 逻辑与（and）
1 and 0 # 0
True and False  # False


# 逻辑或（or）
0 or 1  # 1
True or False # True

# 逻辑非（not）
1 not in [0, 1]  # False
not True  # False

# 成员运算符
1 in [0, 1, 2, 3, 4]  # True

5 in [0, 1, 2, 3, 4]  # False

5 not in [0, 1, 2, 3, 4]  # True

# 身份运算符
a = b = [1,2,3]
a is b  # True
a is not b  # False
