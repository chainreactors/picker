---
title: Crowdstrike蓝屏事件自查结果：错在流程而非人
url: https://www.freebuf.com/news/406953.html
source: FreeBuf网络安全行业门户
date: 2024-07-26
fetch_date: 2025-10-06T17:42:57.153466
---

# Crowdstrike蓝屏事件自查结果：错在流程而非人

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

Crowdstrike蓝屏事件自查结果：错在流程而非人

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Crowdstrike蓝屏事件自查结果：错在流程而非人

2024-07-25 10:30:51

所属地 上海

![](https://image.3001.net/images/20240725/1721874520_66a1b858db71ca03f731b.png!small)**本周三，CrowdStrike发布了导致全球大规模系统崩溃的初步事件评估报告（PIR）。**

此前业界传闻该公司潜入了类似SolarWinds供应链攻击的“特工”，但初步调查结果显示是CrowdStrike的更新工具和流程存在漏洞，**但CrowdStrike否认自己在该事件中存在“不负责任”的行为。**

CrowdStrike解释称，事件的导火索是一次为收集某C2框架新威胁技术遥测数据进行的内容配置更新。由于内容验证器的一个错误，未能检查出模版实例中包含有问题的内容数据。（虽然CrowdStrike没有具体说明是何种C2框架，但一些研究人员认为此更新试图检测的是Cobalt Strike的新Named Pipe功能。）

## **测试流程存在严重漏洞**

CrowdStrike蓝屏事件内部调查受到业界的广泛关注，因为人们不明白CrowdStrike为何会犯下如此低级的测试流程错误。

报告指出，事件的根源是CrowdStrike内容更新器的漏洞，对快速响应内容的漏洞签名更新检测不太严格，导致错误配置通过了验证（同时又没有进行必要的稳定性测试），瘫痪了全球数百万台Windows系统。

CrowdStrike使用其传感器内容配置系统创建模板实例来描述要检测的威胁行为，并通过更新进程间通信（IPC）模板类型的配置数据（存储在通道文件中），使Falcon传感器能够检测到主机设备上的最新可疑行为。

这些IPC模板实例通过CrowdStrike称为“快速响应内容”的定期内容更新进行交付，以便在不需要完整更新传感器的情况下，通过简单更改配置数据来调整传感器的检测能力。

令人吃惊的是，虽然曝出测试工具和流程漏洞，但CrowdStrike辩称在灾难发生之前，该公司已经采取了“负责任”的行动。CrowdStrike的理由是该公司仅仅对一个已经测试并投入生产环境的组件进行了“小的”配置更新，但组件本身经过了充分严格的测试。

据CrowdStrike介绍，导致灾难性事件的错误配置所使用的IPC模板类型及其相应的模板实例通过了完整的压力测试，包括资源利用率、系统性能影响、事件量和对手系统交互等。内容验证器检查并批准了2024年3月5日、4月8日和4月24日推送的三个独立实例，未发现问题。

然而，7月19日部署的两个新IPC模板实例中包含一个错误配置，由于内容验证器的漏洞而未被发现。由于对之前测试和成功部署的（通道文件291的）IPC模板类型的信任，更新未经过额外验证，因此未在推送至运行Falcon 7.11及更高版本的在线主机之前被发现，导致全球大规模IT停机。

尽管CrowdStrike在发现错误后立即撤回了更新，但为时已晚。约850万台Windows系统在内容解释器处理新的配置更新时发生越界内存读取并崩溃。

## **整改：增加五种附加测试**

为了防止类似事件再次发生，CrowdStrike正在更新流程中增加多个附加测试，具体包括：

* 本地开发人员测试：确保每个更新在部署前都经过开发人员的本地测试。
* 内容更新和回滚测试：在推出之前进行全面的内容更新和回滚测试。
* 压力测试、模糊测试和故障注入：通过多种测试方法确保更新的稳定性。
* 稳定性测试：评估更新对系统稳定性的影响。
* 内容接口测试：验证内容接口的正确性和安全性。

此外，CrowdStrike还将对内容验证器增加额外的验证检查，并改进内容解释器中的错误处理机制，以避免类似错误导致Windows机器无法运行。

在快速响应内容部署方面，CrowdStrike计划进行以下更改（尤其值得注意的变化是将更新时间和地点的控制权交给客户）：

* 实施交错部署策略，从小型金丝雀部署开始，然后逐渐扩展。
* 改进部署期间对传感器和系统性能的监控，使用反馈来指导分阶段推出。
* 为客户提供对快速响应内容更新交付的更多控制权限，允许客户选择何时何地部署更新。
* 通过发布说明提供内容更新详情，客户可以订阅以获取及时信息。

最后，CrowdStrike承诺将在未来发布更详细的事件原因分析报告，内部调查完成后将公布更多细节。

来源：GoUpSec

# CrowdStrike # 测试 # 配置错误

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

测试流程存在严重漏洞

整改：增加五种附加测试

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