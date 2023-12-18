from transformers import AutoModelForCausalLM, GenerationConfig, AutoTokenizer


class QWenEvaluator:
    def __init__(self, model_path="/mnt/models/qwen/Qwen-7B-Chat"):
        self.model_path = model_path
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path, device_map="auto", trust_remote_code=True)
        self.model = self.model.eval()
        self.model.generation_config = GenerationConfig.from_pretrained(self.model_path,
                                                                        trust_remote_code=True)  # 可指定不同的生成长度、top_p等相关超参
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)

    def answer(self, query):
        response, history = self.model.chat(self.tokenizer, query, history=[])
        return response


if __name__ == "__main__":
    evaluator = QWenEvaluator()
    print(evaluator.answer("你好"))
