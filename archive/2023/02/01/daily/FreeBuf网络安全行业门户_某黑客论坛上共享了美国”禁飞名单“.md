---
title: 某黑客论坛上共享了美国”禁飞名单“
url: https://www.freebuf.com/news/356083.html
source: FreeBuf网络安全行业门户
date: 2023-02-01
fetch_date: 2025-10-04T05:20:56.628752
---

# 某黑客论坛上共享了美国”禁飞名单“

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

某黑客论坛上共享了美国”禁飞名单“

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

某黑客论坛上共享了美国”禁飞名单“

2023-01-31 11:29:40

所属地 河南省

##

Bleeping Computer 网站披露，某黑客论坛上公开分享了一份美国”禁飞名单“，该名单上有超过 150 万名被禁飞者和超过 25 万名“被选中者”的数据信息。![1675135843_63d88b636ddc560230dd1.png!small?1675135845727](https://image.3001.net/images/20230131/1675135843_63d88b636ddc560230dd1.png!small?1675135845727)

目前，Bleeping Computer 已确认列表名单与 CommuteAir 航空服务器上发现的 TSA 禁飞列表名单相同。

## ****黑客论坛公开分享”禁飞名单“****

2023 年 1 月份，Daily Dot 记者 Mikael Thalen 报道瑞士黑客 maia arson crimew 偶然发现一个包含 TSA 禁飞名单的 AWS 服务器。据悉，该服务器属于俄亥俄州 CommuteAir 航空公司，尽管早些时候可能已采取措施修补漏洞，但截至 1 月 26 日，禁飞名单仍在一个可公开访问的黑客论坛上”浮现“。![1675135855_63d88b6f328a4651aeeb7.png!small?1675135856315](https://image.3001.net/images/20230131/1675135855_63d88b6f328a4651aeeb7.png!small?1675135856315)

美国禁飞名单在一个黑客论坛上公开分享（Bleeping Computer）

Bleeping Computer 查看禁飞名单列表的一部分，这些列表以两个名为 “NOFLY（禁飞名单）”和“SELECTEE”的 CSV 文件的形式列出了一些飞往美国时在机场接受二级安检（SSSS）的乘客。黑客论坛上公布的禁飞名单包含 1566062 条记录（部分重复），SELECTEE 名单包括 251169 条记录，重复和别名意味着暴露的姓名总数少于 150 万。

值得一提的是，两个列表都包含用户的名、姓、潜在的别名和出生日期。据黑客称，这些名单是 2019 年的。据 Daily Dot 观察，列表名单提到了俄罗斯军火商维克托·布特及其 16 个潜在化名。

禁飞名单无疑是国家机密，据悉，美国联邦调查局 TSC（恐怖分子筛查中心）是多个联邦机构用来管理和共享反恐综合信息，该机构就有一个名为“恐怖分子筛查数据库”的观察名单，有时也称为“禁飞名单” ，考虑到这些数据库在协助国家安全和执法任务方面发挥着至关重要的作用，因此绝对保密，即使不是“机密”信息，也被视为敏感的资料。

因此，禁飞名单通常不为公众所知，但是私营航空公司和国务院、国防部、运输安全局（TSA）、海关和边境保护局（CBP）等多个机构都会参考这份名单，以检查乘客是否被允许飞行，是否能够进入美国。![1675135949_63d88bcd1af73e28ba38c.png!small?1675135950446](https://image.3001.net/images/20230131/1675135949_63d88bcd1af73e28ba38c.png!small?1675135950446)

包括鲍勃·迪亚琴科（Bob Diachenko）在内的研究人员此前就已发现互联网上暴露的秘密恐怖分子监视名单，但这些信息早在主流新闻报道之前就被修补好了。然而，此次“禁飞名单”是第一次在公众可访问的网站上共享。

有趣的是，与此次黑客论坛上发布的名单相比，迪亚琴科在 2021 发现的名单相当详细，其中姓名、性别、护照号码，甚至护照签发国、观察名单 ID 等字段都包含。

## ****美国政府********正在********调查********“********禁飞名单********”********泄露事件****

尽管此次安全漏洞源于一家航空公司的 AWS 服务器，但这种行为足够使美国政府机构感到震惊。目前，美国政府官员和立法者都在调查此事。

1 月 27 日，美国运输安全管理局向机场和航空公司发布了安全指令，旨在强化处理敏感安全信息和个人身份信息的现有要求，以保护系统和网络免受网络攻击。

除此之外，据一位知情人士透漏，没有任何 TSA 信息系统被破坏，联邦机构已向所有航空公司发布了行业安全意识信息，以审查其系统并立即采取行动确保其文件受到保护。![1675135981_63d88bedb67c9191e2fd2.png!small?1675135983330](https://image.3001.net/images/20230131/1675135981_63d88bedb67c9191e2fd2.png!small?1675135983330)

CommuteAir 表示，截至目前没有客户数据被泄露，公司也向网络安全和基础设施安全局报告了数据暴露情况，并通知其员工。

1 月 26 日，美国国土安全委员会成员在信中强调，黑客声称其可能已经能够利用服务器，取消或推迟航班，甚至换掉机组成员，如果情况属实，会严重影响国家安全。

注：黑客 maia arson crimew，此前使用 deletescape、antiproprietary 和 Tillie Kottmann 等别名，曾被美国以共谋、电信欺诈和严重的身份盗窃（PDF）起诉。

**文章来源：**

> https://www.bleepingcomputer.com/news/security/us-no-fly-list-shared-on-a-hacking-forum-government-investigating/

# 数据泄漏

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

黑客论坛公开分享”禁飞名单“

美国政府正在调查“禁飞名单”泄露事件

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