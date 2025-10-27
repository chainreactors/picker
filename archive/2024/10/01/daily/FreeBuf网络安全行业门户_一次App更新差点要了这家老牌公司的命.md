---
title: 一次App更新差点要了这家老牌公司的命
url: https://www.freebuf.com/articles/412128.html
source: FreeBuf网络安全行业门户
date: 2024-10-01
fetch_date: 2025-10-06T18:51:56.188198
---

# 一次App更新差点要了这家老牌公司的命

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

一次App更新差点要了这家老牌公司的命

* ![]()
* 关注

一次App更新差点要了这家老牌公司的命

2024-09-30 15:15:46

所属地 上海

一家成立了 22 年的世界领先智能音箱公司 Sonos因为一次App更新正面临严重的声誉危机。该App 本应成为公司 CEO Patrick Spence 扩展市场的重要一环，但在更新之后却引发用户疯狂吐槽，导致公司的声誉大幅受损。![](https://image.3001.net/images/20240930/1727680490_66fa4feae03955e364661.png!small)

Sonos 是一家世界领先的智能音箱公司，由 John MacFarlane、Craig Shelburne、Tom Cullen、Trung Mai 一群音乐发烧友创办。2018 年，Sonos 在纳斯达克上市，该公司表示自己不仅是一家硬件公司，也是软件公司。

今年Sonos 公司发布了一次重要更新，万万没想到却捅了马蜂窝。此次App更新中出现了大量的BUG，导致用户体验极其糟糕。具体问题主要集中在以下三个方面：

> 1.声音断断续续和音量失控：用户报告称，新应用程序导致声音断断续续，音量突然增大且无法调节，甚至设备在应用端偶发性“消失”。
>
> 2.尖锐声响和睡眠问题：有用户反映，扬声器在半夜发出尖锐声响，吓坏了全家人和宠物，甚至有人因为害怕音量突然增大而不敢使用新系统。
>
> 3.功能缺失和界面问题：新版应用删除了不少功能，如编辑歌曲队列、管理播放列表等，并且运行缓慢，系统控制难以使用

此次软件更新问题影响了 Sonos 的新产品发布，原定即将推出的两款产品被迫推迟，包括备受期待的Sonos Arc 2条形音箱。该事故还导致公司股价下跌超过 35%，公司将本财年的最高收入预期从17亿美元下调至15亿美元，主流网站也撤回了对 Sonos 产品的广告推荐。

据媒体报道，此次App更新出现大量bug的原因是，Sonos忽视了大量技术债，长期依赖过时的代码和基础设施，导致新应用发布后出现了大量BUG。公司为了追求快速开发和降低成本，大幅裁员了质量保证团队成员。同时，Sonos在2023年和2024年进行了多次裁员，主要集中在营销部门，以降低成本并确保对产品有意义的投资。

事后，Sonos首席执行官帕特里克·斯彭斯公开道歉，并承诺将加速修复新应用程序中的错误，提高用户使用体验，而修复这些问题预计将耗费 2000 万至 3000 万美元。Sonos计划每两周推送一次更新，逐步修复BUG并增加新功能，如提高音量响应速度、改进用户界面等，希望可以提高用户体验并重新赢回用户信任。

## **Sonos 智能音箱****存在多个漏洞**

除了App更新出现bug外，Sonos 智能音箱还被曝存在严重的安全漏洞。

2024年，NCC集团的研究人员向Sonos 报告了智能音箱中的多个漏洞，其中包括CVE-2023-50809漏洞，这个漏洞可能允许攻击者监听用户。研究人员在2024年BLACK HAT USA会议上披露了这些漏洞。CVE-2023-50809漏洞可以被攻击者在目标Sonos 智能音箱的Wi-Fi范围内exploit，以实现远程代码执行和控制设备。

这个漏洞存在于设备的无线驱动程序中，而驱动程序在negotiating WPA2四个手动时未能正确验证信息元素。成功exploit这个漏洞可以使攻击者录制音频并将其传输到攻击者的服务器。

Sonos 公司通过发布Sonos S2版本15.9对漏洞进行了修复，并通知客户说没有可用的工作周转。MediaTek，Sonos 音箱Wi-Fi SoC的制造商，在2024年3月发布了一份安全公告（CVE-2024-20018）。

NCC Group也发布了一份白皮书，详细介绍了其专家在Sonos Era-100和Sonos One设备上实现任意代码执行的逆向工程过程和exploitation技术。

# 数据安全

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

Sonos 智能音箱存在多个漏洞

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