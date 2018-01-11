#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>

import random
import pickle
from pprint import pprint
from PIL import Image

with open("./example/data_batch_1", 'rb') as file:
    entry = pickle.load(file, encoding='utf-8')
    pprint(entry)
    shape = entry.get("shape")
    random_num = random.randint(0, len(entry.get("data")))
    data = entry.get("data")[random_num].reshape(shape)
    pprint("标签: {}".format(entry.get("labels")[random_num]))
    Image.fromarray(data).show()
