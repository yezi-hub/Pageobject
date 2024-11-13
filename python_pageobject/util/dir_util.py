import os
from util.time_util import *

#创建时间目录
def create_date_dir(dir_path):
    if not os.path.exists(dir_path):
        print("指定的路径 %s 不存在！" %dir_path)
        return None
    cur_date = get_chinese_date()
    date_dir_path = os.path.join(dir_path,cur_date)
    if not os.path.exists(date_dir_path):
        os.mkdir(date_dir_path)
    return date_dir_path

def create_hour_dir(dir_path):
    date_dir = create_date_dir(dir_path)
    if date_dir:
        hour = get_chinese_hour()
        hour_dir_path = os.path.join(date_dir,hour)
        if not os.path.exists(hour_dir_path):
            os.mkdir(hour_dir_path)
        return hour_dir_path
    else:
        return None

if __name__ == "__main__":
    print(create_date_dir("D:\\python_pageobject\\capture_pics"))
    print(create_hour_dir("D:\\python_pageobject\\capture_pics"))
    print(create_hour_dir("D:\\python_pageobject\\capture_pic"))


