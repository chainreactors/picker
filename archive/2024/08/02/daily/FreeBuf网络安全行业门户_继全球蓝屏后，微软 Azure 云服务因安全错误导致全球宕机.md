---
title: 继全球蓝屏后，微软 Azure 云服务因安全错误导致全球宕机
url: https://www.freebuf.com/news/407481.html
source: FreeBuf网络安全行业门户
date: 2024-08-02
fetch_date: 2025-10-06T18:03:04.836330
---

# 继全球蓝屏后，微软 Azure 云服务因安全错误导致全球宕机

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

继全球蓝屏后，微软 Azure 云服务因安全错误导致全球宕机

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

继全球蓝屏后，微软 Azure 云服务因安全错误导致全球宕机

2024-08-01 10:49:33

所属地 上海

7月30日，微软Azure云服务全球宕机约8小时。该事件由一次DDoS攻击引起，成功触发系统保护机制，但这些防御机制中的实施错误反而进一步放大了影响，最终造成一次大宕机事件。据英国广播公司报道，此次中断持续了大约 10 个小时，影响了水务公司、法院、银行和其他类型的组织。![](https://image.3001.net/images/20240801/1722480553_66aaf7a92209d7cff29d6.jpg!small)

Azure云服务早已恢复，微软表示将在72小时内对该事件进行评估，并在两周内发布更详细的报告。

据媒体报道，Azure云服务中断从美国东部时间大约早上7:45开始，一直持续到下午3:43。这次攻击影响了Azure的多个服务，包括Azure应用服务、Azure物联网中心、应用洞察、日志搜索警报和Azure策略，以及主要的Azure门户，Microsoft 365和Microsoft Purview数据保护服务的一部分。

7月31日，微软表示，此次DDoS攻击导致了“意外的使用量激增，使得Azure Front Door（AFD）和Azure内容分发网络（CDN）组件的性能低于可接受的阈值。”从而进一步导致歇性的服务错误、超时和延迟问题。

一个令人费解的结果是，虽然此次触发事件是DDoS攻击，但更关键的原因是微软Azure云服务的DDoS保护机制被激活，防御实施中的错误放大了攻击的影响，而不是降低攻击影响。

**简单来说就是，网络安全防护反过来把业务干宕机了。**

目前微软还没有公布导致DDoS攻击攻击的防御错误具体内容，但很明显，公司为支持DDoS缓解工作所做的初始网络配置更改可能导致了一些意外的“副作用”。

“我们的团队将完成一次内部回顾，以更详细地了解事件，”微软表示。“我们将在大约72小时内发布初步事后审查（PIR），分享更多关于发生了什么以及我们如何应对的细节。”

Tenable的员工研究工程师Rody Quinlan表示，组织可以通过各种实施错误无意中放大网络攻击。

“例如配置不当的速率限制、效率低下的负载均衡、防火墙配置错误、过于激进的安全规则、资源扩展不足、错误的流量过滤和依赖单点故障等，这些错误可能导致合法流量被阻止、服务器过载、防火墙瓶颈和关键服务下线。”

尽管微软的初步响应可能促成了本周Azure服务的问题，但这一事件再次提醒人们，对于寻求破坏和降低目标在线存在的对手来说，DDoS攻击仍然是有效的。

Cloudflare今年早些时候的一份报告发现，网络层DDoS攻击同比增长了117%。部分原因是在黑色星期五和假日购物季节期间，针对零售、航运和公关网站的DDoS攻击有所增加。

许多攻击也是由寻求发出特定信息或表达特定政治立场的团体发起。Cloudflare表示，它观察到针对台湾、以色列和巴勒斯坦网站的DDoS攻击在这些地区的地缘政治紧张局势中大幅增加，以及对环境科学网站的攻击。

有安全专家指出，DDoS的趋势通常是周期性的，但目前的趋势是攻击规模越来越大，持续时间越来越短。最新数据表明，去年攻击规模平均增长了183%，平均规模为0.80Gbps。在2022年和2023年之间，DDoS攻击的平均持续时间降至仅超过101分钟，但目前，81%的DDoS攻击持续时间不到90分钟。

“攻击持续时间减少的部分原因是攻击者在给企业造成干扰时变得越来越高效，其中可能与AI技术的大规模应用有关。缓解DDoS干扰的关键是拥有实时流量分析能力、可扩展的云基础设施、冗余系统和智能负载均衡以防止过载。因此，适当的速率限制、节流和WAFs过滤恶意流量，以及定期软件和硬件漏洞修复对保护系统至关重要。

参考来源：https://www.darkreading.com/cloud-security/microsoft-azure-ddos-attack-amplified-cyber-defense-error

# 网络安全 # 系统安全 # 网络安全技术

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