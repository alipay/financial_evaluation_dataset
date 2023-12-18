import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig


class Baichuan2Evaluator:
    def __init__(self, model_path="/mnt/models/baichuan/Baichuan2-7B-Chat"):
        self.model_path = model_path
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path, trust_remote_code=True,
                                                          torch_dtype=torch.bfloat16, device_map="auto")
        self.model = self.model.eval()
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, use_fast=False, trust_remote_code=True)
        self.model.generation_config = GenerationConfig.from_pretrained(self.model_path,
                                                                        trust_remote_code=True)  # 可指定不同的生成长度、top_p等相关超参

    def answer(self, query):
        messages = []
        messages.append({"role": "user", "content": query})
        response = self.model.chat(self.tokenizer, messages)
        return response


if __name__ == "__main__":
    evaluator = Baichuan2Evaluator()
    print(evaluator.answer("你好"))
    print(evaluator.answer("登鹳雀楼->王之涣\n夜雨寄北->"))

