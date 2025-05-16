MODEL_NAME="llava_next_llama3"
python inference1_d_x.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path detection_x \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty temporal\
    --oringin f

python inference1_d_x.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path detection_x \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty location\
    --oringin f

python inference1_d_x.py \
    --test_dataset "people_knowledge.json" \
    --dataset_name people_knowledge \
    --meta_save_path detection_x \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty Carrer\
    --oringin f

python inference1_d_x.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path detection_x \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty time\
    --oringin f

python inference1_d_x.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path detection_x \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty creator\
    --oringin f

python inference1_d_x.py \
    --test_dataset "logo_knowledge.json" \
    --dataset_name logo_knowledge \
    --meta_save_path detection_x \
    --model_name "$MODEL_NAME" \
    --conflict_type ie \
    --eval_type openqa \
    --ty content\
    --oringin f