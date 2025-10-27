---
title: 不要赎金只破坏基础设施，Twelve 黑客大肆攻击俄罗斯实体
url: https://www.freebuf.com/news/411472.html
source: FreeBuf网络安全行业门户
date: 2024-09-24
fetch_date: 2025-10-06T18:27:12.190296
---

# 不要赎金只破坏基础设施，Twelve 黑客大肆攻击俄罗斯实体

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

不要赎金只破坏基础设施，Twelve 黑客大肆攻击俄罗斯实体

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

不要赎金只破坏基础设施，Twelve 黑客大肆攻击俄罗斯实体

2024-09-23 10:19:15

所属地 上海

![1727058248_66f0d148682ac399c8750.png!small](https://image.3001.net/images/20240923/1727058248_66f0d148682ac399c8750.png!small)

据观察，一个名为 “Twelve ”的黑客组织使用大量公开工具对俄罗斯目标实施破坏性网络攻击。

卡巴斯基在周五的分析中表示：与要求赎金解密数据不同，该组织更倾向于加密受害者的数据，然后使用擦除器破坏他们的基础设施，以防止恢复。

这表明，他们希望对目标组织造成最大程度的损害，而不是直接获得经济利益。

据悉，该黑客组织是在2023年4月俄乌战争爆发后成立的，曾发起过多次网络攻击事件、窃取敏感信息，然后通过其Telegram频道分享这些信息。

卡巴斯基称，Twelve 与一个名为 DARKSTAR（又名 COMET 或 Shadow）的勒索软件组织在基础架构和战术上有重合之处，因此这两个黑客组织很可能相互关联，或者是同一活动集群的一部分。

俄罗斯网络安全厂商说：Twelve 的行动明显具有黑客活动的性质，而 DARKSTAR 则坚持典型的双重勒索模式。集团内部目标的这种变化凸显了现代网络威胁的复杂性和多样性。

攻击链首先通过滥用有效的本地或域账户获得初始访问权限，然后使用远程桌面协议（RDP）进行横向移动。其中一些攻击还通过受害者的承包商实施。

卡巴斯基指出：为此，他们获得了承包商基础设施的访问权限，然后使用其证书连接到客户的 VPN。在获得访问权限后，对手可以通过远程桌面协议（RDP）连接到客户的系统，然后侵入客户的基础设施。

Twelve 使用的其他工具包括 Cobalt Strike、Mimikatz、Chisel、BloodHound、PowerView、adPEAS、CrackMapExec、Advanced IP Scanner 和 PsExec，用于窃取凭证、发现、网络映射和权限升级。与系统的恶意 RDP 连接通过 ngrok 传输。

此外，还部署了具有执行任意命令、移动文件或发送电子邮件功能的 PHP web shell。这些程序（如 WSO web shell）在 GitHub 上随时可用。

在此前的一起事件中，卡巴斯基称威胁分子利用了VMware vCenter中的已知安全漏洞（如CVE-2021-21972和CVE-2021-22005），提供了一个web shell，然后利用这个web shell投放了一个名为FaceFish的后门。

攻击者使用 PowerShell 添加域用户和组，并修改 Active Directory 对象的 ACL（访问控制列表）。而为了避免被发现，攻击者将恶意软件和任务伪装成现有产品或服务的名称。攻击者通过使用包括 “Update Microsoft”、“Yandex”、“YandexUpdate ”和 “intel.exe”等名称伪装成英特尔、微软和 Yandex 的程序来逃避检测。

这些攻击的另一个特点是使用 PowerShell 脚本（“Sophos\_kill\_local.ps1”）来终止受攻击主机上与 Sophos 安全软件相关的进程。

最后阶段需要使用 Windows 任务调度程序来启动勒索软件和清除器有效载荷，但在此之前要通过名为 DropMeFiles 的文件共享服务以 ZIP 压缩文件的形式收集和渗出受害者的敏感信息。

卡巴斯基研究人员说：攻击者使用了一个流行的 LockBit 3.0 勒索软件版本，该版本由公开源代码编译而成，用于加密数据。在开始工作之前，勒索软件会终止可能干扰单个文件加密的进程。

与Shamoon恶意软件相同的擦除器会重写所连接驱动器上的主引导记录（MBR），并用随机生成的字节覆盖所有文件内容，从而有效防止系统恢复。

卡巴斯基研究人员指出：该组织坚持使用公开的、人们熟悉的恶意软件工具，这也表明它没有自制的工具，那么大家就还是有机会能及时发现并阻止 Twelve 的攻击。

> 参考来源：[Hacktivist Group Twelve Targets Russian Entities with Destructive Cyber Attacks (thehackernews.com)](https://thehackernews.com/2024/09/hacktivist-group-twelve-targets-russian.html)

# 黑客攻击 # 黑客组织

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