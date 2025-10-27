---
title: 部署一个利用人工智能进行静态病毒检测的网站
url: https://buaq.net/go-167430.html
source: unSafe.sh - 不安全
date: 2023-06-06
fetch_date: 2025-10-04T11:46:18.352713
---

# 部署一个利用人工智能进行静态病毒检测的网站

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/37ce41239004ea78b8160b03b3433efe.jpg)

部署一个利用人工智能进行静态病毒检测的网站

整体设计思路对于人工检测病毒来说，不管是静态分析，还是动态分析，直接分析是十分消耗精力的，需要大量专家信息作为辅助。而对于机器学习，特别是深度学习来说，端到端的神经
*2023-6-5 23:46:12
Author: [xz.aliyun.com(查看原文)](/jump-167430.htm)
阅读量:49
收藏*

---

## 整体设计思路

对于人工检测病毒来说，不管是静态分析，还是动态分析，直接分析是十分消耗精力的，需要大量专家信息作为辅助。而对于机器学习，特别是深度学习来说，端到端的神经网络雨后春笋般的出现。能够把深度学习引入到病毒检测将大大减轻人工的负担，我们需要做的就是优化网络结构并挑选出更有代表性的特征。

对于静态分析来说，可以将代码当成nlp中的语句，或者是将文件抽象成 CNN 中的图像，来更好的识别一个文件的静态特征。对于动态分析而言，把 api 调用链当成特征也是十分自然。当然还有很多选择的方式。本次选择的方案 CNN 。

这个 CNN 处理思路是看一篇[论文](https://ieeexplore.ieee.org/document/8328749)得到的，用的数据集是微软的[微软恶意软件分类挑战](https://www.kaggle.com/competitions/malware-classification/data)的。这个数据集一百多个G，转成灰度图更是能跑好久好久，差不多跑了4个小时。下边开始介绍，主要分成三个点：

* 图像预处理
* VGG神经网络
* 搭建部署上线

## 前言：理论支撑

> 如何抽取特征以及特征为什么有效？

关于如何将一个病毒的二进制文件格式转变成一张图，论文有很详细的说明，下面我把代码处理逻辑具体说下：

对于逆向工作人员来说，将病毒拖进ida或者各种十六进制查看器是兵家常事。以一个真实的病毒举例：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230605225844-7791f872-03b1-1.png)

对于第一个字节来说，M 不是它唯一能表示的东西，事实上，一个灰度图的像素点也是呈 0-255 分布的，所以我们完全可以把 M 也就是 0x4D，也就是 77，当成一个像素点的灰度。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230605225914-89417b6a-03b1-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230605225921-8dbf360a-03b1-1.png)

那为什么提取的特征是有效的呢？能够工作的原因就是病毒家族之间有着十分相似的布局和纹理。这就和CNN网络特点不谋而合了，所以能够直接借鉴过来。

## 图像预处理

这个数据集文件格式很常规：

```
malware-classification/
├── sampleSubmission.csv
├── trainLabels.csv
├── test/
│   ├── aa.asm
│   ├── aa.bytes
│   └── ...
├── train/
│   ├── bb.asm
│   ├── bb.bytes
│   └── ...
└── dataSample/
    ├── a.asm
    ├── a.bytes
    ├── b.asm
    └── b.bytes
```

dataSample 一个实例文件夹、而 test 是测试数据集，sampleSubmission 是提交格式的说明，因为是个比赛的数据集。我们搭建需要用到就是两个：trainLabels.csv 和 train 文件夹，如名字所说：trainLabels.csv 放的是 train 文件夹下训练数据的标签，可以当成使用文件名索引出 class，如图：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230605230019-b06d79fa-03b1-1.png)

而对于asm文件来说我们这次是用不到的，它是通过ida得出来的，是ida反编译出来的结果：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230605230026-b472ae1c-03b1-1.png)

好的，下面看下主角文件格式：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230605230034-b8dc7c9e-03b1-1.png)

我们其实要做的核心步骤就是把一个文件如a.bytes，转成a.png（文件名前缀一定不能变，因为要靠文件名去csv中当索引找对应的类别）

文件统一从0x401000开始，且长度不定有几百k的也有几m的，但处理不难，就是用空格把文件所有字符分割开，然后append到一个一维数组中。如何将一维数组升到二维，论文提到了一种宽度的设计：小于10kb的宽设成32，10kb到30kb之间的宽度设为64，中间还有一段区间（详细见代码），最后是大于1000kb的话设置为1024。使用这种方式来将数据进行升维，代码如下：

```
import os

# 定义一个函数，将 bytes 文件转换成图片
def bytes_to_image(file_path, output_folder):
    # 读取文件内容
    with open(file_path, 'r') as f:
        content = f.read()

    # 将文件内容转换成像素点的亮度
    pixels = []
    for line in content.split('\n'):
        for byte in line.split()[1:]:
            if byte=='??':continue
            pixels.append(int(byte, 16))

    # 计算图片高度
    print(len(pixels)//1024)
    width = next(w for s, w in widths if len(pixels) < s)
    height = len(pixels) // width
    if len(pixels) % width != 0:
        height += 1

    # 创建图片
    from PIL import Image
    img = Image.new('L', (width, height), 0)
    img.putdata(pixels)

    # 保存图片
    file_name = os.path.splitext(os.path.basename(file_path))[0] + '.png'
    output_path = os.path.join(output_folder, file_name)
    img.save(output_path)

# 定义一个列表，用于存储不同文件大小对应的图片宽度
widths = [(10 * 1024, 32), (30 * 1024, 64), (60 * 1024, 128),(100 * 1024, 256),(200 * 1024, 384),(500 * 1024, 512),(1000 * 1024, 768),(float('inf'), 1024)]

# 遍历文件夹，将所有 .bytes 文件转换成图片
input_folder = 'train'
output_folder = 'rtrainpng'
for file_name in os.listdir(input_folder):
    if file_name.endswith('.bytes'):
        file_path = os.path.join(input_folder, file_name)

        # 读取文件内容，计算像素点数量
        with open(file_path, 'r') as f:
            content = f.read()
        pixels_count = sum(1 for line in content.split('\n') if line.startswith('004010'))

        # 将文件转换成图片
        bytes_to_image(file_path, output_folder)
```

跑代码，坐等结果：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230605230129-d9d4f82c-03b1-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230605230135-dda039a8-03b1-1.png)

这是一小部分中的一小部分，最后所有图片跑出来6个多 g ，图片处理完毕，最费时间233（鬼见条）

![](https://xzfile.aliyuncs.com/media/upload/picture/20230605231618-ebb39e8e-03b3-1.png)

## VGG神经网络搭建

这是安全社区，不是人工智能社区，233，搭建过程见代码。就是个 CNN 神经网络的搭建，代码如下

```
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import models, transforms
from PIL import Image
import os
import pandas as pd

import os
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

import os
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

class MyDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None, train=True, test_ratio=0.2):
        self.df = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform
        self.train = train
        self.test_ratio = test_ratio

        # 获取文件夹中的文件名
        self.filenames = os.listdir(self.root_dir)
        self.filenames = [f for f in self.filenames if f.endswith('.png')]

        # 将数据集分成训练集和测试集
        if self.train:
            self.df = self.df[self.df['Id'].isin([f[:-4] for f in self.filenames])]
            self.df = self.df.sample(frac=1).reset_index(drop=True)
            self.test_size = int(len(self.df) * self.test_ratio)
            self.train_df = self.df.iloc[self.test_size:]
            # self.test_df = self.df.iloc[:self.test_size]
        else:
            self.df = self.df[self.df['Id'].isin([f[:-4] for f in self.filenames])]
            self.df = self.df.sample(frac=1).reset_index(drop=True)
            self.test_size = int(len(self.df) * self.test_ratio)
            # self.train_df = self.df.iloc[self.test_size:]
            self.train_df = self.df.iloc[:self.test_size]

            # self.train_df = self.df[self.df['Id'].isin([f[:-4] for f in self.filenames])]

    def __len__(self):
        return len(self.train_df)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        # 读取图片和标签
        img_name = self.train_df.iloc[idx, 0] + '.png'
        img_path = os.path.join(self.root_dir, img_name)
        image = Image.open(img_path)
        label = self.train_df.iloc[idx, 1]

        # 数据增强
        if self.transform:
            image = self.transform(image)

        return image, label

# 定义数据增强
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5),
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 创建训练集和测试集
train_dataset = MyDataset('trainLabels.csv', 'rtrainpng', transform=transform, train=True)
test_dataset = MyDataset('trainLabels.csv', 'rtrainpng', transform=transform, train=False)

# 创建数据加载器
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# 定义 VGG16 模型
class VGG16(nn.Module):
    def __init__(self, num_classes=9):
        super(VGG16, self).__init__()
        self.features = models.vgg16(pretrained=True).features
        self.avgpool = nn.AdaptiveAvgPool2d((7, 7))
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(i...