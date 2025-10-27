---
title: 美官方为软件供应商提出供应链安全指南
url: https://www.freebuf.com/news/349435.html
source: FreeBuf网络安全行业门户
date: 2022-11-11
fetch_date: 2025-10-03T22:23:41.803497
---

# 美官方为软件供应商提出供应链安全指南

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

美官方为软件供应商提出供应链安全指南

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)
* [咨询](https://www.freebuf.com/consult)

美官方为软件供应商提出供应链安全指南

2022-11-10 16:38:06

所属地 上海

10月31日，美国国家安全局（NSA）、网络安全及基础设施安全局（CISA）、国家情报总监办公室（ODNI）携手发布了保护软件供应链的实操指南。该指南内容总共有40页，主要提及了软件供应商在供应链中所需要承担的责任和改进方法。指南中提及的供应商主要责任包括：

第一，努力识别可能危及组织、软件开发、软件本身和软件交付（即内部部署或SaaS）环境的威胁，并实施相关的缓解措施；第二，作为客户和软件开发团队之间的联络人，需要确保软件在安全环境下开发，并通过安全渠道交付；第三，供应商通过合同协议、软件发布和更新、通知和漏洞缓解机制来提供所交付的软件额外的安全功能。

对于软件供应链的安全实践，NSA、CISA与ODNI有着一系列的规划，相关规划落实在由NSA及CISA所主导的政企工作小组所开发的“长期安全框架”（Enduring Security Framework，ESF）之中。这一框架将产出指导美国重大网络基础设施的安全指南，针对软件供应链总计有3部分：首先是今年9月发布、锁定软件开发者的《Securing the Software Supply Chain for Developers》，10月31日发布的指南适用于软件供应商，下一步则会发布针对软件供应链客户使用者的版本。![](https://image.3001.net/images/20221110/1668069393_636cb811256c234907140.png!small)

该指南针对软件供应商的供应链安全提出了非常多的建议，现将主要要点如下概述：

**第一，****该指南敦促软件供应商在软件收发供货过程中保证供应链安全****。**供应商有义务做到确认发货的软件与客户收到的软件是一样的；需要创建一个安全的哈希值来验证文件是否传送正确；需要确保软件传输通信渠道是安全的。需要通过利用国际公认的标准（如NIST SSDF）对软件进行最终检查，这有助于确保在软件发布前满足软件功能和安全要求。

**第二，该指南认为供应商应提供一种机制，通过在整个软件生命周期内对代码进行数字签名，来验证软件发布的完整性。**经过数字签名的代码，使代码接收者以及客户能够积极地验证和信任代码的来源和完整性。

**第三，该指南要求供应商必须确保本地开发的软件和由第三方供应商提供的任何组件都需要符合安全要求。**由于第三方提供的软件和模块通常会包含在供应商发布的软件产品中，为此，供应商可以通过召集专家评估第三方提供的软件是否符合适用的安全要求、与第三方软件提供者签订合同协议来解决潜在的第三方软件问题。

**第四，该指南认为供应商应尽一切努力，确保提供给客户的任何软件中不存在公开的或容易识别的漏洞。**在向客户提供软件之前，需要测试、了解和消除软件中的漏洞，以防止提供容易被破坏的代码。需要建立一个由架构师、开发、测试人员、密码学家和人为因素工程师组成的漏洞评估小组，其任务是识别软件中可利用的弱点。需实时检查与第三方软件和与软件相关的开放源码组件相关的软件物料清单（SBOM）。在相关问题公布后，建立并遵循企业对嵌入式组件升级的指导。

该指南下载地址：

<https://media.defense.gov/2022/Oct/31/2003105368/-1/-1/0/SECURING_THE_SOFTWARE_SUPPLY_CHAIN_SUPPLIERS.PDF>

> 文章来源： [公安部第三研究所网研基地](https://mp.weixin.qq.com/s/UbNAktwp-IKwqrZMZdCcbw)

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