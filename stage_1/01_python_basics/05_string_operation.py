# 字符串切片
s = "Hello, World!"
# 从索引1到索引5（不包括5）
print(s[1:5])  # 输出 'ello'

# 从索引1开始，到字符串结束
print(s[1:])   # 输出 'ello, World!'

# 从字符串开始，到索引5（不包括5）
print(s[:5])   # 输出 'Hello'

# 从索引6开始，步长为2
print(s[6:-1:2])  # 输出 'ol'

# 逆向切片
print(s[::-1])  # 输出 '!dlroW ,olleH'

#字符串拼接
s1 = "Hello"
s2 = "World"
# 使用 + 运算符
print(s1 + " " + s2)  # 输出 'Hello World'

# 使用 join() 方法
print(" ".join([s1, s2]))  # 输出 'Hello World'

#字符串格式化
name = "AiENG"
age = 22

# 使用 % 格式化
print("Hello, %s. You are %d years old." % (name, age))

# 使用 str.format() 方法
print("Hello, {}. You are {} years old.".format(name, age))

# 使用 f-string
print(f"Hello, {name}. You are {age} years old.")

#  字符串方法
s3 = " Hello, World! "
# 转换为大写
print(s3.upper())  # 输出 ' HELLO, WORLD! '

# 转换为小写    
print(s3.lower())  # 输出 ' hello, world! '

#首字母大写
print(s3.capitalize())  # 输出 'Hello, world! '

#单词首字母大写
print(s3.title())  # 输出 'Hello, World! '

# 去除首尾空格
print(s3.strip())  # 输出 'Hello, World!'

# 替换子字符串
print(s3.replace("World", "Python"))  # 输出 ' Hello, Python! '

# 分割字符串
print(s3.split(", "))  # 输出 ['Hello', 'World!']

