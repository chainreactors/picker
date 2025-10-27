---
title: 新版Prometei僵尸网络感染全球超过1万个系统
url: https://www.freebuf.com/news/360219.html
source: FreeBuf网络安全行业门户
date: 2023-03-14
fetch_date: 2025-10-04T09:30:25.944689
---

# 新版Prometei僵尸网络感染全球超过1万个系统

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

新版Prometei僵尸网络感染全球超过1万个系统

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新版Prometei僵尸网络感染全球超过1万个系统

2023-03-13 11:48:33

所属地 上海

![](https://image.3001.net/images/20230313/1678675680_640e8ee022b495a75d6a8.png!small)

自2022年11月以来，新版本的Prometei的僵尸网络已经感染了全球超过10000个系统。这些感染没有地域的限制，大多数受害网络在巴西、印度尼西亚和土耳其。

Prometei在2016年首次被发现，是一个模块化的僵尸网络，具有大量的组件和几种扩散方法，其中一些还包括利用ProxyLogon微软Exchange服务器的缺陷。

这个跨平台僵尸网络的目标是金融领域，主要是利用其受感染的主机池来挖掘加密货币和收获凭证。

在《黑客新闻》的报告中说，Prometei的最新变体（称为v3）在其现有功能的基础上进行了改进，以进行取证分析，并进一步在受害者机器上钻取访问。

![](https://image.3001.net/images/20230313/1678675767_640e8f37822303d485531.png!small)

其攻击序列如下：在成功站稳脚跟后，执行PowerShell命令，从远程服务器下载僵尸网络恶意软件。然后，Prometei的主要模块被用来检索实际的加密采矿有效载荷和系统中的其他辅助组件。

其中一些辅助模块作为传播者，旨在通过远程桌面协议（RDP）、安全外壳（SSH）和服务器信息块（SMB）传播恶意软件。

Prometei v3还值得注意的是，它使用域生成算法（DGA）来建立其命令和控制（C2）基础设施。它还包括一个自我更新机制和一个扩展的命令集，以获取敏感数据并控制主机。

最后，该恶意软件还部署了一个Apache网络服务器，它捆绑了一个基于PHP的网络外壳，能够执行Base64编码的命令并进行文件上传。

> 参考链接：thehackernews.com/2023/03/new-version-of-prometei-botnet-infects.html

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