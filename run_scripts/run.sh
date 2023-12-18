#!/bin/bash

echo "Running run_chatglm2.sh"
bash run_chatglm2.sh

echo "Running run_baichuan2_7b.sh"
bash run_baichuan2_7b.sh

echo "Running run_baichuan2_13b.sh"
bash run_baichuan2_13b.sh

echo "Running run_qwen_7b.sh"
bash run_qwen_7b.sh

echo "Running run_qwen_14b.sh"
bash run_qwen_14b.sh

echo "Running run_llama2_7b.sh"
bash run_llama2_7b.sh

echo "Running run_llama2_13b.sh"
bash run_llama2_13b.sh

echo "Running run_gpt35.sh"
bash run_gpt35.sh

echo "All scripts executed successfully"