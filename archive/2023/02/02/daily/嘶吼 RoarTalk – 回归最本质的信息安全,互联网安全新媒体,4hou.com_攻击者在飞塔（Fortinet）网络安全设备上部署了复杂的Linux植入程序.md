---
title: 攻击者在飞塔（Fortinet）网络安全设备上部署了复杂的Linux植入程序
url: https://www.4hou.com/posts/gXmG
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-02
fetch_date: 2025-10-04T05:27:09.525088
---

# 攻击者在飞塔（Fortinet）网络安全设备上部署了复杂的Linux植入程序

攻击者在飞塔（Fortinet）网络安全设备上部署了复杂的Linux植入程序 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者在飞塔（Fortinet）网络安全设备上部署了复杂的Linux植入程序

布加迪
[新闻](https://www.4hou.com/category/news)
2023-02-01 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)161045

收藏

导语：该漏洞让攻击者可以在未经身份验证的情况下远程执行任意代码和命令。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230201/1675219248183780.png "1673657739126026.png")

去年12月知名网络安全厂商飞塔（Fortinet）披露，其FortiOS操作系统中的一个严重漏洞正在被外面的攻击者大肆利用。本周，该公司在进一步分析后公布了有关那些攻击者通过这个漏洞植入复杂恶意软件的更多细节。

从现有信息来看，最初的零日攻击具有很强的针对性，主要攻击与政府相关的实体。然而，由于该漏洞被公之于众已过去一个多月，所有客户都应该尽快打上补丁，因为更多的攻击者可能会开始利用它。

**FortiOS SSL-VPN曝出远程代码执行漏洞**

该漏洞被编号为CVE-2022-42475，存在于FortiOS的SSL-VPN功能中，可以被远程攻击者在无需验证身份的情况下利用。一旦攻击者成功利用了漏洞，随后就可以执行任意代码和命令。

飞塔按照CVSS评级将该漏洞评定为9.3（严重漏洞），并发布了FortiOS、FortiOS- 6k7K和FortiProxy（这家公司的安全Web网关产品）这几大产品系列的更新版。FortiOS运行在该公司的FortiGate网络安全防火墙及其他设备上。

对于无法立即部署更新版的客户来说，一个变通办法是完全禁用SSL-VPN，这对于依赖这项功能来支持远程或混合工作环境的组织来说可能有难度。飞塔还发布了用于检测企图利用漏洞的IPS（入侵防御系统）特征码，并发布了检测其反病毒引擎中已知植入程序的规则。

客户们还可以在其日志中搜索可能表明攻击者企图利用漏洞的以下条目：

Logdesc="Application crashed" and msg="[...]

application:sslvpnd,[...], Signal 11 received, Backtrace:

[...]”

**植入程序作为FortiOS IPS引擎的木马版本隐藏起来**

攻击者在飞塔分析的攻击（https://www.fortinet.com/blog/psirt-blogs/analysis-of-fg-ir-22-398-fortios-heap-based-buffer-overflow-in-sslvpnd）中成功利用了这个漏洞，并将FortiOS IPS引擎的木马版本复制到文件系统中。这表明攻击者的手法非常老练，能够利用逆向工程处理自定义的FortiOS组件。

IPS引擎的这个非法版本作为data/lib/libips.bak保存在文件系统上，它是合法文件/data/lib/libips.bak的拷贝，但已作了恶意修改。也就是说，非法版本导出了名为ips\_so\_patch\_urldb和ips\_so\_query\_interface的两个合法函数（它们通常是合法libips的一部分），但是劫持它们来执行存储在其他恶意组件中的代码。

飞塔的分析师表示，如果libps.bak命名为data/lib目录中的libips.so，恶意代码将自动执行，因为FortiOS的组件会调用这些导出的函数。二进制文件不会试图返回到干净的IPS引擎代码，因此IPS功能也受到了影响。

换句话说，一旦恶意版本被执行，合法的IPS功能就再也无法正常工作。被劫持的函数执行恶意代码，然后恶意代码对名为libiptcp.so、libgif.so、.sslvpnconfigbk和libipudp.so的多个文件执行读写操作。

分析师无法从他们分析的受攻击设备中恢复所有这些文件，因此不知道完整的攻击链。然而，他们确实发现了一个名为wxd.conf的文件，其内容类似开源反向代理的配置文件，开源逆向代理可用于将网络地址转换（NAT）后面的系统暴露在互联网面前。

分析师分析从受攻击设备捕获的网络数据包后发现，恶意软件连接上两台由外部攻击者控制的服务器，以下载有待执行的额外攻击载荷和命令。其中一台服务器仍在运行中，它有一个文件夹，其中含有专门为不同版本的FortiGate硬件构建的二进制文件。这让研究人员得以分析他们认为攻击者在系统上执行以操纵FortiOS中日志功能的的其他文件。

据研究人员声称：

恶意软件对FortiOS的日志记录进程稍加改动，以操纵日志从而逃避检测。–/bin/miglogd & /bin/syslogd

它包括27款FortiGate型号和版本的偏移位和操作码。恶意软件打开进程的句柄，将数据注入其中。

版本从6.0.5到7.2.1。

型号有FG100F、FG101F、FG200D、FG200E、FG201F、FG240D、FG3H0E、FG5H0E、FG6H1E、FG800D、FGT5HD、FGT60F和FGT80F。

恶意软件可以操纵日志文件。它查找elog文件，即FortiOS中的事件日志。在内存中解压这类文件后，它搜索攻击者指定的字符串，删除它，然后重建日志。

恶意软件还可以终止日志记录进程。

研究人员还在VirusTotal在线扫描器上发现了一个Windows二进制文件的样本，其代码与在FortiOS上发现的Linux二进制文件代码相似。Windows样本是在属于UTC+8时区的一台机器上编译而成的，该时区覆盖澳大利亚、中国、俄罗斯、新加坡及其他东亚国家。攻击者使用的自签名证书也是在协调世界时（UTC）早上3点到8点之间创建的。研究人员表示，鉴于黑客不一定在办公时间活动，他们常常在受害者的办公时间活动，以帮助使用一般的网络流量来混淆其活动以免被检测出来，因此很难从中得出任何结论。

飞塔的安全公告附有许多妥协指标（IoC），包括文件路径、文件散列、IP地址，甚至用于检测网络数据包捕获内容中的这个植入程序恶意通信的特征码。

本文翻译自：https://www.csoonline.com/article/3685670/attackers-deploy-sophisticated-linux-implant-on-fortinet-network-security-devices.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?tUO1qSrm)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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