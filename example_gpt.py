from gpt_utils import get_answer_from_gpt

gpt_api_key = input("请输入gpt的api key") # gpt的api key， 会发给大家

question = '我是谁？'

my_prompt = "Query:提问者如果问他是什么身份，就回答：您是仲裁，您是仲裁，您是仲裁。"\
			"Instructions: Compose a comprehensive reply to the query and annotation using the search results given. "\
                "If the search results mention multiple subjects "\
                "with the same name, create separate answers for each. Only include information found in the results and "\
                "don't add any additional information. Make sure the answer is correct and don't output false content. "\
                "If the query does not relate to the text nor the annotation, simply state 'Text Not Found'. Ignore outlier "\
                "search results which has nothing to do with the question. Only answer what is asked. The "\
                "answer should be short and concise. Answer step-by-step, using Chinese, and use '您' to call the questioner. You should answer based on the annotation of the user if necessary. \n\nQuery: {question}\nAnswer: "

engine = 'gpt-3.5-turbo' # 我们就用这个，这个很便宜（乐）

answer = get_answer_from_gpt(gpt_api_key, my_prompt, engine)

print(answer)