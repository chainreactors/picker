---
title: 微软发布脚本更新可启动媒体以应对BlackLotus UEFI启动工具包威胁
url: https://www.freebuf.com/sectool/421121.html
source: FreeBuf网络安全行业门户
date: 2025-02-06
fetch_date: 2025-10-06T20:35:37.417507
---

# 微软发布脚本更新可启动媒体以应对BlackLotus UEFI启动工具包威胁

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

微软发布脚本更新可启动媒体以应对BlackLotus UEFI启动工具包威胁

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

微软发布脚本更新可启动媒体以应对BlackLotus UEFI启动工具包威胁

2025-02-05 18:16:04

所属地 上海

![Windows logo](https://image.3001.net/images/20250206/1738800108854450_0e612d1ef4124677a8c4cb46118c083b.jpg!small)

微软近日发布了一款PowerShell脚本，旨在帮助Windows用户和管理员更新可启动媒体，使其在BlackLotus UEFI启动工具包的缓解措施于今年晚些时候生效之前，能够使用新的“Windows UEFI CA 2023”证书。

## BlackLotus UEFI启动工具包的威胁

BlackLotus是一种UEFI启动工具包，能够绕过安全启动（Secure Boot）并控制操作系统的启动过程。一旦获得控制权，BlackLotus可以禁用Windows的安全功能，如BitLocker、Hypervisor-Protected Code Integrity（HVCI）和Microsoft Defender Antivirus，从而在最高权限级别部署恶意软件，同时保持不被检测到。

2023年3月和2024年7月，微软发布了针对CVE-2023-24932漏洞的安全更新，该漏洞允许BlackLotus绕过安全启动。这些更新撤销了BlackLotus使用的易受攻击的启动管理器。

## 分阶段推出安全更新

然而，此修复程序默认情况下是禁用的，因为错误地应用更新或设备上的冲突可能导致操作系统无法加载。因此，分阶段推出修复程序允许Windows管理员在2026年之前的某个时间点强制执行之前进行测试。

启用后，安全更新将把“Windows UEFI CA 2023”证书添加到UEFI的“安全启动签名数据库”中。管理员随后可以安装使用此证书签名的新启动管理器。

此过程还包括更新安全启动禁止签名数据库（DBX），以添加“Windows Production CA 2011”证书。该证书用于签署较旧的、易受攻击的启动管理器，一旦被撤销，这些启动管理器将不再受信任且无法加载。

## 更新可启动媒体的必要性

如果在应用缓解措施后遇到设备启动问题，必须首先更新可启动媒体以使用Windows UEFI CA 2023证书来排查Windows安装问题。

微软在关于CVE-2023-24932分阶段修复的支持公告中解释道：“如果在应用缓解措施后遇到设备问题且设备无法启动，您可能无法从现有媒体启动或恢复设备。恢复或安装媒体需要更新，以便在应用了缓解措施的设备上正常工作。”

## 微软发布PowerShell脚本

昨日，微软发布了一款PowerShell脚本，帮助用户更新可启动媒体，使其使用Windows UEFI CA 2023证书。

![Script to apply CVE-2023-24932 mitigations to bootable Windows media](https://image.3001.net/images/20250206/1738800110073050_3f768910fb714811b6ec9daca1ae9dae.jpg!small)**用于将CVE-2023-24932缓解措施应用于可启动Windows媒体的脚本** *来源：BleepingComputer*

微软解释道：“本文中描述的PowerShell脚本可用于更新Windows可启动媒体，以便该媒体可以在信任Windows UEFI CA 2023证书的系统上使用。”

该PowerShell脚本可从微软下载，并可用于更新ISO CD/DVD映像文件、USB闪存驱动器、本地驱动器路径或网络驱动器路径的可启动媒体文件。

要使用此工具，必须首先下载并安装Windows ADK，这是脚本正常运行所必需的。

运行时，脚本将更新媒体文件以使用Windows UEFI CA 2023证书，并安装由该证书签名的启动管理器。

强烈建议Windows管理员在安全更新强制执行阶段之前测试此过程。微软表示，强制执行将在2026年底之前进行，并在开始前提前六个月通知。

**参考来源：**

> [Microsoft script updates bootable media for BlackLotus bootkit fixes](https://www.bleepingcomputer.com/news/microsoft/microsoft-script-updates-bootable-media-for-blacklotus-bootkit-fixes/)

# 工具 # 终端安全

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

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