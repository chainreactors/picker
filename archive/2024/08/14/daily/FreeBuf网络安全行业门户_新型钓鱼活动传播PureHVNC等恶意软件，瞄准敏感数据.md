---
title: 新型钓鱼活动传播PureHVNC等恶意软件，瞄准敏感数据
url: https://www.freebuf.com/news/408455.html
source: FreeBuf网络安全行业门户
date: 2024-08-14
fetch_date: 2025-10-06T18:03:14.880908
---

# 新型钓鱼活动传播PureHVNC等恶意软件，瞄准敏感数据

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

新型钓鱼活动传播PureHVNC等恶意软件，瞄准敏感数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型钓鱼活动传播PureHVNC等恶意软件，瞄准敏感数据

2024-08-13 11:08:45

所属地 上海

近日，FortiGuard 实验室的网络安全研究人员发现了一种复杂的网络钓鱼活动，该活动利用多阶段执行流程和各种规避技术来传播包括远程访问木马（RAT）PureHVNC在内的多种恶意软件。

![](https://image.3001.net/images/20240813/1723518338_66bacd826cb2ec5040683.png!small)攻击流程

该活动专门针对企业员工，以一封精心制作的电子邮件为诱饵，伪装成来自客户的服务查询，而邮件中包含一个恶意 HTML 附件。邮件使用紧急语气，诱使收件人打开恶意 HTML 附件，从而触发一系列导致多种恶意软件部署的事件。

具体来讲，钓鱼邮件附件中的 HTML 文件利用 "search-ms "功能查询远程共享的恶意 LNK 文件。该 LNK 文件在 Windows 资源管理器中伪装成一个无害的 PDF 图标，其中包含一条命令，该命令使用 conhost.exe 作为父进程运行远程批处理文件，这是一种利用合法的 Windows 进程逃避检测的技术。

名为 new.bat 的批处理文件经过深度混淆，以躲避安全检测。它使用编码技巧和字符串混淆，使得脚本看起来像是使用 UTF-16 编码并包含中文字符，这进一步增加了分析难度。脚本在打开一个假 PDF 文件的同时，通过 PowerShell 悄悄下载包含 Python 环境和恶意 Python 程序的两个ZIP文件，并将它们解压缩隐藏在用户的配置文件目录中。

最后阶段是依次运行 Python 程序，每个程序都会加载并执行 shellcode，以绕过检测机制并部署主要有效载荷PureHVNC。

活动中的每个 Python 文件都使用 GitHub 上名为 "Kramer "的 Python 混淆器进行了精心混淆。Kramer 使用随机生成的密钥对源代码进行加密，为逆向工程增加了一层保护。shellcode 由名为 "donut "的工具生成，旨在解密并执行下一阶段的有效载荷，同时绕过 AMSI 和 WLDP 等 Windows 安全功能。

![](https://image.3001.net/images/20240813/1723518458_66bacdfa4ce77094ef323.png!small)Python混淆器“Kramer”

攻击的第二阶段引入了 shellcode 加载器 "laZzzy"，它伪装成合法的 Microsoft 管理控制台 (MMC) 应用程序。该加载器使用先进的注入技术在 notepad.exe 这个看起来无害的进程中执行最终有效载荷，从而避免被检测到。

在这场活动中部署的恶意软件中，PureHVNC 因其复杂的功能脱颖而出。作为一个 .NET 应用程序，PureHVNC 使用 .NET Reactor 进行了大量混淆处理，使其难以分析。它的主要功能是使用 AES 加密解密有效载荷，然后使用 Gzip 解压缩，提取 DLL 有效载荷并加载到内存中。

一旦激活，PureHVNC 就会执行一系列旨在保持持久性和收集情报的操作。它会使用 PowerShell 设置注册表运行键值或阻止系统休眠，确保恶意软件保持激活状态。然后，它会与命令与控制（C2）服务器通信，上报系统信息，包括已安装杀毒产品的详细信息、系统规格和用户信息。

PureHVNC 专门针对加密货币钱包、密码管理器和双因素身份验证 (2FA) 应用程序等高价值资产。它扫描这些应用的关联路径，并检查注册表中的安装软件，重点窃取敏感数据。

攻击并不仅限于 PureHVNC，C2 服务器还可以部署扩展恶意软件功能的其他插件。这场活动中发现的两个值得注意的插件是：

### 插件 1：PluginRemoteDesktop

该插件可远程控制受害者的系统。它与 C2 服务器通信以执行命令，允许攻击者操纵受害者的桌面环境、捕获屏幕截图、控制鼠标等。

### 插件 2：PluginExecuting

该插件用于执行附加文件、更新恶意软件，甚至卸载恶意软件以掩盖踪迹。它支持多种命令，包括下载和执行新恶意软件的命令，利用进程挖空技术将恶意代码注入合法进程中。

FortiGuard 实验室的网络安全研究人员敦促组织对此类威胁保持警惕，确保员工了解网络钓鱼电子邮件的危险性，并采取强有力的安全措施来检测和缓解多阶段攻击。正如此次活动所表明的，即使是最看似无害的电子邮件，也可能成为破坏性漏洞的起点。

参考来源：
https://securityonline.info/new-phishing-campaign-deploys-purehvnc-and-other-malware-targets-sensitive-data/

# 钓鱼攻击 # 钓鱼邮件 # 网络钓鱼攻击

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