---
title: 新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据
url: https://www.freebuf.com/news/415390.html
source: FreeBuf网络安全行业门户
date: 2024-11-16
fetch_date: 2025-10-06T19:17:49.615850
---

# 新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据

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

新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据

2024-11-15 16:03:33

所属地 上海

Securelist 网络安全研究人员发现了一种新型恶意软件，这种恶意软件冒充PDF编辑器、AutoCAD 和 JetBrains 等合法软件， 通过在线论坛、种子跟踪器和博客传播。

![](https://image.3001.net/images/20241115/1731657970_673700f22eaec92a0cb34.jpg!small)

该恶意软件被研究人员称为 "SteelFox"，最早于2023年2月开始活跃，其主要目标是那些下载盗版软件和软件激活工具（破解版）的 Windows系统用户。到目前为止，该恶意软件已感染了全球超过1.1万名用户。

根据 Securelist 与 Hackread分享的博客文章，SteelFox 是一个功能齐全的“犯罪软件捆绑包”，可从受感染的设备中提取敏感数据，包括信用卡信息、浏览历史记录和登录凭证。它还收集系统信息，例如已安装的软件、正在运行的服务和网络配置。

该恶意软件的初始攻击媒介涉及软件激活器，这些激活器在在线论坛和种子跟踪器上做广告，作为免费激活合法软件的一种方式。安装后，恶意软件会创建一个服务，即使在重启后也会保留在系统上，并使用易受攻击的驱动程序来提升权限。

该恶意软件通过一个多阶段攻击链运行，首先是一个需要管理员权限的下载器。 执行后会将自身安装为 Windows 服务，并使用 AES-128 加密来隐藏其组件。 该恶意软件通过利用易受攻击的驱动程序实现系统级访问，并通过 SSL pinning 实现 TLS 1.3，以便与其命令服务器进行安全通信。

SteelFox 似乎没有针对特定的个人或组织，而是在更大范围内运作以感染尽可能多的用户，目前已受到感染的用户包括阿联酋、印度、巴西、中国、俄罗斯、埃及、阿尔及利亚、墨西哥、越南、斯里兰卡等10多个国家。

由于SteelFox的下载器具有双重功能——同时提供软件 "破解 "和恶意软件，表明网络犯罪分子使用了复杂的工具，并使用过时的驱动程序进行权限升级。因此，企业及用户确保系统及时打上了安全补丁变得格外重要，同时尽量从官方来源下载正版软件。

**参考来源：**

> [New SteelFox Malware Posing as Popular Software to Steal Browser Data](https://hackread.com/steelfox-malware-software-to-steal-browser-data/)

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