---
title: 新型僵尸网络针对 100 个国家发起 30 万次 DDoS 攻击
url: https://www.freebuf.com/news/412218.html
source: FreeBuf网络安全行业门户
date: 2024-10-09
fetch_date: 2025-10-06T18:53:46.318668
---

# 新型僵尸网络针对 100 个国家发起 30 万次 DDoS 攻击

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

新型僵尸网络针对 100 个国家发起 30 万次 DDoS 攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型僵尸网络针对 100 个国家发起 30 万次 DDoS 攻击

2024-10-08 10:02:17

所属地 上海

![](https://image.3001.net/images/20241008/1728354264_670497d82690be10aa63a.png!small)

近日，网络安全研究人员发现了一个名为 Gorilla（又名 GorillaBot）的新僵尸网络恶意软件家族，它是已泄露的 Mirai 僵尸网络源代码的变种。

网络安全公司 NSFOCUS 在上个月发现了这一活动，并称该僵尸网络在今年 9 月 4 日至 9 月 27 日期间发布了 30 多万条攻击命令，攻击密度之高令人震惊。据悉，该僵尸网络平均每天会发出不少于 2万条分布式拒绝服务（DDoS）攻击的命令。

该僵尸网络以 100 多个国家为目标，攻击大学、政府网站、电信、银行、游戏和赌博部门。美国、加拿大和德国等多个国家为主要攻击目标。

据介绍，Gorilla 主要使用 UDP flood、ACK BYPASS flood、Valve Source Engine (VSE) flood、SYN flood 和 ACK flood 进行 DDoS 攻击。同时，UDP 协议的无连接特性允许任意源 IP 欺骗以产生大量流量。

除了支持 ARM、MIPS、x86\_64 和 x86 等多种 CPU 架构外，僵尸网络还具备与五个预定义命令与控制（C2）服务器之一连接的功能，以等待 DDoS 命令。

有趣的是，该恶意软件还嵌入了利用 Apache Hadoop YARN RPC 安全漏洞实现远程代码执行的功能。值得注意的是，据阿里云和趋势科技称，该缺陷早在 2021 年就已在野外被滥用。

通过在“/etc/systemd/system/”目录下创建名为custom.service的服务文件，并将其配置为每次系统启动时自动运行，就可以在主机上实现持久化。

该服务负责从远程服务器（“pen.gorillafirewall[.]su”）下载并执行 shell 脚本（“lol.sh”）。类似的命令还被添加到“/etc/inittab”、“/etc/profile ”和“/boot/bootcmd ”文件中，以便在系统启动或用户登录时下载并运行 shell 脚本。

NSFOCUS 表示：该僵尸网络引入了多种 DDoS 攻击方法，并使用了 Keksec 组织常用的加密算法来隐藏关键信息，同时采用多种技术来保持对物联网设备和云主机的长期控制，作为一个新兴僵尸网络家族其展现出了高度的反侦测意识。

> 参考来源：[New Gorilla Botnet Launches Over 300,000 DDoS Attacks Across 100 Countries](https://thehackernews.com/2024/10/new-gorilla-botnet-launches-over-300000.html)

# 安全漏洞 # 僵尸网络

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