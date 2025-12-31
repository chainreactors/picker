---
title: 第三届“天网杯” AI赛道 writeup合集
url: https://forum.butian.net/share/4690
source: 奇安信攻防社区
date: 2025-12-30
fetch_date: 2025-12-31T03:23:46.817403
---

# 第三届“天网杯” AI赛道 writeup合集

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 第三届“天网杯” AI赛道 writeup合集

* [CTF](https://forum.butian.net/topic/52)

DamnEnv
=======
题目设计
----
25年年初huggingface爆发了一波模型投毒的浪潮，主要针对的是pytorch的供应链pickle和keras的供应链h5。
本题对于后者进行模拟，根据供题要求难度，选择了无隐写的lambda层进行投毒。
writeup
-------
1. 通过查看keras版本，调整对应的tensorflow版本
![image-20250325200326852.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-ea35e36b8a28c21305952df137057c1b7f1cfce4.png)
最终配置环境为tensorflow==2.15.0，keras==2.15.0，python==3.9.12
2. 加载模型，发现被注入了恶意脚本
![image-20250325200205163.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-31a12436a8598324c8b47ceba36e363fa2f96f63.png)
3. 查看模型数据和摘要
```py
print("模型摘要:")
model.summary()
for i, layer in enumerate(model.layers):
print(f"第 {i} 层: {layer.name}, 类型: {type(layer).\_\_name\_\_}")
```
```bash
模型摘要:
Model: "model"
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Layer (type) Output Shape Param # Connected to
==================================================================================================
input\_1 (InputLayer) [(None, 224, 224, 3)] 0 []
conv1\_pad (ZeroPadding2D) (None, 230, 230, 3) 0 ['input\_1[0][0]']
conv1\_conv (Conv2D) (None, 112, 112, 64) 9472 ['conv1\_pad[0][0]']
conv1\_bn (BatchNormalizati (None, 112, 112, 64) 256 ['conv1\_conv[0][0]']
on)
conv1\_relu (Activation) (None, 112, 112, 64) 0 ['conv1\_bn[0][0]']
pool1\_pad (ZeroPadding2D) (None, 114, 114, 64) 0 ['conv1\_relu[0][0]']
pool1\_pool (MaxPooling2D) (None, 56, 56, 64) 0 ['pool1\_pad[0][0]']
conv2\_block1\_1\_conv (Conv2 (None, 56, 56, 64) 4160 ['pool1\_pool[0][0]']
D)
conv2\_block1\_1\_bn (BatchNo (None, 56, 56, 64) 256 ['conv2\_block1\_1\_conv[0][0]']
rmalization)
conv2\_block1\_1\_relu (Activ (None, 56, 56, 64) 0 ['conv2\_block1\_1\_bn[0][0]']
ation)
conv2\_block1\_2\_conv (Conv2 (None, 56, 56, 64) 36928 ['conv2\_block1\_1\_relu[0][0]']
D)
conv2\_block1\_2\_bn (BatchNo (None, 56, 56, 64) 256 ['conv2\_block1\_2\_conv[0][0]']
rmalization)
conv2\_block1\_2\_relu (Activ (None, 56, 56, 64) 0 ['conv2\_block1\_2\_bn[0][0]']
ation)
conv2\_block1\_0\_conv (Conv2 (None, 56, 56, 256) 16640 ['pool1\_pool[0][0]']
D)
conv2\_block1\_3\_conv (Conv2 (None, 56, 56, 256) 16640 ['conv2\_block1\_2\_relu[0][0]']
D)
conv2\_block1\_0\_bn (BatchNo (None, 56, 56, 256) 1024 ['conv2\_block1\_0\_conv[0][0]']
rmalization)
conv2\_block1\_3\_bn (BatchNo (None, 56, 56, 256) 1024 ['conv2\_block1\_3\_conv[0][0]']
rmalization)
conv2\_block1\_add (Add) (None, 56, 56, 256) 0 ['conv2\_block1\_0\_bn[0][0]',
'conv2\_block1\_3\_bn[0][0]']
conv2\_block1\_out (Activati (None, 56, 56, 256) 0 ['conv2\_block1\_add[0][0]']
on)
conv2\_block2\_1\_conv (Conv2 (None, 56, 56, 64) 16448 ['conv2\_block1\_out[0][0]']
D)
conv2\_block2\_1\_bn (BatchNo (None, 56, 56, 64) 256 ['conv2\_block2\_1\_conv[0][0]']
rmalization)
conv2\_block2\_1\_relu (Activ (None, 56, 56, 64) 0 ['conv2\_block2\_1\_bn[0][0]']
ation)
conv2\_block2\_2\_conv (Conv2 (None, 56, 56, 64) 36928 ['conv2\_block2\_1\_relu[0][0]']
D)
conv2\_block2\_2\_bn (BatchNo (None, 56, 56, 64) 256 ['conv2\_block2\_2\_conv[0][0]']
rmalization)
conv2\_block2\_2\_relu (Activ (None, 56, 56, 64) 0 ['conv2\_block2\_2\_bn[0][0]']
ation)
conv2\_block2\_3\_conv (Conv2 (None, 56, 56, 256) 16640 ['conv2\_block2\_2\_relu[0][0]']
D)
conv2\_block2\_3\_bn (BatchNo (None, 56, 56, 256) 1024 ['conv2\_block2\_3\_conv[0][0]']
rmalization)
conv2\_block2\_add (Add) (None, 56, 56, 256) 0 ['conv2\_block1\_out[0][0]',
'conv2\_block2\_3\_bn[0][0]']
conv2\_block2\_out (Activati (None, 56, 56, 256) 0 ['conv2\_block2\_add[0][0]']
on)
conv2\_block3\_1\_conv (Conv2 (None, 56, 56, 64) 16448 ['conv2\_block2\_out[0][0]']
D)
conv2\_block3\_1\_bn (BatchNo (None, 56, 56, 64) 256 ['conv2\_block3\_1\_conv[0][0]']
rmalization)
conv2\_block3\_1\_relu (Activ (None, 56, 56, 64) 0 ['conv2\_block3\_1\_bn[0][0]']
ation)
conv2\_block3\_2\_conv (Conv2 (None, 56, 56, 64) 36928 ['conv2\_block3\_1\_relu[0][0]']
D)
conv2\_block3\_2\_bn (BatchNo (None, 56, 56, 64) 256 ['conv2\_block3\_2\_conv[0][0]']
rmalization)
conv2\_block3\_2\_relu (Activ (None, 56, 56, 64) 0 ['conv2\_block3\_2\_bn[0][0]']
ation)
conv2\_block3\_3\_conv (Conv2 (None, 56, 56, 256) 16640 ['conv2\_block3\_2\_relu[0][0]']
D)
conv2\_block3\_3\_bn (BatchNo (None, 56, 56, 256) 1024 ['conv2\_block3\_3\_conv[0][0]']
rmalization)
conv2\_block3\_add (Add) (None, 56, 56, 256) 0 ['conv2\_block2\_out[0][0]',
'conv2\_block3\_3\_bn[0][0]']
conv2\_block3\_out (Activati (None, 56, 56, 256) 0 ['conv2\_block3\_add[0][0]']
on)
conv3\_block1\_1\_conv (Conv2 (None, 28, 28, 128) 32896 ['conv2\_block3\_out[0][0]']
D)
conv3\_block1\_1\_bn (BatchNo (None, 28, 28, 128) 512 ['conv3\_block1\_1\_conv[0][0]']
rmalization)
conv3\_block1\_1\_relu (Activ (None, 28, 28, 128) 0 ['conv3\_block1\_1\_bn[0][0]']
ation)
conv3\_block1\_2\_conv (Conv2 (None, 28, 28, 128) 147584 ['conv3\_block1\_1\_relu[0][0]']
D)
conv3\_block1\_2\_bn (BatchNo (None, 28, 28, 128) 512 ['conv3\_block1\_2\_conv[0][0]']
rmalization)
conv3\_block1\_2\_relu (Activ (None, 28, 28, 128) 0 ['conv3\_block1\_2\_bn[0][0]']
ation)
conv3\_block1\_0\_conv (Conv2 (None, 28, 28, 512) 131584 ['conv2\_block3\_out[0][0]']
D)
conv3\_block1\_3\_conv (Conv2 (None, 28, 28, 512) 66048 ['conv3\_block1\_2\_relu[0][0]']
D)
conv3\_block1\_0\_bn (BatchNo (None, 28, 28, 512) 2048 ['conv3\_block1\_0\_conv[0][0]']
rmalization)
conv3\_block1\_3\_bn (BatchNo (None, 28, 28, 512) 2048 ['conv3\_block1\_3\_conv[0][0]']
rmalization)
conv3\_block1\_add (Add) (None, 28, 28, 512) 0 ['conv3\_block1\_0\_bn[0][0]',
'conv3\_block1\_3\_bn[0][0]']
conv3\_block1\_out (Activati (None, 28, 28, 512) 0 ['conv3\_block1\_add[0][0]']
on)
conv3\_block2\_1\_conv (Conv2 (None, 28, 28, 128) 65664 ['conv3\_block1\_out[0][0]']
D)
conv3\_block2\_1\_bn (BatchNo (None, 28, 28, 128) 512 ['conv3\_block2\_1\_conv[0][0]']
rmalization)
conv3\_block2\_1\_relu (Activ (None, 28, 28, 128) 0 ['conv3\_block2\_1\_bn[0][0]']
ation)
conv3\_block2\_2\_conv (Conv2 (None, 28, 28, 128) 147584 ['conv3\_block2\_1\_relu[0][0]']
D)
conv3\_block2\_2\_bn (BatchNo (None, 28, 28, 128) 512 ['conv3\_block2\_2\_conv[0][0]']
rmalization)
conv3\_block2\_2\_relu (Activ (None, 28, 28, 128) 0 ['conv3\_block2\_2\_bn[0][0]']
ation)
conv3\_block2\_3\_conv (Conv2 (None, 28, 28, 512) 66048 ['conv3\_block2\_2\_relu[0][0]']
D)
conv3\_block2\_3\_bn (BatchNo (None, 28, 28, 512) 2048 ['conv3\_block2\_3\_conv[0][0]']
rmalization)
conv3\_block2\_add (Add) (None, 28, 28, 512) 0 ['conv3\_block1\_out[0][0]',
'conv3\_block2\_3\_bn[0][0]']
conv3\_block2\_out (Activati (None, 28, 28, 512) 0 ['conv3\_block2\_add[0][0]']
on)
conv3\_block3\_1\_conv (Conv2 (None, 28, 28, 128) 65664 ['conv3\_block2\_out[0][0]']
D)
conv3\_block3\_1\_bn (BatchNo (None, 28, 28, 128) 512 ['conv3\_block3\_1\_conv[0][0]']
rmalization)
conv3\_block3\_1\_relu (Activ (None, 28, 28, 128) 0 ['conv3\_block3\_1\_bn[0][0]']
ation)
conv3\_block3\_2\_conv (Conv2 (None, 28, 28, 128) 147584 ['conv3\_block3\_1\_relu[0][0]']
D)
conv3\_block3\_2\_bn (BatchNo (None, 28, 28, 128) 512 ['conv3\_block3\_2\_conv[0][0]']
rmalization)
conv3\_block3\_2\_relu (Activ (None, 28, 28, 128) 0 ['conv3\_block3\_2\_bn[0][0]']
ation)
conv3\_block3\_3\_conv (Conv2 (None, 28, 28, 512) 66048 ['conv3\_block3\_2\_relu[0][0]']
D)
conv3\_block3\_3\_bn (...