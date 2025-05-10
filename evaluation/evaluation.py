import os 
import glob 
import os

def change_path(path):
    dir_part, filename = os.path.split(path) 
    dir_part = dir_part.replace("original",  "output")
    output_path = os.path.join(dir_part,  filename)
    return output_path

def change_path_ie(original_path):
    new_path = original_path.replace("_ee.jsonl",  "_ie.jsonl")
    return new_path

def get_Types(path):
    dir_name = os.path.basename(os.path.dirname(path)) 
    return dir_name

def get_modelname(path):
    # 尝试按 mcq_ 或 openqa_ 分割
    parts = path.split("mcq_")  if "mcq_" in path else path.split("openqa_") 
    if len(parts) < 2:
        raise ValueError(f"无法从路径中提取模型名: {path}")
    return parts[1].split("_")[0]  # 提取第一个下划线前的内容

def get_kc(path):
    filename = path.split("/")[-1]
    target_part = filename.split("_ee")[0]
    content = target_part.split("_")[-1]
    return content
def get_mcq(path):
    filename = path.split("/")[-1]
    openqa = filename.split("_")[0]
    return openqa

def find_jsonl_files_in_original(root_dir):
    """
    查找大文件夹下original子目录中所有小文件夹内的.jsonl文件路径 
    
    参数:
        root_dir (str): 大文件夹的路径 
        
    返回:
        list: 包含所有找到的.jsonl文件完整路径的列表 
    """
    jsonl_files = []
    
    # 构建original目录的路径 
    original_dir = os.path.join(root_dir,  "original")
    
    # 检查original目录是否存在 
    if not os.path.exists(original_dir): 
        print(f"警告: 未找到original目录: {original_dir}")
        return jsonl_files 
    
    # 遍历original下的所有小文件夹 
    for subdir in os.listdir(original_dir): 
        subdir_path = os.path.join(original_dir,  subdir)
        
        # 确保是目录 
        if os.path.isdir(subdir_path): 
            # 使用glob查找所有.jsonl文件 
            files = glob.glob(os.path.join(subdir_path,  "*.jsonl"))
            jsonl_files.extend(files) 
    
    return jsonl_files 
 
if __name__ == "__main__":
    # 用户输入大文件夹路径 
    root_path = input("请输入大文件夹的路径: ").strip()
    file_list = []
    # 查找文件 
    found_files = find_jsonl_files_in_original(root_path)
    
    # 输出结果 
    if found_files:
        
        for file_path in found_files:
            file_list.append(file_path)
        print(f"\n共找到 {len(found_files)} 个.jsonl文件")
    else:
        print("未找到任何.jsonl文件")
    for i in range(len(file_list)):
        model_name = 'llava-next-llama'
        
        types = get_Types(file_list[i])
        
        mcq = get_mcq(file_list[i])
        if mcq == 'openqa':
            continue
        
        if types =='ER':
            ee_file = change_path(file_list[i])
            print(f'{model_name}在实体识别外外冲突下的结果为:')
            os.system(f"python  evaluation_er.py  --file_a {file_list[i]} --file_b {ee_file} --conflict_type ee")
            ie_file = change_path_ie(ee_file)
            print(f'{model_name}在实体识别内外冲突下的结果为:')
            os.system(f"python  evaluation_er.py  --file_a {file_list[i]} --file_b {ie_file} --conflict_type ie")
        if types =='ED':
            ee_file = change_path(file_list[i])
            print(f'{model_name}在图表数据外外冲突下的结果为:')
            os.system(f"python  evaluation_ed.py  --file_a {file_list[i]} --file_b {ee_file} --conflict_type ee")
            ie_file = change_path_ie(ee_file)
            print(f'{model_name}在图表数据内外冲突下的结果为:')
            os.system(f"python  evaluation_ed.py  --file_a {file_list[i]} --file_b {ie_file} --conflict_type ie")
        if types =='IS':
            ee_file = change_path(file_list[i])
            print(f'{model_name}在图像语义外外冲突下的结果为:')
            os.system(f"python  evaluation_is.py  --file_a {file_list[i]} --file_b {ee_file} --conflict_type ee")
            ie_file = change_path_ie(ee_file)
            print(f'{model_name}在图像语义内外冲突下的结果为:')
            os.system(f"python  evaluation_is.py  --file_a {file_list[i]} --file_b {ie_file} --conflict_type ie")
        if types =='people_knowledge':
            kc = get_kc(file_list[i])
            ee_file = change_path(file_list[i])
            print(f'{model_name}在人物知识下{kc}外外冲突下的结果为:')
            os.system(f"python  evaluation_kc.py  --file_a {file_list[i]} --file_b {ee_file} --conflict_type ee --ty {kc}")
            ie_file = change_path_ie(ee_file)
            print(f'{model_name}在人物知识下{kc}内外冲突下的结果为:')
            os.system(f"python  evaluation_kc.py  --file_a {file_list[i]} --file_b {ie_file} --conflict_type ie --ty {kc}")
        if types =='logo_knowledge':
            kc = get_kc(file_list[i])
            ee_file = change_path(file_list[i])
            print(f'{model_name}在logo知识下{kc}外外冲突下的结果为:')
            os.system(f"python  evaluation_kc.py  --file_a {file_list[i]} --file_b {ee_file} --conflict_type ee --ty {kc}")
            ie_file = change_path_ie(ee_file)
            print(f'{model_name}在logo知识下{kc}内外冲突下的结果为:')
            os.system(f"python  evaluation_kc.py  --file_a {file_list[i]} --file_b {ie_file} --conflict_type ie --ty {kc}")
        
