---
title: CISA警告3个工控软件系统存在严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247532489&idx=4&sn=d6c6237a6da5f631eb34cf0d3e853e15&chksm=c1e9f398f69e7a8e62e1d5339328ff19b972db72e267967ea2297f578af1a3d0531f51cd7c87&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-11-08
fetch_date: 2025-10-03T21:57:02.908566
---

# CISA警告3个工控软件系统存在严重漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogtmNfR7YdBmqP64HNLiagwzpQPEbgUq1EsSO6gYJG0icpoMIMTFNrWdoNQBT5L0524JAu6AYaLTFV8w/0?wx_fmt=jpeg)

# CISA警告3个工控软件系统存在严重漏洞

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogtmNfR7YdBmqP64HNLiagwzpwV6XdriaYRkibF37R7w6suqokKVnb6Owria5ZvcTnTlZWwXybI3G8zxNg/640?wx_fmt=png)

近日，美国网络安全和基础设施安全局（CISA）发布了三份工业控制系统（ICS）公告，涉及ETIC电信、诺基亚和Delta工业自动化的软件中的多个漏洞。其中最突出的是影响ETIC电信公司远程访问服务器（RAS）的一组三个缺陷，它 "可能允许攻击者获得敏感信息，并控制有漏洞的设备和其他连接的机器"，CISA说。

这包括CVE-2022-3703（CVSS评分：9.0），这是一个关键的缺陷，源于RAS网络门户无法验证固件的真实性，从而有可能塞进一个流氓包，授予对手后门权限。

另外两个缺陷与RAS API中的目录穿越错误（CVE-2022-41607，CVSS评分：8.6）和一个文件上传问题（CVE-2022-40981，CVSS评分：8.3）有关，可被利用来读取任意文件和上传恶意文件，从而破坏设备。

以色列工业网络安全公司OTORIO被认为是发现和报告了这些缺陷。ETIC Telecom RAS 4.5.0及之前的所有版本都存在漏洞，法国公司在4.7.3版本中解决了这些问题。

CISA的第二个公告涉及诺基亚ASIK AirScale 5G通用系统模块的三个缺陷（CVE-2022-2482、CVE-2022-2483和CVE-2022-2484），这可能为任意代码执行和安全启动功能的停止铺平道路。所有的缺陷在CVSS严重性等级中被评为8.4级。CISA指出，成功利用这些漏洞可能导致执行恶意内核，运行任意的恶意程序，或运行修改过的诺基亚程序。

据说这家芬兰电信巨头已经公布了影响ASIK 474021A.101和ASIK 474021A.102版本的缺陷的缓解说明。该机构建议用户直接与诺基亚联系，以获得进一步信息。

最后，该网络安全机构还警告说，一个路径穿越漏洞（CVE-2022-2969，CVSS评分：8.1）影响了台达工业自动化公司的DIALink产品，可被利用来在目标设备上植入恶意代码。

该漏洞已在1.5.0.0 Beta 4版本中得到解决，CISA表示可以直接联系台达工业自动化或通过台达现场应用工程（FAEs）获得该版本。

原文来源：E安全

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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