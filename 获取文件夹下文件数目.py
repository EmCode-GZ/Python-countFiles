import os
#path = "G:\Image Data\全部数据新加旧"  # 获取当前路径
path = "G:\GitHub代码\GAN-S\dataset\celebA"
print(path)
count = 0
for root, dirs, files in os.walk(path):    # 遍历统计
    for each in files:
        count += 1
print(count)
