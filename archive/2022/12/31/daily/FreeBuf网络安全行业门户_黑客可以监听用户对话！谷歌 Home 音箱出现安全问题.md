---
title: 黑客可以监听用户对话！谷歌 Home 音箱出现安全问题
url: https://www.freebuf.com/news/353938.html
source: FreeBuf网络安全行业门户
date: 2022-12-31
fetch_date: 2025-10-04T02:47:59.577550
---

# 黑客可以监听用户对话！谷歌 Home 音箱出现安全问题

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

黑客可以监听用户对话！谷歌 Home 音箱出现安全问题

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客可以监听用户对话！谷歌 Home 音箱出现安全问题

2022-12-30 15:17:53

所属地 上海

Bleeping Computer 网站披露，Google Home 智能音箱中出现一个安全漏洞，攻击者可以利用漏洞安装后门账户，远程控制音箱，并通过访问麦克风信号将其变成一个监听设备。![1672384708_63ae90c46947a212d444c.jpg!small?1672384708832](https://image.3001.net/images/20221230/1672384708_63ae90c46947a212d444c.jpg!small?1672384708832)

据悉，一名研究员在去年发现这个漏洞问题，并立刻向谷歌报告，最终还获得了 107500 美元。本周早些时候，该研究员公布了有关漏洞的一些技术细节和攻击场景，以展示如何利用漏洞。

## ****Google Home**** ****音箱********漏洞发现过程****

这名研究员用 Google Home 音箱做实验时，发现使用 Google Home 应用添加的新账户可以通过云端 API 远程向其发送指令。研究员通过使用 Nmap 扫描，找到了 Google Home 本地 HTTP API 的端口，于是设置一个代理来捕获加密 HTTPS 流量，以期获取用户授权令牌。 ![1672384726_63ae90d6547941d3b269a.jpg!small?1672384726612](https://image.3001.net/images/20221230/1672384726_63ae90d6547941d3b269a.jpg!small?1672384726612)

捕获的 HTTPS（加密）流量（downrightnifty.me）

随后，研究员发现向目标设备添加新用户需要两个步骤。首先需要从其本地 API 中获取设备名称、证书和“云 ID”。有了这些信息，便可向谷歌服务器发送一个链接请求。

为向目标 Google Home 设备添加恶意用户，研究员在一个 Python 脚本中实现了链接过程，该脚本能够自动过滤本地设备数据并“再现”链接请求。![1672384737_63ae90e1b2b6b2b3a705c.jpg!small?1672384737932](https://image.3001.net/images/20221230/1672384737_63ae90e1b2b6b2b3a705c.jpg!small?1672384737932)

携带设备 ID 数据的链接请求（downrightnifty.me)

**研究员在博客中总结了攻击过程：**

> 攻击者希望在 Google Home 的无线距离内监视受害者（但没有受害者的Wi-Fi 密码）。
>
> 攻击者通过监听与Google Inc.相关前缀的 MAC 地址（如 E4:F0:42）发现受害者的谷歌Home。
>
> 攻击者发送 deauth 数据包以断开设备与网络的连接，使其进入设置模式。
>
> 攻击者连接到设备的网络设置，并请求其设备信息（名称、证书、云ID）。
>
> 攻击者连接到互联网之后，使用获得的设备信息将其账户链接到受害者的设备上。
>
> 这时候，攻击者就可以通过互联网监视受害者的 Google Home 了（不需要再靠近设备）。

值得一提的是，该研究员在 GitHub 上发布了上述行动的三个 PoCs，但应该对运行最新固件版本的 Google Home 设备不起作用。

这些 PoCs 比单纯的植入恶意用户更进一步，攻击者可以通过麦克风进行监听活动，在受害者的网络上进行任意的 HTTP 请求，并在设备上读/写任意文件。

## ****Google Home 音箱********安全问题********可能********带来********的影响****

一旦有恶意账户链接到目标受害者设备上，就有可能通过 Google Home 音箱控制智能开关、进行网上购物、远程解锁车门，或秘密暴力破解用户的智能锁密码。

更令人担忧的是，研究员发现了一种滥用“呼叫[电话号码]”命令的方法，将其添加到一个恶意程序中，随后将在指定时间激活麦克风，调用攻击者的号码并发送实时麦克风反馈。

![1672384778_63ae910a69d5f45f4d557.jpg!small?1672384778796](https://image.3001.net/images/20221230/1672384778_63ae910a69d5f45f4d557.jpg!small?1672384778796)

捕获麦克风音频的恶意路由（downrightnifty.me）

在通话过程中，设备的 LED 会变成蓝色，这是发生某些监听活动的唯一“指示”，就算受害者注意到它了，也可能会认为是设备正在更新其固件。（注：标准麦克风激活指示灯为脉动 LED，在通话过程中不会出现这种情况）

最后，攻击者还可以在被入侵的智能音箱上播放媒体资源，也可以强制重启，甚至“强迫”其忘记存储的 Wi-Fi 网络，强制进行新的蓝牙或Wi-Fi配对等等。

## ****谷歌的修复措施****

研究员在 2021 年 1 月发现 Google Home 智能音箱的安全问题，同年 4 月，谷歌发布安全补丁，修复了所有问题。

补丁中包括一个新的基于邀请的系统，用于处理帐户链接，阻止任何未添加到 Home 的尝试。至于 "呼叫[电话号码]"命令，谷歌新增一个保护措施，以防止其通过例程进行远程启动。

值得注意的是，Google Home 于 2016 年发布，2018 年添加了预定例程，2020 年引入了 Local Home SDK，因此在 2021 年 4 月之前，发现安全漏洞的攻击者有足够的利用时间。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/google-home-speakers-allowed-hackers-to-snoop-on-conversations/

# 漏洞分析

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

Google Home 音箱漏洞发现过程

Google Home 音箱安全问题可能带来的影响

谷歌的修复措施

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