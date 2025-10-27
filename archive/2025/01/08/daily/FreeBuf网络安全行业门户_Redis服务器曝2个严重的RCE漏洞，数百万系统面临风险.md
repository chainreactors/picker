---
title: Redis服务器曝2个严重的RCE漏洞，数百万系统面临风险
url: https://www.freebuf.com/news/419216.html
source: FreeBuf网络安全行业门户
date: 2025-01-08
fetch_date: 2025-10-06T20:10:05.874396
---

# Redis服务器曝2个严重的RCE漏洞，数百万系统面临风险

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

Redis服务器曝2个严重的RCE漏洞，数百万系统面临风险

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Redis服务器曝2个严重的RCE漏洞，数百万系统面临风险

2025-01-07 15:55:35

所属地 上海

在广泛使用的内存数据库Redis里，发现了两个严重漏洞，这可能使数百万系统面临拒绝服务（DoS）攻击和远程代码执行（RCE）的风险。这些漏洞被标记为CVE - 2024 - 51741和CVE - 2024 - 46981，这凸显了Redis用户面临着重大的安全风险，也强调了及时更新和采取缓解措施的重要性。

![](https://image.3001.net/images/20250107/1736237012_677cdfd4da81961012752.jpg!small)

### 一、CVE - 2024 - 51741：畸形ACL选择器引发的拒绝服务

CVE - 2024 - 51741这个漏洞影响Redis 7.0.0及以上版本。拥有足够权限的认证用户能够创建一个畸形的访问控制列表（ACL）选择器。

当访问这个畸形选择器时，服务器就会崩溃，从而进入拒绝服务状态。该问题已在Redis 7.2.7和7.4.2版本中得到修复。

Redis用户应马上升级到这些修复后的版本，从而保护自己的系统免受可能的利用。此漏洞是由Axel Mierczuk报告的，他为发现这个漏洞做出了贡献。

### 二、CVE - 2024 - 46981：Lua脚本执行远程代码

CVE - 2024 - 46981这个漏洞带来的威胁更大，因为它可能导致远程代码执行。这个问题是由于Redis中Lua脚本功能被滥用而产生的。认证过的攻击者能够编写恶意的Lua脚本来操纵垃圾收集器，进而可能在服务器上执行任意代码。

这个漏洞影响所有开启了Lua脚本功能的Redis版本。针对Redis 6.2.x、7.2.x和7.4.x版本已经发布了修补程序。对于那些不能马上更新的用户，建议通过修改ACL规则来限制“EVAL”和“EVALSHA”命令，从而禁用Lua脚本作为额外的防范措施。

### 三、建议措施

**1. 升级Redis**

用户应该把安装更新到已修复漏洞的版本，即针对CVE - 2024 - 51741的7.2.7或7.4.2版本，以及针对CVE - 2024 - 46981的最新版本。

**2. 限制Lua脚本**

作为针对CVE - 2024 - 46981的临时解决办法，通过修改ACL规则阻止“EVAL”和“EVALSHA”命令来禁用Lua脚本。

**3. 监控访问控制**

要确保只有受信任的用户才能在Redis服务器上执行特权命令。这些漏洞表明在管理数据库系统时实施强大安全策略是非常关键的。强烈建议Redis用户立即行动起来，减轻风险，保护自己的环境免受潜在的利用。

参考来源：<https://cybersecuritynews.com/redis-server-vulnerabilities/>

# 漏洞 # 安全漏洞

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