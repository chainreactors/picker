---
title: ThinkPHP开发框架曝高危漏洞，需紧急修复！
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247498726&idx=1&sn=a3230d5676fae8c8b9e5c65ebe959974&chksm=cfca98f2f8bd11e4d9272df3f0a45408d63956f9566f52f1a4e5718cb866f51f2b91b9ebac4b&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2022-12-10
fetch_date: 2025-10-04T01:07:10.847565
---

# ThinkPHP开发框架曝高危漏洞，需紧急修复！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMLrAEfHajBlJpqhvJf3SxH9OEAoR6JEHwEmicj9OezQCmK62Ic8mvDAANMzkw4TSl8TfHT2iaeXbVEQ/0?wx_fmt=jpeg)

# ThinkPHP开发框架曝高危漏洞，需紧急修复！

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKfKRFs38NM1VwWwgdcibkbZDR4HSKNiboI5RjPvcFIlraPg33FWhm9sz0ZAsdFJspp4l3icRyNE7bQA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

01 漏洞概况

微步在线通过“X漏洞奖励计划”获取到ThinkPHP开发框架命令执行漏洞的0day相关漏洞情报，攻击者可以通过此漏洞实现任意命令执行，导致系统被攻击与控制。该漏洞已在9月25日的V6.0.14被修复。ThinkPHP 是一个免费开源的，快速、简单的面向对象的轻量级PHP开发框架 ，创立于2006年初，遵循Apache2开源协议发布，是为了敏捷WEB应用开发和简化企业应用开发而诞生的。并且拥有众多的原创功能和特性，在社区团队的积极参与下，在易用性、扩展性和性能方面不断优化和改进，已经成长为国内最领先和最具影响力的Web应用开发框架，众多的典型案例确保可以稳定用于商业以及门户级的开发。

**自查检测：**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLrAEfHajBlJpqhvJf3SxH9W8G6TTiaXJl3HDOsqKIuwL4L9BW6hdpAXVECB16dS6YLvZkWUjAZs4A/640?wx_fmt=png)

**此次**受影响版本**如下：**

|  |  |
| --- | --- |
| **ThinkPHP开发框架命令执行漏洞** | **是否受影响** |
| v6.0.0 ~ v6.0.13 | 是 |

02 漏洞评估

**公开程度**：PoC未公开

**利用条件**：无权限要求
**交互要求**：0-click
**漏洞危害**：高危、命令执行
**影响范围**：ThinkPHP开发框架命令执行漏洞

03 修复方案

1、获取官网V6.0.14的补丁包，进行升级即可。

https://github.com/top-think/framework/releases/tag/v6.0.14

2、微步在线TDP已支持相关漏洞检测，对应规则ID为：S3100031334。

3、微步在线X企业版已支持相关漏洞检测：

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLrAEfHajBlJpqhvJf3SxH98myGBbNWfxQDd3eeLgvs1Cylq65gB98lUYHBGD3jneM3ibYLAX0p2lQ/640?wx_fmt=png)

### 04 时间线 2022.09 微步“X漏洞奖励计划”获取该漏洞相关情报 2022.09 漏洞分析与研究 2022.09 TDP支持检测 2022.09 厂商发布补丁 2022.12 X企业版支持检测 2022.12 报送监管 2022.12 微步情报局发布漏洞通告

### ![](https://mmbiz.qpic.cn/mmbiz_gif/pOGBCic4vYicalEg1DqfSPY3LW7QAWjicV2WfUQibCRW6AF0aRfvFV9mqicPVcIMMvuegDhcF3KV4UNHanHkVrQjzSQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

点击下方名片，关注我们

第一时间为您推送最新威胁情报

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

微步在线研究响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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