---
title: 知名打印管理软件存漏洞，能绕过所有安全检测
url: https://www.freebuf.com/news/365552.html
source: FreeBuf网络安全行业门户
date: 2023-05-06
fetch_date: 2025-10-04T11:40:41.889412
---

# 知名打印管理软件存漏洞，能绕过所有安全检测

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

知名打印管理软件存漏洞，能绕过所有安全检测

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

知名打印管理软件存漏洞，能绕过所有安全检测

2023-05-05 13:46:44

所属地 上海

据Security affairs 5月4日消息，VulnCheck 研究人员最近利用打印管理软件 PaperCut 服务器中的一个严重漏洞，设计了一种新的利用方法，可以绕过所有当前安全检测。

![](https://image.3001.net/images/20230505/1683265732_645498c4f29dcf85d1d74.png!small)

PaperCut为佳能、爱普生、施乐和几乎所有其他主要打印机品牌生产打印管理软件，其产品被7万多个组织使用，包括世界各地的政府机构、大学和大公司。此次利用的漏洞被追踪为 CVE-2023-27350，CVSS评分高达9.8，是 PaperCut MF/NG 不当访问控制漏洞。PaperCut MF/NG 在 SetupCompleted 类中包含一个不正确的访问控制漏洞，允许绕过身份验证并在 SYSTEM 上下文中执行代码。

VulnCheck研究人员公开了两个漏洞利用变体：

1.使用 PaperCut 打印脚本接口执行 Windows 命令的漏洞（Horizo​​n3.ai 漏洞的变体）；

2.利用打印脚本接口投放恶意 JAR。

这两种方法都滥用了系统内置的 JavaScript 接口。JavaScript 引擎是 Rhino，允许该用户执行任意 Java。PaperCut Software 实施了配置选项来降低这种任意代码执行向量的风险，但由于攻击者拥有完全的管理访问权限，这些保护措施很容易被禁用。

VulnCheck 设计的 PoC 漏洞利用将 auth 程序设置为 Linux 上的“/usr/sbin/python3”和 Windows 上的“C:\Windows\System32\ftp.exe”，攻击者可以通过在登录尝试期间提供恶意用户名和密码，在易受攻击的服务器上执行任意代码。

4 月 19 日，PaperCut 确认了该漏洞，该公司收到了网络安全公司趋势科技两份关于 PaperCut MF/NG 严重安全漏洞报的告。 趋势科技计划在 2023 年 5 月 10 日披露有关该漏洞的更多信息。

好在PaperCut通过发布 PaperCut MF 和 PaperCut NG 20.1.7、21.2.11 和 22.0.9 及更高系统版本解决了漏洞问题，强烈建议用户升级到其中一个包含修复程序的版本。

> 参考来源：[Experts devised a new exploit for the PaperCut flaw that can bypass all current detection](https://securityaffairs.com/145752/hacking/papercut-new-exploit.html)

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