---
title: DoubleFinger通过加载GreetingGhoul窃取加密货币
url: https://www.4hou.com/posts/WKwn
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-23
fetch_date: 2025-10-04T11:46:27.773605
---

# DoubleFinger通过加载GreetingGhoul窃取加密货币

DoubleFinger通过加载GreetingGhoul窃取加密货币 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# DoubleFinger通过加载GreetingGhoul窃取加密货币

xiaohui
[新闻](https://www.4hou.com/category/news)
2023-06-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)172823

收藏

导语：当受害者打开电子邮件中的恶意PIF附件，最终执行DoubleFinger的第一个加载器阶段时，DoubleFinger会部署在目标计算机上。

![sl-hand-two-fingers-up-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230614/1686733939190174.jpg "1686733939190174.jpg")

窃取加密货币并不是什么新鲜事。例如，早在2010年代初，Mt.Gox交易所就被盗窃了许多比特币，Coinvault勒索软件背后的组织也一直在针对比特币钱包发起攻击。应该是从那时起，窃取加密货币业务就成了攻击者不可或缺的业务。就在前几天，6 月 3 日，Atomic Wallet 发推称接到用户钱包被黑的报告，并已着手调查。6 月 4 日，Atomic Wallet 发推称已联合第三方安全公司对钱包被黑事件进行调查，并阻止了在加密货币交易所交易的被窃加密货币。目前，Atomic Wallet 已下线了其下载服务器—— get.atomicwallet.io。初步统计，有价值超过 3500 万美元的加密货币被窃取。

根据卡巴斯基实验室研究人员的调查，最近出现了一个多级DoubleFinger加载器，它会传播加密货币窃取程序。当受害者打开电子邮件中的恶意PIF附件，最终执行DoubleFinger的第一个加载器阶段时，DoubleFinger会部署在目标计算机上。

**阶段1**

第一阶段是修改后的“espexe.exe”（MS Windows经济服务提供商应用程序）二进制文件，其中对DialogFunc进行了修复，从而执行恶意shellcode。通过哈希解析添加到DialogFunc中的API函数后，shellcode从Imgur.com下载PNG图像。接下来，shellcode在下载的图像中搜索魔术字节(0xea79a5c6)，在图像中定位加密的有效负载。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230614/1686733951412830.png "1686733951412830.png")

Real DialogFunc函数（左）和带有shellcode的修复函数（右）

加密的有效负载包括：

具有第四级有效负载的PNG;

加密的数据blob；

合法的java.exe二进制文件，用于DLL侧加载；

DoubleFinger第二阶段加载器。

**阶段2**

第二阶段的shellcode是通过执行与第二阶段加载器shellcode（文件名为msvcr100.dll）位于同一目录中的合法Java二进制文件来加载的。与第一阶段一样，该文件是一个合法的修复二进制文件，具有与第一阶段类似的结构和功能。

毫无疑问，shellcode会加载、解密并执行第三阶段的shellcode。

**阶段3**

第三阶段shellcode与第一阶段和第二阶段有很大不同。例如，它使用低级Windows API调用，并在进程内存中加载和映射ntdll.dll，以绕过安全解决方案设置的挂钩。

下一步是解密并执行位于上述PNG文件中的第四阶段有效负载。与下载的PNG文件不显示有效图像不同，此PNG文件显示有效图像。然而，所使用的隐写术方法相当简单，因为数据是从特定的偏移量中检索的。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230614/1686733959498278.png "1686733959498278.png")

带有嵌入式第四阶段的aa.png文件

**阶段4**

第四阶段的shellcode相当简单，它在自身内部定位第五阶段，然后使用Process Doppelgänging技术执行该阶段。Process Doppelgänging与Process Hollowing技术类似,不同之处在于前者通过攻击Windows NTFS运作机制和一个来自Windows进程载入器中的过时的应用。

**阶段5**

第五阶段创建一个计划任务，每天在特定时间执行GreetingGhoul 窃取程序。然后，它下载另一个PNG文件（实际上是加密的GreetingGhoul二进制文件，前面有一个有效的PNG头），解密后执行。

**GreetingGhoul 和Remcos**

GreetingGhoul是一款旨在窃取加密货币相关凭证的窃取器，大致由两个协同工作的主部件组成：

一个使用MS WebView2在加密货币钱包接口上创建覆盖的组件;

一个检测加密货币钱包应用程序并窃取敏感信息(例如恢复短语)的组件。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230614/1686733969109952.png "1686733969109952.png")

虚假窗口示例

对于硬件钱包，用户永远不应该在计算机上填写备份种子(recovery seed),。硬件钱包供应商绝不会要求用户提供备份种子，也不会让用户提供与你的设备有关的信息。不要相信任何人要求你提供备份种子，这可能会导致你的账户和资金被损害。

GreetingGhoul之后，研究人员还发现了几个下载Remcos RAT的DoubleFinger样本。Remcos是一种著名的商业RAT，经常被攻击者使用，研究人员已经看到它被用于针对企业和组织。Remcos是一款商业远控木马，包括实现远程桌面控制、屏幕窃取、剪切板窃取、摄像头及音频窥视、命令执行、浏览器窃密、密码窃取、创建代理等丰富功能，能对文件、进程、服务、窗口、注册表、网络等信息进行收集和管理。

**幕后组织分析**

研究人员在恶意软件中发现了几段俄语文本。C2 URL的第一部分是“Privetsvoyu”，这是俄语单词“问候”的拼写错误的音译。研究人员还发现了字符串“salavsmembratyamyazadehayustlokeretodlyagadoveubilinashusferu”。尽管这句话的音译很奇怪，但大致可以翻译成:“向所有兄弟问好，我在这里快窒息了，储物柜是给混蛋用的，你把我们感兴趣的领域搞砸了。”

分析发现，受害者位于欧洲、美国和拉丁美洲。

**总结**

对DoubleFinger加载器和GreetingGhoul恶意软件的分析显示，它们具有高度的复杂性和技能，类似于高级持续威胁（APT），比如它们且具有隐写功能的多级shellcode式加载器、使用Windows COM接口进行秘密执行，以及实现用于注入远程进程的Process Doppelgäging，都表明这是一个精心开发的恶意软件。使用Microsoft WebView2运行时创建加密货币钱包的伪造接口进一步突出了恶意软件所采用的先进技术。

本文翻译自：https://securelist.com/doublefinger-loader-delivering-greetingghoul-cryptocurrency-stealer/109982/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?pJ2vY1TM)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

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

[查看更多](https://www.4hou.com/member/bo2j)

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