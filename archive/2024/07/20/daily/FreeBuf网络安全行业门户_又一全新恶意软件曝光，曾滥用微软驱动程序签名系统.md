---
title: 又一全新恶意软件曝光，曾滥用微软驱动程序签名系统
url: https://www.freebuf.com/news/406489.html
source: FreeBuf网络安全行业门户
date: 2024-07-20
fetch_date: 2025-10-06T17:42:52.133180
---

# 又一全新恶意软件曝光，曾滥用微软驱动程序签名系统

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

又一全新恶意软件曝光，曾滥用微软驱动程序签名系统

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

又一全新恶意软件曝光，曾滥用微软驱动程序签名系统

2024-07-19 13:38:36

所属地 上海

![1721369611_669a040b952705a6efff0.png!small?1721369612878](https://image.3001.net/images/20240719/1721369611_669a040b952705a6efff0.png!small?1721369612878)

近日，研究人员发现了一种名为 HotPage.exe 的新型恶意软件。

这种恶意软件最初是在 2023 年底被检测到的，起初它伪装成了一个安装程序，表面上可以通过阻止广告和恶意网站来改善网页浏览。

但它实际上是将代码注入远程进程并拦截浏览器流量。正如 ESET 在今天早些时候发布的一份公告中所描述的，该恶意软件可以修改、替换或重定向网页内容，并根据特定条件打开新标签。

有趣的是，HotPage.exe 的嵌入式驱动程序是由微软签署的，但却归属于一家另外的公司。由于有关该公司的信息很少，这引起了人们的警惕。该软件向中文用户推销 “网吧安全解决方案”，据称是为了增强浏览体验。

然而，它却将用户重定向到与游戏相关的广告，并收集用户计算机的数据用于统计目的。

2024 年 3 月 18 日，ESET 按照漏洞披露协调流程向微软报告了这一漏洞。微软于 2024 年 5 月 1 日从 Windows 服务器目录中删除了违规驱动程序。此后，ESET将此威胁标记为Win{32|64}/HotPage.A和Win{32|64}/HotPage.B。

进一步调查发现，该公司利用微软的驱动程序代码签名要求，获得了扩展验证（EV）证书。

ESET表示，这说明基于信任的驱动程序签名系统正在被滥用。该公司注册于2022年初，背景不详，其域名dwadsafe.com现已下线。

## HotPage 恶意软件的技术细节

从技术角度看，该恶意软件的安装过程包括在磁盘上投放驱动程序、解密配置文件并将库注入基于 Chromium 的浏览器。

该驱动程序通过挂钩基于网络的 Windows API 功能、更改 URL 或打开带有广告内容的新标签来操纵浏览器流量。

该恶意软件的一个关键问题是其内核组件，它无意中允许其他威胁在 Windows 操作系统的最高权限级别执行代码。

这是由于访问限制不足，使得任何进程都能与内核组件通信并利用其代码注入功能。

这种技术对网络安全行业的广泛影响值得注意。恶意软件使用经过签名的合法驱动程序，不仅为侵入性广告软件提供了便利，还使系统面临更多安全风险。

攻击者可以利用这一漏洞获得系统级权限或向进程中注入恶意代码，从而利用对已签名驱动程序的固有信任。

为防范此类威胁，安全研究人员建议定期更新软件，使用全面的安全解决方案，并保持严格的访问控制。

> 参考来源：[HotPage Malware Hijacks Browsers With Signed Microsoft Driver - Infosecurity Magazine (infosecurity-magazine.com)](https://www.infosecurity-magazine.com/news/hotpage-hijacks-browsers-microsoft/)

# 恶意软件 # 劫持

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

HotPage 恶意软件的技术细节

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