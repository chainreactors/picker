---
title: CNNVD | 人工智能重要漏洞通报（2026年第五期）
url: https://mp.weixin.qq.com/s/GgKdQgtdR7g0_uzFZPeEzA
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:27:07.103516
---

# CNNVD | 人工智能重要漏洞通报（2026年第五期）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LJwWAbW20CiaRsMXDXpZ89ekx9VIxd617wBuN29iaHAS6Zqiczia8QcGZeibaic5ZiaX3ZmeLoiamZQ86q44FUmIeoj0kzQdbJrmC6TyXzLnZt6FibSY/0?wx_fmt=jpeg)

# CNNVD | 人工智能重要漏洞通报（2026年第五期）

中国信息安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_gif/LJwWAbW20CjVOCNTkiaXMLJZu5EN6FYrWq5QTWg6lH8oG45edcqias2emIIn4ByAKpZE9TnOUzMOozK18Oh9aR0yAKvdZq1iaXJ43JNAIfLAJY/640?wx_fmt=gif&from=appmsg)](https://cisat.cn/all/14915419?from_tag=1)

**漏洞情况**

根据国家信息安全漏洞库（CNNVD）统计，近期（2026年3月31日至2026年4月15日）共采集重要人工智能漏洞320个，CNNVD对这些漏洞进行了收录。本周人工智能类漏洞主要涵盖了OpenClaw、Ollama、MLflow等多个厂商（项目）。CNNVD对其危害等级进行了评价，其中超危漏洞35个，高危漏洞107个，中危漏洞178个。

鉴于近期人工智能领域漏洞呈爆发式增长态势，相关系统安全风险急剧攀升，请相关单位及个人尽快开展漏洞消控工作。

## 一 **人工智能漏洞增长数量情况**

近期CNNVD采集人工智能漏洞320个。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uOZw5Efn8evDRqGtxbkZRiajk0Oy45VWBaG8icg0xUbFEHM6pA4QygFqDSelgEkdKAPPRZzYnP6NzHNoTlAyB1khR0ETpQwic4ZHGjb0ibHMOJM/640?wx_fmt=other&from=appmsg&watermark=1#imgIndex=3)

图1 近五周漏洞新增数量统计图

## 二 **人工智能漏洞具体情况**

近期共采集人工智能漏洞320个，包括OpenClaw、Ollama、MLflow等多个厂商（项目）的漏洞。其中超危漏洞35个，高危漏洞107个，中危漏洞178个。具体如表1所示：

表1 人工智能漏洞列表

![](https://mmbiz.qpic.cn/mmbiz_png/uOZw5Efn8evqiaSRURKkFsRlKU5If8Lu40icibBrwGDQrD7qYtJgP6wK2JjMtLbenibg5OYjZicAzpZe6q6gSiboq8RJiacP9pjBZ7KFw5yOSB7Xqo/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

## 三 **重要人工智能漏洞实例**

近期重要漏洞实例如表2所示。

表2 本期重要漏洞实例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uOZw5Efn8evtvDHTosBnOb7negdk2zIg0mg9lqj5PNSeQpcFkZ8bU4eXPTymAIWQopJvYMPbIS7D5HbxK40fyc5yZG7MYQdU3czM5NfdJJk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

1. OpenClaw 操作系统命令注入漏洞（CNNVD-202603-6234）

OpenClaw是一个开源的智能人工助理。

OpenClaw 2026.3.13之前版本存在操作系统命令注入漏洞，该漏洞源于未清理路径包含的shell元字符，攻击者利用该漏洞可以远程注入命令。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/openclaw/openclaw/releases

2. MLflow 操作系统命令注入漏洞（CNNVD-202603-6212）

MLflow是一个开源简化机器学习的开发平台。

MLflow存在操作系统命令注入漏洞，该漏洞源于model\_uri参数未经适当清理可直接嵌入shell命令，攻击者利用该漏洞可以注入命令和提升权限。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://github.com/mlflow/mlflow/releases

3. LoLLMs 安全漏洞（CNNVD-202604-1398）

LoLLMs是一个大型语言与多模态系统。

LoLLMs 2.1.0版本存在安全漏洞，该漏洞源于使用弱密钥签署JSON Web Tokens导致访问控制不当，攻击者利用该漏洞可以离线暴力破解以恢复密钥，进而伪造管理令牌并提升权限。

目前厂商已发布升级补丁以修复漏洞，参考链接：

https://lollms.com/

（来源：CNNVD）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20Ch90C0U9HhePiaDDzrHse2xBydmAsYOkj3g1vHTJECnOV5PmwENG3yNvVJibc15jVAgXMuNfzEd5iaoicqbsoS5dkrIs3LvEU5CIpQ/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/LJwWAbW20ChpyjG6chE3Tjw23vfFrb9ubWVVA4ERfMMn8cAX6iaVQPyynY3c0PZtjKTjvxGQhGjQuTG2Y4puJHVdgoWqiaZyNWGkaM35oUPGU/640?wx_fmt=png&from=appmsg)](https://cisat.cn/)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

中国信息安全

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