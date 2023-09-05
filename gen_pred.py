import json
import pandas as pd

def get_preds(data,prompt_template):
    preds = []
    for _,row in data.iterrows():
        id = row['id']
        prompt = prompt_template.format(row['问题'])
        answer = row.get('答案')
        preds.append({"id":id ,"prompt":prompt ,"answer":answer})
    return preds

if __name__ == '__main__':
    datasets = ["金融意图理解","金融槽位识别","金融情绪识别","对话主题识别","研判观点提取",
                "文本总结归纳","资讯标题生成","营销文案生成","服务小结生成","投教话术生成",
                "证券从业资格考试","基金从业资格考试","金融术语解释","保险知识解读","财富知识解读","知识检索增强","金融文档抽取",
                "金融事件解读","保险核保推理","金融工具调用","金融数值计算","金融产品评测","保险条款解读",
                "安全底线","金融问题识别","信息安全合规","金融合规性","金融事实性"]
    data = pd.read_csv("data/fin_test.csv")
    dataset2prompt = json.load(open("code/dataset2prompt.json", "r"))
    for dataset in datasets:
        prompt_template = dataset2prompt[dataset]
        preds = get_preds(data.query("任务 == @dataset")[['id','问题','答案']],prompt_template)
        with open(f"pred/{dataset}.json","w") as f:
            for pred in preds:
                json.dump(pred,f,ensure_ascii=False)
                f.write('\n')