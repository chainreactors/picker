---
title: 让那个最没用的NPU也忙起来：通过openvino跑大模型
url: https://mp.weixin.qq.com/s/WabZauNTZRA_Iz78v6SVUQ
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:07.114066
---

# 让那个最没用的NPU也忙起来：通过openvino跑大模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RJrNBTwulvfsibiaBySHjbO4I0MovBnt4IGpuGL32yNqL2b56ia0oxCsIY2kNm7v5icBLdEKA5yXe1KzmxmnoCbJgvTuHgodWYA4tncLY4q4Kcs/0?wx_fmt=jpeg)

# 让那个最没用的NPU也忙起来：通过openvino跑大模型

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 让那个最没用的NPU也忙起来：通过openvino跑大模型

## 缘起

看过很多电脑评测视频，都会有一句：这个cpu自带一个没什么用的npu……

就是这个：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvfKl5dwq6jwgiaFxPTX4DkEB3UkJF80eXrPgMiclN5XXTgBOkIhFDrFC7bzJFtb0cVEO1Vz7icn4bxcRcaNXIYsCWm1WakmksovyY/640?wx_fmt=png&from=appmsg)

我实在不信intel搞了这么多年真的一无是处，于是就想着，能不能通过openvino跑大模型？

## 挑选大模型

npu的算力其实并不大，想试试只能找他自己优化过的：https://huggingface.co/OpenVINO

就这个吧：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvfrfqp1Qvibq9afglJh8icmh6a6iaBuKghCIO6wX2rQNfMbxpKC2Y6JBARqmSdm3HIAVVPN28ALORMMaMBe4KPVX7mARurib3U98q4/640?wx_fmt=png&from=appmsg)

## 安装openvino

```
# 创建一个虚拟环境
conda create -n vino python=3.13

# 激活虚拟环境
conda activate vino

# 安装openvino
pip install --upgrade pip
pip install openvino openvino-genai
```

参考官方文档：openvino 安装

特别注意：只能通过pip安装，不能通过conda，因为conda环境中不包括npu的插件，如官方文档的下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvcVtuyOrXWAibz8cnVrjoMfXvFnUtoia5ZLoZAukeHj7w5h5ic4xYzgbktSAWk3uEJgjw2q1Y4PdlgPP0KkAjIWHStPUO2y521pqc/640?wx_fmt=png&from=appmsg)

## 下载大模型

抱脸下载太慢了，好在在魔搭找到了镜像：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulveL0MkT5g0XugerFyh6AwlefoibLRDNXIULJ2xHhn8YOq4NdI10uVbj9nvMYbV1XT0NuQsMwIPXgtPUYrKkNMGWCugsxBtpd8OA/640?wx_fmt=png&from=appmsg)

不知道二者差异的，推荐刚写的：

[Hugging Face vs ModelScope：两大开源模型平台深度对比与高效下载指南](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651443&idx=1&sn=b20bd5341d5d8a81ab154d8ee1e5f0e6&scene=21#wechat_redirect)

## 小试牛刀

直接用模型介绍页面的代码试试：

```
import openvino_genai

model_path = "D:\\model\\openvino"

device = "NPU"
pipe = openvino_genai.LLMPipeline(model_path, device)
config = openvino_genai.GenerationConfig()
config.max_new_tokens = 25600

history = openvino_genai.ChatHistory()
history.append({"role": "system", "content": "You are a helpful assistant."})

def streamer(subword):
    print(subword, end='', flush=True)
    return False

while True:
    try:
        prompt = input('\nquestion:\n')
    except EOFError:
        break
    history.append({"role": "user", "content": prompt})
    result = pipe.generate(history, config, streamer)
    history.append({"role": "assistant", "content": result.texts[0]})
    print(f"\nanswer:\n{result.texts[0]}")
```

看看效果：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvfTuEw9hpRLAbDflPjwduT20IQCbIIdIUcsFjz9Aj9Q66v1oqaCc5hHctgsWG4e7a7NViadJiauEp5WQH2DibulmVVLw9nZt2tQ1w/640?wx_fmt=png&from=appmsg)

速度还可以，第一个token有点慢，后面速度跟上阅读不难。

## 启动服务，接入Cherry-Studio

直接问ima，他给我推了一个star为0的项目：

https://github.com/prskid1000/intel-npu-llm

不过还是能用的：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvegD7tal254KshPPeDJpXMGQUHQ4fyxeibak7aoQnPurj6lwMfsbPvVuKetfEpUfF6mOEe4Hb3XDlUoUfNAOiayfU5r0VRzmUnF8/640?wx_fmt=png&from=appmsg)

试试效果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvflknLzlKs03UJfDkCiaUEHMSErPTDwEX8pMyLaowxqicvasW2PlnKkIUxxAXhXJVCgVsQRoP2KYmXUhme8yhgPxS8QZwBrfich34/640?wx_fmt=png&from=appmsg)

看看是不是npu在跑：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvceK2f3GHEUU8ydMLSsOia1Ticdicz6UeZPWQTXjssJ1pP20yhBtVICH0hLL22icBWYwF1KS8PUbaRIgAliaLybEKa0FKGTE62Xz89k/640?wx_fmt=png&from=appmsg)

## 小结

NPU的算力还是很低的，但是对比GPU来，他的功耗也是很低的，笔记本上能省很多电，再等等小模型的发展，还是足够用的，至少是给本地龙虾聊聊天足够的。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

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