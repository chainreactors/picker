---
title: Lastpass事件调查：黑客在云存储漏洞中窃取了保险库数据
url: https://www.freebuf.com/articles/database/353373.html
source: FreeBuf网络安全行业门户
date: 2022-12-24
fetch_date: 2025-10-04T02:25:49.321707
---

# Lastpass事件调查：黑客在云存储漏洞中窃取了保险库数据

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

Lastpass事件调查：黑客在云存储漏洞中窃取了加密密码库

* ![]()
* 关注

* [数据安全](https://www.freebuf.com/articles/database)

Lastpass事件调查：黑客在云存储漏洞中窃取了加密密码库

2022-12-23 11:49:30

所属地 上海

据Bleeping Computer报道，LastPass当地时间12月22日透露，攻击者在今年早些时候使用2022年8月事件中窃取的信息侵入其云存储，**窃取了客户的加密密码库数据**。

此前，11月30日，该公司首席执行官卡里姆·图巴（Karim Toubba）曾公开承认遭黑客攻击致数据泄露，但他表示[黑客仅获得了部分客户的关键信息](https://www.freebuf.com/news/351313.html)，客户的密码仍被安全加密。这是一年内LastPass发生的两次因云存储漏洞而发生的安全事件。

该公司透露，8月事件的攻击者在被驱逐之前，**对其内部系统访问了四天**。

![](https://image.3001.net/images/20221223/1671767470_63a525ae1fb2a9f3c4ca8.jpg!small)攻击者利用从Lastpass开发者环境中窃取的“云存储访问密钥和双存储容器解密密钥”，获得了对Lastpass云存储的访问。

图巴称，LastPass使用云存储服务来存储生产数据的存档备份。“威胁者从备份中复制了包含****客户基本账户信息和相关元数据的信息，包括公司名称、最终用户名称、账单地址、电子邮件地址、电话号码以及客户访问LastPass服务的IP地址****。”

“威胁者还能够从加密的存储容器中复制客户的保险库数据备份，这些数据以专有的二进制格式存储，既包含未加密的数据如网站URL，也包含完全加密的敏感字段如网站用户名、密码、安全笔记和表格填写的数据。”

但是，LastPass坚称用户的加密数据和主密码仍是安全的。图巴称，LastPass从不知道主密码，它不存储在Lastpass的系统上，LastPass也不维护主密码。

加密数据则采用256位AES加密，只有用每个用户的主密码得出的唯一加密密钥才能解密。

图巴表示，“客户的敏感保险库数据，如用户名和密码、安全笔记、附件和表格填写字段，仍然是基于LastPass的零信任架构进行安全加密。"

公开信息显示，LastPass是一个在线密码管理器和页面过滤器，采用了强大的加密算法，自动登录/云同步/跨平台/支持多款浏览器。该公司声称其产品有超过10万家企业、3300万人员正在使用，是全球最大的在线密码管理软件。

参考链接：

> https://www.bleepingcomputer.com/news/security/lastpass-hackers-stole-customer-vault-data-in-cloud-storage-breach/

# 密码泄露

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