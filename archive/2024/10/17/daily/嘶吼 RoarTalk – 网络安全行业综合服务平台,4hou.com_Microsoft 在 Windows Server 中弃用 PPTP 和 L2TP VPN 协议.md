---
title: Microsoft 在 Windows Server 中弃用 PPTP 和 L2TP VPN 协议
url: https://www.4hou.com/posts/jBnz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-17
fetch_date: 2025-10-06T18:48:13.891535
---

# Microsoft 在 Windows Server 中弃用 PPTP 和 L2TP VPN 协议

Microsoft 在 Windows Server 中弃用 PPTP 和 L2TP VPN 协议 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Microsoft 在 Windows Server 中弃用 PPTP 和 L2TP VPN 协议

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-10-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)112384

收藏

导语：Windows RRAS Server 的未来版本将不再接受使用 PPTP 和 L2TP 协议的传入连接。

Microsoft 已在未来版本的 Windows Server 中正式弃用点对点隧道协议 (PPTP) 和第 2 层隧道协议 (L2TP)，并建议管理员切换到提供更高安全性的不同协议。

20 多年来，该企业一直使用 PPTP 和 L2TP VPN 协议来提供对企业网络和 Windows 服务器的远程访问。

然而，随着网络安全攻击和资源变得更加复杂和强大，协议变得越来越不安全。例如，PPTP 很容易受到捕获的身份验证哈希值的离线强力攻击，而 L2TP 不提供加密，除非与其他协议（如 IPsec）结合使用。

但是，如果 L2TP/IPsec 配置不正确，可能会引入使其容易受到攻击的弱点。

因此，Microsoft 建议用户转向更新的安全套接字隧道协议 (SSTP) 和 Internet 密钥交换版本 2 (IKEv2) 协议，这些协议可提供更好的性能和安全性。

微软表示：“此举是微软战略的一部分，旨在通过将用户过渡到安全套接字隧道协议（SSTP）和互联网密钥交换版本 2（IKEv2）等更强大的协议来增强安全性和性能。”

这些更新协议能提供相对来说的更加安全的加密、更快的连接速度和更好的可靠性，使它们更适合当今日益复杂的网络环境。

Microsoft 还分享了每个协议的以下优点：

**SSTP 的优点**

**·强加密**：SSTP使用SSL/TLS加密，提供安全的通信通道。

**·防火墙穿越**：SSTP可以轻松穿过大多数防火墙和代理服务器，确保无缝连接。

**·易于使用**：凭借 Windows 的本机支持，SSTP 的配置和部署非常简单。

**IKEv2的优点**

**·安全性高**：IKEv2支持强大的加密算法和稳健的认证方法。

**·移动性和多宿主**：IKEv2 对于移动用户特别有效，可在网络变化期间保持 VPN 连接。

**·性能卓越**：与传统协议相比，IKEv2 能够更快地建立隧道并降低延迟，提供卓越的性能。

微软强调，当一项功能被弃用时，并不意味着它被删除。相反，它只是不再处于积极开发状态，并且可能会从未来版本的 Windows 中删除。此弃用期可能会持续数月至数年，让管理员有时间迁移到建议的 VPN 协议。

作为此弃用的一部分，Windows RRAS Server（VPN 服务器）的未来版本将不再接受使用 PPTP 和 L2TP 协议的传入连接。但是，用户仍然可以进行传出 PPTP 和 L2TP 连接。

为了帮助管理员迁移到 SSTP 和 IKEv2，Microsoft 在 6 月份发布了支持公告，其中包含了有关如何配置这些协议的步骤。

文章翻译自：https://www.bleepingcomputer.com/news/microsoft/microsoft-deprecates-pptp-and-l2tp-vpn-protocols-in-windows-server/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?n9HILybu)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)