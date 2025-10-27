---
title: 适用于macOS的多个微软应用程序发现库注入漏洞，用户数据安全受威胁
url: https://www.freebuf.com/news/409025.html
source: FreeBuf网络安全行业门户
date: 2024-08-21
fetch_date: 2025-10-06T18:03:49.516274
---

# 适用于macOS的多个微软应用程序发现库注入漏洞，用户数据安全受威胁

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

适用于macOS的多个微软应用程序发现库注入漏洞，用户数据安全受威胁

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

适用于macOS的多个微软应用程序发现库注入漏洞，用户数据安全受威胁

2024-08-20 11:26:04

所属地 上海

根据 Cisco Talos 的最新研究，macOS 上的八个微软应用程序容易受到库注入攻击，有可能让攻击者劫持应用程序的权限并泄露敏感数据。

受影响的微软应用程序包括 Microsoft Teams、Outlook、PowerPoint 和 Word 等流行服务，共有八个 CVE 编号。

* Microsoft Outlook: CVE-2024-42220
* Microsoft Teams (work or school): CVE-2024-42004
* Microsoft PowerPoint: CVE-2024-39804
* Microsoft OneNote: CVE-2024-41159
* Microsoft Excel: CVE-2024-43106
* Microsoft Word: CVE-2024-41165
* Microsoft Teams (work or school) WebView.app helper app: CVE-2024-41145
* Microsoft Teams (work or school) com.microsoft.teams2.modulehost.app: CVE-2024-41138

攻击者通过使用现有的应用程序权限而不提示用户进行任何额外验证来绕过 macOS 的权限模型，这样，就可以在用户未察觉的情况下从用户账户发送电子邮件、录制音频片段、拍照或录制视频，而无需与用户进行任何交互。

## macOS 的许可模式受到审查

Cisco Talos 强调了 macOS 基于用户同意的权限模型，该模型包含旨在保护用户隐私和维护系统安全的功能。但研究发现，macOS 对应用程序的权限管理过于信任，允许它们自我监管，这一缺陷可能使攻击者得以利用应用程序的高级权限。

![](https://image.3001.net/images/20240820/1724126539_66c4154b5ee348d33feb0.png!small)更令人担忧的是，八款流行的微软  macOS 应用程序都激活了禁用库验证的权限“com.apple.security.cs.disable-library-validation ”。

据苹果公司称，该权限允许加载由第三方开发者签名的插件，旨在增强应用程序的功能性。但这一机制存在安全隐患，攻击者可能利用这一点注入任意库，并在被攻击的应用程序中运行恶意代码，进而完全控制应用程序的权限和功能。

研究人员还观察到，macOS 上的所有 Microsoft Office 应用程序都允许加载未签名的动态库。如果要修改已经执行过一次的应用程序，需要特定的权限。不过，攻击者可以通过将应用程序复制到如 /tmp 等其他文件夹来绕过这一安全措施，但这也增加了数据泄露和系统被攻击的风险。

研究人员指出，由于存在相对导入和禁用库验证的权限，所有 Microsoft Office 应用程序都容易受到库注入攻击。

## 微软用户面临不必要的风险

Cisco Talos 的研究人员说，他们的发现让人们对禁用库验证的必要性产生了疑问，尤其是应用程序不打算加载其他库的情况下。微软通过使用特定权限绕开了 macOS 的加固安全措施，这可能使用户面临原本不必要的风险。

在 Cisco Talos 报告漏洞后，微软虽然认为发现的问题风险较低，但已经对其中的四款应用程序进行了更新，移除了 com.apple.security.cs.disable-library-validation 权限，这意味着它们不再容易受到已知库注入攻击的威胁。

这四款应用程序是 Microsoft Teams 的主应用程序、WebView 应用程序和 ModuleHost 应用程序，以及 Microsoft OneNote。不过，截至 2024 年 8 月 19 日，Microsoft Excel、Outlook、PowerPoint 和 Word 仍然存在漏洞。

![](https://image.3001.net/images/20240820/1724126449_66c414f1ce0a7b9223aa8.png!small)

检查 macOS 应用程序是否易受库注入攻击影响的流程图  来源：Cisco Talos

研究人员建议，macOS 可以引入用户提示来降低这一风险。这将允许用户决定是否加载特定的第三方插件，从而提供一种更可控的访问授权方式。

参考来源：<https://www.infosecurity-magazine.com/news/microsoft-apps-macos-exposed/>

# Microsoft # macOS # macOS系统 # 系统权限

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

macOS 的许可模式受到审查

微软用户面临不必要的风险

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)