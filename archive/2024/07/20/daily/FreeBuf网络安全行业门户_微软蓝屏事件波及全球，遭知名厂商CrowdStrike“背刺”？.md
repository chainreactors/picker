---
title: 微软蓝屏事件波及全球，遭知名厂商CrowdStrike“背刺”？
url: https://www.freebuf.com/news/406518.html
source: FreeBuf网络安全行业门户
date: 2024-07-20
fetch_date: 2025-10-06T17:42:51.784858
---

# 微软蓝屏事件波及全球，遭知名厂商CrowdStrike“背刺”？

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

微软蓝屏事件波及全球，遭知名厂商CrowdStrike“背刺”？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软蓝屏事件波及全球，遭知名厂商CrowdStrike“背刺”？

2024-07-19 14:48:34

所属地 上海

今天（7月19日）下午，全球多地的Windows系统用户遭遇了电脑崩溃的问题，一时间**“微软蓝屏”**的话题登上微博热搜榜首，热度居高不下。

![1721371467_669a0b4be6119fd25bd37.png!small](https://image.3001.net/images/20240719/1721371467_669a0b4be6119fd25bd37.png!small)

点进相关话题下，有大量网友晒出自己的电脑呈现蓝屏画面，其中不少出现了“csagent.sys”错误。还有网友戏称：“提前过上周末了。”

![1721371647_669a0bffc4f02c266f8e8.png!small](https://image.3001.net/images/20240719/1721371647_669a0bffc4f02c266f8e8.png!small)

![1721371692_669a0c2cb97224a5420bc.png!small](https://image.3001.net/images/20240719/1721371692_669a0c2cb97224a5420bc.png!small)

有安全专家表示，此次全球蓝屏事件的原因是由CrowdStrike代理（csagent.sys）导致的“WIN32K\_POWER\_WATCHDOG\_TIMEOUT”错误，从而引发了系统崩溃，出现蓝屏。由于全球大量用户使用了CrowdStrike的网络安全解决方案，从而引发大范围的服务中断，看起来似乎是一个“全球事件”。

据阿里云监控发现，北京、深圳、上海、杭州、东京、新加坡、印度尼西亚（雅加达）、菲律宾（马尼拉）、泰国（曼谷）、德国（法兰克福）、英国（伦敦）等地域的Windows 系统的云服务器ECS 实例异常重启，阿里云工程师已向微软反馈，目前正在紧急介入排查。

![1721372253_669a0e5d771dfb52f9cc5.png!small](https://image.3001.net/images/20240719/1721372253_669a0e5d771dfb52f9cc5.png!small)

![1721372231_669a0e479672d81a7b21c.png!small](https://image.3001.net/images/20240719/1721372231_669a0e479672d81a7b21c.png!small)

据悉，此次 Windows 系统中断还波及到了LME交易所、多家银行、航空公司等行业。

根据美国联邦航空管理局空中交通管制系统指挥中心，美国联合航空、美国航空和达美航空已对所有航班发出地面停飞指令。德国柏林机场也称，由于技术故障，登机手续将出现延误。

**对此，专家提出了以下可能有效的方案：**
1、三次异常重启进入安全模式
2、打开路径C:\Windows\System32\drivers\CrowdStrike找到csagent.sys，修改此文件名

## 网友反馈曾多次遇到更新错误

昨天（7月18日），科技媒体Windows Latest发文称有网友反馈，在安装Windows 11的7月份累积更新 KB5040442 过程中，曾多次遇到0x80d02002、0x800f081f、0x80073cf3等错误。还有网友反馈，连续安装3次KB5040442更新，每次都会报告0x80d02002错误。

另一位网友从Microsoft Catalog Update下载更新，手动安装更新也失败了。Windows 11用户还反馈安装7月份累积更新KB5040442之后，出现了拖慢性能、循环重启、卡死在修复模式（最终蓝屏）的问题。此外还有一位Reddit用户，在更新之后电脑和虚拟机变砖。

微软出现蓝屏，通常是指Windows操作系统在运行过程中出现的屏幕显示蓝色错误信息的现象，‌通常伴随着系统崩溃，‌严重影响了用户的工作效率。

此次Windows操作系统遭遇大范围蓝屏故障，‌引发了用户对其安全性的担忧。‌

## Microsoft 365系列服务访问中断

除此之外，微软还发布官方消息称，旗下Microsoft 365系列服务出现访问中断，受影响的包括但不限于Microsoft 365各个应用，状态页面警告称客户可能无法访问SharePoint Online、OneDrive for Business、Teams、Intune、PowerBI、Microsoft Fabric、Microsoft Defender和Viva Engage。

微软方面表示，服务中断始于美国东部时间周四下午6点左右，其部分客户在美国中部地区的多项Azure服务中遇到了问题，目前微软的策略是将流量路由到其他未受影响的区域尝试恢复恢复。Azure是一个云计算平台，提供用于构建、部署和管理应用程序和服务的服务。另外，微软表示正在调查影响各种Microsoft 365应用和服务的问题。该公司还表示，随着问题不断得到缓解，其观察到服务可用性呈现积极趋势。

根据网站故障追踪软件 Downdetector 今天（7 月 19 日）公布的数据来看，日本用户报告 Microsoft 365 出现了问题。截至当地时间下午 1:35 左右，共有 2800 多份故障报告，其中 69% 的报告与 Onedrive 有关。

微软的Azure状态页面建议，已设置灾难恢复程序的客户可以考虑尝试采取措施将其服务故障转移到其他地区，如果遇到问题，可以考虑使用编程选项。目前，微软虽然已经宣布美国中部地区已恢复运营，但Microsoft 365 仍处于降级状态，许多服务对部分用户不可用。

文章来源综合自网络

# 微软安全 # Windows系统

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

网友反馈曾多次遇到更新错误

Microsoft 365系列服务访问中断

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