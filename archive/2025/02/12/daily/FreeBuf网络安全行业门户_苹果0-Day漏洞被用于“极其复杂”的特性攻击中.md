---
title: 苹果0-Day漏洞被用于“极其复杂”的特性攻击中
url: https://www.freebuf.com/news/421415.html
source: FreeBuf网络安全行业门户
date: 2025-02-12
fetch_date: 2025-10-06T20:36:23.295054
---

# 苹果0-Day漏洞被用于“极其复杂”的特性攻击中

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

苹果0-Day漏洞被用于“极其复杂”的特性攻击中

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

苹果0-Day漏洞被用于“极其复杂”的特性攻击中

2025-02-11 10:40:41

所属地 上海

近日，苹果公司发布了紧急安全更新，以修补一个0-Day漏洞，编号CVE - 2025 - 24200，由公民实验室 安全研究人员比尔·马尔扎克报告。该漏洞在有针对性的且“极其复杂”的攻击中被利用，“在设备锁定时禁用USB限制模式”。

![](https://image.3001.net/images/20250211/1739252296_67aae248243ce64daa37e.png!small)

USB限制模式是苹果设备的一项安全功能，如果设备锁定超过一小时，该功能会阻止USB配件创建数据连接。此功能旨在阻止像Graykey和Cellebrite（执法部门常用）这类取证软件从锁定的iOS设备中提取数据。2024年11月，苹果还公司推出了另一项安全功能——闲置重启，即在长时间闲置后自动重启iPhone，以重新加密数据，使取证软件更难提取数据。

受影响的设备包括iPhone XS及更新机型、iPad Pro 13英寸、iPad Pro 12.9英寸第3代及更新机型、iPad Pro 11英寸第1代及更新机型、iPad Air第3代及更新机型、iPad第7代及更新机型、iPad mini第5代及更新机型。

尽管此漏洞仅在有针对性的攻击中被利用，但仍强烈建议立即安装iOS 18.3.1更新，以阻止潜在的持续攻击尝试。

公民实验室曾在2023年9月的紧急安全更新中披露了另外两个零日漏洞（CVE - 2023 - 41061和CVE - 2023 - 41064），苹果公司对此进行了修复。这两个漏洞被用作零点击漏洞利用链（被称为BLASTPASS）的一部分，用于感染完全打过补丁的iPhone，使其感染NSO集团的Pegasus商业间谍软件。

上个月，苹果公司修复了今年第一个被标记为在针对iPhone用户的攻击中被利用的零日漏洞（CVE - 2025 - 24085）。

2024年，该公司修补了六个正在被利用的零日漏洞；即2023年，苹果公司修补了20个在野外被利用的零日漏洞，其中包括：

11月的两个零日漏洞（CVE - 2023 - 42916和CVE - 2023 - 42917）；
10月的两个零日漏洞（CVE - 2023 - 42824和CVE - 2023 - 5217）；
9月的五个零日漏洞（CVE - 2023 - 41061、CVE - 2023 - 41064、CVE - 2023 - 41991、CVE - 2023 - 41992和CVE - 2023 - 41993）；
7月的两个零日漏洞（CVE - 2023 - 37450和CVE - 2023 - 38606）；
6月的三个零日漏洞（CVE - 2023 - 32434、CVE - 2023 - 32435和CVE - 2023 - 32439）；
5月的另外三个零日漏洞（CVE - 2023 - 32409、CVE - 2023 - 28204和CVE - 2023 - 32373）；
4月的两个零日漏洞（CVE - 2023 - 28206和CVE - 2023 - 28205）；
以及2月的另一个WebKit零日漏洞（CVE - 2023 - 23529）。

参考来源：<https://www.bleepingcomputer.com/news/apple/apple-fixes-zero-day-exploited-in-extremely-sophisticated-attacks/>

# 漏洞 # 网络安全 # 数据安全

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