#!/bin/bash

# 定义默认路径
#实体识别的路径
MODEL_NAME="Qwen2.5-VL-3B-Instruct"


# 运行实体识别
python inference_d.py \
    --test_dataset "ER.json" \
    --dataset_name ER \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin f

python inference1_d.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty temporal\
    --oringin f


python inference1_d.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty time\
    --oringin f



python inference_d.py \
    --test_dataset "IS.json" \
    --dataset_name IS \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin f

python inference2_d.py \
    --test_dataset "ED.json" \
    --dataset_name ED \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin f

python inference_d.py \
    --test_dataset "ER.json" \
    --dataset_name ER \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --oringin f

python inference1_d.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty temporal\
    --oringin f
python inference1_d.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty location\
    --oringin f

python inference1_d.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty Carrer\
    --oringin f

python inference1_d.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty time\
    --oringin f

python inference1_d.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty creator\
    --oringin f

python inference1_d.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty content\
    --oringin f



python inference_d.py \
    --test_dataset "IS.json" \
    --dataset_name IS \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --oringin f

python inference2_d.py \
    --test_dataset "ED.json" \
    --dataset_name ED \
    --meta_save_path detection \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --oringin f