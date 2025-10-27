---
title: 苹果曝严重漏洞，可窃听用户与Siri对话
url: https://www.freebuf.com/news/348108.html
source: FreeBuf网络安全行业门户
date: 2022-10-29
fetch_date: 2025-10-03T21:13:54.358729
---

# 苹果曝严重漏洞，可窃听用户与Siri对话

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

苹果曝严重漏洞，可窃听用户与Siri对话

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

苹果曝严重漏洞，可窃听用户与Siri对话

2022-10-28 11:24:08

所属地 上海

据The Hacker News 10月27日消息，在苹果近期披露的漏洞中包含了名为SiriSpy的 iOS 和 macOS系统漏洞，使具有蓝牙访问权限的应用程序能够窃听用户与 Siri 的对话。

![](https://image.3001.net/images/20221028/1666927476_635b4b748acfc3c726665.jpg!small)

应用程序开发人员 Guilherme Rambo 在 2022 年 8 月发现并报告了该漏洞，编号为 CVE-2022-32946。

Rambo表示，在使用 AirPods 或 Beats 等设备时，只要请求访问蓝牙权限的都可以记录用户与Siri的对话。而该漏洞与 AirPods 中一项名为 DoAP 的服务有关，该服务用于支持 Siri 和听写功能，从而使攻击者能够制作可通过蓝牙连接到 AirPods 并在后台录制音频的应用程序，且不会显示麦克风的访问请求。

而在 macOS 系统上，该漏洞可能被滥用以完全绕过TCC用户隐私保护框架，这意味着任何应用程序都可以记录用户与 Siri 的对话，且无需请求任何权限。

Rambo表示，造成这一漏洞的原因是由于缺乏对 BTLEServerAgent 的权利检查，BTLEServerAgent 是负责处理 DoAP 音频的保护程序服务。

目前该漏洞已通过系统更新补丁得到修复，涉及的产品包括iPhone8及之后的所有机型；所有的iPad Pro；iPad Air 第 3 代、标准版iPad 第 5 代、iPad mini 第 5 代及后续机型。

> 参考来源：[Apple iOS and macOS Flaw Could've Let Apps Eavesdrop on Your Conversations with Siri](https://thehackernews.com/2022/10/apple-ios-and-macos-flaw-couldve-let.html)

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