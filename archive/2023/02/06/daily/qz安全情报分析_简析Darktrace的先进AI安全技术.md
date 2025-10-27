---
title: 简析Darktrace的先进AI安全技术
url: https://mp.weixin.qq.com/s?__biz=MzI1MDA1MjcxMw==&mid=2649907964&idx=1&sn=c28c44cf81c785e565d182fad58923e5&chksm=f18eebfac6f962ec96a12a798ce2e72de528e4fbad3b93fe5f2b1ef52eb7a80fe6a9d2a86771&scene=58&subscene=0#rd
source: qz安全情报分析
date: 2023-02-06
fetch_date: 2025-10-04T05:47:57.635311
---

# 简析Darktrace的先进AI安全技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aff8CeTWGibCnuXJ615DHDITgKJfpKp7jVAPpIibfqqPyy6SqhlfQ0WsRTKk6fv4XMQd7TEHm9MtibQnI6q4yFYnQ/0?wx_fmt=jpeg)

# 简析Darktrace的先进AI安全技术

原创

rayh4c

先进攻防

Darktrace是由剑桥大学的数学家以及英美网络情报专家于2013年创立的网络安全AI公司，与其他网络安全公司不同，Darktrace 使用多种独特的算法和数学模型来查找计算机网络中的恶意活动。

**算法**

Darktrace使用了两种算法：贝叶斯统计和蒙特卡罗模拟。

前者是一种概率论，它允许计算机网络专家建立网络常规活动的基线。  这些专家将这个参考点纳入算法，帮助计算机使用观察证据寻找异常行为，例如像斯诺登这样的人翻阅敏感文件。

后者是一种预测方法，帮助网络安全分析师尝试预测未来的不确定性。具体来说，它可以帮助分析师估计一系列变量，例如攻击者渗透目标计算机系统的可能性。然而，不仅如此，它还可以帮助分析师了解每个变量结果的可能性有多大。

**调查取证需求**

由于Darktrace创立人员都有国家安全部门情报人员身份背景，大部分产品应该符合APT调查响应和取证需求，执法部门的APT调查取证，在定位到某台主机的异常后，经常会对主机的系统日志、文件痕迹和网络流量等按照时间线进行精细化的线性评估分析。

从Darktrace早期的界面可以发现这样的痕迹，Darktrace会为使用者呈现单个主机根据时间排序的所有网络行为。

![](https://mmbiz.qpic.cn/mmbiz_png/aff8CeTWGibB3pHt1U7pN0Nq8vYzluvM19wTAVXAObibPlf3iaz9T0Z2IIPpro1X1Tbvj9nplicaa2R3S5byhr728A/640?wx_fmt=png)

**企业级产品**

早期的Darktrace完全是供给情报分析人员的流量调查取证产品，在接受大量的资金支持后，流量调查取证产品进化为了企业级产品，Darktrace开发了各种端点、云环境和虚拟化环境的传感器。

Darktrace的这些传感器部署在企业网络之中，使用无监督的机器学习来大规模地分析网络数据，并根据它所看到的证据进行数十亿次基于概率的计算，可以呈现大型网络中所有网络节点连续的、关联的异常行为。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aff8CeTWGibB3pHt1U7pN0Nq8vYzluvM1LZjxib1GQdXQuqO2kbDT3heib9dMYSaIrOg7bic8QjoLPKIciaYxHDVtiaQ/640?wx_fmt=jpeg)

**异常告警**

Darktrace的安全运营方式类似于UEBA类产品，但专注的是APT攻击的威胁检测，其主要的核心还是根据企业的网络流量和端点行为建"正常"模型，当行为偏离这些模型时，Darktrace会将行为标记成异常。

![](https://mmbiz.qpic.cn/mmbiz_png/aff8CeTWGibCnuXJ615DHDITgKJfpKp7jsIBIZnibEu8NyDPb0hsAsC3hE0IMU5ejYMOhJ0CbZJiaBUlfavhHUa6g/640?wx_fmt=png)

这些告警模型主要分为以下几个大类，每个大类又细分为几百种异常行为：

Anomalous Connection- 异常网络连接

Anomalous File - 异常文件

Anomalous Server Activity - 异常服务器活动

Antigena - 免疫

Compliance  - 违规

Compromise  - 失陷

Device  - 设备

Infrastructure -  基础服务

System - 系统

Unusual Activity -异常活动

User - 用户

**APT调查响应**

以SolarWinds供应链攻击为例，Darktrace的一些模型并非专门为检测SolarWinds的APT攻击而设计，已经存在多年。

![](https://mmbiz.qpic.cn/mmbiz_png/aff8CeTWGibA1z9lVKpoHDyQlPozGgNXdhXOvun1y9GtnWibhCkicQJB2OqWm8Ol4mQI6QbvxKdE0mBYUNSvREvHQ/640?wx_fmt=png)

按照Darktrace的说法，比如一些传统的C2分析方法会基于IP地理位置进行异常分析，而**Darktrace可以快速分析并告警出网络中任意端点第一次出现的C2异常行为。**

比如检测Beacon类型C2的三个模型，在SolarWinds供应链攻击活动中就已经准确告警：

**Compromise / Agent Beacon to New Endpoint**

**Compromise / SSL Beaconing to New Endpoint**

**Compromise / HTTP Beaconing to New Endpoint**

接着攻击者进入内部网络，他们就会使用多个不同的失陷凭证进行横向移动，用于横向移动的凭证总是与正常的用于远程访问的凭证不同。**一个设备第一次出现多个用户凭证进行登录和管理员凭据登录都是异常行为，这可能会触发以下网络人工智能模型**：

**User / Multiple Uncommon New Credentials on Device**

**User / New Admin Credentials on Client**

在后渗透阶段，攻击者会以远程方式执行各种荷载和工具，**从网络、设备到异常行为都会触发Darktrace的多个模型告警**：

**Anomalous Connection / New or Uncommon Service Control**

**Anomalous Connection / High Volume of New or Uncommon Service Control**

**Device / AT Service Scheduled Task**

**Device / Multiple RPC Requests for Unknown Services**

**Device / Anomalous SMB Followed By Multiple Model Breaches**

**Device / Suspicious File Writes to Multiple Hidden SMB Shares**

**Unusual Activity / Anomalous SMB to New or Unusual Locations**

**Unusual Activity / Sustained Anomalous SMB Activity**

**小结**

Darktrace这类产品的最早定位是为满足执法机构的取证和情报人员的调查分析需求，对于使用者的要求极高。

在转变为企业产品后，可以看到Darktrace定位仍然没有改变，致力于攻击者攻击过程的全阶段异常告警，这对于企业级的安全运营要求太高，其产品形态更适合于保密等级更高的涉密网络。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/aff8CeTWGibA5zAI16OFZEHI5c51EBAElrFjYskP0ecgvlYSJqIs1gTpBpvQfXOXicpEefcQxeu3icgfruknxYCAQ/0?wx_fmt=png)

先进攻防

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aff8CeTWGibA5zAI16OFZEHI5c51EBAElrFjYskP0ecgvlYSJqIs1gTpBpvQfXOXicpEefcQxeu3icgfruknxYCAQ/0?wx_fmt=png)

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