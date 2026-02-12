---
title: 微信 Linux版本命令执行漏洞
url: https://mp.weixin.qq.com/s/90kehAH0b7H1if9CHTVQ9Q
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:18:43.371913
---

# 微信 Linux版本命令执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HqolA1dQic6iboXqqRNibaDh7kh165Nnt7XMMibChT1SibvYADicr8rt4dftYfUEv8Ribf1T5wUb608GaAT4UAL1Mwd5VS8vogcpUPr0pNibk2bzzq0/0?wx_fmt=jpeg)

# 微信 Linux版本命令执行漏洞

奇安信 CERT
奇安信 CERT

HACK之道

![]()

在小说阅读器中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | 微信 Linux版本命令执行漏洞 | | |
| **漏洞编号** | QVD-2026-7687 | | |
| ****公开时间**** | 2026-02-10 | ****影响量级**** | 千万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **8.0** |
| **威胁类型** | 命令执行 | **利用可能性** | ****高**** |
| **POC状态** | **已公开** | **在野利用状态** | 未发现 |
| **EXP状态** | **未公开** | **技术细节状态** | **已公开** |
| **危害描述：**攻击者可诱导用户打开恶意文件名的文件从而导致命令执行，获取系统权限。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

微信 Linux版一款跨平台的通讯工具。支持单人、多人参与。通过手机网络发送语音、图片、视频和文字。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到微信 Linux版本命令执行漏洞(QVD-2026-7687)，该漏洞源于微信 Linux版文件名校验不严格，攻击者可诱导用户打开恶意文件名的文件从而导致命令执行，获取系统权限。目前该漏洞PoC已公开。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**>****>****>****>**

**利用条件**

用户点击恶意文件。

**02**

**影响范围**

**>****>****>****>**

**影响版本**

微信 Linux版本 <= 4.1.0.13

**>****>****>****>**

**其他受影响组件**

无

**03**

**复现情况**

目前，奇安信威胁情报中心安全研究员已成功复现微信 Linux版本命令执行漏洞(QVD-2026-7687)，截图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555v7ViblMVZXApnIa3V0SKuBKiaWW7SLAs6YHmPmmRYn6DlvTV9RunXz4fcPTT8v4j3gkknPicCGFBNZtuQjha7oXA2OPia0ibjCCY0s/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=0)

**04**

**处置建议**

**>****>****>****>**

**安全更新**

官方已发布安全补丁，请及时更新至最新版本：

微信 Linux版本 >= 4.1.0.16

下载地址：

https://linux.weixin.qq.com/

**05**

**参考资料**

[1]https://linux.weixin.qq.com/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

HACK之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

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