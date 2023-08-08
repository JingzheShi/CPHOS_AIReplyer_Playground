from prompt_utils import useLLM, hint
from id_search import get_id_info
def final_answer(user_wechat_nickname,user_question,type):
    if type == '参考材料中无相关信息':
        return '我暂时不清楚这个问题的答案，您可以重新表述您的问题，或者咨询人工服务。'
    else:
        prompt = hint() #Used to load hints.

        #Add the question to the prompt.
        prompt_str = f"请你不要使用自己的常识，仅根据后面的参考材料，回答：“{user_question}”"

        #Load the hint.
        prompt_str += prompt.pdf(type,user_question)
        
        #Use LLM to generate the answer
        answer = useLLM(prompt_str,'glm')

        #For '身份信息录入问题', we need to get the id information.
        if type == '身份信息录入问题':
            answer +=  get_id_info(user_wechat_nickname)

        return answer

        