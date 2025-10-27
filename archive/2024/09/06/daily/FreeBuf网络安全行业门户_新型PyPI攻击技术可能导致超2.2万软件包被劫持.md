---
title: 新型PyPI攻击技术可能导致超2.2万软件包被劫持
url: https://www.freebuf.com/news/410259.html
source: FreeBuf网络安全行业门户
date: 2024-09-06
fetch_date: 2025-10-06T18:26:52.709404
---

# 新型PyPI攻击技术可能导致超2.2万软件包被劫持

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

新型PyPI攻击技术可能导致超2.2万软件包被劫持

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型PyPI攻击技术可能导致超2.2万软件包被劫持

2024-09-05 09:26:45

所属地 上海

![1725499957_66d90a355bc5fd946b26d.png!small](https://image.3001.net/images/20240905/1725499957_66d90a355bc5fd946b26d.png!small)

一种针对 Python 软件包索引（PyPI）注册表的新型供应链攻击技术已在野外被利用，并且目前正试图渗透到下游组织中。

软件供应链安全公司 JFrog 将其代号定为Revival Hijack，并称这种攻击方法可用于劫持 2.2万个现有 PyPI 软件包，并导致数十万次恶意软件包下载。这些易受攻击的软件包下载量已超过 10 万次，或已活跃超过 6 个月。

JFrog安全研究人员Andrey Polkovnychenko和Brian Moussalli在与《黑客新闻》分享的一份报告中说："这种攻击技术涉及劫持PyPI软件包，一旦这些软件包被原所有者从PyPI索引中删除，就操纵重新注册这些软件包的选项。

这种被称为“Revival Hijack”的技术利用了一项政策漏洞，允许攻击者在原始开发人员将软件包从PyPI中删除后重新注册并劫持软件包名称。

与传统的域名抢注攻击不同，Revival Hijack攻击利用的是用户拼写错误的软件包名称，而传统域名抢注攻击则利用了热门软件包的删除和重新注册。当开发人员从PyPI中删除他们的项目时，软件包名称就会可供其他任何人注册。然后，攻击者可以上传这些软件包的恶意版本，毫无戒心的用户可能会下载并安装这些软件包，并认为它们是合法的。

JFrog 分享的统计数据显示，平均每月约有 309 个软件包被删除。出现这些情况的原因有很多，比如：缺乏维护（即废弃软件）、软件包以不同的名称重新发布，或将相同的功能引入官方库或内置 API。

这也构成了一个有利可图的攻击面，它比错别字抢注更有效，攻击者可以利用自己的账户，以相同的名称和更高的版本发布恶意软件包，感染开发者环境。

虽然PyPI确实有防止冒充作者和抢注的措施，但JFrog的分析发现，运行 “pip list--outdated ”命令会将假冒软件包列为原始软件包的新版本，而前者对应的是来自完全不同作者的不同软件包。

更令人担忧的是，运行 “pip install -upgrade ”命令会将实际软件包替换为虚假软件包，而软件包的作者却没有任何警告，这可能会让不知情的开发者面临巨大的软件供应链风险。

JFrog 表示，它采取的措施是创建一个名为 “security\_holding ”的新 PyPI 用户账户，用来安全地劫持易受攻击的软件包，并用空的占位符取代它们，以防止恶意行为者利用被删除的软件包。

此外，每个软件包的版本号都被指定为 0.0.0.1，这与依赖关系混乱攻击的情况正好相反，以避免在运行 pip 升级命令时被开发人员调用。

更令人不安的是，Revival 劫持已经在野外被利用，一个名为 Jinnis 的未知威胁行为者于 2024 年 3 月 30 日引入了一个名为 “pingdomv3 ”的软件包的良性版本，而就在同一天，原所有者（cheneyyan）从 PyPI 中删除了该软件包。

2024 年 4 月 12 日，新的开发者发布了一个更新，其中包含一个 Base64 编码的有效载荷，该有效载荷会检查是否存在 “JENKINS\_URL ”环境变量，如果存在，则会执行从远程服务器获取的未知下一阶段模块。

JFrog认为攻击者可能推迟了攻击的发送时间，或者将其设计得更有针对性，将其限制在特定的IP范围内。

新的攻击行为表明，威胁行为者正盯上更大规模的供应链攻击，以删除的 PyPI 软件包为目标，从而扩大攻击范围。建议企业和开发人员检查他们的 DevOps 管道，以确保他们没有安装已经从版本库中删除的软件包。

JFrog安全研究团队负责人Moussalli表示：利用处理已删除软件包的漏洞行为，攻击者可以劫持现有软件包，从而在不改变用户工作流程的情况下将其安装到目标系统中。

PyPI 软件包的攻击面正在不断扩大。尽管在此进行了主动干预，但用户仍应始终保持警觉，并采取必要的预防措施来保护自己和 PyPI 社区免受这种劫持技术的侵害。

> 参考来源：[Researchers Find Over 22,000 Removed PyPI Packages at Risk of Revival Hijack (thehackernews.com)](https://thehackernews.com/2024/09/hackers-hijack-22000-removed-pypi.html)

# PyPI

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