---
title: 重大供应链威胁！这个 Java 开源框架存在严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247535137&idx=4&sn=e2323b85a30494c647b84f9ab8100c6b&chksm=c1e9c670f69e4f66027c941af8c6edea7b4f7128b43e6b7b73e00f104d42398b2679cf1cb3f3&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-03-04
fetch_date: 2025-10-04T08:39:56.748570
---

# 重大供应链威胁！这个 Java 开源框架存在严重漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguJ86m5mDbJOo3oc8pib7tf1jHcQkxibU4pRfwRe9v87wHhoPhIhDpam8uZ8RBWznQGmUI2E17TdIXA/0?wx_fmt=jpeg)

# 重大供应链威胁！这个 Java 开源框架存在严重漏洞

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguJ86m5mDbJOo3oc8pib7tf1aAU0biabiaMHxVEleq0rpjwolMibb2ALLliaC2YszqS2o6sgMErm2xPic8Q/640?wx_fmt=jpeg)

美国网络安全和基础设施安全局（CISA）的安全研究人员报告称，一个受广泛使用的开源Java框架中存在严重漏洞并被攻击者利用，以向未打补丁的服务器部署后门。专家表示，这种情况可能会对未打补丁的软件构成重大供应链威胁。

CISA已将CVE-2022-36537添加到其已知已开发漏洞（KEV）目录中，该漏洞影响ZK Java Web框架9.6.1、9.6.0.1、9.5.1.3、9.0.1.2和8.6.4.1版本。

根据KEV列表，在ZK框架AuUploader servlets中发现的这个漏洞，可能允许攻击者 “检索位于Web上下文中的文件内容”，从而窃取敏感信息。CISA表示：该漏洞可以影响多个产品，包括但不限于ConnectWise R1Soft Server Backup Manager。

事实上，该漏洞在2022年10月首次出现便引起广泛关注，当时ConnectWise对其产品中漏洞的存在发出了警报，特别是ConnectWise Recover和R1Soft服务器备份管理器技术。Huntress的高级安全研究人员John Hammond和Caleb Stewart随后发表了一篇关于如何利用该漏洞的博文。

CISA和Huntress都是根据Fox-IT 2月22日发表的研究报告发出警告的，该报告发现有证据表明攻击者使用易受攻击版本的ConnectWise R1Soft Server Backup Manager软件 作为初始访问点和控制通过R1Soft Backup Agent连接的下游系统的平台，研究人员在一篇博客文章中写道。

研究人员在博文中还写道：这个代理被安装在系统上，以支持被R1Soft服务器软件备份，通常以高权限运行。这意味着，在对手最初通过R1Soft服务器软件获得访问权后，它能够在连接到该R1Soft服务器的所有运行代理的系统上执行命令。

# **漏洞的历史**

ConnectWise方面在10月迅速采取行动为产品打补丁，向ConnectWise服务器备份管理器（SBM）的云端和客户端实例推送了自动更新，并敦促R1Soft服务器备份管理器的客户立即升级到新的SBM v6.16.4。

总部位于德国的安全厂商Code White GmbH的一名研究人员率先发现了CVE-2022-36537，并在2022年5月向ZK Java Web框架的维护者报告。他们在该框架的9.6.2版本中修复了这个问题。

根据Huntress的博文，ConnectWise意识到其产品的漏洞，当时同一公司的另一位研究人员发现ConnectWise的R1Soft SBM技术正在使用有漏洞的ZK库版本，并向公司报告了这个问题。

当该公司在90天内没有回应时，研究人员在Twitter上公布了一些关于如何利用该漏洞的细节，Huntress的研究人员利用这些细节复制了该漏洞并完善了一个概念验证（PoC）漏洞。

Huntress的研究人员最终证明他们可以利用该漏洞泄露服务器私钥、软件许可信息和系统配置文件，并最终在系统超级用户的背景下获得远程代码执行。

当时，研究人员通过Shodan发现了 多达5000个暴露的服务器管理器备份实例，所有这些都有可能被威胁者利用，同时还有他们的注册主机。他们推测，该漏洞有可能影响到比这更多的机器。

# **供应链面临风险**

当Huntress对该漏洞进行分析时，没有证据表明存在主动利用的情况。现在，随着这种情况的改变，不仅在ConnectWise，在其他产品中也存在任何未打补丁的ZK Java Web框架版本。这对攻击者来说无疑是利好的，同时这可能给供应链带来重大风险。

Fox-IT的研究表明，全世界对ConnectWise的R1Soft服务器软件的利用大约始于11月底，也就是Huntress发布其PoC之后不久。

研究人员写道：在指纹识别的帮助下，我们已经在全球范围内确定了多个被攻击的主机供应商。

Fox-IT研究人员在1月9日说，他们已经确定了 总共有286台运行R1Soft服务器软件的服务器带有特定后门。

根据KEV列表，CISA敦促任何仍在使用受影响ConnectWise产品的未修补版本的组织，根据供应商说明更新其产品。虽然到目前为止，该漏洞的存在仅在ConnectWise产品中被发现，但使用未修补版本框架的其他软件也容易受到攻击。

**参考链接：**

https://www.darkreading.com/risk/cisa-zk-java-framework-rce-flaw-under-active-exploit

原文来源：FreeBuf

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