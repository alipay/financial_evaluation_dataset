#!/bin/bash

model_name="gpt35"
dataset_type="dev"
result_path="../results"

cd ../src

python exec_fineva_main.py \
    --model_name ${model_name} \
    --dataset_type ${dataset_type} \
    --save_path ${result_path}

python get_score.py \
    --model_name ${model_name} \
    --result_path ${result_path}


