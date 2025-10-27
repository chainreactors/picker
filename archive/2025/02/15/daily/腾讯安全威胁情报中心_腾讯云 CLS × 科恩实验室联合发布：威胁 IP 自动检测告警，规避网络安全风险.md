---
title: 腾讯云 CLS × 科恩实验室联合发布：威胁 IP 自动检测告警，规避网络安全风险
url: https://mp.weixin.qq.com/s?__biz=MzI5ODk3OTM1Ng==&mid=2247510033&idx=1&sn=9ba4b11c79a48058d7fa30f0c24b884c&chksm=ec9f7162dbe8f8740b4cbf063ea30f25411764ac497b46f88f131b30e82e8cc03105c26a4182&scene=58&subscene=0#rd
source: 腾讯安全威胁情报中心
date: 2025-02-15
fetch_date: 2025-10-06T20:37:04.352858
---

# 腾讯云 CLS × 科恩实验室联合发布：威胁 IP 自动检测告警，规避网络安全风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HSLP4ziapR9g4PhKKwkUcZlibeUVRlU6icQtEujCI65ZyUR9h4oGlCp2zlT1RdmGCNRwBvT6OFrofhic1ZdXbQjBGQ/0?wx_fmt=jpeg)

# 腾讯云 CLS × 科恩实验室联合发布：威胁 IP 自动检测告警，规避网络安全风险

腾讯安全威胁情报中心

以下文章来源于云原生日志服务CLS
，作者日志服务 CLS

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM768g4iak3b3ib0FicYbaib1uMWzjibcbn6ibMaUVduLGoJMmBA/0)

**云原生日志服务CLS**
.

云原生日志服务CLS官方认证公众号，不定时为您推送CLS产品最新动态，分享技术干货，为您解决各种业务运营、安全监控、日志审计、日志分析等问题，日志接入请与我们联系。

**导语**

网络安全威胁日益严峻，企业面临的攻击手段不断演变。为了帮助用户有效识别和防范潜在风险，日志服务 CLS 联合科恩实验室推出“威胁 IP 检测”功能。

该功能基于腾讯安全（https://tix.qq.com/）提供的海量威胁情报，可自动分析日志中的访问来源 IP，识别并定位恶意 IP，助力企业构建更完善的安全防护体系。

**功能介绍**

CLS 威胁 IP 检测功能基于腾讯安全威胁情报中心（科恩实验室）提供的情报库，该情报库拥有 **3亿+安全情报，每日处理威胁数据超过 3万亿**，帮助用户有效预防网络安全风险。

开启威胁 IP 检测功能后，系统会自动对访问日志中的 IP 进行实时分析，识别恶意 IP，包括但不限于：

* **网络攻击：**曾对计算机信息系统、基础设施、计算机网络或个人计算机设备进行攻击
* **漏洞利用：**利用程序中的某些漏洞使攻击者能够在未经授权的情况下访问或者破坏系统
* **Web 攻击：**包括 XSS 跨站脚本攻击；CSRF 跨站请求伪造；SQL 注入攻击等
* **网络爆破：**通过暴力破解尝试获取用户账户访问权限

当检测到恶意 IP 时，系统提供详细的情报信息，包括威胁等级、威胁分类标签以及在当前业务系统下的关联访问日志，帮助用户快速评估威胁，并通过黑名单等安全策略封禁相关 IP。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HSLP4ziapR9g4PhKKwkUcZlibeUVRlU6icQ7c9OiczaDaLYy7HMoQAwKEXpPXRlMYH46rMficu9Bos296pDFB5EcvPQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HSLP4ziapR9g4PhKKwkUcZlibeUVRlU6icQhicVvBCmMFcAgFvpGS6npyiaIgLHzGKA99CysUCAPsN6ed8rKjVSIHGg/640?wx_fmt=png&from=appmsg)

以负载均衡 CLB 为例，通过绑定安全组可禁止指定IP访问。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HSLP4ziapR9g4PhKKwkUcZlibeUVRlU6icQmwCATUC7rWUOCZ8AeHdvrjQ4yOfkRXYE8sw78LLCXCUKJXvS9SXPUw/640?wx_fmt=png&from=appmsg)

**适用场景**

* **云服务访问安全：**检测负载均衡 CLB、对象存储 COS、内容分发网络 CDN、边缘安全加速平台 EO、云原生 API 网关等云服务是否存在恶意IP访问，防止恶意流量攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HSLP4ziapR9g4PhKKwkUcZlibeUVRlU6icQyBGGoD3zamGoZ9ncR3xYMc3LnSarGDicW9vdngnZqKftPYtb9CmiadPQ/640?wx_fmt=png&from=appmsg)

* **Web 应用安全：**检测访问网站的恶意 IP，发现潜在安全威胁
* **API 安全：**识别恶意 IP 请求，防止 API 滥用
* **安全审计：**分析企业内部的流量及操作日志，及时发现异常行为

**核心优势**

* **实时检测：**无需对日志进行预处理，即可实时全量自动分析
* **主动告警：**可配置告警策略，发现恶意 IP 后主动通知用户，便于及时采取应对措施
* **安全协同：**检测结果可与安全组、防火墙、WAF 等云服务安全策略协同，构建更完善的安全防护体系

**立即体验**

登录日志服务控制台，在云产品中心页面点击【腾讯安全 | 威胁 IP 检测】，选择需要检测的日志主题及 IP 字段即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HSLP4ziapR9g4PhKKwkUcZlibeUVRlU6icQIIJ2ybOQwibrNF3SjSSicEbCFmEL7k5oQjxqYlibDziaPMQytXOKiaeUQNA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HSLP4ziapR9g4PhKKwkUcZlibeUVRlU6icQAK4iaBTsWb5wVYjmQTIe5TwuicvwBNiclC0T4uET3lbEBr4qmm2NMOJdg/640?wx_fmt=png&from=appmsg)

点击文末“阅读原文”，快速体验检测效果。

END

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HSLP4ziapR9g4PhKKwkUcZlibeUVRlU6icQ0JrmycfvmdNuJJibZyr2oB2p2kpLxz0orYicI8NU7a0Z9iaXgNwaDJibJw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWUu1j1TYiaYRU8wWVGpaHhqaEDCiah9eDwNn00ncbMsWBQwBbd41N9WNYEvp7neMHMksDS9dScCZ2aQ/0?wx_fmt=png)

腾讯安全威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWUu1j1TYiaYRU8wWVGpaHhqaEDCiah9eDwNn00ncbMsWBQwBbd41N9WNYEvp7neMHMksDS9dScCZ2aQ/0?wx_fmt=png)

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