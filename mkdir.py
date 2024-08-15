import os
for i in range(1, 101):
    # 使用format函数来确保是两位数
    file_name = "Day{:02d}".format(i)
    # 创建文件夹
    
    os.makedirs(file_name, exist_ok=True)