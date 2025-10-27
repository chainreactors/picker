---
title: Mirai 恶意软件新变种感染 Linux 设备，以期构建 DDoS 僵尸网络
url: https://www.freebuf.com/articles/357881.html
source: FreeBuf网络安全行业门户
date: 2023-02-18
fetch_date: 2025-10-04T07:23:10.449403
---

# Mirai 恶意软件新变种感染 Linux 设备，以期构建 DDoS 僵尸网络

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

Mirai 恶意软件新变种感染 Linux 设备，以期构建 DDoS 僵尸网络

* ![]()
* 关注

Mirai 恶意软件新变种感染 Linux 设备，以期构建 DDoS 僵尸网络

2023-02-17 13:59:27

所属地 上海

Bleeping Computer 网站披露，一个被追踪为“V3G4”的 Mirai 恶意软件新变种异常活跃，正在利用基于 Linux 服务器和物联网设备中的 13 个漏洞，展开 DDoS（分布式拒绝服务）攻击。![1676613581_63ef17cdc446d46fa8a59.png!small](https://image.3001.net/images/20230217/1676613581_63ef17cdc446d46fa8a59.png!small)

据悉，Mirai 恶意软件主要通过暴力破解 telnet/SSH 凭证或利用硬编码缺陷，在目标设备上执行远程代码进行传播，一旦攻破目标设备防御系统，立刻感染设备并将其招募到自身僵尸网络中。

2022 年 7 月至 2022 年 12 月，Palo Alto Networks（Unit 42）研究员在三个不同网络攻击活动中发现了“V3G4”恶意软件。经详细分析，研究员发现硬编码的 C2 域包含相同字符串，shell 脚本也类似，并且所有攻击中使用的僵尸网络客户端具有相同功能，基于此，Unit 42 推测这三个攻击都来自同一网络犯罪分子。

此外，安全研究员指出“V3G4”的攻击活动从利用以下 13 个漏洞开始：

> CVE-2012-4869: FreePBX Elastix remote command execution
>
> Gitorious remote command execution
>
> CVE-2014-9727: FRITZ!Box Webcam remote command execution
>
> Mitel AWC remote command execution
>
> CVE-2017-5173: Geutebruck IP Cameras remote command execution
>
> CVE-2019-15107: Webmin command injection
>
> Spree Commerce arbitrary command execution
>
> FLIR Thermal Camera remote command execution
>
> CVE-2020-8515: DrayTek Vigor remote command execution
>
> CVE-2020-15415: DrayTek Vigor remote command execution
>
> CVE-2022-36267: Airspan AirSpot remote command execution
>
> CVE-2022-26134: Atlassian Confluence remote command execution
>
> CVE-2022-4257: C-Data Web Management System command injection

![1676613605_63ef17e568e3fc5bef483.png!small](https://image.3001.net/images/20230217/1676613605_63ef17e568e3fc5bef483.png!small)

V3G4 利用的安全漏洞

一旦成功入侵目标设备，基于 Mirai 恶意软件的有效载荷便立即投放到系统中，并开始尝试连接硬编码的C2 地址。此外，“V3G4 ”还试图终止硬编码列表中其它竞争性僵尸网络恶意软件家族的感染进程。  ![1676613620_63ef17f4698ca2a400e5b.png!small](https://image.3001.net/images/20230217/1676613620_63ef17f4698ca2a400e5b.png!small)

试图停止“竞争者”进程

值得注意的是，不同于其它大多数 Mirai 恶意软件变种仅仅使用一个 OXR 加密密钥，“V3G4”使用四个不同的 XOR 加密密钥，这样使得对恶意软件代码的逆向工程和对其功能解码更具挑战性。

当“V3G4”传播到其它目标设备时，DDoS 僵尸网络使用 telnet/SSH 暴力程序，试图使用默认或弱凭据进行连接。最后，被攻击设备直接从 C2 发出包括 TCP、UDP、SYN 和 HTTP 泛滥方法等在内的 DDoS 命令。![1676613637_63ef1805d7d8e0f4bbb83.png!small](https://image.3001.net/images/20230217/1676613637_63ef1805d7d8e0f4bbb83.png!small)

DDoS 命令

安全研究人员指出，新变种“V3G4”很可能向希望对特定网站或在线服务发动网络攻击的客户出售 DDoS 服务。

值得一提的是，虽然目前没有迹象表明变体“V3G4”与某个网络攻击服务联系起来，但为了更好的确保设备免受类似 Mirai 恶意软件感染，用户应及时改变默认密码并安装安全更新。

**文章来源：**

> https://www.bleepingcomputer.com/news/security/new-mirai-malware-variant-infects-linux-devices-to-build-ddos-botnet/

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