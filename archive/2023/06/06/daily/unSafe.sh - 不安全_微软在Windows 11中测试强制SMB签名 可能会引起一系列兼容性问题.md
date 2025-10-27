---
title: 微软在Windows 11中测试强制SMB签名 可能会引起一系列兼容性问题
url: https://buaq.net/go-167376.html
source: unSafe.sh - 不安全
date: 2023-06-06
fetch_date: 2025-10-04T11:46:19.082009
---

# 微软在Windows 11中测试强制SMB签名 可能会引起一系列兼容性问题

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/908724fc1e27d8caf58ea4dbcc4deabc.jpg)

微软在Windows 11中测试强制SMB签名 可能会引起一系列兼容性问题

要说大型企业最关心的问题，那 SMB 共享肯定是其中之一，大部分企业内部都会采用 SMB 来共享某些文件夹，方便公司内部人员访问。所以对 IT 管理员来说，接下来微软强制启用 SMB
*2023-6-5 23:42:40
Author: [www.landiannews.com(查看原文)](/jump-167376.htm)
阅读量:21
收藏*

---

要说大型企业最关心的问题，那 SMB 共享肯定是其中之一，大部分企业内部都会采用 SMB 来共享某些文件夹，方便公司内部人员访问。

所以对 IT 管理员来说，接下来微软强制启用 SMB 签名又要增加工作量了，不过好处是这个真的可以增强安全性。

上周六微软发布 Windows 11 Canary Build 25381 版，在这个版本中微软强制启用了 SMB 签名，Windows XP~8.1、Windows 10、Windows 11、Windows Server 版本都已经支持 SMB 签名，但某些第三方的软件不一定支持。

[![微软在Windows 11中测试强制SMB签名 可能会引起一系列兼容性问题](https://img.lancdn.com/landian/2020/03/71046.png)](https://img.lancdn.com/landian/2020/03/71046.png)

**SMB 签名机制：**

SMB 签名也称为安全签名，这是 SMB 协议中的一种安全机制，每个 SMB 消息都包含使用会话密钥生成的签名，客户端则是将 SMB 块的哈希放在 SMB 标头的签名字段中。

这与 HTTPS 加密有些类似：当 SMB 块在传输中遭到篡改，那么哈希无法匹配，此时 SMB 就知道有人劫持或篡改了数据。

微软推荐的机制是使用 Kerberos 而非 NTLMv2，这可以继续增强安全性，这样也不需要使用 IP 地址连接，也不需要 CNAME 记录。

**强制启用的后果：**

对于所有 Windows 系统而言启用 SMB 签名不会产生兼容性问题，还可以提高安全性，只是企业中通常使用的不只是 Windows 系统和 Windows 服务器，这就会产生问题。

根据微软的说明，如果第三方软件或系统禁用或不支持 SMB 签名，则连接到这些软件、系统、服务器时会报错，常见错误消息包括：

* 0xc000a000
* -1073700864
* STATUS\_INVALID\_SIGNATURE
* The cryptographic signature is invalid.

要解决此问题只能寻求第三方软件、系统开发商的支持，如果只是禁用那还好，启用就行，如果是不支持的话那就歇菜了，尤其是那些仅支持 SMB 3.0 的东东( 3.0 这类老旧版本是不支持签名的，所以无法使用)。

**举个例子：**

群晖 NAS 的 DSM 系统，默认情况下 SMB 是禁用签名的，如果要实现互通访问，则需要在 DSM 控制面板、文件服务、SMB、高级设置、常规，将启用服务器签发改成强制 (如果是域控设备还需要在 LADP 中加入域)。

好消息是目前大多数 SMB 软件、客户端系统、服务器都支持 SMB 签名，唯一要做的就是挨个检查这些东西，把 SMB 签名全部改成启用或强制。

对 IT 管理员来说这不算技术问题，但可能会增加工作量，提前测试的好处就是未来不影响业务系统。至于微软何时在 Windows 10、Windows 11、Windows Server 稳定版通道强制启用 SMB 签名暂时还不清楚。

对了，IT 管理员们还有个工作不要忘记：[微软修复安全启动漏洞导致所有旧版Windows镜像全部作废 请及时更新](https://www.landiannews.com/archives/98730.html)

相关支持文档 1：<https://techcommunity.microsoft.com/t5/storage-at-microsoft/smb-signing-required-by-default-in-windows-insider/ba-p/3831704>

相关支持文档 2：<https://learn.microsoft.com/zh-cn/troubleshoot/windows-server/networking/overview-server-message-block-signing>

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/98997.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/98997.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)