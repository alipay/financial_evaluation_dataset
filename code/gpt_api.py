import openai

MODEL_TYPE = "gpt-3.5-turbo" # gpt-4

gpt_eval_template = """
你是一个金融任务评估专家，你将收到一个{task}问题和一个由金融大模型生成的答案。
你的任务是评估金融大模型针对问题生成的答案质量。

任务: {question}

生成的答案:{generated_answer}

你需要基于回答的质量（答案自身的自洽性，是否回答任务所给出的问题，答案信息是否丰富）综合判断给出0-10分，10分为最高；
答案(仅打分数字):
"""

def gpt_eval(query, model_type=MODEL_TYPE):
    response = openai.ChatCompletion.create(
    model=model_type,
    messages=[
            {"role": "system", "content": "你是一个任务评估专家"},
            {"role": "user", "content": query},
        ],
    temperature=0
    )
    result = response['choices'][0]['message']['content']
    return result.strip("分")

if __name__ == '__main__':
    text = "你好啊"
    print(gpt_eval(text))