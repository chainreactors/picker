---
title: Windows远程协助保护机制失效可致攻击者绕过Web标记防御系统
url: https://mp.weixin.qq.com/s/HertrVZz6VHBXW5KibvxBQ
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:34:20.957495
---

# Windows远程协助保护机制失效可致攻击者绕过Web标记防御系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo49E74BLfrEBM3Nko9RBqsZmz5oWfibkwbwSgQFwzOkvRZhYu9BbrYS4gCLprsGch8icnKkY5rWuqgQ/0?wx_fmt=jpeg)

# Windows远程协助保护机制失效可致攻击者绕过Web标记防御系统

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo49E74BLfrEBM3Nko9RBqsZ7ehx5YL2dR0XUWnHwjdaib86OW8JxicRCbuDHOpGMpqGy6m1TMukutag/640?wx_fmt=jpeg&from=appmsg)

该漏洞于2026年1月13日披露，影响范围涵盖从Windows 10至Windows Server 2025的多个Windows平台。

CVE-2026-20824属于安全功能绕过漏洞，严重程度评级为"重要"。

此缺陷使未经授权的本地攻击者能够规避MOTW（Mark of the Web）防御系统——该系统是Windows内置的保护机制，旨在限制对从不可信来源下载的文件执行危险操作。

| 属性 | 值 |
| --- | --- |
| CVE编号 | CVE-2026-20824 |
| 漏洞类型 | 安全功能绕过 |
| 分配CNA | Microsoft |
| 弱点分类 | CWE-693：保护机制失效 |
| 最高严重性 | 重要 |
| CVSS向量字符串 | CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N/E:U/RL:O/RC:C |

该漏洞的CVSS v3.1评分为5.5，利用时需要本地访问权限和用户交互，但对机密性构成重大风险。

此弱点源于Windows远程协助在验证和处理下载内容时的保护机制失效。

攻击者无法直接强制利用此漏洞，而是必须通过社会工程学手段诱骗用户打开特制文件。

基于电子邮件的攻击场景是最常见的攻击向量，攻击者通过具有诱惑性的邮件主题分发恶意文件。

基于Web的攻击则要求用户从被攻陷或攻击者控制的网站手动下载并打开文件。

## 受影响系统与补丁

Microsoft已为29种不同的Windows配置发布安全更新。

| 产品系列 | 受影响版本 | KB文章 |
| --- | --- | --- |
| Windows 10 | 版本1607、1809、21H2、22H2 | KB5073722、KB5073723、KB5073724 |
| Windows 11 | 版本23H2、24H2、25H2 | KB5073455、KB5074109 |
| Windows Server 2012 | 2012、2012 R2（所有安装） | KB5073696、KB5073698 |
| Windows Server 2016 | 所有安装 | KB5073722 |
| Windows Server 2019 | 所有安装 | KB5073723 |
| Windows Server 2022 | 所有安装、23H2版 | KB5073457、KB5073450 |
| Windows Server 2025 | 所有安装 | KB5073379 |

* **Windows 10 Version 22H2**用户（包括32位、ARM64和x64系统）应安装KB5073724。
* **Windows 11**部署（包括最新的23H2、24H2和25H2版本）需根据架构安装KB5073455或KB5074109。
* **企业环境**中运行Windows Server 2019、2022和2025的系统必须立即使用相应的知识库文章进行修补。

鉴于该漏洞同时影响客户端和服务器操作系统，且跨越多个版本，修补工作应被视为紧急任务。

所有更新均被标记为"必需"（Required）客户操作，表明Microsoft认为此修补对组织的安全态势至关重要。

目前，该漏洞在野外尚未被利用，且在修补前未被公开披露。

Microsoft的可利用性评估将此漏洞评级为"不太可能被利用"（Exploitation Less Likely），表明存在技术障碍，使得大规模利用的可能性较低。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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