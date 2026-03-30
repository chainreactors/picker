---
title: 【AI安全】零训练成本到模型后门植入
url: https://mp.weixin.qq.com/s/nsBN0fbeSQ8CXVxMkDah1w
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:39:14.681294
---

# 【AI安全】零训练成本到模型后门植入

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1uGoyC3Wx0icZEwlT4oAJN7d9LvRSKTIAaxsrLLickDKicLkgHlNNouFhumpwqGwRJvBHrqMTC47OONTHEpUo31JvBuW53OicbsWqo/0?wx_fmt=jpeg)

# 【AI安全】零训练成本到模型后门植入

原创

十月的进阶之路
十月的进阶之路

十月的进阶之路

![]()

在小说阅读器中沉浸阅读

> 供应链攻击的隐蔽新玩法，全程无需数据集、无需重新训练

## 0x01 背景

在上一篇《模型后门之木马攻击》中，我们通过给ResNet50外挂神经网络、构造带触发器的数据集完成训练，实现了特定触发模式的后门攻击。但这套方案流程繁琐，既要定制化制作训练数据，还要让模型重新学习触发器的映射规律，如同老太太的裹脚布又臭又长。这一次我们玩个更有趣的：如果能拿到目标模型的权重文件，我们能不能直接修改权重数值，完成一次精准的供应链攻击？当然是可以的，而且全程**零训练、零数据集依赖**，只需要修改几个字节，就能操控模型的预测结果。

## 0x02 PyTorch权重文件结构

我们还是沿用之前用于CIFAR-10数据集分类的best\_model\_bak.pth权重文件，先大概了解它的内部结构，以便于精准修改。当然神经网络逆向工程也是个前沿的领域，如果您有兴趣的话我也乐于分享。

### 2.1 权重文件的本质：ZIP归档包

把权重文件拖入任意二进制编辑器，第一眼就能看到文件开头的504B0304魔数，对应的ASCII字符是PK——这是ZIP归档文件的标准标识。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1s5YxMjGYxfcI7MZyKibeftFEGHBaic0T2iceelcWeqVg0ILiaThERFWSicyknx2FB4kGN73Ztrybnh6CMSTvVThemYdBxaqT9dDQibU/640?wx_fmt=png&from=appmsg)

权重文件结构

这说明，这是**PyTorch 1.6+版本默认的ZIP格式权重文件**，而非旧版的纯pickle单文件。从PyTorch 1.6开始，`torch.save`默认用ZIP格式打包权重，把「模型元数据」和「张量纯数值数据」分离存储，既提升了加载效率，也增强了稳定性。继续往下看，我们能从二进制内容里提取到更多关键信息：

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1vwWZCJvcQFrcBcpnHEWZpByewiaib9YIoLdGlkZdxO13EELibo5A1zzGtd3PgXbWwhCia1icDDmslFgHOZhzibzpiceKaZG5a4W7czaw/640?wx_fmt=png&from=appmsg)

权重文件结构

从层名的命名规律（`conv1→bn1→layer1/layer2/layer3/layer4残差块），可以大概率确定这是一个ResNet`系列的CNN卷积神经网络（大概率是ResNet18/34/50等经典分类网络），并且包含完整的BatchNorm层running统计量，是训练完成的可直接推理的权重。同时能看到.cuda:0标识，说明这个模型是在CUDA GPU上完成训练并保存的。

### 2.2 解压后：权重文件的完整目录结构

既然本质是ZIP包，我们直接解压，就能看到它的完整内部结构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1sPaSKNBeKlBm6X1ZWlUZj3GzSicEibegPcage8UI2BHxWlBZzsbqUKvzugPCUCcDyMzdu7cqcMwMZdCRZJPQ0HrCjqfQOFTEQKU/640?wx_fmt=png&from=appmsg)

权重文件结构

下面我们逐个拆解每个文件/文件夹的核心作用，搞懂PyTorch加载权重的完整流程：

| 文件/文件夹 | 核心作用 |
| --- | --- |
| `version` | 序列化协议版本标识，PyTorch加载时会先校验版本兼容性，避免格式不匹配导致加载失败 |
| `byteorder` | 字节序标识，记录张量二进制数据的存储顺序（x86/ARM架构和NVIDIA GPU默认都是小端序`little`），PyTorch需要靠它正确解析二进制数值 |
| `.data/serialization_id` | 全局唯一序列化ID，`torch.save`执行时随机生成，用于校验元数据和张量数据的一致性，避免跨文件引用错乱 |
| `data.pkl` | 权重的「核心蓝图+索引目录」，Python Pickle序列化格式，存储了完整的模型层名、张量形状、数据类型，以及每个张量对应`data/`目录下的文件索引，是把二进制数据还原成可用张量的关键 |
| `data/` | 权重的「纯数值仓库」，里面的每个数字命名文件，都对应一个张量的原始二进制数据，没有任何元数据，单独打开是无意义的乱码 |

各文件的具体结构如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1ul89S97J1jup94ibbicwicKCKg1CD0jib0ZSbTvSfHvXx3jzz6qNp8jGzFPwkctY8L8oETdQxuNlkGKDib7VcUdwkYStMriaM58NZ9A/640?wx_fmt=jpeg&from=appmsg)

serialization\_id文件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1uBALRT7RvpngVwotjghtzfeqpxwAlZibqzLibkfwBHpwDtyWyojMlpd39rtbGf2ocE5VIMMINF6xsWRcAH0ISM8B2WxXRSOk1qo/640?wx_fmt=jpeg&from=appmsg)

data.pkl文件

![](https://mmbiz.qpic.cn/mmbiz_jpg/ocg1gpicEs1u6QIPibqtmnToCFKARibNDYArCQMEicNR9rSQYmickL7GlgvtnbA0F4hvmU4NfKvUhGf9B6jExCOMMOmgibhtwicXdqyVrzEia6yMNKY/640?wx_fmt=jpeg&from=appmsg)

data目录文件

当你调用`torch.load("best_model")`时，PyTorch内部会按以下步骤完整重建模型权重：

1. 读取`version`和`byteorder`，确认格式兼容性和数据解析规则；
2. 反序列化`data.pkl`，解析出所有层名、张量元数据，以及对应`data/`目录的文件索引；
3. 根据索引，逐个读取`data/`目录下的二进制文件；
4. 结合张量形状、数据类型、字节序，把二进制数据还原成PyTorch张量；
5. 把层名和张量组装成`collections.OrderedDict`格式的`state_dict`，完成权重加载。

## 0x03 为什么改权重能操控模型预测？

我们的目标是让模型在CIFAR-10数据集上，更倾向于把图片判别为「狗」，先明确两个关键前提：

### 3.1 CIFAR-10的类别索引对应

CIFAR-10数据集是10分类任务，采用0-based索引，类别顺序固定如下：

| 索引 | 0 | 1 | 2 | 3 | 4 | **5** | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 类别 | 飞机 | 汽车 | 鸟 | 猫 | 鹿 | **狗** | 青蛙 | 马 | 船 | 卡车 |

我们要操控的「狗」，对应索引`5`，也就是1-based计数的第6个数值。

### 3.2 为什么修改全连接层bias就能直接提升概率？

模型最后一层全连接层的输出公式为：

最终的类别概率，由`softmax(logits)`归一化计算得出。

* 全连接层的`bias_i`，是对应类别`i`的固定偏置项，直接决定了该类别logit的基础值；
* 我们手动增大`bias_5`，就相当于给「狗」这个类别加了一个固定的“加分项”，logit值变大后，经过softmax归一化，该类别的输出概率会显著提升；
* 哪怕图片本身和狗无关，模型在难以判别时，也会有更高概率把它判定为狗，实现我们想要的后门效果。

回到我们的权重文件，`data/`目录下有一个40字节的文件，对应全连接层的bias：PyTorch默认用`float32`单精度浮点数存储权重，每个数值占4字节，40字节刚好对应10个数值，完美匹配CIFAR-10的10个分类。

## 0x04 手动修改权重实现后门

### 4.1 手动修改的关键注意事项

1. **数值格式**：必须使用**IEEE 754标准的float32单精度浮点数**，不能直接写入十进制数；
2. **字节序**：必须遵循小端序规则，数值的十六进制需要倒序存储；
3. **文件大小**：修改时只能覆盖字节，不能插入/删除字节，否则会导致文件大小变化，元数据匹配失败，权重无法加载；
4. **打包规则**：重新打包ZIP时，必须使用「存储（无压缩）」模式，且目录结构必须符合PyTorch的要求，否则会加载报错。

### 4.2 完整修改步骤

找到目标文件：定位到全连接层bias对应的`data/`目录下的二进制文件，我们要修改索引5（第6个）的数值，对应文件内偏移`0x14 ~ 0x17`的4个字节。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ocg1gpicEs1uojVqAbvZS3tUatXg1jkdzxjdJMkrWqIOG6sBwXRHDdZnFPmswb4licDkrse8eHW0HHo3GHjfl1O9NOWfoJON7NmR2M4FrVznE/640?wx_fmt=jpeg&from=appmsg)

权重文件修改

**数值转换**：通过IEEE 754浮点数转换工具，把你想要的目标数值，转换为float32格式的十六进制，再按小端序反转。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1vvX44MEZArqghQIuldcQGhaDbAB5BrmnNUGgriaUvibMmbXEWyndXbkofhvYib2k7kATCyC0MJfcicOqwbQBPTyEkicPxeIAGwc4Ss/640?wx_fmt=jpeg&from=appmsg)

查看原始权重的十进制数值大小

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1vZtff9F5XIPSOpdg85q84g6XPr6mzhhnsbyFNCDFic3p0lgtR7hk7byR3DuQbwzYib6uVX1dMEamIkPEfkYB0feRkjJFWTmwd6Q/640?wx_fmt=jpeg&from=appmsg)

选择合适的替换值

写入修改：用十六进制编辑器（如HxD）打开目标文件，覆盖对应偏移的4个字节，保存文件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ocg1gpicEs1tUXpzpajFdbes1ib3Ex3FadMYZK2Y11oIJBmOJ4o8z7zvc2BOnL5kOYlmmnxoCotkKkQWWLRYsUOg3qbTXiaic6PqaWrib5vqs1as/640?wx_fmt=jpeg&from=appmsg)

手动修改数值转换

重新打包：按PyTorch要求的格式，用「存储模式」重新打包为ZIP文件，修改后缀为`.pth`。**如果您打包遇到任何问题，请评论区留言，我将乐于与您探讨。**

### 4.3 效果验证

我们用修改后的权重替换原模型，在CIFAR-10测试集上进行预测，效果如下：

* 原始权重：模型按正常训练的逻辑分类，误判为狗的样本极少

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vdZTJp8R6uxTUR8NibC9azwPibWdxNY6mXdlh63iazBPtTKiaFTFssxiaCP2nfvCbW0yA8zKdmiaCxhIE3vabicxEfGHibibibokhWWbMcs/640?wx_fmt=png&from=appmsg)

  原始权重预测

* 修改后权重：模型判别为狗的样本数量显著增加，我们成功通过修改权重，操控了模型的预测结果

  ![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1tFkfu7WKQYAcK6icBAOmd2I3FLX1ef5ByLwBzap9iaPbU7NDRPPQksmM8n3BL3iakeKAGXV551B4DZLwpcYLdmPHiarQ8UMxjKmicI/640?wx_fmt=png&from=appmsg)

  手动修改权重后的预测

## 0x05 批量测试：不同增量的攻击效果

手动修改二进制流程繁琐、极易踩坑，我们可以直接用Python脚本完成bias的修改，安全又高效。我们测试了不同增量对模型预测的影响：

* 增量`0.1`：对模型影响极小，分类结果几乎无变化

  ![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1siaXymfNicpKtSpCnr3gzic2zoISG7ODqBiauQgeRWS74gudLoGp9Bf8RWyN0HeMpYT6QBvkZqlGhibTC0saneKaIlRBUjJsGQcCUM/640?wx_fmt=png&from=appmsg)

  增量：0.1

* 增量`1`：模型开始出现明显的偏向，误判为狗的样本增多

  ![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1tuu3IDhATfmFSVyVrrpEQyycC2uiaw3Twe0icEvu2vjEgAUNmbVy0B5VzbonnHXBqSIYQCvFVVWPUzg3Wnb470kmBxJfqzNiafpo/640?wx_fmt=png&from=appmsg)

  增量：1

* 增量`2`：模型的偏向性继续增强

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1u0eA0XFCvoZ0TGq91yZwpxVKBvEaia1bJt149C0fwzkz29joB4dR26G8EHfxaR9icny8CyQfgd3XGU5TxatLsOSOe89JgRrxzicY/640?wx_fmt=png&from=appmsg)

  增量：2

您可以根据自己的需求调整增量大小，实现不同强度的后门效果。

## 0x06 代码地址

完整的自动化修改脚本、测试代码已上传至`github`，可自行下载体验。

```
https://github.com/wml1001/model-backdoor
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

十月的进阶之路

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过