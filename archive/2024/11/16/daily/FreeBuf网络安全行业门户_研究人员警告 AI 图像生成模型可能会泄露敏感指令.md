---
title: 研究人员警告 AI 图像生成模型可能会泄露敏感指令
url: https://www.freebuf.com/news/415336.html
source: FreeBuf网络安全行业门户
date: 2024-11-16
fetch_date: 2025-10-06T19:17:52.241689
---

# 研究人员警告 AI 图像生成模型可能会泄露敏感指令

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

研究人员警告 AI 图像生成模型可能会泄露敏感指令

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

研究人员警告 AI 图像生成模型可能会泄露敏感指令

2024-11-15 11:16:22

所属地 上海

据Cyber Security News消息，研究人员最近在高级人工智能图像生成模型中发现了一个潜在的安全漏洞，能够在无意中泄露敏感系统指令，尤其是在高级扩散模型 Recraft 中。

![](https://image.3001.net/images/20241115/1731641046_6736bed69ef463f4ddfb8.jpg!small)

近来，以Stable Diffusion 和 Midjourney 为代表的图像生成模型在人工智能生成图像领域掀起了一场革命。Invicti 的安全研究人员称，Invicti 公司的安全研究人员发现，这些模型的工作原理是通过一种称为 "去噪 "的过程，将随机噪音逐渐细化为清晰的图片。

目前在文本到图片排行榜上处于领先地位的 Recraft 所展示的功能已经超越了典型的扩散模型。研究人员注意到，Recraft 可以完成图像生成模型通常无法完成的语言任务。 例如，当提示数学运算或地理问题时，Recraft 会生成包含正确答案的图像，而其他模型则不同，它们只是将文本可视化，而无法理解。

此外，进一步的调查还发现，Recraft 采用了两级架构： 大型语言模型 (LLM) 处理和改写用户提示信息，以及将处理后的提示传递给扩散模型。这种独特的方法使 Recraft 能够处理复杂的查询，并生成更准确、更能感知上下文的图像。 不过也带来了一个潜在的漏洞。

通过仔细实验，研究人员发现某些提示可以诱使系统泄露部分内部指令。 通过生成带有特定提示的多个图像，研究人员能够拼凑出用于指导大模型行为的系统提示片段。

一些泄露的说明包括：以 "法师风格 "或 "形象风格 "开始描述、提供物体和人物的详细描述、将说明转化为描述性句子、包括具体的构图细节、避免使用 "太阳 "或 "阳光 "等词语、必要时将非英语文本翻译成英语。

这种无意中泄露系统提示的行为引起了人们对人工智能模型的安全性和隐私性的极大关注。 如果恶意行为者能够提取敏感指令，他们就有可能操纵系统、绕过安全措施或深入了解专有的人工智能技术。

这一事件为 AI 开发人员和研究人员敲响了警钟，随着 AI 不断进步并更深入地融入我们生活的各个方面，确保这些系统的安全性和完整性变得至关重要。

**参考来源：**

> [Researchers Warn of AI Image Generators Potentially Leaking Sensitive Instructions](https://cybersecuritynews.com/researchers-warn-of-ai-image-generators/#google_vignette)

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