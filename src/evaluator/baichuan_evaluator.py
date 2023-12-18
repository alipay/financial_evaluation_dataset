from transformers import AutoModelForCausalLM, AutoTokenizer


class BaichuanEvaluator:
    def __init__(self, model_path="/mnt/models/baichuan/Baichuan-7B"):
        self.model_path = model_path
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path, device_map="auto", trust_remote_code=True).half().cuda()
        self.model = self.model.eval()
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, use_fast=False, trust_remote_code=True)

    def answer(self, query):
        # response, history = self.model.chat(self.tokenizer, query, history=[])
        # return response
        inputs = self.tokenizer(query, return_tensors='pt')
        inputs = inputs.to('cuda:0')
        pred = self.model.generate(**inputs, max_new_tokens=64, repetition_penalty=1.1)
        return self.tokenizer.decode(pred.cpu()[0], skip_special_tokens=True)


if __name__ == "__main__":
    evaluator = BaichuanEvaluator()
    print(evaluator.answer("你好"))
    print(evaluator.answer("登鹳雀楼->王之涣\n夜雨寄北->"))

