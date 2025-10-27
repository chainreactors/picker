---
title: 利用Windows漏洞，攻击者能降级系统组件恢复漏洞
url: https://www.freebuf.com/news/413826.html
source: FreeBuf网络安全行业门户
date: 2024-10-29
fetch_date: 2025-10-06T18:50:13.056608
---

# 利用Windows漏洞，攻击者能降级系统组件恢复漏洞

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

利用Windows漏洞，攻击者能降级系统组件恢复漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

利用Windows漏洞，攻击者能降级系统组件恢复漏洞

2024-10-28 11:11:02

所属地 上海

据Hackread消息，在最近的一项研究中，SafeBreach Labs 研究员揭露了一种新的攻击技术，能够操纵Windows 11系统在更新时降级关键系统组件，从而让一些漏洞修复补丁失效。

![](https://image.3001.net/images/20241028/1730085410_671f02224bf7ff2a064e8.png!small)

该攻击原理最初于2024 年 8 月在Black Hat USA 2024上披露，而现在研究人员公布了更多细节，以加强公众对这次攻击的了解。

这种被称为 Windows Downdate 的技术利用的其中一个漏洞是“ItsNotASecurityBoundary”驱动程序签名强制 （DSE） 绕过，能允许攻击者加载未签名的内核驱动程序，将经过验证的安全目录替换为恶意版本，从而能够加载未签名的内核驱动程序。

比如，攻击者可以针对特定组件，例如解析安全目录所必需的“ci.dll”模块，并将它们降级到易受攻击的状态，从而能够利用此绕过并获得内核级权限。

"ItsNotASecurityBoundary "DSE 绕过是一类名为 "虚假文件不变性"（FFI）的新漏洞的一部分，利用了关于文件不可变性的错误假设 ，允许通过清除系统工作集来修改 "不可变 "文件。

研究人员概述了在具有不同级别虚拟化安全（VBS）保护的 Windows 系统中可利用漏洞的步骤，发现了多种禁用 VBS 关键功能的方法，包括凭证防护和受管理程序保护的代码完整性（HVCI）等功能，甚至首次使用了 UEFI 锁。

要利用没有 UEFI 锁的系统，攻击者必须通过修改注册表设置来禁用 VBS。一旦禁用，就可以将 ci.dll 模块降级到易受攻击的版本，并利用“ItsNotASecurityBoundary”漏洞。对带有 UEFI 锁和 "强制（Mandatory ）"标志的 VBS 是最安全的配置，即使锁被绕过，VBS 也不会被禁用。 研究人员解释说，目前还没有已知的方法可以在没有物理访问的情况下利用具有这种保护级别的系统。

总体而言，这种 Windows 更新接管功能允许攻击者加载未签名的内核驱动程序、启用自定义 rootkit 以解除安全控制、隐藏进程并保持隐蔽性，从而对企业构成了重大威胁。攻击者可以对关键操作系统组件（包括 DLL、驱动程序甚至 NT 内核）进行自定义降级。 通过对这些组件进行降级，攻击者可以暴露以前修补过的漏洞，使系统容易被利用。

为降低风险，企业应及时更新系统，打上最新的安全补丁，以解决漏洞问题，同时部署有效的端点检测和响应（EDR）解决方案，以检测和响应恶意活动，防止未经授权的访问和数据泄露。 此外，使用 UEFI 锁定和 "强制 "标志启用 VBS 还能提供额外的保护。

参考来源：

> [New Attack Lets Hackers Downgrade Windows to Exploit Patched Flaws](https://hackread.com/hackers-downgrade-windows-exploit-patched-flaws/)

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