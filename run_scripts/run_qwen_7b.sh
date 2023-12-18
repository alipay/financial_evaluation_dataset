#!/bin/bash

model_name="qwen7b"
model_path="../models/qwen/Qwen-7B-Chat"
dataset_type="dev"
result_path="../results"

cd ../src

python exec_fineva_main.py \
    --model_name ${model_name} \
    --model_path ${model_path} \
    --dataset_type ${dataset_type} \
    --save_path ${result_path}

python get_score.py \
    --model_name ${model_name} \
    --result_path ${result_path}