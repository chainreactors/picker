---
title: 黑客滥用AWS泄露的信息进行云狩猎
url: https://www.freebuf.com/news/418985.html
source: FreeBuf网络安全行业门户
date: 2025-01-04
fetch_date: 2025-10-06T20:10:20.316332
---

# 黑客滥用AWS泄露的信息进行云狩猎

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

黑客滥用AWS泄露的信息进行云狩猎

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客滥用AWS泄露的信息进行云狩猎

2025-01-03 11:10:50

所属地 上海

名为“EC2 Grouper”的黑客组织，近年来一直在利用AWS工具以及泄露的凭证对云环境展开狩猎型攻击。在过去的数年里，这个相当活跃的威胁行为主体在数十个客户环境中被发现，这使其成为网络安全专家追踪的最活跃的组织之一。

![](https://image.3001.net/images/20250103/1735874034_677755f204ca51a03dc1f.jpg!small)

Fortinet的研究人员发现，“EC2 Grouper”有一个显著特点，那就是始终使用AWS工具，尤其偏爱利用PowerShell来实施攻击。该组织会采用独特的用户代理字符串和安全组命名规范，通常会创建多个名称类似“ec2group”、“ec2group1”一直到“ec2group12345”的安全组。

攻击者主要是从与有效账户相关的代码库中窃取凭证。一旦获取这些凭证后，他们就会借助API进行侦察、创建安全组以及配置资源。攻击策略包括调用DescribeInstanceTypes来盘点EC2类型，还会调用DescribeRegions来收集有关可用区域的信息。

有趣的是，研究人员并未观察到他们调用AuthorizeSecurityGroupIngress，而这一操作通常是配置对使用安全组启动的EC2实例的入站访问所必需的。不过，研究人员注意到了他们调用CreateInternetGateway和CreateVpc的情况，这些操作是实现远程访问所必需的。

虽然该组织的最终目标还没有被确定，但是专家认为资源劫持可能是他们的主要目的。

报告指出，在受感染的云环境中并没有发现基于特定目标的手动操作或者行动。检测“EC2 Grouper”的活动对安全团队来说是一项重大挑战。由于像用户代理和组名称这类传统指标具有短暂性，所以已被证实对于全面的威胁检测并不可靠。

相反，专家建议采用更为细致的方法，将多个弱信号关联起来，从而准确识别恶意行为。建议组织实施多种安全措施，以降低与“EC2 Grouper”以及类似威胁相关的风险。这些措施包括利用云安全态势管理（CSPM）工具持续监控和评估云环境安全状况，实施异常检测技术来识别异常行为，并且对分配给用户和实例的所有角色遵循最小权限原则。

随着云环境依旧是复杂威胁行为主体的主要攻击目标，“EC2 Grouper”这类组织的被发现和分析凸显了高级检测机制和强大安全实践在保护数字资产和敏感信息方面的重要性。

参考来源：<https://cybersecuritynews.com/ec2-grouper-hackers-abusing-aws-tools/>

# 数据安全

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