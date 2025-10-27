---
title: WPS Office两个严重漏洞曝光，已被武器化且在野利用
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545423&idx=2&sn=f444f16d478e86e7304a44ab986ff6ae&chksm=c1e9be1ef69e3708414dae4e58d69554f9f1e62d8a2e5f72726f9132daaeec1218eb529ed743&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-21
fetch_date: 2025-10-06T18:04:19.079675
---

# WPS Office两个严重漏洞曝光，已被武器化且在野利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogslNOsaiaibfyicc59iaSOxvwHanjJYkfuibaMjMtibR4TiavG42CrMEjuz2Gh3xP6ibmUJEib5Hfuc8ibXC7iaw/0?wx_fmt=jpeg)

# WPS Office两个严重漏洞曝光，已被武器化且在野利用

关键基础设施安全应急响应中心

WPS Office作为一款用户基数超过2亿的广泛使用的办公套件，被发现存在两个关键漏洞（CVE-2024-7262和CVE-2024-7263），这些漏洞可能导致用户遭受远程代码执行攻击。这两个漏洞的CVSS评分为9.3，表明它们的严重性很高，且易于被利用。其中CVE-2024-7262已经被武器化，ESET的安全研究人员发现它正在野外被积极利用。但也有圈内小道消息称，该漏洞只会影响国际版，国内版本不受影响。

# **漏洞位置**

这两个漏洞都存在于WPS Office的`promecefpluginhost.exe`组件中。

* CVE-2024-7262影响版本为12.2.0.13110至12.2.0.13489。
* CVE-2024-7263影响版本为12.2.0.13110至12.2.0.17153（不包括17153）。

# **漏洞原因**

两个漏洞都源于不恰当的路径验证，使攻击者能够加载并执行任意的Windows库文件。

**CVE-2024-7262：**

该漏洞存在于`promecefpluginhost.exe`进程如何验证文件路径的方式中。攻击者只需诱骗用户打开一个欺骗性的电子表格文档，即可加载恶意的Windows库文件。

这种「单击即中」的漏洞允许攻击者在受害者的机器上执行任意代码，可能导致数据盗窃、勒索软件攻击或进一步的系统破坏。

**CVE-2024-7263：**

为了解决CVE-2024-7262，金山软件发布了版本12.2.0.16909的补丁。但研究人员很快发现这个补丁并不充分。

CVE-2024-7263利用了一个在原始修复中被忽略的未正确消毒的参数。这个疏忽使攻击者能够再次加载任意的Windows库文件，绕过了金山软件最初实施的安全措施。

武器化与利用

特别令人担忧的是，CVE-2024-7262已经被武器化。ESET的安全研究人员发现它正在野外被积极利用，恶意行为者正在分发旨在触发该漏洞的欺骗性电子表格文档。

# **风险缓解措施**

鉴于这些漏洞的严重性以及CVE-2024-7262已被确认的活跃利用，所有WPS Office用户必须尽快将软件更新到最新可用版本（12.2.0.17153或更高版本）。此外，建议用户采取以下额外安全措施：

* 不要随意打开来源不明的文件：特别是电子表格、文档和其他可能包含恶意代码的文件。
* 启用防火墙和反病毒软件：确保这些安全工具处于最新状态，并定期扫描系统以检测和清除潜在威胁。
* 保持警惕：关注WPS Office和其他常用软件的安全公告，及时应用补丁和更新。

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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