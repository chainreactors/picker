---
title: FreeBuf 周报 | 谷歌拟允许Web应用访问敏感USB设备；GitLab曝严重漏洞
url: https://www.freebuf.com/news/405330.html
source: FreeBuf网络安全行业门户
date: 2024-07-06
fetch_date: 2025-10-06T17:43:31.286276
---

# FreeBuf 周报 | 谷歌拟允许Web应用访问敏感USB设备；GitLab曝严重漏洞

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

FreeBuf 周报 | 谷歌拟允许Web应用访问敏感USB设备；GitLab曝严重漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

FreeBuf 周报 | 谷歌拟允许Web应用访问敏感USB设备；GitLab曝严重漏洞

2024-07-05 17:11:03

所属地 上海

各位 Buffer 周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、安全事件、一周好文和省心工具，保证大家不错过本周的每一个重点！![](https://image.3001.net/images/20220923/1663923572_632d7574ead5a97f52086.jpg!small)

## 热点资讯

### 1. 谷歌拟允许独立 Web应用访问敏感的USB设备

WebUSB 是一种 JavaScript API，能够让网络应用程序访问计算机上的本地 USB 设备。作为 WebUSB 规范的一部分，某些接口，比如HID、大容量存储、智能卡、视频、音频/视频设备和无线控制器会受保护，不能通过网络应用程序访问，以防止恶意脚本访问潜在的敏感数据。

### 2. 影响大量路由器，Juniper Networks曝最严重的“身份验证”漏洞

该漏洞编号为CVE-2024-2973，攻击者可利用该漏洞完全控制设备。简单来说，JuniperSession Smart 路由器、Session Smart Conductor在运行冗余对等设备时，存在使用替代路径或通道绕过身份验证的漏洞，从而使得攻击者可以有效绕过身份验证，并对设备具有高控制度。

### 3. OpenSSH漏洞预警：无需用户交互，可提权至 root

成功利用该漏洞的攻击者可以以 root 身份进行未经身份验证的远程代码执行 (RCE)。在某些特定版本的 32 位操作系统上，攻击者最短需 6-8 小时即可获得最高权限的 root shell。而在 64 位机器上，目前没有在可接受时间内的利用方案，但未来的改进可能使其成为现实。

### 4. 国际行动关闭了 593 台恶意 Cobalt Strike 服务器

这项为期一周的行动于 2024 年 6 月 24 日开始，代号为“墨菲斯行动”，由英国国家犯罪局（NCA）牵头，由欧洲刑警组织协调。参与的机构包括联邦调查局、澳大利亚联邦警察和加拿大皇家骑警，针对 27 个国家和地区的 129 家互联网服务提供商的 690 个恶意 Cobalt Strike 软件实例。

### 5. 100 亿条密码汇编集合 RockYou2024 泄露，酿成史上最大密码泄露事件

RockYou2024密码汇编集合里包含世界各地个人使用的真实密码。研究人员认为，黑客将数量如此庞大的密码泄露出去，大大增加了凭证填充攻击的风险。

## 安全事件

### 1. GitLab 曝一严重漏洞，威胁软件开发管道

在 GitLab 中，管道可以自动完成构建、测试和部署代码的过程。从理论上讲，攻击者如果有能力以其他用户的身份运行管道，就可以访问他们的私有存储库，并操作、窃取或外泄其中包含的敏感代码和数据。

### 2.Kimsuky 组织利用 TRANSLATEXT Chrome 扩展程序窃取敏感数据信息

网络安全公司 CyberArmor 指出，该恶意程序后门似乎此前从未公开记录过，允许威胁攻击者执行基本侦察，并投放额外的有效载荷来接管或远程控制机器。目前，尚不清楚与新发现活动相关的初始访问的确切模式，但是，研究人员已经获悉该组织利用鱼叉式网络钓鱼和社交工程攻击来激活感染链。

### 3. 澳大利亚男子炮制虚假航空公司WIFI骗取乘客账户凭证

该男子42岁，通过便携式设备模仿航空公司及飞机上提供的官方WIFI名称建立虚假网络，当用户尝试连接时会被定向到虚假登录页面或强制门户网页，要求他们使用电子邮件地址、密码或其他凭证登录。

### 4. Xbox 全球瘫痪，多个平台用户受影响

这次中断影响了不同平台的用户，包括云游戏、Xbox One 游戏机、Windows 上的 Xbox、安卓设备、苹果设备和网络服务等。在第一批用户报告出现在网上几个小时之后，Xbox 团队承认了这一问题。

### 5. 黑客滥用 API 端点验证了数百万个Authy MFA 电话号码

Twilio 表示，有威胁分子使用了一个未经验证的 API 端点编译了电话号码列表。目前，Twilio 检测到由于使用了未经身份验证的端点，威胁行为者能够识别与 Authy 账户相关的数据，包括电话号码。Twilio 现已采取措施保护该端点的安全，不再允许未经身份验证的请求。

## 一周好文共读

### 1. PowerShell 技术在网络安全测试中的应用

在现代网络安全领域，渗透测试工具的选择和使用方式显得尤为关键。PowerShell，作为一种强大的自动化和配置管理工具，不仅仅是系统管理员的利器，同样也是渗透测试者的得力助手。本文将探讨如何利用 PowerShell 的高级功能，如动态函数定义、反射、文件系统监控以及并行处理，来增强渗透测试的效率和效果。【[阅读全文](https://www.freebuf.com/articles/web/404542.html)】

![1719383456_667bb5a05000ee7693c04.png](https://image.3001.net/images/20240626/1719383456_667bb5a05000ee7693c04.png)

### 2. 攻防演练中的IPv6（上）针对IPv6的扫描与攻击

IPv6是（Internet Protocol version 6）是互联网协议的一种版本，用来为连接到互联网的设备来分配唯一的IP地址以便于标识。本身IPV6的设计是为了接替IPv4（Internet Protocol version 4），因为IPv4现在面临一个巨大的问题，那就是IPV4的地址空间不足。【[阅读全文](https://www.freebuf.com/defense/378522.html)】

![1](https://image.3001.net/images/20230919/1695093185_650911c14a03eeb2cab28.png!small)

### 3. 深度好文 | 从零开始构建大模型安全测试基准

通过自动发现LM有害的地方（“红队”）来补充手动测试并减少这种疏忽。为此，我们使用AI本身生成测试输入，并使用分类器检测测试输入上的有害行为。基于LM的红队使我们能够发现成千上万的多样化失败案例，而无需手工编写它们。【[阅读全文](https://www.freebuf.com/articles/es/404287.html)】

![1719198198_6678e1f6016c872e387dd.png!small?1719198198682](https://image.3001.net/images/20240624/1719198198_6678e1f6016c872e387dd.png!small?1719198198682)

## 省心工具

### 1. CrimsonEDR：一款恶意软件模式识别与EDR策略评估工具

CrimsonEDR是一个功能强大的开源项目，该项目旨在帮助广大研究人员识别特定的恶意软件模式，以此来优化终端检测与响应（EDR）的策略方案。通过使用各种不同的检测方案，可以加深开发人员与研究人员加深对安全规避策略的理解。【[阅读全文](https://www.freebuf.com/sectool/404792.html)】

![1719564735_667e79bfbf809fcd7dcff.png!small](https://image.3001.net/images/20240628/1719564735_667e79bfbf809fcd7dcff.png!small)

### 2. APKDeepLens：一款针对Android应用程序的安全扫描工具

APKDeepLens是一款针对Android应用程序的安全扫描工具，该工具基于Python开发，旨在扫描和识别Android应用程序（APK文件）中的安全漏洞。【[阅读全文](https://www.freebuf.com/sectool/404813.html)】

![1719567578_667e84da15a4003f28931.jpg!small](https://image.3001.net/images/20240628/1719567578_667e84da15a4003f28931.jpg!small)

### 3. AttackGen：一款基于LLM的网络安全事件响应测试工具

AttackGen是一款功能强大的网络安全事件响应测试工具，该工具利用了大语言模型和MITRE ATT&CK框架的强大功能，并且能够根据研究人员选择的威胁行为组织以及自己组织的详细信息生成定制化的事件响应场景。【[阅读全文](https://www.freebuf.com/sectool/405042.html)】

![](https://image.3001.net/images/20240702/1719914602_6683d06a5cc76eddc17e2.png!small)

# FreeBuf周报

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

热点资讯

* 1. 谷歌拟允许独立 Web应用访问敏感的USB设备
* 2. 影响大量路由器，Juniper Networks曝最严重的“身份验证”漏洞
* 3. OpenSSH漏洞预警：无需用户交互，可提权至 root
* 4. 国际行动关闭了 593 台恶意 Cobalt Strike 服务器
* 5. 100 亿条密码汇编集合 RockYou2024 泄露，酿成史上最大密码泄露事件

安全事件

* 1. GitLab 曝一严重漏洞，威胁软件开发管道
* 2.Kimsuky 组织利用 TRANSLATEXT Chrome 扩展程序窃取敏感数据信息
* 3. 澳大利亚男子炮制虚假航空公司WIFI骗取乘客账户凭证
* 4. Xbox 全球瘫痪，多个平台用户受影响
* 5. 黑客滥用 API 端点验证了数百万个Authy MFA 电话号码

一周好文共读

* 1. PowerShell 技术在网络安全测试中的应用
* 2. 攻防演练中的IPv6（上）针对IPv6的扫描与攻击
* 3. 深度好文 | 从零开始构建大模型安全测试基准

省心工具

* 1. CrimsonEDR：一款恶意软件模式识别与EDR策略评估工具
* 2. APKDeepLens：一款针对Android应用程序的安全扫描工具
* 3. AttackGen：一款基于LLM的网络安全事件响应测试工具

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