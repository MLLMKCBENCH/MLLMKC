## Table of Contents

- [Table of Contents](#table-of-contents)
- [🔔 News](#-news)
- [🌟 Overview](#overview)
- [🤗 Dataset](#-dataset)
- [🛠️ Requirements and Installation](#️-requirements-and-installation)
- [💥 Inference](#training)




## 🔔 News


* **[2025.5.16]**  **Code** is available now!

* **[2025.5.16]**  We release the **MMKE-Bench dataset** at 🤗 [Huggingface Dataset](https://huggingface.co/datasets/starjyf/MLLMKC-dataset).




## 🌟Overview

**TL;DR:** We propose <span style="color:brown">**MLLMKC**</span>, a challenging benchmark for evaluating factual multi-modal knowledge conflict.

<img src="figs\fig1.png" width="900px">

<p align="justify">
    <strong><span style="color:black">Overview</span> of the <span style="color:brown">MLMMKC</span> dataset. Our contribution can be summarized as follows:</strong>
</p>


<p align="justify" style="margin-left: 30px; text-indent: -30px;">
    <strong><span style="color:black">1) Overview of MLLMKC</span></strong>: 
    MLLMKC is a benchmark for evaluating how multimodal large models perform in the face of factuality conflicts. It is made from factual instances and includes four conflict types depending on the actual situation.
</p>


<p align="justify" style="margin-left: 30px; text-indent: -30px;">
    <strong><span style="color:black">2) Development of the Benchmark Pipeline</span></strong>: 
    Describes the novel pipeline used to develop the benchmark, which includes collecting original knowledge, generating counterfactual knowledge, and formulate the evaluation questions according to the type of conflict.
</p>


<p align="justify" style="margin-left: 30px; text-indent: -30px;">
    <strong><span style="color:black">3) Experimental Analysis and Challenges</span></strong>: 
    xxx
</p>

## 🤗 Dataset

<p align="justify">
We introduce <strong><span style="color:brown">MMKE-Bench</span></strong>, a benchmark designed to evaluate the ability of LMMs to edit visual knowledge in real-world scenarios. <strong><span style="color:brown">MMKE-Bench</span></strong> incorporates three editing tasks: <strong><span style="color:brown">visual entity editing</span></strong>, <strong><span style="color:brown">visual semantic editing</span></strong>, and <strong><span style="color:brown">user-specific editing</span></strong>. Additionally, it uses free-form natural language to represent and edit knowledge, offering more flexibility. The benchmark includes <strong><span style="color:brown">2,940</span></strong> pieces of knowledge and <strong><span style="color:brown">7,229</span></strong> images across 110 fine-grained types, with automatically generated, human-verified evaluation questions.
</p>


You can download **MMKE-Bench data** 🤗 [Huggingface Dataset](https://huggingface.co/datasets/starjyf/MLLMKC-dataset). And the expected structure of files is:

```text
MLLMKC
|-- image
|   |-- nike
|   |-- kobe
|   |-- .....
|-- ER.json
|-- people_knowledge.json
|-- logo_knowledge.json
|-- IS.json
|-- ED.json
```

## 🛠️ Requirements and Installation

```text
# clone MMKE-Bench
git clone https://github.com/MLLMKCBENCH/MLLMKC.git

cd MLLMKC

# create conda env
conda create -n mllmkc python=3.10

cd VLMEvalKit

pip install -r requirements.txt

```


## 💥Inference
**If you want to use local model weights, download them ahead of time:** And in VLMEvalKit/vlmeval/config.py change local weight inside

**Began to replace sh file to review the model name, name and VLMEvalKit vlmeval/config.py offer is consistent with the name of the file.**

For non-GPT models：
**For The original answer(mcq):**
```shell
bash start_original_mcq.sh
```

**For The internal and external conflicts answer(mcq):**
```shell
bash start_mcq_ie.sh
```

**For The external and external conflicts answer(mcq):**
```shell
bash start_mcq_ee.sh
```

**For The original answer(openqa):**
```shell
bash start_original_open.sh
```

**For The internal and external conflicts answer(openqa):**
```shell
bash start_open_ie.sh
```

**For The external and external conflicts answer(openqa):**
```shell
bash start_open_ee.sh
```

For GPT models：
**For The external and external conflicts answer(openqa):**
```shell
bash start_gpt.sh
```

**For Coarse-grained conflict detection:**
```shell
bash detection.sh
```
**For fine-grained conflict detection:**
```shell
bash detection_xin.sh
```


    



