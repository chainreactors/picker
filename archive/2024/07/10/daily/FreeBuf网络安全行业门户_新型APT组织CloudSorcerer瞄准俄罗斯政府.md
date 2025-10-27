---
title: 新型APT组织CloudSorcerer瞄准俄罗斯政府
url: https://www.freebuf.com/news/405508.html
source: FreeBuf网络安全行业门户
date: 2024-07-10
fetch_date: 2025-10-06T17:45:13.039551
---

# 新型APT组织CloudSorcerer瞄准俄罗斯政府

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

新型APT组织CloudSorcerer瞄准俄罗斯政府

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型APT组织CloudSorcerer瞄准俄罗斯政府

2024-07-09 11:19:16

所属地 上海

网络安全公司卡巴斯基发现，一个名为 CloudSorcerer的新型APT组织通过滥用公共云服务，对俄罗斯政府机构实施攻击并窃取数据。

![](https://image.3001.net/images/20240709/1720495870_668caefe4018f6ff4e225.png!small)

卡巴斯基于 2024 年 5 月发现了这一活动，攻击者采用的技术与 CloudWizard 相似，但指出了恶意软件源代码的不同之处，称这是一种复杂的网络间谍工具，通过Microsoft Graph、Yandex Cloud和 Dropbox 云基础设施进行隐形监控、数据收集和泄露。

该恶意软件利用云资源作为其命令和控制（C2）服务器，通过使用身份验证令牌的 API 访问这些资源。 此外，CloudSorcerer 还使用 GitHub 作为其初始 C2 服务器。目前尚不清楚用于渗透目标的确切方法，但初始访问被用来投放基于 C 语言的便携式可执行程序二进制文件，该二进制文件可用作后门、启动 C2 通信，或根据其执行的进程向其他合法进程注入 shellcode。

卡巴斯基指出，该恶意软件能够根据所运行的进程动态调整其行为，再加上它通过 Windows 管道使用复杂的进程间通信，这进一步凸显了它的复杂性。 后门组件旨在收集受害者机器的信息，并检索指令以枚举文件和文件夹、执行 shell 命令、执行文件操作和运行其他有效载荷。

此外，恶意软件的后门组件能收集受害者机器的信息，并获取枚举文件和文件夹、执行shell命令、执行文件操作和运行其他有效载荷的指令。

C2模块则连接到一个GitHub页面，该页面充当死区解析器（dead drop resolver），以获取一个十六进制字符串，该字符串指向托管在Microsoft Graph或Yandex Cloud上的实际服务器。此外，CloudSorcerer没有连接到GitHub，而是试图从一个基于俄罗斯云的照片托管服务器获取相同的数据。

由于使用 Microsoft Graph、Yandex Cloud 和 Dropbox 等云服务作为 C2 基础设施，并使用 GitHub 进行初始 C2 通信，显示这是通过精心策划的网络间谍攻击。

总体而言，CloudSorcerer 后门是一种强大的工具，使攻击者能够在受感染的机器上执行恶意操作。目前卡巴斯基已发布用于检测CloudSorcerer恶意软件的入侵指标（IoC）和Yara规则。

**参考来源：**

> [New APT Group "CloudSorcerer" Targets Russian Government Entities](https://thehackernews.com/2024/07/new-apt-group-cloudsorcerer-targets.html)

# 恶意软件 # APT组织

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