# coding=utf-8
'''
Author: GitHub-LP
Date: 2024-09-13 17:48:08
LastEditors: LP
LastEditTime: 2024-09-14 11:43:32
FilePath: \pythonFor100Days\stage_1\02_controlling_processes_and_data_structures\06_conditional_statement.py
Description: 
Copyright (c) 2024 by GitHub-LP, All Rights Reserved.
'''
# 示例1 简单条件
x = 10
y = 20

if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")

# 示例2 复杂条件
# and or not
age = 17
is_student = True

if age >= 18 and is_student:
    print("You are an eligible student.")
elif age >= 18:
    print("You are eligible but not a student.")
elif is_student:
    print("You are a student but not eligible.")
else:
    print("You are neither eligible nor a student.")

# 示例3 条件表达式（三元运算符）
# exp1 if contion else exp2
age = 18
status = "adult" if age >= 18 else "minor"
print(status)

# 示例4 链式条件
score = 75
if 0 <= score < 50:
    print("Fail")
elif 50 <= score < 75:
    print("Pass")
else:
    print("Distinction")