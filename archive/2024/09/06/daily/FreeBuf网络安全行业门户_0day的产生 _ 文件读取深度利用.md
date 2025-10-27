---
title: 0day的产生 | 文件读取深度利用
url: https://www.freebuf.com/articles/web/409192.html
source: FreeBuf网络安全行业门户
date: 2024-09-06
fetch_date: 2025-10-06T18:26:52.273537
---

# 0day的产生 | 文件读取深度利用

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

0day的产生 | 文件读取深度利用

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

0day的产生 | 文件读取深度利用

2024-09-05 10:28:52

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 一.引子

```
大家好,又是鄙人小雷,这次为大家带来的分享是nday产生0day第一篇,没错你没看错是第一篇,也就是后续还会更新一系列如何利用nday去挖掘属于自己的0day。
  至于为什么突发奇想更新此系列,最大的一个原因是网上有很多0day思路分享的文章(尤其cn*d教学居多)都提到了利用nday去产生0day,但是大部分只是提一嘴,真正讲如何去做的却很少，所以小雷也想尽自己所能填补一些公开知识的空缺,为师傅们少走一些弯路做些力所能及的。
```

## 二.初遇

```
又是一个悠闲的周末,窗外乌云密布,为了不让自己的小脑壳生锈小雷决定去挖点0day,于是便有了本文。
```

经过小雷一顿不知名操作锁定了一套系统: xxxx的xxx设备

![1724291141_66c69845d843f9303c9bc.jpg!small?1724291142271](https://image.3001.net/images/20240822/1724291141_66c69845d843f9303c9bc.jpg!small?1724291142271)

```
小雷可是个聪明人，像这种大厂的设备肯定是有很多同行盯着的，如果没有点新颖的骚操作还真不好出货，于是小雷果断用高级搜索引擎:edge查询了该设备存在过的nday。
```

![1724291154_66c698527518503a8970c.jpg!small?1724291154827](https://image.3001.net/images/20240822/1724291154_66c698527518503a8970c.jpg!small?1724291154827)

```
不愧是高级搜索引擎,我小雷没看错你。接下来就是复现nday,0day的第一步是玩转nday。
```

![1724291174_66c6986608c026b663e76.jpg!small?1724291174502](https://image.3001.net/images/20240822/1724291174_66c6986608c026b663e76.jpg!small?1724291174502)

```
成功复现nday,一切顺利,那么接下来就该获取该系统的目录结构了。
  作为一代肾透大师的小雷迅速罗列出了可以获取到目录结构的方法:①通过各种工具fuzz;②该系统存在目录遍历漏洞;③手上有该系统的源码
  显然第三条无法实现直接pass,小雷决定先尝试fuzz
```

# web安全 # 0Day漏洞 # 挖洞思路 # 思路分享 # 漏洞挖掘技术

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

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

一.引子

二.初遇

三.正题

四.成果

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