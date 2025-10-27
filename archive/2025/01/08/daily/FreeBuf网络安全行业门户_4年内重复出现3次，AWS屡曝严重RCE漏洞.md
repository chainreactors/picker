---
title: 4年内重复出现3次，AWS屡曝严重RCE漏洞
url: https://www.freebuf.com/news/419192.html
source: FreeBuf网络安全行业门户
date: 2025-01-08
fetch_date: 2025-10-06T20:10:10.034338
---

# 4年内重复出现3次，AWS屡曝严重RCE漏洞

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

4年内重复出现3次，AWS屡曝严重RCE漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

4年内重复出现3次，AWS屡曝严重RCE漏洞

2025-01-07 11:27:24

所属地 上海

据Cyber Security News消息，因为Python 包安装过程方面的严重失误，Amazon Web Services （AWS） 在过去四年中通过其 Neuron SDK 三次引入了相同的远程代码执行 （RCE） 漏洞。

![](https://image.3001.net/images/20250107/1736220779_677ca06bd7abc08ec4d88.png!small)

该问题于 2022 年 4 月首次被发现，当时 Giraffe Security 标记了 AWS 的 Neuron SDK 中的一个漏洞，该开发工具包是一组 Python 库，可在 AWS 的专用硬件上启用机器学习工作负载。

该问题源于 AWS 的官方安装说明和文档，其中建议使用如下命令：

> pip install transformers-neuronx --extra-index-url=https://pip.repos.neuron.amazonaws.com

乍一看，该命令似乎很简单，指示 Python 的软件包管理器从特定于 AWS 的存储库 （） 安装软件包。但是，这种方法包含根植于如何处理参数的隐藏危险。

> piptransformers-neuronxhttps://pip.repos.neuron.amazonaws.compip

该参数并不专门将包下载限制为指定的私有存储库，相反，它允许在默认的公共 PyPi 存储库中搜索包，如果在指定索引中找不到包，执行退回操作。这会产生一个严重漏洞：攻击者可以将同名的包上传到 PyPi，诱骗用户下载和执行恶意代码。

2022年， Giraffe Security 通过在 PyPi 上声明未受保护的 AWS 软件包名称（如 mx-neuron）确认了这一漏洞，并通过 AWS 的漏洞赏金计划报告了这一漏洞。AWS 迅速解决了这个问题做出反应，将受影响软件包的 "假 "版本上传到 PyPi，防止了进一步的利用。 然而，问题的根源——对 --extra-index-url 参数的错误依赖仍未得到解决。

2022 年的进一步研究显示，这并非此类漏洞的首次出现。 来自开源软件数据库 libraries.io 的历史数据显示，AWS 的 torch-neuron 软件包在 2020 年也曾暴露过类似的漏洞，这表明也曾出现过同样的依赖关系混乱风险。当时，一名安全研究人员将该程序包的多个版本上传到 PyPi 以突出显示该漏洞，迫使 AWS 采取纠正措施。

尽管已多次发出警告并进行了修复，但 Giraffe Security 在 2024 年 12 月进行的最新调查显示，AWS 再次引入了相同的漏洞。

Amazon 一再的失误引发了人们的质疑。一方面，Amazon 对过去漏洞报告的快速反应表明确实有认真对待漏洞，但同样的漏洞反复出现，说明缺乏系统性的防范流程。这种情况凸显了一个重要的安全教训：即使是像 AWS 官方文档这样的可信来源也不一定安全。

虽然这个反复出现的问题看似是一个小众漏洞，但它对云生态系统的安全具有更广泛的影响。依赖关系混乱攻击已成为一个日益令人担忧的问题，尤其是当越来越多的组织依赖于私有软件包注册中心和 PyPi 或 npm 等公共软件源的情况下。 降低这些风险的责任不仅在于最终用户，也在于 AWS 等服务提供商，他们必须确保其工具和文档遵循安全最佳实践。

尽管 Giraffe Security 曾多次尝试联系亚马逊以征求意见，但一直没有得到回应。 作为全球最大的云服务提供商之一，AWS 在这一事件中未拿出强有力永久性解决方案的情况颇令人意外。

**参考来源：**

> [AWS Repeats Same Critical RCE Vulnerability 3 Times in 4 Years](https://cybersecuritynews.com/aws-repeats-same-critical-rce-vulnerability-3-times-in-4-years/)

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