---
title: 7-Zip高危漏洞，攻击者可绕过安全机制远程执行代码
url: https://www.freebuf.com/news/420514.html
source: FreeBuf网络安全行业门户
date: 2025-01-23
fetch_date: 2025-10-06T20:10:25.522844
---

# 7-Zip高危漏洞，攻击者可绕过安全机制远程执行代码

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

7-Zip高危漏洞，攻击者可绕过安全机制远程执行代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

7-Zip高危漏洞，攻击者可绕过安全机制远程执行代码

2025-01-22 10:50:18

所属地 上海

![](https://image.3001.net/images/20250122/1737522487_67907d370a28fd0336c8a.jpg!small)

近日，流行文件压缩软件7-Zip被曝出一个新漏洞，编号为CVE-2025-0411，CVSS评分为7.0，严重程度较高，引发了广泛的安全担忧。

CVE-2025-0411漏洞允许远程攻击者绕过Windows的“网络标记”（Mark-of-the-Web, MOTW）保护机制，在受影响的系统上执行任意代码。

## 7-Zip代码执行漏洞详情

CVE-2025-0411漏洞源于7-Zip在处理带有MOTW标志的恶意压缩包时的不当操作。当用户使用存在漏洞的7-Zip版本解压此类文件时，解压后的文件不会保留MOTW标志。这一疏忽使得攻击者能够绕过防范恶意内容的关键安全检查，在当前用户权限下执行任意代码。

利用此漏洞需要用户交互，例如访问恶意网页或打开恶意文件。在用户频繁处理来自不可信来源文件的环境中，尤为危险。

此前，7-Zip还曾曝出另一个代码执行漏洞，编号为CVE-2024-11477，影响24.07版本。CVE-2024-11477漏洞允许攻击者在用户与恶意压缩包交互时，在当前进程上下文中执行任意代码。

## 受影响版本

CVE-2025-0411漏洞影响24.07及之前的所有7-Zip版本。用户被强烈建议升级到24.09版本，24.09版本修复存在的问题，并确保MOTW标记能够正确传递到解压后的文件中。

* 2024 年10 月1 日：漏洞报告给供应商。
* 2025 年1 月19 日：协调公开披露并发布修复版本。

CVE-2025-0411漏洞对用户构成重大风险，因为它破坏了Windows的一项关键安全功能，这项安全功能主要被用于防止未经适当审查的不可信文件执行。攻击者可能利用此漏洞分发恶意软件或者未经授权访问系统，尤其是在用户具有管理员权限的环境中。

## 缓解措施

* 升级软件：用户应立即升级到7-Zip 24.09或更高版本。
* 谨慎操作：避免打开来自未知或不可信来源的压缩包。
* 启用额外保护：使用能够检测和阻止可疑文件活动的终端安全解决方案。

尽管7-Zip长期以来一直是文件压缩和解压的可信工具，但即使是广泛使用的软件也可能存在漏洞。用户和组织应迅速采取措施，以减轻该漏洞带来的风险。

**参考链接：**

> <https://cybersecuritynews.com/7-zip-vulnerability-arbitrary-code-2/>

# 资讯 # 安全漏洞

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

7-Zip代码执行漏洞详情

受影响版本

缓解措施

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