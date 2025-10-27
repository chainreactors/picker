---
title: 疑似俄罗斯“军事黑客”持续攻击波兰政府机构
url: https://www.freebuf.com/news/400468.html
source: FreeBuf网络安全行业门户
date: 2024-05-11
fetch_date: 2025-10-06T17:16:56.172478
---

# 疑似俄罗斯“军事黑客”持续攻击波兰政府机构

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

疑似俄罗斯“军事黑客”持续攻击波兰政府机构

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

疑似俄罗斯“军事黑客”持续攻击波兰政府机构

2024-05-10 11:07:53

所属地 上海

近日，波兰政府宣布，疑似与俄罗斯军事情报局（GRU）有关的威胁攻击者一直在“袭击”波兰政府机构。![1715310435_663d8f630a0072a37c021.png!small](https://image.3001.net/images/20240510/1715310435_663d8f630a0072a37c021.png!small)

CSIRT MON（波兰国防部长领导的计算机安全事件响应小组）和 CERT Polska（波兰计算机应急响应小组）近期发现很多资料，证实了疑似具有俄罗斯背景的黑客组织 APT28 在一次大规模网络钓鱼活动中，攻击了多个波兰政府机构。

威胁攻击者通过发布一些网络钓鱼邮件，试图诱使收件人点击显示为”获得更多有关一名神秘的乌克兰妇女向波兰和乌克兰高级当局 "出售 "二手内衣信息的链接。一旦点击链接，收件人就会被重定向到多个网站，然后进入一个下载 ZIP 压缩包的页面。

据悉，该压缩包包含了一个伪装成 JPG 图像文件的恶意可执行文件以及名为 DLL 和 .BAT 脚本的隐藏文件。

在受害目标打开伪装的可执行文件后，隐藏的脚本就会立刻自动运行，脚本会在 Microsoft Edge 浏览器中显示一张泳装女子的照片，分散受害者的注意力，同时”偷偷“下载 CMD 文件并将其扩展名更改为 JPG。

值得一提的是，此次网络攻击活动中使用的策略和基础工具与另一起网络攻击运动中使用的策略和基础工具非常相似，APT28 组织成员使用“以色列-哈马斯冲突”作为诱饵，给 13 个国家（包括联合国人权理事会成员）的官员“提供”带有 Headlace 恶意软件的后门设备。
![1715310449_663d8f7162d0c2f457789.png!small](https://image.3001.net/images/20240510/1715310449_663d8f7162d0c2f457789.png!small)

APT28 攻击流 （CERT Polska）

APT28 黑客组织自 2000 年代中期浮出水面以来，组织发动了许多备受瞩目的网络攻击时间。2018 年，业内很多从业者将其与 GRU 的军事单位 26165 联系在一起。

据悉，APT28 组织不仅可能是 2016 年美国总统大选前入侵民主党全国委员会（DNC）和民主党国会竞选委员会（DCCC）的幕后黑手，也有可能是 2015 年入侵德国联邦议会（Deutscher Bundestag）的幕后真凶。

2018 年 7 月，美国当局曾指控 APT28 多名成员参与到 DNC 和 DCCC 网络攻击事件中，欧盟理事会在 2020 年 10 月因联邦议院网络攻击事件，宣布制裁 APT28 组织。

一周前，北约、欧盟以及一些国际合作伙伴正式谴责了针对包括德国和捷克在内的多个欧洲国家的长期 APT28 网络间谍活动。德国表示，APT28 组织入侵了社会民主党执行委员会成员的多个电子邮件账户。捷克外交部也透露，APT28 在 2023 年袭击了捷克境内的一些机构。

美国国务院曾发布声明，呼吁 APT28 组织背后的运营商立刻停止一恶意网络攻击活动，遵守国际承诺和义务，并一再强调，美国将与欧盟和北约盟国一道，继续采取更加严厉的措施，打击 APT28 组织的网络攻击活动，保护其公民的信息资产，追究威胁攻击者的责任。

参考文章：

> https://www.bleepingcomputer.com/news/security/poland-says-russian-military-hackers-target-its-govt-networks/

# 黑客攻击 # APT组织

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