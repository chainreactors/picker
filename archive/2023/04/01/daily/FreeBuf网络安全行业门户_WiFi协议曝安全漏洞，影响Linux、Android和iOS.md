---
title: WiFi协议曝安全漏洞，影响Linux、Android和iOS
url: https://www.freebuf.com/news/362195.html
source: FreeBuf网络安全行业门户
date: 2023-04-01
fetch_date: 2025-10-04T11:22:26.318158
---

# WiFi协议曝安全漏洞，影响Linux、Android和iOS

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

WiFi协议曝安全漏洞，影响Linux、Android和iOS

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

WiFi协议曝安全漏洞，影响Linux、Android和iOS

2023-03-31 14:06:15

所属地 上海

![](https://image.3001.net/images/20230331/1680240543_64266f9f9fd9e6bd3d490.png!small)

来自美国东北大学和鲁汶大学的学者披露了一组IEEE 802.11 Wi-Fi协议标准的一个基础设计漏洞，影响到运行Linux、FreeBSD、Android和iOS的各种设备。

研究人员Domien Schepers、Aanjhan Ranganathan和Mathy Vanhoef在本周发表的一篇论文中披露，利用这一漏洞可以劫持TCP连接、拦截客户端和web流量。主要手段是利用终端设备的电源节能机制，诱使接入点泄漏数据帧，或使用全零密钥对其进行加密。

其原理是利用大多数Wi-Fi堆栈在安全环境发生变化时没有充分地去清除其发送队列这一现象，从发往受害客户端站的接入点泄漏帧。

除此之外，攻击者还可以覆盖接入点使用的客户端安全栈，以接收发送给受害者的数据包。这种攻击的前提是目标方连接到一个类似热点的网络。

内部人员可以利用这一点，通过断开受害者的连接，然后在受害者的MAC地址下进行连接（使用对手的证书），拦截通往Wi-Fi客户端的数据。任何仍在通往受害者的数据包，如受害者仍在加载的网站数据，现在都由对方接收。

![](https://image.3001.net/images/20230331/1680240579_64266fc3b5e76b54d5530.png!small)

思科在一份信息通报中把这些漏洞描述为 "机会主义攻击“，攻击者获得的信息在一个安全配置的网络中价值很小。

但是，该公司也承认，研究中提出的攻击可能会成功针对思科无线接入点产品和具有无线功能的思科Meraki产品。

为了减少此类攻击的概率，建议实施传输层安全（TLS）来加密传输中的数据，并限制网络访问。

> 参考链接：thehackernews.com/2023/03/new-wi-fi-protocol-security-flaw.html

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