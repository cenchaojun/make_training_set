#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>

import os
import glob
import pickle
from PIL import Image
import numpy as np


data_set = {
    "batch_label": "ten pictures form http://shixin.court.gov.cn",  # description
    "labels": None,    # list
    "data": None,      # <class 'numpy.ndarray'>
    "filenames": None  # list ['leptodactylus_pentadactylus_s_000004.png', 'camion_s_000148.png',]
}

labels = []
data = []
filenames = []

count = 0
for infile in glob.glob("./pics/*.jpg"):
    filename = os.path.basename(infile)
    file, ext = os.path.splitext(infile)

    try:
        image = Image.open(infile)
    except OSError:
        print("图片错误")
        continue
    count += 1
    if count > 100000:
        break

    width, height = image.size

    label = str(filename).split("_")[0]

    # print(image.mode)   # RGBA A Alpha的色彩空间，也就是透明度/不透明度
    if image.mode != "RGB":
        image = image.convert("RGB")

    r, g, b = image.split()
    r_array = np.array(r).reshape([width * height])
    g_array = np.array(g).reshape([width * height])
    b_array = np.array(b).reshape([width * height])
    merge_array = np.concatenate((r_array, g_array, b_array))
    data.append(merge_array)
    labels.append(label)
    filenames.append(str(filename))


data_set.update({"labels": labels, "data": data, "filenames": filenames})


with open('./example/data_batch_1', 'wb') as file:
    pickle.dump(data_set, file)



