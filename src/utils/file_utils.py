import json

import pandas as pd


def load_json(json_path):
    if not json_path.endswith('.json'):
        raise ValueError('json_path should end with.json')
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data


def save_json(data, json_path):
    with open(json_path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def jsonl_to_df(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(pd.read_json(line, lines=True))
    return pd.concat(data, ignore_index=True)


def df_to_jsonl(df, jsonl_path):
    df.to_json(jsonl_path, orient='records', lines=True, force_ascii=False)
    print(f"Successfully write to {jsonl_path}")
