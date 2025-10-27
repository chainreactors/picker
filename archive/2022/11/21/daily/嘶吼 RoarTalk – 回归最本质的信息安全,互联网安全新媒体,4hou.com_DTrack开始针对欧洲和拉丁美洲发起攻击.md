---
title: DTrack开始针对欧洲和拉丁美洲发起攻击
url: https://www.4hou.com/posts/JXMv
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-21
fetch_date: 2025-10-03T23:18:40.436007
---

# DTrack开始针对欧洲和拉丁美洲发起攻击

DTrack开始针对欧洲和拉丁美洲发起攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# DTrack开始针对欧洲和拉丁美洲发起攻击

luochicun
[新闻](https://www.4hou.com/category/news)
2022-11-20 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)156024

收藏

导语：本文文中强调一些有趣的修改，Dtrack将自己隐藏在一个看起来像合法程序的可执行文件中，在恶意软件有效负载开始之前，需要经过几个阶段的解密。

![sl-abstract-world-map-chip-danger-1200-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565764272775.jpeg "1668565642848207.jpeg")

DTrack是Lazarus组织开发的后门，该后门最早于2019年被发现，目前仍在使用。Lazarus组织用它来攻击各种各样的目标。例如，我们已经看到它被用于攻击自动取款机，攻击核电站和有针对性的勒索软件攻击。基本上，Lazarus组织都是冲着经济利益去的。

DTrack允许攻击者在受害主机上上传、下载、启动或删除文件。在标准DTrack工具集中已经发现的那些已下载和执行的文件中，有一个键盘记录器、一个截图生成器和一个用于收集受害系统信息的模块。有了这样的工具集，攻击者可以在受害者的基础设施中实施横向移动，以检索泄露信息。

DTrack本身在过去的时间里并没有太大的变化。尽管如此，我们还是想在本文文中强调一些有趣的修改，Dtrack将自己隐藏在一个看起来像合法程序的可执行文件中，在恶意软件有效负载开始之前，需要经过几个阶段的解密。

**第一阶段——植入代码**

DTrack分几个阶段解压恶意软件。第二阶段存储在恶意软件PE文件中。要实现这一点，有两种方法：

基于偏移；

基于资源；

DTrack通过从文件中的偏移量读取有效负载，或者通过从PE二进制文件中的资源读取有效负载来检索有效负载。下面是使用基于偏移量的方法检索数据的反编译伪函数的示例。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565765189912.png "1668565650204364.png")

DTrack偏移量检索函数示例

在检索到下一个阶段的位置及其密钥后，恶意软件然后解密缓冲区(使用修改过的RC4算法)并将控制权传递给它。为了计算有效负载的偏移量、大小和解密密钥，DTrack有一个特殊的二进制（我们称之为“解密配置”）结构，隐藏在PE文件的一个不显眼的部分。

**第二阶段——shellcode**

第二阶段有效负载由高度混淆的shellcode组成，如下所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565769129208.png "1668565659491419.png")

高度混淆的第二阶段shellcode

第二阶段使用的加密方法因每个样本而异。到目前为止，我们已经发现了RC4、RC5和RC6算法的修改版本。通过再次读取Decrypt config来获得第三阶段有效负载及其解密密钥的值。

DTrack改进的一个方面是第三阶段有效负载不一定是最终有效负载，可能存在由二进制配置和至少一个shellcode组成的另一段二进制数据，该shellcode依次解密并执行最终有效负载。

**第三阶段——shellcode和最终的二进制代码**

shellcode有一些非常有趣的混淆技巧，使分析更加困难。启动时，搜索密钥(用于解密最终有效负载)的开头。例如，当密钥的开头是0xDEADBEEF时，shellcode将搜索第一个出现的0xDEADEEF。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565770140681.png "1668565673211745.png")

Chunk解密例程示例

一旦找到密钥，shellcode使用它来解密密钥之后的8个字节，这些字节形成了另一个配置块，具有最终的有效负载大小及其入口点偏移量。配置块之后是一个加密的PE有效负载，它在使用自定义算法解密后的入口点偏移处开始。

**最终有效负载**

一旦最终的有效负载（DLL）被解密，它将使用process hollowing技术加载到explorer.exe中。在以前的DTrack示例中，要加载的库是模糊字符串。在最新的版本中，他们使用API哈希来加载适当的库和函数。另一个小变化是使用3台C2服务器而不是6台。负载的其余功能保持不变。

**基础设施**

当我们查看C2服务器使用的域名时，在某些情况下可以看到一种模式。例如，攻击者将一种颜色与一种动物的名字结合起来(例如，pinkgoat, purplebear, salmonrabbit)。DTrack基础设施中使用的一些特殊名称如下：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668565770838438.png "1668565681187575.png")

**攻击目标**

根据KSN的跟踪分析，他们已经在德国、巴西、印度、意大利、墨西哥、瑞士、沙特阿拉伯、土耳其和美国探测到DTrack的活动，这表明DTrack正在向世界上更多的地区扩散。目标行业包括教育、化工制造、政府研究中心和政策研究所、IT服务提供商、公用事业提供商和电信。

DTrack后门继续被Lazarus组织使用表明，Lazarus仍然将DTrack视为一项重要的攻击工具。尽管如此，自2019年首次被发现以来，Lazarus并没有太过改变后门。当对受害者进行分析时，我们就会清楚地看到，活动已经扩展到欧洲和拉丁美洲，这一趋势越来越明显。

本文翻译自：https://securelist.com/dtrack-targeting-europe-latin-america/107798/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?alfSWCbh)

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

![](https://img.4hou.com/wp-content/uploads/2017/07/6cfb327dad8fe371f6fa.jpg)

# [luochicun](https://www.4hou.com/member/aOZG)

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

[查看更多](https://www.4hou.com/member/aOZG)

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