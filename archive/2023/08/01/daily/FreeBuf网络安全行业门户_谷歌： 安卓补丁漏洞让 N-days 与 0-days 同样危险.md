---
title: 谷歌： 安卓补丁漏洞让 N-days 与 0-days 同样危险
url: https://www.freebuf.com/news/373462.html
source: FreeBuf网络安全行业门户
date: 2023-08-01
fetch_date: 2025-10-06T17:00:44.389558
---

# 谷歌： 安卓补丁漏洞让 N-days 与 0-days 同样危险

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

谷歌： 安卓补丁漏洞让 N-days 与 0-days 同样危险

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

谷歌： 安卓补丁漏洞让 N-days 与 0-days 同样危险

2023-07-31 14:00:10

所属地 上海

![](https://image.3001.net/images/20230731/1690770457_64c71c19d606fa20078ef.png!small)

近日，谷歌发布了年度零日漏洞报告，展示了 2022 年的野外漏洞统计数据，并强调了 Android 平台中长期存在的问题，该问题在很长一段时间内提高了已披露漏洞的价值和使用。

更具体地说，谷歌的报告强调了安卓系统中的 "N-days "问题，该问题源于安卓生态系统的复杂性，涉及上游供应商（谷歌）和下游制造商（手机制造商）之间的多个环节。致使不同设备型号之间的安全更新时间存在重大差异，即对于威胁行为者来说，"N-days "就是 "0-days"。

“0-day漏洞”（又称零日漏洞），通常就是指还没有补丁的安全漏洞，也就是已经被少数人发现的，但还没被传播开来，官方还未修复的漏洞。 当“0-day漏洞”被发现并公开后，没有补丁的一段时间内（通常时间会很短），根据习惯这个漏洞会被称为1-day漏洞。当厂商提供了修复补丁，但是漏洞仍然还在被利用时，我们一般会称呼这个漏洞为N-day漏洞。

谷歌在报告中表示，尽管谷歌或其他厂商已经提供了补丁，但攻击者仍可以利用该漏洞。因为即使谷歌或其他厂商修复了漏洞，但下游的设备制造商仍需要几个月的时间才能在自己的安卓版本中推出。

因此，上游厂商和下游厂商之间补丁的间隔使得N-days（公开已知的漏洞）可以像0-days一样，因为用户无法随时获得补丁，他们唯一的办法就是停止使用设备。

## N-days 与 0-days 同样危险

2022 年，诸如此类的问题对安卓系统造成了很大的影响，其中最著名的是 CVE-2022-38181，这是 ARM Mali GPU 中的一个漏洞。该漏洞于 2022 年 7 月报告给安卓安全团队，被认定为 "无法修复"，2022 年 10 月被 ARM 修补，最后被纳入安卓 2023 年 4 月的安全更新中。

2022 年 11 月，即 ARM 发布修补程序一个月后，该漏洞在野外被发现。

直到 2023 年 4 月，Android 安全更新推送修复程序时，对该漏洞的利用仍有增无减，这距离 ARM 解决该安全问题足足过去了 6 个月。

CVE-2022-3038：Chrome 105 中的沙箱逃逸漏洞，该漏洞已于 2022 年 6 月得到修补，但基于早期 Chrome 版本的供应商浏览器（如三星的 "互联网浏览器"）仍未得到解决。

CVE-2022-22706：ARM Mali GPU 内核驱动程序中的漏洞，供应商已于 2022 年 1 月修补了该漏洞。

这两个漏洞于 2022 年 12 月被发现利用，是三星安卓设备感染间谍软件的攻击链的一部分。

三星于 2023 年 5 月发布了针对 CVE-2022-22706 的安全更新，而安卓安全更新则在 2023 年 6 月的安全更新中采用了 ARM 的修复程序，延迟时间长达 17 个月之久。

即使谷歌发布了安卓安全更新，设备供应商也需要长达三个月的时间才能为支持的机型提供修补程序，这就给攻击者提供了针对特定设备攻击的机会。

这种补丁间隙实际上使 "N-day "与 "0-day "具有同等威胁，威胁者可以在未打补丁的设备上利用 "N-day"。相比于0日漏洞N-day可能威胁会更大，因为其技术细节已经公布，可能还有概念验证（PoC）漏洞，使威胁者更容易滥用它们。

好消息是，谷歌 2022 年的活动总结显示，零日漏洞与 2021 年相比有所下降，发现了 41 个，而浏览器类别的下降幅度最大，发现了 15 个漏洞（2021 年为 26 个）。

另一个值得注意的发现是，在 2022 年发现的零日漏洞中，有 40% 以上是以前报告过的漏洞的变种，因为绕过已知漏洞的修复程序通常，比找到一个新型零日漏洞要容易得多。

> 参考链接：https://www.bleepingcomputer.com/news/security/google-android-patch-gap-makes-n-days-as-dangerous-as-zero-days/

# 资讯 # 漏洞 # Android

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

N-days 与 0-days 同样危险

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