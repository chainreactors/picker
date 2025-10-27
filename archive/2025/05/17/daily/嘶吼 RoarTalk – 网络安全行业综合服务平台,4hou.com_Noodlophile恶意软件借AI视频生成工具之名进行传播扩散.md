---
title: Noodlophile恶意软件借AI视频生成工具之名进行传播扩散
url: https://www.4hou.com/posts/omlB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-17
fetch_date: 2025-10-06T22:26:08.941661
---

# Noodlophile恶意软件借AI视频生成工具之名进行传播扩散

Noodlophile恶意软件借AI视频生成工具之名进行传播扩散 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Noodlophile恶意软件借AI视频生成工具之名进行传播扩散

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-16 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)105138

收藏

导语：防止恶意软件的最好方法是避免从未知网站下载和执行文件。在打开前一定要验证文件扩展名，并在执行前用最新的防病毒工具扫描所有下载的文件。

假冒的人工智能视频生成工具正被用来传播一种新的窃取信息的恶意软件，名为“Noodlophile”，它以生成的媒体内容为幌子。

这些网站使用“Dream Machine”等名字，并在Facebook上的高知名度群组中做广告，冒充先进的人工智能工具，根据上传的用户文件生成视频。

尽管使用人工智能工具来传播恶意软件并不是一个新概念，而且已经被经验丰富的网络犯罪分子所采用，但Morphisec最新活动的发现为这一组合引入了一个新的信息杀手。

根据Morphisec的说法，“Noodlophile”是在暗网论坛上出售的，通常与“Get Cookie + Pass”服务捆绑在一起，所以这是一种新的恶意软件即服务，与讲越南语的运营商有关。

![ad.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250512/1747040455124978.png "1747039872127915.png")

Facebook广告将用户带到恶意网站

**多级感染链**

一旦受害者访问恶意网站并上传他们的文件，他们就会收到一个ZIP档案，其中应该包含人工智能生成的视频。

相反，ZIP包含一个看似可执行文件（Video Dream machinai .mp4.exe），以及一个隐藏文件夹，其中包含后续阶段所需的各种文件。如果Windows用户禁用了文件扩展名（永远不要这样做），那么一眼望去，它看起来就像一个MP4视频文件。

“Video Dream MachineAI.mp4.exe文件是一个32位的c++应用程序，使用通过Winauth创建的证书进行签名，”Morphisec解释说。

尽管它的名字具有误导性（暗示是一个mp4视频），但这个二进制文件实际上是CapCut的改版版本，CapCut是一个合法的视频编辑工具（版本445.0）。这种欺骗性的命名和证书帮助它逃避用户的怀疑和一些安全解决方案。

![site(1).webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250512/1747040456645525.png "1747039963152059.png")

DreamMachine网站放弃了有效载荷

双击假MP4将执行一系列可执行文件，最终启动批处理脚本（Document.docx/install.bat）。

该脚本使用合法的Windows工具“certutil.exe”解码并提取base64编码的密码保护的RAR存档，冒充PDF文档。同时，它还为持久化添加了一个新的Registry键。

接下来，脚本执行‘srchost.exe ’，它运行一个从硬编码的远程服务器地址获取的混淆的Python脚本（randomuser2025.txt），最终在内存中执行noodle lophile Stealer。

如果在受感染的系统上检测到Avast，则使用PE掏空将有效载荷注入RegAsm.exe。否则，将使用shellcode注入在内存中执行。

![VideoDream_AI_Diagram_5.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250512/1747040458300530.png "1747039994150404.png")

完整的执行链

noodle lophile是一种新的信息窃取恶意软件，其目标是存储在web浏览器上的数据，如帐户凭据、会话cookie、令牌和加密货币钱包文件。

Noodlophile代表了恶意软件生态系统的新成员。以前在公共恶意软件跟踪或报告中没有记录，这种窃取程序结合了浏览器凭证盗窃、钱包泄露和可选的远程访问部署。

被窃取的数据是通过电报机器人泄露的，它作为一个秘密的命令和控制（C2）服务器，让攻击者实时访问被盗的信息。

在某些情况下，Noodlophile与XWorm（一种远程访问木马）捆绑在一起，使攻击者能够提升数据窃取能力，远远超出了信息窃取器所提供的被动窃取能力。

防止恶意软件的最好方法是避免从未知网站下载和执行文件。在打开前一定要验证文件扩展名，并在执行前用最新的防病毒工具扫描所有下载的文件。

文章翻译自：https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-drop-new-noodlophile-infostealer-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?tay82fuf)

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