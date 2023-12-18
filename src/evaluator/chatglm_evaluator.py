from transformers import AutoModel, AutoTokenizer


class ChatGLMEvaluator:
    def __init__(self, model_path="/mnt/models/chatglm/chatglm-6b"):
        self.model_path = model_path
        self.model = AutoModel.from_pretrained(self.model_path, trust_remote_code=True).half().cuda()
        self.model = self.model.eval()
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)

    def answer(self, query):
        response, history = self.model.chat(self.tokenizer, query, history=[])
        return response


if __name__ == "__main__":
    evaluator = ChatGLMEvaluator()
    print(evaluator.answer("你好"))
