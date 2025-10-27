---
title: polyfill.io 供应链攻击，超 38 万台主机受影响
url: https://www.freebuf.com/news/405435.html
source: FreeBuf网络安全行业门户
date: 2024-07-09
fetch_date: 2025-10-06T17:45:07.386699
---

# polyfill.io 供应链攻击，超 38 万台主机受影响

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

polyfill.io 供应链攻击，超 38 万台主机受影响

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

polyfill.io 供应链攻击，超 38 万台主机受影响

2024-07-08 13:54:45

所属地 上海

近日，网络安全公司 Censys 发现超过 38 万台主机仍在引用 polyfill.io 恶意域。

![](https://image.3001.net/images/20240708/1720418321_668b801189432386984b3.png!small)在接到多起恶意活动报告后，polyfill.io 域名被暂停。Polyfill.io 域曾用于托管 JavaScript 代码，为不支持某些网络标准的旧版浏览器添加现代功能。

根据报告，该域名被用于将嵌入 polyfill.io 代码的网站的访问者重定向到博彩和成人网站。专家估计，超过 10 万个网站受到影响。

截至 2024 年 7 月 2 日，Censys 检测到 384773 台主机在其 HTTP 响应中包含对 "https://cdn.polyfill[.]io "或 "https://cdn.polyfill[.]com "的引用。其中约 237700 台主机主要集中在德国的 Hetzner 网络 (AS24940)。Hetzner 是一种流行的虚拟主机服务，许多网站开发人员都会利用它。

这些主机包括与 Hulu、梅赛德斯-奔驰（Mercedes-Benz）和 WarnerBros 等主要平台相关的网站。专家敦促网站所有者从其代码库中删除对 polyfill.io 及其相关域的任何引用，以防万一。

另外，Censys 还注意到，有 182 台受影响的主机是使用 polyfill.io 脚本的政府网站（".gov"）。专家们强调，这次供应链攻击产生了广泛的影响。

对此，Cloudflare 和 Fastly 为用户创建了替代的安全 polyfill 端点以减轻威胁，同时防止网站被攻破。Censys 观察到 216504 台主机引用了其中一个替代 polyfill 端点： "polyfill-fastly.io "或 "cdnjs.cloudflare.com/polyfill"，较 6 月 28 日观察到的 80312 台主机有所增加。

Censys 还在一个论坛上发现了一名开发者发布的帖子，该帖子警告说，cdn.bootcss.com 上有一个与 polyfill.io 类似的恶意 JavaScript 文件，会根据地理位置对用户进行重定向。专家们发现有 160 万台面向公众的主机引用了这些域名，其中 bootcss.com 涉及恶意活动。

报告总结道，他们在 Censys Search 中挖掘任何引用其他可疑域名的暴露主机时，观察到总共有 1637160 个面向公众的主机链接到了其中一个域。"到目前为止，这个域名（bootcss.com）是唯一一个显示出潜在恶意迹象的域名，其他相关端点的性质尚不清楚。不过，考虑到对 polyfill.io 攻击负责的同一恶意行为者将来可能利用这些其他域名进行类似活动的可能性，也并非完全不合理。

参考来源：https://securityaffairs.com/165302/hacking/polyfill-io-supply-chain-attack.html

# 供应链攻击 # 主机安全 # 恶意域名威胁

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