---
title: 利用 DoS 漏洞可瘫痪 Palo Alto 防火墙
url: https://www.freebuf.com/news/418739.html
source: FreeBuf网络安全行业门户
date: 2024-12-31
fetch_date: 2025-10-06T19:40:51.328434
---

# 利用 DoS 漏洞可瘫痪 Palo Alto 防火墙

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

利用 DoS 漏洞可瘫痪 Palo Alto 防火墙

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

利用 DoS 漏洞可瘫痪 Palo Alto 防火墙

2024-12-30 11:05:41

所属地 上海

Palo Alto Networks警告，称黑客正在利用CVE - 2024 - 3393拒绝服务漏洞，通过强制重启防火墙的方式，使其保护功能丧失。反复利用这一安全漏洞会让设备进入维护模式，必须手动干预才能恢复正常运行状态。![](https://image.3001.net/images/20241230/1735528040_67720e68e986b89ebeb50.png!small)

公告指出：“Palo Alto Networks PAN - OS软件中的DNS安全功能存在一个拒绝服务漏洞，未经身份验证的攻击者能够经由防火墙的数据平面发送恶意数据包，从而造成防火墙重启。”

## DoS漏洞正在被积极利用

Palo Alto Networks表示，未经身份验证的攻击者可以向受影响的设备发送特制的恶意数据包来利用此漏洞。这一问题仅出现在启用了“DNS安全”日志记录的设备上，受CVE - 2024 - 3393影响的产品版本如下：

> PAN - OS 10.1.14 - h8
> PAN - OS 10.2.10 - h12
> PAN - OS 11.1.5
> PAN - OS 11.2.3

厂商确认该漏洞正在被积极利用，并且指出客户在防火墙阻止攻击者利用该漏洞发送的恶意DNS数据包时，出现了服务中断的情况。该公司已经在PAN - OS 10.1.14 - h8、PAN - OS 10.2.10 - h12、PAN - OS 11.1.5、PAN - OS 11.2.3以及后续版本中修复了这个漏洞。

![](https://image.3001.net/images/20241230/1735528132_67720ec4db05fd7db954c.png!small)

不过需要注意的是，受CVE - 2024 - 3393影响的PAN - OS 11.0版本不会收到补丁，因为该版本已于11月17日到达其生命周期终止（EOL）日期。对于无法立即更新的用户，Palo Alto Networks还发布了缓解问题的临时措施和步骤：

对于未管理的下一代防火墙（NGFW）、由Panorama管理的NGFW或者由Panorama管理的Prisma Access：

> 1. 导航至：Objects（对象）→Security Profiles（安全配置文件）→Anti - spyware（反间谍软件）→DNS Policies（DNS策略）→DNS Security（DNS安全），针对每个反间谍配置文件进行操作。
>
> 2. 将所有已配置的DNS安全类别的日志严重性更改为“none”（无）。
>
> 3. 提交更改，并且在应用修复之后恢复日志严重性设置。

对于由Strata Cloud Manager（SCM）管理的NGFW：

* 选项1：按照上述步骤直接在每台NGFW上禁用DNS安全日志记录。
* 选项2：通过提交支持案例，在租户中的所有NGFW上禁用DNS安全日志记录。

对于由Strata Cloud Manager（SCM）管理的Prisma Access：

* 提交支持案例，以在租户中的所有NGFW上禁用DNS安全日志记录。
* 如有需要，可在支持案例中请求加快Prisma Access租户的升级。

参考来源：<https://www.bleepingcomputer.com/news/security/hackers-exploit-dos-flaw-to-disable-palo-alto-networks-firewalls/>

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

DoS漏洞正在被积极利用

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