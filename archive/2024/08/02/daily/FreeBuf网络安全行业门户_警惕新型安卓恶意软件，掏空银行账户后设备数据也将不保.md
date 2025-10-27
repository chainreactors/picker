---
title: 警惕新型安卓恶意软件，掏空银行账户后设备数据也将不保
url: https://www.freebuf.com/news/407491.html
source: FreeBuf网络安全行业门户
date: 2024-08-02
fetch_date: 2025-10-06T18:03:02.937214
---

# 警惕新型安卓恶意软件，掏空银行账户后设备数据也将不保

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

警惕新型安卓恶意软件，掏空银行账户后设备数据也将不保

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

警惕新型安卓恶意软件，掏空银行账户后设备数据也将不保

2024-08-01 11:47:49

所属地 上海

一种被研究人员称为"BingoMod"的新型安卓恶意软件，在成功利用设备上的欺诈技术从受害者的银行账户中窃取资金后，可以清除设备数据。

BingoMod通过短信推广，通常伪装成一个合法的移动安全工具，每次交易最多可窃取15000欧元。

根据研究人员的分析，BingoMod目前正在积极开发中，其开发者专注于添加代码混淆和各种逃避机制，以降低被检测率。

![Android](https://image.3001.net/images/20240801/1722489788_66ab1bbc39fab9d19b2c8.jpg!small)

## BingoMod的详细信息

在线欺诈管理和预防解决方案公司Cleafy的研究人员发现，BingoMod是通过smishing（短信钓鱼）活动传播的，并使用通常表明移动安全工具的各种名称（例如APP Protection, Antivirus Cleanup, Chrome Update, InfoWeb, SicurezzaWeb, WebSecurity, WebsInfo, WebInfo, APKAppScudo）。

有一次，BingoMod使用了Google Play上免费的AVG AntiVirus & Security工具的图标。在安装过程中，该恶意软件请求使用无障碍服务的权限，该服务可提供高级功能，允许对设备进行广泛控制。一旦激活，BingoMod就会窃取任何登录凭证、截图并拦截短信消息。

为了在设备上进行欺诈（ODF），恶意软件建立了一个基于套接字的通道来接收命令，以及一个基于HTTP的通道来发送屏幕截图源，从而实现几乎实时的远程操作。

![VNC mechanism and data exchange](https://image.3001.net/images/20240801/1722489792_66ab1bc0ca370be54c831.jpg!small)

虚拟网络计算 （VNC） 机制和数据交换  来源：Cleafy

ODF是一种从受害者的设备发起欺诈交易的常用技术，可以骗过依赖身份验证和认证的标准反欺诈系统。

Cleafy研究人员在报告中解释说，“VNC程序滥用安卓的Media Projection API来获取实时屏幕内容。一旦接收到这些内容，就会将其转换为合适的格式，并通过HTTP传输到威胁行为者的基础设施。”

该程序的一个特点是，它可以利用无障碍服务“冒充用户并启用由Media Projection API公开的屏幕投影请求。”

![VNC routing](https://image.3001.net/images/20240801/1722489797_66ab1bc59f053327c6adb.jpg!small)

BingoMod 的 VNC 路由器  来源：Cleafy

远程操作者可以向BingoMod发送的命令包括点击特定区域、在指定的输入元素上写文本和启动应用程序。

该恶意软件还允许通过威胁行为者发起的虚假通知手动进行覆盖攻击。此外，感染了BingoMod的设备还可以通过短信进一步传播恶意软件。

## 禁用防御和清除数据

BingoMod可以从受害者的设备中移除安全解决方案或阻止威胁行为者在命令中指定的应用程序的活动。

为了逃避检测，BingoMod的创建者添加了代码扁平化和字符串混淆层，根据VirusTotal上的扫描结果，实现了预期的目标。

![VirusTotal scan results](https://image.3001.net/images/20240801/1722489802_66ab1bca01e08a7875816.jpg!small)

VirusTotal 扫描结果  来源：Cleafy

如果BingoMod作为设备管理应用程序注册在设备上，操作者就可以发送远程命令来清除系统。根据研究人员的说法，这个功能只有在成功转账后才会执行，并且只影响外部存储。

![Data wiping routing](https://image.3001.net/images/20240801/1722489805_66ab1bcd8ee87324cba39.jpg!small)

数据清除程序  来源：Cleafy

如果要彻底清除系统，威胁行为者可能使用远程访问功能从系统设置中清除所有数据并重置手机。

虽然BingoMod目前的版本是1.5.1，但Cleafy表示它似乎处于早期开发阶段。根据代码中的注释，研究人员认为BingoMod可能是罗马尼亚开发者的作品。不过，也有可能是其他国家的开发者所为。

参考来源：https://www.bleepingcomputer.com/news/security/new-android-malware-wipes-your-device-after-draining-bank-accounts/

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

BingoMod的详细信息

禁用防御和清除数据

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