---
title: 思科爆出严重漏洞，更新补丁明年一月才能发布！
url: https://www.freebuf.com/news/352199.html
source: FreeBuf网络安全行业门户
date: 2022-12-13
fetch_date: 2025-10-04T01:18:57.516989
---

# 思科爆出严重漏洞，更新补丁明年一月才能发布！

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

思科爆出严重漏洞，更新补丁明年一月才能发布！

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

思科爆出严重漏洞，更新补丁明年一月才能发布！

2022-12-12 11:51:00

所属地 上海

The Hacker News 网站披露，近日思科发布了新的安全公告，指出 IP 电话（网络电话） 7800 和 8800 系列某个固件中存在高危漏洞，一旦攻击者成功利用该漏洞，或引发远程代码执行或拒绝服务（DoS）情况。![1670817080_6396a5383e014599acfc7.jpg!small?1670817079987](https://image.3001.net/images/20221212/1670817080_6396a5383e014599acfc7.jpg!small?1670817079987)

漏洞被追踪为 CVE-2022-20968（CVSS 评分：8.1），由 Qianxin Group Legendsec Codesafe 团队的 Qian Chen 发现并报告。据悉，漏洞产生的原因是在收到 Cisco 发现协议（CDP）数据包时，存在输入验证不足的情况，思科目前正在积极开发新补丁来解决漏洞问题。

注：通过运行 CDP 协议，思科设备能够在与它们直连的设备之间分享有关操作系统软件版本，以及 IP 地址，硬件平台等相关信息。（默认情况下自动开启。）

## ****漏洞最早要明年一月才能修复****

2022 年 12 月 8 日，Cisco 在一份公告中表示，潜在攻击者可以通过向受影响设备发送“精心制作”的思科发现协议流量来利用这一漏洞，若成功利用漏洞，潜在攻击者能够造成堆栈溢出，导致受影响设备上可能出现远程代码执行或拒绝服务（DoS）的情况。

值得一提的是，漏洞主要影响运行固件版本 14.2 及更早版本的Cisco IP 电话，思科方面声称目前暂时没有更新补丁和解决方案来解决该问题，但公司正在加紧开发更新补丁，计划在 2023 年 1 月发布。

![](https://image.3001.net/images/20221212/1670817176_6396a5983d76d44e8fd63.jpeg!small)此外，在同时支持 CDP 和链路层发现协议（LLDP）用于邻居发现的部署中，用户可以选择禁用 CDP，以便受影响的设备能够切换到 LLDP，向局域网（LAN）中直连的对等设备公布其身份和能力。这种变化可能会带来其它安全风险，需要企业努力评估设备可能会受到的任何潜在影响。

最后，思科强调，CVE-2022-20968 漏洞虽已被公开披露，但迄今为止，没有证据表明该漏洞在野外被积极滥用。

**文章来源：**

> thehackernews.com/2022/12/cisco-warns-of-high-severity-unpatched.html

# 漏洞利用

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

漏洞最早要明年一月才能修复

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