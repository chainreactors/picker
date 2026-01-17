---
title: Windows远程协助漏洞可绕过安全防护机制
url: https://mp.weixin.qq.com/s/fH2llcfoXD7qtsjXnIUAZg
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:24:26.647951
---

# Windows远程协助漏洞可绕过安全防护机制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9atdmscibKyiaD3eFAGakBMIUI5UeVdoarClTp9GIZFbkHicLydPj9Vvebtg/0?wx_fmt=jpeg)

# Windows远程协助漏洞可绕过安全防护机制

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9at1r0t8mQHnppv6fng6m2U3hpHZgI08gmazq2DWiayv2nY3iaicDCb4bticg/640?wx_fmt=jpeg&from=appmsg)

微软已发布关键安全更新修复（CVE-2026-20824），该漏洞存在于Windows远程协助功能中，会导致保护机制失效，允许攻击者绕过"网络标记"（MOTW）防御系统。

**Part01**

## ****漏洞概括****

该漏洞于2026年1月13日披露，影响从Windows 10到Windows Server 2025的多个Windows平台。（CVE-2026-20824）被评定为"重要"级别的安全功能绕过漏洞。

该缺陷使未经授权的本地攻击者能够规避MOTW防御机制——该系统旨在限制对来自不可信源文件的危险操作。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9atiaC5ruLIOjWEQu7IoqBPdHNrTD8f4bQR9ialjicr2QTyvfCLUrc6lVORQ/640?wx_fmt=png&from=appmsg)

该漏洞CVSS v3.1评分为5.5分，需要本地访问和用户交互才能利用，但会造成严重的机密性风险。漏洞根源在于Windows远程协助对下载内容验证和处理机制存在缺陷。

**Part02**

## ****攻击方式****

攻击者无法直接强制利用该漏洞，必须通过社会工程学手段诱使用户打开特制文件。最常见的攻击载体是电子邮件，攻击者会使用诱人主题分发恶意文件。网络攻击则需要用户手动从被攻陷或攻击者控制的网站下载并打开文件。

**Part03**

## ****受影响系统及补丁****

微软已针对29种不同Windows配置发布安全更新：

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9atibz5We5ZCDsLW6icF1PLgHoANBjgLZvkMQofibxB9icHeCnum8U5iczT1oQ/640?wx_fmt=png&from=appmsg)

具体更新要求：

* Windows 10 22H2版本（32位、ARM64和x64系统）需安装KB5073724
* Windows 11（含最新23H2、24H2和25H2版本）需根据架构安装KB5073455或KB5074109
* 运行Windows Server 2019、2022和2025的企业环境应立即通过相应知识库文章打补丁

**Part04**

## ****修复建议****

由于该漏洞影响多代客户端和服务器操作系统，补丁安装应视为紧急事项。所有更新均标记为"必需"操作级别，表明微软认为修复对组织安全态势至关重要。

目前该漏洞尚未在野利用，补丁发布前也未公开披露。微软评估其利用可能性为"不太可能"，表明存在技术障碍使大规模利用难以实现。但作为保护机制漏洞，成功利用可能部署先前检测到的恶意软件，或规避依赖MOTW指标的终端检测系统。

建议组织在标准更新窗口内优先打补丁，但无需启动紧急事件响应程序。

**参考来源：**

Windows Remote Assistance Vulnerability Allow Attacker to Bypass Security Features

https://cybersecuritynews.com/windows-remote-assistance-vulnerability/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39H4eicalbOEwZ1t8X3mSSZssMSDW4LkuO5g3W31c7ibGVXTlUPk3BqrUoic8Rqt25DJOCygq1FzABicw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651333596&idx=1&sn=a5f1d8decaf400a24f3b9e74a3a357e1&scene=21#wechat_redirect)

###

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icIRaltrZVKxHyDE18c4IRVw3NnALmIwxqOb5mKhbDhBIRRU7MLD2zkbPgnNPvhyk5ibAhhLAavEIA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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