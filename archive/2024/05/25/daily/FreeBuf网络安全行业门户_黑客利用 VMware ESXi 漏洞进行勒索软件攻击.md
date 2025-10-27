---
title: 黑客利用 VMware ESXi 漏洞进行勒索软件攻击
url: https://www.freebuf.com/news/401744.html
source: FreeBuf网络安全行业门户
date: 2024-05-25
fetch_date: 2025-10-06T17:17:48.703801
---

# 黑客利用 VMware ESXi 漏洞进行勒索软件攻击

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

黑客利用 VMware ESXi 漏洞进行勒索软件攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客利用 VMware ESXi 漏洞进行勒索软件攻击

2024-05-24 09:46:15

所属地 上海

![1716516775_664ff7a766b1b3475e734.png!small](https://image.3001.net/images/20240524/1716516775_664ff7a766b1b3475e734.png!small)

针对 VMware ESXi 基础架构的勒索软件攻击无论部署何种文件加密恶意软件，都遵循一种既定模式。

网络安全公司Sygnia在与《黑客新闻》共享的一份报告中提到：虚拟化平台是组织IT基础设施的核心组成部分，但它们往往存在固有的错误配置和漏洞，这使它们成为威胁行为者有利可图和高度有效的滥用目标。

这家以色列公司通过对LockBit、HelloKitty、BlackMatter、RedAlert (N13V)、Scattered Spider、Akira、Cactus、BlackCat和Cheerscrypt等各种勒索软件家族的事件响应工作发现，对虚拟化环境的攻击遵循类似的行动顺序。

这包括以下步骤：

* 通过网络钓鱼攻击、恶意文件下载和利用面向互联网资产的已知漏洞获取初始访问权限
* 利用暴力攻击或其他方法提升权限，获取 ESXi 主机或 vCenter 的凭证
* 验证他们对虚拟化基础架构的访问权限并部署勒索软件
* 删除或加密备份系统，或在某些情况下更改密码，使恢复工作复杂化
* 将数据渗出到外部位置，如 Mega.io、Dropbox 或他们自己的托管服务
* 启动勒索软件的执行以加密 ESXi 文件系统的"/vmfs/volumes "文件夹
* 将勒索软件传播到非虚拟化服务器和工作站，以扩大攻击范围

为降低此类威胁带来的风险，建议企业确保实施充分的监控和日志记录，创建强大的备份机制，执行强有力的身份验证措施，加固环境，并实施网络限制以防止横向移动。

网络安全公司 Rapid7 警告称，自 2024 年 3 月初以来，该公司一直在利用常用搜索引擎上的恶意广告，通过错别字域名分发 WinSCP 和 PuTTY 的木马安装程序，并最终安装勒索软件。

这些伪装安装程序充当了投放 Sliver 后期漏洞工具包的渠道，该工具包随后被用于投放更多有效载荷，包括用于部署勒索软件的 Cobalt Strike Beacon。

该活动与之前的 BlackCat 勒索软件攻击在战术上有共同之处，后者使用恶意广告作为初始访问载体，是交付氮气恶意软件的重复性活动的一部分。

安全研究员Tyler McGraw说：该活动一定程度上影响了 IT 团队的成员，他们最有可能在寻找合法版本的同时下载木马文件。

## 勒索软件攻击

恶意软件一旦被成功执行可能会为威胁行为者提供更多便利，让其通过模糊后续管理操作的意图来阻碍分析。

此次攻击也是继Beast、MorLock、Synapse和Trinity等新勒索软件家族出现后的又一次最新事件披露，其中MorLock家族广泛针对俄罗斯公司，并在不先外泄文件的情况下对文件进行加密。

Group-IB在俄罗斯的分支机构F.A.C.C.T.表示：为了恢复数据访问，MorLock攻击者要求支付相当高的赎金，赎金数额可达数千万或数亿卢布。

根据 NCC 集团共享的数据，2024 年 4 月全球勒索软件攻击比上月下降了 15%，从 421 起降至 356 起。

值得注意的是，2024 年 4 月也标志着 LockBit 结束了长达 8 个月的受害者最多的威胁行为体统治，这也说明了其在今年早些时候执法部门大举打击后的艰难生存状况。

然而，令人惊讶的是，LockBit 3.0 并不是本月最突出的威胁组织，其观察到的攻击次数还不到 3 月份的一半。反倒Play 成为了最活跃的威胁组织，紧随其后的是 Hunters。

除了勒索软件领域的动荡之外，网络犯罪分子还在宣传隐藏的虚拟网络计算（hVNC）和远程访问服务，如 Pandora 和 TMChecker，这些服务可被用于数据外渗、部署额外的恶意软件和促进勒索软件攻击。

Resecurity表示：多个初始访问代理（IAB）和勒索软件操作员使用 TMChecker 来检查可用的受损数据，以确定是否存在企业VPN和电子邮件账户的有效凭证。

因此，TMChecker 的同时崛起意义重大，因为它大大降低了那些希望获得高影响力企业访问权限的威胁行为者的进入成本门槛，这些访问权限既可以用于初次利用，也可以在二级市场上出售给其他对手。

> 参考来源：[Ransomware Attacks Exploit VMware ESXi Vulnerabilities in Alarming Pattern (thehackernews.com)](https://thehackernews.com/2024/05/ransomware-attacks-exploit-vmware-esxi.html)

# 勒索软件攻击

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

勒索软件攻击

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