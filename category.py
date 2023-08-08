from prompt_utils import useLLM, hint
from string import ascii_uppercase
def cate(user_question):
    alphabet = [] 
    prompt = hint() #Used to load hints.

    #Add the question to the prompt.
    prompt_str = f"请你不要使用自己的常识，仅根据后面的参考材料，判断“{user_question}”属于以下哪类问题，选择对应的英文字母："
    
    #Generate an alphabet.
    for item in ascii_uppercase:
        alphabet.append(item)

    #Add choices to the prompt.
    for num in range(len(prompt.prob_list)):
        prompt_str += f'{alphabet[num]}.{prompt.prob_list[num]} '
    prompt_str += f'Z.参考材料中无相关信息。'\
    #Add the confienment.
    '\n回答不要多于15个字，请你不需要告诉我选择的理由，只回答选项对应的英文字母。'\
    #Load the hint.
    f'\n{prompt.profile}\n一些典型的常见问题：\n'
    for name in prompt.prob_list:
        prompt_str += f'{name}：'
        for num in range(1,len(prompt.prob[name])):
            prompt_str += f'{num}.{prompt.prob[name][num]}'
        prompt_str += '\n'

    #Modify the answer into a standard form.
    judge = False
    for item in prompt.prob_list:
        if item in useLLM(prompt_str,'glm'):
            judge = True
            return item
                
    if judge == False:
        return '参考材料中无相关信息'

#This function can be used to test the prompt.
#The right output should be blocked and orderly, just like:
'''考试进行中的问题
考试进行中的问题
考试进行中的问题
考试进行中的问题
考试进行中的问题
老师阅卷时的问题
老师阅卷时的问题
老师阅卷时的问题
老师阅卷时的问题
考生查分时的问题
考生查分时的问题
考生查分时的问题...'''

def test_cate():
    test = hint()
    for name in test.prob_list:
        for num in range(1,len(test.prob[name])):
            print(cate(test.prob[name][num]))
print(cate('原神，启动！'))

