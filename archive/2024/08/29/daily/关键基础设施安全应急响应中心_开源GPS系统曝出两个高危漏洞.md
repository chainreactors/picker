---
title: 开源GPS系统曝出两个高危漏洞
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545525&idx=2&sn=2561e9c960843541f48a7c0485262341&chksm=c1e9bee4f69e37f2159a41ed177df75958f3736f9f965e767cd823cbca87a8c875b9ccb5150c&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-29
fetch_date: 2025-10-06T18:04:59.798067
---

# 开源GPS系统曝出两个高危漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogv4nsnxkj3icF47kAr8fBgaR2AQ78zrbDLChAbbMZAoFeib0QUiaF1EHqV8OiboHzp3n3qygs800HEjLw/0?wx_fmt=jpeg)

# 开源GPS系统曝出两个高危漏洞

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogv4nsnxkj3icF47kAr8fBgaR8PeZ5y4CQ0xRXtwZ9k0kY444znXgeG6ogVUL0s9XAD8kWiaBz3BriaYg/640?wx_fmt=png&from=appmsg)

开源GPS跟踪系统Traccar近日曝出两个高危漏洞，可被黑客利用远程执行代码。

在全球GPS跟踪市场中，Traccar因其灵活的开源架构和可定制化特点，深受企业和个人用户的青睐。它被广泛应用于物流运输、车队管理、资产跟踪、安全监控以及个人定位等多个领域。通过Traccar，用户可以实现对车辆位置的实时监控、历史轨迹回放、地理围栏设置等功能，从而提高运营效率和安全性。

根据Horizon3.ai的研究员Naveen Sunkavally所述，披露的两个漏洞都是路径遍历（PathTraversal）漏洞，当启用访客注册功能（Traccar5的默认配置）时，漏洞就会被武器化利用。

以下是这两个漏洞的简要描述：

* CVE-2024-24809（CVSS分数：8.5）-路径遍历漏洞，允许上传具有危险类型的文件，攻击路径为dir/../../filename。
* CVE-2024-31214（CVSS分数：9.7）-设备图片上传功能中存在不受限制的文件上传漏洞，可能导致远程代码执行。

Sunkavally表示：“CVE-2024-31214和CVE-2024-24809的综合结果是，攻击者可将任意内容的文件放置到文件系统的任意位置。不过，攻击者只能部分控制文件名。”

这些问题与程序处理设备图片文件上传的方式有关，攻击者可以借此覆盖文件系统中的某些文件，从而触发代码执行。这些文件必须符合以下命名格式：

1. device.ext：攻击者可以控制ext（扩展名），但必须存在扩展名。
2. blah"：攻击者可以控制blah，但文件名必须以双引号结尾。
3. blah1";blah2=blah3：攻击者可以控制blah1、blah2和blah3，但必须包含双引号、分号序列和等号。

**攻击场景与利用方式**

在Horizon3.ai提出的概念验证（PoC）中，攻击者可以利用Content-Type头中的路径遍历漏洞来上传crontab文件，从而在攻击者主机上获取反向shell。然而，这种攻击方式无法在基于Debian或Ubuntu的Linux系统上运行，因为这些系统禁止crontab文件包含句号或双引号。

另一种攻击方式是利用Traccar以root用户权限安装的特性，攻击者可以投放一个内核模块，或者配置一个udev规则，使其在每次触发硬件事件时执行任意命令。

在易受攻击的Windows实例中，攻击者可以通过在C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp目录中放置一个名为device.lnk的快捷方式文件来实现远程代码执行。当目标用户登录Traccar主机时，该文件会被自动执行。

**受影响版本及修复措施**

Traccar版本5.1至5.12均受到CVE-2024-31214和CVE-2024-24809的影响。这些漏洞已在2024年4月发布的Traccar 6中得到修复，新版本默认关闭了自注册功能，从而减少了攻击面。

Sunkavally进一步解释道：“如果注册设置为true、readOnly为false且deviceReadonly为false，那么未经身份验证的攻击者可以利用这些漏洞。而这些正是Traccar 5的默认配置。”

**总结**

Traccar GPS是颇为流行的开源GPS跟踪系统，此次曝光的两个远程执行漏洞对设备和系统安全构成严重威胁。虽然这些漏洞已在Traccar 6中得到了修复，但对使用Traccar 5系列的用户来说，关闭自注册功能并更新至最新版本至关重要。确保这些配置安全，才能有效抵御潜在的网络攻击。

**参考链接：**

https://www.horizon3.ai/attack-research/disclosures/traccar-5-remote-code-execution-vulnerabilities/

原文来源：GoUpSec

“投稿联系方式：sunzhonghao@cert.org.cn”

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