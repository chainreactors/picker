---
title: GitLab 曝出严重漏洞，可能导致任意 CI/CD 管道执行
url: https://www.freebuf.com/news/412651.html
source: FreeBuf网络安全行业门户
date: 2024-10-13
fetch_date: 2025-10-06T18:50:31.275526
---

# GitLab 曝出严重漏洞，可能导致任意 CI/CD 管道执行

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

GitLab 曝出严重漏洞，可能导致任意 CI/CD 管道执行

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

GitLab 曝出严重漏洞，可能导致任意 CI/CD 管道执行

2024-10-12 09:36:10

所属地 上海

![1728697044_6709d2d444adc25624d6d.png!small](https://image.3001.net/images/20241012/1728697044_6709d2d444adc25624d6d.png!small)

近日，GitLab 发布了社区版（CE）和企业版（EE）的安全更新，以解决八个安全漏洞，其中包括一个可能允许在任意分支上运行持续集成和持续交付（CI/CD）管道的关键漏洞。该漏洞被跟踪为 CVE-2024-9164，CVSS 得分为 9.6（满分 10 分），攻击者可以在某些情况下以任意用户身份触发Pipeline，可能导致权限提升或执行恶意操作 。

GitLab 在一份公告中说："在 GitLab EE 中发现了一个漏洞，影响了从 12.5 开始到 17.2.9 之前的所有版本、从 17.3 开始到 17.3.5 之前的所有版本，以及从 17.4 开始到 17.4.2 之前的所有版本。目前，GitLab CE/EE 17.1.7，17.2.5，17.3.2及以上版本已修复该漏洞。

在其余七个问题中，四个被评为严重程度高，两个被评为严重程度中，一个被评为严重程度低：

* CVE-2024-8970（CVSS 得分：8.2），允许攻击者在某些情况下以其他用户身份触发管道
* CVE-2024-8977（CVSS 得分：8.2），允许在配置并启用产品分析仪表板的 GitLab EE 实例中进行 SSRF 攻击
* CVE-2024-9631 (CVSS score: 7.5)，可导致在查看有冲突的合并请求的差异时速度变慢
* CVE-2024-6530 （CVSS 得分：7.3），由于跨站点脚本问题，当授权新应用程序时，会在 OAuth 页面中注入 HTML

近几个月来，GitLab 不断披露与管道相关的漏洞，该公告是其中的最新进展。

## 近期历史漏洞回顾

GitLab近期频繁披露与管道相关的漏洞，此次更新只是其中的一部分。

上个月，GitLab修复了另一个关键漏洞（CVE-2024-6678，CVSS得分：9.9），该漏洞允许攻击者以任意用户身份运行管道作业。

此前，GitLab还修补了其他三个类似的缺陷——CVE-2023-5009（CVSS得分：9.6）、CVE-2024-5655（CVSS得分：9.6）和CVE-2024-6385（CVSS得分：9.6）。

尽管目前没有证据表明这些漏洞已被主动利用，但GitLab强烈建议用户将其实例更新至最新版本，以确保系统安全并防范潜在威胁。定期更新和监控是保护关键基础设施免受攻击的重要措施。

GitLab的安全更新反映了当前软件安全环境的动态性，企业需保持警惕并及时响应安全公告，以维护其数字资产的安全。

> 参考来源：[New Critical GitLab Vulnerability Could Allow Arbitrary CI/CD Pipeline Execution (thehackernews.com)](https://thehackernews.com/2024/10/new-critical-gitlab-vulnerability-could.html)

# 安全漏洞 # GitLab安全

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

近期历史漏洞回顾

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