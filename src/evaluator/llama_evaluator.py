import torch
from transformers import LlamaTokenizer, LlamaForCausalLM


class LLaMAEvaluator:
    def __init__(self, max_length, generation_config, model_path="/mnt/models/llama/llama-7b-hf"):
        self.model_path = model_path
        # load_8bit = False
        self.tokenizer = LlamaTokenizer.from_pretrained(self.model_path)
        self.tokenizer.padding_side = "right"
        self.model = LlamaForCausalLM.from_pretrained(
            self.model_path,
            torch_dtype=torch.float16,
            # torch_dtype=torch.bfloat16,
            device_map="auto").eval()
        # unwind broken decapoda-research config
        self.model.config.pad_token_id = self.tokenizer.pad_token_id = 0  # unk
        self.model.config.bos_token_id = 1
        self.model.config.eos_token_id = 2
        self.max_length = max_length
        self.device = "cuda"
        self.generation_config = generation_config

    def answer(self, query):
        query = """USER: {}. ASSISTANT:""".format(query)
        # query = """A chat between a curious user and an artificial intelligence assistant (name FIAI) . The assistant gives helpful, detailed, and polite answers to the user's questions. USER: Hello! ASSISTANT: Hi!</s> USER: {} ASSISTANT:""".format(
        #     query)
        inputs = self.tokenizer(query, return_tensors='pt', return_attention_mask=False, add_special_tokens=False,
                                truncation=True, max_length=self.max_length)
        generation_output = \
            self.model.generate(input_ids=inputs["input_ids"].to(
                self.device), **self.generation_config)[0]
        generate_text = self.tokenizer.decode(
            generation_output, skip_special_tokens=False)
        # result = generate_text.split('</s>')[1]
        # 会加一个bos token
        # .strip("!@#$%^&*()_-+=[]{}|\\;':\",.<>/?~` \t\n？。")
        return generate_text[len(query) + 1:].replace("</s>", "")


if __name__ == "__main__":
    max_new_tokens = 1024
    generation_config = dict(
        temperature=0.2,
        top_k=40,
        top_p=0.7,
        num_beams=1,
        do_sample=False,
        repetition_penalty=1.0,
        max_new_tokens=max_new_tokens
    )
    evaluator = LLaMAEvaluator(max_new_tokens, generation_config)
    print(evaluator.answer("hi"))
    print(evaluator.answer("你好"))
