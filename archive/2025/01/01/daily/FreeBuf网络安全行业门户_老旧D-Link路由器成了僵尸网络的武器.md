---
title: 老旧D-Link路由器成了僵尸网络的武器
url: https://www.freebuf.com/news/418839.html
source: FreeBuf网络安全行业门户
date: 2025-01-01
fetch_date: 2025-10-06T20:07:00.335497
---

# 老旧D-Link路由器成了僵尸网络的武器

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

老旧D-Link路由器成了僵尸网络的武器

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

老旧D-Link路由器成了僵尸网络的武器

2024-12-31 14:43:57

所属地 上海

近期，两个名为“Ficora”和“Capsaicin”的僵尸网络在针对已停产或运行过时固件版本的D-Link路由器的攻击活动中表现活跃。受影响的设备包括个人和组织常用的D-Link型号，如DIR-645、DIR-806、GO-RT-AC750和DIR-845L。

![](https://image.3001.net/images/20241231/1735627195_677391bb9b4137064f68a.png!small)

这两个恶意软件利用已知的漏洞进行初始入侵，其中包括CVE-2015-2051、CVE-2019-10891、CVE-2022-37056和CVE-2024-33112。一旦设备被攻破，攻击者会利用D-Link管理接口（HNAP）中的弱点，通过GetDeviceSettings操作执行恶意命令。

这些僵尸网络具备窃取数据和执行Shell脚本的能力。攻击者似乎利用这些设备进行分布式拒绝服务（DDoS）攻击。

Ficora是Mirai僵尸网络的一个新变种，专门针对D-Link设备的漏洞。根据Fortinet的遥测数据，该僵尸网络在10月和11月期间活动显著增加，表现出随机攻击的特点。

![](https://image.3001.net/images/20241231/1735627315_67739233b2ac656ce311a.png!small)

感染过程

Ficora在获得D-Link设备的初始访问权限后，会使用名为“multi”的Shell脚本，通过多种方法（如wget、curl、ftpget和tftp）下载并执行其有效载荷。该恶意软件包含一个内置的暴力破解组件，使用硬编码的凭据感染其他基于Linux的设备，并支持多种硬件架构。

Ficora支持UDP洪水攻击、TCP洪水攻击和DNS放大攻击，以最大化其攻击威力。

![](https://image.3001.net/images/20241231/1735627349_67739255f215f7e23ac4b.png!small)

Capsaicin是Kaiten僵尸网络的一个变种，被认为是Keksec组织开发的恶意软件，该组织以“EnemyBot”和其他针对Linux设备的恶意软件家族而闻名。Fortinet仅在10月21日至22日期间观察到其爆发性攻击，主要针对东亚国家。

![](https://image.3001.net/images/20241231/1735627433_677392a9b89b738de85cd.png!small)

Capsaicin的感染通过一个下载脚本（“bins.sh”）进行，该脚本获取不同架构的二进制文件（前缀为“yakuza”），包括arm、mips、sparc和x86。该恶意软件会主动查找并禁用同一主机上其他活跃的僵尸网络有效载荷。

除了与Ficora相似的DDoS能力外，Capsaicin还可以收集主机信息并将其外泄到命令与控制（C2）服务器以进行跟踪。

![](https://image.3001.net/images/20241231/1735627416_67739298b5ed0e173c849.png!small)

防止路由器和物联网设备感染僵尸网络恶意软件的一种方法是确保它们运行最新的固件版本，以修复已知漏洞。如果设备已停产且不再接收安全更新，则应更换为新设备。

参考来源：<https://www.bleepingcomputer.com/news/security/malware-botnets-exploit-outdated-d-link-routers-in-recent-attacks/>

# 系统安全

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