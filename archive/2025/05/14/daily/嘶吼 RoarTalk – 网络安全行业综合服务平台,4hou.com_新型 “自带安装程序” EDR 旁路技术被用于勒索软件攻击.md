---
title: 新型 “自带安装程序” EDR 旁路技术被用于勒索软件攻击
url: https://www.4hou.com/posts/2XN1
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-14
fetch_date: 2025-10-06T22:26:29.867238
---

# 新型 “自带安装程序” EDR 旁路技术被用于勒索软件攻击

新型 “自带安装程序” EDR 旁路技术被用于勒索软件攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型 “自带安装程序” EDR 旁路技术被用于勒索软件攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)62367

收藏

导语：威胁者可以利用新版本或旧版本的代理来进行这种攻击，所以即使最新版本在设备上运行，他们仍然容易受到攻击。

一种新的“自带安装程序”EDR 旁路技术在攻击中被利用，以绕过 SentinelOne 的防篡改保护功能，使恶意分子能够禁用端点检测和响应（EDR）代理，从而安装 Babuk 勒索软件。

这种技术利用了代理升级过程中的一个漏洞，使威胁者能够终止正在运行的 EDR 代理，从而使设备失去保护。

此次攻击是由 Stroz Friedberg事件响应团队的人员在与今年早些时候遭受勒索软件攻击的一位客户合作期间发现的。

该技术并非像我们通常看到的 EDR 旁路那样依赖第三方工具或驱动程序，而是滥用 SentinelOne 安装程序本身。

SentinelOne 建议客户启用默认关闭的“在线授权”设置，以防范此类攻击。

**在勒索软件攻击中被积极利用**

Stroz Friedberg的研究人员解释说，SentinelOne 通过一项防篡改保护功能来保护其 EDR 代理，该功能要求在 SentinelOne 管理控制台中进行手动操作或输入唯一代码才能移除代理。

然而，与许多其他软件安装程序一样，在安装不同版本的代理程序时，SentinelOne 安装程序会在现有文件被新版本覆盖之前终止任何相关的 Windows 进程。

威胁者发现他们可以利用这一短暂的机会窗口，运行一个合法的 SentinelOne 安装程序，然后在安装程序关闭正在运行的代理服务后强行终止安装过程，从而使设备处于未受保护的状态。

![Bring-Your-Own-Installer-EDR-Bypass-attack-flow.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250506/1746516384180859.png "1746515952933668.png")

自带安装器EDR绕过攻击链

今年早些时候，Stroz Friedberg被委托调查对客户网络的攻击，日志显示攻击者通过漏洞获得了对客户网络的管理访问权限。

然后，攻击者通过在SentinelOne Windows Installer（“msiexec.exe”）进程安装和启动新版本的代理程序之前终止该进程，使用了这种新的绕过。由于设备上的保护被禁用，威胁者随后能够部署勒索软件。

威胁者可以利用新版本或旧版本的代理来进行这种攻击，所以即使最新版本在设备上运行，他们仍然容易受到攻击。

Stroz Friedberg在报告中说：“Stroz Friedberg还观察到，在安装程序终止后不久，SentinelOne管理控制台的主机就离线了。进一步的测试表明，攻击成功地跨越了多个版本的SentinelOne代理，并且不依赖于本次事件中观察到的特定版本。”

SentinelOne已于2025年1月私下与客户分享了缓解措施。缓解措施是在哨兵策略设置中启用“在线授权”功能，启用该功能时，需要在发生代理的本地升级、降级或卸载之前获得SentinelOne管理控制台的批准。

SentinelOne还与所有其他主要的EDR供应商分享了Stroz Friedberg关于这项新技术的建议，以防他们也受到影响。经证实，这次攻击并未影响其EDR软件。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-bring-your-own-installer-edr-bypass-used-in-ransomware-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?S2rX5av0)

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