#!/bin/bash


MODEL_NAME="InternVL3-8B"


python inference.py \
    --test_dataset "ER.json" \
    --dataset_name ER \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin t

python inference1.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty temporal\
    --oringin t

python inference1.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty location\
    --oringin t



python inference1.py --test_dataset "people_knowledge.json" --dataset_name people_knowledge --meta_save_path original --model_name "$MODEL_NAME" --conflict_type ee --eval_type openqa --ty Career --oringin t


python inference1.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty time\
    --oringin t

python inference1.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty creator\
    --oringin t

python inference1.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty content\
    --oringin t

python inference.py \
    --test_dataset "IS.json" \
    --dataset_name IS \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin t
