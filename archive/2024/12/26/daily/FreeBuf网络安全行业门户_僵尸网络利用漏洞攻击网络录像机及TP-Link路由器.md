---
title: 僵尸网络利用漏洞攻击网络录像机及TP-Link路由器
url: https://www.freebuf.com/news/418486.html
source: FreeBuf网络安全行业门户
date: 2024-12-26
fetch_date: 2025-10-06T19:38:38.535098
---

# 僵尸网络利用漏洞攻击网络录像机及TP-Link路由器

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

僵尸网络利用漏洞攻击网络录像机及TP-Link路由器

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

僵尸网络利用漏洞攻击网络录像机及TP-Link路由器

2024-12-25 11:44:29

所属地 上海

据BleepingComputer消息，一个基于Mirai的新型僵尸网络正在积极利用DigiEver网络录像机中的一个远程代码执行漏洞，该漏洞尚未获得编号，也暂无修复补丁。

![](https://image.3001.net/images/20241225/1735104782_676b990ec6e4209f904ac.png!small)

Akamai 研究人员观察到，该僵尸网络于 11 月中旬开始利用该漏洞，但证据表明该活动至少自 9 月以来就一直活跃。

除了 DigiEver 漏洞外，新的 Mirai 恶意软件变体还分别利用CVE-2023-1389和 CVE-2018-17532 漏洞针对未打安全补丁的 TP-Link 和 Teltonika RUT9XX 路由器。

研究人员称，被用来攻击 DigiEver NVR 的远程代码执行 （RCE） 漏洞源自“/cgi-bin/cgi\_main. cgi”URI，该URI 未正确验证用户输入，允许未经身份验证的远程攻击者通过某些参数（如 HTTP POST 请求中的 ntp 字段）注入 "curl "和 "chmod "等命令。

通过命令注入，攻击者从外部服务器获取恶意软件二进制文件，并将设备加入其僵尸网络。 设备一旦被入侵，就会被用来进行分布式拒绝服务（DDoS）攻击，或利用漏洞集和凭证列表扩散到其他设备。

Akamai表示，新Mirai变种的显著特点是使用了XOR和ChaCha20加密技术，并以x86、ARM和MIPS等多种系统架构为目标，这不同于许多基于 Mirai 的僵尸网络仍然依赖于原始的字符串混淆逻辑，这种逻辑来自于原始 Mirai 恶意软件源代码发布时包含的回收代码。 虽然采用复杂的解密方法并不新颖，但这表明基于Mirai的僵尸网络的战术、技术和程序在不断发展。

据悉，早在去年罗马尼亚布加勒斯特举行的 DefCamp 安全会议上，TXOne 研究员 Ta-Lun Yen就曾揭露过该漏洞，该问题当时影响了多个 DVR 设备。

**参考来源：**

> [New botnet exploits vulnerabilities in NVRs, TP-Link routers](https://www.bleepingcomputer.com/news/security/new-botnet-exploits-vulnerabilities-in-nvrs-tp-link-routers/)

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