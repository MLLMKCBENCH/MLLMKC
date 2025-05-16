#!/bin/bash

# 定义默认路径
#实体识别的路径
MODEL_NAME="gpt-4o-mini"


#封闭问答的原始知识
python inference_gpt.py \
    --test_dataset "ER.json" \
    --dataset_name ER \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --oringin t

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty temporal\
    --oringin t

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty location\
    --oringin t


python inference1_gpt.py --test_dataset "people_knowledge.json" --dataset_name people_knowledge --meta_save_path original --model_name "$MODEL_NAME" --conflict_type ee --eval_type mcq --ty Career --oringin t

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty time\
    --oringin t

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty creator\
    --oringin t

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty content\
    --oringin t

python inference_gpt.py \
    --test_dataset "IS.json" \
    --dataset_name IS \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --oringin t

python inference2_gpt.py \
    --test_dataset "ED.json" \
    --dataset_name ED \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --oringin t

#开放问答原始知识
python inference_gpt.py \
    --test_dataset ER.json \
    --dataset_name ER \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin t

python inference1_gpt.py \
    --test_dataset people_knowledge.json \
    --dataset_name people_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty temporal\
    --oringin t

python inference1_gpt.py \
    --test_dataset people_knowledge.json \
    --dataset_name people_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty location\
    --oringin t



python inference1_gpt.py --test_dataset "people_knowledge.json" --dataset_name people_knowledge --meta_save_path original --model_name "$MODEL_NAME" --conflict_type ee --eval_type openqa --ty Career --oringin t

python inference1_gpt.py \
    --test_dataset logo_knowledge.json \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty time\
    --oringin t

python inference1_gpt.py \
    --test_dataset logo_knowledge.json \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty creator\
    --oringin t

python inference1_gpt.py \
    --test_dataset logo_knowledge.json \
    --dataset_name logo_knowledge \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty content\
    --oringin t

python inference_gpt.py \
    --test_dataset IS.json \
    --dataset_name IS \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin t

python inference2_gpt.py \
    --test_dataset ED.json\
    --dataset_name ED \
    --meta_save_path original \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin t

#封闭回答的内外冲突
python inference_gpt.py \
    --test_dataset "ER.json" \
    --dataset_name ER \
    --meta_save_path  output\
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type mcq \
    --oringin f

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type mcq \
    --ty temporal\
    --oringin f

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type mcq \
    --ty location\
    --oringin f

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path output \
    --model_name"$MODEL_NAME" \
    --conflict_type ie \
    --eval_type mcq \
    --ty Career\
    --oringin f

python inference1_gpt.py --test_dataset "people_knowledge.json" --dataset_name people_knowledge --meta_save_path output --model_name "$MODEL_NAME" --conflict_type ie --eval_type mcq --ty Career --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type mcq \
    --ty time\
    --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type mcq \
    --ty creator\
    --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type mcq \
    --ty content\
    --oringin f

python inference_gpt.py \
    --test_dataset "IS.json" \
    --dataset_name IS \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type mcq \
    --oringin f

python inference2_gpt.py \
    --test_dataset "ED.json" \
    --dataset_name ED \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type mcq \
    --oringin f


# 封闭回答的外外冲突
python inference_gpt.py \
    --test_dataset "ER.json" \
    --dataset_name ER \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --oringin f

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty temporal\
    --oringin f

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty location\
    --oringin f


python inference1_gpt.py --test_dataset "people_knowledge.json" --dataset_name people_knowledge --meta_save_path output --model_name "$MODEL_NAME" --conflict_type ee --eval_type mcq --ty Career --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty time\
    --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty creator\
    --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --ty content\
    --oringin f

python inference_gpt.py \
    --test_dataset "IS.json" \
    --dataset_name IS \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --oringin f

python inference2_gpt.py \
    --test_dataset "ED.json" \
    --dataset_name ED \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type mcq \
    --oringin f


# 开放回答的内外冲突
python inference_gpt.py \
    --test_dataset "ER.json" \
    --dataset_name ER \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --oringin f

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty temporal\
    --oringin f

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty location\
    --oringin f



python inference1_gpt.py --test_dataset "people_knowledge.json" --dataset_name people_knowledge --meta_save_path output --model_name "$MODEL_NAME" --conflict_type ie --eval_type openqa --ty Career --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty time\
    --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty creator\
    --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty content\
    --oringin f

python inference_gpt.py \
    --test_dataset "IS.json" \
    --dataset_name IS \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --oringin f

python inference2_gpt.py \
    --test_dataset "ED.json" \
    --dataset_name ED \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --oringin f

# 开放回答的外外冲突
python inference_gpt.py \
    --test_dataset "ER.json" \
    --dataset_name ER \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin f

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty temporal\
    --oringin f

python inference1_gpt.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty location\
    --oringin f



python inference1_gpt.py --test_dataset "people_knowledge.json" --dataset_name people_knowledge --meta_save_path output --model_name "$MODEL_NAME" --conflict_type ee --eval_type openqa --ty Career --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty time\
    --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty creator\
    --oringin f

python inference1_gpt.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --ty content\
    --oringin f

python inference_gpt.py \
    --test_dataset "IS.json" \
    --dataset_name IS \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin f

python inference2_gpt.py \
    --test_dataset "ED.json" \
    --dataset_name ED \
    --meta_save_path output \
    --model_name "$MODEL_NAME" \
    --conflict_type ee \
    --eval_type openqa \
    --oringin f
