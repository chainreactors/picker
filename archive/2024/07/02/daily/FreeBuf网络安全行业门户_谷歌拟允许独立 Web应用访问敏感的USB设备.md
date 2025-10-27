---
title: 谷歌拟允许独立 Web应用访问敏感的USB设备
url: https://www.freebuf.com/news/404867.html
source: FreeBuf网络安全行业门户
date: 2024-07-02
fetch_date: 2025-10-06T17:45:10.099630
---

# 谷歌拟允许独立 Web应用访问敏感的USB设备

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

谷歌拟允许独立 Web应用访问敏感的USB设备

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

谷歌拟允许独立 Web应用访问敏感的USB设备

2024-07-01 10:34:50

所属地 上海

据BleepingComputer消息，谷歌正在开发一项不受限制的 WebUSB 新功能，可允许受信任的隔离网络应用程序绕过 WebUSB API 中的安全限制。

![](https://image.3001.net/images/20240701/1719801567_668216df4c0cafa9a1c3c.jpg!small)

WebUSB 是一种 JavaScript API，能够让网络应用程序访问计算机上的本地 USB 设备。作为 WebUSB 规范的一部分，某些接口，比如HID、大容量存储、智能卡、视频、音频/视频设备和无线控制器会受保护，不能通过网络应用程序访问，以防止恶意脚本访问潜在的敏感数据。

此外，WebUSB 规范还包括一个阻止列表，禁止通过 API 访问的特定 USB 设备，如用于多因素身份验证的 YubiKeys、Google Titan 密钥和 Feitian 安全密钥。

谷歌目前正在测试的 "无限制 WebUSB "功能，允许隔离的网络应用程序访问这些受限制的设备和接口。谷歌在 Chrome 浏览器的状态更新中指出："WebUSB 规范定义了一个易受攻击设备的屏蔽列表和一个受保护接口类的列表，这些设备和接口类被禁止通过 WebUSB 访问。有了这项功能，拥有访问 ‘usb-un-restricted’ 权限策略功能的隔离网络应用程序将被允许访问这些列表中的设备和受保护的接口。“

独立网络应用程序是指不托管在实时网络服务器上，而是打包成网络捆绑包（Web Bundles）、由开发人员签名并分发给最终用户的应用程序。这些应用程序通常供公司内部使用。为使其正常运行，这些网络应用必须拥有使用 "USB-unrestricted "功能的权限。

当具有该权限的应用程序试图访问 USB 设备时，系统会首先检查该设备是否在易受攻击设备的拦截列表中。如果是，该设备通常会从访问列表中移除。但使用 "usb-unrestricted "权限的网络应用程序可以绕过这一限制。

这一功能无疑会让受信任的隔离网络应用程序能够访问更广泛的 USB 设备，从而在受信任的环境中实现更多功能。谷歌表示，它计划在将于 2024 年 8 月发布 Chome 128 版本中对其进行测试。

参考来源：

> [Google Chrome to let Isolated Web App access sensitive USB devices](https://www.bleepingcomputer.com/news/google/google-chrome-to-let-isolated-web-app-access-sensitive-usb-devices/)

# web安全

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