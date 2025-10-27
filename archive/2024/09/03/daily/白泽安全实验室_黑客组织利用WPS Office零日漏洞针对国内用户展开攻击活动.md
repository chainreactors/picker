---
title: 黑客组织利用WPS Office零日漏洞针对国内用户展开攻击活动
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492305&idx=1&sn=d9cc7a790db58f5b22afa02b52a9cde2&chksm=e90dc8fbde7a41ede9648f2572bb5e59d26f8e7c663778e3bb1a1fdc5560c59c3bb6668177cc&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-09-03
fetch_date: 2025-10-06T18:28:22.149589
---

# 黑客组织利用WPS Office零日漏洞针对国内用户展开攻击活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 黑客组织利用WPS Office零日漏洞针对国内用户展开攻击活动

BaizeSec

白泽安全实验室

**事件概述：**

近期，ESET研究团队披露了一起严重的网络安全事件，疑似韩国背景的APT-C-60网络间谍组织以国内和东亚国家为目标，利用WPS Office的两个零日漏洞（CVE-2024-7262和CVE-2024-7263）进行网络攻击，并部署了SpyGlace恶意软件。WPS Office是一款在全球拥有超过5亿活跃用户的办公软件，尤其在国内及东亚地区被广泛使用。攻击者通过精心构造的恶意文档，利用软件漏洞执行远程代码，在用户不知情的情况下执行任意代码，从而控制受害者的计算机系统，严重威胁了数百万用户的网络安全。2024年8月金山软件虽然“悄无声息”地修补了该漏洞问题，但是并没有通知客户该漏洞已被积极利用的情况。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMINc1H4Vz3AFTP6SP4qu3KGfOSLNLgXbENsyUT4Eicr7vhvia25y4JVFjGv7ufyHgUSOpvEM46bgFrMQ/640?wx_fmt=png&from=appmsg)漏洞利用的控制流程

**技术分析：**

* **CVE-2024-7262：**此漏洞允许攻击者通过劫持WPS Office插件组件 promecefpluginhost.exe执行代码。攻击者利用MHTML格式的恶意文档，嵌入隐藏的恶意超链接，诱使用户点击，从而触发漏洞。研究人员发现，攻击者通过MHTML文件格式的自动下载特性，预先将恶意库下载到目标计算机上，再通过漏洞触发执行。
* **CVE-2024-7263：**在CVE-2024-7262的补丁分析过程中，研究人员发现了另一个代码执行漏洞。此漏洞同样通过劫持 promecefpluginhost.exe 来实现代码执行，但利用了一个不同的逻辑错误。攻击者可以绕过签名验证，加载并执行攻击者控制的库。

**攻击过程：**

**1.利用MHTML格式下载恶意库：**攻击者利用MHTML格式的自动下载特性，预先将恶意库下载到目标计算机上，再通过漏洞触发执行。

**2.构造恶意超链接：**攻击者在恶意文档中嵌入隐藏的恶意超链接，诱使用户点击，从而触发漏洞。

**3.利用漏洞执行恶意库：**一旦用户点击超链接，攻击者控制的恶意库就会被加载并执行，从而实现对目标计算机的控制。

**受影响版本：**

受影响的WPS Office for Windows版本从2023年8月发布的12.2.0.13110到2024年3月发布的修补版本12.1.0.16412（CVE-2024-7262）和2024年5月底发布的12.2.0.17119（CVE-2024-7263）。

**处置及建议:**

强烈建议WPS Office用户立即更新其软件至最新版本，以确保安全。用户应确保他们的软件和操作系统都保持最新，以防止潜在的安全威胁。

参考链接：

https://www.welivesecurity.com/en/eset-research/analysis-of-two-arbitrary-code-execution-vulnerabilities-affecting-wps-office/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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