---
title: 严重 CUPS 漏洞使 Linux 和其他系统面临远程攻击
url: https://www.anquanke.com/post/id/300521
source: 安全客-有思想的安全新媒体
date: 2024-09-30
fetch_date: 2025-10-06T18:20:02.105731
---

# 严重 CUPS 漏洞使 Linux 和其他系统面临远程攻击

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 严重 CUPS 漏洞使 Linux 和其他系统面临远程攻击

阅读量**221462**

发布时间 : 2024-09-29 15:50:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Do son，文章来源：securityonline

原文地址：<https://securityonline.info/critical-cups-vulnerabilities-expose-linux-and-other-systems-to-remote-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

在网络安全的重大发展中，在 CUPS（通用 Unix 打印系统）中发现了多个关键漏洞，CUPS（通用 Unix 打印系统）是 Linux 系统和其他平台（如 BSD、Oracle Solaris 和 Google Chrome OS）上广泛使用的打印服务器。安全研究员 Simone Margaritelli 发现了这些漏洞，并提供了一份全面的文章，详细说明了它们的潜在影响。

## CVE 详情

Margaritelli 在他的博客文章中总结了核心问题：

*“未经身份验证的远程攻击者可以静默地将现有打印机（或安装新打印机）的 IPP URL 替换为恶意 URL，从而导致在（从该计算机）启动打印作业时（在计算机上）执行任意命令。”*

这些漏洞不会影响 Linux 内核本身，但会影响 CUPS 系统的组件。分配的 CVE 包括：

* **CVE-2024-47176**漏洞此漏洞存在于 **cups-browsed**（最高版本 2.0.1）中。**cups-browsed** 守护程序在端口 631 上侦听 UDP 数据包，并使用 DNS 服务发现自动查找打印机，使其可供用户使用。该漏洞是由于未正确验证打印机发现期间收到的 URL 造成的。攻击者可利用此漏洞诱骗 **cups-browsed** 请求任意 URL。
* **漏洞：CVE-2024-47076**此漏洞存在于 **libcupsfilters**（最高版本 2.1b1）中，它与库如何处理文件转换以使其可在特定打印机上打印有关。与上一个问题类似，它允许攻击者注入恶意数据，这些数据会传递到其他 CUPS 组件。
* **CVE-2024-47175**漏洞此漏洞会影响 **libppd**（最高版本 2.1b1）。该库无法验证 IPP 属性，并无意中将它们添加到 PPD（PostScript 打印机描述）文件中，然后由驱动程序和其他组件使用，这可能会导致进一步的漏洞利用。
* **CVE-2024-47177**漏洞在 **cups-filters**（版本 2.0.1）中，此缺陷允许由无效的 PPD 参数触发任意命令执行。**cups-filters** 组件执行外部代码（“filters”）来转换文件。通过接受来自未经验证的外部来源的数据，它为攻击者执行任意代码打开了大门。具体来说，**“foomatic-rip”**过滤器使攻击者能够提供任意命令行。

此外，根据 Margaritelli 的说法，还有“其他几个或多或少可以利用的错误”。

## 利用链

这些漏洞可以链接在一起以实现远程代码执行。利用过程包括：

1. **启用 cups-browsed**：必须在目标系统上手动启用或启动 **cups-browsed** 服务。
2. **访问易受攻击的服务器**：攻击者通过以下方式获得对易受攻击的服务器的访问权限：
   * 不受限制的公共 Internet 访问，或
   * 访问本地连接受信任的内部网络。
3. **公布恶意 IPP 服务器**：攻击者公布虚假 IPP 服务器，从而有效地配置恶意打印机。
4. **受害者发起打印作业**：用户尝试使用恶意打印机进行打印。
5. **执行任意代码**：攻击者在打印作业启动期间在受害者的计算机上执行任意代码。

值得注意的是，假设 CUPS 端口通过路由器或防火墙打开，则可以通过公共互联网通过将 UDP 数据包发送到**端口 631** 来利用这种远程代码执行，而无需任何身份验证。LAN 攻击也可以通过欺骗 zeroconf、mDNS 或 DNS-SD 通告来实现。

## 影响和受影响的系统

由于 CUPS 在各种平台上的广泛使用，这些漏洞具有广泛的影响。运行 Linux 发行版的系统、某些 BSD 变体、Oracle Solaris 和 Google Chrome OS 都会受到影响。截至目前，没有适用于 Linux 系统的可用修复程序，因此立即缓解至关重要。

Margaritelli 针对 CVE-2024-47176 开发了概念验证 （PoC），可在 GitHub 公告中找到。另一个基于 OpenPrinting CUPS 存储库中提交的 PoC 也已在 GitHub 上发布。

截至 9 月 26 日，Shodan.io 显示有超过 75,000 台可访问 Internet 的主机正在运行 CUPS。FOFA 搜索引擎发现了超过 270,000 个唯一 IP 地址，其中近 70,000 个专门与 IPP 相关。这表示有大量可通过 Internet 访问的主机，其中大多数主机使用默认端口 631。

![]()

图片：Shodan.io

![]()

图片来源： FOFA

公告和所有错误均已发布：

* https://github.com/OpenPrinting/cups-browsed/security/advisories/GHSA-rj88-6mr5-rcw8
* https://github.com/OpenPrinting/libcupsfilters/security/advisories/GHSA-w63j-6g73-wmg5
* https://github.com/OpenPrinting/libppd/security/advisories/GHSA-7xfx-47qg-grp6
* https://github.com/OpenPrinting/cups-filters/security/advisories/GHSA-p9rh-jxmq-gq47

OpenPrinting 现在也已开始发布修复程序：

* CVE-2024-47175：https://github.com/OpenPrinting/libppd/commit/d681747ebf
* CVE-2024-47076：https://github.com/OpenPrinting/libcupsfilters/commit/95576ec3
* CVE-2024-47176 的临时解决方法：https://github.com/OpenPrinting/cups-browsed/commit/1debe6b140c

## 缓解策略

鉴于这些漏洞的严重性，建议立即采取行动：

* **禁用 cups-browsed**：由于 **cups-browsed** 是漏洞利用链的核心，因此禁用它可以阻止潜在的攻击。

  *$ sudo systemctl stop cups-浏览*
* **防止 cups-browsed 在重新启动时启动**：

  *$ sudo systemctl disable cups-浏览*
* **阻止流向 UDP 端口 631 的流量**：如果禁用 **cups-browsed** 不可行，则阻止所有流向 UDP 端口 631 的流量可以减少暴露。
  *$ sudo iptables -A 输入 -p tcp –dport 631 -j DROP*
  *$ sudo iptables -A 输入 -p udp –dport 631 -j DROP*
* **更新 CUPS 组件**：请留意补丁，并在修复程序发布后立即更新 CUPS 和相关组件。

## 检测

要检查您的系统是否易受攻击，请验证 **cups-browsed** 的状态：

*$ sudo systemctl status cups-浏览*

* 如果结果包括 **“Active： inactive （dead）”**，则漏洞利用链已停止，系统不易受到攻击。
* 如果服务处于 **“running”** 或 **“enabled”** 状态，并且 **BrowseRemoteProtocols** 指令在配置文件 */etc/cups/cups-browsed.conf* 中包含值 **“cups”**，则系统容易受到攻击。

## 供应商响应

### 红帽

Red Hat 已确认这些漏洞，并将其严重性影响评为**“重要**”。虽然 Red Hat Enterprise Linux （RHEL） 的所有版本都受到影响，但默认配置并不容易受到攻击。Red Hat 建议管理员禁用 **cups-browsed** 作为缓解措施。他们正在与上游社区和研究人员合作开发补丁。

**Palo Alto 网络**

在最近的更新中，**Palo Alto Networks** 确认其所有产品均未受到这些漏洞的影响，这为他们的安全解决方案的用户提供了一些缓解。

### 规范

Canonical 的安全团队已针对所有支持的 Ubuntu LTS 版本发布了多个 CUPS 软件包的更新，包括 cups-browsed、cups-filters、libcupsfilters 和 libppd。强烈建议升级这些软件包并重新启动 CUPS 守护程序。

```
sudo apt update && sudo apt upgrade
sudo systemctl restart cups.service
```

如果无法做到这一点，则可以将受影响的组件作为目标：

```
sudo apt update && sudo apt install --only-upgrade cups-browsed cups-filters cups-filters-core-drivers libcupsfilters2t64 libppd2 libppd-utils ppdc
sudo systemctl restart cups
```

默认情况下，从 Ubuntu 16.04 LTS 及更高版本开始启用无人值守升级功能。这项服务：

* 每 24 小时自动应用一次新的安全更新
* 如果您启用了此功能，上述补丁将在 24 小时内自动应用
* 但是，我们仍然建议使用 systemctl restart cups.service 重新启动 CUPS 守护程序

### 缓解

* **台式电脑：**删除 cups-browsed 或禁用网络协议会阻碍网络打印机的发现。
* **打印服务器：**禁用网络打印机检测可能是一种临时修复，因为现有打印机仍可访问。但是，在 Ubuntu 上，修改配置文件可能会中断将来的自动更新。除非绝对必要，否则我们建议不要这样做，如果这样做，则应在应用更新后恢复原始配置。

以下缓解步骤将删除打印服务器检测新网络打印机和停止注入恶意 PPD 文件的能力：

1. 编辑 /etc/cups/cups-browsed.conf
2. 搜索 BrowseRemoteProtocols 配置选项
3. 将选项设置为 none （默认值为 “dnssd cups”）
4. 使用 systemctl 重新启动 cups-browsed restart cups-browsed

本文翻译自securityonline [原文链接](https://securityonline.info/critical-cups-vulnerabilities-expose-linux-and-other-systems-to-remote-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300521](/post/id/300521)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-cups-vulnerabilities-expose-linux-and-other-systems-to-remote-attacks/)

如若转载,请注明出处： <https://securityonline.info/critical-cups-vulnerabilities-expose-linux-and-other-systems-to-remote-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

### 热门推荐

文章目录

* [CVE 详情](#h2-0)
* [利用链](#h2-1)
* [影响和受影响的系统](#h2-2)
* [缓解策略](#h2-3)
* [检测](#h2-4)
* [供应商响应](#h2-5)
  + [红帽](#h3-6)
  + [规范](#h3-7)
  + [缓解](#h3-8)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribut...