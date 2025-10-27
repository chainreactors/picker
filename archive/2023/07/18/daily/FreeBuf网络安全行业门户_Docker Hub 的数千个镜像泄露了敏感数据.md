---
title: Docker Hub 的数千个镜像泄露了敏感数据
url: https://www.freebuf.com/news/372226.html
source: FreeBuf网络安全行业门户
date: 2023-07-18
fetch_date: 2025-10-04T11:55:56.314141
---

# Docker Hub 的数千个镜像泄露了敏感数据

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

Docker Hub 的数千个镜像泄露了敏感数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Docker Hub 的数千个镜像泄露了敏感数据

2023-07-17 11:01:48

所属地 上海

德国亚琛工业大学的研究人员发表的一项研究表明，Docker Hub 上托管的数以万计的容器镜像包含机密信息，使软件、在线平台和用户面临巨大的攻击面。

![](https://image.3001.net/images/20230717/1689563071_64b4afbf1cfb39121dee1.png!small)

Docker Hub 是一个基于云的存储库，供 Docker 社区存储、共享和分发 Docker 镜像，这些容器创建模板包括所有必要的软件代码、运行时刻、库、环境变量和配置文件，以便在Docker中轻松部署应用程序。

研究人员分析了来自 Docker Hub 和数千私人注册表的 337171 个镜像，发现大约 8.5% 包含私钥和 API 密钥等敏感数据，并且许多暴露的密钥都被积极利用，破坏了依赖它们的元素的安全性。

该研究从 337171 个 Docker 镜像中收集了包含 1647300 个层面的海量数据集，并尽可能从每个存储库中获取最新的镜像版本。使用正则表达式搜索特定数据分析显示，28621 个 Docker 镜像中暴露了 52107 个有效私钥和 3158 个不同的 API密钥。经过研究人员验证，这些不包括测试密钥、API密钥示例和无效匹配。大多数暴露的数据（95% 为私钥，90% 为 API密钥）都驻留在单用户映像中，这表明它们很可能是无意泄露的。

![](https://image.3001.net/images/20230717/1689563039_64b4af9f0571fe6ba16b3.png!small)调查结果

影响最大的是 Docker Hub，其暴露比例为 9.0%，而来自私有注册表的镜像暴露比例为 6.3%。这种差异可能表明 Docker Hub 用户通常比设置私有存储库的用户对容器安全性的了解较差。

## 使用暴露的密钥

接下来，研究人员确定了所暴露秘密的实际用途，以了解攻击面的大小。令人震惊的是，研究人员发现了 22082 个依赖于暴露私钥的受损证书，其中包括 7546 个私有 CA 签名证书和 1060 个公共 CA 签名证书。

这上千个 CA 签名证书尤其值得关注，因为这些证书通常被大量用户使用。在研究时，141 个 CA 签名的证书仍然有效，这在一定程度上降低了风险。

为了进一步确定暴露的秘密在野外的用途，研究人员使用了 Censys 数据库提供的全互联网测量结果，发现275269 台主机与泄露的密钥存在关联，其中包括了8674 个 MQTT和19 个 AMQP 主机可能传输隐私敏感的物联网 (IoT) 数据。

这种程度的暴露凸显了容器安全方面的巨大问题，以及在创建镜像时未首先清除镜像中的机密信息这类过失性错误。

关于API暴露，分析发现大多数容器（2920个）属于亚马逊AWS等云提供商，但也有一些涉及Stripe等金融服务。目前，研究人员还不清楚这些API在野外的具体利用情况。

> 参考来源：[Thousands of images on Docker Hub leak auth secrets, private keys](https://www.bleepingcomputer.com/news/security/thousands-of-images-on-docker-hub-leak-auth-secrets-private-keys/)

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

使用暴露的密钥

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