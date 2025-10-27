---
title: LiteSpeed 曝出严重漏洞，致使超 600 万 WordPress 网站遭攻击
url: https://www.freebuf.com/news/410350.html
source: FreeBuf网络安全行业门户
date: 2024-09-07
fetch_date: 2025-10-06T18:28:10.273516
---

# LiteSpeed 曝出严重漏洞，致使超 600 万 WordPress 网站遭攻击

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

LiteSpeed 曝出严重漏洞，致使超 600 万 WordPress 网站遭攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

LiteSpeed 曝出严重漏洞，致使超 600 万 WordPress 网站遭攻击

2024-09-06 09:26:55

所属地 上海

![WordPress](https://image.3001.net/images/20240906/1725587149_66da5ecdb06dfe0e2d22b.jpg!small)

近日，Patchstack 的 Rafie Muhammad 在 LiteSpeed Cache 插件中发现了一个严重漏洞，该插件主要用于加快超 600 万个 WordPress 网站的用户浏览速度。该漏洞被追踪为 CVE-2024-44000，并被归类为未经身份验证的帐户接管问题 。随着 LiteSpeed Cache 6.5.0.1 版本的发布，修复程序也于昨天（9月4日）发布。

## 调试功能将 cookie 写入文件

该漏洞与插件的调试日志功能有关，当启用该功能时，它会将所有 HTTP 响应头（包括 “Set-Cookie ”头）记录到文件中。

这些标头包含用于验证用户身份的会话 cookie，一旦攻击者成功窃取这些 cookie，就可以冒充管理员用户完全控制网站。

要利用该漏洞，攻击者必须能够访问“/wp-content/debug.log ”中的调试日志文件。在未实施文件访问限制（如 .htaccess 规则）的情况下，只需输入正确的 URL 即可。

当然，攻击者只能窃取在调试功能激活时登录网站的用户的会话 cookie，但如果日志被无限期保存而不是定期清除，这甚至包括过去的登录事件。

该插件的供应商 LiteSpeed Technologies 通过将调试日志移至专用文件夹（'/wp-content/litespeed/debug/'）、随机化日志文件名、移除记录 Cookie 的选项，以及添加一个虚假索引文件以提供额外保护，解决了这一问题。

建议 LiteSpeed Cache 用户清除其服务器上的所有 “debug.log ”文件，以删除可能被威胁行为者窃取的潜在有效会话 cookie。

此外，还应设置 .htaccess 规则，拒绝直接访问日志文件，因为新系统上的随机名称仍可能通过暴力破解来猜测。

WordPress.org报告称，昨天，也就是v6.5.0.1发布的当天，下载LiteSpeed Cache的用户刚刚超过37.5万，因此易受这些攻击影响的网站数量可能超过560万。

## 受到攻击的 LiteSpeed Cache

LiteSpeed Cache 插件漏洞因其广泛的影响力成为了近期安全研究人员的重点研究对象。与此同时，黑客们一直在寻找机会通过利用该漏洞对网站发起攻击。

2024 年 5 月，有人发现黑客利用该插件的一个过时版本（受跟踪为 CVE-2023-40000 的未验证跨站脚本缺陷影响）创建管理员用户并控制网站。

今年 8 月 21 日，研究人员又发现了一个关键的未经身份验证的权限升级漏洞，该漏洞被追踪为 CVE-2024-28000，研究人员对利用该漏洞的难度敲响了警钟。

该漏洞披露后仅几个小时，威胁者就开始大规模攻击网站，Wordfence 报告称阻止了近 5万次攻击。

据统计，在过去的 24 小时内，因其漏洞导致的攻击次数达到了 34 万次。

> 参考来源：[LiteSpeed Cache bug exposes 6 million WordPress sites to takeover attacks](https://www.bleepingcomputer.com/news/security/litespeed-cache-bug-exposes-6-million-wordpress-sites-to-takeover-attacks/)

# 安全漏洞 # WordPress安全

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

调试功能将 cookie 写入文件

受到攻击的 LiteSpeed Cache

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