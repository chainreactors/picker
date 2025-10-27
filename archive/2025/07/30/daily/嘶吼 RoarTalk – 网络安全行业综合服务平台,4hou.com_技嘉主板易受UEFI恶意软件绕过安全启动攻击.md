---
title: 技嘉主板易受UEFI恶意软件绕过安全启动攻击
url: https://www.4hou.com/posts/OGjp
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-30
fetch_date: 2025-10-06T23:26:31.173512
---

# 技嘉主板易受UEFI恶意软件绕过安全启动攻击

技嘉主板易受UEFI恶意软件绕过安全启动攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 技嘉主板易受UEFI恶意软件绕过安全启动攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-07-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)78604

收藏

导语：使用技嘉主板的来自不同OEM的计算机可能面临攻击风险，因此建议用户关注固件更新并及时应用它们。

最新发现，数十款技嘉主板型号运行在易受安全问题影响的UEFI固件上，这些安全问题允许植入对操作系统不可见的引导恶意软件，该恶意软件可在重新安装系统后仍然存在。

这些漏洞可能允许具有本地或远程管理员权限的攻击者在系统管理模式（SMM）中执行任意代码，SMM 是一个与操作系统（OS）隔离的环境，并且在机器上具有更多权限。

在操作系统以下运行的机制具有低级硬件访问权限，并在系统启动时初始化。因此，这些环境中的恶意软件可以绕过系统上的传统安全防御。

UEFI，或统一可扩展固件接口，由于具有安全启动功能，固件更加安全，该功能通过加密验证确保设备在启动时使用的是安全和受信任的代码。

因此，像引导程序（BlackLotus、CosmicStrand、MosaicAggressor、MoonBounce、LoJax）这样的EFI级恶意软件可以在每次启动时部署恶意代码。

**大量主板受到影响**

这四个漏洞是由固件安全公司Binarly的研究人员发现的，他们与卡内基梅隆大学的CERT协调中心（CERT/CC）分享了他们的发现。

最初的固件供应商是American megtrends Inc. (AMI)，该公司在披露后解决了这些问题，但一些OEM固件版本（例如技嘉）当时没有实现修复。

在技嘉固件的实现中，Binarly发现了以下漏洞，所有漏洞的严重性评分都为8.2：

**·**CVE-2025-7029: SMI 处理程序（OverClockSmiHandler）中的错误可能导致 SMM 权限提升。

**·**CVE-2025-7028: SMI处理程序（SmiFlash）中的错误，允许对系统管理RAM （SMRAM）进行读/写访问，这可能导致恶意软件安装。

**·**CVE-2025-7027：可以导致SMM权限升级，并通过向SMRAM写入任意内容来修改固件。

**·**CVE-2025-7026：允许任意写入SMRAM，并可能导致特权升级到SMM和持久固件危害。

根据统计，有超过240个主板型号受到影响——包括修订，变体和特定地区的版本，固件在2023年底到2024年8月中旬之间更新。其中，一位公司代表表示“超过100条产品线受到影响。”

其他企业设备供应商的产品也受到这四个漏洞的影响，但它们的名称在修复程序可用之前不会公开。

据CERT/CC称，Binarly研究人员于4月15日通知卡内基梅隆CERT/CC有关这些问题，技嘉于6月12日确认了这些漏洞，随后发布了固件更新。但是，OEM还没有发布关于Binarly报告的安全问题的安全公告。

与此同时，Binarly的创始人兼首席执行官Alex Matrosov表示，技嘉很可能还没有发布修复程序。由于许多产品的使用寿命已经结束，用户可能不会收到任何安全更新。

“因为这四个漏洞都来自AMI的参考代码，AMI在前一段时间才在保密协议下向付费客户披露了这些漏洞，这对下游供应商造成了多年的重大影响，因为这些漏洞一直处于脆弱状态，而且没有打补丁。”

虽然普通消费者的风险很低，而那些在关键环境中的人可以使用Binarly的risk Hunt扫描工具来评估特定的风险，该工具包括对这四个漏洞的免费检测。

使用技嘉主板的来自不同OEM的计算机可能面临攻击风险，因此建议用户关注固件更新并及时应用它们。

文章翻译自：https://www.bleepingcomputer.com/news/security/gigabyte-motherboards-vulnerable-to-uefi-malware-bypassing-secure-boot/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?dx48wf7z)

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