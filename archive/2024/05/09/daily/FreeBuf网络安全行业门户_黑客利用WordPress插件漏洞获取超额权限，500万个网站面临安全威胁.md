---
title: 黑客利用WordPress插件漏洞获取超额权限，500万个网站面临安全威胁
url: https://www.freebuf.com/news/400200.html
source: FreeBuf网络安全行业门户
date: 2024-05-09
fetch_date: 2025-10-06T17:16:22.680064
---

# 黑客利用WordPress插件漏洞获取超额权限，500万个网站面临安全威胁

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

黑客利用WordPress插件漏洞获取超额权限，500万个网站面临安全威胁

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客利用WordPress插件漏洞获取超额权限，500万个网站面临安全威胁

2024-05-08 10:15:06

所属地 上海

![1715134344_663adf882ed70c9474978.png!small](https://image.3001.net/images/20240508/1715134344_663adf882ed70c9474978.png!small)

网络安全研究人员近期发现 WordPress LiteSpeed Cache 插件中存在一个安全漏洞，该漏洞被追踪为 CVE-2023-40000，未经身份验证的威胁攻击者可利用该漏洞获取超额权限。

LiteSpeed Cache 是一种缓存插件，被用于 500 多万个 WordPress 网站，可帮助加快页面加载速度、改善访客体验并提高谷歌搜索排名。

今年4月，Automattic 的安全团队 WPScan 发现，威胁行为者扫描和入侵使用 5.7.0.1 以上版本插件的 WordPress 网站的活动有所增加，因为这些网站存在一个高严重性（8.8）未经验证的跨站脚本漏洞，该漏洞被追踪为 CVE-2023-40000。

在扫描易受攻击的网站时，来自 94[.]102[.]51[.]144 IP 地址的探测请求超过 120 万个。

WPScan 报告称，这些攻击使用恶意 JavaScript 代码注入关键 WordPress 文件或数据库，并创建了名为 "wpsupp-user "或 "wp-configuser "的管理员用户。

另一个感染迹象是数据库中的 "litespeed.admin\_display.messages "选项中出现了 "eval(atob(Strings.fromCharCode "字符串。

![1715134401_663adfc1f12929b9082ec.png!small](https://image.3001.net/images/20240508/1715134401_663adfc1f12929b9082ec.png!small)

恶意 JS 代码创建流氓管理员用户，图源：WPScan

大部分 LiteSpeed Cache 用户已迁移到不受 CVE-2023-40000 影响的最新版本，但仍有大量用户（多达 1,835,000 人）运行有漏洞的版本。

## 锁定电子邮件订阅者插件

攻击者可通过在 WordPress 网站上创建管理员账户的功能获得网站的完全控制权，从而修改内容、安装插件、更改关键设置、将流量重定向到不安全的网站、分发恶意软件、网络钓鱼或窃取可用的用户数据。

本周初，Wallarm 报道了另一起针对 WordPress 插件 "电子邮件订阅者 "创建管理员账户的攻击活动。

黑客利用的是 CVE-2024-2876，这是一个严重程度为 9.8/10 的关键 SQL 注入漏洞，影响的插件版本为 5.7.14 及更早版本。

Wallarm表示，在观察到的攻击实例中，CVE-2024-27956 已被用于对数据库执行未经授权的查询，并在易受攻击的 WordPress 网站（例如，以 "xtw "开头的网站）上建立新的管理员账户。

虽然 "Email Subscribers "远没有 LiteSpeed Cache 那么流行，它的有效安装总数只有 90000 个，但观察到的攻击表明，黑客不会放过任何能攻击的机会。

研究人员建议WordPress 网站管理员将插件立即更新到最新版本，删除或禁用不需要的组件，并监控是否有新的管理员账户创建。

如果确认出现漏洞，必须对网站进行全面清理，需要删除所有恶意账户，重置所有现有账户的密码，并从干净的备份中恢复数据库和网站文件。

> 参考来源：[Hackers exploit LiteSpeed Cache flaw to create WordPress admins (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/hackers-exploit-litespeed-cache-flaw-to-create-wordpress-admins/)

# Wordpress插件漏洞

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

锁定电子邮件订阅者插件

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