from config.proj_vars import test_data_file_path,caputre_pic_dir_path
from util.excel_util import Excel
from test_cases.mail_test_case import login,visit_contact,add_contact
from util.time_util import get_chinese_date_time
from util.capture_pic import cature_pic
import traceback
from config.proj_vars import  *
from util.log_util import *
#生成excel文件对象
test_data_wb = Excel(test_data_file_path)

test_data_wb.set_sheet("126账号")

all_test_data =  test_data_wb.get_all_cell_values()#读取登录的所有数据
#for test_data in all_test_data:
#    print(test_data)


login_data_header = all_test_data[0]

for test_data in all_test_data [1:]:
    user_name = test_data[login_user_name_col_no]
    pass_word = test_data[login_pass_word_col_no]
    contact_data_sheet_name = test_data[login_contact_sheet_name_col_no]
    executed_flag = test_data[login_executed_flag_col_no ]
    test_data_wb.set_sheet(contact_data_sheet_name)
    contact_test_data = test_data_wb.get_all_cell_values()#拿到所有的联系人数据
    contact_header = contact_test_data[0]
    if executed_flag.lower()=="y":
        try:
            print(user_name)
            info("开始使用用户名%s和密码%s执行登录操作" %(user_name,pass_word))
            driver = login(user_name,pass_word)
            visit_contact(driver)
            test_data[login_test_result_col_no]="成功"
            info("登录操作成功！")
            test_data[login_executed_time_col_no ]=get_chinese_date_time()
            test_data_wb.set_sheet("测试结果")
            test_data_wb.write_one_line(login_data_header, pattern="00FF00")
            test_data_wb.write_one_line(test_data)
            test_data_wb.write_one_line(contact_header, pattern="00FF00")
            for contact_data in contact_test_data[1:]:
                name = contact_data[contact_name_col_no]
                email = contact_data[contact_email_col_no]
                star = contact_data[contact_star_col_no]
                if star=="是":
                    star=True
                else:
                    star=False
                mobile = contact_data[contact_mobile_col_no]
                comment = contact_data[contact_comment_col_no]

                assert_word = contact_data[contact_assert_word_col_no]
                contact_executed_flag = contact_data[contact_executed_flag_col_no ]
                if not name:name = ""
                if not email: email = ""
                if not mobile: mobile = ""
                if not comment: comment = ""
                if not star: star = False
                if not assert_word:assert_word=""
                if not contact_executed_flag:contact_executed_flag=""
                if contact_executed_flag.lower()=="y":
                    try:
                        add_contact(driver,name=name,email=email,star=star,mobile=mobile,comment=comment,assert_word=assert_word)
                        contact_data[contact_test_result_col_no] = "成功"

                    except Exception as e:
                        contact_data[contact_test_result_col_no]="失败"
                        exception_info = traceback.format_exc()
                        contact_data[contact_exception_info_col_no]=str(e)+"\n"+exception_info
                        pic_path = cature_pic(driver)
                        contact_data[contact_capture_pic_col_no ]=pic_path
                    contact_data[contact_executed_time_col_no ] = get_chinese_date_time()
                    test_data_wb.write_one_line(contact_data)

            test_data[login_test_result_col_no]="成功"
            driver.quit()
        except Exception as e:
            print(e)
            test_data[login_test_result_col_no] = "失败"
            exception_info = traceback.format_exc()
            test_data[login_exception_info_col_no] = str(e)+"\n"+exception_info
            info("登录操作失败，异常信息："+str(e)+"\n"+exception_info)
            test_data[login_executed_time_col_no] = get_chinese_date_time()
            pic_path = cature_pic(driver)
            test_data[login_capture_pic_path_col_no] = pic_path
            test_data_wb.write_one_line(login_data_header, pattern="00FF00")
            test_data_wb.write_one_line(test_data)


    else:
        continue
test_data_wb.save()