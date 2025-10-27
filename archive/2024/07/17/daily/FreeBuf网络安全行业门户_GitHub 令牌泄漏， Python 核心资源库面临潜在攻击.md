---
title: GitHub 令牌泄漏， Python 核心资源库面临潜在攻击
url: https://www.freebuf.com/news/406078.html
source: FreeBuf网络安全行业门户
date: 2024-07-17
fetch_date: 2025-10-06T17:41:30.397549
---

# GitHub 令牌泄漏， Python 核心资源库面临潜在攻击

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

GitHub 令牌泄漏， Python 核心资源库面临潜在攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

GitHub 令牌泄漏， Python 核心资源库面临潜在攻击

2024-07-16 11:28:57

所属地 上海

![](https://image.3001.net/images/20240716/1721100260_6695e7e4979bc843ac584.png!small)TheHackerNews网站消息，软件供应链安全公司 JFrog 的网络安全研究人员称，他们发现了一个意外泄露的 GitHub 令牌，可授予 Python 语言 GitHub 存储库、Python 软件包索引（PyPI）和 Python 软件基金会（PSF）存储库的高级访问权限。

该令牌属于 Python 软件基金会的基础设施主管，并且意外地包含在一个编译的二进制文件中，该文件作为容器镜像的一部分发布在 Docker Hub 上。

JFrog 的研究人员在一份报告中写道：“这次的情况比较特殊，如果令牌落入不法分子之手，他们可能向 PyPI 软件包甚至 Python 语言本身注入恶意代码（类似于用恶意软件包替换所有 Python 软件包），其潜在后果难以估量。”

因此，理论上攻击者可以利用管理员权限，通过毒化与 Python 编程语言核心或 PyPI 软件包管理器相关的源代码，策划大规模的供应链攻击。

这一事件表明，仅从源代码中清除访问令牌（某些开发工具会自动这样做）不足以防止潜在的安全漏洞。由于自动构建过程和开发人员的失误，敏感凭据也可能被包含在环境变量、配置文件甚至二进制文件中。

## 令牌泄漏

PyPI 管理员兼 Python 软件基金会 (PSF) 基础设施主管 Ee Durbin 撰写了一份事件报告，解释了泄露事件发生的原因。该事件涉及 Durbin 自己账户的访问令牌，由于他在组织中的角色，该账户拥有管理权限。

2023 年初，Durbin 正在开发 cabotage-app，这是 PSF 开发的一款基于 Docker 的工具，用于在 Kubernetes 集群上部署 PyPI 和相关服务。在开发代码库的构建部分时，他不断遇到 GitHub 对匿名访问实施的 API 速率限制。

在Durbin 所谓的 "偷懒行为 "中，他决定在本地修改源代码，为自己的账户添加一个访问令牌，以绕过默认的速率限制，更快地完成工作。这是一个快速解决方案，是配置本地主机 GitHub 应用程序来完成构建而不是使用 GitHub API 的替代方案。

Durbin 知道在源代码中添加个人访问令牌 (PAT) 并不安全，但这种更改只是针对他的本地代码库副本，从未打算远程推送。事实上，自动构建和部署脚本应该恢复本地变更，从而清除令牌。

但 Durbin 没有意识到的是，作为构建过程的一部分而生成的 .pyc（Python 编译字节码）文件中也包含了令牌，而这些存储在 \_\_pycache\_\_ 文件夹中的文件并未配置为从上传到 Docker Hub 的最终 Docker 镜像中排除。

PyPI 安全团队在 6 月下旬收到 JFrog 的通知后，撤销了该令牌，并审查了所有 GitHub 审计日志和账户活动，以查找该令牌可能被恶意使用的迹象。目前，没有发现恶意使用的证据。包含令牌的 cabotage-app 版本于 2023 年 3 月 3 日发布在 Docker Hub 上，并于 2024 年 6 月 21 日（即 15 个月后）被移除。

Durbin 写道：" Cabotage 现在完全是自托管的，这意味着 cabotage-app 的构建不再使用公共注册表，部署构建仅从源代码的清洁检查中启动。这减少了本地编辑进入开发环境之外的镜像构建的情况，同时也消除了发布到公共注册表的需要。”

Durbin 表示，除非万不得已，他今后将避免为自己的账户创建个人访问令牌。除了这一案例之外，这种长效令牌并没有在其他任何情况发挥作用。

关于此次事件，Durbin 认为这是一个很好的提醒，要为 API 令牌设置严格的过期日期（如果需要的话），像对待源代码一样对待 .pyc 文件，并在自动化系统上只从干净的源代码执行构建。

参考来源：

https://www.csoonline.com/article/2515722/python-github-token-leak-shows-binary-files-can-burn-developers-too.html

https://thehackernews.com/2024/07/github-token-leak-exposes-pythons-core.html

# python # github

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

令牌泄漏

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