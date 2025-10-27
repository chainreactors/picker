---
title: Python 恶意软件 AndroxGh0st 开始窃取 AWS 密钥
url: https://buaq.net/go-139743.html
source: unSafe.sh - 不安全
date: 2022-12-13
fetch_date: 2025-10-04T01:17:22.237319
---

# Python 恶意软件 AndroxGh0st 开始窃取 AWS 密钥

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

![](https://8aqnet.cdn.bcebos.com/58489bc90c4e5bff5ef6e4f8a8bafaae.jpg)

Python 恶意软件 AndroxGh0st 开始窃取 AWS 密钥

主站 分类 漏洞 工具 极客
*2022-12-12 17:27:17
Author: [www.freebuf.com(查看原文)](/jump-139743.htm)
阅读量:35
收藏*

---

[![freeBuf](https://www.freebuf.com/images/logoMax.png)](https://www.freebuf.com/)

主站

分类

漏洞

工具

极客

Web安全

系统安全

网络安全

无线安全

设备/客户端安全

数据安全

安全管理

企业安全

工控安全

特色

头条

人物志

活动

视频

观点

招聘

报告

资讯

区块链安全

标准与合规

容器安全

公开课

官方公众号企业安全新浪微博

![](https://www.freebuf.com/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](https://www.freebuf.com/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

* [网络安全](https://www.freebuf.com/articles/network)

入侵 AWS 主机的动机有很多，最常见的就是挖矿与垃圾邮件。过去的一年内，Lacework 发现关键事件中有近三分之一都与垃圾邮件和恶意邮件有关。其中，大部分都与一个名为 AndroxGh0st 的 Python 恶意软件有关，背后至少有一个名为 Xcatze 的攻击者。

![image.png-746.9kB](https://image.3001.net/images/20221212/1670837237_6396f3f569b69c2be4bdf.png!small)AndroxGh0st 选项

AndroxGh0st 主要用于从暴露的 .env 文件中扫描并解析 Laravel 应用程序的配置数据。Laravel 是一个常用的开源 PHP 框架，.env 文件通常包括 AWS、SendGrid 和 Twilio 在内的各种配置信息。

AndroxGh0st 具备多种滥用 SMTP 的能力，例如扫描、利用暴露的凭据或 API，甚至是部署 WebShell。特别是对于 AWS，该恶意软件能够扫描并解析 AWS 密钥，也支持暴力破解密钥。

研究人员最近发现了该恶意软件的多个变种。其中一个与硬编码的用户名 ses\_xcatze 有关。在 GitHub 上也能够发现其他版本的 AndroxGhost，分别具备不同的名称与句柄。源码已经很难进行归因了，已经经过许多实体的修改和更新。

![image.png-403.4kB](https://image.3001.net/images/20221212/1670837238_6396f3f69985be831fccf.png!small)AWS 密钥生成

AndroxGh0st 有两个最主要的功能，最常见的是检查环境是否支持发送垃圾邮件。AndroxGh0st 通过调用 GetSendQuota 来实现这一点，但并没有后续操作。

另一个主要的功能就是升级 AWS 管理控制台，步骤如下：

> CreateUser - 尝试创建具有失陷凭据的用户，用户名在恶意软件中硬编码预制
>
> CreateLoginProfile - 为新用户创建登录配置文件以访问管理控制台。密码也在恶意软件中硬编码预制
>
> AttachUserPolicy - 尝试将管理员权限分配给新用户。（arn:aws:iam::aws:policy/AdministratorAccess）
>
> 如果前面的步骤成功，恶意软件会将登录数据写入配置文件供以后使用
>
> DeleteAccessKey - 如果实现管理控制台访问，则删除原始的失陷密钥

![image.png-219.4kB](https://image.3001.net/images/20221212/1670837239_6396f3f7db689bf411715.png!small)功能介绍

![image.png-1060.8kB](https://image.3001.net/images/20221212/1670837240_6396f3f8a4a76999174f9.png!small).env 解析函数

## 在野活动

研究人员发现，在涉及 SMTP 滥用的 AWS 攻击事件中，大约 68% 来自 Windows 系统。从 User-Agent 来看，87% 都为 Python 发起的攻击。

根据 Lacework 的观察，在野攻击活动中以挖矿为目的的 AWS 攻击仅有 20% 来自 Windows 系统、50% 与 Python 有关。

以下是 AWS API 请求中经常发现的 User-Agent：

> Boto3/1.24.13 Python/3.10.5 Windows/10 Botocore/1.27.1

AndroxGh0st 获取凭据的主要方法就是扫描 .env 配置文件。研究人员发现，一周的网络日志中近 40% 都是 .env 的探测流量。这使其他类型的流量都相形见绌，例如 .env 探测流量是 OAST（带外应用程序安全测试）流量的 50 倍以上。

绝大多数（83%）的 .env 扫描都使用单个 User-Agent，这也是恶意软件硬编码的。

![image.png-91.2kB](https://image.3001.net/images/20221212/1670837241_6396f3f9924b84fe0e0eb.png!small)User-Agent 情况

几乎所有与 .env 探测的流量都使用这两个 User-Agent，这意味着该 User-Agent 是与扫描功能相关的，而非与攻击活动相关。

![image.png-354.2kB](https://image.3001.net/images/20221212/1670837242_6396f3fa3602154546adf.png!small)硬编码 User-Agent

扫描活动的另一个指标就是包含字符串 androxgh0st 的 POST 请求。如果恶意软件无法通过 GET 请求获取 .env 文件，那么它也会尝试通过 POST 请求来获取，并使用 androxgh0st 作为 POST 数据的占位符。

## 攻击者 Xcatze

研究人员发现与攻击者 Xcatze 使用的攻击 IP 107.182.128.11 有关的恶意软件。这两个与该 IP 通信的 Windows 恶意软件，都是 RedLine 家族的恶意软件。尽管如此，尚不清楚 Python 恶意软件是否也可以归因于 Xcatze。然而，基于 Windows 的黑客工具的流行，尤其是用于信息窃取和 SMTP 滥用的黑客工具，可能会产生大量源自 Windows 系统的攻击。

## 如何检测

为了识别与 AndroxGhost 功能相似的恶意软件，可以查找以下 API 的异常调用：

> GetSendQuota
>
> CreateUser
>
> CreateLoginProfile
>
> AttachUserPolicy
>
> DeleteAccessKey

## IOC

> 70f35dfd9650437229453570f53969fb1644b1d07f282645c27a3877752a68bd
> f6f240dc2d32bfd83b49025382dc0a1cf86dba587018de4cd96df16197f05d88
> 3b04f3ae4796d77e5a458fe702612228b773bbdefbb64f20d52c574790b5c81a
> 319e572856a098f7beb8a07a4955e2ba823e24e31b84dfdd714bfcd5acf47a28
> 45e051313272899973f16f5e79bf9ebe0a7f303b9dbeca13af9d65b97c59beae
> 94f98c908743b75f578002abe6eae36c36673924f66a5a594b1928e7cc757260
> 61b44259ef97fd64d081f1b95f8cd140c52c73e95dadf62980c4dff78b146e5f
> 107.182.128.11

## 参考来源

> [Lacework](https://www.lacework.com/blog/androxghost-the-python-malware-exploiting-your-aws-keys/)

文章来源: https://www.freebuf.com/articles/network/352251.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)