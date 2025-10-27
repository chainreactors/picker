---
title: 罪恶的”复苏“，Medusa勒索软件正以全球企业为攻击目标
url: https://www.freebuf.com/news/360208.html
source: FreeBuf网络安全行业门户
date: 2023-03-14
fetch_date: 2025-10-04T09:30:26.353135
---

# 罪恶的”复苏“，Medusa勒索软件正以全球企业为攻击目标

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

罪恶的”复苏“，Medusa勒索软件正以全球企业为攻击目标

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

罪恶的”复苏“，Medusa勒索软件正以全球企业为攻击目标

2023-03-13 10:53:29

所属地 上海

据BleepingComputer消息，过去两年一向低调的勒索软件组织Medusa（美杜莎）近期开始变得活跃，目标针对全球范围内的多个企业组织，并索要数百万美元赎金。本月初，Medusa袭击了明尼阿波利斯公立学校 (MPS) ，索要100 万美元的赎金。

Medusa 最早出现于2021 年 6 月，在今年之前所记录到的攻击活动相对较少。但到了 2023 年，该组织的活动明显增加，并推出了一个“Medusa博客”，用于泄露那些拒绝支付赎金的受害者数据。

## Medusa的加密策略

BleepingComputer 分析了适用于 Windows系统的 Medusa 加密器，目前尚不清楚是否有适用于 Linux 的加密器。

Windows 加密器的命令行选项能够允许攻击者配置文件在设备上的加密方式：

> # Command Line
> Option | Description
> ---------------------
> -V | Get version
> -d | Do not delete self
> -f | Exclude system folder
> -i | In path
> -k | Key file path
> -n | Use network
> -p | Do not preprocess (preprocess = kill services and shadow copies)
> -s | Exclude system drive
> -t | Note file path
> -v  | Show console window
> -w | Initial run powershell path (powershell -executionpolicy bypass -File %s)

例如，-v 命令行参数将导致勒索软件显示一个控制台，在它加密设备时显示状态消息。

![](https://image.3001.net/images/20230313/1678674744_640e8b3863e5587f84d03.jpg!small)Medusa 勒索软件控制台窗口

在没有命令行参数的常规运行中，Medusa 勒索软件将终止 280 多个 Windows 服务和程序进程，这些程序可能会阻止文件被加密。其中包括用于邮件服务器、数据库服务器、备份服务器和安全软件的 Windows 服务。随后，Medusa将删除 Windows 卷影副本以防止文件被恢复：

> deletes shadow volume copies
> vssadmin Delete Shadows /all /quiet
> vssadmin resize shadowstorage /for=%s /on=%s /maxsize=unbounded

为防止从备份恢复文件，Medusa将运行以下命令来删除本地存储的相关备份文件。此命令还将删除虚拟机使用的虚拟硬盘驱动器 (VHD)：

> del /s /f /q %s\*.VHD %s\*.bac %s\*.bak %s\*.wbcat %s\*.bkf %sBackup\*.\* %sbackup\*.\* %s\*.set %s\*.win %s\*.dsk

在加密文件时，该勒索软件会将“.Medusa"扩展名附加到被加密的文件名中。在每个文件夹中，Medusa都会创建一个名为 !!!READ\_ME\_MEDUSA!!!.txt 文本的赎金票据，除了告知受害者文件被加密的情况，还会包括Tor 数据泄露网站、Tor 协商网站、Telegram 频道、Tox ID 和 key.medusa.serviceteam@protonmail.com 电子邮件地址等联系信息。

Tor 协商网站自称为“安全聊天”（Secure Chat），其中每个受害者都有一个唯一的 ID，可用于与勒索软件组织进行通信。

![](https://image.3001.net/images/20230313/1678675513_640e8e397cb57bfd7cccf.png!small)Medusa 的 Secure Chat 通信网站

与大多数以企业为目标的勒索软件组织一样，Medusa 有一个名为“Medusa Blog”的数据泄露网站。该网站被用作织双重勒索策略的一部分，会在被拒绝支付赎金后泄露受害者数据。

![](https://image.3001.net/images/20230313/1678675669_640e8ed58f63faece2b7a.png!small)Medusa Blog

当受害者被添加到数据泄露网站中时，Medusa为受害者提供了付费选项，以在数据发布前延长倒计时、删除数据或下载所有数据。这些选项中的每一个都有不同的价格，比如延长1天需要支付1万美元。

![](https://image.3001.net/images/20230313/1678675884_640e8faca36872c479d87.png!small)数据泄露站点的支付选项

这三个支付选项是为了对受害者施加额外压力，迫使他们支付赎金。

到目前为止，还未发现针对Medusa的有效解密器，研究人员将继续分析，寻找其中的弱点。

## Medusa真假难辨

BleepingComputer指出，有许多恶意软件都自称为Medusa，包括具有勒索软件功能的Mirai 的僵尸网络以及广为人知的 MedusaLocker 勒索软件。就 MedusaLocker而言，该恶意软件组织最早出现于2019年，拥有众多附属组织以及名为 ”How\_to\_back\_files.html“ 的赎金票据，文件加密扩展名也不止一个，这些都不同于Medusa的显著特征。

> 参考来源：[Medusa ransomware gang picks up steam as it targets companies worldwide](https://www.bleepingcomputer.com/news/security/medusa-ransomware-gang-picks-up-steam-as-it-targets-companies-worldwide/)

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

Medusa的加密策略

Medusa真假难辨

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