---
title: 至少35个Chrome扩展被劫持，新细节揭示了黑客的攻击手法
url: https://www.freebuf.com/news/418912.html
source: FreeBuf网络安全行业门户
date: 2025-01-03
fetch_date: 2025-10-06T20:09:27.930404
---

# 至少35个Chrome扩展被劫持，新细节揭示了黑客的攻击手法

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

至少35个Chrome扩展被劫持，新细节揭示了黑客的攻击手法

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

至少35个Chrome扩展被劫持，新细节揭示了黑客的攻击手法

2025-01-02 11:41:04

所属地 上海

据BleepingComputer消息，近期，黑客针对多个Chrome扩展程序进行了攻击，数十万用户受到影响。随着调查的深入，一些攻击活动细节也得到了披露。

根据最新调查，攻击导致至少 35 个扩展程序被植入数据窃取代码，较之前的初步怀疑数量直接翻倍，其中包括来自网络安全公司 Cyberhaven 的扩展。尽管最初的报道集中在 Cyberhaven 的安全扩展上，但随后的调查显示，这些扩展被大约 260 万人使用。

根据 LinkedIn 和Google Groups 上目标开发者的报告，攻击活动大约在 2024 年12 月5 日开始。然而，BleepingComputer 发现的早期命令和控制子域名早在 2024 年 3 月就已经存在。

## **一个欺骗性的 OAuth 攻击链**

攻击始于直接发送给 Chrome 扩展开发者或通过与其域名关联的支持邮箱发送的钓鱼邮件。 BleepingComputer 发现以下域名在此活动中被用来发送钓鱼邮件：

* supportchromestore.com
* forextensions.com
* chromeforextension.com

钓鱼邮件伪装成来自 Google官方，声称扩展违反了 Chrome Web Store 政策，并面临被删除的风险。

“我们不允许扩展包含误导性、格式不良、非描述性、无关、过多或不适当的元数据，包括但不限于扩展描述、开发者名称、标题、图标、截图和宣传图片，”钓鱼邮件中写道。

具体来说，扩展开发者被引导相信其软件描述包含误导信息，必须同意 Chrome Web Store 政策。

![](https://image.3001.net/images/20250102/1735796460_677626ec410d3a55f5b4a.png!small)攻击中使用的网络钓鱼电子邮件

如果开发者点击嵌入的“前往政策”按钮以了解他们违反了哪些规则，他们将被带到一个 Google 域上含有恶意OAuth 应用程序的合法登录页面，该页面是 Google 标准授权流程的一部分，旨在安全地授予第三方应用程序访问特定 Google 账户资源的权限。

在该平台上，攻击者托管了一个名为“隐私政策扩展”的恶意 OAuth 应用程序，要求受害者授予通过其账户管理 Chrome Web Store 扩展的权限。在这过程中，多因素认证（MFA）并未帮助开发者保护账户，因为 OAuth 授权流程中不需要直接批准，而是默认用户完全理解他们授予的权限范围。

![](https://image.3001.net/images/20250102/1735796540_6776273c265c61a1db092.png!small)权限审批提示

Cyberhaven 在事后分析中解释道，有员工遵循了标准流程，无意中授权了这个恶意的第三方应用程序。但员工启用了 Google 高级保护，并且账户覆盖了 MFA，且在过程中没有收到 MFA 提示，员工的 Google 凭证未被泄露。

一旦威胁行为者获得了扩展开发者账户的访问权限，便会修改扩展，加入“worker.js”和“content.js” 两个恶意文件，其中包含从 Facebook 账户窃取数据的代码。

这些恶意扩展随后作为新版本发布在 Chrome Web Store 。虽然 Extension Total 正在跟踪受此钓鱼活动影响的 35 个扩展，但攻击的 IOC 表明，目标数量远不止这些。

根据 VirusTotal 的数据，攻击者为目标扩展预注册了域名。虽然大多数域名是在 11 月和 12 月创建的，但 BleepingComputer 发现攻击者在 2024 年3 月就在对攻击进行测试。

![](https://image.3001.net/images/20250102/1735796597_67762775c9dad5a49bff8.png!small)网络钓鱼活动中使用的早期子域

## **针对 Facebook 商业账户**

对受感染机器的设备显示，攻击者瞄准了恶意扩展受害者的Facebook 账户，试图通过数据窃取代码获取 Facebook ID 、访问令牌、账户信息、广告账户信息和商业账户。

![](https://image.3001.net/images/20250102/1735796722_677627f20610cf09644d4.png!small)窃取Facebook数据的扩展程序

此外，恶意代码还添加了一个鼠标点击事件监听器，专门用于受害者在 Facebook.com 上的交互，寻找与平台的双因素认证或 CAPTCHA 机制相关的 QR 码图像，从而试图绕过 Facebook 账户的 2FA 保护并劫持账户。

被盗信息将与 Facebook cookie 、用户代理字符串、 Facebook ID 和鼠标点击事件一起打包，并外泄到攻击者的命令和控制（C2）服务器。

攻击者一直在通过各种攻击途径针对 Facebook 商业账户，以直接从受害者的信用卡窃取资金、发布虚假信息、执行钓鱼活动，或通过出售访问权限来获利。

**参考来源：**

> [New details reveal how hackers hijacked 35 Google Chrome extensions](https://www.bleepingcomputer.com/news/security/new-details-reveal-how-hackers-hijacked-35-google-chrome-extensions/)

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

一个欺骗性的 OAuth 攻击链

针对 Facebook 商业账户

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