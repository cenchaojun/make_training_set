#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>

import random
import pickle
from pprint import pprint
from PIL import Image

with open("./example/data_batch_1", 'rb') as file:
    entry = pickle.load(file, encoding='utf-8')
    # pprint(entry.keys())
    # pprint(entry.get("filenames"))
    # pprint(entry.get("batch_label"))  # string
    # pprint(entry.get("data"))
    pprint(entry)
    random_num = random.randint(0, len(entry.get("data")))
    data = entry.get("data")[random_num].reshape(3, 70, 160).transpose([1, 2, 0])
    pprint("标签: {}".format(entry.get("labels")[random_num]))
    Image.fromarray(data, mode="RGB").show()
