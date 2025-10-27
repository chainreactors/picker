---
title: 新的 &quot;HinataBot &quot;僵尸网络可以发动大规模的 DDoS攻击
url: https://www.freebuf.com/news/361013.html
source: FreeBuf网络安全行业门户
date: 2023-03-21
fetch_date: 2025-10-04T10:09:12.737379
---

# 新的 &quot;HinataBot &quot;僵尸网络可以发动大规模的 DDoS攻击

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

新的 &ampquotHinataBot &ampquot僵尸网络可以发动大规模的 DDoS攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新的 "HinataBot "僵尸网络可以发动大规模的 DDoS攻击

2023-03-20 14:24:09

所属地 上海

![](https://image.3001.net/images/20230320/1679290518_6417f096732839699dfdb.png!small)

一个新的恶意僵尸网络被发现，它以Realtek SDK、华为路由器和Hadoop YARN服务器为目标，将设备引入到DDoS（分布式拒绝服务）群中，有可能进行大规模攻击。

这个新的僵尸网络是Akamai的研究人员今年年初在自己的HTTP和SSH蜜罐上发现的，该僵尸网络利用了CVE-2014-8361和CVE-2017-17215等漏洞。

Akamai说，HinataBot的操作者最初分发Mirai二进制文件，而HinataBot首次出现在2023年1月中旬。它以Mirai为基础，是基于Go的变体。

## 显著的DDoS能力

该恶意软件通过对SSH端点进行暴力攻击或使用已知漏洞的感染脚本和RCE有效载荷进行分发。感染设备后，恶意软件会默默地运行，等待来自命令和控制服务器的命令执行。

HinataBot的旧版本支持HTTP、UDP、ICMP和TCP洪水，但较新的变体只具有前两种。然而，即使只有两种攻击模式，该僵尸网络也可以潜在地进行非常强大的分布式拒绝服务攻击。

![](https://image.3001.net/images/20230320/1679290630_6417f10613da7ab6928ba.png!small)

攻击函数

虽然 HTTP 和 UDP 攻击命令不同，但它们都创建了一个包含 512 个工作线程（进程）的工作线程池，这些工作线程在自定义的持续时间内向目标发送硬编码数据包。

HTTP数据包的大小在484和589字节之间。而HinataBot产生的UDP数据包则特别大（65,549字节），由大量的空字节组成。

![](https://image.3001.net/images/20230320/1679290668_6417f12cbb4d0cc0df4da.png!small)

UDP泛滥数据包捕获

HTTP产生大量的网站请求，而UDP则向目标发送大量的垃圾流量；攻击者通过两种不同的方法来实现断网。

Akamai对僵尸网络的HTTP和UDP的10秒攻击进行了基准测试，在HTTP攻击中，恶意软件产生了20,430个请求，总大小为3.4MB。UDP产生了6733个包，总大小为421MB。

研究人员估计，如果有1000个节点，UDP可以产生大约336Gbps，而在10000个节点，攻击数据量将达到3.3Tbps。

在HTTP洪的情况下，1000个被捕获的设备将产生每秒2000000个请求，而10000个节点将采取这个数字的20400000 rps和27 Gbps。

目前，HinataBot仍在不断开发中，随时可能实施更多的漏洞并扩大其目标范围。

> 参考链接：www.bleepingcomputer.com/news/security/new-hinatabot-botnet-could-launch-massive-33-tbps-ddos-attacks/

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

显著的DDoS能力

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