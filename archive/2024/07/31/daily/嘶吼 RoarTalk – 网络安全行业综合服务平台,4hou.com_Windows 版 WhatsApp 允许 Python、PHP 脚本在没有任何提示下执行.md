---
title: Windows 版 WhatsApp 允许 Python、PHP 脚本在没有任何提示下执行
url: https://www.4hou.com/posts/xyv9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-31
fetch_date: 2025-10-06T17:41:09.386580
---

# Windows 版 WhatsApp 允许 Python、PHP 脚本在没有任何提示下执行

Windows 版 WhatsApp 允许 Python、PHP 脚本在没有任何提示下执行 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Windows 版 WhatsApp 允许 Python、PHP 脚本在没有任何提示下执行

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-07-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)120036

收藏

导语：如果所有资源都存在，接收者只需单击接收文件上的“打开”按钮，脚本就会执行。

WhatsApp for Windows 最新版本中存在一个安全问题，允许发送 Python 和 PHP 附件，当收件人打开这些附件时，这些附件会在没有任何警告的情况下执行。要成功攻击，需要安装 Python，这一先决条件可能会将目标限制在软件开发人员、研究人员和高级用户。

该问题与 4 月份影响 Windows 版 Telegram 的问题类似，该问题最初被拒绝但后来得到修复，攻击者可以在通过消息传递客户端发送 Python .pyzw 文件时绕过安全警告并执行远程代码执行。

WhatsApp 屏蔽了多种被认为对用户有风险的文件类型，但该公司不打算将 Python 脚本添加到列表中且PHP 文件 (.php) 也不包含在 WhatsApp 的阻止列表中。

**Python、PHP 脚本未被阻止**

安全研究员 Saumyajeet Das 在试验可以附加到 WhatsApp 对话中的文件类型时发现了此漏洞，以查看该应用程序是否允许任何有风险的文件。当发送潜在危险的文件（例如 .EXE）时，WhatsApp 会显示该文件并为收件人提供两个选项：打开或另存为。

![CalcEXE_WhatsApp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240729/1722245834216869.png "1722245621165300.png")

WhatsApp 的可执行文件选项

但是，当尝试打开文件时，WhatsApp for Windows 会生成错误，用户只能选择将文件保存到磁盘并从那里启动它。在测试中，使用 WhatsApp for Windows 客户端时，此行为与 .EXE、.COM、.SCR、.BAT 和 Perl 文件类型一致。Das 发现 WhatsApp 还会阻止 .DLL、.HTA 和 VBS 的执行。

对于所有这些程序，当尝试通过单击“打开”直接从应用程序启动它们时，都会发生错误，只有先保存到磁盘后才能执行它们。

![CalcEXE_WhatsApp_error.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240729/1722245836200887.png "1722245681154687.png")

从 WhatsApp 客户端启动 .EXE 失败

Das 在接受采访时表示，他发现 WhatsApp 客户端不会阻止三种文件类型启动：.PYZ（Python ZIP 应用程序）、.PYZW（PyInstaller 程序）和 .EVTX（Windows 事件日志文件）。

测试证实，WhatsApp 不会阻止 Python 文件的执行，并发现 PHP 脚本也会发生同样的情况。

如果所有资源都存在，接收者只需单击接收文件上的“打开”按钮，脚本就会执行。

Das 于 6 月 3 日向 Meta 报告了该问题，该公司于 7 月 15 日回复称，另一位研究人员已经报告了该问题。目前。该漏洞仍然存在于适用于 Windows 的最新 WhatsApp 版本中，我们可以在 Windows 11 v2.2428.10.0 上对此多加注意。

相关媒体企图联系 WhatsApp，以澄清驳回研究人员报告的原因，一位发言人解释说，他们不认为这是他们的问题，因此没有修复计划。

该公司代表解释说，WhatsApp 有一个系统，当用户收到不在其联系人列表中的用户或电话号码在其他国家/地区注册的用户发送的消息时，会发出警告。然而，如果用户的帐户被劫持，攻击者可以向联系人列表中的每个人发送恶意脚本，这些脚本更容易直接从消息应用程序中执行。

此外，这些类型的附件可能会发布到公共和私人聊天组中，威胁者可能会滥用这些聊天组来传播恶意文件。在回应 WhatsApp 拒绝该报告时，Das 对该项目处理这种情况的方式表示失望。

其实只需将 .pyz 和 .pyzw 扩展名添加到阻止列表中，Meta 便可以阻止通过这些 Pythonic zip 文件进行的潜在攻击。通过解决该问题，WhatsApp 不仅可以增强其用户的安全性，还可以表明他们致力于迅速解决安全问题的良好态度。

有关媒体联系了 WhatsApp，提醒他们 PHP 扩展也没有被阻止，但目前尚未收到其回复。

文章翻译自：https://www.bleepingcomputer.com/news/security/whatsapp-for-windows-lets-python-php-scripts-execute-with-no-warning/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0dkEqwrl)

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