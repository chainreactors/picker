---
title: 新型安卓系统银行恶意软件能窃取77家金融机构的账户凭证
url: https://www.freebuf.com/news/417038.html
source: FreeBuf网络安全行业门户
date: 2024-12-07
fetch_date: 2025-10-06T19:39:29.963167
---

# 新型安卓系统银行恶意软件能窃取77家金融机构的账户凭证

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

新型安卓系统银行恶意软件能窃取77家金融机构的账户凭证

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型安卓系统银行恶意软件能窃取77家金融机构的账户凭证

2024-12-06 13:47:34

所属地 上海

据BleepingComputer消息，一种名为“DroidBot”的新型安卓系统银行恶意软件试图窃取77 家加密货币交易所和银行应用程序的凭证，涉及英国、意大利、法国、西班牙、葡萄牙等多个国家。

据发现恶意软件的 Cleafy 研究人员称，DroidBot 自 2024 年 6 月以来一直活跃，并作为恶意软件即服务 （MaaS） 平台运行，每月的使用价格为3000美元。

尽管 DroidBot 缺乏任何新颖或复杂的功能，但对其一个僵尸网络的分析显示，英国、意大利、法国、土耳其和德国发生了 776 起感染活动，表明其存在显著活跃的迹象，且该恶意软件似乎仍在积极开发中。目前，一些比较典型的凭证窃取对象包括Binance、KuCoin、BBVA、Unicredit、Santander、Metamask、BNP Paribas、Credit Agricole、Kraken和Garanti BBVA。

DroidBot 的开发人员可能是土耳其人，为威胁组织提供进行攻击所需的所有工具，包括恶意软件构建器、命令和控制 （C2） 服务器以及中央管理面板，可以从目标那里控制其操作、检索被盗数据和发出命令。通过对一个C2 基础设施的分析，已有17个威胁组织在使用该恶意软件。

![](https://image.3001.net/images/20241206/1733464271_675290cf3778e7f4aa83a.png!small)DroidBot 的后台面板

有效负载构建器允许威胁组织自定义 DroidBot 以针对特定应用程序、使用不同的语言并设置其他 C2 服务器地址，此外还可以访问详细的文档、获得恶意软件创建者的支持，并访问定期发布更新的 Telegram 频道。 总而言之，DroidBot MaaS 操作使没有经验或技能较低的网络犯罪分子的进入门槛相当低。

## 模仿热门应用

DroidBot 通常伪装成 Google Chrome、Google Play 商店或“Android Security”，以诱骗用户安装恶意应用程序，主要功能包括：

* **键盘记录**– 捕获受害者输入的每次击键。
* **叠加**– 在合法的银行应用程序界面上显示虚假登录页面。
* **SMS interception （SMS 拦截）**– 劫持传入的 SMS 消息，尤其是那些包含用于银行登录的一次性密码 （OTP） 的消息。
* **虚拟网络计算**– VNC 模块使威胁组织能够远程查看和控制受感染的设备、执行命令以及使屏幕变暗以隐藏恶意活动。

要实现上述恶意功能，一个关键要素也在于DroidBot能够滥用 Android 的辅助功能服务来监控用户操作，并代表恶意软件模拟滑动和点击。因此，如果用户安装的应用程序请求非必要且敏感的权限，应该提高警惕并拒绝相关请求。

此外，建议安卓用户仅从官方应用商店下载程序，在安装时仔细检查权限请求，并确保 Play Protect 在其设备上处于活动状态。

**参考来源：**

> [New DroidBot Android malware targets 77 banking, crypto apps](https://www.bleepingcomputer.com/news/security/new-droidbot-android-malware-targets-77-banking-crypto-apps/)

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

模仿热门应用

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