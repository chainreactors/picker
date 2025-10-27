---
title: 知名基因测序仪曝BIOS漏洞，可禁用疾病监测和疫苗开发
url: https://www.freebuf.com/news/419295.html
source: FreeBuf网络安全行业门户
date: 2025-01-09
fetch_date: 2025-10-06T20:10:22.020888
---

# 知名基因测序仪曝BIOS漏洞，可禁用疾病监测和疫苗开发

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

知名基因测序仪曝BIOS漏洞，可禁用疾病监测和疫苗开发

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

知名基因测序仪曝BIOS漏洞，可禁用疾病监测和疫苗开发

2025-01-08 13:51:02

所属地 上海

美国生物技术公司Illumina的iSeq 100 DNA测序仪存在BIOS/UEFI漏洞，这可能导致攻击者禁用用于检测疾病和开发疫苗的设备。Illumina iSeq 100被宣传为医疗和研究实验室可使用的、能提供“快速且具成本效益的遗传分析”的DNA测序系统。

![](https://image.3001.net/images/20250108/1736315700_677e1334000525c859e43.png!small)

固件安全公司Eclypsium对Illumina设备中的BIOS固件进行了分析，发现该设备启动时没有标准的写入保护，这就容易遭受重写攻击，从而可能“使系统变砖”或者植入长期存在的恶意软件。

## 过时且易受攻击的BIOS

研究人员发现，iSeq 100运行的BIOS固件版本过时，此版本在兼容性支持模式（CSM）下运行以支持旧设备，并且没有采用安全启动技术进行保护。

### 漏洞情况

Eclypsium的分析找出了五个主要问题，这些问题致使九个漏洞被利用，这些漏洞的严重程度为高或中等，其中一个漏洞的出现甚至可以追溯到2017年。

除了缺乏BIOS写入保护之外，iSeq 100设备还容易受到LogoFAIL、Spectre 2和微架构数据采样（MDS）攻击。虽然在CSM模式下启动能够支持传统设备，但对于敏感设备，特别是新一代设备而言，这种方式是不被推荐的。

研究人员还发现，iSeq 100上存在风险的BIOS（B480AM12 - 2018年4月12日）未启用固件保护，这就允许对启动设备的代码进行修改。再加上缺乏安全启动（安全启动可检查启动代码的有效性和完整性），任何恶意更改都不会被发现。

### 潜在影响范围

在报告中，Eclypsium强调他们的分析仅针对iSeq 100测序仪设备，但类似问题可能也存在于其他医疗或工业设备中。

研究人员解释说，医疗设备制造商会借助外部供应商提供系统的计算能力。就iSeq 100而言，它依赖IEI Integration Corp的OEM主板。由于IEI Integration Corp开发多种工业计算机产品，并且是医疗设备的原始设计制造商（ODM），Eclypsium认为在使用IEI主板的其他医疗或工业设备中“很可能发现这些或类似的问题”。

## 攻击可能造成的危害

研究人员还指出，如果攻击者已经攻陷设备，就可以利用这些漏洞修改固件，这可能导致系统变砖；有足够知识的威胁行为者还能篡改测试结果。Eclypsium表示：“如果这些设备中的数据被植入/后门操纵，那么威胁行为者可能会操纵包括伪造遗传病状的存在或缺席、操纵医疗治疗或新疫苗、伪造祖先DNA研究等在内的广泛结果。

Eclypsium将iSeq 100设备中的BIOS问题告知了Illumina，生物技术公司回复已向受影响的客户发布补丁。
该公司发言人表示，Illumina正在遵循其“标准流程，若需要任何缓解措施，将会通知受影响的客户”。

Illumina的代表称：“我们最初的评估表明这些问题不是高风险。”Illumina还强调致力于产品的安全性和基因组数据的隐私，已建立监督和问责流程，包括产品开发和部署的安全最佳实践，并且一直在努力改进为现场仪器提供安全更新的方式。

在报告中，Eclypsium的研究人员警告，能够覆盖iSeq 100上固件的威胁行为者“可以轻松禁用设备”。勒索软件行为者可能会通过接管高价值系统来破坏业务，因为他们的目的是让受害者的恢复工作困难重重，从而迫使受害者支付赎金。除了出于经济利益的攻击者外，国家行为者也可能会对DNA测序系统感兴趣，因为这些系统“对于检测遗传病、癌症、识别耐药细菌以及疫苗的生产至关重要”。

2023年，美国网络安全基础设施安全局（CISA）和食品药品监督管理局（FDA）发布了关于Illumina的通用复制服务（UCS）中的两个漏洞的紧急咨询，这两个漏洞存在于全球医疗设施和实验室使用的多种产品中。其中一个问题（CVE - 2023 - 1968）的严重程度最高，另一个（CVE - 2023 - 1966）的严重程度较高。

参考来源：<https://www.bleepingcomputer.com/news/security/bios-flaws-expose-iseq-dna-sequencers-to-bootkit-attacks/>

# 漏洞

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

过时且易受攻击的BIOS

* 漏洞情况
* 潜在影响范围

攻击可能造成的危害

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