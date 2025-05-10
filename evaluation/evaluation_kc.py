import json
import re
import argparse 
def extract_answer(prediction):
    """从prediction中提取第一个A、B、C或D字母（不区分大小写）"""
    if isinstance(prediction, str):
        # 使用正则表达式查找第一个A/B/C/D（忽略大小写）
        match = re.search(r'[A-Da-d]', prediction)
        if match:
            return match.group().upper()  # 返回大写的A/B/C/D
    return None  # 如果没有找到或prediction不是字符串

def compare_jsonl_files(file_a_path, file_b_path,ty):
    # 初始化统计变量
    total_count = 0
    filtered_count = 0  # 被过滤掉的条目数
    match_count = 0
    mismatch_count = 0
    confused_count = 0
    missing_in_b = 0
    a_missing_answer = 0
    b_missing_answer = 0
    
    # 用于存储b文件的内容，以instance为键
    b_data = {}
    
    # 首先读取b文件，建立instance到数据的映射
    with open(file_b_path, 'r', encoding='utf-8') as b_file:
        for line in b_file:
            try:
                data = json.loads(line)
                instance = data.get('instance')
                if instance is not None:
                    b_data[instance] = data
            except json.JSONDecodeError:
                print(f"警告: 无法解析b文件中的一行: {line}")
    
    # 然后读取a文件进行比较
    with open(file_a_path, 'r', encoding='utf-8') as a_file:
        for line in a_file:
            try:
                a_data = json.loads(line)
                a_instance = a_data.get('instance')
                a_prediction = a_data.get('prediction')
                
                if a_instance is None:
                    print(f"警告: a文件中有一行缺少instance字段: {line}")
                    continue
                
                # 检查是否需要过滤（prediction等于"mcq_disanswer1"）
                if a_prediction == a_data.get(f"mcq_disanswer_{ty}_1"):
                    filtered_count += 1
                    continue
                
                total_count += 1
                
                # 查找b文件中对应的数据
                b_item = b_data.get(a_instance)
                if b_item is None:
                    missing_in_b += 1
                    print(f"警告: instance '{a_instance}' 在b文件中不存在")
                    continue
                
                b_prediction = b_item.get('prediction')
                b_disanswer1=b_item.get(f"mcq_disanswer_{ty}_1")
                # 提取答案
                a_answer = extract_answer(a_prediction)
                b_answer = extract_answer(b_prediction)
                
                if a_answer is None:
                    a_missing_answer += 1
                    print(f"警告: a文件instance '{a_instance}' 无法从prediction中提取答案: {a_prediction}")
                    continue
                
                if b_answer is None:
                    b_missing_answer += 1
                    print(f"警告: b文件instance '{a_instance}' 无法从prediction中提取答案: {b_prediction}")
                    continue
                
                # 比较答案
                if a_answer == b_answer:
                    match_count += 1
                else:
                    if b_answer==b_disanswer1:
                        confused_count +=1
                    mismatch_count += 1
                    #print(f"差异: instance '{a_instance}' - a答案: {a_answer}, b答案: {b_answer}")
                    
            except json.JSONDecodeError:
                print(f"警告: 无法解析a文件中的一行: {line}")
    
    # 打印统计结果
    '''
    print("\n统计结果:")
    print(f"a文件总条目数: {total_count + filtered_count}")
    print(f"过滤掉的条目数(prediction=='mcq_disanswer1'): {filtered_count}")
    print(f"参与比较的条目数: {total_count}")
    print(f"答案匹配数: {match_count}")
    print(f"答案不匹配数: {mismatch_count}")
    print(f"b文件中缺失的instance数: {missing_in_b}")
    print(f"a文件中无法提取答案数: {a_missing_answer}")
    print(f"b文件中无法提取答案数: {b_missing_answer}")'''
    print(f"有效比较数: {match_count + mismatch_count}")
    print(f"知识保持率: {(match_count/(match_count + mismatch_count))*100:.2f}%" if (match_count + mismatch_count) > 0 else "匹配率: N/A")
    print(f"知识误导率: {(confused_count/(match_count + mismatch_count))*100:.2f}%")
    print(f"无关之事率: {100-(match_count/(match_count + mismatch_count)+confused_count/(match_count + mismatch_count))*100:.2f}%")
    return {
        'total_entries': total_count + filtered_count,
        'filtered_count': filtered_count,
        'compared_count': total_count,
        'match_count': match_count,
        'mismatch_count': mismatch_count,
        'missing_in_b': missing_in_b,
        'a_missing_answer': a_missing_answer,
        'b_missing_answer': b_missing_answer,
        'valid_comparisons': match_count + mismatch_count,
        'match_rate': match_count / (match_count + mismatch_count) if (match_count + mismatch_count) > 0 else 0
    }
def compare_jsonl_files1(file_a_path, file_b_path,ty):
    # 初始化统计变量
    total_count = 0
    filtered_count = 0  # 被过滤掉的条目数
    match_count = 0
    mismatch_count = 0
    confused_count = 0
    missing_in_b = 0
    a_missing_answer = 0
    b_missing_answer = 0
    
    # 用于存储b文件的内容，以instance为键
    b_data = {}
    
    # 首先读取b文件，建立instance到数据的映射
    with open(file_b_path, 'r', encoding='utf-8') as b_file:
        for line in b_file:
            try:
                data = json.loads(line)
                instance = data.get('instance')
                if instance is not None:
                    b_data[instance] = data
            except json.JSONDecodeError:
                print(f"警告: 无法解析b文件中的一行: {line}")
    
    # 然后读取a文件进行比较
    with open(file_a_path, 'r', encoding='utf-8') as a_file:
        for line in a_file:
            try:
                a_data = json.loads(line)
                a_instance = a_data.get('instance')
                a_prediction = a_data.get('prediction')
                
                if a_instance is None:
                    print(f"警告: a文件中有一行缺少instance字段: {line}")
                    continue
                
                # 检查是否需要过滤（prediction等于"mcq_disanswer1"）
                if a_prediction == a_data.get(f"mcq_disanswer_{ty}_1") or a_prediction ==a_data.get(f"mcq_disanswer_{ty}_2") :
                    filtered_count += 1
                    continue
                
                total_count += 1
                
                # 查找b文件中对应的数据
                b_item = b_data.get(a_instance)
                if b_item is None:
                    missing_in_b += 1
                    print(f"警告: instance '{a_instance}' 在b文件中不存在")
                    continue
                
                b_prediction = b_item.get('prediction')
                b_disanswer1=b_item.get(f"mcq_disanswer_{ty}_1")
                b_disanswer2=b_item.get(f"mcq_disanswer_{ty}_2")
                # 提取答案
                a_answer = extract_answer(a_prediction)
                b_answer = extract_answer(b_prediction)
                
                if a_answer is None:
                    a_missing_answer += 1
                    print(f"警告: a文件instance '{a_instance}' 无法从prediction中提取答案: {a_prediction}")
                    continue
                
                if b_answer is None:
                    b_missing_answer += 1
                    print(f"警告: b文件instance '{a_instance}' 无法从prediction中提取答案: {b_prediction}")
                    continue
                
                # 比较答案
                if a_answer == b_answer:
                    match_count += 1
                else:
                    if b_answer==b_disanswer1 or b_answer==b_disanswer2:
                        confused_count +=1
                    mismatch_count += 1
                    #print(f"差异: instance '{a_instance}' - a答案: {a_answer}, b答案: {b_answer}")
                    
            except json.JSONDecodeError:
                print(f"警告: 无法解析a文件中的一行: {line}")
    
    # 打印统计结果
    '''
    print("\n统计结果:")
    print(f"a文件总条目数: {total_count + filtered_count}")
    print(f"过滤掉的条目数(prediction=='mcq_disanswer1'): {filtered_count}")
    print(f"参与比较的条目数: {total_count}")
    print(f"答案匹配数: {match_count}")
    print(f"答案不匹配数: {mismatch_count}")
    print(f"b文件中缺失的instance数: {missing_in_b}")
    print(f"a文件中无法提取答案数: {a_missing_answer}")
    print(f"b文件中无法提取答案数: {b_missing_answer}")'''
    print(f"有效比较数: {match_count + mismatch_count}")
    print(f"知识保持率: {(match_count/(match_count + mismatch_count))*100:.2f}%" if (match_count + mismatch_count) > 0 else "匹配率: N/A")
    print(f"知识误导率: {(confused_count/(match_count + mismatch_count))*100:.2f}%")
    print(f"无关之事率: {100-(match_count/(match_count + mismatch_count)+confused_count/(match_count + mismatch_count))*100:.2f}%")
    return {
        'total_entries': total_count + filtered_count,
        'filtered_count': filtered_count,
        'compared_count': total_count,
        'match_count': match_count,
        'mismatch_count': mismatch_count,
        'missing_in_b': missing_in_b,
        'a_missing_answer': a_missing_answer,
        'b_missing_answer': b_missing_answer,
        'valid_comparisons': match_count + mismatch_count,
        'match_rate': match_count / (match_count + mismatch_count) if (match_count + mismatch_count) > 0 else 0
    }
# 使用示例
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='比较两个JSONL文件的内容')
    
    # 添加必需的参数 
    parser.add_argument('--file_a',  required=True, help='第一个JSONL文件路径')
    parser.add_argument('--file_b',  required=True, help='第二个JSONL文件路径')
    parser.add_argument("--conflict_type",type=str, required=True, choices=["ie", "ee"],help="冲突类型") 
    parser.add_argument("--ty",type=str, required=True, help="冲突类型") 

    # 解析参数 
    args = parser.parse_args() 
    if args.conflict_type=='ie':
    # 调用比较函数 
        results = compare_jsonl_files(args.file_a,  args.file_b,args.ty) 
    if args.conflict_type=='ee':
        results = compare_jsonl_files1(args.file_a,  args.file_b,args.ty) 