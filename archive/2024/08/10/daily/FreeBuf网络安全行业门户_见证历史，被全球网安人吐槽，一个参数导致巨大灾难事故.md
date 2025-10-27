---
title: 见证历史，被全球网安人吐槽，一个参数导致巨大灾难事故
url: https://www.freebuf.com/news/408183.html
source: FreeBuf网络安全行业门户
date: 2024-08-10
fetch_date: 2025-10-06T18:05:10.398056
---

# 见证历史，被全球网安人吐槽，一个参数导致巨大灾难事故

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

见证历史，被全球网安人吐槽，一个参数导致巨大灾难事故

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

见证历史，被全球网安人吐槽，一个参数导致巨大灾难事故

2024-08-09 10:49:17

所属地 上海

在7月19日引发全球网络动荡的数百万台Windows系统电脑蓝屏宕机后，CrowdStrike于当地时间8月7日发布了一份事件分析报告，从技术角度对故障原因进行了详细阐述。

这份长达12页的根本原因分析 (RCA)相比于在事发5天后发布的初步事故后调查 （PIR），从调查结果、缓解措施和技术细节方面均提供了更加细致的内容，但同时也暴露出这家网安巨头企业在产品质量和测试方面存在重大瑕疵和纰漏。

一句话概括：一个令人大跌眼镜的小错误引发了一场巨大灾难。CrowdStrike公司调查报告发布后，不仅没有获得大家的谅解，反而引发全球安全人的疯狂吐槽。

![](https://image.3001.net/images/20240809/1723187639_66b5c1b733b7f751254f6.png!small)

## 事件原因：就只是多了一个参数？

根据这份名为“通道文件 291事件”（Channel File 291 Incident）的报告内容分析，CrowdStrike 于今年2月为识别并修复最新高级威胁的Falcon 传感器发布了7.11版本，其中包括了用于Windows 进程间通信 （IPC） 机制的新模板类型，该模板实例通过编号为 291 的相应通道文件作为快速响应内容交付给传感器，以便查看并检测滥用命名管线及其他 Windows 进程间通信（IPC）机制的新型攻击技术。

![](https://image.3001.net/images/20240809/1723187556_66b5c164d484e31728a28.png!small)

报告截图

但新的IPC模板类型定义了21个输入参数字段，而调用带有通道文件291模板实例的内容解释器的集成代码仅提供了20个输入值进行匹配。CrowdStrike称这种不匹配躲过了多层构建验证和测试，造成这一情况的部分原因在于测试期间和最初的 IPC 模板实例中对第 21 个输入值使用了通配符匹配标准。

在7月19日事发当天，CrowdStrike在更新中部署了两个新的 IPC 模板实例，其中一个对第 21 个输入参数采用了非通配符匹配标准，因此需要传感器检查第 21 项输入参数。在将此通道文件传送给传感器之前，原有通道版本中的 IPC 模板实例从未使用过第 21 项输入参数。内容验证器评估了新的模板实例，但评估过程同样以 IPC 模板类型能够提供 21 项输入为前提和基本预期。

因而，接收到携带问题内容的新版通道文件 291 传感器在内容解释器中便会存在越界读取问题。 在操作系统发出下一次 IPC 通知时，对新的 IPC 模板实例进行了评估，指定与第 21 个输入值进行比较，但内容解释器预期只能处理20 个值，在尝试访问第 21 个值时产生了超出输入数据数组末尾的越界内存读取，最终导致系统崩溃。

总结下来，是在7月19日的更新当中，Falcon引入的新传感器预计只更新20项参数，但实际输入了21项参数，且对第21项参数缺乏非通配符匹配标准的特定测试，引发越界内存读取导致系统崩溃。

是的，你没有理解错，就是单纯的多个一个参数，引发了一场全球电脑集体蓝屏事件。以至于被业内专家吐槽，如此糟糕的代码，如此糟糕的产品，如此糟糕的测试。

CrowdStrike也在报告中列出了如下改进措施：

> * 对模板类型输入字段实施编译时验证
> * 在内容解释器中增加运行时数组边界检查
> * 扩大模板类型测试范围，以涵盖更多匹配标准
> * 更正内容验证器中的逻辑错误
> * 引入模板实例的分阶段部署
> * 提供客户对快速响应内容更新的控制权

## 一个令网安人大跌眼镜的错误

这份报告虽然很详细地列出了故障原因，但从中暴露出的问题也引发了部分专家对这家拥有雄厚技术实力网安公司的指责。

微软独立安全研究员Kevin Beaumont表示，“CrowdStrike 在部署之前，频道更新没有在真实的 Windows PC 上进行测试，它们依赖于自动化的定制代码测试。这一点在报告中没有提及，而这才是导致事故的真正原因。“

![](https://image.3001.net/images/20240809/1723184357_66b5b4e51236e6610529c.png!small)工程师 Eduardo Bellani 表示，”问题的核心是一个数组越界错误，这是缓冲区溢出的特殊情况，在开发 Crowdstrike 系统的 C++ 语言中被视为未定义行为。对于这种关键性的软件，这样的问题不应该发生。“

他还称：”RCA 中提出的所有技术缓解措施都只是堵塞漏洞。但安全不能以这种方式实现，此类努力需要在一开始就将安全性融入设计、工具和语言中。如果我是 Crowdstrike 的客户，我会担心未来。”

可见，这份长达12页的报告，暴露了Crowdstrike在做部署时测试环节的缺位，以及没有反映如何从根本上避免类似缺陷问题再次发生。

毫无疑问，这次事件是对安全大厂的一次彻底“祛魅”，给一些所谓安全、可靠且受众广泛的安全产品给予了当头一棒，如果厂商对产品无法保证严格的安全测试，无法进一步牢固产品质量基础，及时发现并修复存在的错误，那么下一次重大事故的发生将只是时间问题。

CrowdStrike表示，已经聘请了两家独立的第三方软件安全供应商，对Falcon传感器代码进行进一步审查，以确保安全性和质量保证，同时还将对从开发到部署的端到端质量流程进行独立审查。

**参考资料：**

> [CrowdStrike Publishes Technical Root Cause Analysis of Faulty Falcon Update](https://cybersecuritynews.com/crowdstrike-root-cause-analysis/#google_vignette)
>
> [Massive CrowdStrike outage caused by an out-of-bounds memory error](https://www.scmagazine.com/news/massive-crowdstrike-outage-caused-by-an-out-of-bounds-memory-error)
>
> [External Technical Root Cause Analysis — Channel File 291](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf)

# 系统安全

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

事件原因：就只是多了一个参数？

一个令网安人大跌眼镜的错误

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