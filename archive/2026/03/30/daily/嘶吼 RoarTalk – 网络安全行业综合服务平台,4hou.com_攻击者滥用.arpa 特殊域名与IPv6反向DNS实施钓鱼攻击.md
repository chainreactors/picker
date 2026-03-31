---
title: 攻击者滥用.arpa 特殊域名与IPv6反向DNS实施钓鱼攻击
url: https://www.4hou.com/posts/Zg5g
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-30
fetch_date: 2026-03-31T04:35:38.972936
---

# 攻击者滥用.arpa 特殊域名与IPv6反向DNS实施钓鱼攻击

攻击者滥用.arpa 特殊域名与IPv6反向DNS实施钓鱼攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者滥用.arpa 特殊域名与IPv6反向DNS实施钓鱼攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-03-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9393

收藏

导语：由于 .arpa 域名专用于互联网基础设施，不包含普通注册域名的公开信息，如 WHOIS 注册信息、域名年龄、联系方式等，导致邮件网关与安全工具更难识别其恶意属性。

网络黑产团伙正在滥用专用顶级域名 .arpa 以及 IPv6 反向域名解析（DNS）开展钓鱼活动，此类攻击可更轻松地绕过域名信誉检测机制与邮件安全网关。

.arpa 是为互联网基础设施预留的特殊顶级域名，并非用于普通网站，主要用于反向 DNS 解析，即让系统将 IP 地址反向映射为对应的主机名。

例如，www.google.com 的 IP 地址为 192.178.50.36 (IPv4) 和 2607:f8b0:4008:802::2004 (IPv6)。使用 dig 工具查询 Google 的 IP 地址 192.178.50.36 会解析为 in-addr.arpa 主机名，最终解析为常规主机名：

```
; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> -x 192.178.50.36
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 59754
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;36.50.178.192.in-addr.arpa.  IN   PTR
;; ANSWER SECTION:
36.50.178.192.in-addr.arpa. 1386 IN  PTR  lcmiaa-aa-in-f4.1e100.net.
;; Query time: 7 msec
;; SERVER: 127.0.0.1#53(127.0.0.1) (UDP)
;; WHEN: Fri Mar 06 13:57:31 EST 2026
;; MSG SIZE  rcvd: 94
```

查询 Google 的 IPv6 地址 2607:f8b0:4008:802::2004 显示，它首先解析为 IPv6.arpa 主机名，然后解析为主机名，如下所示。

```
; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> -x 2607:f8b0:4008:802::2004
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 31116
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;4.0.0.2.0.0.0.0.0.0.0.0.0.0.0.0.2.0.8.0.8.0.0.4.0.b.8.f.7.0.6.2.ip6.arpa. IN PTR
;; ANSWER SECTION:
4.0.0.2.0.0.0.0.0.0.0.0.0.0.0.0.2.0.8.0.8.0.0.4.0.b.8.f.7.0.6.2.ip6.arpa. 78544 IN PTR tzmiaa-af-in-x04.1e100.net.
4.0.0.2.0.0.0.0.0.0.0.0.0.0.0.0.2.0.8.0.8.0.0.4.0.b.8.f.7.0.6.2.ip6.arpa. 78544 IN PTR mia07s48-in-x04.1e100.net.
;; Query time: 10 msec
;; SERVER: 127.0.0.1#53(127.0.0.1) (UDP)
;; WHEN: Fri Mar 06 13:58:43 EST 2026
;; MSG SIZE  rcvd: 171
```

**钓鱼攻击滥用 .arpa 域名的真实手法**

安全研究员观测到的一起钓鱼攻击活动，正是利用了 ip6.arpa 这一反向 DNS 顶级域名。正常情况下，该域名仅用于 PTR 记录，实现 IPv6 地址到主机名的反向映射。

但攻击者发现：只要申请并持有一段专属的 IPv6 地址段，就可以控制该网段对应的反向 DNS 区域，并在其中配置额外的 DNS 记录，用于搭建钓鱼站点。

在标准 DNS 功能中，反向 DNS 域名仅用于 PTR 记录，用于查询 IP 对应的主机名。然而攻击者发现，在获取某段 IPv6 地址的 DNS 区域控制权后，部分 DNS 管理平台允许其配置非 PTR 类型的记录，进而被滥用于钓鱼攻击。

研究员指出：发现黑产团伙利用Hurricane Electric与 Cloudflare 平台创建此类记录——这两家服务商本身信誉良好，攻击者正是利用了这一点。同时，其他部分 DNS 服务商也支持此类配置。

下图展示了攻击者构造钓鱼邮件所用域名的完整流程，为搭建攻击基础设施，攻击者先通过 IPv6 隧道服务获取一段 IPv6 地址。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260309/1773041243154733.png "1773041152202734.png")

对 .arpa 顶级域名在网络钓鱼邮件中被滥用情况的概述

在获得地址段控制权后，攻击者基于该 IPv6 网段生成反向 DNS 主机名，并搭配随机子域名，使其难以被检测和封堵。

与常规配置 PTR 记录不同，攻击者直接创建 A 记录，将这些反向 DNS 域名指向钓鱼站点服务器。该钓鱼活动中的邮件通常以奖品、调研奖励或账户通知为诱饵，并将恶意链接伪装成图片嵌入邮件。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260309/1773041251206050.png "1773041177104994.png")

网络钓鱼邮件诱饵

链接地址如：d.d.e.0.6.3.0.0.0.7.4.0.1.0.0.2.ip6.arpa而非常规域名，受害者在界面上无法直接看到可疑的 .arpa 域名。

当受害者点击钓鱼邮件中的图片时，设备会通过第三方 DNS 服务商，解析到攻击者控制的反向 DNS 域名服务器。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260309/1773041249990576.png "1773041249990576.png")

使用 .arpa 主机名显示图像和链接的 HTML 代码

在部分案例中，权威域名服务器由 Cloudflare 托管，反向 DNS 域名最终解析至 Cloudflare IP，从而隐藏后端钓鱼基础设施的真实位置。

点击图片后，受害者会先被跳转至流量分发系统（TDS）。该系统会根据设备类型、IP 地址、页面来源等条件判断目标是否有效。符合条件者会被跳转到钓鱼页面，否则跳转到正常网站。

此类钓鱼链接存活时间极短，通常仅有效数天。链接失效后，会跳转至域名错误页面或正规网站。研究人员认为，这种做法是为了增加安全研究人员分析与溯源的难度。

此外，由于 .arpa 域名专用于互联网基础设施，不包含普通注册域名的公开信息，如 WHOIS 注册信息、域名年龄、联系方式等，导致邮件网关与安全工具更难识别其恶意属性。

研究人员还发现，该钓鱼活动同时结合了其他攻击手段，包括劫持悬空 CNAME 记录、子域名影子劫持等，使攻击者能够借助正规机构的子域名下发钓鱼内容。

研究员目前已发现超过 100 个相关案例，攻击者劫持了知名政府机构、高校、电信运营商、媒体机构及零售企业的 CNAME 记录。通过将安全工具普遍信任的反向 DNS 机制武器化，攻击者可生成能够绕过传统检测规则的钓鱼 URL。

与所有钓鱼防御建议一致，抵御此类攻击最有效的方式，仍是避免点击邮件中来历不明的链接，直接通过官方网站访问相关服务。

文章来源自：https://www.bleepingcomputer.com/news/security/hackers-abuse-arpa-dns-and-ipv6-to-evade-phishing-defenses/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?crAoR71V)

#### 你可能感兴趣的

* [![]()

  嘶吼安全动态｜全国网安标委发布关于征集个人信息保护标准应用实践案例的通知 AI工作流工具Langflow曝未授权RCE漏洞](https://www.4hou.com/posts/l0Kj)
* [![]()

  攻击者滥用.arpa 特殊域名与IPv6反向DNS实施钓鱼攻击](https://www.4hou.com/posts/Zg5g)
* [![]()

  嘶吼安全动态｜国家安全部：搜索引擎排名遭 “投毒”，恶意链接暗藏窃取风险 谷歌发布高风险Chrome安全更新](https://www.4hou.com/posts/kgJJ)
* [![]()

  嘶吼安全动态｜国家安全部提示：谨防深度伪造魔改陷阱 Forescout发布2026高风险连接设备报告](https://www.4hou.com/posts/jBGy)
* [![]()

  AI时代中国网络安全产业的五年变局|| 影子AI之困：企业数据安全最大的灰犀牛](https://www.4hou.com/posts/vwXn)
* [![]()

  嘶吼安全动态｜工信部征求AI安全治理标准，规范模型上下文协议安全 浙江警方破获特大电商数据泄露案，200万条订单信息被贩卖](https://www.4hou.com/posts/rpQL)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [嘶吼安全动态｜全国网安标委发布关于征集个人信息保护标准应用实践案例的通知 AI工作流工具Langflow曝未授权RCE漏洞](https://www.4hou.com/posts/l0Kj)
  2026-03-31 11:59:00
* [攻击者滥用.arpa 特殊域名与IPv6反向DNS实施钓鱼攻击](https://www.4hou.com/posts/Zg5g)
  2026-03-30 12:00:00
* [嘶吼安全动态｜国家安全部：搜索引擎排名遭 “投毒”，恶意链接暗藏窃取风险 谷歌发布高风险Chrome安全更新](https://www.4hou.com/posts/kgJJ)
  2026-03-30 11:59:00
* [嘶吼安全动态｜国家安全部提示：谨防深度伪造魔改陷阱 Forescout发布2026高风险连接设备报告](https://www.4hou.com/posts/jBGy)
  2026-03-27 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [嘶吼安全动态｜全国网安标委发布关于征集个人信息保护标准应用实践案例的通知 AI工作流工具Langflow曝未授权RCE漏洞](https://www.4hou.com/posts/l0Kj)

  胡金鱼
* [攻击者滥用.arpa 特殊域名与IPv6反向DNS实施钓鱼攻击](https://www.4hou.com/posts/Zg5g)

  胡金鱼
* [嘶吼安全动态｜国家安全部：搜索引擎排名遭 “投毒”，恶意链接暗藏窃取风险 谷歌发布高风险Chrome安全更新](https://www.4hou.com/posts/kgJJ)

  胡金鱼
* [嘶吼安全动态｜国家安全部提示：谨防深度伪造魔改陷阱 Forescout发布2026高风险连接设备报告](https://www.4hou.com/posts/jBGy)

  胡金鱼
* [AI时代中国网络安全产业的五年变局|| 影子AI之困：企业数据安全最大的灰犀牛](https://www.4hou.com/posts/vwXn)

  山卡拉
* [嘶吼安全动态｜工信部征求AI安全治理标准，规范模型上下文协议安全 浙江警方破获特大电商数据泄露案，200万条订单信息被贩卖](https://www.4hou.com/posts/rpQL)

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
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/n...