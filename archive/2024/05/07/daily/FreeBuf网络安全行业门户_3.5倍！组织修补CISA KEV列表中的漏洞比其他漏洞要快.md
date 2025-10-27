---
title: 3.5倍！组织修补CISA KEV列表中的漏洞比其他漏洞要快
url: https://www.freebuf.com/news/399968.html
source: FreeBuf网络安全行业门户
date: 2024-05-07
fetch_date: 2025-10-06T17:17:48.315898
---

# 3.5倍！组织修补CISA KEV列表中的漏洞比其他漏洞要快

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

3.5倍！组织修补CISA KEV列表中的漏洞比其他漏洞要快

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

3.5倍！组织修补CISA KEV列表中的漏洞比其他漏洞要快

2024-05-06 10:20:32

所属地 上海

therecord网站消息，研究人员发现，联邦政府维护的已知被利用漏洞（KEV）目录对联邦政府内外的组织机构产生了实质性的影响。

![](https://image.3001.net/images/20240506/1714962836_66384194a34902b13f8d2.png!small)网络安全和基础设施安全局（CISA）的KEV目录已经运行了近三年，早已迅速成为全球黑客积极利用的软件和硬件漏洞的首选存储库。对此，网络安全扫描公司Bitsight的专家提出了一个问题："与不在KEV目录中的漏洞相比，企业修复KEV的速度是否更快？“

答案明确是「是」。根据Bitsight的研究人员对100多万个实体（包括公司、学校、地方政府等）进行漏洞扫描的数据显示，KEV所列漏洞的修复时间中位数为174天，而非KEV所列漏洞的修复时间为621天。换句话说，修补目录中列出的漏洞所需的时间中位数是非KEV漏洞的3.5倍。

该公司证实，KEV列表通过帮助公司和地方政府从大量漏洞中筛选出真正重要的漏洞产生了实际效果。2023 年，在Bitsight观察到的所有组织中，有35%的组织处理过KEV，其中绝大多数的组织有一个以上的KEV。

## 漏洞修复时间

每个添加到KEV列表中的漏洞都附带一个截止日期，该日期根据漏洞的严重程度和被定位的紧急性而有所不同。这个截止日期正式适用于联邦机构，但对于美国政府之外的组织，它可以作为漏洞严重程度的一个指南。

Bitsight发现，受CISA约束性指令监管的联邦民事机构比其他组织更有可能在截止日期前解决KEV漏洞，概率高出63%。而大约40%的组织（即那些不必遵守CISA规定的联邦政府以外的组织）能够在CISA的截止日期前解决漏洞。

报告指出，从KEV列表创建至今，给予漏洞修补的截止日期发生了巨大变化。该列表首次创建时，CISA通常给联邦民事机构一周、两周或六个月的时间来修补漏洞。但到2022年春季，他们将截止日期调整为三周。直到最近几个月，又重新规定了一周的期限。

为什么会发生这种变化？早期的这些漏洞通常在添加到KEV目录时就已经存在了，考虑到这种情况，CISA给组织时间解决问题似乎是合理的。

截止日期还可能受漏洞是否被勒索软件使用的影响：一周内需要解决的漏洞比其他漏洞更容易被用于勒索软件，因为这些漏洞非常紧急，如果黑客在组织机构系统上利用它们，可能会造成重大损失。

科技公司是最快解决漏洞的公司之一，部分原因是它们在Bitsight列出的暴露漏洞最多的行业中名列榜首。

在Bitsight追踪的行业中，教育机构和地方政府的情况最为糟糕，这两个行业受KEV列表漏洞影响较大，修复时间较慢。而保险公司、信用社和工程公司受KEV列表漏洞影响的程度相对较低，通常修复问题的速度也较快。

## 列表上的新漏洞

上周，CISA在KEV列表中增加了两个漏洞。其中被命名为CVE-2024-29988的漏洞是微软在四月份发布的 “补丁星期二”（Patch Tuesday）中公布的，该漏洞会影响微软产品中包含的云端反钓鱼和反恶意软件组件SmartScreen。

Immersive Labs的首席网络安全工程师本·麦卡锡（Ben McCarthy）表示，SmartScreen是一个大型弹出窗口，SmartScreen是一个大型弹出窗口，会警告用户有关运行未知文件的情况，它通常是网络钓鱼攻击的终端，用于吓唬用户，让他们不敢继续打开文件。

他补充说，该漏洞在使用文件下载作为获取初始访问权限的攻击技术的攻击者中很流行，因为他们想找到绕过SmartScreen等安全功能的方法。

CISA指出，在攻击过程中，该漏洞可以与CVE-2024-21412链接。一位发现CVE-2024-21412和CVE-2024-29988漏洞的零日计划研究人员表示，通过直接手段（电子邮件和直接消息）进行的社会工程攻击需要某种用户交互，这是这类漏洞典型的利用途径。

CVE-2024-21412被用作DarkGate活动的一部分，该活动利用假冒苹果iTunes、Notion、英伟达（NVIDIA）等公司的虚假软件安装程序。Microsoft Defender SmartScreen本应为终端用户提供额外保护，防止网络钓鱼和恶意网站，但由于这些漏洞绕过了安全功能，导致终端用户感染恶意软件。

上个月，《Bleeping Computer》报道称，一个出于经济动机的黑客组织利用该漏洞攻击了外汇交易论坛和股票交易Telegram频道。

参考来源：

[Organizations patch CISA KEV list bugs 3.5 times faster than others, researchers find (therecord.media)](https://therecord.media/kev-list-vulnerabilities-patched-significantly-faster)

# 漏洞 # 安全漏洞 # 漏洞修复 # 漏洞管理

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

漏洞修复时间

列表上的新漏洞

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