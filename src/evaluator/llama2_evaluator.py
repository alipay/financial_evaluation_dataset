import torch
from transformers import LlamaForCausalLM, AutoTokenizer


class LLaMA2Evaluator:
    def __init__(self, generation_config, model_path="/mnt/models/llama/llama-2-7b-hf"):
        self.model_path = model_path
        self.model = LlamaForCausalLM.from_pretrained(self.model_path, torch_dtype=torch.float16, device_map="auto").eval()
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.generation_config = generation_config

    def answer(self, query):
        query = f"User: {query} \n\nAssistant:"
        inputs = self.tokenizer(query, return_tensors="pt")
        generate_ids = self.model.generate(inputs.input_ids.to("cuda"), **self.generation_config)
        output = \
        self.tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        return output[len(query):].strip("!@#$%^&*()_-+=[]{}|\\;':\",.<>/?~` \t\n？。")


if __name__ == "__main__":
    max_new_tokens = 1024
    generation_config = dict(
        temperature=0.01,
        top_k=40,
        top_p=0.7,
        max_new_tokens=1024
    )
    evaluator = LLaMA2Evaluator(generation_config)
    # print(evaluator.answer("hi"))
    print(evaluator.answer("你好"))
    