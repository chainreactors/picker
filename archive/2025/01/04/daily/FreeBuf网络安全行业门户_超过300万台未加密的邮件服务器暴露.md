---
title: 超过300万台未加密的邮件服务器暴露
url: https://www.freebuf.com/news/418975.html
source: FreeBuf网络安全行业门户
date: 2025-01-04
fetch_date: 2025-10-06T20:10:21.123397
---

# 超过300万台未加密的邮件服务器暴露

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

超过300万台未加密的邮件服务器暴露

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

超过300万台未加密的邮件服务器暴露

2025-01-03 10:22:53

所属地 上海

目前，超过300万台未启用TLS加密的POP3和IMAP邮件服务器暴露在互联网上，容易受到网络嗅探攻击。

IMAP和POP3是访问邮件服务器上邮件的两种方式。IMAP适用于从多个设备（如手机和笔记本电脑）查看邮件，因为它会将邮件保留在服务器上并在设备间同步。而POP3则会将邮件从服务器下载，使其仅能从下载的设备访问。

![](https://image.3001.net/images/20250103/1735870953_677749e93f59b5e5fcfa5.png!small)

TLS安全通信协议有助于在通过客户端/服务器应用程序在互联网上交换和访问邮件时保护用户信息。然而，如果未启用TLS加密，用户的消息内容和凭证将以明文形式发送，容易受到窃听的网络嗅探攻击。

根据ShadowServer安全威胁监控平台的扫描结果显示，约有330万台主机运行未启用TLS加密的POP3/IMAP服务，并在通过互联网传输时以明文形式暴露用户名和密码。

目前，ShadowServer正在通知邮件服务器运营商，他们的POP3/IMAP服务器未启用TLS，导致用户的未加密用户名和密码暴露于嗅探攻击。

![](https://image.3001.net/images/20250103/1735870968_677749f8c0ae318f11c64.png!small)

未启用TLS的IMAP和POP3邮件服务器（Shadowserver）

“这意味着用于邮件访问的密码可能被网络嗅探器拦截。此外，服务暴露可能使服务器遭受密码猜测攻击，”Shadowserver表示。“如果您收到我们的报告，请为IMAP启用TLS支持，并考虑是否需要启用该服务或将其移至VPN后面。”

TLS 1.0规范及其后续版本TLS 1.1已使用了近二十年。TLS 1.0于1999年推出，TLS 1.1于2006年推出。经过广泛讨论和28个协议草案的开发，互联网工程任务组（IETF）于2018年3月批准了TLS 1.3，这是TLS协议的下一个主要版本。

2018年10月，微软、谷歌、苹果和Mozilla在协调公告中表示，将在2020年上半年淘汰不安全的TLS 1.0和TLS 1.1协议。微软从2020年8月开始在最新的Windows 10 Insider版本中默认启用TLS 1.3。

2021年1月，美国国家安全局（NSA）还提供了关于识别和替换过时的TLS协议版本和配置的指导，建议采用现代、安全的替代方案。

“过时的配置使对手能够使用各种技术访问敏感操作流量，例如通过中间人攻击被动解密和修改流量，”NSA表示。

“攻击者可以利用过时的传输层安全（TLS）协议配置，以非常低的技能要求访问敏感数据。”

参考来源：<https://www.bleepingcomputer.com/news/security/over-3-million-mail-servers-without-encryption-exposed-to-sniffing-attacks/>

# 系统安全 # 邮件安全

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