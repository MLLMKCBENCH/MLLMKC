## 1. Environment Installation
```bash
cd VLMEvalKit
pip install -r requirements.txt
# If any packages are missing, install them individually with pip install
```
## 2. DATA
```
|______LLMKC
|______image
    |_________nike
    |_________kobe
    |_________....
|______ER.json
|______people_knowledge.json
|______logo_knowledge.json
|______IS.json
|______ED.json
```
## 3.命令脚本
```bash

original_mcq:bash start_original_mcq.sh

original_openqa:bash start_original_mcq.sh

mcq_ie:bash start_mcq_ie.sh

mcq_ee:bash start_mcq_ee.sh

open_ie:bash start_mcq_ie.sh

open_ee:bash start_mcq_ee.sh
```
## 4.在sh文件里换模型的类型
```
MODEL_NAME="这里填写你的模型"
```



