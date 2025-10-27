---
title: 针对 Facebook 业务和广告帐户的 DUCKTAIL 恶意软件又回来了
url: https://www.freebuf.com/news/351010.html
source: FreeBuf网络安全行业门户
date: 2022-11-30
fetch_date: 2025-10-04T00:05:15.158559
---

# 针对 Facebook 业务和广告帐户的 DUCKTAIL 恶意软件又回来了

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

针对 Facebook 业务和广告帐户的 DUCKTAIL 恶意软件又回来了

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

针对 Facebook 业务和广告帐户的 DUCKTAIL 恶意软件又回来了

2022-11-29 10:46:21

所属地 上海

![](https://image.3001.net/images/20221129/1669688258_63856bc2c7555cba922fe.png!small)

一群可能位于越南的攻击者专门针对可能访问 Facebook 业务和广告管理帐户的员工，在几个月前首次曝光后，他们重新出现并改变了其基础设施、恶意软件和作案手法。

该组织被WithSecure的研究人员称为 DUCKTAIL，该组织使用鱼叉式网络钓鱼来针对 LinkedIn 上的个人，从这些个人的职位描述来看可能他们有权管理 Facebook 企业帐户。最近，还观察到攻击者通过 WhatsApp 瞄准受害者。受感染的 Facebook 商业帐户用于在平台上投放广告，以获取攻击者的经济利益。

## DUCKTAIL 攻击者进行研究

帐户滥用是通过恶意软件程序使用受害者的浏览器实现的，该恶意软件程序伪装成与品牌、产品和项目规划相关的文档。攻击者首先建立一个在 Facebook 上有业务页面的公司列表。然后，他们在 LinkedIn 和其他来源上搜索为这些公司工作并拥有可以让他们访问这些业务页面的职位的员工。这些包括管理、数字营销、数字媒体和人力资源角色。

最后一步是向他们发送一个链接，其中包含一个伪装成 .pdf 的恶意软件的存档，以及看似属于同一项目的图像和视频。研究人员看到的一些文件名包括项目“发展计划”、“项目信息”、“产品”和“新项目预算业务计划”。

DUCKTAIL 组织自 2021 年下半年以来一直在开展这项活动。在今年 8 月WithSecure 曝光他们的行动后，该行动停止了，攻击者重新设计了他们的一些工具集。

## 攻击者改用 GlobalSign 作为证书颁发机构

今年早些时候分析的恶意软件样本使用以一家越南公司的名义从 Sectigo 获得的合法代码签名证书进行了数字签名。由于该证书已被报告和撤销，攻击者已切换到 GlobalSign 作为他们的证书颁发机构。在他们继续以原公司的名义向多个 CA 申请证书的同时，他们还建立了其他六家企业，全部使用越南语，其中三个获得了代码签名证书。

2021 年底出现的 DUCKTAIL 恶意软件样本是用 .NET Core 编写的，并使用框架的单文件功能编译，该功能将所有必需的库和文件捆绑到一个可执行文件中，包括主程序集。这确保恶意软件可以在任何 Windows 计算机上执行，无论它是否安装了 .NET 运行时。自 2022 年 8 月活动停止以来，WithSecure 研究人员观察到从越南上传到 VirusTotal 的多个开发 DUCKTAIL 样本。

其中一个示例是使用 .NET 7 的 NativeAOT 编译的，它提供与 .NET Core 的单文件功能类似的功能，允许二进制文件提前本地编译。然而，NativeAOT 对第三方库的支持有限，因此攻击者转而使用 .NET Core。

## 坏演员一直在试验

其他实验也被观察到，例如包含来自 GitHub 项目的反分析代码，但从未真正打开过，从命令和控制服务器发送电子邮件地址列表作为 .txt 文件的能力在恶意软件中对它们进行硬编码，并在执行恶意软件时启动一个虚拟文件，以减少用户的怀疑——观察到文档 (.docx)、电子表格 (.xlsx) 和视频 (.mp4) 虚拟文件。

攻击者还在测试多级加载程序以部署恶意软件，例如 Excel 加载项文件 (.xll)，它从加密的 blob 中提取二级加载程序，然后最终下载信息窃取程序恶意软件。研究人员还确定了一个用 .NET 编写的下载程序，他们高度信任 DUCKTAIL，它执行 PowerShell 命令，从 Discord 下载信息窃取程序。

infostealer 恶意软件使用电报频道进行命令和控制。自从 8 月被曝光以来，攻击者更好地锁定了这些频道，一些频道现在有多个管理员，这可能表明他们正在运行类似于勒索软件团伙的附属程序。研究人员说：“聊天活动的增加和新的文件加密机制可确保只有特定用户能够解密某些泄露的文件，这进一步加强了这一点。”

## 浏览器劫持

部署后，DUCKTAIL 恶意软件会扫描系统上安装的浏览器及其 cookie 存储路径。然后它会窃取所有存储的 cookie，包括存储在其中的任何 Facebook 会话 cookie。会话 cookie 是网站在身份验证成功完成后在浏览器中设置的一个小标识符，用于记住用户已经登录了一段时间。

该恶意软件使用 Facebook 会话 cookie 直接与 Facebook 页面交互，或向 Facebook Graph API 发送请求以获取信息。此信息包括个人帐户的姓名、电子邮件、生日和用户 ID；个人帐户可以访问的 Facebook 业务页面的名称、验证状态、广告限制、名称、ID、账户状态、广告支付周期、货币、adtrust DSL 以及任何相关 Facebook 广告账户的花费金额。

该恶意软件还会检查是否为被劫持的帐户启用了双因素身份验证，并在启用时使用活动会话获取 2FA 的备份代码。“从受害者机器窃取的信息还允许威胁行为者从受害者机器外部尝试这些活动（以及其他恶意活动）。研究人员说：“窃取的会话 cookie、访问令牌、2FA 代码、用户代理、IP 地址和地理位置等信息，以及一般帐户信息（如姓名和生日）可用于隐藏和冒充受害者。”

该恶意软件旨在尝试将攻击者控制的电子邮件地址添加到被劫持的 Facebook 企业帐户中，这些帐户可能具有较高的身份：管理员和财务编辑。根据 Facebook 所有者 Meta 的文档，管理员可以完全控制帐户，而财务编辑可以控制存储在帐户中的信用卡信息以及帐户上的交易、发票和支出。他们还可以将外部业务添加到存储的信用卡和月度发票中，从而使这些业务可以使用相同的付款方式。

## 冒充合法客户经理身份

在目标受害者没有足够的访问权限以允许恶意软件将攻击者的电子邮件地址添加到预期的企业帐户的情况下，攻击者依靠从受害者的机器和 Facebook 帐户中泄露的信息来冒充他们。

在 WithSecure 事件响应人员调查的一个案例中，受害者使用的是 Apple 机器，并且从未从 Windows 计算机登录过 Facebook。系统上未发现恶意软件，无法确定初始访问向量。目前尚不清楚这是否与 DUCKTAIL 有关，但研究人员确定袭击者也来自越南。

建议 Facebook Business 管理员定期审查在 Business Manager > Settings > People 下添加的用户，并撤销对任何授予管理员访问权限或财务编辑角色的未知用户的访问权限。

在我们的调查中，WithSecure 事件响应团队发现业务历史日志和目标个人的 Facebook 数据与事件分析相关。“然而，对于与个人 Facebook 帐户相关的日志，门户网站上可见的内容与下载数据副本时获得的内容之间存在广泛的不一致。作为对其他调查人员的建议，WithSecure 事件响应团队强烈建议尽快捕获业务历史日志的本地副本，并为其帐户请求用户数据的副本。

> 参考来源：https://www.csoonline.com/article/3681108/ducktail-malware-campaign-targeting-facebook-business-and-ads-accounts-is-back.html

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

DUCKTAIL 攻击者进行研究

攻击者改用 GlobalSign 作为证书颁发机构

坏演员一直在试验

浏览器劫持

冒充合法客户经理身份

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