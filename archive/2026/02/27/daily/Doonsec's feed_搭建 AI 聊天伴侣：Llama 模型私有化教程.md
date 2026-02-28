---
title: 搭建 AI 聊天伴侣：Llama 模型私有化教程
url: https://mp.weixin.qq.com/s/f2tdQQZOFCG28qvAnY1crg
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:55:55.317953
---

# 搭建 AI 聊天伴侣：Llama 模型私有化教程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lFfjZayicKlH8BX9AJwOEKDvkqx7Or2g7067pW6hHO2uvQla9NQmThfEGIJrwT46wjxVoXCOLkAVP9oOuk9jjEkoLibspACEoMQgLVLFPWjZ8/0?wx_fmt=jpeg)

# 搭建 AI 聊天伴侣：Llama 模型私有化教程

蚁景网安

![]()

在小说阅读器中沉浸阅读

以下文章来源于蚁景网络安全
，作者Jumbo

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7Yk0SeU4ibQcLl1mDLlqhbAOdK1Ik3EO85soOvkh9e8wQ/0)

**蚁景网络安全**
.

致力于为你带来更实用的网络安全技术内容！

## 前言

AI新时代，提高了生产力且能帮助用户快速解答问题，现在用的比较多的是Openai、Claude，为了保证个人隐私数据，所以尝试本地（Mac M3）搭建Llama模型进行沟通。

## Gpt4all

安装比较简单，根据https://github.com/nomic-ai/gpt4all下载客户端软件即可，打开是这样的：

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ibIibCKC4RSKicbPoJG1OTraLI3wkXvyM7C3icPFiaezD9YlreWichz5DicTNA/640?wx_fmt=other&from=appmsg)

然后选择并下载模型文件，这里以Llama为例：

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ibPK1nIXNe6ND5t2DEa2IN34LWHDCvPL7YWtlsuCic9fyJxqwG43l4wYg/640?wx_fmt=other&from=appmsg)

下载模型文件完，选择模型文件则可以进行对话了：

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ib2ZiaVicy8TAKwwNsU1S5eTBMCczqgZ6pQrVY8H0oPmAkg8H1sUvUt3icg/640?wx_fmt=other&from=appmsg)

也可以利用基于 nomic-embed-text嵌入模型，把文档转成向量方便语义检索和匹配。选择文档所在的目录：

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ibP8qzlIZZKEIDbL4WNiazibAXY1OYPhVjdnb0AtmltS583JeiaVBqBDNPg/640?wx_fmt=other&from=appmsg)

然后对话中选择对应的文档即可：

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ibLtbb08WnKVxY5ia3umrrxF292icPPkMFGbArd3kMeYiauic0BbgMhs9o8A/640?wx_fmt=other&from=appmsg)

如果文件太大，需要在设置适当添加token大小，太大也不好，处理会慢且机器会卡死：

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ibyWAPJIZibVwoj3oQNPeIr3tN5HbGz91zPlH6gEHrYdJOHDMIibMMntNg/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ibTuSZzfib9eH2g1rx2zliaaJauiaWlsal5cvoYyjwRkEh3yj2roaXbu8SQ/640?wx_fmt=other&from=appmsg)

gpt4all使用起来还是比较方便的，但是有几个缺点：有些能在huggingface.co搜到的模型在gpt4all上面搜不到、退出应用后聊天记录会消失。

## Ollama

安装也很方便，下载https://ollama.com/download/Ollama-darwin.zip，然后运行如下命令即可启动Llama：

```
ollama run llama3.2
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ibQrUh3vbBL4uD26Gice6LC5ibVrrPZFSfsnNPhquBrNkdm0mY5icfrQlKg/640?wx_fmt=other&from=appmsg)

为了方便图形化使用，可以借助https://github.com/open-webui/open-webui完整图形化的使用，启动也很简单，直接使用官方仓库中的命令即可：

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

然后访问本地的3000端口即可：

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ibqDmXibshlZvVS8rKriaHnyeSlPz9tV9v7LZ5HQovWf09W0X4iaNeuKmmA/640?wx_fmt=other&from=appmsg)

open-webui的原理也比较简单，Ollama启动后会在本地监听11434端口，open-webui也是利用这个端口来和Ollama通信完成的图形化使用。 open-webui还可以多选模型一起回答：

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldwnlhg1MjfbJnNicnaHnK18ibSHWoGDUFMKG6W89ffViajABSLXqqF7Qr5CmGeZVYEurCBz9fb6k87Xw/640?wx_fmt=other&from=appmsg)

整体测试下来，发现Llama3.2对于文档分析差点意思，给他提供一个pdf文档，也看不出个啥来。但是上面的gpt4all，然后通过nomic-embed-text模型嵌入后好点。

## 总结

本文演示了通过不同手段来运行Llama模型，来达到本地使用LLM的目的。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

蚁景网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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