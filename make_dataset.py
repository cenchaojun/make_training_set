#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>

import os
import glob
import pickle
import string
from pprint import pprint
from PIL import Image
import numpy as np

characters = string.digits + string.ascii_lowercase

# 目标分别率 长*宽
target_pixel = (160, 70)


data_set = {
    "batch_label": "ten pictures form http://shixin.court.gov.cn",  # description
    "labels": None,     # list
    "data": None,       # <class 'numpy.ndarray'>
    "filenames": None,  # list ['leptodactylus_pentadactylus_s_000004.png', 'camion_s_000148.png',]
    "shape": (),        #
}

labels = []
data = []
filenames = []

count = 0
for infile in glob.glob("./pics/*.jpg"):
    filename = os.path.basename(infile)
    file, ext = os.path.splitext(infile)
    y = np.zeros([4, len(characters)], dtype=np.uint8)

    try:
        image = Image.open(infile)
    except OSError:
        print("图片错误")
        continue
    else:
        count += 1
    if count > 10000:
        break

    width, height = image.size

    if image.size != target_pixel:
        print("分辨率不同")
        continue

    label = str(filename).split("_")[0]

    # print(image.mode)   # RGBA A Alpha的色彩空间，也就是透明度/不透明度
    if image.mode != "RGB":
        image = image.convert("RGB")

    shape = np.array(image).shape
    data_set.update({"shape": shape})
    data.append(np.array(image).reshape([shape[0] * shape[1] * shape[2]]))
    for j, ch in enumerate(label):
        y[j][characters.find(ch)] = 1

    labels.append(y)
    filenames.append(str(filename))


data_set.update({"labels": labels, "data": data, "filenames": filenames})

pprint(data_set)
with open('./example/data_batch_1', 'wb') as file:
    pickle.dump(data_set, file)



