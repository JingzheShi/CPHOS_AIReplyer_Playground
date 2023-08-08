from db_api.DataQueryApis.GetTeacherInfoApis import *
def get_id_info(user_wechat_nickname):
    from db_api import customTransaction
    user_id_returned_list = customTransaction.executeOperation(GetTeacherInfoByWechatName(user_wechat_nickname))
    user_id_to_be_verified_list = customTransaction.executeOperation(GetToBeVerifiedTeacherInfoByWechatName(user_wechat_nickname))
        
    sql_returned_str = ''
        
    if len(user_id_returned_list) == 0 and len(user_id_to_be_verified_list) == 0:
        sql_returned_str += '您目前的状态是“不在系统中”。您尚未提交审核，或未按要求在报名时登陆。您无法提交试卷、阅卷、也无法完成领队或者副领队相关操作。'
    elif len(user_id_returned_list) == 0 and len(user_id_to_be_verified_list) == 1:
        sql_returned_str += '您目前的状态是“待审核”，需要等待审核。审核完成之后，才能提交试卷或阅卷、才能完成领队或者副领队相关操作。'       
    elif len(user_id_returned_list) == 1:
        teacher_id = user_id_returned_list[0]['id']
        teacher_type = user_id_returned_list[0]['type'] # 仲裁，副领队，领队
        sql_returned_str += '{}您好，您目前已在系统中了，身份是{}'.format(teacher_id, teacher_type)
    
    return sql_returned_str