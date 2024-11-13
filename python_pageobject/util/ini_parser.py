import configparser
import os

def get_option_value(ini_file_path,section_name,option_name):
    if not os.path.exists(ini_file_path):
        print("读取的 ini 文件 %s 路径不存在! " %ini_file_path)
        return None

    # 创建配置解析器对象
    config = configparser.ConfigParser()
    # 读取 UTF-8 编码的 INI 文件
    with open(ini_file_path, 'r', encoding='utf-8') as f:
        config.read_file(f)

    try:
        value = config.get(section_name,option_name)
        return value
    except Exception as e:
        print(e)
        print("无法从ini文件 %s 读取 section：%s 中的option:%s的值" %(ini_file_path,section_name,option_name))
        return None

if __name__ =="__main__":
    ini_file_path ="d:\\python_pageobject\\config\\object_map.ini"
    print(get_option_value("e:\\a.ini", "index_page", "iframe"))
    print(get_option_value(ini_file_path, "index_page1", "iframe"))
    print(get_option_value(ini_file_path, "index_page", "iframe1"))
    print(get_option_value(ini_file_path,"index_page","iframe"))
