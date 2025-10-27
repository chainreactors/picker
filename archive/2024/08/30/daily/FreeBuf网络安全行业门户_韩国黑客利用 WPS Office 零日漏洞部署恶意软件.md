---
title: 韩国黑客利用 WPS Office 零日漏洞部署恶意软件
url: https://www.freebuf.com/news/409715.html
source: FreeBuf网络安全行业门户
date: 2024-08-30
fetch_date: 2025-10-06T18:04:56.263180
---

# 韩国黑客利用 WPS Office 零日漏洞部署恶意软件

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

韩国黑客利用 WPS Office 零日漏洞部署恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

韩国黑客利用 WPS Office 零日漏洞部署恶意软件

2024-08-29 10:59:51

所属地 上海

据BleepingComputer消息，与韩国有关的网络黑客组织 APT-C-60近期一直在利用 Windows 版 WPS Office 中的零日漏洞，针对东亚地区目标部署 SpyGlace 后门。![](https://image.3001.net/images/20240829/1724910411_66d00b4bc5d9e11db7b35.png!small)

这个被跟踪为 CVE-2024-7262 的零日漏洞至少自 2024 年 2 月下旬以来就被用于野外攻击，影响了WPS 12.2.0.13110至12.1.0.16412之间的版本。今年3月，金山软件已经修补了该漏洞。

CVE-2024-7262 存在于软件处理自定义协议处理程序的方式中，特别是 "ksoqing://"，允许通过文档中特制的 URL 执行外部应用程序。 由于对这些 URL 的验证和消毒不当，该漏洞允许攻击者制作恶意超链接，从而导致任意代码执行。

APT-C-60 通过创建MHTML 文件，在其中嵌入了隐藏在诱饵图像下的恶意超链接，诱使受害者点击并触发漏洞。

恶意URL 参数包括一个 base64 编码命令，用于执行一个特定插件 (promecefpluginhost.exe)，该插件会尝试加载包含攻击者代码的恶意 DLL (ksojscore.dll)，该 DLL 作为 APT-C-60 的下载器组件，用于从攻击者的服务器（一个名为 "SpyGlace "的自定义后门）获取最终有效载荷 (TaskControler.dll)。

![](https://image.3001.net/images/20240829/1724910250_66d00aaae188f34697efd.png!small)APT-C-60攻击概述

此外，研究人员还发现了另外一个任意代码执行漏洞 CVE-2024-7263，该漏洞出现于针对 CVE-2024-7262的补丁缺陷当中。具体来说，金山软件虽然增加了对特定参数的验证，但一些参数（如 "CefPluginPathU8"）仍未得到充分保护，从而允许攻击者再次通过promecefpluginhost.exe指向恶意DLL的路径。目前该漏洞也于今年5月得到了修补。

由于这两个漏洞利用具有较高的欺骗性，能诱使任何用户点击看起来合法的电子表格，安全专家建议WPS用户尽快升级至12.2.0.17119以上或最新版本。

**参考来源：**

> [South Korean hackers exploited WPS Office zero-day to deploy malware](https://www.bleepingcomputer.com/news/security/apt-c-60-hackers-exploited-wps-office-zero-day-to-deploy-spyglace-malware/)

# 黑客

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