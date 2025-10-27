---
title: 揭秘新型安卓间谍软件LianSpy的攻击手段
url: https://www.freebuf.com/news/408008.html
source: FreeBuf网络安全行业门户
date: 2024-08-08
fetch_date: 2025-10-06T18:05:22.429120
---

# 揭秘新型安卓间谍软件LianSpy的攻击手段

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

揭秘新型安卓间谍软件LianSpy的攻击手段

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

揭秘新型安卓间谍软件LianSpy的攻击手段

2024-08-07 11:19:49

所属地 上海

自2021年起，俄罗斯用户已成为一种新型未被记录的安卓后门间谍软件“LianSpy”的攻击目标。

![](https://image.3001.net/images/20240807/1723001053_66b2e8dda28b1fb7d1237.png!small)网络安全公司卡巴斯基在2024年3月发现了这款恶意软件，并指出其利用俄罗斯的云服务Yandex Cloud进行命令和控制（C2）通信，以避免设立专用基础设施并逃避检测。

安全研究员Dmitry Kalinin在周一发布的技术报告中表示：LianSpy能够捕获屏幕录像、窃取用户文件、收集通话记录和应用程序列表。

目前尚不清楚该间谍软件的传播方式，但卡巴斯基推测，它可能是通过未知的安全漏洞或是直接接触目标手机来部署的，这些带有恶意软件的应用程序看起来像是支付宝或安卓系统的一个服务。

LianSpy一旦被激活，会先检查自己是不是以系统应用身份在运行。如果是，它会利用管理员权限在后台操作。如果不是，它会请求一系列权限以访问联系人、通话记录、通知，甚至会在手机屏幕上绘制覆盖层。

它还会检查自己是否在调试环境中运行，以便设置一个在手机重启后也能保持的配置。然后从手机的启动器中隐藏图标，并触发屏幕截图、导出数据和更新配置等活动，以指定需要捕获的信息类型。

某些变种被发现能够收集俄罗斯流行的即时通讯应用的数据，并根据是否连接到Wi-Fi或移动网络来允许或禁止运行恶意软件。

Kalinin说：“为了更新间谍软件配置，LianSpy每隔30秒会在攻击者的Yandex Disk上搜索与正则表达式'^frame\_.+.png$'匹配的文件，如果找到，文件将被下载到应用程序的内部数据目录中。”

并且，收集的数据以加密形式存储在SQL数据库中，指定记录类型和SHA-256哈希值，只有拥有相应私有RSA密钥的攻击者才能解密窃取的信息。

LianSpy的隐蔽性体现在它能够绕过谷歌在Android 12中引入的隐私指示器功能，该功能要求请求麦克风和相机权限的应用显示状态栏图标。LianSpy开发者通过修改Android安全设置参数，防止通知图标出现在状态栏。

它还利用NotificationListenerService隐藏后台服务的通知，处理并抑制状态栏通知。

LianSpy恶意软件的另一个复杂之处在于它使用了修改名称为"mu"的su二进制文件来获取root权限，这增加了它可能是通过一个以前未知的漏洞或对设备的物理访问来传播的可能性。

此外，LianSpy的C2通信是单向的，只接收命令，不发送任何回应。它使用Yandex Disk传输被盗数据和存储配置命令，从硬编码的Pastebin URL更新Yandex Disk的凭据，不同恶意软件变种的 Pastebin URL 各不相同，使用这种合法服务增加了混淆层，追踪LianSpy变得更加困难。

LianSpy是不断增长的间谍软件工具列表中的最新成员，通常利用零日漏洞攻击目标移动设备（无论是 Android 还是 iOS）。Kalinin表示：“除了收集通话记录和应用列表等标准间谍行为外，它还利用root权限进行隐蔽的屏幕录制，避开安全检查，其依赖重命名的su二进制文件，暗示了初次入侵后的二次感染。”

**参考来源：**

> https://thehackernews.com/2024/08/new-android-spyware-lianspy-evades.html

# 恶意软件 # Android恶意软件 # 间谍软件

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