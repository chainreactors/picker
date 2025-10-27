---
title: NGate安卓恶意软件可利用 NFC 窃取 ATM 内资金
url: https://www.freebuf.com/news/409267.html
source: FreeBuf网络安全行业门户
date: 2024-08-24
fetch_date: 2025-10-06T18:04:59.704413
---

# NGate安卓恶意软件可利用 NFC 窃取 ATM 内资金

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

NGate安卓恶意软件可利用 NFC 窃取 ATM 内资金

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

NGate安卓恶意软件可利用 NFC 窃取 ATM 内资金

2024-08-23 13:33:18

所属地 上海

近日，ESET 的研究人员发现了一款名为 NGate 的恶意软件，它可以通过恶意应用程序将受害者支付卡上的数据传输到攻击者已root的安卓手机上。

![1724391128_66c81ed88134ddff7786d.png!small](https://image.3001.net/images/20240823/1724391128_66c81ed88134ddff7786d.png!small)

攻击概述（来源：ESET）

## 未经授权的 ATM 提款

该活动针对银行的主要目的是从受害者的银行账户中为未经授权的 ATM 取款提供便利。具体来看，该活动主要是通过使用 NGate Android 恶意软件，将受害者实体支付卡中的 NFC 数据通过被入侵的 Android 智能手机转发到攻击者的设备来实现的。然后，攻击者会利用这些数据进行 ATM 交易。如果这种方法失败，攻击者还有一个后备计划，即从受害者的账户向其他银行账户转移资金。

发现这种新型威胁和技术的 Lukáš Štefanko 说表示：我们还没有在以前发现的任何安卓恶意软件中看到过这种新颖的NFC中继技术。该技术基于德国达姆施塔特技术大学学生设计的一种名为 NFCGate 的工具，用于捕获、分析或更改 NFC 流量；因此，我们将这个新的恶意软件系列命名为 NGate。

## NGate 安卓恶意软件活动

受害者可能误以为自己正在与银行通信，但实际上设备已遭入侵，并在不知情的情况下通过一条关于潜在退税的欺骗性短信中的链接下载并安装了一个应用程序，导致自己的安卓设备受到了威胁。

值得注意的是，NGate 从未在 Google Play 官方商店上架过。

NGate安卓恶意软件与一个自2023年11月起就在捷克活动的威胁行为者的网络钓鱼活动有关。不过，ESET 认为，在 2024 年 3 月逮捕一名嫌疑人后，这些活动就被搁置了。ESET Research首次发现该威胁行为者从2023年11月底开始针对捷克著名银行的客户进行攻击。恶意软件是通过冒充合法银行网站或 Google Play 商店中的官方手机银行应用程序的短暂域名进行传播的。

攻击者利用了渐进式网络应用程序（PWA）的潜力，后来又通过使用被称为 WebAPK 的更复杂版本的 PWA 来完善其策略，这次行动以部署 NGate 恶意软件而告终。

## 收集个人信息

2024 年 3 月，ESET Research 发现 NGate Android 恶意软件在以前用于促进提供恶意 PWA 和 WebAPK 的网络钓鱼活动的分发域上可用。安装并打开后，NGate 会显示一个虚假网站，要求用户提供银行信息，然后将其发送到攻击者的服务器。

除了网络钓鱼功能外，NGate 恶意软件还附带一个名为 NFCGate 的工具，该工具被滥用于在两个设备之间中继 NFC 数据——受害者的设备和犯罪者的设备。其中一些功能仅适用于已获得 root 权限的设备;但是，在这种情况下，也可以从非 root 设备中继 NFC 流量。

NGate 还会提示受害者输入敏感信息，例如他们的银行客户 ID、出生日期和银行卡的 PIN 码。它还要求他们在智能手机上打开 NFC 功能。然后指示受害者将他们的支付卡放在智能手机的背面，直到恶意应用程序识别出该卡。

![1724394783_66c82d1f6b3e3401af277.png!small?1724394783924](https://image.3001.net/images/20240823/1724394783_66c82d1f6b3e3401af277.png!small?1724394783924)

## 物理访问支付卡

除了 NGate 恶意软件使用的技术外，攻击者还可以通过物理访问支付卡来复制和仿真支付卡。攻击者可以通过无人看管的钱包、背包或装有支付卡的智能手机壳读取支付卡，尤其是在公共场所和人群密集的地方。不过，这种情况一般仅限于在终端点进行小额非接触式支付。

Štefanko 建议：想要防范此类复杂的攻击，就必须采取某些主动措施，比如防范网络钓鱼、社交工程和安卓恶意软件等手段。同时要注意检查网站的 URL、从官方商店下载应用程序、对 PIN 码保密、在智能手机上使用安全应用程序、在不需要时关闭 NFC 功能、使用保护壳或使用受身份验证保护的虚拟卡等等。

> 参考来源：[Android malware uses NFC to steal money at ATMs - Help Net Security](https://www.helpnetsecurity.com/2024/08/22/android-malware-nfc-data-atm-withdrawals/)

# 恶意软件 # NFC安全

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

未经授权的 ATM 提款

NGate 安卓恶意软件活动

收集个人信息

物理访问支付卡

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