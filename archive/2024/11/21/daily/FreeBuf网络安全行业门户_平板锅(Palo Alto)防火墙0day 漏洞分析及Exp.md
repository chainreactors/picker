---
title: 平板锅(Palo Alto)防火墙0day 漏洞分析及Exp
url: https://www.freebuf.com/news/415767.html
source: FreeBuf网络安全行业门户
date: 2024-11-21
fetch_date: 2025-10-06T19:15:38.278339
---

# 平板锅(Palo Alto)防火墙0day 漏洞分析及Exp

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

平板锅(Palo Alto)防火墙0day 漏洞分析及Exp

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

平板锅(Palo Alto)防火墙0day 漏洞分析及Exp

2024-11-20 19:49:18

所属地 上海

watchTowr的研究人员Sonny近期发布了一份技术分析报告，深入剖析了影响Palo Alto Networks下一代防火墙(NGFW)的两个零日漏洞。这两个漏洞编号为CVE-2024-0012和CVE-2024-9474，已引起包括美国网络安全和基础设施安全局(CISA)在内的多个网络安全机构的高度关注。CISA已将其列入已知漏洞目录，并要求联邦机构必须在12月9日前完成修复。![](https://image.3001.net/images/20241120/1732103295_673dcc7f1a6a69d8404d1.png!small)

CVE-2024-0012是PAN-OS管理Web界面中的一个认证绕过漏洞。根据Sonny的分析，该漏洞允许远程攻击者在无需认证的情况下获得管理员权限。研究人员详细说明了他们的分析方法，从仔细审查Nginx配置文件开始。

Sonny在分析报告中指出："查看主要的Nginx路由配置文件`/etc/nginx/conf/locations.conf`时，发现了一处看似很小但影响巨大的变更。"

![](https://image.3001.net/images/20241120/1732103346_673dccb20d83f21d11723.png!small)研究人员发现，在未打补丁的版本中，X-PAN-AUTHCHECK头部设置存在缺陷，这可能导致未经授权的用户访问本应受保护的端点。

通过利用这个疏忽，研究人员找到了一个简单但破坏力极强的绕过方法：只需将X-PAN-AUTHCHECK HTTP头部设置为off，就能完全禁用认证机制。

第二个漏洞CVE-2024-9474则允许恶意的PAN-OS管理员提升权限，以root身份执行命令。该漏洞存在于AuditLog.php文件中，由于用户输入未经proper过滤，导致可能遭受命令注入攻击。

研究人员在负责写入审计日志的函数中发现了一处关键性更改。Sonny演示了如何利用这个漏洞提升权限，他表示："用户竟然可以传入包含shell元字符的用户名到`AuditLog.write()`函数中，这些字符随后会被传递给pexecute()函数。"

Sonny敦促管理员们迅速采取行动，并指出这个漏洞利用链的简单性："这两个漏洞能够出现在生产环境的设备中着实令人吃惊，更让人惊讶的是它们是通过Palo Alto设备底层那堆杂乱的shell脚本调用实现的。"

为了给管理员留出打补丁的时间，watchTowr暂时没有公布完整的概念验证利用代码，但他们提供了一个Nuclei模板用于检测系统是否存在漏洞。

另一方面，安全研究员Valentin Lobstein已经开发并发布了CVE-2024-0012和CVE-2024-9474的PoC利用代码，使得漏洞利用变得极其简单。基于watchTowr的分析，Lobstein开发的Go语言工具实现了攻击过程的自动化，用户只需输入目标URL即可。这个现成的利用工具增加了遭受攻击的风险，也凸显了及时修补易受攻击系统的紧迫性。

Palo Alto Networks已在PAN-OS 10.2.12-h2版本中修复了这些漏洞。

watchTowr详细分析：<https://labs.watchtowr.com/pots-and-pans-aka-an-sslvpn-palo-alto-pan-os-cve-2024-0012-and-cve-2024-9474/>

nuclei检测模板：<https://github.com/watchtowrlabs/palo-alto-panos-cve-2024-0012>

Exp利用代码：<https://github.com/Chocapikk/CVE-2024-9474>

请合法合规使用，任何乱用与本公众号无关，本公众号出于研究学习目的分享。

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