---
title: GitHub Actions 遭利用，14个热门开源项目令牌泄露风险激增
url: https://www.freebuf.com/news/408680.html
source: FreeBuf网络安全行业门户
date: 2024-08-16
fetch_date: 2025-10-06T18:03:53.210266
---

# GitHub Actions 遭利用，14个热门开源项目令牌泄露风险激增

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

GitHub Actions 遭利用，14个热门开源项目令牌泄露风险激增

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

GitHub Actions 遭利用，14个热门开源项目令牌泄露风险激增

2024-08-15 10:36:30

所属地 上海

![](https://image.3001.net/images/20240815/1723693531_66bd79db05b978c5af4bd.png!small)

近日，有攻击者通过 CI/CD 工作流中的 GitHub Actions 工具窃取了谷歌、微软、AWS 和 Red Hat 等多个知名开源项目的 GitHub 身份验证令牌。

窃取这些令牌的攻击者可在未经授权的情况下访问私有存储库、窃取源代码或向项目中注入恶意代码。

Palo Alto Networks  Unit 42 发现这个情况后，立刻敦促所有受到影响的企业立刻采取行动。但由于 GitHub 暂未对此有所行动，因此根本问题仍未解决。

鉴于这种情况，GitHub 用户需要了解风险，评估自己所面临的风险，并采取措施防止未来发生泄密事件。

![1723689245_66bd691d3c3612bfa8867.png!small](https://image.3001.net/images/20240815/1723689245_66bd691d3c3612bfa8867.png!small)

GitHub 操作生成的工件，来源：GitHub Unit 42

## GitHub 令牌泄露

Unit 42 的报告强调了一系列因素，包括不安全的默认设置、用户错误配置和不充分的安全检查，这些都可能导致 GitHub 令牌泄漏，他们称之为 “ArtiPACKED ”攻击。

第一个风险点是 “actions/checkout ”操作，该操作通常用于 GitHub 工作流，以克隆版本库代码，使其在工作流运行期间可用。

默认情况下，该操作会将 GitHub 标记持久化到本地 .git 目录（隐藏）中，这是工作流中验证操作所必需的。

如果用户误将整个签出目录作为工件的一部分上传，git 文件夹内的 GitHub 标记现在就会暴露。

![1723689283_66bd6943989e70e88fc52.png!small](https://image.3001.net/images/20240815/1723689283_66bd6943989e70e88fc52.png!small)

公开暴露的 GitHub 令牌，来源：GitHub Unit 42

该文件夹中可能包含的其他敏感信息包括 API 密钥、云服务访问令牌和各种账户凭据。

在 CI/CD 过程中生成的工件（如构建输出和测试结果）也会因错误的工件上传而发生类似的暴露，这些工件的存储和访问时间长达三个月。

另一个故障点是使用环境变量存储 GitHub 标记的 CI/CD 管道。如果工作流中的操作或脚本有意或无意记录了这些变量，这些记录就会作为人工制品上传。

Unit 42指出，当 “CREATE\_LOG\_FILE ”属性设置为 “True ”时，“super-linter ”操作可以创建包含环境变量的详细日志。

最终，攻击者会在短暂的 GitHub 令牌过期前从日志中提取并使用这些令牌。GitHub 令牌在工作流作业持续期间保持有效，因此其利用潜力因情况而异。

GitHub 内部用于缓存和管理工件的 “Actions\_Runtime\_Token ”有效期通常为 6 小时，利用窗口很小。

而自定义秘密和令牌（如 API 密钥或云服务的访问令牌）的生命周期各不相同，从几分钟到永不过期不等。

Unit 42介绍了一种攻击方案，该方案可识别使用 GitHub Actions 的项目或公共源，并使用自动脚本扫描它们，以确定可提高工件生成可能性的标准。

另一套脚本可以自动从目标软件仓库的 CI/CD 管道中下载工件，对于公共软件仓库来说这个过程并不复杂。

![1723689357_66bd698da50dd1d027432.png!small](https://image.3001.net/images/20240815/1723689357_66bd698da50dd1d027432.png!small)

攻击流，资料来源：Unit 42

## 缓解措施

Unit 42 发现了以下 14 个可能受到影响的大型开源项目，并建议它们立即采取补救措施：

* Firebase（谷歌）
* OpenSearch Security（AWS）
* 克莱尔（红帽）
* 活动目录系统（Adsys）（Canonical）
* JSON 模式（微软）
* TypeScript Repos 自动化、TypeScript Bot 测试触发器、Azure Draft（微软）
* CycloneDX SBOM（OWASP）
* 鳕鱼
* Libevent
* 用于 Apache Kafka 的 Guardian（Aiven-Open）
* Git 附件（Datalad）
* Penrose
* Deckhouse
* Concrete-ML (Zama AI)

Unit 42建议 GitHub 用户应尽量避免在上传的工件中包含整个目录，对日志进行消毒，并定期检查 CI/CD 管道配置。同时，应调整 “actions/checkout ”等危险操作的默认设置，以避免凭证持久化。此外，工作流中使用的令牌权限应设置为必要的最低权限，以限制它们被暴露时造成的损害。

> 参考来源：[GitHub Actions artifacts found leaking auth tokens in popular projects](https://www.bleepingcomputer.com/news/security/github-actions-artifacts-found-leaking-auth-tokens-in-popular-projects/)

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

GitHub 令牌泄露

缓解措施

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