---
title: WordPress Ninja Forms 曝出严重安全漏洞
url: https://www.freebuf.com/news/373286.html
source: FreeBuf网络安全行业门户
date: 2023-07-29
fetch_date: 2025-10-04T11:53:59.934949
---

# WordPress Ninja Forms 曝出严重安全漏洞

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

WordPress Ninja Forms 曝出严重安全漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

WordPress Ninja Forms 曝出严重安全漏洞

2023-07-28 11:44:35

所属地 上海

Bleeping Computer 网站披露，WordPress 表单构建插件 Ninja Forms 存在三个安全漏洞，攻击者可以通过这些漏洞实现权限提升并窃取用户数据。![1690515859_64c33993af0b1a24fdea0.png!small?1690515859713](https://image.3001.net/images/20230728/1690515859_64c33993af0b1a24fdea0.png!small?1690515859713)

2023 年 6 月 22 日，Patchstack 的研究人员向插件开发者 Saturday Drive 报告了这三个漏洞详情，并警告称漏洞会影响 NinjaForms 3.6.25 及以上版本。

2023 年 7 月 4 日，Saturday Drive 发布新版本 3.6.26 修复了漏洞问题，但根据 WordPress.org 统计数据显示只有大约一半的 NinjaForms 用户下载最新版本。（大约 40 万个网站仍未更新，可能存在被攻击的风险）

## 漏洞详情

Patchstack 发现的第一个漏洞是 2CVE-2023-37979，该漏洞是一个基于 POST 的反射 XSS（跨站点脚本）漏洞，允许未经身份验证的用户通过诱骗特权用户访问特制的网页，以此提升权限并窃取信息。

第二个漏洞和第三个漏洞分别被跟踪为 CVE-2023-38393 和 CVE-2023-3 8386，允许订阅服务器和贡献者导出用户在受影响的 WordPress 网站上提交的所有数据。

值得一提的是，以上漏洞都高度危险，尤其是 CVE-2023-38393 更是如此。任何支持会员资格和用户注册的网站，一旦使用易受攻击的 Ninja Forms 插件版本，都容易因该漏洞而发生大规模数据泄露事件。![1690515844_64c3398496406def5c152.png!small?1690515844310](https://image.3001.net/images/20230728/1690515844_64c3398496406def5c152.png!small?1690515844310)

包含 CVE-2023-38393 的处理功能

Saturday Drive 在 3.6.26 版本中应用的修补程序主要包括为损坏的访问控制问题添加权限检查，以及防止触发已识别 XSS 的功能访问限制。

Patchstack 报告中包含了三个漏洞的详细技术信息，因此对于懂技术的威胁攻击者来说，利用这些漏洞应该是得心应手。为防止网络攻击者利用这些漏洞，Patchstack 公开披露漏洞的时间推迟了三周多，并一再督促Ninja Form用户尽快进行修补。

最后，建议所有使用 Ninja Forms 插件的网站管理员尽快更新到 3.6.26 或以上版本，如果发现未更新的用户，管理员应该从用户的网站禁用插件，直到其应用最新补丁。

**文章来源：**

> https://www.bleepingcomputer.com/news/security/wordpress-ninja-forms-plugin-flaw-lets-hackers-steal-submitted-data/#google\_vignette

# 漏洞

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

漏洞详情

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