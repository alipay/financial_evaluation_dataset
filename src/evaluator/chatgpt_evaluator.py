from utils.gpt_utils import gpt_api


class ChatGPTEvaluator:
    def __init__(self, model_type="text-davinci-002"):
        self.mode_type = model_type

    def answer(self, query, model_type="text-davinci-002"):
        return gpt_api(query, model_type)


if __name__ == "__main__":
    evaluator = ChatGPTEvaluator()
    print(evaluator.answer("你好"))
