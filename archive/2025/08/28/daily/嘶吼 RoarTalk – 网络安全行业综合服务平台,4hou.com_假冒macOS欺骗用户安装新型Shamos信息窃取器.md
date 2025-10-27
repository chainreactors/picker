---
title: 假冒macOS欺骗用户安装新型Shamos信息窃取器
url: https://www.4hou.com/posts/7MZA
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-28
fetch_date: 2025-10-07T00:18:12.953973
---

# 假冒macOS欺骗用户安装新型Shamos信息窃取器

假冒macOS欺骗用户安装新型Shamos信息窃取器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 假冒macOS欺骗用户安装新型Shamos信息窃取器

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)53694

收藏

导语：它会在设备上搜索敏感数据，包括加密货币钱包文件、钥匙串数据、苹果备忘录数据以及受害者浏览器中存储的信息。

一款名为“Shamos”的新型信息窃取恶意软件正针对Mac设备发起攻击，它借助“ClickFix攻击”（伪装成故障排除指南及修复方案）实施行动。

该恶意软件是“Atomic macOS Stealer（AMOS，原子 macOS 窃取者）”的变种，由网络犯罪团伙“COOKIE SPIDER”开发，用于窃取存储在网页浏览器、钥匙串项目、苹果备忘录以及加密货币钱包中的数据和凭证。

发现Shamos的CrowdStrike公司报告称，自2025年6月以来，该恶意软件已尝试对其监控的全球超300个环境发起感染。

**借助ClickFix攻击进行传播**

受害者会被恶意广告或伪造的GitHub仓库引诱——这些渠道利用ClickFix攻击，诱导用户在macOS终端中执行shell命令。

威胁者会催促用户运行这些命令以“安装软件”或“修复虚假错误”，但命令一旦执行，实际上会在设备上下载并运行恶意软件。

![github.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250825/1756106605657770.jpg "1756106275155262.jpg")

恶意GitHub存储库

相关广告或伪造页面（如mac-safer[.]com、rescue-mac[.]com）声称能解决用户可能搜索的macOS相关问题，其中包含让用户复制粘贴命令以“修复问题”的指示。

![sponsored.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250825/1756106606104202.jpg "1756106378124856.jpg")

谷歌搜索上的恶意赞助结果

然而，这些命令并不会解决任何问题，反而会解码一个Base64编码的URL，并从远程服务器获取恶意的Bash脚本。

![printer.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250825/1756106606170515.jpg "1756106447533476.jpg")

在macOS上修复打印机问题的错误说明

该脚本会获取用户密码，下载Shamos的mach-O可执行文件，还会利用“xattr”（移除隔离标记）和“chmod”（赋予二进制文件可执行权限）来绕过Gatekeeper，进而准备并执行恶意软件。

**Shamos的数据窃取行为**

Shamos在设备上执行后，会先运行反虚拟机命令，确认自身并非在沙箱中运行，随后通过AppleScript命令进行主机侦察和数据收集。

它会在设备上搜索敏感数据，包括加密货币钱包文件、钥匙串数据、苹果备忘录数据以及受害者浏览器中存储的信息。

收集完所有数据后，它会将这些数据打包成名为“out.zip”的压缩包，再通过curl传输给攻击者。

若该恶意软件以sudo权限运行，还会创建一个Plist文件（com.finder.helper.plist），并将其存储在用户的LaunchDaemons目录中，通过系统启动时自动执行来确保持久化驻留。

CrowdStrike还指出，Shamos能够将额外的载荷下载到受害者的主目录中，且已观察到威胁者投放伪造的Ledger Live钱包应用程序和僵尸网络模块的情况。

**给macOS用户的建议**

建议macOS用户，若不完全清楚命令，切勿在自己的系统上执行。对于GitHub仓库也应如此。该平台上存在众多恶意项目，其目的就是感染毫无防备的用户。

当macOS出现问题时，应避免点击赞助搜索结果，而是到由苹果审核的苹果社区论坛，或通过系统内置的“帮助”功能（按下Cmd + Space，输入“Help”）寻求帮助。

ClickFix攻击已成为一种广泛用于传播恶意软件的策略，威胁者会在TikTok视频中使用该策略，或将其伪装成验证码，亦或是作为“修复”虚假Google Meet错误的方案。

事实证明，这种策略在恶意软件部署方面极为有效，已被用于勒索软件攻击。

文章翻译自：https://www.bleepingcomputer.com/news/security/fake-mac-fixes-trick-users-into-installing-new-shamos-infostealer/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?pT1O5Q50)

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