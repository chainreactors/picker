---
title: 入侵物理隔离的系统，这家APT组织怎么做到的？
url: https://www.freebuf.com/news/412316.html
source: FreeBuf网络安全行业门户
date: 2024-10-10
fetch_date: 2025-10-06T18:53:01.248475
---

# 入侵物理隔离的系统，这家APT组织怎么做到的？

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

入侵物理隔离的系统，这家APT组织怎么做到的？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

入侵物理隔离的系统，这家APT组织怎么做到的？

2024-10-09 11:44:20

所属地 上海

将机要系统与任何联网系统完全隔离通常被认为是最安全的防御措施，但随着黑客技术的发展，这道坚不可摧的安全屏障已不再牢固，甚至有一家专门针对政府设施下手的APT组织已研发出了两套工具集，对已隔离系统展开了全方位攻势。

ESET 的研究人员近期详细披露了一个名为“GoldenJackal”的网络APT 组织，能够利用多种恶意工具组合对政府和外交实体进行攻击，包括使用特定工具成功针对气隙系统（即已隔离系统）的攻击。

## GoldenJackal 简介

GoldenJackal于2023年5月被卡巴斯基首次披露，但该组织最早的活动可追溯至2019年8月至9月间针对白俄罗斯南亚大使馆的攻击，期间使用的恶意工具于2021年7月再度被检测到。

据称，GoldenJackal长期以欧洲、中东和南亚的政府实体为目标，但根据卡巴斯基的报告，2020年之后，针对中东和南亚政府和外交实体的攻击数量有所缓和。根据ESET近期的监测数据，从 2022 年 5 月到 2024 年 3 月，欧盟政府组织多次成为了该组织的目标。

目前，ESET和卡巴斯基都未明确将该组织与任何国家联系起来，但其中一款名为GoldenHowl 恶意软件的C&C 协议被称为 transport\_http，与已知的 Turla和 MoustachedBouncer 通常使用的表达方式相同，可能表明 其背后的开发者是俄语使用者。

## 针对已隔离系统的攻击

为了最大限度地降低泄露风险，高度敏感的网络通常采用了完全隔离的系统，以保护那些最有价值的系统（如投票系统和运行电网的工业控制系统），这些网络通常正是攻击者最感兴趣的目标。相应的，破坏隔离系统比破坏一般互联网连接的系统要耗费更多资源，迄今为止此类攻击都是由 APT 组织专门开发的间谍活动。

而GoldenJackal在5年时间内构建和部署了两套独立的工具集来破坏已隔离系统，显示出该组织出色的技术实力。

### 针对白俄罗斯的攻击

在2019年针对白俄罗斯南亚大使馆的攻击中，研究人员观察到3个自定义工具集：

> GoldenDealer：通过 USB 监控将可执行文件植入到已隔离系统，可从 C&C 服务器下载可执行文件并将其隐藏在U盘中，或者从这些U盘中检索可执行文件并在没有连接的系统上执行 ；
>
> GoldenHowl：具有各种功能的模块化后门，包括从 JSON 文件解密并加载恶意软件的配置 、创建恶意软件使用的目录以及为每个模块启动一个线程 ；
>
> GoldenRobo：执行文件收集和渗透功能，执行 Robocopy 实用程序来暂存文件并将其发送到其 C&C 服务器。

在攻击链中，具体的初始攻击媒介未知，研究人员假设 GoldenDealer 和未知蠕虫组件已经存在于可以访问互联网的受感染 PC 上，每当插入U盘时，未知组件都会将自身和 GoldenDealer 组件复制到驱动器中。

研究人员将这个未知组件暂称为 JackalWorm，该组件很可能在U盘上找到最后修改的目录，将其隐藏，并使用该目录的名称将自身重命名。此外，该组件使用了文件夹图标，以诱使用户在将 U 盘插入已隔离系统时点击运行。

当驱动器再次插入连接到互联网的PC时，GoldenDealer会从U盘中获取关于已隔离系统的信息，并将其发送到C&C服务器。服务器回复一个或多个要在已隔离系统上运行的可执行文件。最后，当U盘再次插入已隔离系统时，GoldenDealer会从驱动器中获取可执行文件并运行。

![](https://image.3001.net/images/20241009/1728453431_67061b37bb1cc9d8cd69a.png!small)针对已隔离系统的攻击链

### 针对欧洲政府的攻击

在近期针对欧洲政府机构的攻击中，GoldenJackal 转向了高度模块化的新工具集，这种模块化方法不仅适用于恶意工具的设计，还包括其具体的功能，如收集和处理信息，将文件、配置和命令分发到其他系统以及外泄文件。

2022 年 5 月，研究人员观察到GoldenJackal 在针对欧洲的一家政府组织时使用了新工具集，这些工具中的大多数都是用 Go 编写的，并提供了多种功能，例如从U盘收集文件、通过U盘 在网络中传播有效载荷、泄露文件以及使用网络中的一些 PC 作为服务器将各种文件传送到其他系统。此外，研究人员还看到攻击者使用 Impacket 在网络中横向移动。

![](https://image.3001.net/images/20241009/1728456009_67062549977e05a3a5ec1.png!small)GoldenJackal 最新工具集中的组件

在观察到的攻击中，GoldenJackal 通过高度模块化的工具，使用各种组件来执行不同的任务。一些主机被滥用以泄露文件，另一些主机被用作本地服务器来接收和分发暂存文件或配置文件，而另一些主机则被认为用于间谍目的。一些典型工具包括：

> GoldenUsbCopy：监视U盘的插入，并将目标文件复制到存储在磁盘上的加密容器中，以供其他组件泄露；
>
> GoldenAce：属分发工具，用于传播其他恶意可执行文件并通过U盘检索暂存文件；
>
> GoldenBlacklist：从本地服务器下载加密存档，并处理其中包含的电子邮件，以仅保留目标内容。并为其他组件生成一个新的存档以进行外泄；
>
> GoldenMailer：通过向攻击者控制的帐户发送带有附件的电子邮件来泄露文件；
>
> GoldenDrive：与 GoldenMailer 相反，此组件通过将文件上传到 Google Drive 来泄露文件。

目前尚不清楚 GoldenJackal 如何设法获得初始妥协以破坏目标环境。但是，卡巴斯基此前曾暗示过木马化 Skype 安装程序和恶意 Microsoft Word 文档作为入口点的可能性。

上述两起典型攻击表明，即便是安全保障严格的隔离系统，仍然存在被一些有实力的黑客组织通过研发复杂工具来成功实施攻击。但研究人员强调，这些工具并非没有缺陷，仍可通过观察其战术来更好地准备应对未来的攻击。研究人员已在 GitHub 上分享了一份公开的 IOC 列表，供防御者进行监控。

#### **参考来源：**

> [Mind the (air) gap: GoldenJackal gooses government guardrails](https://www.welivesecurity.com/en/eset-research/mind-air-gap-goldenjackal-gooses-government-guardrails/)

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

GoldenJackal 简介

针对已隔离系统的攻击

* 针对白俄罗斯的攻击
* 针对欧洲政府的攻击

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