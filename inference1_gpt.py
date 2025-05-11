import threading
from concurrent.futures import ThreadPoolExecutor
import os
import json
import asyncio
import argparse
from typing import Tuple, Dict, Any, List
from models.vlmevalkit_model_api import VLMEvalModel
import base64 
from openai import OpenAI
class OpenVLM:
    def __init__(self, model_type: str):
        self.model = VLMEvalModel(model_type=model_type)
    
    def ask_vlm(self, messages: List[Dict[str, Any]], idx: int) -> Tuple[bool, int, Dict[str, Any]]:
        """
        调用 VLM 模型获取回答
        """
        return self.model.infer(messages, idx)

def get_conflict_message(item, conflict_type,ty):
    conflict_message = []
    question_image = None  # Initialize question_image
    
    if conflict_type == "ee":
        if ty == 'temporal':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["Temporal_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["Temporal_error"]["mis_knowledge2"]
            conflict_message.extend([external_image, external_text,external_image1,external_text1])
        if ty=='location':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["location_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["location_error"]["mis_knowledge2"]
            conflict_message.extend([external_image, external_text,external_image1,external_text1])
        if ty=='Career':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["Career_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["Career_error"]["mis_knowledge2"]
            conflict_message.extend([external_image, external_text,external_image1,external_text1])
        if ty=='time':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["time_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["time_error"]["mis_knowledge2"]
            conflict_message.extend([external_image, external_text,external_image1,external_text1])
        if ty=='creator':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["creator_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["creator_error"]["mis_knowledge2"]
            conflict_message.extend([external_image, external_text,external_image1,external_text1])
        if ty=='content':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["content_error"]["mis_knowledge1"]
            external_image1 = item["image_path"][2]
            external_text1 = item["mis_knowledge"]["content_error"]["mis_knowledge2"]
            conflict_message.extend([external_image, external_text,external_image1,external_text1])
    elif conflict_type == "ie":
        if ty == 'temporal':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["Temporal_error"]["mis_knowledge1"]
            conflict_message.extend([external_image, external_text])
        if ty=='location':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["location_error"]["mis_knowledge1"]
            conflict_message.extend([external_image, external_text])
        if ty=='Career':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["Career_error"]["mis_knowledge1"]
            conflict_message.extend([external_image, external_text])
        if ty=='time':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["time_error"]["mis_knowledge1"]
            conflict_message.extend([external_image, external_text])
        if ty=='creator':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["creator_error"]["mis_knowledge1"]
            conflict_message.extend([external_image, external_text])
        if ty=='content':
            question_image = item["image_path"][0]
            external_image = item["image_path"][1]
            external_text = item["mis_knowledge"]["content_error"]["mis_knowledge1"]
            conflict_message.extend([external_image, external_text])
                    
    else:
        raise ValueError("conflict_type must be 'ie' or 'visual_conflict'")
    
    if question_image is None:
        raise ValueError("question_image was not set - check conflict_type and item structure")
    
    return conflict_message, question_image

def get_query_instruction_prompt(dataset, eval_type,tye='temporal'):
    instruction_prompt = {
        'openqa_query': "Answer the question using a single word or phrase based on the context and the image.",
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
def gpt_inner(confict_message,question_message,model,conflict_type,oringin):

    client = OpenAI(
        # openai系列的sdk，包括langchain，都需要这个/v1的后缀
        base_url='https://api.openai-proxy.org/v1',
        api_key='sk-ifaeShm4AUoohgWo7ur4YpOBs2yaGj7p8I29PEy1niAHCDk5',
    )
    if conflict_type=="ie" and oringin=='f':
        conflict_image_path_1=confict_message[0]
        conflict_txt = confict_message[1]
        question = question_message[0]
        query = question_message[1]
        question_image_path = question_message[2]
        conflict_image = base64.b64encode(open(conflict_image_path_1, "rb").read()).decode("ascii")
        question_image = base64.b64encode(open(question_image_path, "rb").read()).decode("ascii")
        messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Here are the external images and information:"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{conflict_image}"
                }
            },
            {"type": "text", "text": f"{conflict_txt}"},
            {"type": "text", "text": f"{query}"},
            {"type": "text", "text": f"{question}"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{question_image}"
                }
            }
        ]
    }
]
        chat_completion = client.chat.completions.create(
        messages=messages,
        model=f"{model}", # 如果是其他兼容模型，比如deepseek，直接这里改模型名即可，其他都不用动
    )
    if conflict_type=="ee" and oringin=='f':
        conflict_image_path_1=confict_message[0]
        conflict_txt_1 = confict_message[1]
        conflict_image_path_2=confict_message[0]
        conflict_txt_2 = confict_message[1]
        question = question_message[0]
        query = question_message[1]
        question_image_path = question_message[2]
        conflict_image_1 = base64.b64encode(open(conflict_image_path_1, "rb").read()).decode("ascii")
        conflict_image_2 = base64.b64encode(open(conflict_image_path_2, "rb").read()).decode("ascii")
        question_image = base64.b64encode(open(question_image_path, "rb").read()).decode("ascii")
        messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Here are the external images and information:"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{conflict_image_1}"
                }
            },
            {"type": "text", "text": f"{conflict_txt_1}"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{conflict_image_2}"
                }
            },
            {"type": "text", "text": f"{conflict_txt_2}"},
            {"type": "text", "text": f"{query}"},
            {"type": "text", "text": f"{question}"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{question_image}"
                }
            }
           
        ]
    }
]
        chat_completion = client.chat.completions.create(
        messages=messages,
        model=f"{model}", # 如果是其他兼容模型，比如deepseek，直接这里改模型名即可，其他都不用动
    )
    if oringin=='t':
        conflict_image_path_1=confict_message[0]
        conflict_txt = confict_message[1]
        question = question_message[0]
        query = question_message[1]
        question_image_path = question_message[2]
        conflict_image = base64.b64encode(open(conflict_image_path_1, "rb").read()).decode("ascii")
        question_image = base64.b64encode(open(question_image_path, "rb").read()).decode("ascii")
        messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": f"{query}"},
            {"type": "text", "text": f"{question}"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{question_image}"
                }
            }
        ]
    }
]
        chat_completion = client.chat.completions.create(
        messages=messages,
        model=f"{model}", # 如果是其他兼容模型，比如deepseek，直接这里改模型名即可，其他都不用动
    )
   

    return chat_completion.choices[0].message.content
def main(test_dataset, dataset_name, meta_save_path, model_name, conflict_type, eval_type,ty,oringin):
    
    with open(test_dataset, "r", encoding="utf-8") as f:
        dataset = json.load(f) 

    output_path = os.path.join(meta_save_path, dataset_name, f"{eval_type}_{model_name}_{ty}_{conflict_type}.jsonl")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if os.path.exists(output_path):
        with open(output_path, "r") as fin:
            done_id = [json.loads(data)['ID'] for data in fin.readlines()]
            dataset = [data for data in dataset if data['ID'] not in done_id]
    
    from tqdm import tqdm
    # import json
    with open(output_path, "a", encoding="utf-8") as fout:
        for item in tqdm(dataset, desc="Processing items"):
            conflict_messsage,image = get_conflict_message(item, conflict_type,ty)  
            query_prompt, instruction = get_query_instruction_prompt(item, eval_type,ty)
            if oringin=="t":
                final_message = [query_prompt, instruction]  +[image]
            if oringin=="f":
                final_message =conflict_messsage+[query_prompt, instruction]  +[image]
            question_message = [query_prompt, instruction,image]
            print('------------------------------------------')
            print('final_message:', final_message)
            print('------------------------------------------')

            answer = gpt_inner(conflict_messsage, question_message, model_name,conflict_type,oringin)
            
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