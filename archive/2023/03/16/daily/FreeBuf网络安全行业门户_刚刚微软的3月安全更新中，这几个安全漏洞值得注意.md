---
title: 刚刚微软的3月安全更新中，这几个安全漏洞值得注意
url: https://www.freebuf.com/news/360485.html
source: FreeBuf网络安全行业门户
date: 2023-03-16
fetch_date: 2025-10-04T09:44:55.735099
---

# 刚刚微软的3月安全更新中，这几个安全漏洞值得注意

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

刚刚微软的3月安全更新中，这几个安全漏洞值得注意

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

刚刚微软的3月安全更新中，这几个安全漏洞值得注意

2023-03-15 11:28:43

所属地 上海

![](https://image.3001.net/images/20230315/1678850764_64113acc399e4a0c17cb2.png!small)

近日，安全专家建议IT团队应优先修补两个零日漏洞，一个是微软Outlook的认证机制，另一个是web标记的绕过。这两个漏洞是微软在其3月补丁星期二安全更新中披露的74个安全漏洞的一部分。

在一篇博文中，Automox的研究人员建议企业在24小时内修补这两个漏洞，因为攻击者正在野外利用它们。此外，3月更新中的几个关键漏洞能够实现远程代码执行（RCE），因此它们也是需要高度优先修补的。

## 特权升级零日

其中一个零日是微软Outlook中的一个关键的权限升级漏洞，被追踪为CVE-2023-23397，它允许攻击者访问受害者的Net-NTLMv2挑战-回应认证哈希，然后冒充用户。

该漏洞的危险之处在于，攻击者只需发送一封特制的电子邮件，在用户在预览窗口中查看该邮件之前，Outlook就会检索并处理该邮件。

Tenable公司的高级研究工程师评论说：这是因为该漏洞是在电子邮件服务器端触发的，这意味着在受害者查看恶意邮件之前就会被利用。攻击者可以使用受害者的Net-NLMv2哈希值进行攻击，利用NTLM挑战-响应机制，让对手以用户身份进行认证。

ZDI研究员在博文中补充说，这使得该漏洞更像是一个认证绕过漏洞，而不是一个权限升级问题。而且，禁用预览窗口选项并不能减轻威胁，因为该漏洞甚至在这之前就已经被触发了。

## 安全绕过零日

微软将第二个零日漏洞确定为CVE-2023-248，这是一个Windows SmartScreen安全功能绕过问题，攻击者可以利用它绕过微软用来识别用户可能从互联网上下载的文件的Mark of the Web指定。

CVE-2023-248 影响到所有运行Windows 10及以上版本的桌面系统和运行Windows Server 2016、2019和2022的系统。

Goettl在一份声明中说：CVSSv3.1的得分虽然只有5.4，这可能不会引起太多企业的注意。确实，就其本身而言，CVE可能没有那么大的威胁，但它很可能被用在一个有其他漏洞的攻击链中。

## 其他安全漏洞

需要特别注意的一个RCE漏洞是CVE-2023-23415，它存在于网络设备用来诊断通信问题的互联网控制消息协议（ICMP）中。

微软表示：攻击者可以通过使用一个低级别的协议错误来远程利用这个漏洞，该错误在其标题中包含一个碎片化的IP数据包，被发送到目标机器上。该漏洞影响到多个微软产品，包括Windows 10、Windows 11、Windows Server 2008、2012、2016、2019和2022。

Automox还建议企业在72小时内解决CVE-2023-23416，即Windows加密服务协议中的一个RCE漏洞。这是因为，除其他外，它影响到所有版本的台式机Windows 10及以上，以及从Server 2012开始的所有Windows服务器版本。

除了新漏洞的补丁，微软还在3月的补丁周期中发布了四个之前漏洞的更新，全部来自2022年。Ivanti说，这次更新扩大了受漏洞影响的微软软件和应用程序的数量，并为它们提供了补丁。该安全厂商将这四个更新补丁列为CVE-2022-43552，CVE-2022-23257，CVE-2022-23825，以及CVE-2022-23816。

> 参考链接：www.darkreading.com/vulnerabilities-threats/microsoft-zero-day-bugs-security-feature-bypass

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

特权升级零日

安全绕过零日

其他安全漏洞

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