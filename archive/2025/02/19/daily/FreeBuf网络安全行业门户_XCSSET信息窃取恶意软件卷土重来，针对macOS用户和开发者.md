---
title: XCSSET信息窃取恶意软件卷土重来，针对macOS用户和开发者
url: https://www.freebuf.com/articles/422056.html
source: FreeBuf网络安全行业门户
date: 2025-02-19
fetch_date: 2025-10-06T20:40:04.239459
---

# XCSSET信息窃取恶意软件卷土重来，针对macOS用户和开发者

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

XCSSET信息窃取恶意软件卷土重来，针对macOS用户和开发者

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

XCSSET信息窃取恶意软件卷土重来，针对macOS用户和开发者

2025-02-18 13:26:38

所属地 上海

![](https://image.3001.net/images/20250218/1739856380_67b419fcea39229829273.png!small)

近日，一种新型 XCSSET macOS 模块化恶意软件变体在攻击活动中现身，其目标是窃取用户的敏感信息，涵盖数字钱包数据以及合法 Notes 应用程序中的数据。

这种恶意软件通常借助受感染的 Xcode 项目进行传播，至少已存在五年之久，每次更新都堪称 XCSSET发展历程中的一个里程碑。此次的改进是自2022年以来首次被发现。

微软威胁情报团队在有限的攻击活动中识别出了这一最新变体，并指出与过往的 XCSSET 变体相比，新变体具备更强的代码混淆能力、更好的持久化能力以及全新的感染策略。

## **关键特性****剖析**

### 1.隐匿性强化

新变体采用动态迭代的Base64 + xxd双重编码技术，这种技术能够实现多层级的代码混淆。通过不断变化的编码迭代次数，使得安全工具难以对其进行有效的解析和追踪。

同时，对关键模块名称进行加密处理，即使逆向分析专家试图拆解其代码结构，也会因为这些加密的模块名称而倍感棘手，显著增加了逆向分析的难度，让恶意代码在系统中能够更长久地潜伏。

### 2.持久化创新

在实现持久化驻留系统方面，新变体采用了两种创新方案。

* **zshrc 方案：**新变体创建名为～/.zshrc\_aliases 的文件，并将恶意负载巧妙植入其中。然后通过修改.zshrc 配置文件，实现了会话级自启动。这意味着只要用户开启新的 shell 会话，恶意文件就会自动运行，长期潜伏在系统中，持续收集信息或执行其他恶意指令。
* **Dock 劫持方案：**从攻击者的命令与控制（C2）服务器下载经过签名的 dockutil 工具，利用其合法身份绕过部分系统检测。通过伪造 Launchpad 应用路径，精心设计了 “双触发” 机制，当用户启动正版应用时，恶意负载也会同时被执行，实现了神不知鬼不觉的恶意操作。

### 4.Xcode感染策略进化

在针对 Xcode 项目的感染策略上，新变体也有了重大进化。

* **滥用构建参数：**利用 TARGET、RULE、FORCED\_STRATEGY 等构建参数，将恶意代码注入到 Xcode 项目中。这些参数在正常的开发过程中有着重要作用，但被恶意软件利用后，就成为了恶意代码进入项目的 “绿色通道”。
* **设备定向渗透：**通过篡改 TARGET\_DEVICE\_FAMILY 构建设置，实现对特定设备的精准部署。这使得攻击者可以有针对性地对某些设备类型进行攻击，提高攻击效率和成功率。

XCSSET 并非首次展现其强大的攻击能力，早在 2021 年 5 月，它就利用零日漏洞（漏洞编号 CVE - 2021 - 30713，苹果已修复）发起攻击。此次新变体的升级，再次印证其开发者具备持续突破系统防御的能力，不断给网络安全带来新的挑战。

## **Xcode项目与XCSSET攻击范围**

Xcode 是苹果的开发者工具集，其中包含集成开发环境（IDE），开发者能借助它创建、测试和发布适用于所有苹果平台的应用程序。Xcode 项目的创建方式灵活多样，既可以从头开始搭建，也能基于从各种代码库下载或克隆的资源来构建。

然而，这种开放性和灵活性也为 XCSSET 的操控者提供了可乘之机。他们通过针对这些项目，巧妙地扩大了攻击目标范围，从开发源头就开始埋下恶意种子，一旦项目被使用，恶意软件就可能随之进入用户系统。

XCSSET 拥有多个功能各异的模块，这些模块相互协作，能够解析系统数据、收集各类敏感信息，并将这些信息偷偷泄露出去。其攻击目标数据类型极为广泛，涵盖登录信息、聊天应用程序和浏览器数据、Notes 应用程序数据、数字钱包数据、系统信息以及文件等，几乎涉及用户在系统中的方方面面数据。

## **微软给出的安全建议**

鉴于 XCSSET 恶意软件的威胁，微软团队建议：

### 1.注重开发环境安全

* 仅从官方仓库获取Xcode项目资源
* 建立代码审计机制，重点检查构建参数异常配置

### 2.搭建终端防护策略

* 监控.zshrc等配置文件异常修改
* 部署EDR解决方案检测隐蔽进程链

**参考链接：**

> <https://www.bleepingcomputer.com/news/security/microsoft-spots-xcsset-macos-malware-variant-used-for-crypto-theft/>

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

关键特性剖析

* 1.隐匿性强化
* 2.持久化创新
* 4.Xcode感染策略进化

Xcode项目与XCSSET攻击范围

微软给出的安全建议

* 1.注重开发环境安全
* 2.搭建终端防护策略

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