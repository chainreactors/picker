---
title: 三星 Galaxy Store 曝严重漏洞，黑客可在目标设备上”偷偷“安装 APP
url: https://www.freebuf.com/news/348588.html
source: FreeBuf网络安全行业门户
date: 2022-11-03
fetch_date: 2025-10-03T21:39:54.755539
---

# 三星 Galaxy Store 曝严重漏洞，黑客可在目标设备上”偷偷“安装 APP

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

三星 Galaxy Store 曝严重漏洞，黑客可在目标设备上”偷偷“安装 APP

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

三星 Galaxy Store 曝严重漏洞，黑客可在目标设备上”偷偷“安装 APP

2022-11-02 13:51:09

所属地 上海

The Hacker News 网站披露，三星 Galaxy Store 中披露一个现已修复的安全漏洞，该漏洞可能会触发受影响手机上的远程命令执行。![1667368295_63620567c0799dcb8c8cf.jpg!small](https://image.3001.net/images/20221102/1667368295_63620567c0799dcb8c8cf.jpg!small)

据悉，该漏洞由一名独立安全研究员发现并上报，主要影响 Galaxy Store 4.5.32.4 版本，与处理某些深度链接时出现的跨站脚本（XSS）漏洞有关。

上周，Disclosure 在公告中表示，由于没有安全检查深层链接，当用户从包含深层链接的网站访问链接时，攻击者可以在 Galaxy Store 应用程序的 webview 上下文中执行 JS 代码。![1667368302_6362056e78541a6deed6e.jpg!small](https://image.3001.net/images/20221102/1667368302_6362056e78541a6deed6e.jpg!small)

XSS 攻击允许攻击者在从浏览器或其他应用程序访问网站时注入和执行恶意的 JavaScript 代码。

Galaxy Store 应用程序中出现的安全漏洞与三星的营销和内容服务（MCS）深层链接配置方式有关，这可能导致向 MCS 网站注入并执行任意代码。

之后，当用户访问该链接时，可能被用来在三星设备上下载和安装带有恶意软件的应用程序。另外，研究人员指出，为了能够成功利用受害者的服务器，攻击者有必要对 chrome 进行 HTTPS 和 CORS 绕过。

**参考文章：**

> https://thehackernews.com/2022/10/samsung-galaxy-store-bug-couldve-let.html

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