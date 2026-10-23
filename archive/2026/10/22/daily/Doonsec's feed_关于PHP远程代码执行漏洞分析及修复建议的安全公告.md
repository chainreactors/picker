---
title: 关于PHP远程代码执行漏洞分析及修复建议的安全公告
url: https://mp.weixin.qq.com/s/0pz73RAqoliAPYhM6MASbg
source: Doonsec's feed
date: 2026-10-22
fetch_date: 2026-10-23T06:44:47.729877
---

# 关于PHP远程代码执行漏洞分析及修复建议的安全公告

# 关于PHP远程代码执行漏洞分析及修复建议的安全公告

国家互联网应急中心CNCERT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于CNVD漏洞平台
，作者CNVD

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM4Feicia15peMqhiakNKwwYia1jf7VRCsgbvzMKK6yMty7jEg/0)

**CNVD漏洞平台**
.

国家信息安全漏洞共享平台（China National Vulnerability Database）是由国家计算机网络应急技术处理协调中心联合重要信息系统单位、基础电信运营商、网络安全厂商、软件厂商和互联网企业建立的国家网络安全漏洞库。

2026年10月21日，国家信息安全漏洞共享平台（CNVD）收录了PHP远程代码执行漏洞（CNVD-2026-41674、CNVD-2026-41675，对应CVE-2026-109618、CVE-2026-109619）。未经身份验证的远程攻击者可构造恶意HTTP请求触发内存错误，在特定条件下实现对目标服务器的拒绝服务攻击、敏感数据窃取、远程代码执行。目前，漏洞技术细节与PoC已广泛传播，CNVD建议受影响用户立即升级至最新版本。

**一、漏洞情况分析**

PHP是一种广泛使用的开源通用脚本语言，适用于Web开发并可嵌入HTML中。PHP解释器内核为全球多数Web应用运行提供了基础运行时环境，包括WordPress、Drupal、Joomla、Laravel等主流框架和内容管理系统。

2026年10月21日，国家信息安全漏洞共享平台收录了PHP远程代码执行漏洞。PHP解释器内核在内存管理环节存在逻辑处理缺陷，攻击者可构造特定HTTP请求触发程序异常处理流程，导致内部数据状态异常或已释放内存被再次访问，引发内存破坏。未经身份验证的远程攻击者，可构造恶意HTTP请求触发内存错误，并在特定条件下实现对目标服务器的拒绝服务攻击、敏感数据窃取、远程代码执行。

CNVD对该漏洞的综合评级为“高危”。

**二、****漏洞影响范围**

目前，已知受漏洞影响的PHP产品版本包括：

1、8.2.35版本之前的8.2.x版本；

2、8.3.36版本之前的8.3.x版本；

3、8.4.27版本之前的8.4.x版本；

4、8.5.12版本之前的8.5.x版本。

厂商发布的修复版本为PHP8.5.12、8.4.27、8.3.36、8.2.35。

此外，该漏洞还影响Magento、WordPress、Drupal、Joomla、MediaWiki、Roundcube、phpMyAdmin、Nextcloud、Laravel、Symfony、WHMCS、OpenCart等基于PHP环境的主流CMS和框架。

**三、漏洞处置建议**

1、排查建议。互联网用户可通过以下方式查看PHP使用版本，在此基础上对照影响范围判断是否受此漏洞影响：

1）使用php -v命令查询；

2）CLI和Web服务器可能运行不同的PHP版本，需使用php-fpm -v或php-fpm8.3 -v命令查询网站提供版本。

2、**修复建议**。目前，PHP安全团队已修复漏洞并发布安全公告，受影响用户应密切关注官方信息，通过官方渠道下载并更新至最新版本（https://www.php.net/archive/2026.php#2026-10-21-5）。

3、**缓解建议**。暂无法更新的用户可采取以下措施减少部分攻击路径，缓解漏洞威胁：

1）PHP-FPM可设置memory\_limit=-1移除可预测的单次请求内存限制；mod\_php可关闭会话上传进度功能与fatal backtrace：全局设置session.upload\_progress.enabled=0（PHP 8.5可设置fatal\_error\_backtraces=0），并重启全部工作进程或Web服务器。

2）阻断跨请求状态传递，此方式会降低服务性能。FPM池pm.max\_requests=1，mod\_php对应Apache的MaxRequestsPerChild=1。

3）通过WAF等安全设备拦截异常multipart/form-data的HTTP请求。

4）持续监测PHP进程异常退出、系统异常命令调用、陌生进程创建、异常文件写入等行为，留存日志用于溯源分析。

4、**防护建议**。信息系统运营单位应进一步加强安全防护。全面梳理本单位网络资产，按照非必要不上网原则，缩小信息系统的公网暴露面；暂不具备修复条件的运营单位应采取网络隔离、网络访问限制、非必要业务系统下线等临时性应对措施。

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz65uZccENTFwtVytvibEnzNbibwZw0F5MItQaglR2pQNzcw4dYE1FfLGuMhRztcV49nmwkkexPBKZPibQ/0?wx_fmt=png)

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