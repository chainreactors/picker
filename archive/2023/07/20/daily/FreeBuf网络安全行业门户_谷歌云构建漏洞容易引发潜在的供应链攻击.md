---
title: 谷歌云构建漏洞容易引发潜在的供应链攻击
url: https://www.freebuf.com/news/372456.html
source: FreeBuf网络安全行业门户
date: 2023-07-20
fetch_date: 2025-10-04T11:55:51.811394
---

# 谷歌云构建漏洞容易引发潜在的供应链攻击

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

谷歌云构建漏洞容易引发潜在的供应链攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

谷歌云构建漏洞容易引发潜在的供应链攻击

2023-07-19 11:22:16

所属地 上海

![](https://image.3001.net/images/20230719/1689733975_64b74b57ea1af82f90a36.png!small)

云安全公司Orca Security在谷歌云构建（Google Cloud Build）服务中发现了一个关键的设计漏洞，该漏洞会让攻击者的权限升级，使他们可以在未经授权的情况下访问谷歌构件注册表（Google Artifact Registry）代码库。

该漏洞被称为 "Bad.Build"，可使威胁者冒充谷歌云构建管理的服务账户，针对构件注册表运行 API 调用，并控制应用程序映像。

这样，他们就可以注入恶意代码，从而在客户环境中部署恶意软件，导致潜在的供应链攻击。

Orca安全研究员Roi Nisimi表示：潜在的威胁可能是多种多样的，所有使用构件注册中心作为主要或次要镜像库的组织都应该警惕。

最直接的影响是破坏依赖于这些镜像的应用程序。这也可能导致 DOS、数据窃取和向用户传播恶意软件。正如我们在 SolarWinds 以及最近的 3CX 和 MOVEit 供应链攻击中所看到的那样，这可能会产生深远的影响。

Orca Security的攻击利用了cloudbuild.builds.create来升级权限，允许攻击者使用artifactregistry权限来篡改谷歌Kubernetes引擎（GKE）的docker镜像，并以root身份在docker容器内运行代码。

在 Orca Security 报告该问题后，谷歌安全团队实施了部分修复措施，撤销了默认云构建服务账户中与构件注册表无关的 logging.privateLogEntries.list 权限。

但是，这一措施并不能直接解决Artifact Registry中的底层漏洞，权限升级和供应链攻击风险依然存在。

因此，企业必须密切关注谷歌云构建服务账户的行为。应用 "最小特权原则"（Principle of Least Privilege）和实施云检测与响应功能来识别异常从而降低风险。

美国东部时间 7 月 18 日谷歌发表了如下声明：

> 我们创建了漏洞奖励计划，专门用于识别和修复类似的漏洞。我们非常感谢 Orca 和更多的安全社区参与这些计划。我们感谢研究人员所做的工作，并已根据他们的报告在 6 月初发布的安全公告中进行了修复。
>
> 参考链接：https://www.bleepingcomputer.com/news/security/google-cloud-build-bug-lets-hackers-launch-supply-chain-attacks/

# 资讯 # 漏洞

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