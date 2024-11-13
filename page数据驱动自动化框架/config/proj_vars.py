import os

proj_path = os.path.dirname(os.path.dirname(__file__))
ini_file_path = os.path.join(proj_path,"config","object_map.ini")
test_data_file_path = os.path.join(proj_path,"test_data","126邮箱联系人.xlsx")
caputre_pic_dir_path = os.path.join(proj_path,"capture_pics")

#数据信息对应的execel表格中的列序号，从0开始
login_sn_col_no = 0
login_user_name_col_no = 1
login_pass_word_col_no = 2
login_contact_sheet_name_col_no = 3
login_executed_flag_col_no = 4
login_test_result_col_no = 5
login_exception_info_col_no = 6
login_executed_time_col_no = 7
login_capture_pic_path_col_no = 8

contact_sn_col_no= 0
contact_name_col_no=1
contact_email_col_no=2
contact_star_col_no=3
contact_mobile_col_no=4
contact_comment_col_no=5
contact_assert_word_col_no=6
contact_executed_flag_col_no = 7
contact_executed_time_col_no = 8
contact_test_result_col_no = 9
contact_exception_info_col_no = 10
contact_capture_pic_col_no =11

log_conf_file_path = os.path.join(proj_path,"config","Logger.conf")

if __name__ == "__main__":
    print(__file__)
    # 获取当前文件的绝对路径
    print(os.path.dirname(__file__))
    # 获得当前文件所在的目录
    print(os.path.dirname(os.path.dirname(__file__)))  # 获得当前工程的绝对目录
    # 工程中的ini的绝路路径
    print(ini_file_path)
    # 获取测试数据文件excel的路径
    print(test_data_file_path)
    # 获取截图的路径
    print(caputre_pic_dir_path)
    #日志配置文件所在的路径
    print(log_conf_file_path)


