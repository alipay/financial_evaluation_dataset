import re

SC = "(){}[]<>\"'`\\/|:;,." 

def normalize(result):
    result = result.strip(SC)
    pattern = r"\s*A|B|C|D\s*" # 定义一个正则表达式匹配answer XML tag中的大写
    match = re.search(pattern, result)
    if match:
        answer = match.group(0)
    else:
        answer = "No match"
    return answer

def normalize_option(answer, options):
    for option in options:
        keywords = option.split('&')
        keywords_pattern = '|'.join(re.escape(keyword.strip()) for keyword in keywords)
        if bool(re.search(keywords_pattern, answer)):
            return option
    else:
        return "No Match"

if __name__ == '__main__':
    text = "这是一些文字(A)和另一些文字（B），还有一些文字（C）和最后一些文字（D）。"
    print(normalize(text))

