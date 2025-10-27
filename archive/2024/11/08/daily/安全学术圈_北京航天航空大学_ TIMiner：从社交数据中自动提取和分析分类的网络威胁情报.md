---
title: 北京航天航空大学| TIMiner：从社交数据中自动提取和分析分类的网络威胁情报
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491363&idx=1&sn=016f19fb9aff072510b7bcdf6c025c98&chksm=fe2ee0a8c95969be6be0ff7bc1b9f59b3905f5c81f7bb32566bdb369d8757655eb7fb2eff06f&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-11-08
fetch_date: 2025-10-06T19:20:18.599168
---

# 北京航天航空大学| TIMiner：从社交数据中自动提取和分析分类的网络威胁情报

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WEX6ASTKBTcgRtJR5icMSf0nIugCCddcnHjfupOTl5aR1Jc9XkiaVTbQdPcniaqwMkuG7C9MH6p9fWpQ/0?wx_fmt=jpeg)

# 北京航天航空大学| TIMiner：从社交数据中自动提取和分析分类的网络威胁情报

原创

Ledraw

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WEX6ASTKBTcgRtJR5icMSf0nibtFuOOtkv8sUHuNUia1Z4uvpfAiaRmchwibDYiaywLwmgwEM0H8cJth1Dg/640?wx_fmt=jpeg)
> *原文标题：TIMiner: Automatically extracting and analyzing categorized cyber threat intelligence from social data*
> *原文作者：Jun Zhao , Qiben Yan , Jianxin Li , Minglai Shao , Zuti He , Bo Li*
> *发表期刊：Computer & Security*
> *原文链接：https://seit.egr.msu.edu/paper/CS2020\_TIMiner.pdf*
> *主题类型：CTI*
> *笔记作者：Ledraw*

## 研究背景

现有的大多数方法无法识别未知的 IOC；无法自动生成带有域标签的分类 CTI

## 创新点

基于卷积神经网络 （CNN） 的识别器，可自动识别 CTI 所属的域，以及分层 IOC 提取方法，将单词嵌入和句法依赖性无缝融合，可以识别看不见的 IOC 类型，从而生成特定域的网络威胁情报。

## 贡献

* 开发基于 CNN 的自动化域识别器，以将 CTI 分配给它所影响的相应域。本研究中主要关注金融、政府、教育、物联网和工业控制系统。
* 提出一种基于词嵌入和句法依赖性的自动化 IOC 提取方法，从威胁描述文本中提取 IOC，既保证了预定义 IOC 提取的高精度，又能识别和提取不可见类型的 IOC。
* 提出了 Threat-Index，这是一种新的安全评估标准，用于评估不同领域的安全状态；Threat-Index 捕获多个域中威胁影响的差异，并量化每个域的威胁严重性。
* 分析了超过 118000 篇文本，对每个领域的威胁情报的演变有了更深层次的认识，最有趣的为以下方面：

+ DDOS(分布式拒绝服务攻击)
+ Phishing（网络钓鱼）
+ Ransomware （勒索软件）

## TIMiner 总体框架

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WEX6ASTKBTcgRtJR5icMSf0nCpwy0Mibxca3UtaCAZEvo7VPa24pFRvRrQtgicIBSKmEqwjRqicyqtplQ/640?wx_fmt=jpeg)

### CTI 域识别器

用于识别已知和未知的 IOC，利用 kernel=5 的 256 个过滤器来了解每个威胁描述的本地特征，然后将池化的特征向量拼接成一个完全连接的层。最后，利用 soft-max 激活函数计算 CTI 的每个域标签的概率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEX6ASTKBTcgRtJR5icMSf0nGQ2sSPdIZISlbKtcqjDOQ2caQE9cGWwKpoJK6hvRq4pZ2MHORxNnBA/640?wx_fmt=png&from=appmsg)

处理过程算法：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEX6ASTKBTcgRtJR5icMSf0nPARtuEkV69z1c1ZIicQ76HF6KIj4coicXvBOAF1SelS0VLhyY9Rnym5A/640?wx_fmt=png&from=appmsg)

### 生成具有域标签的 CTI

算法：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEX6ASTKBTcgRtJR5icMSf0nIDM8OvzzKkj9Fv4ntlbZdro639oOy3FTianq6T08tM2qxa7IFWgS0Fg/640?wx_fmt=png&from=appmsg)

生成示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEX6ASTKBTcgRtJR5icMSf0nlY4d7Z8DXKSkQGyZmIl7SMLiaTugiaoCxdCDDJrq7FFLtV3fJiaJPxsJg/640?wx_fmt=png&from=appmsg)

### 识别 IOC 方法

1. 正则匹配

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEX6ASTKBTcgRtJR5icMSf0nzZaDaRCX5nezrZqFKM4O2wuNrw1UMbdIibLuuUwKUv69sZH2C8PIPhw/640?wx_fmt=png&from=appmsg)

2. 深度识别：BiLSTM+CRF 识别 IOC（正则表达无法识别的 IOC）
3. 词嵌入方法：利用word2vec模型实现一种有效的词表示方法，它超越了简单的句法规律，允许在嵌入式向量空间中进行简单的代数操作。

## 发现

DDOS:

* 大多数教育性 DDoS 攻击是 TCP 洪水攻击；
* 大多数政府和 ICS DDoS 攻击是域名系统 （DNS） 反射器攻击；
* 对于金融 DDoS 攻击，黑客通常会不断向目标服务器提交查询脚本以请求资源。
* 在物联网 DDoS 攻击中，攻击者入侵暴露在互联网上的物联网设备（例如摄像头、传感器）以构建僵尸网络，而被感染的设备将由隐蔽的 C&C 服务器远程控制。

勒索软件：

* Petya 利用 CVE-20170199 漏洞进行网络钓鱼攻击，然后通过 EternalBlue 和 Eternal Ransom 漏洞传播。但是，WannaCry 会自动扫描 Windows 的 445 端口甚至电子信息屏幕，并在受感染的计算机和服务器中放置勒索软件、远程控制、特洛伊木马、矿工和其他恶意组件。

网络钓鱼：

* 从电子邮件网络钓鱼演变为鱼叉式网络钓鱼，并最终演变为最复杂的 Watering hole 网络钓鱼

## 攻击趋势分析结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEX6ASTKBTcgRtJR5icMSf0nwugoW5aJRT4d3SvV3FicfITzjiaXm01tc2R1GHRoqD2Emyic0FMZejIzw/640?wx_fmt=png&from=appmsg)

## 总结

在本文中，提出了一种新的 CTI 提取框架 TIMiner，用于自动提取 IOC 并从社交媒体中生成带有域标签的分类 CTI。更具体地说，首先，提出了一种基于 CNN 变体的域标记方法，用于标记威胁描述的域标记。然后，提出了一种基于词嵌入和句法依赖性的分层 IOC 提取方法，该方法能够有效地识别未知的 IOC。最后，将 IOC 与其相应的域标记组合在一起，以生成特定于域的 CTI。特定于域的 CTI 可以与相关的 CTI 订阅者共享，并允许他们快速识别各自行业的安全状况。此外，还提出了 Threat-Index 来定量衡量每个域中不同类型攻击造成的威胁严重性。通过分析 TIMiner 生成的特定域 CTI，可以发现有关威胁的新见解，并执行威胁趋势分析，以促进为多个域设计更好的网络防御机制。

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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