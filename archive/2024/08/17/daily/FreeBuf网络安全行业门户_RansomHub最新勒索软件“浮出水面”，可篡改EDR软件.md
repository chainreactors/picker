---
title: RansomHub最新勒索软件“浮出水面”，可篡改EDR软件
url: https://www.freebuf.com/news/408777.html
source: FreeBuf网络安全行业门户
date: 2024-08-17
fetch_date: 2025-10-06T18:05:44.990265
---

# RansomHub最新勒索软件“浮出水面”，可篡改EDR软件

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

RansomHub最新勒索软件“浮出水面”，可篡改EDR软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

RansomHub最新勒索软件“浮出水面”，可篡改EDR软件

2024-08-16 10:54:45

所属地 上海

![1723777303_66bec11727fb37de8df6e.png!small](https://image.3001.net/images/20240816/1723777303_66bec11727fb37de8df6e.png!small)

据观察，一个与 RansomHub 勒索软件有关联的网络犯罪团伙使用了一种新工具，该工具能够终止受攻击主机上的端点检测和响应（EDR）软件，并加入了 AuKill（又名 AvNeutralizer）和 Terminator 等其他类似程序。

网络安全公司Sophos将这种工具命名为EDRKillShifter，该公司是在今年5月的一次勒索软件攻击事件中注意到该工具的。

安全研究员 Andreas Klopsch 称EDRKillShifter 工具是一个‘加载器’可执行文件，一种合法驱动程序的交付机制，容易被滥用（也被称为‘自带易受攻击驱动程序’或 BYOVD 工具）。根据威胁行为者的要求，它可以提供各种不同的驱动程序有效载荷。

RansomHub看起来似乎是 Knight 勒索软件的改良版，最早被发现于2024年2月。它利用已知的安全漏洞获取初始访问权限，并将Atera和Splashtop等合法远程桌面软件丢弃以实现持久访问。

上个月，微软披露， Scattered Spider 电子犯罪集团 已将 RansomHub 和 Qilin 等勒索软件纳入其武器库。

该可执行文件通过命令行和密码字符串输入执行，解密名为 BIN 的嵌入式资源并在内存中执行。BIN 资源解包并运行基于 Go 的最终混淆有效载荷，然后利用不同的易受攻击的合法驱动程序来获得更高的权限并解除 EDR 软件。

二进制文件的语言属性是俄语，这表明恶意软件作者是在具有俄语本地化设置的计算机上编译可执行文件的。Klopsch 表示，所有解压缩的 EDR 杀手都在 .data 部分嵌入了一个易受攻击的驱动程序。

为减轻威胁，研究人员建议保持系统处于最新状态，并启用 EDR 软件中的篡改保护功能，对 Windows 安全角色采取严格措施。

Klopsch 认为：只有当攻击者升级了他们所控制的权限，或者当他们可以获得管理员权限时，这种攻击才有可能发生。因此，将用户和管理员权限加以区分有助于防止攻击事件的发生。

> 参考来源：[RansomHub Group Deploys New EDR-Killing Tool in Latest Cyber Attacks](https://thehackernews.com/2024/08/ransomhub-group-deploys-new-edr-killing.html)

# 勒索软件

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