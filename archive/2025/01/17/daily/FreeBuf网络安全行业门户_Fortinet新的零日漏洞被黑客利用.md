---
title: Fortinet新的零日漏洞被黑客利用
url: https://www.freebuf.com/news/419968.html
source: FreeBuf网络安全行业门户
date: 2025-01-17
fetch_date: 2025-10-06T20:10:20.739548
---

# Fortinet新的零日漏洞被黑客利用

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

Fortinet新的零日漏洞被黑客利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Fortinet新的零日漏洞被黑客利用

2025-01-16 10:51:31

所属地 上海

## Fortinet修复了多个严重漏洞，其中包含一个自2024年11月起就在野外被利用的零日漏洞。

周二，Fortinet发布了十多份新的安全公告，阐述了近期在其产品里发现的严重和高危漏洞，其中就有那个自2024年11月起已在野外被利用的零日漏洞。

![](https://image.3001.net/images/20250116/1736995884_6788742cafa8bf960a12d.jpg!small)

这个零日漏洞被标记为CVE - 2024 - 55591，Fortinet称其是影响FortiOS和FortiProxy的严重漏洞。远程攻击者能够通过向Node.js websocket模块发送特制请求来获取超级管理员权限。

Fortinet表示，CVE - 2024 - 55591影响以下版本：
- FortiOS的7.0.0至7.0.16版本；
- FortiProxy的7.2.0至7.2.12版本；
- FortiProxy的7.0.0至7.0.19版本。

而修复补丁包含在以下版本中：
- FortiOS的7.0.17版本；
- FortiProxy的7.2.13版本；
- FortiProxy的7.0.20版本。

Fortinet已经确认该漏洞在野外被利用，并且在公告里提供了入侵指标（IoCs），以助力防御者检测攻击。

上周，网络安全公司Arctic Wolf发出警告，称观察到针对Fortinet FortiGate防火墙的攻击活动，这些防火墙的管理界面暴露在互联网上，这引发了关于潜在零日漏洞的新闻报道。

Arctic Wolf称：“这种攻击活动涉及对防火墙管理界面的未授权管理员登录、创建新账户、利用这些账户进行SSL VPN认证以及其他各种配置更改。”并且补充道：“虽然最初的攻击途径还没有完全确定，但零日漏洞的可能性极大。”

虽然Fortinet的公告未提及Arctic Wolf，但两家公司共有的入侵指标表明，CVE - 2024 - 55591正是Arctic Wolf在攻击中观察到的零日漏洞。Arctic Wolf在12月中旬向Fortinet通报了这些攻击，Fortinet表示已经知晓并且正在调查相关活动。

Arctic Wolf在2024年11月和12月追踪了这个攻击活动，先是观察到漏洞扫描，接着是侦察、建立SSL VPN访问以及在受感染系统上的横向移动。

Arctic Wolf报告称，攻击者只是对少数组织进行了机会性利用，不过攻击者的目标还不明确。

Fortinet在周二还修复了另一个严重漏洞CVE - 2023 - 37936，这是FortiSwitch中的一个硬编码加密密钥问题，可能让远程未认证攻击者通过恶意加密请求执行代码。

1月14日发布的13份公告涉及影响FortiManager、FortiAnalyzer、FortiClient、FortiOS、FortiRecorder、FortiProxy、FortiSASE、FortiVoice、FortiWeb和FortiSwitch等产品的高危漏洞。

这些安全漏洞可能被利用来实现账户删除后的持久性、任意文件写入、经过认证的代码和命令执行、暴力破解攻击、未经认证提取配置数据以及造成拒绝服务（DoS）状态。

Fortinet尚未将这些漏洞中的任何一个标记为已被利用，但指出其中一个漏洞是由WatchTowr披露的。

威胁行为者针对Fortinet产品漏洞发动攻击并不罕见，所以组织不应忽视最新一轮安全漏洞的修补或者缓解措施。

参考来源：<https://www.securityweek.com/fortinet-confirms-new-zero-day-exploitation/>

# 漏洞 # 安全漏洞 # 漏洞分析

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

Fortinet修复了多个严重漏洞，其中包含一个自2024年11月起就在野外被利用的零日漏洞。

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