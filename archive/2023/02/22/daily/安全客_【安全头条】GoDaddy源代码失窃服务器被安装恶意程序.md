---
title: 【安全头条】GoDaddy源代码失窃服务器被安装恶意程序
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649783157&idx=2&sn=f2a45d28e741aabd4f0533696299a752&chksm=88934b1abfe4c20c2e2f71bf44362c64142232acd858ba3f41983a5de7463c0a2c305207ee40&scene=58&subscene=0#rd
source: 安全客
date: 2023-02-22
fetch_date: 2025-10-04T07:43:23.723980
---

# 【安全头条】GoDaddy源代码失窃服务器被安装恶意程序

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb7hTrJTpdcjwOoHYOYuKbLTmEV1woXIuu09eKzvkvVDD6jRLvJgTRhA1bb1ODPE29zLI6FvDl7ia9A/0?wx_fmt=jpeg)

# 【安全头条】GoDaddy源代码失窃服务器被安装恶意程序

安全客

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb484SnTLnoXJ62gPG7yjtA3l5Lia57HmsbMcUrPLCCf2fgE9c0NcLfPPT7icG57k4mzibKmDrqEnlx6g/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**第460期**

**你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。****欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！**

## **1、GoDaddy源代码失窃**

## **服务器被安装恶意程序**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb7hTrJTpdcjwOoHYOYuKbLTyhPKxQyvk9xiaZbIur9oqK9VJhuJueafVaAia5tjKoSsV0THfwL1npWw/640?wx_fmt=png)

Web 托管巨头 GoDaddy 证实它遭到了持续多年的入侵，源代码失窃服务器也被安装恶意程序。

GoDaddy 是在去年 12 月初收到客户报告其网站被重定向到随机域名后发现未知攻击者入侵了它的 cPanel 共享托管环境。它的调查显示攻击者在它的服务器上活跃了多年，近几年披露的多起安全事故都与此相关。黑客在它的服务器上安装了恶意程序，还窃取到部分服务相关的源代码。它在 2021 年 11 月和 2020 年 3 月披露的安全事件都与此相关。其中 2021 年 11 月的事件影响到了它管理的 120 万 WordPress 客户，攻击者利用一个窃取的密码入侵了它的 WordPress 托管环境，窃取到了客户的邮件地址、管理员密码、sFTP 和数据库凭证，以及部分 SSL 私钥。[点击“阅读原文”查看详情]

## **2、恶意程序滥用微软IIS功能**

## **在Windows上执行恶意代码**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb7hTrJTpdcjwOoHYOYuKbLTHBjzapf5mg5KWw6SSN1lhcWQsh8LialhGnK8PibsBADObNHnVxhaMdog/640?wx_fmt=png)

安全公司赛门铁克的研究人员发现一种恶意程序滥用微软 IIS 的一项功能隐蔽的渗出数据和执行恶意代码。

微软 IIS（Internet Information Services）是广泛使用的 Web 服务器，它的一项功能叫 Failed Request Event Buffering（FREB），旨在帮助管理员诊断错误，FREB 能从缓存中将部分错误相关的请求写入磁盘。黑客找到了滥用该功能的方法，攻击者首先需要入侵运行 IIS 的 Windows 系统，启用 FREB，通过将恶意代码注入 IIS 进程内存劫持执行，它随后就能拦截所有 HTTP 请求，寻找特殊格式的请求，这种特殊的请求能以隐蔽的方式执行远程代码，系统上没有可疑文件或进程在运行。研究人员将这种恶意程序命名为 Frebniis。[点击“阅读原文”查看详情]

## **3、Mirai 恶意软件**

## **新变种感染 Linux 设备**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb7hTrJTpdcjwOoHYOYuKbLTWkQ2zck52x8beNsiaMicGch5ekTePW1c3U8AF9do1TJJymETotsEYBnQ/640?wx_fmt=png)

一个被追踪为“V3G4”的 Mirai 恶意软件新变种异常活跃，正在利用基于Linux 服务器和物联网设备中的13个漏洞，展开 DDoS（分布式拒绝服务）攻击。

据悉，该恶意软件通过暴力破解弱的或默认的 telnet/SSH 凭据并利用硬编码缺陷在目标设备上执行远程代码执行来传播。一旦设备遭到破坏，恶意软件就会感染该设备并将其招募到僵尸网络群中。

Palo Alto Networks（第 42 单元）的研究人员在三个不同的活动中发现了该特定恶意软件，他们报告称在 2022 年 7 月至 2022 年 12 月期间监测了恶意活动。[点击“阅读原文”查看详情]

## **4、ClamAV 开源防病毒软件中**

## **发现严重的 RCE 漏洞**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb7hTrJTpdcjwOoHYOYuKbLTMLRFq46Rd4djjQlxibwbiarUMUMhApFFoiamFrh9ia130GzHDF1BXJ4hJA/640?wx_fmt=png)

日前，思科推出了安全更新，以解决 ClamAV 开源防病毒引擎中报告的一个严重缺陷，该缺陷可能导致在易受感染的设备上远程执行代码。

据悉，该漏洞被跟踪为CVE-2023-20032（CVSS 评分：9.8），问题与驻留在 HFS+ 文件解析器组件中的远程代码执行案例有关。

该缺陷影响版本 1.0.0 及更早版本、0.105.1 及更早版本以及 0.103.7 及更早版本。谷歌安全工程师 Simon Scannell 因发现并报告了该漏洞而受到赞誉。“这个漏洞是由于缺少缓冲区大小检查，可能导致堆缓冲区溢出写入，”Cisco Talos在一份公告中说。“攻击者可以通过提交一个精心制作的 HFS+ 分区文件来利用此漏洞，以便在受影响的设备上由 ClamAV 扫描。”成功利用该弱点可能使对手能够以与 ClamAV 扫描进程相同的权限运行任意代码，或使进程崩溃，从而导致拒绝服务 (DoS) 情况。[点击“阅读原文”查看详情]

## **5、斯堪的纳维亚航空公司**

## **称网络攻击导致乘客数据泄露**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb7hTrJTpdcjwOoHYOYuKbLT3FQGvIRGzXBxSeTehtP2HxqKqU49rN1sbMGbOkzwA8H62FclE6JmcA/640?wx_fmt=png)

## 斯堪的纳维亚航空公司 (SAS) 已发布通知警告乘客，其网站和移动应用程序最近数小时的中断是由同时暴露客户数据的网络攻击造成的。网络攻击导致航空公司的在线系统出现某种形式的故障，导致乘客数据对其他乘客可见。这些数据包括联系方式、之前和即将到来的航班，以及信用卡号的最后四位数字。

该航空公司运营着131架飞机的机队，将乘客送往168个目的地，该公司表示，这种暴露的风险很小，因为泄露的财务信息只是部分信息，不易被利用。此外，它澄清说没有护照详细信息被泄露。[点击“阅读原文”查看详情]

## **6、专家警告RambleOn Android**

## **恶意软件针对韩国记者**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb7hTrJTpdcjwOoHYOYuKbLTj2Do7KEEXibaiaesRq4TSdAhTFK4qlhk9DGLpp41P1qsrnaaGEFJmhtg/640?wx_fmt=png)

作为社会工程活动的一部分，疑似国家背景黑客组织使用带有恶意软件的 Android 应用程序瞄准韩国一记者。

调查结果来自总部位于韩国的非营利组织 Interlab，该组织创造了新的恶意软件RambleOn。Interlab 威胁研究员 Ovi Liber 在本周发布的一份报告中表示，恶意功能包括“从目标受到攻击时开始读取和泄露目标联系人列表、短信、语音通话内容、位置和其他内容的能力” 。该间谍软件伪装成名为 Fizzle ( ch.seme ) 的安全聊天应用程序，但实际上，它充当传递托管在 pCloud 和 Yandex 上的下一阶段有效载荷的管道。[点击“阅读原文”查看详情]

![](https://mmbiz.qpic.cn/mmbiz_gif/Ok4fxxCpBb7QxxODhJSnPyIZe6ZNAgPibByWLDwGu5SWicFr0g9FbXs5Ffdsx3EibAuPaf8njVefjA9B54oHsRqwg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb7QxxODhJSnPyIZe6ZNAgPibsxfq5yL6kPEIaGDzibzV1W1QWNXic8dnx3Ky93Ay7PEpb7lgYGREddkA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

上期回顾

[【安全头条】数千人因汉莎航空 IT 故障而陷入困境](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649783046&idx=2&sn=f0e586dfa86d7ad4bdfd0226e33f5eb6&chksm=88934b69bfe4c27f72fff6211bb2d69c29185666a1d3f746001bd42aae94078140f6262925dd&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ok4fxxCpBb5ZMeq0JBK8AOH3CVMApDrPvnibHjxDDT1mY2ic8ABv6zWUDq0VxcQ128rL7lxiaQrE1oTmjqInO89xA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**戳“阅读原文”查看更多内容**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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