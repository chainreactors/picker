---
title: DeepSeek本地化部署有风险！快来看看你中招了吗？
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497165&idx=1&sn=2f1f262f9e69206aa6fccf6cd80e3584&chksm=e8a5ffaedfd276b898f3c0cc96edb79b699b254f320aa3af684f5c41c82099039993b999525b&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-02-20
fetch_date: 2025-10-06T20:38:40.069861
---

# DeepSeek本地化部署有风险！快来看看你中招了吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4mAAwpya3hhejrd56sYbpcTs1jwK3bQu2kxxOCcblaoeDT0aknZsiacNpgo4hjyC3uEhLT4X571oQ/0?wx_fmt=jpeg)

# DeepSeek本地化部署有风险！快来看看你中招了吗？

迪哥讲事

以下文章来源于腾讯安全应急响应中心
，作者腾讯朱雀实验室

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7CTo6zpdyFSNyOal2JdEBLQtttLRAuLRUcW46Q0XM1Iw/0)

**腾讯安全应急响应中心**
.

腾讯安全应急响应中心（TSRC）官方微信

![](https://mmbiz.qpic.cn/mmbiz_gif/JMH1pEQ7qP4jpMV2Vj3wZOo7FMicC1lHPloKMIicIBoEEhk8YKd1p5Tvdyh9neQBuZRG9M9LBF4iceRNaxKfJw5CA/640?wx_fmt=gif)

2025年伊始，AI领域迎来一个重要变革 - DeepSeek R1开源发布，凭借着低成本、性能出众的优势，这个模型在短短几周内就获得空前关注。由于官网服务经常繁忙，大家开始选择使用Ollama+OpenWebUI、LM Studio等工具进行本地快速部署，从而将AI能力引入企业内网和个人PC环境。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JMmQSvzh5UZgZjiaBBDA1WojzAf9qpjBgFrCYKPWPlBQQRfr4qS4ygabg/640?wx_fmt=png&from=appmsg)

近期腾讯朱雀实验室发现：这些广受欢迎的AI工具中普遍存在安全漏洞。如果使用不当，攻击者可能窃取用户数据、滥用算力资源，甚至控制用户设备。

文本将介绍这些流行AI工具的安全问题，以及如何使用开源的AI-Infra-Guard一键检测与收敛相关风险。

**一、Ollama**

Ollama是一个开源应用程序，允许用户在Windows、Linux和macOS设备上本地部署和操作大型语言模型（LLM），受 Docker 的启发，Ollama 简化了打包和部署 AI 模型的过程， 现在已成为最流行的的个人电脑跑大模型的方案，目前网络上大部分本地部署DeepSeek R1的文章也是推荐的此工具。

Ollama默认启动时会开放11434端口，在此端口上公开使用restful api执行核心功能，例如下载模型，上传模型，模型对话等等。默认情况下ollama只会在本地开放端口，但是在Ollama的docker中，默认会以root权限启动，并且开放到公网上。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JMJIuxIrhxCSOST0LcGzfjMnKScu2PEv1uJtkw6gmlGgsM3zDiajzasIA/640?wx_fmt=png&from=appmsg)

ollama对这些接口普遍没有鉴权，导致攻击者扫描到这些ollama的开放服务后可以进行一系列攻击手段。

### 1）模型删除

例如，通过接口删除模型。

### 2）模型窃取

通过接口查看ollama模型。

ollama支持自定义镜像源，自建一个镜像服务器，再通过接口就能轻松窃取私有模型文件。

### 3）算力窃取

通过接口查看ollama模型。之后便能用请求对话，窃取了目标机器的算力。

### 4）模型投毒

可以通过接口查看正在运行的模型，接着可以用下载有毒的模型，通过删除正常模型，在通过接口迁移有毒模型到正常模型路径，通过有毒模型污染使用者的对话。

### 5）远程命令执行漏洞 CVE-2024-37032

ollama在去年6月爆发过严重的远程命令执行漏洞【CVE-2024-37032】是Ollama开源框架中一个严重的路径遍历漏洞，允许远程代码执行（RCE），CVSSv3评分为9.1。该漏洞影响Ollama 0.1.34之前的版本，通过自建镜像伪造manifest文件，实现任意文件读写和远程代码执行。

###

* ### 缓解方案

升级到最新版ollama，但是ollama官方目前无任何鉴权方案，运行ollama serve时确认环境变量OLLAMA\_HOST为本地地址，避免公网运行。建议本地运行ollama再使用反向代理工具（如Nginx）为服务端增加访问保护

据统计,目前公网上仍有约4万个未设防的Ollama服务,请检查您的部署是否安全。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JMDic1I6QGiccTZnrAs2Lz4ATwjMibHxmq4nZMEJFnchTblnF6uskx5vajQ/640?wx_fmt=png&from=appmsg)

**二、OpenWebUI**

openwebui是现在最流行的大模型对话webui，包含大模型聊天，上传图片，RAG等多种功能且方便与ollama集成。也是现在deepseek本地化部署常见的搭配。openwebui在历史上也出现了不少漏洞，这里挑选几个典型。

### 【CVE-2024-6707】一个文件黑掉你的AI

用户通过Open WebUI的HTTP界面点击消息输入框左侧的加号（+）上传文件时，文件会被存储到静态上传目录。上传文件名可伪造，未进行校验，允许攻击者通过构造包含路径遍历字符（如../../）的文件名，将文件上传至任意目录。

攻击者可通过上传恶意模型（如包含Python序列化对象的文件），反序列化后执行任意代码，或通过上传authorized\_keys实现远程命令执行。

流程图如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JMNOH40W0LUj0vXWmjQftKPwVfSfBD0zDeNlCB74ibrFFxrkCgicbLQ8ibw/640?wx_fmt=jpeg&from=appmsg)

* ### 缓解方案

升级到最新版，避免开启用户系统。

**三、ComfyUI‍**

ComfyUI是现在最流行的diffusion模型应用，因其丰富的插件生态和高度定制化节点闻名，常用于文生图、文生视频等领域。

ComfyUI和Ollama一样，开发者最初可能只想在本地使用，没有任何鉴权方式，但是也有大量开放到公网的ComfyUI应用。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JMqtLTdvGXZwU2Lq9lgGYQ6r8qPV2QDjP7Q4L3lV2NdaBjPxNib5mpBrw/640?wx_fmt=png&from=appmsg)

ComfyUI因为插件生态闻名，但是插件的作者一般为个人开发者，对安全性没有太多关注，腾讯朱雀实验室在去年就发现多个ComfyUI及其插件漏洞。

**朱雀实验室历史发现漏洞：**

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JMicDYQ2nnibHvUdtsE74LKNDa4bNicvVQ0GtpVmnzzBVYOx2QDhVUb8J7Q/640?wx_fmt=png&from=appmsg)

以上大部分漏洞影响ComfyUI全系列核心代码(包含目前最新版本)，部分流行插件，影响包括远程命令执行、任意文件读取/写入，数据窃取等。

* ### 缓解方案

由于漏洞修复缓慢，ComfyUI最新版本目前仍然存在漏洞，不建议将其暴露公网使用。

**四、AI-Infra-Guard: AI风险一键检测与防范**

在过去一年中，朱雀蓝军围绕混元大模型安全开展了深入研究和实践，逐步落地了一套大模型软件供应链安全解决方案。该项目拥有轻量、快速、无害发现AI安全威胁的能力， 利用大模型进行漏洞采集，已经帮助收敛了多处“开源软件供应链漏洞导致混元数据泄露”的风险盲点，验证了利用大模型赋能安全的应用潜力。

一个日常场景：

安全团队："求求你们先把ollama的鉴权打开"

算法团队："可是文档没说需要安全配置啊..."

运维团队："这框架我都没听说过，怎么扫描？"

也正是这些痛点，催生了AI-Infra-Guard的诞生。

**AI-Infra-Guard是什么**

AI Infra Guard(AI Infrastructure Guard) 是一个高效、轻量、易用的AI基础设施安全评估工具，专为发现和检测AI系统潜在安全风险而设计。目前已经支持检测30种AI组件、不仅支持常见的AI应用dify、comfyui、openwebui，也支持像ragflow、langchain、llama-factory等开发训练框架的漏洞检测。

1）通过大模型自动积累漏洞规则

为了解决海量AI组件CVE漏洞规则的人工分析成本，我们实现了用大模型自动将历史漏洞收集的方案，传统方式中可能需要人工分析CVE描述 → 写正则匹配规则（耗时3h/漏洞），现在利用混元大模型，自动同步CVE+大模型自动解析 -> 生成漏洞检测逻辑只需要30s。也实现了对AI组件相关漏洞的实时监控：

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JMTXv54evW3d1a6vuicC4IiabXcvJRtZ4maMqF797jIHvy7OLnrTtxzdSA/640?wx_fmt=png&from=appmsg)

2）使用友好

· 零依赖，开箱即用，二进制文件仅8MB

· 内存占用＜50MB，扫完千节点集群不卡顿

· 跨平台兼容，同时支持Windows/MacOS/Linux

**使用**

Al-Infra-Guard 已在GitHub开源，目前已收录30+AI应用指纹，200+安全漏洞数据库，且已包含腾讯朱雀实验室独家发现的英伟达Triton，Pytorch，ComfyUI与Ray等知名AI组件漏洞。

对于个人用户，想检测自己本地AI组件应用，可以执行如下命令一键检测

```
./ai-infra-guard -localscan
```

将对本地开放端口进行检查和识别，给出安全建议。

如上文中使用了包含漏洞的ollama版本，一键检测后提示如下：

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JMpTarZjD6TqexrjnFfPPkddNJA4NvQsm5iajutlmxDMwfkadtzDLaAcA/640?wx_fmt=png&from=appmsg)

‍

如果在检测到AI服务在公网开放，也会提示

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JMbg9ubmBQvyIx9JcEmNcGN5TO7TSgyMZokKH7v0UwxrAyxZo6J2yqIg/640?wx_fmt=png&from=appmsg)

对于开发者/运维，想检测部署AI服务的安全性，执行命令

```
单个目标./ai-infra-guard -target [IP:PORT/域名]
多个目标./ai-infra-guard -target [IP:PORT/域名] -target [IP:PORT/域名]
# 扫描网段寻找AI服务  ./ai-infra-guard -target 192.168.1.0/24
# 从文件读取目标扫描./ai-infra-guard -file target.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5zBOhplgtLPSeLtib6pe2JM4O3FSZLtakrRGEGEsIKEc87Cwria3cIx98CIicnDhnAGBBBYKkfVzulQ/640?wx_fmt=png&from=appmsg)

**获取地址**

开源地址：https://github.com/Tencent/AI-Infra-Guard/

下载地址（根据系统下载自己系统的版本）：https://github.com/Tencent/AI-Infra-Guard/releases

‍

欢迎大家Star、体验并反馈工具的任何问题！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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