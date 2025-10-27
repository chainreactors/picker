---
title: 关于Ollama存在未授权访问漏洞的安全公告
url: https://mp.weixin.qq.com/s?__biz=MzU3ODM2NTg2Mg==&mid=2247495797&idx=1&sn=405ff36b426052ed5994f6793b38063c&chksm=fd74c0bcca0349aa01515105ac52bece7179a4bf2df9578d84c8e1dec5cf48b729349935bf04&scene=58&subscene=0#rd
source: CNVD漏洞平台
date: 2025-03-02
fetch_date: 2025-10-06T21:57:40.934159
---

# 关于Ollama存在未授权访问漏洞的安全公告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/pMINP9OQkbia6uGzTIEXQ5wkjrFic6v4OhnwLJVWsNDeqJPlDFicp0ft343WQUeOCibQw4eXd1dQI7TeCFttxsuwaw/0?wx_fmt=jpeg)

# 关于Ollama存在未授权访问漏洞的安全公告

原创

CNVD

CNVD漏洞平台

安全公告编号:CNTA-2025-0003

近日，国家信息安全漏洞共享平台（CNVD）收录了Ollama未授权访问漏洞（CNVD-2025-04094）。未经授权的攻击者可以远程访问Ollama服务接口执行敏感资产获取、虚假信息投喂、拒绝服务等恶意操作。CNVD建议受影响的单位和用户立即采取措施防范漏洞攻击风险。

**一、漏洞情况分析**

Ollama是一个本地私有化部署大语言模型（LLM，如DeepSeek等）的运行环境和平台，简化了大语言模型在本地的部署、运行和管理过程，具有简化部署、轻量级可扩展、API支持、跨平台等特点，在AI领域得到了较为广泛的应用。

Ollama存在未授权访问漏洞。由于Ollama默认未设置身份验证和访问控制功能，未经授权的攻击者可在远程条件下调用Ollama服务接口，执行包括但不限于敏感模型资产窃取、虚假信息投喂、模型计算资源滥用和拒绝服务、系统配置篡改和扩大利用等恶意操作。未设置身份验证和访问控制功能且暴露在公共互联网上的Ollama易受此漏洞攻击影响。

CNVD对该漏洞的综合评级为“高危”。

**二、漏洞影响范围**

漏洞影响的产品和版本：

Ollama所有版本（未设置访问认证的情况下）

**三、漏洞处置建议**

请使用Ollama部署大模型的单位和用户立即采取以下措施进行漏洞修复：

1、若Ollama只提供本地服务，设置环境变量Environment="OLLAMA\_HOST=127.0.0.1"，仅允许本地访问。

2、若Ollama需提供公网服务，选择以下方法添加认证机制：

1）修改config.yaml、settings.json 配置文件，限定可访问Ollama 服务的IP地址；

2）通过防火墙等设备配置IP白名单，阻止非授权IP的访问请求；

3）通过反向代理进行身份验证和授权（如使用OAuth2.0协议），防止未经授权用户访问。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/pMINP9OQkbhv2uDwc7hNMH9gPUUt39C13bYw7EhIhmITpa6692RtN0xDyb4rTiaTpewIpuGUrD1Ckf1lCVStiaRg/0?wx_fmt=png)

CNVD漏洞平台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pMINP9OQkbhv2uDwc7hNMH9gPUUt39C13bYw7EhIhmITpa6692RtN0xDyb4rTiaTpewIpuGUrD1Ckf1lCVStiaRg/0?wx_fmt=png)

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