#!/bin/bash

# 定义默认路径
#实体识别的路径
MODEL_NAME="InternVL3-8B"


# 运行实体识别
python inference.py \
    --test_dataset "ER.json" \
    --dataset_name ER \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --oringin t

python inference1.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty temporal\
    --oringin t

python inference1.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty location\
    --oringin t


python inference1.py --test_dataset "people_knowledge.json" --dataset_name people_knowledge --meta_save_path original --model_name "$MODEL_NAME" --conflict_type ee --eval_type mcq --ty Career --oringin t


python inference1.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty time\
    --oringin t

python inference1.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty creator\
    --oringin t

python inference1.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty content\
    --oringin t

python inference.py \
    --test_dataset "IS.json" \
    --dataset_name IS \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --oringin t

python inference2.py \
    --test_dataset "ED.json" \
    --dataset_name ED \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --oringin t
