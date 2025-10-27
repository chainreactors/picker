---
title: 警惕！新的ShellBot DDoS 恶意软件正针对 Linux SSH服务器
url: https://www.freebuf.com/news/361255.html
source: FreeBuf网络安全行业门户
date: 2023-03-23
fetch_date: 2025-10-04T10:22:59.650823
---

# 警惕！新的ShellBot DDoS 恶意软件正针对 Linux SSH服务器

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

警惕！新的ShellBot DDoS 恶意软件正针对 Linux SSH服务器

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

警惕！新的ShellBot DDoS 恶意软件正针对 Linux SSH服务器

2023-03-22 10:59:52

所属地 上海

![](https://image.3001.net/images/20230322/1679452635_641a69db2516201421c7b.png!small)

AhnLab安全应急响应中心（ASEC）发现了ShellBot恶意软件的一种新变种，该变种被用于针对Linux SSH服务器。

ShellBot，也称为PerlBot，是一个基于Perl的DDoS机器人，使用IRC协议进行C2通信。

ShellBot 对打开端口 22 的服务器执行 SSH 暴力攻击，它使用包含已知 SSH 凭据列表的字典。

ShellBot恶意软件是攻击者在目标系统上使用扫描仪和SSH暴力破解恶意软件获得的帐户凭据之后安装的。在扫描具有可操作端口 22 的系统后，攻击者会搜索 SSH 服务处于活动状态的系统，并使用常用的 SSH 帐户凭据列表来发起字典攻击。

以下是 ShellBot 操作员用于危害目标服务器的帐户凭据列表：

| USER | PASSWORD |
| --- | --- |
| deploy | password |
| hadoop | hadoop |
| oracle | oracle |
| root | 11111 |
| root | Passw0rd |
| ttx | ttx2011 |
| ubnt | ubnt |

研究人员将ShellBot分为三个不同的组，因为攻击者可以创建自己的版本：LiGhT的Modded perlbot v2，DDoS PBot v2.0和PowerBots（C）GohacK。

LiGhT 的 Modded perlbot v2 和 DDoS PBot v2.0 支持使用 HTTP、TCP 和 UDP 协议的多个 DDoS 攻击命令。PowerBots （C） GohacK支持后门功能，包括反向shell和文件下载功能。

此外，威胁行为者可以使用各种其他后门功能来安装其他恶意软件或从受感染的服务器发起不同类型的攻击。

研究人员建议为管理员帐户使用强密码，并定期更改它们，以保护Linux服务器免受暴力攻击和字典攻击。他们还建议使服务器保持最新状态并使用安全程序。

参考链接：thehackernews.com/2023/03/new-shellbot-ddos-malware-targeting.html

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