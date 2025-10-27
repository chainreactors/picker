---
title: 新的macOS漏洞允许攻击者绕过安全控制
url: https://www.freebuf.com/news/413157.html
source: FreeBuf网络安全行业门户
date: 2024-10-19
fetch_date: 2025-10-06T18:52:25.437594
---

# 新的macOS漏洞允许攻击者绕过安全控制

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

新的macOS漏洞允许攻击者绕过安全控制

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新的macOS漏洞允许攻击者绕过安全控制

2024-10-18 11:37:30

所属地 上海

据Cyber Security News消息， 微软威胁情报发现，macOS出现了一个名为“HM Surf”的新漏洞，能允许攻击者绕过操作系统的透明、同意和控制（TCC）技术，在未经授权的情况下访问用户受保护的数据。

![](https://image.3001.net/images/20241018/1729222693_6711d825601ad56ad1d60.jpg!small)

该漏洞被追踪为CVE-2024-44133，能够被利用收集敏感信息（例如浏览历史记录），并在未经授权的情况下访问设备的摄像头、麦克风和位置。

HM Surf 能够更改当前用户的主目录，修改用户真实主目录下的敏感文件，以及运行 Safari 打开一个网页，该网页拍摄相机快照并跟踪设备位置。

![](https://image.3001.net/images/20241018/1729222533_6711d78505a825fb742fe.jpg!small)Safari 弹出窗口

攻击者可以执行一些隐秘的操作，例如私下托管快照、保存整个摄像头数据流、录制和串流麦克风音频，以及在小窗口中启动 Safari 以避免引起注意。

微软通过 Microsoft Security Vulnerability Research （MSVR） 的协调漏洞披露 （CVD） 与 苹果分享了这一漏洞发现。目前，只有 Safari 使用 TCC 提供的新保护，微软正在与其他主要浏览器供应商合作，以调查强化本地配置文件的好处。

目前苹果已在9 月 16 日发布的 macOS Sequoia 最新安全更新中修复了该漏洞。微软建议macOS 用户尽快应用 Apple 发布的安全更新。

此前，微软已发现多个存在于macOS和Linux系统中的漏洞，随着跨平台威胁的持续增加，对漏洞发现和威胁情报共享的协调响应将有助于加强保护技术，以保护用户在所有平台和设备上的安全。

**参考来源：**

> [New macOS Vulnerability Allows Attackers to Bypass Security Controls](https://cybersecuritynews.com/macos-vulnerability-bypass-security-controls/)

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