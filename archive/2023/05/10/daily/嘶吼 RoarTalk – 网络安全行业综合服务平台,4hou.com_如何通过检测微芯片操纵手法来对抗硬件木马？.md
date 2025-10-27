---
title: 如何通过检测微芯片操纵手法来对抗硬件木马？
url: https://www.4hou.com/posts/YYW9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-10
fetch_date: 2025-10-04T11:38:49.147935
---

# 如何通过检测微芯片操纵手法来对抗硬件木马？

如何通过检测微芯片操纵手法来对抗硬件木马？ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 如何通过检测微芯片操纵手法来对抗硬件木马？

布加迪
[新闻](https://www.4hou.com/category/news)
2023-05-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)149145

收藏

导语：安全漏洞不仅存在于软件中，还可能直接嵌入到硬件中，导致技术应用软件暴露在广泛攻击的面前。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230509/1683601808128245.jpeg "1683532283362342.jpeg")

研究人员为其项目拍摄了数千张微芯片的显微镜图像。图1为采用金色芯片封装的微芯片。被检查的芯片面积只有2平方毫米大小。

来自德国波鸿市鲁尔大学与马克斯普朗克安全和隐私研究所（MPI-SP）的研究人员正在率先采用创新的检测技术来对付这些硬件木马。他们研发的先进算法可以通过将芯片图纸与实际芯片的电子显微镜图像进行比较来识别差异之处。这种开创性的方法检测出差异之处的成功率达到了92.5%。

这支研究团队在网上免费提供了所有的芯片图像、设计数据和分析算法（https://github.com/emsec/ChipSuite），使研究人员同行能够访问这些资源，将这些资源用于他们自己的研究，促进该领域的发展。

**生产设施：硬件木马的潜在入口点**

如今，电子芯片被集成到众多硬件设备中。它们通常是由不自行运营生产设施的公司设计的。因此，设计图纸被送到高度专业化的芯片工厂用于生产芯片。

Steffen Becker博士解释：“可以想象，工厂的设计图纸可能会在生产前夕被引入微小的变化，而这可能会破坏芯片的安全性。在极端情况下，这种硬件木马可能允许攻击者只需摁下按钮，就能使部分电信基础设施处于瘫痪状态。”

Steffen Becker 博士领导的CASA卓越中心和 Endres Puschner领导的MPI-SP团队的研究人员分析了采用28纳米、40纳米、65纳米和 90纳米这四种现代技术工艺生产的芯片。为此，他们与Thorben Moos博士进行了合作。Moos博士在波鸿鲁尔大学攻读博士学位期间设计并制造了多款芯片。

研究人员手头拥有设计图纸和已制造出来的芯片。他们显然无法在事后修改芯片、内置硬件木马。于是他们采用了一个花招：Moos不是对芯片做手脚，而是追溯性地改变了芯片设计，力求设计图纸和芯片之间的偏差尽可能小。然后，研究人员测试自己是否能够在不知道具体找什么、去哪里找的情况下检测到这些变化。

第一步，研究人员不得不使用复杂的化学和机械方法准备好芯片，用扫描电子显微镜拍摄数千张芯片最底层的图像。芯片最低层含有数十万个执行逻辑操作的所谓的标准单元。

Endres Puschner表示：“结果表明，比较芯片图像和设计图纸是一个相当艰巨的挑战，因为我们首先必须精确地叠加数据。”此外，芯片上的每一个小杂质都会挡住图像某些部分的视线。他得出结论：“在尺寸为 28 纳米的最小芯片上，一粒灰尘或一根头发就可以遮住一整排的标准单元。”

**几乎所有操纵手法都被检测出来**

研究人员利用图像处理方法，认真匹配标准单元，寻找设计图纸与芯片显微镜图像之间的偏差。Puschner总结研究结果时说：“结果让人感到谨慎乐观。”针对90纳米、65纳米和40纳米的芯片尺寸，研究团队成功识别出了所有改动。误报结果的数量总计为500，误报是指标准单元被标记为已被改动，不过它们实际上并没有受到影响。“就检查的150多万个标准单元而言，这个误报率已是非常低了。只有面对最小的28纳米芯片，研究人员未能检测到三个细微的变化。”

**通过洁净室和优化算法提高检测率**

更好的记录质量有望在未来解决这个问题。Becker指出：“确实存在专门为拍摄芯片图像而设计的扫描电子显微镜。”此外，在可以防止污染的洁净室中使用扫描电子显微镜有望进一步提高检测率。

Steffen Becker概述潜在的未来开发时说：“我们也希望其他研究小组会使用我们的数据进行后续研究。机器学习可能会大大改进检测算法，以便也能检测到我们未检查的最小尺寸芯片上的变化。”

本文翻译自：https://www.helpnetsecurity.com/2023/03/22/hardware-trojans-detecting-microchip-manipulations/?web\_view=true如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?cUPM8FLr)

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