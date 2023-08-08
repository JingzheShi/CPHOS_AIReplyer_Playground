from gpt_utils import get_answer_from_gpt
from glm_utils import get_answer_from_glm
from search_pdf_utils import SemanticSearch, load_recommender
import sys
#load the problem base
prob = {
        '身份信息录入问题':['references/身份变动问题.pdf','为什么老师审核没有通过？','怎么添加副领队？','怎么在系统中添加学生信息？','发现学生信息显示不正确？'],
        '考试进行中的问题':['references/试题传输问题.pdf','试卷解压不了？','时间节点过了能否上传试卷？','我该怎么上传试卷？','试卷传错了怎么重新上传？','我们没赶上交卷，能再开一下通道吗？','请问能提前下发试卷吗？'],
        '老师阅卷时的问题':['references/阅卷相关问题.pdf','我该如何阅卷？','为什么我要批改的卷子这么多？','可以让学生帮我阅卷吗？','为什么我没上传试卷却有阅卷任务？'],
        '考生查分时的问题':['references/出分相关问题.pdf','请问如何查询成绩？','请问我该如何查分？','为什么我看不到学生的分数？','为什么我看不到学生的分数？','为什么我看不到学生的排名？','查分能再延长一段时间吗？'],
        '赛季结束咨询问题':['references/休赛期的问题.pdf','下次考试什么时候开始？','如何才能加入CPHOS组织？','请问能发一下往届考题吗？','怎么报名参加考试？','上届的试题评析什么时候出？']
    }
profile = '以下是一些参考材料：\nCPHOS是一个民间公益组织，定期为所有物理竞赛生组织联考。联考的流程如下：'\
            "1.将参赛各校学生、教练的身份信息录入信息系统。\n"\
            "2.进行考试。\n"\
            "3.组织老师进行阅卷。\n"\
            "4.开放学生进行查分。\n"\
            "5.休赛期。"
prob_list = []
for name, address in prob.items():
    prob_list.append(name)

#This function is used to employ the LLM.
def useLLM(prompt,model): #model can be gpt or glm.
    if model == 'gpt':
        return get_answer_from_gpt('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',prompt,'gpt-3.5-turbo')
    elif model == 'glm':
        return get_answer_from_glm('76ac5e2039ac8a8da4bd924957e03b20.kJAQi8ptu0ynObZr',prompt,'chatglm_130b')
    else:
        print('MODError. The engine should be glm or gpt.')
        sys.exit(1)

#This class is used to generate hints in the prompt.
class hint:
    def __init__(self,prob=prob,profile=profile,prob_list = prob_list):
        self.prob = prob
        self.profile = profile
        self.prob_list = prob_list
    
    #This method is used to search hint in pdf saved in references.dic.
    def pdf(self,type,question): #type can be an element in prob_list; question is the key word.
        recommender = SemanticSearch()
        for name in self.prob_list:
            if type == name:
                load_recommender(recommender,self.prob_list[name][0])
                result_list = recommender(question)
            else:
                print('TYPError. The type should be in:\n')
                for name in self.prob_list:
                    print('{} '.format(name))
                sys.exit(1)
        hint_str = '\n|||\n'.join(result_list)
        hint_str = '以下一些是参考材料：\n' + hint_str.replace('|||','以下一些是参考材料：')
        return hint_str
    
    
    

            
            
        

