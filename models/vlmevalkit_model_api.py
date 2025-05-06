import os
import sys

# 添加 VLMEvalKit 目录到 sys.path
vlmevalkit_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'VLMEvalKit')
sys.path.append(vlmevalkit_path)

# 打印 sys.path 以检查路径是否正确添加
# print("Current sys.path:", sys.path)

from vlmeval.config import supported_VLM

import argparse
import torch
import json
from tqdm import tqdm
import shortuuid
import copy
import hashlib
from PIL import Image
import logging
from constants import *
import time
logger = logging.getLogger(__name__)


import re

logger = logging.getLogger(__name__)


class VLMEvalModel:
    def __init__(self, model_type):
        model_name = model_type.split('vlmevalkit_')[-1]
        self.model = supported_VLM[model_name](max_new_tokens=512)

    # for onevision interleaved
    def infer(self, messages,idx):
        '''
        image_files: a list of image file path or bytes (could be directly loaded with Image.open()). The order of the image files is the same order to LMM.
        text_query: the instruction to the LMM. We use '<image>' to denote the place for an image.
        '''
        response = None

        while response is None:
            try:
                response = self.model.generate(message = messages, dataset='MathVerse_MINI_Vision_Only') # the dataset here is only for not throwing an error

                return (True,idx,response)


            except Exception as e:
                print(f"Error occurred: {e}")
                print('Retrying...')
                time.sleep(1)  # 等待一秒后重试
                continue


'''
IMAGE_PTH = 'assets/apple.jpg'
IMAGE_URL = 'https://raw.githubusercontent.com/open-compass/VLMEvalKit/main/assets/apple.jpg'
msg1 = [IMAGE_PTH, 'What is in this image?']
msg2 = [IMAGE_URL, IMAGE_URL,  'How many apples are there in these images?']
response = model.generate(msg1)

message = [
    dict(role='user', content=msg1),
    dict(role='assistant', content=msg2),
    dict(role='user', content=msg3),
    dict(role='assistant', content=msg4),
	......
    dict(role='user', content=msgn),
]
response = model.chat(message)
'''
