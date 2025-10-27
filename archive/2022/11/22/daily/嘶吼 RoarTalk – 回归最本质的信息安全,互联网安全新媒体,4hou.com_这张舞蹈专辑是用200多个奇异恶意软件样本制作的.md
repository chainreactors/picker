---
title: 这张舞蹈专辑是用200多个奇异恶意软件样本制作的
url: https://www.4hou.com/posts/kMnK
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-22
fetch_date: 2025-10-03T23:22:21.815483
---

# 这张舞蹈专辑是用200多个奇异恶意软件样本制作的

这张舞蹈专辑是用200多个奇异恶意软件样本制作的 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 这张舞蹈专辑是用200多个奇异恶意软件样本制作的

布加迪
[新闻](https://www.4hou.com/category/news)
2022-11-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)149474

收藏

导语：Greg Linares新的电子舞曲（EDM）专辑《VX》是用恶意软件制作的，一点也不夸张。

![0.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221121/1668983544196360.jpeg "1668983490170076.jpeg")

Greg Linares新的电子舞曲（EDM）专辑《VX》是用恶意软件制作的，一点也不夸张。

早在20世纪90年代末，Linares的两项爱好就是制作电子音乐和编写电脑病毒。

他现在是一家投资公司网络安全部门的白帽黑客，不过仍在继续制作音乐，只不过其方式很特别：从恶意软件和代码中提取数据，以便做成声音，然后将声音组装到舞曲中。

Linares近日发布了采用开源许可证（CC BY-SA）的专辑，供人下载。专辑含有用200多个恶意软件样本制作而成的多首歌曲，包括从90年代末的流行恶意软件到REvil和Stuxnet之类的恶意软件。

他告诉外媒，这张专辑使用了代码、图像、网络流量和恶意软件的熵值来组成专辑的声音、音符模式和音效——这位单身父亲称该专辑是向其老本行和所有在90年代从事病毒编写工作这门“黑艺术”的病毒开发者致敬。

为了了解更多信息，外媒采访了Linares。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221121/1668983544913253.jpeg "1668983504113323.jpeg")

图1. Greg Linares，又名Laughing Mantis

**用恶意软件制作音乐的想法从何而来？**

Linares：大概七年前，我在逆向工程分析一个名为Careto的恶意软件时，注意到汇编代码MOV值看起来与DAW（数字音频工作站）步进音序器中的节拍排列很相似，于是萌生了跨界捣鼓的念头。

作为一名兴趣广泛的极客，我决定将每个汇编代码命令映射到一个鼓通道，并基于从我拥有的Careto恶意软件样本中分解出来的内容制作音符模式。幸运的是，它实际上是相当稳定的4/4电子舞曲节拍。

**这项工作有多难/你用了什么工具？**

Linares：极其困难，可能是迄今为止最低效的音乐制作方式。这就好比使用那些由文本生成图像的AI工具，但只能在提示符处输入一个单词，而接下来的三个单词由喝醉的猴子随机输入。用这种方法制作歌曲，你完全受数据的支配，然而你映射数据是为了制作“音乐”。说实话，大多数时候当我做这样的音乐时，感觉更像模糊测试软件以查找漏洞，而不是制作传统音乐。

从最初的原始方法开始，我改进了许多不同的方法从恶意软件和代码中提取数据，以便制作声音。第一种方法我称之为x86转码，通常只适用于节奏和鼓点。然后我尝试将代码、推文和恶意软件中的字符串字母转换成莫尔斯电码值，然后使用点和破折号本身作为发送到音符的信号。这会生成大量的节奏模式，甚至是最新专辑中的一些旋律。

我使用的另一种方法是将恶意软件的熵值作为音频波形，用于一种名为波表合成的合成技术。基本上，通过映射恶意软件代码部分的随机性值，然后利用这些值绘制声音波形，我就能够使用数据从一个恶意软件中实际生成声音。就这个项目而言，使用Novation Nova的波表绘制、Waldorf Kyra波表合成器和Iridium的引擎是制作专辑中大多数声音的关键。

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221121/1668983544752569.jpeg "1668983515604725.jpeg")

图2. 用于针对SolarWinds的恶意软件中经过改装的恶意软件表示为波形。

**我们在这张专辑中听到的是什么恶意软件？**

Linares：《VX》专辑中有200多个恶意软件样本，用于制作合成器声音、鼓点、音效、琶音和LFO调制。这张专辑的一些亮点是来自90年代病毒编写组织29A、NuKE、SLAM、No Mercy、Team Necrosis和Metaphase的罕见恶意软件。

还有来自REvil、Conti和Lapsus$的现代勒索软件和恶意软件工具样本。其中一个音轨是完全由2000年代早期的远程访问木马程序（比如NetBUS、Sub7和Back Orifice 2k）制作的。这张专辑的第二部分将在圣诞节前后发布，会含有几个颇有意思的昔日恶意软件，比如Solar Winds、Duqu和Disk Wiper。

**完成和打磨专辑的难度有多大？**

Linares：你不知道我为了制作这张专辑，DAW崩溃了多少次。回头查看我的错误日志文件夹，发现自开始制作这张专辑以来遇到了483次崩溃。这相当于损失了三首音轨和好多小时的制作时间。由于渲染和音乐开发变得很不稳定，专辑不得不一分为二。我要用接下来的几周时间重建我的系统，为我开发的几个工具重新编程。说到打磨，这次我可是施展了浑身的技术才华。

**专辑标题“VX”指的是什么？**

Linares：其全称是“病毒交流”，是指20世纪90年代的电脑病毒编写场景。

**为什么要开源它？**

Linares：说实话，我的梦想之一就是把我的音乐放在视频游戏中，游戏音轨以及The Prodigy、Juno Reactor、 Velvet Acid Christ、Numb和Frontline Assembly等乐队是我在90年代制作音乐的最大灵感来源。我确实设法让我的音乐出现在了《黑客帝国》续集以及《黑客帝国》大型多人在线角色扮演游戏（MMORPG）的一部预告片中。原本最有机会出现在真正的视频游戏中是被第三方雇佣去帮助制作《星际争霸：幽灵》声音和音乐，结果在干了两周后被解雇了。通过开源我的音乐、以便免费用于所有地方，我真的希望流媒体网站、游戏工作室及其他艺术家可以在他们的内容中使用我的音乐。这听起来比再度成为签约音乐人好得多。

可以在此处从BandCamp下载《VX》：https://laughingmantis.bandcamp.com/album/vx-part-1

本文翻译自：https://thestack.technology/this-album-was-made-with-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?H41TstEQ)

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