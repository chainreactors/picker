---
title: Windows Quick Assist 在 Black Basta 勒索软件攻击中被滥用
url: https://www.4hou.com/posts/jgyP
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-06-06
fetch_date: 2025-10-06T16:55:19.722698
---

# Windows Quick Assist 在 Black Basta 勒索软件攻击中被滥用

Windows Quick Assist 在 Black Basta 勒索软件攻击中被滥用 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Windows Quick Assist 在 Black Basta 勒索软件攻击中被滥用

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-06-05 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)187867

收藏

导语：截至 2023 年 11 月，Black Basta 已从 90 多名受害者那里收取了至少 1 亿美元的赎金。

网络犯罪分子在社会工程攻击中滥用 Windows Quick Assist 功能，在受害者的网络上部署 Black Basta 勒索软件负载。

微软至少从 2024 年 4 月中旬开始就一直在调查这一活动，他们观察到，威胁组织（追踪为 Storm-1811）在将其地址订阅到各种电子邮件订阅服务后，通过电子邮件轰炸目标开始了攻击。

一旦他们的邮箱充斥着未经请求的消息，威胁分子就会冒充 Microsoft 技术支持人员或受攻击公司的 IT 或服务台工作人员给他们打电话，以帮助修复垃圾邮件问题。

在这次语音网络钓鱼攻击中，攻击者通过启动 Quick Assist 内置远程控制和屏幕共享工具，诱骗受害者授予其 Windows 设备访问权限。

微软表示：“一旦用户允许访问和控制，威胁分子就会运行脚本化的 cURL 命令来下载一系列用于传递恶意负载的批处理文件或 ZIP 文件。”在一些情况下，微软威胁情报发现此类活动会导致下载 Qakbot、ScreenConnect 和 NetSupport Manager 等 RMM 工具以及 Cobalt Strike。

安装恶意工具并结束通话后，Storm-1811 会执行域枚举，在受害者网络中横向移动，并使用 Windows PsExec telnet 替换工具部署 Black Basta 勒索软件。

![Quick_Assist_screen_sharing_prompts.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240516/1715852320113918.jpg "1715852210146933.jpg")

Quick Assist 屏幕共享提示

网络安全公司 Rapid7 也发现了这些攻击，该公司表示，恶意分子将使用“批处理脚本，使用 PowerShell 从命令行获取受害者的凭据”。“凭据是在要求用户登录的‘更新’的虚假上下文下收集的。在大多数观察到的批处理脚本变体中，凭据会通过安全复制命令 (SCP) 立即泄露到威胁行为者的服务器。

为了阻止这些攻击，微软建议网络防御者阻止或卸载不使用的 Quick Assist 和类似的远程监控和管理工具，并培训员工识别技术支持诈骗。

这些攻击的目标仅应允许其他人在联系其 IT 支持人员或 Microsoft 支持人员的情况下连接到其设备，并在怀疑存在恶意意图时立即断开任何快速协助会话。

**Black Basta 勒索软件操作**

两年前，Conti 网络犯罪组织因一系列数据泄露事件而被关闭，此后分裂成多个派系，其中一个就是 Black Basta。

Black Basta 于 2022 年 4 月以勒索软件即服务 (RaaS) 形式浮出水面。此后，其附属公司已经入侵了许多知名受害者，包括德国国防承包商莱茵金属、英国技术外包公司 Capita、现代汽车的欧洲分部、多伦多公共图书馆、美国牙科协会、工业自动化公司和政府承包商 ABB、Sobeys、Knauf 和加拿大黄页。

最近，Black Basta 与美国医疗保健巨头 Ascension 遭受的勒索软件攻击有关，迫使其将救护车转移到未受影响的设施。

正如 CISA 和 FBI 在联合咨询中透露的那样，Black Basta 勒索软件附属机构在 2022 年 4 月至 2024 年 5 月期间侵入了 500 多个组织，加密并窃取了 16 个关键基础设施部门中至少 12 个部门的数据。

Health-ISAC（信息共享和分析中心）也在公告中称，勒索软件团伙“最近加速了针对医疗保健行业的攻击”。

根据网络安全公司 Elliptic 和网络保险公司 Corvus Insurance 的研究显示，截至 2023 年 11 月，Black Basta 已从 90 多名受害者那里收取了至少 1 亿美元的赎金。

文章翻译自：https://www.bleepingcomputer.com/news/security/windows-quick-assist-abused-in-black-basta-ransomware-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?e6Y8cSst)

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