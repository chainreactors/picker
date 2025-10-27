---
title: I-O Data路由器0Day漏洞被利用，无修复补丁
url: https://www.freebuf.com/news/417010.html
source: FreeBuf网络安全行业门户
date: 2024-12-07
fetch_date: 2025-10-06T19:39:32.057679
---

# I-O Data路由器0Day漏洞被利用，无修复补丁

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

I-O Data路由器0Day漏洞被利用，无修复补丁

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

I-O Data路由器0Day漏洞被利用，无修复补丁

2024-12-06 10:48:56

所属地 上海

日本计算机紧急响应小组（CERT）警告称 ，黑客正在利用I-O Data路由器设备中的零日漏洞来修改设备设置、执行命令，甚至关闭防火墙。

I-O Data在其网站上发布的安全公告中承认确实存在三个零日漏洞，但目前暂无完整的修复补丁，预计将在2024年12月18日发布，因此在此之前用户将面临比较严重的风险。![](https://image.3001.net/images/20241206/1733465818_675296daa225460d24332.png!small)

上述三个零日漏洞在2024年11月13日被发现，包括信息泄露、远程任意操作系统命令执行和导致防火墙禁用的漏洞。

具体如下：

* CVE-2024-45841：敏感资源上的不当权限配置，导致低权限用户可以访问关键文件。
* CVE-2024-47133：认证的管理员用户可以在设备上注入并执行任意操作系统命令，利用配置管理中的输入验证不充分漏洞。
* CVE-2024-52464：固件中的未记录特性或后门可导致远程攻击者在无需认证的情况下，关闭设备防火墙并修改设置。

**受影响的设备**：这些漏洞影响UD-LT1和UD-LT1/EX设备，前者是为多功能连接解决方案设计的混合LTE路由器，而后者是工业级版本。

最新可用的固件版本v2.1.9仅解决了CVE-2024-52564漏洞，I-O Data表示其他两个漏洞的修复将在计划于2024年12月18日发布的v2.2.0版本中提供。比较糟糕的消息是，已经有客户因为这些漏洞而遭到黑客攻击。

I-O Data安全公告指出，“已收到使用混合LTE路由器UD-LT1和UD-LT1/EX的客户的咨询，这些客户报告了来自外部来源的潜在未经授权访问。”

在安全更新发布之前，I-O Data 建议用户实施以下缓解措施：

* 禁用所有互联网连接方式的远程管理功能，包括WAN端口、调制解调器和VPN设置。
* 仅限VPN连接的网络访问，以防止未经授权的外部访问。
* 将默认的“访客”用户的密码更改为超过10个字符的更复杂的密码。
* 定期监控和验证设备设置，以尽早检测未经授权的更改，并在检测到泄露时将设备重置为出厂默认设置并重新配置。

不过国内的企业用户不需要太过担心，因为I-O DATA UD-LT1和UD-LT1/EX LTE路由器主要在日本市场销售，旨在支持NTT Docomo和KDDI等多个运营商，并兼容该国的主要MVNO SIM卡。

参考来源：<https://www.bleepingcomputer.com/news/security/japan-warns-of-io-data-zero-day-router-flaws-exploited-in-attacks/>

# 系统安全 # 数据安全

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