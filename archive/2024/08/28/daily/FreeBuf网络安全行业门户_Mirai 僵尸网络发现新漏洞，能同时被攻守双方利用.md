---
title: Mirai 僵尸网络发现新漏洞，能同时被攻守双方利用
url: https://www.freebuf.com/news/409539.html
source: FreeBuf网络安全行业门户
date: 2024-08-28
fetch_date: 2025-10-06T18:04:08.230384
---

# Mirai 僵尸网络发现新漏洞，能同时被攻守双方利用

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

Mirai 僵尸网络发现新漏洞，能同时被攻守双方利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Mirai 僵尸网络发现新漏洞，能同时被攻守双方利用

2024-08-27 11:38:41

所属地 上海

Mirai 僵尸网络在全球 DDoS 攻击中发挥了重要作用，特别是针对 IoT 设备和服务器的攻击。最近，Mirai的命令和控制服务器中发现了一个新漏洞，该漏洞允许攻击者执行DDoS攻击，但同时也能被安全人员用来进行反制。

![](https://image.3001.net/images/20240827/1724737775_66cd68ef6c65c27108687.png!small)

僵尸网络的核心基础设施完全依赖于 C2 服务器，其中可以控制数千台受感染的僵尸计算机。一位名叫“Jacob Masse”的研究人员发现表明，这种DDoS 攻击的存在是由于 CNC 服务器上的会话管理不当造成的。

研究人员表示，发起此攻击不需要身份验证，从而很容易被利用。执法部门或安全研究人员也可以使用这种攻击场景来使 CNC 服务器无法运行，从而导致僵尸网络被拆除。具体原理基于此漏洞会压垮服务器的会话缓冲区，当同时建立多个连接时，无法正确处理该缓冲区。 此外，这种攻击还存在于预验证阶段，即验证打开后的多个同时连接尝试未得到正确处理。

在此情况下，攻击者可以使用根用户名发送验证请求，从而在 CNC 服务器上打开多个连接。 服务器无法管理这些连接尝试，从而导致资源耗尽和服务器崩溃。

因此，对于安全人员而言，利用此漏洞可以破坏僵尸网络活动，从而随后消除与僵尸网络相关的威胁。但从攻击者角度出发，该漏洞导致的恶意网络压力也会破坏数据并造成业务中断。

Mirai 僵尸网络被发现于2016年8月，因其潜在的DDoS攻击和庞大网络而多次成为头条新闻，特别是针对 IoT 设备和服务器的攻击。Mirai 拥有数千台遭到入侵的设备，并通过利用弱默认密码和已知漏洞来瞄准 IP 摄像头和家用路由器等消费类设备，其他几个变体的源代码与 Mirai相似。

**参考来源：**

> [Researchers Uncovered Remote DoS Exploit in Mirai Botnet](https://cybersecuritynews.com/dos-exploit-in-mirai-botnet/)

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