---
title: DeepSeek本地化部署有风险！快来看看你中招了吗?
url: https://www.freebuf.com/sectool/422066.html
source: FreeBuf网络安全行业门户
date: 2025-02-19
fetch_date: 2025-10-06T20:40:03.150539
---

# DeepSeek本地化部署有风险！快来看看你中招了吗?

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

DeepSeek本地化部署有风险！快来看看你中招了吗?

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

DeepSeek本地化部署有风险！快来看看你中招了吗?

2025-02-18 14:16:51

所属地 广东省

2025年伊始，AI领域迎来一个重要变革 - DeepSeek R1开源发布，凭借着低成本、性能出众的优势，这个模型在短短几周内就获得空前关注。由于官网服务经常繁忙，大家开始选择使用Ollama+OpenWebUI、LM Studio等工具进行本地快速部署，从而将AI能力引入企业内网和个人PC环境。![](https://image.3001.net/images/20250218/1739858858_67b423aa6eba03d67e850.png!small)

近期腾讯朱雀实验室发现：这些广受欢迎的AI工具中普遍存在安全漏洞。如果使用不当，攻击者可能窃取用户数据、滥用算力资源，甚至控制用户设备。

文本将介绍这些流行AI工具的安全问题，以及如何使用开源的AI-Infra-Guard一键检测与收敛相关风险。

**一、Ollama**

Ollama是一个开源应用程序，允许用户在Windows、Linux和macOS设备上本地部署和操作大型语言模型（LLM），受 Docker 的启发，Ollama 简化了打包和部署 AI 模型的过程， 现在已成为最流行的的个人电脑跑大模型的方案，目前网络上大部分本地部署DeepSeek R1的文章也是推荐的此工具。

Ollama默认启动时会开放11434端口，在此端口上公开使用restful api执行核心功能，例如下载模型，上传模型，模型对话等等。默认情况下ollama只会在本地开放端口，但是在Ollama的docker中，默认会以root权限启动，并且开放到公网上。![](https://image.3001.net/images/20250218/1739858908_67b423dcbdb2ddef95b6e.png!small)
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

据统计,目前公网上仍有约4万个未设防的Ollama服务,请检查您的部署是否安全。![](https://image.3001.net/images/20250218/1739858962_67b42412244b2cd0a8f8a.png!small)

**二、OpenWebUI**

openwebui是现在最流行的大模型对话webui，包含大模型聊天，上传图片，RAG等多种功能且方便与ollama集成。也是现在deepseek本地化部署常见的搭配。openwebui在历史上也出现了不少漏洞，这里挑选几个典型。

### 【CVE-2024-6707】一个文件黑掉你的AI

用户通过Open WebUI的HTTP界面点击消息输入框左侧的加号（+）上传文件时，文件会被存储到静态上传目录。上传文件名可伪造，未进行校验，允许攻击者通过构造包含路径遍历字符（如../../）的文件名，将文件上传至任意目录。

攻击者可通过上传恶意模型（如包含Python序列化对象的文件），反序列化后执行任意代码，或通过上传authorized\_keys实现远程命令执行。

流程图如下：

![](https://image.3001.net/images/20250218/1739858997_67b424351b5413f25e7e9.png!small)

* ### 缓解方案

升级到最新版，避免开启用户系统。

**三、ComfyUI**

ComfyUI是现在最流行的diffusion模型应用，因其丰富的插件生态和高度定制化节点闻名，常用于文生图、文生视频等领域。ComfyUI和Ollama一样，开发者最初可能只想在本地使用，没有任何鉴权方式，但是也有大量开放到公网的ComfyUI应用。![](https://image.3001.net/images/20250218/1739859056_67b424706c47257b0faec.png!small)
ComfyUI因为插件生态闻名，但是插件的作者一般为个人开发者，对安全性没有太多关注，腾讯朱雀实验室在去年就发现多个ComfyUI及其插件漏洞。
**朱雀实验室历史发现漏洞：**![](https://image.3001.net/images/20250218/1739859096_67b42498b6e0b67d60eef.png!small)

以上大部分漏洞影响ComfyUI全系列核心代码(包含目前最新版本)，部分流行插件，影响包括远程命令执行、任意文件读取/写入，数据窃取等。

* ### 缓解方案

由于漏洞修复缓慢，ComfyUI最新版本目前仍然存在漏洞，不建议将其暴露公网使用。

**四、AI-Infra-Guard: AI风险一键检测与防范**

在过去一年中，朱雀蓝军围绕混元大模型安全开展了深入研究和实践，逐步落地了一套大模型软件供应链安全解决方案。该项目拥有轻量、快速、无害发现AI安全威胁的能力， 利用大模型进行漏洞采集，已经帮助收敛了多处“开源软件供应链漏洞导致混元数据泄露”的风险盲点，验证了利用大模型赋能安全的应用潜力。一个日常场景：安全团队："求求你们先把ollama的鉴权打开"算法团队："可是文档没说需要安全配置啊..."运维团队："这框架我都没听说过，怎么扫描？"也正是这些痛点，催生了AI-Infra-Guard的诞生。

**AI-Infra-Guard是什么**

AI Infra Guard(AI Infrastructure Guard) 是一个高效、轻量、易用的AI基础设施安全评估工具，专为发现和检测AI系统潜在安全风险而设计。目前已经支持检测30种AI组件、不仅支持常见的AI应用dify、comfyui、openwebui，也支持像ragflow、langchain、llama-factory等开发训练框架的漏洞检测。

1）通过大模型自动积累漏洞规则

为了解决海量AI组件CVE漏洞规则的人工分析成本，我们实现了用大模型自动将历史漏洞收集的方案，传统方式中可能需要人工分析CVE描述 → 写正则匹配规则（耗时3h/漏洞），现在利用混元大模型，自动同步CVE+大模型自动解析 -> 生成漏洞检测逻辑只需要30s。实现了对AI组件相关漏洞的实时监控.

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

将对本地开放端口进行检查和识别，给出安全建议。如上文中使用了包含漏洞的ollama版本，一键检测后提示如下：![](https://image.3001.net/images/20250218/1739859202_67b425020ea7a75ea77a9.png!small)

如果在检测到AI服务在公网开放，也会提示

![](https://image.3001.net/images/20250218/1739859210_67b4250a78f00cae62d4f.png!small)
对于开发者/运维，想检测部署AI服务的安全性，执行命令

```
单个目标./ai-infra-guard -target [IP:PORT/域名] 多个目标./ai-infra-guard -target [IP:PORT/域名] -target [IP:PORT/域名]# 扫描网段寻找AI服务  ./ai-infra-guard -target 192.168.1.0/24# 从文件读取目标扫描./ai-infra-guard -file target.txt
```

![](https://image.3001.net/images/20250218/1739859226_67b4251a74e20fab4cd14.png!small)

**获取地址**

开源地址：https://github.com/Tencent/AI-Infra-Guard/下载地址（根据系统下载自己系统的版本）：https://github.com/Tencent/AI-Infra-Guard/releases

欢迎大家Star、体验并反馈工具的任何问题！

# AI安全

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)