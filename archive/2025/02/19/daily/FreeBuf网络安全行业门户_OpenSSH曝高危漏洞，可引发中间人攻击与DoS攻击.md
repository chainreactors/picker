---
title: OpenSSH曝高危漏洞，可引发中间人攻击与DoS攻击
url: https://www.freebuf.com/vuls/422180.html
source: FreeBuf网络安全行业门户
date: 2025-02-19
fetch_date: 2025-10-06T20:40:00.640875
---

# OpenSSH曝高危漏洞，可引发中间人攻击与DoS攻击

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

OpenSSH曝高危漏洞，可引发中间人攻击与DoS攻击

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

OpenSSH曝高危漏洞，可引发中间人攻击与DoS攻击

2025-02-18 22:59:04

所属地 上海

![DDoS攻击](https://image.3001.net/images/20250219/1739926887142682_a244dd2ef7554f33a1776f99ce1d2c1e.jpg!small)
图片来源：SynthEx / Shutterstock

OpenSSH是远程管理Linux和BSD系统的最常用工具，近期修复了两个高危漏洞。其中一个漏洞允许攻击者在特定配置下对OpenSSH客户端发起中间人攻击，冒充服务器以拦截敏感通信；另一个漏洞则可能导致CPU资源耗尽。

## 漏洞详情及潜在危害

研究人员在报告中指出：“SSH会话是攻击者拦截凭证或劫持会话的主要目标。一旦被攻破，黑客可以查看或操纵敏感数据，横向跨越多个关键服务器，并窃取诸如数据库凭证等重要信息。此类泄露可能导致声誉受损、违反合规要求（如GDPR、HIPAA、PCI-DSS），并通过迫使系统停机以遏制威胁，从而破坏关键业务。”

此次发现的中间人漏洞编号为CVE-2025-26465，其代码缺陷可追溯至2014年12月，距今已有10年之久。该漏洞影响了从6.8p1到9.9p1的所有OpenSSH版本。第二个漏洞编号为CVE-2025-26466，影响了9.5p1到9.9p1版本。用户应尽快升级至新发布的OpenSSH 9.9p2版本。

## DNS密钥验证机制的失效

OpenSSH是SSH（安全外壳协议）最流行的实现，由维护OpenBSD操作系统的OpenBSD项目开发。OpenBSD以其代码质量和安全性著称，OpenSSH也不例外。

SSH协议的工作方式是在交换凭证之前先建立加密连接。客户端通过查看服务器的公钥来验证其身份，类似于TLS协议。如果密钥已被信任，握手将继续；如果密钥指纹与客户端known\_hosts文件中存储的不一致，客户端会发出中间人攻击的警告。

known\_hosts文件中的服务器身份是如何填充的？通常，当客户端首次连接服务器时，系统会提示用户是否接受并信任服务器提供的密钥，从而在本地创建记录。然而，并非所有SSH用户都是人类，SSH还通过自动化脚本进行大量机器与机器之间的交互。

为了支持这些自动化脚本信任新配置的服务器，OpenSSH提供了一个名为VerifyHostKeyDNS的功能，允许客户端通过检查服务器密钥是否与其主机名的SSHFP DNS记录匹配来自动信任该密钥。

### 漏洞成因与利用场景

VerifyHostKeyDNS功能在大多数部署中默认关闭，但用户可以在配置中启用它。2013年9月至2023年3月期间，FreeBSD附带的OpenSSH包默认启用了该选项。

Qualys研究人员发现，当VerifyHostKeyDNS启用并设置为“ask”或“yes”时，检查服务器密钥的函数存在逻辑错误：除-1（SSH\_ERR\_INTERNAL\_ERROR）之外的任何错误值都不会被视为错误，反而被认为是成功的。通过尝试不同的错误代码，他们发现只有-2（SSH\_ERR\_ALLOC\_FAIL，内存不足错误）可以被利用。

### 配合漏洞实现攻击

在真实场景中，如何触发客户端的内存错误？一种方法是在伪造的服务器上放置一个超长的密钥，但由于握手期间交换的数据包最大约为256KB，这不足以耗尽客户端内存。因此，研究人员需要另一个漏洞，在身份验证之前触发，并尽可能消耗客户端进程的内存，以便在提供伪造服务器密钥时触发内存不足错误。

最终，研究人员发现了第二个漏洞CVE-2025-26466，该漏洞在初始密钥交换期间会导致内存的无限分配，直到交换结束才释放。虽然该漏洞可能导致客户端和服务器的拒绝服务，但在客户端上，它还可用于为利用第一个漏洞创造条件，从而实现中间人攻击。

研究人员在概念验证场景中解释道：“如果伪造的服务器实施上述内存耗尽攻击（通过分配1024位RSA密钥、约140KB的证书扩展以及约234MB的PONG数据包），则客户端调用sshkey\_from\_private()时返回SSH\_ERR\_ALLOC\_FAIL，从而完全绕过对真实服务器主机密钥的检查，使得伪造的服务器能够成功冒充真实服务器。”

**参考来源：**

> [OpenSSH fixes flaws that enable man-in-the-middle, DoS attacks](https://www.csoonline.com/article/3827268/openssh-fixes-two-flaws-that-enable-a-man-in-the-middle-attack-and-denial-of-service.html)

# 网络安全 # 终端安全

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

漏洞详情及潜在危害

DNS密钥验证机制的失效

* 漏洞成因与利用场景
* 配合漏洞实现攻击

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