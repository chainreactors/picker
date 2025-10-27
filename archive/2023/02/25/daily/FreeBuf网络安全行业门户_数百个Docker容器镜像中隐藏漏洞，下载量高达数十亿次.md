---
title: 数百个Docker容器镜像中隐藏漏洞，下载量高达数十亿次
url: https://www.freebuf.com/news/358546.html
source: FreeBuf网络安全行业门户
date: 2023-02-25
fetch_date: 2025-10-04T08:04:25.601213
---

# 数百个Docker容器镜像中隐藏漏洞，下载量高达数十亿次

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

数百个Docker容器镜像中隐藏漏洞，下载量高达数十亿次

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

数百个Docker容器镜像中隐藏漏洞，下载量高达数十亿次

2023-02-24 14:01:46

所属地 上海

Rezilion发现了数百个Docker容器镜像的存在，这些镜像包含了大多数标准漏洞扫描器和SCA工具都没有检测到的漏洞。

![](https://image.3001.net/images/20230224/1677207811_63f82903815452b9015a4.png!small)

研究发现，数百个Docker容器镜像中隐藏着许多高危险性/关键性的漏洞，这些容器镜像的下载量合计达数十亿次。其中包括已被公开的高知名漏洞。

一些隐藏的漏洞在野外被积极利用，这些漏洞是CISA已知被利用漏洞合集中的一部分，包括CVE-2021-42013、CVE-2021-41773、CVE-2019-17558。

经过研究发现漏洞存在的根本原因是无法检测未被软件包管理器管理的软件组件。

该研究解释了标准漏洞扫描器和SCA工具的固有操作方法是如何依靠从软件包管理器获取数据来了解扫描环境中存在哪些软件包的，这使得它们容易在多种常见情况下遗漏易受攻击的软件包，即软件的部署方式规避了这些软件包管理器。

根据该报告，规避部署方式的软件包管理器在Docker容器中很常见。研究小组已经发现了超过10万个以绕过软件包管理器的方式部署代码的容器镜像，包括DockerHub的大多数官方容器镜像。这些容器要么已经包含隐藏的漏洞，要么在其中一个组件的漏洞被发现后容易出现隐藏的漏洞。

研究人员确定了四种不同的情况，在这些情况下，软件的部署没有与软件包管理器进行交互，如应用程序本身、应用程序所需的运行、应用程序工作所需的依赖性，以及在容器镜像构建过程结束时没有删除的应用程序部署，并展示了隐藏的漏洞如何找到容器镜像。

"我们希望这项研究能让开发者和安全从业者了解这一漏洞的存在，这样他们就能采取适当的行动来减少风险，并推动供应商和开源项目增加对这些类型场景的支持，"Rezilion公司漏洞研究部主任Yotam Perkal说。"

最后需要提醒大家的是，只要漏洞扫描程序和SCA工具无法适应这些情况，任何以这种方式安装软件包或可执行文件的容器映像最终都可能包含'隐藏'漏洞。

> 参考链接：https://www.helpnetsecurity.com/2023/02/23/hidden-vulnerabilities-docker-containers/

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