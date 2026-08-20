---
title: CNNVD | 人工智能重要漏洞通报（2026年第十二期）
url: https://mp.weixin.qq.com/s/TdQovX34rdzHOv4UbJF1gQ
source: Doonsec's feed
date: 2026-08-19
fetch_date: 2026-08-20T02:53:01.311432
---

# CNNVD | 人工智能重要漏洞通报（2026年第十二期）

# CNNVD | 人工智能重要漏洞通报（2026年第十二期）

中国信息安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_gif/LJwWAbW20CjVOCNTkiaXMLJZu5EN6FYrWq5QTWg6lH8oG45edcqias2emIIn4ByAKpZE9TnOUzMOozK18Oh9aR0yAKvdZq1iaXJ43JNAIfLAJY/640?wx_fmt=gif&from=appmsg)](https://cisat.cn/all/14915419?from_tag=1)

**漏洞情况**

根据国家信息安全漏洞库（CNNVD）统计，近期（2026年8月5日至2026年8月17日）共采集重要人工智能漏洞201个，CNNVD对这些漏洞进行了收录。本周人工智能类漏洞主要涵盖了FlowiseAI、IBM、MLflow等多个厂商（项目）。CNNVD对其危害等级进行了评价，其中超危漏洞31个，高危漏洞89个，中危漏洞81个。

## 一 **人工智能漏洞增长数量情况**

近期CNNVD采集人工智能漏洞201个。

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8etwNTuxcs61BiaH5bnQkKs7VJly6ycdWZHibiaeDJSQYt6sIxcan9e0fwibMREibcRbhpI28dka0BZtdibkYbaI4EGL0cQrcQcoBSd64/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

图1 近五周漏洞新增数量统计图

## 二 **人工智能漏洞具体情况**

近期共采集重要人工智能漏洞201个，包括FlowiseAI、IBM、MLflow等多个厂商（项目）的漏洞。其中超危漏洞31个，高危漏洞89个，中危漏洞81个。具体如表1所示：

表1 人工智能漏洞列表

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8etiaD2yuwQViaUbNFribl7Gdk3eSWheTLsQ0rBvRRk8TsrA7eRANYNhjvT3bxeVOcWAxSWeEu0SMdxRr8B8RBibfJB4vXNuRianTXXM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

## 三 **重要人工智能漏洞实例**

近期重要漏洞实例如表2所示。

表2 本期重要漏洞实例

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8esuwicpnoGKuZ2zHEQVd52WAvEsZHVjTER3H961JKdSfzZCErQQLqibOElicdt5xtXQdF5LqibWTxm7eJKXf4Ml1RSn9eO3jNsx0Qk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

1. FlowiseAI Flowise 代码注入漏洞（CNNVD-2026-19688940）

FlowiseAI Flowise是FlowiseAI公司开源的一个用于轻松构建 LLM 应用程序的工具。

FlowiseAI Flowise 3.1.3之前版本存在代码注入漏洞，该漏洞源于CSVAgent未验证初始代码块，允许CSV数据直接可以直接插入Python代码中，攻击者利用该漏洞可以执行任意操作系统命令。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/FlowiseAI/Flowise/releases

2. IBM Langflow OSS 代码注入漏洞（CNNVD-2026-63003627）

IBM Langflow OSS是美国IBM公司的一款可视化构建AI工作流的低代码工具平台。

IBM Langflow OSS 1.0.0版本至1.10.3版本存在代码注入漏洞，该漏洞源于对用户输入代码控制不当，攻击者利用该漏洞可以对目标系统注入任意代码。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://www.ibm.com/support/pages/node/7282646

3. MLflow 服务端请求伪造漏洞（CNNVD-2026-44491345）

MLflow是一个开源的机器学习开发平台,包括跟踪实验、将代码打包成可重复的运行以及共享和部署模型。

MLflow 3.14.0版本及之前版本存在服务端请求伪造漏洞，该漏洞源于创建网关密钥时未验证auth\_config.api\_base值的协议、主机或IP范围，攻击者利用该漏洞可以通过代理端点访问内部地址，从而暴露云实例IAM凭据。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://mlflow.org/

（来源：CNNVD）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20Ch90C0U9HhePiaDDzrHse2xBydmAsYOkj3g1vHTJECnOV5PmwENG3yNvVJibc15jVAgXMuNfzEd5iaoicqbsoS5dkrIs3LvEU5CIpQ/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/LJwWAbW20ChpyjG6chE3Tjw23vfFrb9ubWVVA4ERfMMn8cAX6iaVQPyynY3c0PZtjKTjvxGQhGjQuTG2Y4puJHVdgoWqiaZyNWGkaM35oUPGU/640?wx_fmt=png&from=appmsg)](https://cisat.cn/)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

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