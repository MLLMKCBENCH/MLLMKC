import threading
from concurrent.futures import ThreadPoolExecutor
import os
import json
import asyncio
import argparse
from typing import Tuple, Dict, Any, List
from models.vlmevalkit_model_api import VLMEvalModel

class OpenVLM:
    def __init__(self, model_type: str):
        self.model = VLMEvalModel(model_type=model_type)
    
    def ask_vlm(self, messages: List[Dict[str, Any]], idx: int) -> Tuple[bool, int, Dict[str, Any]]:
        """
        调用 VLM 模型获取回答
        """
        return self.model.infer(messages, idx)

def get_conflict_message(item, conflict_type,ty):
    conflict_message = ["The following information is provided externally:"]
    question_image = None  # Initialize question_image
    
    if conflict_type == "ee":
        if ty == 'temporal':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["Temporal_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["Temporal_error"]["mis_knowledge2"]
            correct_text = item["knowledge"]
            conflict_message.extend([external_image,correct_text])
        if ty=='location':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["location_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["location_error"]["mis_knowledge2"]
            correct_text = item["knowledge"]
            conflict_message.extend([external_image,correct_text])
        if ty=='Career':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["Career_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["Career_error"]["mis_knowledge2"]
            correct_text = item["knowledge"]
            conflict_message.extend([external_image,correct_text])
        if ty=='time':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["time_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["time_error"]["mis_knowledge2"]
            correct_text = item["knowledge"]
            conflict_message.extend([external_image,correct_text])
        if ty=='creator':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["creator_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["creator_error"]["mis_knowledge2"]
            conflict_message.extend([external_image, correct_text])
        if ty=='content':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["content_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["content_error"]["mis_knowledge2"]
            conflict_message.extend([external_image, correct_text])
    elif conflict_type == "ie":
        if ty == 'temporal':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["Temporal_error"]["mis_knowledge1"]
            sentences = [s.strip() for s in external_text.split('. ') if s]
            m = sentences[0] if len(sentences) > 2 else ""
            conflict_message.extend([external_image, m])
        if ty=='location':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["location_error"]["mis_knowledge1"]
            sentences = [s.strip() for s in external_text.split('. ') if s]
            m = sentences[1] if len(sentences) > 2 else ""
            m =sentences[1]
            conflict_message.extend([external_image, m])
        if ty=='Career':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["Career_error"]["mis_knowledge1"]
            sentences = [s.strip() for s in external_text.split('. ') if s]
            m = sentences[2] if len(sentences) > 2 else ""
            m =sentences[2]
            conflict_message.extend([external_image, m])
        if ty=='time':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["time_error"]["mis_knowledge1"]
            sentences = [s.strip() for s in external_text.split('. ') if s]
            m = sentences[0] if len(sentences) > 2 else ""
            conflict_message.extend([external_image, m])
        if ty=='creator':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["creator_error"]["mis_knowledge1"]
            sentences = [s.strip() for s in external_text.split('. ') if s]
            m = sentences[1] if len(sentences) > 2 else ""
            conflict_message.extend([external_image, m])
        if ty=='content':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["content_error"]["mis_knowledge1"]
            sentences = [s.strip() for s in external_text.split('. ') if s]
            m = sentences[2] if len(sentences) > 2 else ""
            conflict_message.extend([external_image, m])
                    
    else:
        raise ValueError("conflict_type must be 'ie' or 'visual_conflict'")
    
    if question_image is None:
        raise ValueError("question_image was not set - check conflict_type and item structure")
    
    return conflict_message, question_image

def get_query_instruction_prompt(dataset, eval_type,tye='temporal'):
    instruction_prompt = {
        'openqa_query': "Read the following document carefully and answer No if it does not agree with what you remember, and Yes if it does.",
        'mcq_query': "Answer with the option's letter from the given choices directly based on the context and the image."}
    
    if eval_type == 'openqa':
         if tye=='temporal':
            return dataset['open_query_temporal'], instruction_prompt['openqa_query']
         if tye=='location':
             return dataset['open_query_location'], instruction_prompt['openqa_query']
         if tye=='Career':
             return dataset['open_query_Career'], instruction_prompt['openqa_query']
         if tye=='time':
             return dataset['open_query_time'], instruction_prompt['openqa_query']
         if tye=='creator':
             return dataset['open_query_creator'], instruction_prompt['openqa_query']
         if tye=='content':
             return dataset['open_query_content'], instruction_prompt['openqa_query']
    elif eval_type == 'mcq':
        if tye=='temporal':
            return dataset['mcq_query_temporal'], instruction_prompt['mcq_query']
        if tye=='location':
            return dataset['mcq_query_location'], instruction_prompt['mcq_query']
        if tye=='Career':
             return dataset['mcq_query_Career'], instruction_prompt['mcq_query']
        if tye=='time':
             return dataset['mcq_query_time'], instruction_prompt['mcq_query']
        if tye=='creator':
             return dataset['mcq_query_creator'], instruction_prompt['mcq_query']
        if tye=='content':
             return dataset['mcq_query_content'], instruction_prompt['mcq_query']
    else:
        return None, "Invalid eval_type. Please choose 'openqa' or 'mcq'."

def process_item(item, final_message, model_name,qa_agent: OpenVLM):
    idx = item['ID']
    success, idx, answer = qa_agent.ask_vlm(final_message, idx)
    return success, idx, answer

def main(test_dataset, dataset_name, meta_save_path, model_name, conflict_type, eval_type,ty,oringin):
    
    with open(test_dataset, "r", encoding="utf-8") as f:
        dataset = json.load(f) 

    output_path = os.path.join(meta_save_path, dataset_name, f"{eval_type}_{model_name}_{ty}_{conflict_type}.jsonl")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if os.path.exists(output_path):
        with open(output_path, "r") as fin:
            done_id = [json.loads(data)['ID'] for data in fin.readlines()]
            dataset = [data for data in dataset if data['ID'] not in done_id]
    qa_agent = OpenVLM(model_type=model_name)
    from tqdm import tqdm
    # import json
    with open(output_path, "a", encoding="utf-8") as fout:
        for item in tqdm(dataset, desc="Processing items"):
            conflict_messsage,image = get_conflict_message(item, conflict_type,ty)  
            query_prompt, instruction = get_query_instruction_prompt(item, eval_type,ty)
            ss = conflict_messsage[1]
            print(ss)
            if ss =='':
                continue
            if oringin=="t":
                final_message = [query_prompt, instruction]  +[image]
            if oringin=="f":
                final_message =[instruction]+conflict_messsage
            print('------------------------------------------')
            print('final_message:', final_message)
            print('------------------------------------------')

            success, idx, answer = process_item(item, final_message, model_name,qa_agent)
            item['success'] = success
            item['prediction'] = answer
            print('------------------------------------------')
            print("请注意模型的回答如下：")
            print(answer)

            fout.write(json.dumps(item, ensure_ascii=False) + "\n")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="运行指定的数据集")
    parser.add_argument("--test_dataset", type=str, required=True, help="数据集路径")
    parser.add_argument("--dataset_name", type=str, required=True, help="数据集名称")
    parser.add_argument("--meta_save_path", type=str, required=True, help="存储路径")
    parser.add_argument("--model_name",type=str, required=True, help="请输入模型名称")
    parser.add_argument("--conflict_type",type=str, required=True, choices=["ie", "ee"],help="冲突类型") 
    parser.add_argument("--eval_type",type=str, required=True, choices=["openqa", "mcq"],help="评估类型")
    parser.add_argument("--oringin",type=str, required=True, choices=["t", "f"],help="评估类型")
    parser.add_argument("--ty",type=str, required=True,help="评估类型") 
    args = parser.parse_args()

    main(args.test_dataset,args.dataset_name, args.meta_save_path, args.model_name, args.conflict_type, args.eval_type,args.ty,args.oringin)