---
title: 新的加密货币 Dero 挖矿活动，正以Kubernetes集群为目标进行
url: https://www.freebuf.com/news/360635.html
source: FreeBuf网络安全行业门户
date: 2023-03-17
fetch_date: 2025-10-04T09:51:23.935667
---

# 新的加密货币 Dero 挖矿活动，正以Kubernetes集群为目标进行

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

新的加密货币 Dero 挖矿活动，正以Kubernetes集群为目标进行

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新的加密货币 Dero 挖矿活动，正以Kubernetes集群为目标进行

2023-03-16 13:27:22

所属地 上海

![](https://image.3001.net/images/20230316/1678935094_641284365dab3772a5f08.png!small)

CrowdStrike在一份新报告中说：新的Dero加密货币开采活动集中定位在Kubernetes集群，该集群在Kubernetes API上启用了匿名访问，并在可从互联网访问的非标准端口上进行监听。

这一发展标志着从Monero的一个明显转变，Monero是此类活动中普遍使用的加密货币。这可能与Dero 提供更大的奖励和更好的匿名功能有关。

这些攻击是由一个不知名的攻击者进行的，首先是扫描Kubernetes集群，认证设置为--anonymous-auth=true，这允许匿名请求服务器，从三个不同的美国IP地址投放初始有效载荷。

这包括部署一个名为 "proxy-api "的Kubernetes DaemonSet，反过来，它被用来在Kubernetes集群的每个节点上投放一个恶意的pod，以启动采矿活动。

![](https://image.3001.net/images/20230316/1678935115_6412844baa33cc146bbac.png!small)

同时，DaemonSet的YAML文件被安排运行一个Docker镜像，其中包含一个 "暂停 "二进制文件，这实际上是Dero币的矿工。

该公司指出：在合法的Kubernetes部署中，pause容器被Kubernetes用来启动一个pod。攻击者可能使用相同的名字来混入，以避免常规的检测。

这家网络安全公司说，它发现了一个平行的Monero挖矿活动，也针对暴露的Kubernetes集群，试图删除与Dero活动相关的现有 "proxy-api "DaemonSet。

这表明加密劫持团体之间正在进行角力，他们争夺云资源，以获取并保留对机器的控制权，并消耗其所有资源。这两个活动都在试图寻找未被发现的Kubernetes攻击面，并正在进行争夺。

> 参考链接：https://thehackernews.com/2023/03/new-cryptojacking-operation-targeting.html

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