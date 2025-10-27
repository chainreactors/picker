---
title: 新的 Bandit 恶意软件攻击浏览器，窃取个人和财务登录信息
url: https://www.4hou.com/posts/po2m
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-06
fetch_date: 2025-10-04T11:44:49.519227
---

# 新的 Bandit 恶意软件攻击浏览器，窃取个人和财务登录信息

新的 Bandit 恶意软件攻击浏览器，窃取个人和财务登录信息 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 Bandit 恶意软件攻击浏览器，窃取个人和财务登录信息

walker
[新闻](https://www.4hou.com/category/news)
2023-06-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)132713

收藏

导语：Bandit Stealer 是趋势科技最近发现的一种信息窃取程序，它有效地针对加密货币钱包和网络浏览器，同时巧妙地避免检测。

![New Bandit Malware Attacks Browsers to Steal Personal & Financial Logins.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685693908139059.jpeg "1685693105195409.jpeg")

Bandit Stealer 是趋势科技最近发现的一种信息窃取程序，它有效地针对加密货币钱包和网络浏览器，同时巧妙地避免检测。

该恶意软件优先将 Windows 作为其目标，并利用合法的命令行工具runas[.]exe 在不同的用户权限下执行程序。

目的是提升权限、获得管理访问权限并绕过安全措施以有效收集大量用户数据。

**逃避杀毒软件**

由于使用 Go 编程语言，该恶意软件具有跨平台兼容性，使其能够将影响扩展到各种平台。

Bandit Stealer 采用沙盒检测机制来调整其行为并根据其检查的特定指标逃避检测或分析：

container

jail

KVM

QEMU

sandbox

Virtual Machine

VirtualBox

VMware

Xen

在恶意软件中包含特定于 Linux 的命令表明它可能旨在感染Linux 机器并且可能正在接受测试，因为在 Windows 系统上访问“/proc/self/status”文件路径会导致错误。

恶意软件从 AppData 文件夹中的 Pastebin 链接 (hxxps[:]//pastebin[.]com/raw/3fS0MSjN) 检索内容并将其保存为名为“blacklist.txt”的文件。

在下面，我们提到了此列表包含的所有详细信息：

硬件 ID

IP地址

MAC地址

用户名

主机名

进程名称

所有这些细节主要的目的是确定恶意软件是在沙盒中运行还是在接受测试。

**恶意软件的传播**

恶意软件通过钓鱼邮件传播，将自己伪装成无害的 MS Word 附件，在后台启动感染过程，从而分散用户的注意力。

微软的访问控制机制将以管理员身份运行恶意软件，当用户缺乏执行程序所需的足够权限时，该机制非常有用。

恶意软件修改了 Windows 注册表，并持续收集从加密货币钱包和浏览器中提取的个人和财务数据。

![image-134-1024x752.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685693910550408.png "1685693501212797.png")

Bandit Stealer 窃取Telegram会话以进行未经授权的访问，从而实现冒充和恶意行为，例如访问私人消息和数据。

**扫描浏览器和钱包**

以下是我们提到的浏览器：

7Star

YandexBrowser

Brave-Browser

Amigo

Torch

Google Chrome Canary

Google Chrome

Cent Browser

Sputnik

Iridium

Orbitum

UCozMedia

Epic Privacy Browser

Microsoft Edge

Kometa

以下是被扫描的所有钱包：

Clover Wallet

Jaxx Liberty

Wombat

TronLink

Trust Wallet

Crypto.com

BitKeep: Crypto & NFT Wallet

以下是我们从受害者的浏览器中窃取的数据类型：

Login data

Cookies

Web history

Credit card details

研究人员发现了一个伪造的 Heart Sender安装程序，它可以诱骗用户启动嵌入式恶意软件、自动发送垃圾短信和电子邮件。

从 Bandit Stealer 和类似窃取者窃取的信息使攻击者能够从事身份盗窃、数据泄露、经济利益、帐户劫持、凭据填充、出售给其他网络犯罪分子，以及进行双重勒索和勒索软件等后续攻击。

本文翻译自：https://gbhackers.com/bandit-malware-attacks-browsers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0nVEvv1h)

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

![](https://img.4hou.com/images/u=2076373339,2173673275&fm=26&gp=0.jpg)

# [walker](https://www.4hou.com/member/xyv9)

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

[查看更多](https://www.4hou.com/member/xyv9)

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