# make_training_set

制作类似[CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)的数据集.

原理： 将组织好的数据结构 使用python的[pickle](https://docs.python.org/3/library/pickle.html)模块 dump到一个文件里.

数据结构:

```python
data_set = {
    "batch_label": "ten pictures form http://shixin.court.gov.cn",  # 关于对数据集的描述信息
    "labels": None,    # 图片标签信息 python 列表
    "data": None,      # 每一张图片转换成RGB三个矩阵, 每个矩阵展平, 然后按RGB的顺序拼接起一个 3*width*height 长度的向量.
    "filenames": None  # 图片文件名 python 列表
}

```

感谢[Jimmy](http://blog.csdn.net/qq_32166627/article/details/68946809)的思路.

