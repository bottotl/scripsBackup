import os
import datetime
import re
import subprocess

# 遍历的文件夹路径
folder_path = "/Volumes/ST1/网盘备份/来自：iPhone"
# folder_path = "/Users/yulintao/Downloads/test"

def updateFile(filename, root):
    # 将文件名转换为日期格式
    date_str = filename.split(".")[0]   # 去掉文件扩展名
    clean_filename = date_str.split('(')[0].strip()
    clean_filename = clean_filename.split(' ')
    if len(date_str) > 0 and len(clean_filename) >= 2:
        print(clean_filename)
        date_str = clean_filename[0]+ ' ' + clean_filename[1]
        # 将字符串解析为日期对象
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H%M%S")
    
        # 获取时间戳
        timestamp = date_obj.timestamp()
        formatted_date = date_obj.strftime("%m/%d/%y %H:%M:%S")

        # 修改文件的访问时间、修改时间和创建时间
        filepath = os.path.join(root, filename)

        subprocess.call(['setfile', '-d', formatted_date, '-m', formatted_date, filepath])

def updateDir(filename , root):
    # 将文件名转换为日期格式
    date_str = filename.split(".")[0]   # 去掉文件扩展名
    clean_filename = date_str.split('(')[0].strip()
    clean_filename = clean_filename.split(' ')
    if len(date_str) > 0 and len(clean_filename) >= 2:
        print(clean_filename)
        date_str = clean_filename[0]+ ' ' + clean_filename[1]
        # 将字符串解析为日期对象
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H%M%S")
    
        # 获取时间戳
        timestamp = date_obj.timestamp()
        formatted_date = date_obj.strftime("%m/%d/%y %H:%M:%S")

        # 修改文件的访问时间、修改时间和创建时间
        filepath = os.path.join(root, filename)

        # 遍历文件夹中的所有文件并修改创建时间、访问时间和修改时间
        for root, dirs, files in os.walk(filepath):
            for file in files:
                internalFilePath = os.path.join(root, file)
                print(internalFilePath)
                os.utime(internalFilePath, (timestamp, timestamp))
                subprocess.call(['setfile', '-d', formatted_date, '-m', formatted_date, internalFilePath])


def updateFolder(folder_path):
    # 遍历文件夹中的所有文件并修改创建时间、访问时间和修改时间
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
           updateFile(filename, root)
        for dir in dirs:
            updateDir(dir, root)

updateFolder(folder_path)