---
title: 谷歌：间谍软件供应商利用安卓和iOS设备上的零日漏洞
url: https://www.freebuf.com/news/362018.html
source: FreeBuf网络安全行业门户
date: 2023-03-31
fetch_date: 2025-10-04T11:15:56.325838
---

# 谷歌：间谍软件供应商利用安卓和iOS设备上的零日漏洞

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

谷歌：间谍软件供应商利用安卓和iOS设备上的零日漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

谷歌：间谍软件供应商利用安卓和iOS设备上的零日漏洞

2023-03-30 11:27:27

所属地 上海

![](https://image.3001.net/images/20230330/1680145054_6424fa9e9251cc72d3100.png!small)

谷歌威胁分析小组（TAG）透露，去年解决的一些零日漏洞被商业间谍软件供应商利用，以Android和iOS设备为目标。

这两个不同的活动都有很强的针对性，利用补丁发布与目标设备上实际修复之间的时间差。

TAG  Clement Lecigne在报告中指出，这些供应商通过扩散具有攻击性的工具，来武装那些无法在内部开发这些能力的政府及组织。

根据国家或国际法律，虽然部分监控技术的使用是合法的，但人们经常发现，有关政府利用这些技术来监控不同政见者、记者、人权工作者和反党人士。

这两次恶意活动，第一次发生在2022年11月，通过短信向位于意大利、马来西亚和哈萨克斯坦的用户发送短链接。点击后，这些URL将收件人重定向到承载安卓或iOS漏洞的网页，然后他们又被重定向到合法的新闻或货运追踪网站。

iOS的漏洞链利用了多个漏洞，包括CVE-2022-42856（当时的零日）、CVE-2021-30900和一个指针认证代码（PAC）绕过，将一个.IPA文件安装到易受影响的设备上。

安卓系统的漏洞链包括三个漏洞--CVE-2022-3723、CVE-2022-4135（滥用时为零日）和CVE-2022-38181以传递一个未指定的有效载荷。

虽然CVE-2022-38181是一个影响Mali GPU内核驱动的特权升级漏洞，在2022年8月被Arm打了补丁，但对方可能在补丁发布之前已经掌握了该漏洞的利用方法。

另一点值得注意的是，在三星浏览器中打开链接的安卓用户，会被重新定向到Chrome。

第二个活动是在2022年12月观察到的，包括几个针对三星浏览器最新版本的零日和n日，这些漏洞通过短信作为一次性链接发送到位于阿联酋的设备。

该网页与西班牙间谍软件公司Variston IT使用的网页类似，都植入了一个基于C++的恶意工具包，能够从聊天和浏览器应用程序中获取数据。

被利用的漏洞包括CVE-2022-4262、CVE-2022-3038、CVE-2022-22706、CVE-2023-0266和CVE-2023-26083。

目前，这两个活动的规模和目标还不清楚。

在拜登签署“限制使用商业间谍软件”的行政命令几天后，这些消息就被披露出来。足以见得，商业间谍软件行业任然在蓬勃发展。监控供应商之间正在分享漏洞和技术，即使是较小的监控供应商也能获得零日漏洞。供应商秘密储存和使用零日漏洞在短时间内对互联网仍构成严重的风险。

> 参考链接：thehackernews.com/2023/03/spyware-vendors-caught-exploiting-zero.html

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