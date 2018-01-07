#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>

import pickle
from PIL import Image

with open("./example/data_batch_1", 'rb') as file:
    entry = pickle.load(file, encoding='latin1')
    # print(entry)
    # print(entry.keys())
    # print(entry.get("filenames"))
    # print(entry.get("batch_label"))  # string
    print(entry.get("data"))
    data = entry.get("data")[0].reshape(3, 70, 160).transpose([1, 2, 0])
    Image.fromarray(data, mode="RGB").show()
