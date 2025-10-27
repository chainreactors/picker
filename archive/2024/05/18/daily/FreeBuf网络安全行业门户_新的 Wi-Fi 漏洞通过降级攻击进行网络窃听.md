---
title: 新的 Wi-Fi 漏洞通过降级攻击进行网络窃听
url: https://www.freebuf.com/news/401222.html
source: FreeBuf网络安全行业门户
date: 2024-05-18
fetch_date: 2025-10-06T16:51:22.056563
---

# 新的 Wi-Fi 漏洞通过降级攻击进行网络窃听

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

新的 Wi-Fi 漏洞通过降级攻击进行网络窃听

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新的 Wi-Fi 漏洞通过降级攻击进行网络窃听

2024-05-17 11:34:58

所属地 上海

据英国TOP10VPN的一份最新研究报告指出，一种基于 IEEE 802.11 Wi-Fi 标准中的设计缺陷能够允许攻击者诱导用户连接至不安全的网络，进而对用户进行网络窃听。

![](https://image.3001.net/images/20240517/1715916935_6646d08729aca9549827d.png!small)

报告指出，该缺陷是基于CVE-2023-52424 SSID 混淆攻击的漏洞利用，涉及所有操作系统和 Wi-Fi 客户端，包括基于 WEP、WPA3、802.11X/EAP 和 AMPE 协议的家庭网络和网状网络。

TopVPN表示，攻击者可以通过发动 "中间人"（AitM）攻击，欺骗客户端连接到一个不受信任的 Wi-Fi 网络，而不是它打算连接的网络。比如当用户想要连接到网络 TrustedNet 时，攻击者会诱骗它连接到使用类似凭证的另一个网络 WrongNet。因此，用户客户端会显示连接到了 TrustedNet，而实际上却连接到的是 WrongNet。

换句话说，即使在连接到受保护的 Wi-Fi 网络时——密码或其他凭证经过了相互验证，也不能保证用户连接到的是他们想要的网络。

研究人员指出，之所以能够利用这一缺陷，一个重要原因是目前的Wi-Fi网络依靠 4 路握手来验证自己和客户端的身份，并协商加密连接的密钥。4路握手需要一个共享的配对主密钥（PMK），根据Wi-Fi版本和所使用的特定认证协议，PMK可以以不同的方式获得。

问题在于，IEEE 802.11 标准并未强制要求在密钥推导过程中包含 SSID。换句话说，当客户端设备连接到 SSID 时，SSID 并不总是认证过程的一部分。在这些实施过程中，攻击者有机会设置一个恶意接入点，欺骗受信任网络的 SSID，并利用它将受害者降级到信任度较低的网络。

攻击者要利用这一弱点，必须具备某些条件，即只在可能拥有两个共享凭证的 Wi-Fi 网络的情况下起作用。例如，环境中可能有分别有一个 2.4 GHz 和5GHz 网络频段，每个频段都有不同的 SSID，但具有相同的验证凭据。通常情况下，客户端设备会连接到安全性更好的 5 GHz 网络。但如果攻击者足够接近目标网络以实施中间人攻击，就可以粘贴一个与 5 GHz 频段具有相同 SSID 的恶意接入点，然后就可以利用恶意接入点接收所有验证帧并将其转发到较弱的 2.4 GHz 接入点，让客户端设备与该网络连接。

值得注意的是，在某些情况下它还可能使 VPN 保护失效。研究人员表示，许多 VPN，如 Clouldflare's Warp、hide.me 和 Windscribe在连接到受信任的 Wi-Fi 网络时可以自动禁用 VPN。他们指出，这是因为 VPN 根据 SSID 识别 Wi-Fi 网络。

TOP10VPN也指出了了针对SSID混淆攻击的三种防御措施：

* 更新IEEE 802.11标准，以强制执行SSID身份验证；
* 妥善存储接入点定期发送的信标，以在客户端连接时能检测 SSID 变化；
* 避免在不同的 SSID 之间重复使用凭证。

**参考来源：**

> [New Wi-Fi Vulnerability Enables Network Eavesdropping via Downgrade Attacks](https://thehackernews.com/2024/05/new-wi-fi-vulnerability-enabling.html)
>
> [Flaw in Wi-Fi Standard Can Enable SSID Confusion Attacks](https://www.darkreading.com/endpoint-security/flaw-in-wi-fi-standard-can-enable-ssid-confusion-attacks)

# 移动安全

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