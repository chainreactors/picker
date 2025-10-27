---
title: 曾冒充Sophos进行非法活动，又一新型勒索软件曝光！
url: https://www.freebuf.com/news/372446.html
source: FreeBuf网络安全行业门户
date: 2023-07-20
fetch_date: 2025-10-04T11:55:52.779419
---

# 曾冒充Sophos进行非法活动，又一新型勒索软件曝光！

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

曾冒充Sophos进行非法活动，又一新型勒索软件曝光！

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

曾冒充Sophos进行非法活动，又一新型勒索软件曝光！

2023-07-19 10:54:24

所属地 上海

![1689734654_64b74dfe351e597320a13.png!small](https://image.3001.net/images/20230719/1689734654_64b74dfe351e597320a13.png!small)

近日，市面上出现了一款名为SophosEncrypt的新型勒索软件，该软件与网络安全厂商Sophos同名，因此有一些威胁行为者专门冒用该公司名称进行一些非法行动。

MalwareHunterTeam在本周一（7月17日）首次发现了这款勒索软件，起初还以为它是 Sophos 红队演习的一部分。

但很快Sophos X-Ops团队就在推特上表明，他们并没有创建该加密程序，且正在对此次事件进行调查。

Sophos X-Ops团队表示，他们早些时候在VT上发现了这个勒索软件并且一直在调查。但据初步调查结果显示，Sophos InterceptX可以抵御这些勒索软件样本。

此外，ID勒索软件显示了一份受害者提交的报告，表明此勒索软件目前仍处于活动状态。虽然对RaaS操作及其推广方式知之甚少，但MalwareHunterTeam还是发现了一个加密器的样本。

## SophosEncrypt 勒索软件

据悉，该勒索软件的加密程序是用 Rust 编写的，并使用了 "C:\Users\Dubinin\"路径作为其原型。 在内部，该勒索软件被命名为 "sophos\_encrypt"，因此被称为SophosEncrypt，检测结果已添加到ID Ransomware中。

执行时，加密程序会提示联盟成员输入一个与受害者相关的令牌，该令牌可能首先从勒索软件管理面板中获取。

输入令牌后，加密程序将连接到 179.43.154.137:21119 并验证令牌是否有效。 勒索软件专家Michael Gillespie发现可以通过禁用网卡绕过这一验证，从而有效地离线运行加密程序。输入有效令牌后，加密器会提示勒索软件联盟在加密设备时使用其他信息，包括联系人电子邮件、jabber 地址和 32 个字符的密码，Gillespie称这也是加密算法的一部分。

然后，加密器会提示联盟成员加密一个文件或加密整个设备，如下图所示。

![1689735608_64b751b8e5129089abbbf.png!small?1689735609486](https://image.3001.net/images/20230719/1689735608_64b751b8e5129089abbbf.png!small?1689735609486)

加密器在加密前提示信息，来源：BleepingComputer BleepingComputer

在加密文件时，Gillespie告诉BleepingComputer，它使用了AES256-CBC加密和PKCS#7填充。每个加密文件都会在文件名后附加输入的令牌、输入的电子邮件和sophos扩展名，格式为：.[[[]].[[[]].sophos。下面是 BleepingComputer 的加密测试示例。

![1689735703_64b7521778a6c21ace18e.png!small?1689735704067](https://image.3001.net/images/20230719/1689735703_64b7521778a6c21ace18e.png!small?1689735704067)

被SophosEncrypt加密的文件，来源：BleepingComputer BleepingComputer

在每个文件被加密的文件夹中，勒索软件都会创建一个名为 information.hta 的赎金说明，加密完成后会自动启动。该赎金说明包含有关受害者文件遭遇情况的信息，以及关联方在加密设备前输入的联系信息。

![1689735825_64b7529165f69bd3731b8.png!small?1689735826767](https://image.3001.net/images/20230719/1689735825_64b7529165f69bd3731b8.png!small?1689735826767)

SophosEncrypt 勒索信，来源：BleepingComputer BleepingComputer

该勒索软件还能更改 Windows 桌面壁纸，壁纸会直接显示为它所冒充的 "Sophos "品牌。

![1689735899_64b752db3aff3cbd9f348.png!small?1689735899992](https://image.3001.net/images/20230719/1689735899_64b752db3aff3cbd9f348.png!small?1689735899992)

SophosEncrypt 壁纸，来源：BleepingComputer BleepingComputer

加密程序中多次提到位于 http://xnfz2jv5fk6dbvrsxxf3dloi6by3agwtur2fauydd3hwdk4vmm27k7ad.onion 的 Tor 网站。这个 Tor 网站不是一个谈判或数据泄漏网站，而似乎是勒索软件即服务操作的附属面板。

![1689736041_64b753696a6d87848acf5.png!small?1689736042581](https://image.3001.net/images/20230719/1689736041_64b753696a6d87848acf5.png!small?1689736042581)

勒索软件面板，来源：BleepingComputer BleepingComputer

Sophos研究人员对 SophosEncrypt 恶意软件进行分析后发布了一份关于新的 SophosEncrypt 勒索软件的报告。

该报告显示，该勒索软件团伙位于 179.43.154.137 的命令和控制服务器与之前攻击中使用的 Cobalt Strike C2 服务器有所关联。

此外，两个样本都包含一个硬编码 IP 地址，该地址在近一年多的时间内一直与 Cobalt Strike 命令控制和自动攻击有关，这些攻击还曾试图用加密采矿软件感染其他计算机。

> 参考来源：[Cybersecurity firm Sophos impersonated by new SophosEncrypt ransomware](https://www.bleepingcomputer.com/news/security/cybersecurity-firm-sophos-impersonated-by-new-sophosencrypt-ransomware/)

# 勒索软件 # 非法入侵 # 勒索软件攻击 # 网络安全厂商

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

SophosEncrypt 勒索软件

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