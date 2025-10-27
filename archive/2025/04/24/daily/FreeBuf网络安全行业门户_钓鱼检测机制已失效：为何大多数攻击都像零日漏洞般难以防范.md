---
title: 钓鱼检测机制已失效：为何大多数攻击都像零日漏洞般难以防范
url: https://www.freebuf.com/articles/web/428525.html
source: FreeBuf网络安全行业门户
date: 2025-04-24
fetch_date: 2025-10-06T22:05:56.623465
---

# 钓鱼检测机制已失效：为何大多数攻击都像零日漏洞般难以防范

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

钓鱼检测机制已失效：为何大多数攻击都像零日漏洞般难以防范

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

钓鱼检测机制已失效：为何大多数攻击都像零日漏洞般难以防范

2025-04-23 10:02:12

所属地 上海

![推送式钓鱼攻击头图](https://image.3001.net/images/20250424/1745424276521178_1ed3094409cc492ba8e75f7e2d19a622.jpg!small)

## 钓鱼攻击威胁持续升级

2025年，钓鱼攻击仍是企业面临的重大安全挑战。随着攻击者越来越多地采用基于身份验证的技术而非软件漏洞利用，钓鱼攻击的威胁程度甚至超过以往。如今绕过多因素认证（MFA）的钓鱼工具包已成常态，能够窃取受短信验证码、一次性密码（OTP）和推送验证保护的账户，在预防措施失效的情况下，检测系统承受着持续压力。

钓鱼检测的核心困境在于：基于行业通用的钓鱼页面识别指标（IoC），几乎每个钓鱼攻击都使用独特的域名、URL、IP地址、页面结构、目标应用等组合。实质上，每次钓鱼攻击都是全新的——甚至可称之为"零日攻击"（这说法可能令人倒吸凉气）。本文目的并非夸大钓鱼威胁，而是揭示当前检测机制的缺陷。如果每次钓鱼攻击都像零日漏洞，说明我们的检测方法存在根本性问题。

## 钓鱼检测基础原理

典型钓鱼攻击流程包含三个环节：攻击者向用户发送恶意链接→用户点击加载恶意页面→该页面通常是特定网站的登录门户，旨在窃取受害者账户凭证。当前检测机制主要依赖由已确认的恶意页面指标（IoC）组成的黑名单，这些指标包括攻击中出现的恶意域名、URL和IP地址。

安全厂商通过多种渠道收集IoC数据，但前提是该恶意页面必须已被用于实际攻击。这意味着需要潜在受害者与之交互——要么上当受骗，要么举报可疑行为。页面被标记后，安全人员或自动化工具会进行调查分析，确认存在恶意内容后将其IoC加入黑名单。这些信息随后通过威胁情报渠道传播，最终集成到安全邮件网关（SEG）、安全Web网关（SWG）等网络层防护系统中。

![基于IoC的黑名单是钓鱼检测与拦截的基础](https://image.3001.net/images/20250424/1745424277067298_b0f208f9a24f432388a3a115f2009199.png!small)

这种机制存在根本缺陷：要检测拦截钓鱼页面，必须先有受害者遭遇攻击...

## 攻击者如何制造"全新"钓鱼攻击

现代攻击者深谙钓鱼检测的三大弱点：(1)依赖域名/URL/IP黑名单 (2)部署在邮件和网络层 (3)需先访问分析页面才能拦截。这些十年未变的方法已被攻击者轻松规避。

### 轻松绕过IoC检测

钓鱼域名本身具有高度可弃性：攻击者批量购买域名、劫持合法网站，并预设域名会被封杀。现代钓鱼架构还能动态轮换特征元素——例如从持续更新的链接池分配不同URL给每个点击者，甚至采用一次性魔法链接（使后续安全调查无法复现）。当域名被标记为恶意时，攻击者只需注册新域名或入侵受信任的WordPress服务器即可，这两种手段目前已被大规模使用。

### 多渠道攻击规避邮件检测

攻击者采用跨平台组合攻击规避邮件检测：通过即时通讯、社交媒体、恶意广告或可信应用发送信息。例如先在社交平台发送含链接的"无害"PDF，最终导向恶意网页。邮件安全方案虽有发件人信誉评估和DMARC/DKIM等检查，但无法直接识别恶意页面。深度邮件内容分析也仅能发现可疑链接，对跨媒介攻击束手无策。

![攻击者通过IM、社交媒体、恶意广告和可信应用实施跨平台钓鱼](https://image.3001.net/images/20250424/1745424277354446_23d2f4b2b4cd487f82d31767ca7e771d.png!small)

### 阻止安全分析的手段

现代钓鱼页面已非静态HTML，而是通过JavaScript动态渲染的Web应用，使基础静态检测失效。为应对沙箱分析，攻击者部署验证码或Cloudflare Turnstile等机器人防护。即使突破这些防护，还需提供正确的URL参数、请求头并执行JavaScript才能触发恶意内容。此外，攻击者还混淆视觉和DOM元素以规避特征检测。

![Cloudflare Turnstile等机器人检查能有效绕过沙箱分析工具](https://image.3001.net/images/20250424/1745424277647822_6f2856ad8eeb4e04a3d46268441a0683.png!small)

## 事后检测模式亟待变革

这些规避技术导致实时钓鱼检测几乎不存在。基于代理的解决方案最多能通过用户交互产生的网络流量检测恶意行为，但由于TLS加密后网络请求重构的复杂性，这种检测存在延迟且不可靠。从页面被标记到IoC分发至黑名单，通常需要数天甚至数周——这就是为何大多数钓鱼攻击都能"全新"出现：当前检测本质是事后追溯（post mortem），依赖已知恶意指标。而指标被标记为恶性的前提，恰恰是有用户已上当...

## 浏览器安全：钓鱼防御新战线

终端安全的发展历程为我们指明方向：2000年代末期，当终端攻击激增时，依赖网络检测、文件特征分析和沙箱运行的防御方式，最终被端点检测与响应（EDR）技术取代。EDR通过实时监控操作系统活动实现了有效防护。

![EDR在操作系统层面实现实时检测响应](https://image.3001.net/images/20250424/1745424278832564_8fa3709ea8654c468e9c1417e52abfc3.png!small)

当前我们面临相似转折点：现代钓鱼攻击发生在浏览器访问的网页上，而依赖邮件、网络甚至终端的检测工具都缺乏必要能见度。浏览器已成为新的操作系统——既是主要工作场景，也是攻击发生地。

![现有钓鱼检测无法实时观察阻止恶意活动](https://image.3001.net/images/20250424/1745424281074574_c4c817cd45c24c14b69b10da1fe17cdb.png!small)

要实现有效防护，必须能在用户访问时实时观察页面内容（而非沙箱环境），才能建立基于战术技术流程（TTP）而非易变IoC的检测体系。

![实时监控页面行为是实现TTP检测的关键](https://image.3001.net/images/20250424/1745424282973218_c6e40a20e4dc4488901634e6f43bebe9.png!small)

## 浏览器扩展防护实战对比

攻击者入侵WordPress获取可信域名后部署钓鱼工具包，向员工发送含恶意链接的邮件。传统SWG或邮件扫描方案在沙箱检测时，钓鱼工具会重定向至无害页面通过检查。最终用户可自由访问钓鱼页面，输入凭证和MFA代码导致账户沦陷。

![传统防护下的攻击流程](https://image.3001.net/images/20250424/1745424285220120_a42818cc0dc549b19bce086132849d78.png!small)

而部署浏览器安全扩展后，系统能实时检测到：用户输入的密码曾用于其他网站（密码重用或正被钓鱼）、页面克隆自合法登录页、页面运行着钓鱼工具包。随即阻止用户继续交互，从根本上阻断攻击。

![浏览器扩展实时拦截钓鱼攻击](https://image.3001.net/images/20250424/1745424286839573_8c19d36facc54ba3bdf483e74463b411.png!small)

这种防护机制使攻击者难以规避——当用户无法在钓鱼页面输入凭证时，攻击自然失效。

**参考来源：**

> [Phishing detection is broken: Why most attacks feel like a zero day](https://www.bleepingcomputer.com/news/security/phishing-detection-is-broken-why-most-attacks-feel-like-a-zero-day/)

# web安全 # 企业安全

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

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