---
title: 官方强烈建议升级，GitLab又曝严重的账户接管漏洞
url: https://www.freebuf.com/news/405728.html
source: FreeBuf网络安全行业门户
date: 2024-07-12
fetch_date: 2025-10-06T17:43:42.920639
---

# 官方强烈建议升级，GitLab又曝严重的账户接管漏洞

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

官方强烈建议升级，GitLab又曝严重的账户接管漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

官方强烈建议升级，GitLab又曝严重的账户接管漏洞

2024-07-11 13:54:07

所属地 上海

7月10日，GitLab警告称，其产品GitLab社区和企业版本中存在一个严重漏洞，允许攻击者以任何其他用户的身份运行管道作业。

![](https://image.3001.net/images/20240711/1720677087_668f72dfa3bdfcda77b60.png!small)

> GitLab DevSecOps平台拥有3000多万注册用户，活跃用户数仅次于 GitHub，超过50%的财富100强公司都在使用该平台，包括T-Mobile、高盛、空客、洛克希德·马丁、英伟达和瑞银。

在昨天发布的安全更新中，修补的漏洞被追踪为CVE-2024-6385，CVSS评分为9.6分(满分10分)。它影响所有GitLab CE/EE版本，从15.8到16.11.6，17.0到17.0.4，17.1到17.1.2。

在GitLab尚未披露漏洞某些信息的情况下，攻击者可以利用该漏洞作为任意用户触发新的管道。GitLab管道是一个持续集成/持续部署(CI/CD)系统功能，允许用户自动并行或顺序运行流程和任务，以构建、测试或部署代码更改。

为解决这一严重安全漏洞，GitLab发布了GitLab社区和企业版本17.1.2、17.0.4和16.11.6。该公司强烈建议所有安装运行受以上问题影响的版本尽快升级到最新版本，GitLab.com和GitLab Dedicated已经在运行补丁版本。

## 账户接管漏洞在攻击中被积极利用

6月底，GitLab修复了一个与CVE-2024-6385几乎相同的漏洞CVE-2024-5655，该漏洞也可能被利用来作为其他用户运行管道。

一个月前，GitLab还修复了一个高严重性漏洞CVE-2024-4835，该漏洞允许未经身份验证的攻击者在跨站点脚本(XSS)攻击中接管帐户。

5月份，CISA发出警告，未经身份验证的攻击者也在积极利用1月份修补的另一个零点击GitLab漏洞CVE-2023-7028通过重置密码来劫持帐户。

今年1月，Shadowserver发现5300多个易受攻击的GitLab实例暴露在网络上，目前仍有不到一半(1795个)的实例可以访问。

攻击者以GitLab为目标，大概率是因为它托管各种类型的企业敏感数据，包括API密钥和专有代码，一旦遭到破坏，托管项目的完整性和机密性将面临重大风险。

这包括供应链攻击，如果威胁行为者在CI/CD(持续集成/持续部署)环境中插入恶意代码，被破坏组织的存储库岌岌可危。

**参考来源：**

https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-bug-that-lets-attackers-run-pipelines-as-an-arbitrary-user/

https://www.darkreading.com/application-security/critical-gitlab-bug-threatens-software-development-pipelines

# Gitlab # GitLab安全 # 管道安全 # CICD

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

账户接管漏洞在攻击中被积极利用

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