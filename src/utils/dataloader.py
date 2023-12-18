# Copyright (c) 2023 Ant Group
# All rights reserved.
import pandas as pd
import os


def load_dataset(path, dataset_type):
    dataset = []
    if dataset_type not in ["dev", "test", "full"]:
        raise ValueError("加载数据集类型错误，限定在dev、test、full中，当前赋值为 ：" + str(dataset_type))

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(".csv")]:
            subject = dirpath.split("/")[-1]
            path = os.path.join(dirpath, filename)
            domain = filename.split(".")[0]
            frame = pd.read_csv(path)  
            headers = frame.head(0)
            headers = list(headers)
            for i in range(len(frame)):
                tid = "/"
                context = "/"
                question = "/"
                A="/"
                B="/"
                C="/"
                D="/"
                E="/"
                answer = "/"

                if "id" in headers:
                    id = frame["id"][i]
                if "context" in headers:
                    context = frame["context"][i]   
                if "question" in headers:
                    question = frame["question"][i]
                if "A" in headers:
                    A = frame["A"][i]
                if "B" in headers:
                    B = frame["B"][i]
                if "C" in headers:
                    C = frame["C"][i]
                if "D" in headers:
                    D = frame["D"][i]
                if "E" in headers:
                    E = frame["E"][i]

                if "answer" in headers:
                    answer = frame["answer"][i]
                    if answer != answer:
                        answer = ""

                # 判断加载数据集类型，其中
                # dev集是披露answer的评测题
                # test集是未披露answer的评测题
                # full集是所有评测题
                if dataset_type == "dev" and answer == "":
                    continue
                elif dataset_type == "test" and answer != "":
                    continue
                elif dataset_type == "full":
                    pass



                if domain == "会计从业资格考试":
                    prompt_constructor = f"""你是一名专业的会计从业人员，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
会计从业资格考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""

                elif domain == "金融文档抽取":
                    prompt_constructor = f"""你是一名专业的金融从业者，你会收到一份资讯内容，以及一个问题内容，你需要从A、B、C、D四个选项中选出一个作为该问题内容最恰当的回答，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
金融资讯：{context}
问题：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "保险知识解读":
                    prompt_constructor = f"""你是一名专业的保险专家，你对任何保险知识都了解，你需要从A、B、C、D四个选项中选出一个作为问题最恰当的回答，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
保险问题：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "理财知识解读":
                    prompt_constructor = f"""你是一名专业的理财专家，你对任何理财知识都了解，你需要从A、B、C、D四个选项中选出一个作为问题最恰当的回答，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
理财问题：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "金融术语解释":
                    prompt_constructor = f"""你是一名专业的金融专家，你对任何金融术语都了解，你需要从A、B、C、D四个选项中选出一个作为术语最恰当的描述，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
金融术语：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""

                elif domain == "执业药师资格考试":
                    prompt_constructor = f"""你是一名专业的执业药师人员，你需要从A、B、C、D、E五个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D、E中一个。
执业药师资格考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
E.{E}
答："""
                elif domain == "执业医师资格考试":
                    prompt_constructor = f"""你是一名专业的执业医师人员，你需要从A、B、C、D、E五个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D、E中一个。
执业医师资格考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
E.{E}
答："""
                elif domain == "保险从业资格考试":
                    prompt_constructor = f"""你是一名专业的保险从业人员，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
基金从业资格考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "基金从业资格考试":
                    prompt_constructor = f"""你是一名专业的基金从业人员，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
基金从业资格考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "证券从业资格考试":
                    prompt_constructor = f"""你是一名专业的证券从业人员，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
证券从业资格考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "银行从业资格考试":
                    prompt_constructor = f"""你是一名专业的银行从业人员，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
银行从业资格考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""

                elif domain == "期货从业资格考试":
                    prompt_constructor = f"""你是一名专业的期货从业人员，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
期货从业资格考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "期权从业人员考试":
                    prompt_constructor = f"""你是一名专业的期权从业人员，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
期权从业人员考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "注册税务师":
                    prompt_constructor = f"""你是一名专业的注册税务师，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
注册税务师资格考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "审计师考试":
                    prompt_constructor = f"""你是一名专业的审计师，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
审计师考试问题是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""

                elif domain == "金融意图理解":
                    prompt_constructor = f"""你是一名专业的金融专家，你可以对用户提问的意图进行理解，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
用户的提问是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "保险意图理解":
                    prompt_constructor = f"""你是一名专业的保险顾问，你可以对用户提问的意图进行理解，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
用户的提问是：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "金融槽位识别":
                    prompt_constructor = f"""你是一位金融领域的专家，你可以从一段文本中识别出其中特定的公司、政府主体。你需要从A、B、C、D四个选项中选出一个作为主体识别的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
这是你收到的文本信息：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "保险槽位识别":
                    prompt_constructor = f"""你是一位保险领域的专家，你可以从一段文本中识别出其中特定的险种、保险产品名词。你需要从A、B、C、D四个选项中选出一个作为识别的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
这是你收到的文本信息：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""

                elif domain == "金融情绪识别":
                    prompt_constructor = f"""你是一名专业的金融分析师，你能够识别出一段金融文本的多种情绪分类：积极、中性、消极。接下来你会得到一段金融文本，你需要判断该文本所表达的情绪是属于积极、中性、消极的哪一类别。你需要从A、B、C三个选项中选出一个作为识别的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C中一个。
金融文本是：{question}
选项：
A.{A}
B.{B}
C.{C}
答："""

                elif domain == "研判观点提取":
                    prompt_constructor = f"""你是一位金融领域的专家，你能够识别出一段研报文本反映的市场走向：利空、中性、利好、未知。接下来你会得到一段研报文本，你需要判断该文本所反映的市场走向是属于利空、中性、利好、未知的哪一类别。你需要从A、B、C、D四个选项中选出一个作为识别的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
研报内容是：
{question}
以下哪个选项可以最恰当的描述研报的研判观点？
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "金融数值计算":
                    prompt_constructor = f"""你是数值计算的专家，你可以完成金融数值计算的题目。你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
题目：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "金融产品分析":
                    prompt_constructor = f"""你是金融产品的专家，你会收到一段基金的描述，然后你需要回答关于基金描述的问题。你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
基金描述：
{context}
问题：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "金融事件解读":
                    prompt_constructor = f"""你是金融事件解读的专家，你会收到一段金融事件内容，然后你需要回答关于该金融事件解读的问题，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
资讯内容：
{context}
问题：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""

                elif domain == "保险属性抽取":
                    prompt_constructor = f"""你是保险属性抽取的专家，请根据提取要求，给出正确答案的选项，请选出其中最恰当的答案选项，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
保险条款内容：{context}
提取要求：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "保险条款解读":
                    prompt_constructor = f"""你是保险条款解读的专家，你会收到一段保险条款内容，然后你需要回答关于该条款内容的问题，你需要从A、B、C、D四个选项中选出一个作为回答问题的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
保险条款内容：
{context}
问题：{question}
选项：
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "保险核赔推理":
                    prompt_constructor = f"""你是一名专业的保险核赔审核专家，假设投保人的其他赔付条件都满足，现基于患者的既往史、现病史、主诉、诊断信息判断该保险案例是否符合保险理赔赔付。你的输出只能是“是”或者“否”。
案例内容：
{question}
输出：”"""

                elif domain == "文本总结归纳":
                    prompt_constructor = f"""你是一名专业的金融专家，你需要对给定的文本进行总结归纳。你需要从A、B、C、D四个选项中选出一个作为文本总结归纳的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
文本内容是：
{question}
以下哪个选项可以最恰当的对文本内容进行归纳？
A.{A}
B.{B}
C.{C}
D.{D}
答："""

                elif domain == "资讯标题生成":
                    prompt_constructor = f"""你是一名专业的金融专家，你需要对给定的文本进行标题生成。你需要从A、B、C、D四个选项中选出一个作为标题生成的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
文本内容是：
{question}
以下哪个选项可以最恰当的作为文本的标题？
A.{A}
B.{B}
C.{C}
D.{D}
答："""
                elif domain == "投教话术生成":
                    prompt_constructor = f"""你是一位金融领域的专家，你会收到一个简短词汇（金融术语等），你可以生成文本让用户更好理解这个词的含义。你需要从A、B、C、D四个选项中选出一个作为话术生成的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
金融词汇：{question}
以下哪个选项可以最恰当得让用户更好理解这个词的含义？
A.{A}
B.{B}
C.{C}
D.{D}
答："""

                elif domain == "营销文案生成":
                    prompt_constructor = f"""你是一名专业的金融营销专家，你可以基于一个产品的名称、功能介绍、产品特点为它设定一句营销文案。你需要从A、B、C、D四个选项中选出一个作为营销文案生成的最恰当的答案，你只能输出一个字符，并且这个字符是A、B、C、D中一个。
产品内容是：
{question}
以下哪个选项可以最恰当的作为该产品的营销文案？
A.{A}
B.{B}
C.{C}
D.{D}
答："""

                elif domain == "金融合规性":
                    prompt_constructor = f"""你是一名专业的金融行业金融合规审核员，你可以判断给定的输入包含的信息是否金融合规。
问题是：{question}
你的输出只能是“是”或者“否”"""
                elif domain == "金融问题识别":
                    prompt_constructor = f"""你是一名专业的金融行业安全审核员，你可以判断给定的问题是否属于金融问题。
问题是：{question}
你的输出只能是“是”或者“否”"""
                elif domain == "信息安全合规":
                    prompt_constructor = f"""你是一名专业的金融行业信息安全审核员，你可以判断给定的输入包含的信息是否安全合规。
问题是：{question}
你的输出只能是“是”或者“否”"""
                elif domain == "金融事实性":
                    prompt_constructor = f"""你是一名专业的金融行业金融信息事实性审核员，你可以判断给定的输入包含的信息是否符合事实。
问题是：{question}
你的输出只能是“是”或者“否”"""


                details = {}
                details["id"] = int(id)
                details["subject"] = subject
                details["domain"] = domain
                details["prompt"] = prompt_constructor
                details["answer"] = answer
                dataset.append(details)
    return dataset
            
        
        

            
