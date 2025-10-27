---
title: 亚马逊查获使用恶意远程桌面操作以窃取数据的域名
url: https://www.4hou.com/posts/KGAz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-08
fetch_date: 2025-10-06T19:16:39.348668
---

# 亚马逊查获使用恶意远程桌面操作以窃取数据的域名

亚马逊查获使用恶意远程桌面操作以窃取数据的域名 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 亚马逊查获使用恶意远程桌面操作以窃取数据的域名

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-11-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)92498

收藏

导语：亚马逊指出，在这次特定的活动中，APT29 遵循其典型的“窄目标”策略的相反方法，向比平常更多的目标发送了网络钓鱼电子邮件。

据悉，亚马逊已查获了俄罗斯 APT29 黑客组织用于针对政府和军事组织进行针对性攻击的域名，以使用恶意远程桌面操作连接文件窃取 Windows 凭据和数据。

APT29，也被称为“舒适熊”和“午夜暴雪”，是一个由俄罗斯国家支持的网络间谍组织，与俄罗斯对外情报局 (SVR) 有联系。亚马逊澄清说，尽管 APT29 使用的网络钓鱼页面被伪装成 AWS 域，但亚马逊或其云平台的凭证都不是这些攻击的直接目标。

其公告中写道：“他们使用的一些域名试图欺骗目标，让人们相信这些域是 AWS 域（但事实并非如此），但亚马逊不是目标，该组织也不是目标 AWS 客户凭证。相反，APT29 通过 Microsoft 远程桌面寻找目标的 Windows 凭据。”

威胁者以针对全球政府、智库和研究机构的高度复杂的攻击而闻名，通常使用网络钓鱼和恶意软件来窃取敏感信息。

**全球范围内的目标组织**

尽管 APT29 最近的活动在乌克兰产生了重大影响，但其范围很广泛，并针对多个被视为俄罗斯对手的国家。

亚马逊指出，在这次特定的活动中，APT29 遵循其典型的“窄目标”策略的相反方法，向比平常更多的目标发送了网络钓鱼电子邮件。乌克兰计算机紧急响应小组 (CERT-UA) 发布了有关这些“流氓 RDP”附件的公告，以警告他们在“UAC-0215”下跟踪的大规模电子邮件活动。

这些消息的主题是解决亚马逊和微软服务的“集成”问题以及实施“零信任”网络安全架构（零信任架构，ZTA）。

这些电子邮件包含 RDP（远程桌面协议）连接文件，其名称如“零信任安全环境合规性检查.rdp”，打开时会自动启动与恶意服务器的连接。

![malicious-rdp-attachment.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241107/1730948556129557.png "1730084850601911.png")

恶意 RDP 配置屏幕

从上面这些 RDP 连接配置文件之一的图像可以看出，它们与攻击者控制的 RDP 服务器共享所有本地资源，包括：

**·**本地磁盘和文件

**·**网络资源

**·**打印机

**·**COM 端口

**·**音频设备

**·**剪贴板

此外，UA-CERT 表示，它们还可以用于在受感染的设备上执行未经授权的程序或脚本。

![files.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241107/1730948557490418.png "1730084933170046.png")

共享驱动器和设备被重定向到攻击者的 RDP 服务器

虽然亚马逊表示，该活动用于窃取 Windows 凭据，但由于目标的本地资源与攻击者的 RDP 服务器共享，因此威胁者也可以直接从共享设备窃取数据。

这包括存储在目标硬盘、Windows 剪贴板和映射网络共享上的所有数据。 CERT-UA 建议应仔细检查其公告 IoC 部分中共享的 IP 地址的网络交互日志，以检测可能的攻击或违规迹象。此外，建议采取以下措施来减少攻击面：

1.在邮件网关处阻止“.rdp”文件。

2.防止用户在不需要时启动任何“.rdp”文件。

3.配置防火墙设置以限制从 mstsc.exe 程序到外部网络资源的 RDP 连接。

4.配置组策略以通过 RDP 禁用资源重定向（“远程桌面服务”->“远程桌面会话主机”->“设备和资源重定向”->“不允许...”）。

目前，APT29 仍然是俄罗斯最强大的网络威胁之一，善于使用间谍软件供应商独有的漏洞。据透露，去年威胁者攻击了 TeamViewer、Microsoft 和 Hewlett Packard Enterprise 等重要软件供应商。

本月早些时候，APT29“集体”就利用 Zimbra 和 JetBrains TeamCity 服务器漏洞破坏全球重要组织。

文章翻译自：https://www.bleepingcomputer.com/news/security/amazon-seizes-domains-used-in-rogue-remote-desktop-campaign-to-steal-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?eKQI1zVj)

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