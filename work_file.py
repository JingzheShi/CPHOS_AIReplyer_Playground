def answer_user_question(user_wechat_nickname, user_question):
    try:
        # ---------------------------------- TODO ---------------------------------------
        # TODO: fill in here to answer user's question.
        # You can make new files in the /utils folder and import them here, to make this file cleaner.
        
        pass

        import random # modify this
        return 'test answer' + str(random.randint(114514,1919810)) # modify this
        # ---------------------------------- TODO ---------------------------------------
    except Exception as e:
        print(e)
        return 'an Error of type ' + str(type(e)) + ' has occurred.'