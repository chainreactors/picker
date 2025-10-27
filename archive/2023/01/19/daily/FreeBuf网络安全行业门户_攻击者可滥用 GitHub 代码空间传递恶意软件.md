---
title: 攻击者可滥用 GitHub 代码空间传递恶意软件
url: https://www.freebuf.com/news/355582.html
source: FreeBuf网络安全行业门户
date: 2023-01-19
fetch_date: 2025-10-04T04:17:38.030725
---

# 攻击者可滥用 GitHub 代码空间传递恶意软件

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

攻击者可滥用 GitHub 代码空间传递恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

攻击者可滥用 GitHub 代码空间传递恶意软件

2023-01-18 11:14:55

所属地 上海

Security Affairs 网站披露，Trend Micro 安全研究人员证实攻击者可能滥用开发环境 GitHub Codespaces中某项合法功能，将恶意软件发送给受害系统。![1674011760_63c7647099624a1dd8e9f.png!small](https://image.3001.net/images/20230118/1674011760_63c7647099624a1dd8e9f.png!small)

安全研究人员发现，用户可通过将配置文件提交到至存储库，定制 GitHub 代码空间项目，此举会为项目所有用户创建可重复的代码空间配置，每个代码空间都可在 GitHub 托管的虚拟机上运行。此外，代码空间支持端口转发功能，允许用户从本地浏览器访问和调试运行在特定端口上的网络应用。

Trend Micro 安全研究人员指出，开发人员可在组织内部或者直接公开分享转发端口，任何知道 URL 和端口号的人都可以访问公共端口，这就意味着攻击者可滥用此功能来托管恶意内容，并在其攻击中共享指向这些资源的链接。

在帖子中，Trend Micro 表示为了验证其对威胁建模滥用情况的假设，在 8080 端口上运行一个基于Python 的 HTTP 服务器，转发并公开暴露了该端口。整个过程中，很容易就发现了 URL 和没有 cookies 的认证。

GitHub 代码空间通常使用 HTTP 转发端口，如果需要，开发人员也可以将任何端口更改为 HTTPS。一旦开发人员将公开可见的端口更新为 HTTPS，端口的可见性将自动变为私有，快速查看 VirusTotal 等威胁情报平台将显示该域没有恶意历史记录，如果通过该域分发，阻止下载恶意文件的可能性会大大降低。![1674011777_63c76481f2621b30ca653.png!small](https://image.3001.net/images/20230118/1674011777_63c76481f2621b30ca653.png!small)

攻击者可通过创建一个简单脚本，以自动创建具有公开端口的代码空间，并使用其托管恶意内容。安全专家解释称这一过程包括创建一个 Web 服务器，其中包含一个为恶意文件提供服务的开放目录，并在下载100 秒后删除。

Trend Micro 强调，，攻击者可使用这样的脚本，轻松滥用 GitHub 代码空间，通过在其代码空间环境中公开端口来快速提供恶意内容。

此外，由于每个代码空间都有唯一的标识符，因此关联的子域也是唯一的。这为攻击者提供了足够的空间来创建不同的打开目录实例。好消息是，研究人员设计的攻击技术尚未在野外攻击中得到应用。

**文章来源：**

> https://securityaffairs.com/140932/hacking/github-codespaces-attack-technique.html?

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