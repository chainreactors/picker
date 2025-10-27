---
title: Apache Tomcat新漏洞允许攻击者执行远程代码
url: https://www.freebuf.com/news/418076.html
source: FreeBuf网络安全行业门户
date: 2024-12-20
fetch_date: 2025-10-06T19:38:34.354475
---

# Apache Tomcat新漏洞允许攻击者执行远程代码

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

Apache Tomcat新漏洞允许攻击者执行远程代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Apache Tomcat新漏洞允许攻击者执行远程代码

2024-12-19 11:12:11

所属地 上海

据Cyber Security News消息，安全研究人员在流行的开源 Web 服务器 Apache Tomcat和servlet 容器中发现了两个严重漏洞，可能允许攻击者执行远程代码并导致拒绝服务。

![](https://image.3001.net/images/20241219/1734577955_67638f231bb575b81f505.jpg!small)

第一个漏洞被追踪为 CVE-2024-50379， 影响 Apache Tomcat  11.0.0-M1 到 11.0.1、10.1.0-M1 到 10.1.33 和 9.0.0.M1 到 9.0.97版本 。如果默认 servlet 在不区分大小写的文件系统上配置了写入权限，攻击者可在并发读取和上传操作期间利用竞争条件。这种绕过 Tomcat 大小写敏感性检查的做法会导致上传的文件被视为 JSP，最终导致远程代码执行。

第二个漏洞被追踪为 CVE-2024-54677，虽然严重性较低，但仍可能构成重大威胁。它影响相同版本的 Apache Tomcat，可使攻击者触发拒绝服务攻击。 该漏洞源于 Tomcat 提供的 Web 应用程序示例，其中许多示例无法限制上传的数据大小，可能会导致 OutOfMemoryError，从而导致拒绝服务。

值得注意的是，默认情况下，示例网络应用程序只能从 localhost 访问，这在一定程度上限制了潜在的攻击面。

目前Apache 已经发布了解决这些安全漏洞的补丁，敦促用户立即升级：

* Apache Tomcat 11.0.2 或更高版本
* Apache Tomcat 10.1.34 或更高版本
* Apache Tomcat 9.0.98 或更高版本

这些漏洞的发现突显了在网络服务器环境中定期进行安全审计和及时打补丁的重要性。由于 Apache Tomcat 在企业环境中的广泛使用，因此这些漏洞的潜在影响十分巨大。

最近，Apache还披露了一个CVSS 4.0 评分高达9.5的高危漏洞，影响Apache Struts 2.0.0 到 2.3.37、2.5.0 到 2.5.33 以及 6.0.0 到 6.3.0.2版本，攻击者可以操纵文件上传参数以启用路径遍历，在某些情况下，这可能导致上传可用于执行远程代码执行的恶意文件 。

**参考来源：**

> [New Apache Tomcat Vulnerabilities Let Attackers Execute Remote Code](https://cybersecuritynews.com/apache-tomcat-rce-vulnerability/)

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