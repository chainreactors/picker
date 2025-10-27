---
title: IBM 云数据库 PostgreSQL 出现安全漏洞
url: https://www.freebuf.com/news/351588.html
source: FreeBuf网络安全行业门户
date: 2022-12-06
fetch_date: 2025-10-04T00:34:44.407035
---

# IBM 云数据库 PostgreSQL 出现安全漏洞

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

IBM 云数据库 PostgreSQL 出现安全漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

IBM 云数据库 PostgreSQL 出现安全漏洞

2022-12-05 14:02:54

The Hacker News 网站披露，IBM 近日修复一个影响其 PostgreSQL 云数据库（ICD）产品的高严重性安全漏洞（CVSS分数：8.8），该漏洞可能被利用来篡改内部存储库并运行未经授权的代码。![1670221510_638d8ec62a97d9f88f481.jpg!small](https://image.3001.net/images/20221205/1670221510_638d8ec62a97d9f88f481.jpg!small)

云安全公司 Wiz 将该漏洞称为“Hell's Keychain ”，一旦恶意攻击者成功利用该漏洞可能会在客户环境中远程执行代码，甚至读取或修改存储在 PostgreSQL 数据库中的数据。

Wiz 研究人员 Ronen Shustin 和 Shir Tamari 表示：该漏洞由三个暴露的秘密 Kubernetes 服务帐户令牌、私有容器注册密码、CI/CD 服务器凭据组成，再加上对内部构建服务器的过度许可网络访问。

Hell's Keychain 始于 ICD 中的一个 SQL 注入漏洞，该漏洞可能授予攻击者超级用户（又称 "ibm"）权限，然后允许其在托管数据库实例的底层虚拟机上执行任意命令。

据悉，这个功能被武器化以期访问 Kubernetes API 令牌文件，从而允许更广泛的开发后工作，包括从 IBM 的私有容器注册表中提取容器图像，该注册表存储与用于PostgreSQL 的 ICD 相关的图像，并扫描这些图像以获取其他机密。

![1670221539_638d8ee3bb0c93116c076.jpg!small](https://image.3001.net/images/20221205/1670221539_638d8ee3bb0c93116c076.jpg!small)

研究人员强调，容器图像通常包含公司知识产权的专有源代码和二进制工件，此外，它们还可以包含攻击者可以利用的信息，以发现其他漏洞并在服务的内部环境中执行横向移动。

Wiz 表示，它能够从图像清单文件中提取内部工件存储库和 FTP 凭证，有效地允许对受信任的存储库和 IBM 构建服务器进行不受限制的读写访问。

这种攻击能够覆盖到 PostgreSQL 映像构建过程中使用的任意文件，然后将这些文件安装在每个数据库实例上，因此可能会产生严重后果。

IBM 在一份独立的咨询报告中表示，所有用于 PostgreSQL 实例的 IBM 云数据库都可能受到该 漏洞的影响，但目前还没有发现恶意活动的迹象，修补措施于 2022 年 8 月 22 日和 9 月 3 日推出，已自动应用于客户实例，无需进一步操作。

研究人员表示：作为广泛攻击链的一部分，这些漏洞可能被恶意攻击者利用，最终导致对平台的供应链攻击。 为了减轻此类威胁，建议组织监控其云环境中分散的凭据，强制实施网络控制以防止访问生产服务器，并防止容器注册表损坏。

**参考文章：**

> https://thehackernews.com/2022/12/researchers-disclose-supply-chain-flaw.html

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