---
title: 美国国防承包商 Belcan 泄露管理员凭据
url: https://www.freebuf.com/news/376003.html
source: FreeBuf网络安全行业门户
date: 2023-08-25
fetch_date: 2025-10-04T12:01:54.870433
---

# 美国国防承包商 Belcan 泄露管理员凭据

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

美国国防承包商 Belcan 泄露管理员凭据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

美国国防承包商 Belcan 泄露管理员凭据

2023-08-24 11:15:36

所属地 上海

Cyber News 研究小组披露，美国政府和国防承包商 Belcan 向公众公开了其超级管理员凭据，这一“失误”可能会引起严重的供应链攻击。![1692846893_64e6cb2d1610d5ff0e29f.png!small](https://image.3001.net/images/20230824/1692846893_64e6cb2d1610d5ff0e29f.png!small)

Belcan 作为一家政府、国防和航空航天承包商，主要为客户提供设计、软件、制造、供应链、信息技术和数字工程解决方案。据悉，该公司 2022 年的收入达到 9.5 亿美元，是 40 多个美国联邦机构值得信赖的战略合作伙伴。

5 月 15 日，Cybernews 研究团队发现一个开放的 Kibana 实例，其中包含部分 Belcan 公司员工和内部基础设施的敏感信息。（Kibana 是数据搜索和分析引擎 ElasticSearch 的可视化仪表板，这些系统能够帮助企业处理大量数据。）

值得注意的是，虽然泄露的信息凸显了 Belcan 公司通过实施渗透测试和审计对信息安全的承诺，但攻击者可能会利用这一漏洞，公开测试结果以及用 bcrypt 加密的管理凭据。

**开放 Kibana 实例中泄露的 Belcan 数据包含以下内容：**

> 管理员电子邮件；
>
> 管理员密码（使用 bcrypt 散列，成本设置为 12）；
>
> 管理员用户名；
>
> 管理员角色（分配给哪些组织）；
>
> 内部网络地址；
>
> 内部基础设施主机名和 IP 地址；
>
> 内部基础架构漏洞以及采取的补救/不补救措施。

Bcrypt 是一种常见的安全哈希算法，为防范攻击者增加了一层安全保护，但其哈希值仍有可能被破解，其它身份验证数据也可能被用于鱼叉式网络钓鱼攻击。在这种情况下，攻击者可能需要长达 22 年的时间才能破解一个非常强大的管理员密码，但如果密码较弱的话，容易受到字典攻击，攻击者可能在几天内就会破解密码。

此外，Cybernews 研究小组指出数据表明并非所有漏洞都得到了修补，攻击者可以通过检查 Belcan 公司修复漏洞的进展，识别出尚未打补丁的脆弱系统，并为其提供具有特权访问权限的账户凭证，从而使针对组织的潜在攻击变得更加容易和快速。这样带来的最大风险是由间谍活动、影响力或代理人战争等政治和军事目标驱动的高级持续威胁 (APT)。![1692846914_64e6cb420422d25f270f8.png!small](https://image.3001.net/images/20230824/1692846914_64e6cb420422d25f270f8.png!small)

Cybernews 向 Belcan 公司通报了发现的安全漏洞，在文章发布之前，该公司已采取保障措施解决了这一问题。

**文章来源：**

> https://securityaffairs.com/149779/data-breach/belcan-leaks-admin-password.html

# 漏洞

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