import argparse
import os
import re

import pandas as pd
from sklearn.metrics import accuracy_score

from utils.file_utils import save_json


def extract_choice(response: str) -> str:
    '''
        Always return a choice, even cannot match by regex,
        to ensure fair comparison to other models.
    '''
    if response == '':
        return ""
    choices = ["A", "B", "C", "D", "E"]
    if response == '':
        return ""
    # 1. Single match
    patterns = [
        (r'答案(选项)?(是|为)：? ?([ABCDE])', 3),
        (r'答案(是|为)选项 ?([ABCDE])', 2),
        (r'故?选择?：? ?([ABCDE])',1),
        (r'([ABCDE]) ?选?项(是|为)?正确',1),
        (r'正确的?选项(是|为) ?([ABCDE])',2),
        (r'答案(应该)?(是|为)([ABCDE])',3),
        (r'选项 ?([ABCDE]) ?(是|为)?正确',1),
        (r'选择答案 ?([ABCDE])',1),
        (r'答案?：?([ABCDE])',1),
        (r'([ABCDE])(选?项)?是?符合题意',1),
        (r'答案选项：? ?([ABCDE])', 1), # chatglm
        (r'答案(选项)?为(.*?)([ABCDE])', 3), # chatgpt
        (r'选项([ABCDE])是最恰当的', 1),
        (r'选项([ABCDE]).*最恰当', 1),
        (r'选项([ABCDE]).*最能恰当', 1),
        (r'选项([ABCDE]).*最能', 1),
        (r'最恰当.*是选项([ABCDE])', 1),
        (r'correct answer is.*([ABCDE])', 1),
    ]
    for pattern, idx in patterns:
        m = re.search(pattern, response, re.M)
        if m:
            answer = m.group(idx)
            assert answer in choices
            return answer

    # 2. Recursive match
    patterns = [
        (r'([ABCDE])(.*?)当选', 1),
        (r'([ABCDE])(.*?)正确', 1),
    ]
    for pattern, idx in patterns:
        m = re.search(pattern, response, re.M)
        if m:
            while m:
                answer = m.group(idx)
                m = re.search(pattern, m.group(0)[1:], re.M)
            assert answer in choices
            return answer

    # 3. Weak single match
    patterns = [
        (r'[^不]是：? ?([ABCDE])', 1),
    ]
    for pattern,idx in patterns:
        m = re.search(pattern, response, re.M)
        if m:
            answer = m.group(idx)
            assert answer in choices
            return answer

    # 4. Check the only mentioned choices
    pattern = r'^[^ABCDE]*([ABCDE])[^ABCDE]*$'
    m = re.match(pattern, response)
    if m:
        answer = m.group(1)
        assert answer in choices
        return answer

    # 5. Check the only mentioned choices in the start of the sentence
    m = re.match(pattern, response[:4])
    if m:
        answer = m.group(1)
        assert answer in choices
        return answer

    m = re.match(pattern, response[:2])
    if m:
        answer = m.group(1)
        assert answer in choices
        return answer

    return ""


def extract_yn(response: str) -> str:
    choices = ["是", "否", "对", "错"]

    if response == '':
        return ""

    # Single match
    patterns = [
        (r'([是对])[ ？]*正确', 1),
        (r'([否错])[ ？]*错误', 1),
        (r'([是对])', 1),
        (r'([否错])', 1),
    ]

    for pattern, idx in patterns:
        m = re.search(pattern, response, re.M)
        if m:
            answer = m.group(idx)
            if answer in choices:
                return answer

    return ""


def get_score(args):
    check_ture_false_list = ["安全合规_金融合规性", "安全合规_金融问题识别", "安全合规_信息安全合规", "安全合规_金融事实性"]
    model_name = args.model_name
    result_path = args.result_path

    if not os.path.exists(result_path):
        os.makedirs(result_path)

    ga_result_path = os.path.join(result_path, f'{model_name}_ga.csv')
    df = pd.read_csv(ga_result_path)
    sid_set = set()
    for index, row in df.iterrows():
        # 正则提取正确选项
        sid = row["subject"] + "_" + row["domain"]
        sid_set.add(sid)
        if sid in check_ture_false_list:
            df.at[index, f'{model_name}_extract'] = extract_yn(row[f'{model_name}_answer'])
        else:
            df.at[index, f'{model_name}_extract'] = extract_choice(row[f'{model_name}_answer'])

    df.to_csv(os.path.join(result_path, f'{model_name}_result.csv'), index=False)

    # 计算 accuracy
    task_acc = {}
    sid_list = list(sid_set)
    sid_list.sort()
    for task in sid_list:
        task_df = df[df["subject"] + "_" + df["domain"] == task]
        acc = accuracy_score(task_df['answer'].tolist(), task_df[f'{model_name}_extract'].tolist())
        print(f'{task}: {acc}')
        task_acc[task] = acc

    save_json(task_acc, os.path.join(result_path, f'{model_name}_score.json'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', required=True, type=str)
    parser.add_argument('--result_path', required=True, type=str)
    args = parser.parse_args()
    get_score(args)
