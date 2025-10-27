---
title: 新型恶意软件能利用WIFI定位设备地理位置
url: https://www.freebuf.com/articles/376176.html
source: FreeBuf网络安全行业门户
date: 2023-08-26
fetch_date: 2025-10-04T12:00:35.075893
---

# 新型恶意软件能利用WIFI定位设备地理位置

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

新型恶意软件能利用WIFI定位设备地理位置

* ![]()
* 关注

新型恶意软件能利用WIFI定位设备地理位置

2023-08-25 10:59:56

所属地 上海

Secureworks的研究人员发现，Smoke Loader 僵尸网络背后的网络犯罪分子正在使用一种名为 Whiffy Recon 的新恶意软件，通过 WiFi 扫描和 Google 地理定位 API 来定位受感染设备的位置。

![](https://image.3001.net/images/20230825/1692932300_64e818cca749ccb9918ff.png!small)

Google 的地理定位 API 是一项带有 WiFi 接入点信息的 HTTPS 请求，能返回纬度和经度坐标以定位没有 GPS 系统的设备。

在 Whiffy Recon 的案例中，了解受害者的位置有助于更好地针对特定地区甚至城市进行攻击，或者通过展示跟踪能力来帮助恐吓受害者。根据该区域 WiFi 接入点的数量，通过 Google 地理定位 API 进行的三角测量精度范围可达20米——50 米甚至更小。但在人口密度较低的区域，该精度可能会降低。

恶意软件首先检查服务名称“WLANSVC”，如果不存在，则会将僵尸程序注册到命令和控制（C2）服务器并跳过扫描部分。

![](https://image.3001.net/images/20230825/1692932316_64e818dc25f87b75d2818.png!small)Whiffy Recon 主要功能

对于存在该服务的 Windows 系统，Whiffy Recon 会进入每分钟运行一次的 WiFi 扫描循环，滥用 Windows WLAN API 来收集所需数据，并向 Google 的地理定位 API 发送包含 JSON 格式的 WiFi 接入点信息的 HTTPS POST 请求。

使用 Google 响应中的坐标，恶意软件会制定有关接入点更完整的报告，包括其地理位置、加密方法、SSID，并将其作为 JSON POST 请求发送到攻击者的 C2。

由于此过程每 60 秒发生一次，因此攻击者可以几乎实时对设备进行跟踪。

Secureworks的研究人员于 8 月 8 日发现了这种新型恶意软件，并注意到恶意软件在向 C2 发出的初始 POST 请求中使用的版本号是“1”，表明恶意软件可能还会存在后续开发版本。

> 参考来源：[New Whiffy Recon malware uses WiFi to triangulate your location](https://www.bleepingcomputer.com/news/security/new-whiffy-recon-malware-uses-wifi-to-triangulate-your-location/)

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