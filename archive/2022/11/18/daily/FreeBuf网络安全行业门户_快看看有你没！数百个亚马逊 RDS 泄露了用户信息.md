---
title: 快看看有你没！数百个亚马逊 RDS 泄露了用户信息
url: https://www.freebuf.com/articles/350099.html
source: FreeBuf网络安全行业门户
date: 2022-11-18
fetch_date: 2025-10-03T23:07:13.137313
---

# 快看看有你没！数百个亚马逊 RDS 泄露了用户信息

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

快看看有你没！数百个亚马逊 RDS 泄露了用户信息

* ![]()
* 关注

快看看有你没！数百个亚马逊 RDS 泄露了用户信息

2022-11-17 17:45:57

所属地 上海

安全公司 Mitiga 最新发现显示，亚马逊关系型数据库服务（Amazon RDS）上数百个数据库正在暴露用户个人身份信息（PII）。![1668678400_637603006c032b08572a7.jpg!small?1668678400005](https://image.3001.net/images/20221117/1668678400_637603006c032b08572a7.jpg!small?1668678400005)

安全研究员 Ariel Szarf、Doron Karmi 和 Lionel Saposnik 在与 The Hacker News 分享的报告中表示，泄露的数据库中包含用户姓名、电子邮件地址、电话号码、出生日期、婚姻状况、汽车租赁信息，甚至是公司登录信息，如此详细的用户数据，为潜在攻击者提供了丰富的“素材”。

亚马逊 RDS 是一项 Web 服务，可以在亚马逊网络服务（AWS）云中建立关系型数据库。不仅如此，RDS 还支持不同的数据库引擎，例如 MariaDB、MySQL、Oracle、PostgreSQL 和SQL Server 等。

## ****亚马逊 RDS**** ****数据泄露事件详情****

此次亚马逊 RDS 用户个人数据泄漏事件源于一个称为公共 RDS 快照的功能，该功能允许创建一个在云中运行数据库的环境备份，并且可以被所有 AWS 账户访问。

亚马逊方面表示，当用户准备把快照分享为公共快照时，请确保公共快照中不包括自身私人信息，一旦快照被公开共享时，会给予所有 AWS 账户复制快照和从中创建 DB 实例的权限。![1668678754_637604624afdbbc5b3bc0.jpg!small?1668678754107](https://image.3001.net/images/20221117/1668678754_637604624afdbbc5b3bc0.jpg!small?1668678754107)

2022 年 9 月 21 日至 10 月 20 日期间，安全研究人员进行了细致实验，最后发现实验的 810 张快照在不同时间段（从几小时到几周）内被公开分享，照片很容易被恶意行攻击滥用。

在这 810 张快照中，有超过 250 个备份暴露了 30 天，侧面反映它们很可能已经被遗忘了。

根据所暴露信息的特殊性质，潜在攻击者可以窃取数据以期获取经济利益，或利用数据信息来更好地掌握用户所属公司的 IT 环境。

因此，亚马逊强烈建议用户不要开启 RDS 快照公开访问权限，以防止敏感数据的潜在泄漏、滥用或任何其他类型的安全威胁。当然，最好在适当的时候对快照进行加密。

**参考文章：**

https://thehackernews.com/2022/11/researchers-discover-hundreds-of-amazon.html

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

亚马逊 RDS 数据泄露事件详情

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