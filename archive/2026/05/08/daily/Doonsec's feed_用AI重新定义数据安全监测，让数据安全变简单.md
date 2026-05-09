---
title: 用AI重新定义数据安全监测，让数据安全变简单
url: https://mp.weixin.qq.com/s/Im663UjQ-Re4knyFHGEBnQ
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:06:36.696224
---

# 用AI重新定义数据安全监测，让数据安全变简单

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdbpLuPph3RAofUeGyhM2M4ODpicrXicdvH45ibjcfgqUrgE7xIYLpzE0ictOKWYo6mB0hjzQt8t5TibR07yQLqFibTXxE5juj2USOLFY/0?wx_fmt=jpeg)

# 用AI重新定义数据安全监测，让数据安全变简单

Cismag
Cismag

信息安全与通信保密杂志社

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年春节以来，AI智能体（Agent）无疑是最炙手可热的技术概念，并逐渐从“咨询专家”变成“执行助理”。具体到数据安全领域，智能体如何落地，真正解决实际问题，而非停留在概念层面？

## **一、一个数据专员的"日常困局"**

数据安全领域，“多设备、多厂商、多格式”的复杂性，让很多组织的安全运营陷入被动。某政务数据中心，负责整体安全产品使用和风险处置的数据专员日常工作通常是这样的：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81kLROu3c7Szry8uK0r7pJPrUG7zicVSicr5We39MZpKFkH2fPbct6m520g6rCTG1bzOLPW0UzLOMDxUY3rjIaLvJxjZDCJiaXK4Dg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

**01**

### **日志接入，协调成本高**

十几家安全厂商的设备，数据库审计、API网关、终端防泄漏……每接入一种日志，就要协调厂商提供字段字典，反复沟通格式规范。一个新设备接入，**周期以周计**。

**02**

### **海量告警，甄别难度大**

日志进来了，又面临新问题——海量告警。每天成百上千条风险提示，哪些是真风险？哪些是误报？需要逐一排查，**专业门槛高、人力成本大**。

**03**

### **三级联动，检出压力重**

该省政务实行省市区三级联动的安全体系化建设。下级单位最怕的不是误报多，而是检出率低——上层通过其他事件反查下来，**追责压力极大**。

⇚左滑继续查看

## **二、“主动检出”：从源头提升检出能力**

市面上的安全智能体，大多围绕一个场景：海量误报事件，用AI做风险降噪。而美创选择了另一条路，先搭建行为图谱，再基于图谱做异常监测，从源头提升风险检出能力。这套风险监测智能体，核心是三步：

**1**

### **AI驱动的智能接入**

AI驱动的智能接入。只要设备支持Syslog、Kafka或前置库方式输出日志，无需提供字段字典，AI自动完成格式标准化。一个安全设备的日志**接入时效压缩至约1小时**。

**2**

### **行为图谱自动构建**

行为图谱自动构建。基于访问身份（终端、应用、账号）、资产（库表字段、敏感等级）、操作行为三个维度，自动搭建动态行为图谱。以周为单位作为基准线，学习周期以月为单位，**学习四个周期，完成初始化行为图谱构建**。

**3**

### **图谱驱动的风险监测**

图谱驱动的风险监测。新行为来了，先问两个问题：是否在图谱范围内？行为分布是否偏离基线？双上下文确认，实现精准检出，**检出率提升到95%**。

## **三、已落地验证，从概念走向实战**

2025年世界互联网大会上，美创正式发布美创数据安全风险监测智能体及基于AI+eBPF驱动的无侵入数据安全多智体治理技术，获得行业关注。

目前，美创数据安全风险监测智能体已在多个政企客户的生产环境部署运行，支持对接DeepSeek、通义千问、文心等主流国产大模型，适配国产算力平台。

某企业财务系统中，某业务账号正常日均访问 160 次，时长 5 分钟。

**智能体监测到：**该账号单日访问次数突然增至 200 次，会话时长仅 1 分钟，且访问路径发生变更，从常规的“表 A”转向敏感的“表 B”，访问的敏感数据量也远超历史上限，**行为偏离度高达70%**。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81lt94lP1nsajSF8aKnPibgibV8WrlRCMbNd0dXEtxRGtsJxjX9E75X8XFpQyF8ILHaeP214mQ7bhGg28LowYic4WUnOvb7eticodEg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

## **四、AI智能体时代，让数据安全变简单**

作为国内专业数据安全头部企业，美创一直希望让数据安全从抽象、专业变得简单，不再需要高专业门槛。目前，在大模型能力的加持下，这一愿景正一步步实现。

除了美创数据安全风险监测智能体，美创智能数据安全分类分级平台等产品都应用了大模型能力。其中美创智能数据安全分类分级平台、数据安全一体化平台（DSC）、美创灾备一体化平台（DRCC）等产品可以打包算力平台一起出。

AI智能体时代，美创数据安全风险监测智能体只是开端。根据规划，美创正在构建“安全多智能体”体系，涵盖智能审核专家、资产智能体、身份智能体、响应智能体、报告智能体等，配合一体化平台，实现从监测到处置的全链条智能化。

**来源：美创资讯**

**★**

**★ ★ ★**

**★**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iclynibMMTgBwgCg9mGbuByfRqykUw7pNibhqs5FTfibiagTERwjA5aIr1nWU877gknbu4l0icwleVpLxzotXXbK3thA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwhRphiasJXbLerI7qNNnpia0ibWnpkzdSTrWuZwf32kY8m9Qu17zSDTJSmvib7TNVWcIQu4M9QsFbBdA/0?wx_fmt=png)

信息安全与通信保密杂志社

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwhRphiasJXbLerI7qNNnpia0ibWnpkzdSTrWuZwf32kY8m9Qu17zSDTJSmvib7TNVWcIQu4M9QsFbBdA/0?wx_fmt=png)

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