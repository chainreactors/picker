---
title: GitLab 曝一严重漏洞，威胁软件开发管道
url: https://www.freebuf.com/news/404873.html
source: FreeBuf网络安全行业门户
date: 2024-07-02
fetch_date: 2025-10-06T17:45:09.349759
---

# GitLab 曝一严重漏洞，威胁软件开发管道

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

GitLab 曝一严重漏洞，威胁软件开发管道

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)
* [开发安全](https://www.freebuf.com/articles/development)

GitLab 曝一严重漏洞，威胁软件开发管道

2024-07-01 10:58:15

所属地 上海

DARKReading 网站消息，一个严重的 GitLab 漏洞可能允许攻击者以另一个用户的身份运行管道，该公司正敦促运行易受攻击版本的用户立即修补该漏洞，以避免 CI/CD 失常。

![](https://image.3001.net/images/20240701/1719802552_66821ab87c8a2ef43ab07.png!small)GitLab 是仅次于 GitHub 的流行 Git 存储库，拥有数百万活跃用户。上周，它发布了社区版（开源）和企业版的新版本。

更新包括对 14 个不同安全问题的修复，包括跨站请求伪造（CSRF）、跨站脚本（XSS）、拒绝服务（DoS）等。根据通用漏洞评分系统 (CVSS)，其中一个问题的严重程度较低，九个问题的严重程度中等，三个问题的严重程度较高，但有一个关键漏洞的 CVSS 得分为 9.6（满分 10 分）。

## CVE-2024-5655 对代码开发构成严重威胁

据该公司称，CVE-2024-5655 这个关键漏洞影响的 GitLab 版本从 15.8 到 16.11.5，从 17.0 到 17.0.3，以及从 17.1 到 17.1.1。该漏洞允许攻击者以另一个用户的身份触发管道，但仅限于 GitLab 没有详细说明的情况（GitLab 也没有提供有关该漏洞的任何其他信息）。

在 GitLab 中，管道可以自动完成构建、测试和部署代码的过程。从理论上讲，攻击者如果有能力以其他用户的身份运行管道，就可以访问他们的私有存储库，并操作、窃取或外泄其中包含的敏感代码和数据。

与 CVE-2023-7028 不同，GitLab 到目前为止还没有发现 CVE-2024-5655 漏洞在野外被利用的证据，而 CVE-2023-7028 在今年春天早些时候已经被利用。不过，这种情况可能很快就会改变。

## 合规问题，不仅仅是安全问题

像 CVE-2024-5655 这样根植于开发过程中的问题，有时会带来的困扰远不止于它们在文档上所呈现的简单风险。

Synopsys Software Integrity Group 首席副顾问 Jamie Boote 说："在最坏的情况下，这个漏洞甚至不需要被利用就会给公司造成收入损失。"一个软件或软件驱动的产品是使用一个易受攻击的 GitLab 版本构建的，这一事实本身就可能引起关注。

像这样的管道漏洞不仅会带来安全风险，还会带来监管和合规风险。Jamie Boote 解释说："由于美国公司正在努力满足向美国政府销售软件和产品所需的自检表要求，如果不解决这个漏洞，可能会导致合规性漏洞，从而使销售和合同面临风险。”他特别提到了美国商务部《安全软件开发证明表说明》第三部分的第 1c 行，其中要求 "在开发和构建软件的相关环境中执行多因素身份验证和有条件访问，以最大限度地降低安全风险"。

Jamie Boote 表示，不解决这一漏洞的公司将很难符合第 1c 项的要求，因为攻击者可以利用漏洞绕过公司为符合要求而依赖的条件访问控制。

参考来源：https://www.darkreading.com/application-security/critical-gitlab-bug-threatens-software-development-pipelines

# 安全漏洞 # Gitlab # CICD

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

CVE-2024-5655 对代码开发构成严重威胁

合规问题，不仅仅是安全问题

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