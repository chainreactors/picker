---
title: NSA敦促组织使用内存安全的编程语言
url: https://www.4hou.com/posts/pVpm
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-17
fetch_date: 2025-10-03T22:58:08.789068
---

# NSA敦促组织使用内存安全的编程语言

NSA敦促组织使用内存安全的编程语言 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# NSA敦促组织使用内存安全的编程语言

布加迪
[新闻](https://www.4hou.com/category/news)
2022-11-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)163509

收藏

导语：由于美国国家安全局信任Rust、C#、 Go、 Java、Ruby和 Swift，C/C++已被嫌弃。

美国国家安全局（NSA）近日发布了指导方针，鼓励众多组织将编程语言从C和C++之类的语言转向内存安全的替代语言，即C#、Rust、Go、Java、Ruby或Swift。

这家政府机构发公告称：“NSA建议各组织尽可能使用内存安全的语言，并通过诸多代码强化防御措施来加强保护，比如编译器选项、工具选项和操作系统配置。”

这家政府机构主要担心的是，不法分子可能会利用内存管理不善的代码中的漏洞，内存管理不善的情况在为程序员提供更多选项和灵活性的语言中较为常见。

NSA举了这样的例子：威胁分子通过缓冲区溢出或利用软件内存分配缺陷来潜入系统。

与此同时，内存安全语言结合使用编译时检查和运行时检查，自动阻止由程序员犯错误引起的漏洞。注意，不是所有的错误，但每一点都有所帮助。比如说，涉及不安全使用内存指针或并发线程之间竞态的错误可以被这些语言发现。

NSA表示，恶意网络威胁分子可以利用这些漏洞实现远程代码执行或造成其他不利影响，这常常会危及设备，成为大规模网络入侵的第一步。

很明显，最好避免遇到这种情况。

NSA网络安全技术总监Neal Ziring表示，在开发软件时，一致地使用内存安全语言及其他保护机制很有必要，以消除此类漏洞。

然而NSA确实认识到，“内存安全”这个名称有点不当，这个概念比较宽泛。

内存安全也有其自身的难题。比如说，额外的内存保护级别可能一开始会减慢开发速度，因为内存不安全的代码不会由特定的工具链构建，不过漏洞数量较少、将来代码的可维护性更强，其回报可以说是值得的。从一种语言转换到另一种语言可能是ASCII的老问题，即使有时可以转换。比如说，虽然Rust功能强大，但学用起来难度相当大。

据调研公司SlashData声称，从2020年第一季度到2022年第一季度，Rust用户的数量增长了两倍。Go也非常受追捧，据统计它拥有330万名开发者组成的社区。JavaScript十年来一直是最受欢迎的语言，拥有1750万名开发者。

虽然这两种语言无处不在，但NSA坚称C和C++特别成问题，这是一种流行的观点。微软的Azure首席技术官Mark Russinovich在9月份亮明了其观点，是时候停止使用这两种经受时间考验的语言编写的任何新项目了。

这位首席技术官确实承认，尽管他会偏向于用Rust编写新工具，但仍然存在“大量的C/ C++，将被维护和完善几十年（更长时间）。”就在他发推文的前一天晚上，Russinovich已经往其85000行Sysinternals添加了C/ C++代码。

网络安全公司Acronis的首席信息安全官（CISO）Kevin Reed在接受IT外媒The Register采访时表示：“我认为NSA的做法是正确的。”

“像地址空间布局随机化（ASLR）和堆栈保护这样的缓解措施是一种权宜之计，而不是全面的解决方案；改用内存安全语言要好得多”，Reed在呼应Russinovich的观点前补充道。

Reed表示，他对立马会看到效果持怀疑态度，因为多年来编写的C和C++代码数量很庞大，即使明天都开始使用Rust和Go，也需要几十年的时间才能收拾好这副烂摊子。

本文翻译自：https://www.theregister.com/2022/11/11/nsa\_urges\_orgs\_to\_use/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KFzUPdI7)

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