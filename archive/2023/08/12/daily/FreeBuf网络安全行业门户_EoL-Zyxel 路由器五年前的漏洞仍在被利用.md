---
title: EoL-Zyxel 路由器五年前的漏洞仍在被利用
url: https://www.freebuf.com/news/374532.html
source: FreeBuf网络安全行业门户
date: 2023-08-12
fetch_date: 2025-10-04T12:01:47.235202
---

# EoL-Zyxel 路由器五年前的漏洞仍在被利用

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

EoL-Zyxel 路由器五年前的漏洞仍在被利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

EoL-Zyxel 路由器五年前的漏洞仍在被利用

2023-08-11 10:44:58

所属地 上海

Bleeping Computer 网站消息，Gafgyt 恶意软件正积极利用 Zyxel P660HN-T1A 路由器五年前曝出的漏洞，每天发动数千次网络攻击活动。据悉，漏洞被追踪为 CVE-2017-18368，是路由器设备远程系统日志转发功能中存在的严重性未验证命令注入漏洞（CVSS v3：9.8），Zyxel 已于 2017 年修补了该漏洞。![1691721866_64d5a08af1f1d14a2421a.png!small](https://image.3001.net/images/20230811/1691721866_64d5a08af1f1d14a2421a.png!small)

早在 2019 年，Zyxel 就强调当时的新变种 Gafgyt 可能会利用该漏洞发动网络攻击，敦促仍在使用旧固件版本的用户尽快升级到最新版本，以保护其设备免遭接管。然而自 2023 年 7 月初以来，Fortinet 仍能够监测到平均每天 7100 次的攻击活动，且攻击数量持续至今。

Fortinet 发布警报表示截止到 2023 年 8 月 7 日，FortiGuard 实验室持续监测到利用 CVE-2017-18368 漏洞的攻击活动，并在过去一个月中阻止了超过数千个独特 IPS 设备的攻击企图。

![1691721876_64d5a094b3c06f786d645.png!small](https://image.3001.net/images/20230811/1691721876_64d5a094b3c06f786d645.png!small)

试图利用 Zyxel 路由器中的 CVE-2017-18368 漏洞（来源：Fortinet ）

Fortinet 指出虽然目前还尚不清楚观察到的攻击活动中有哪一部分成功感染了设备，但自 7 月份以来，攻击活动一直保持稳定。值得一提的是，CISA 近期发布了 CVE-2017-18368 在野外被利用的情况，并将该漏洞添加到其已知利用漏洞目录中，要求联邦机构在 2023 年 8 月 28 日前修补 Zyxel 漏洞。

为应对漏洞利用的爆发，Zyxel 又更新了安全公告，提醒客户 CVE-2017-18363 只影响运行 7.3.15.0 v001/3.40(ULM.0)b31 或更旧固件版本的设备，运行 2017 年为修复漏洞而推出的最新固件版本 3.40(BYF.11) 的 P660HN-T1A 路由器不受影响。

此外，Zyxel 表示 P660HN-T1A 在几年前就已达到报废年限。因此，强烈建议用户将其更换为更新一代的产品，以获得最佳保护。

路由器感染恶意软件常见迹象包括连接不稳定、设备过热、配置突然改变、反应迟钝、非典型网络流量、开放新端口和意外重启，如果怀疑自己的设备受到网络恶意软件的攻击，用户可以执行出厂重置，将设备固件更新到最新版本，更改默认的管理员用户凭据，并禁用远程管理面板，只从内部网络管理设备。

**文章来源：**

> https://www.bleepingcomputer.com/news/security/gafgyt-malware-exploits-five-years-old-flaw-in-eol-zyxel-router/#google\_vignette

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