from category import cate
from answer import final_answer
def answer_user_question(user_wechat_nickname, user_question):
    try:
        return final_answer(user_wechat_nickname,user_question,cate(user_question))
    except Exception as e:
        print(e)
        return 'an Error of type ' + str(type(e)) + ' has occurred.'