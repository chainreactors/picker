---
title: Bootkitty：首个针对Linux的UEFI引导程序恶意软件
url: https://www.freebuf.com/news/416423.html
source: FreeBuf网络安全行业门户
date: 2024-11-29
fetch_date: 2025-10-06T19:17:21.055902
---

# Bootkitty：首个针对Linux的UEFI引导程序恶意软件

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

Bootkitty：首个针对Linux的UEFI引导程序恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Bootkitty：首个针对Linux的UEFI引导程序恶意软件

2024-11-28 15:09:35

所属地 上海

研究人员发现了首个专门针对Linux系统UEFI引导程序恶意软件，这标志着以前专注于Windows的隐蔽且难以清除的引导程序威胁发生了转变。

这款名为“Bootkitty”的Linux恶意软件是一个概念验证，仅在某些Ubuntu版本和配置上有效，而不是实际攻击中部署的完全成熟的威胁。引导程序恶意软件旨在感染计算机的启动过程，在操作系统加载之前运行，从而允许其在非常低的级别上控制系统。

这种做法的优势在于，引导程序可以规避在操作系统级别运行的安全工具，并修改系统组件或注入恶意代码而不被检测到。发现Bootkitty的ESET研究人员警告说，尽管目前对现实世界的影响有限，但它的存在是UEFI引导程序威胁领域的一个重要演变。

![](https://image.3001.net/images/20241128/1732777757_6748171d2d92245975ed3.png!small)ESET在2024年11月检查VirusTotal上传的一个可疑文件（bootkit.efi）后发现了Bootkitty。经过分析，ESET确认这是第一个绕过内核签名验证并在系统启动过程中预加载恶意组件的Linux UEFI引导程序案例。

Bootkitty依赖于自签名证书，因此它不会在启用安全启动的系统上执行，只针对某些Ubuntu发行版。此外，硬编码的偏移量和简化的字节模式匹配使其仅适用于特定的GRUB和内核版本，因此不适合广泛部署。

ESET还指出，恶意软件包含许多未使用的功能，并且处理内核版本兼容性不佳，常常导致系统崩溃。

![](https://image.3001.net/images/20241128/1732777680_674816d08792f158a5691.png!small)引导程序中包含的ASCII，来源：ESET

恶意软件的缺陷性质以及ESET的遥测数据显示Live系统上没有Bootkitty的迹象，使研究人员得出结论，它处于早期开发阶段。

## Bootkitty的能力

在启动过程中，Bootkitty挂钩UEFI安全认证协议（EFI\_SECURITY2\_ARCH\_PROTOCOL和EFI\_SECURITY\_ARCH\_PROTOCOL），以绕过安全启动的完整性验证检查，确保引导程序加载，无论安全策略如何。

接下来，它挂钩各种GRUB函数，如'start\_image'和'grub\_verifiers\_open'，以操纵引导加载程序对二进制文件的完整性检查，包括Linux内核，关闭签名验证。

然后，Bootkitty截获Linux内核的解压缩过程，并挂钩'module\_sig\_check'函数。这迫使它在内核模块检查期间始终返回成功，允许恶意软件加载恶意模块。

此外，它将第一个环境变量替换为'LD\_PRELOAD=/opt/injector.so'，以便在系统启动时将恶意库注入进程。

![](https://image.3001.net/images/20241128/1732777921_674817c152ef53d3be403.png!small)Bootkitty执行流程的一部分，来源：ESET

整个过程留下了几个工件，有些是有意的，有些则不是，ESET解释说，这也是Bootkitty缺乏精细化的另一个佐证。研究人员还指出，上传Bootkitty到VT的同一用户还上传了一个名为'BCDropper'的未签名内核模块，但现有证据只能弱弱地将两者联系起来。

BCDropper会释放一个名为'BCObserver'的ELF文件，这是一个具有rootkit功能的内核模块，在受感染的系统上隐藏文件、进程并打开端口。这种类型恶意软件的发现说明了攻击者是如何开发之前仅限于Windows的Linux恶意软件的，因为企业越来越多地采用Linux。

与Bootkitty相关的入侵指标（IoCs）已在此GitHub存储库中共享。

参考来源：<https://www.bleepingcomputer.com/news/security/researchers-discover-bootkitty-first-uefi-bootkit-malware-for-linux/>

# 恶意软件

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

Bootkitty的能力

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