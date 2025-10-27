---
title: 由于域验证错误，DigiCert 大规模撤销 TLS 证书
url: https://www.freebuf.com/news/407484.html
source: FreeBuf网络安全行业门户
date: 2024-08-02
fetch_date: 2025-10-06T18:03:04.334382
---

# 由于域验证错误，DigiCert 大规模撤销 TLS 证书

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

由于域验证错误，DigiCert 大规模撤销 TLS 证书

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

由于域验证错误，DigiCert 大规模撤销 TLS 证书

2024-08-01 11:12:07

所属地 上海

DigiCert 警告称，由于域控制验证 （DCV） 的不合规问题，该公司正大规模撤销已经发放的 SSL/TLS 证书，数量超过8万个。

![](https://image.3001.net/images/20240801/1722482027_66aafd6b38e37bdb333f1.png!small)

DigiCert 是提供 SSL/TLS 证书的著名证书颁发机构 （CA） 之一，包括域验证 （DV）、组织验证 （OV） 和扩展验证 （EV） 证书。这些证书用于加密用户与网站或应用程序之间的通信，从而提高安全性，防止恶意网络监控和中间人攻击。

为域颁发证书时，证书颁发机构必须首先执行域控制验证 （DCV） 以确认客户拥有该域。用于验证域所有权的方法之一是在证书的 DNS CNAME 记录中添加一个带有随机值的字符串，然后对域执行 DNS 查找以确保随机值匹配。

根据 CABF 基线要求，随机值应由域名分隔，并带有下划线。否则，域与用于验证的子域之间存在冲突的风险。但DigiCert称，最近在一些基于CNAME的验证案例中没有在随机值中包含下划线前缀。

## 一个已事发5年的错误

DigiCert表示，造成这种错误的根本原因是2019年8月的系统更新，导致删除了某些验证路径中的自动下划线添加，影响了 2019 年 8 月至 2024 年 6 月期间的 83267 个证书。2024 年 6 月 11 日，一个用户体验提升项目通过整合随机值生成过程，修复了这个长达5年都未发现的问题。7 月 29 日，DigiCert 在调查一份关于生成随机值的单独报告时正式披露了这一问题。

目前DigiCert已通知 6807 名受影响的客户，要求他们尽快替换其证书，方法是登录其 DigiCert 帐户，生成证书签名请求 （CSR），并在通过 DCV 后重新颁发证书。需要注意的是，DigiCert 将在 24 小时内（UTC时间 7 月 31 日 19：30 之前）撤销受影响的证书。如果在此之前未完成该过程，则将导致网站或应用程序的连接丢失。

这一事态发展促使美国网络安全和基础设施安全局 （CISA） 发布了一份警报，指出“撤销这些证书可能会导致依赖这些证书进行安全通信的网站、服务和应用程序暂时中断。

**参考来源：**

> [DigiCert mass-revoking TLS certificates due to domain validation bug](https://www.bleepingcomputer.com/news/security/digicert-mass-revoking-tls-certificates-due-to-domain-validation-bug/)

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

一个已事发5年的错误

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