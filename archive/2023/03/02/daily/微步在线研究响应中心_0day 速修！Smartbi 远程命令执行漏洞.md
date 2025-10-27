---
title: 0day 速修！Smartbi 远程命令执行漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247499991&idx=1&sn=18dee09de6007d604de3d05bdb87e577&chksm=cfcaa3c3f8bd2ad506d1591df7d6e31c5e0029be63a45ded0df9225bb330debed7783748b5f6&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2023-03-02
fetch_date: 2025-10-04T08:27:10.116728
---

# 0day 速修！Smartbi 远程命令执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMLSfha8Xprsk9MWCa28ibqwCthlAEzf4pics781uwV6LFWxqfABr1yfO75ymTu2wPcarxZ3ounFY5Zg/0?wx_fmt=jpeg)

# 0day 速修！Smartbi 远程命令执行漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKfKRFs38NM1VwWwgdcibkbZDR4HSKNiboI5RjPvcFIlraPg33FWhm9sz0ZAsdFJspp4l3icRyNE7bQA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

01 漏洞概况

近日，微步在线通过“X漏洞奖励计划”获取到Smartbi大数据分析平台远程命令执行漏洞的0day相关漏洞情报，攻击者可以通过此漏洞进行任意命令执行，导致系统被攻击与控制。Smartbi是思迈特软件推出的商业智能BI软件，满足BI产品的发展阶段。思迈特软件整合了各行业的数据分析和决策支持的功能需求，满足最终用户在企业级报表、数据可视化分析、自助探索分析、数据挖掘建模、AI 智能分析等场景的大数据分析需求。 **自查检测：**

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLSfha8Xprsk9MWCa28ibqwCibudqlxiaKgVZyDwE2O8ZmKnBkgglgJUc1SRT11vfZQY2KUXiciap5TLpg/640?wx_fmt=png)

**此次**受影响版本**如下：**

|  |  |
| --- | --- |
| **Smartbi大数据分析平台** | **是否受影响** |
| V7<=Smartbi<= V10.5.8 | 是 |

02 漏洞评估

**公开程度**：PoC未公开

**利用条件**：无权限要求
**交互要求**：0-click
**漏洞危害**：高危、命令执行
**影响范围**：Smartbi大数据分析平台

03 修复方案

**1、官方修复缓解措施**
**自动升级**：
登录后台->右上角系统监控->系统补丁->安装补丁->在线更新

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLSfha8Xprsk9MWCa28ibqwChKfWFMSbeVhYicasph4552mcP1waIAcBobvQQSm4rm23fX0KPz1goZQ/640?wx_fmt=png)

**手动升级**：
下载补丁->登录后台->右上角系统监控->系统补丁->安装补丁->手动更新
**（1）补丁地址：**
https://www.smartbi.com.cn/patchinfo
**（2）参考链接：**
https://www.smartbi.com.cn/patchinfo
https://wiki.smartbi.com.cn/pages/viewpage.action?pageId=50692623 **2、流量侧检测排查**
微步在线威胁感知平台TDP已支持检测该漏洞：

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLSfha8Xprsk9MWCa28ibqwCJxBmQpq3ibvUY4QzdP8g5EnaGd9kpRqEgQXZibm4a1mxXORlMlWrpgug/640?wx_fmt=png)

**3、受影响资产排查**
微步在线攻击面管理平台OneRisk可以检出该漏洞：

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLSfha8Xprsk9MWCa28ibqwC8FhX7ewXGpGwLGcnALox2p4QkHI1hfGWBw4139icPKCicCJjibib7Iia1pA/640?wx_fmt=png)

微 步 在 线 OneCare 安 全 服 务 已 支 持 该 漏 洞 的 风 险 排 查 和 处 置
https://www.threatbook.cn/next/onecare

### 04 时间线 2022.11 微步“X漏洞奖励计划”获取该漏洞相关情报 2022.12 漏洞分析与研究 2022.12 TDP 支持检测 2023.01 OneRisk 支持检测 2023.02 厂商发布补丁 2023.03 微步发布报告

### ![](https://mmbiz.qpic.cn/mmbiz_gif/pOGBCic4vYicalEg1DqfSPY3LW7QAWjicV2WfUQibCRW6AF0aRfvFV9mqicPVcIMMvuegDhcF3KV4UNHanHkVrQjzSQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

点击下方名片，关注我们

第一时间为您推送最新威胁情报

预览时标签不可点

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