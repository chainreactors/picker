---
title: 勒索软件团伙使用泄露的勒索软件代码攻击 Windows、Linux 系统
url: https://www.4hou.com/posts/1pG0
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-31
fetch_date: 2025-10-04T11:37:09.493592
---

# 勒索软件团伙使用泄露的勒索软件代码攻击 Windows、Linux 系统

勒索软件团伙使用泄露的勒索软件代码攻击 Windows、Linux 系统 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索软件团伙使用泄露的勒索软件代码攻击 Windows、Linux 系统

walker
[新闻](https://www.4hou.com/category/news)
2023-05-30 11:20:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)98170

收藏

导语：一个新的勒索软件操作名为“Bhuti”,使用 LockBit 和 Babuk 勒索软件家族的泄露代码分别针对 Windows 和 Linux 系统进行攻击。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685094521106139.png "1685093666742655.png")

一个新的勒索软件操作名为“Bhuti”,使用 LockBit 和 Babuk 勒索软件家族的泄露代码分别针对 Windows 和 Linux 系统进行攻击。

虽然 Buhti 背后的威胁行为者（现在被称为“Blacktail”）尚未开发出自己的勒索软件，但他们创建了一个自定义数据渗漏实用程序，用于勒索受害者，这种策略被称为“双重勒索”。

Buhti 于 2023 年 2 月首次被 Palo Alto Networks 的Unit 42 团队发现 ，该团队将其确定为基于 Go 的以 Linux 为目标的勒索软件。

赛门铁克威胁猎手团队今天发布的一份报告显示，Buhti 还针对 Windows，使用代号为“LockBit Black”的略微修改的 LockBit 3.0 变体。

**勒索软件回收**

Blacktail 使用 Windows LockBit 3.0 构建器，一位心怀不满的开发人员 于 2022 年 9 月在 Twitter 上泄露了该架构 。

成功的攻击会将攻陷的电脑的墙纸更改为要求受害者打开勒索信的提示，同时所有加密的文件都会获得“.buthi”的扩展名。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685094523187831.png "1685094051203285.png")

Buhti 赎金记录 （第 42 单元）

针对 Linux 攻击，Blacktail 使用基于一名威胁参与者在 2021 年 9 月在一个俄罗斯黑客论坛上发布的 Babuk 源代码的载荷。

本月早些时候，  SentinelLabs 和 Cisco Talos 强调了使用 Babuk 攻击 Linux 系统的新勒索软件操作案例。

虽然恶意软件重用通常被认为是不那么老练的行为者的标志，但在这种情况下，多个勒索软件团体倾向于使用 Babuk，因为它被证明能够破坏 VMware ESXi 和 Linux 系统，这对网络犯罪分子来说非常有利可图。

**Blacktail 的特征**

Blacktail 不仅仅是一个仅仅对其他人黑客工具进行轻度修改的抄袭者。相反，这个新团伙使用自己的自定义数据泄露工具和独特的网络渗透策略。

赛门铁克报告称，Buhti 攻击利用了 最近披露的 PaperCut NG 和 MF RCE 漏洞，LockBit 和 Clop 团伙也利用了该漏洞。

攻击者依赖 CVE-2023-27350 来在目标计算机上安装 Cobalt Strike、Meterpreter、Sliver、Any Desk 和 ConnectWise，并使用它们来窃取凭证、横向渗透已受感染的网络、窃取文件、发起额外的载荷等。

2 月，该团伙利用了 CVE-2022-47986，这是一个影响 IBM Aspera Faspex 文件交换产品的关键远程代码执行漏洞。

Buhti 的渗透工具是一个基于 Go 的窃取器，可以接收指定文件系统中目标目录的命令行参数。

该工具针对以下文件类型进行盗窃：pdf、php、png、ppt、psd、rar、raw、rtf、sql、svg、swf、tar、txt、wav、wma、wmv、xls、xml、yml、zip、 aiff、aspx、docx、epub、json、mpeg、pptx、xlsx 和 yaml。

这些文件被复制到一个 ZIP 存档中，然后被泄露到 Blacktail 的服务器上。

Blacktail 及其勒索软件操作 Buhti 构成了一个现代示例，展示了如何使用有效的恶意软件工具，轻松地发动攻击，并对组织造成重大损害。

此外，泄露的 LockBit 和 Babuk 源代码可以被现有的勒索软件团伙重新命名，不留任何与之前勒索软件的联系。

卡巴斯基研究员 Marc Rivero 告诉 BleepingComputer，他们目睹了对捷克、中国、英国、埃塞俄比亚、美国、法国、比利时、印度、爱沙尼亚、德国、西班牙和瑞士的攻击。

这意味着 Buthi 已经是一个非常活跃的勒索软件活动，而 Blacktail 仍然是全球组织的重大威胁。

Blacktail 快速利用新披露的漏洞的策略使它们成为一个强大的威胁，需要提高警惕和主动防御策略，如及时修补。

本文翻译自：https://www.bleepingcomputer.com/news/security/new-buhti-ransomware-gang-uses-leaked-windows-linux-encryptors/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?He1pI5wB)

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