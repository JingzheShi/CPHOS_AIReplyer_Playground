from prompt_utils import useLLM, hint
from string import ascii_uppercase
def cate(user_question):
    alphabet = []
    prompt = hint()
    prompt_str = f"请你不要使用自己的常识，仅根据后面的参考材料，判断“{user_question}”属于以下哪类问题，选择对应的英文字母："
    for item in ascii_uppercase:
        alphabet.append(item)
    for num in range(len(prompt.prob_list)):
        prompt_str += f'{alphabet[num]}.{prompt.prob_list[num]} '

    prompt_str += f'Z.参考材料中无相关信息。\n回答不要多于15个字，请你不需要告诉我选择的理由，只回答选项对应的英文字母。\n{prompt.profile}\n一些典型的常见问题：\n'

    for name in prompt.prob_list:
        prompt_str += f'{name}：'
        for num in range(1,len(prompt.prob[name])):
            prompt_str += f'{num}.{prompt.prob[name][num]}'
        prompt_str += '\n'

    return useLLM(prompt_str,'glm')

def test_cate():
    test = hint()
    for name in test.prob_list:
        for num in range(1,len(test.prob[name])):
            print(cate(test.prob[name][num]))
print(cate('这次考试谁是上海第一？'))

