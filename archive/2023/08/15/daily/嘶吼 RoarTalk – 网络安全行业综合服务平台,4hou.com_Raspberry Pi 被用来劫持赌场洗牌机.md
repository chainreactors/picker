---
title: Raspberry Pi 被用来劫持赌场洗牌机
url: https://www.4hou.com/posts/BXvk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-15
fetch_date: 2025-10-04T12:01:14.125693
---

# Raspberry Pi 被用来劫持赌场洗牌机

Raspberry Pi 被用来劫持赌场洗牌机 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Raspberry Pi 被用来劫持赌场洗牌机

布加迪
[新闻](https://www.4hou.com/category/news)
2023-08-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)127194

收藏

导语：安全研究人员演示证明，可以利用黑客设备连接到赌场洗牌机从而劫持洗牌机。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230814/1691976860185940.png "1691891837103020.png")

赌博是一门大生意，赌场的经营收入让场内最大的高额赌注都显得微不足道。因此，赌场落实严格的程序和流程，以确保不存在客户欺骗的情况。然而，与计算机领域相比，一些安全研究人员认为赌博法规和安全技术“有点过时”，这导致对此感兴趣的研究人员使用Raspberry Pi Zero来制造自己的概念证明工具。

去年9月，YouTube上播放了一段备受争议的洛杉矶扑克节目《Hustler Live Casino》牌局。长话短说，一个新手骗倒了一个老手。《连线》杂志报道，“成千上万愤怒的扑克玩家”高呼犯规，暗示这个新手在某种程度上作弊了。

《连线》杂志报道了《洗牌和发牌：分析自动洗牌机的安全性》，IOActive公司的Joseph Tartaro、Enrique Nissim和Ethan Shackelford在2023年黑帽大会上对此进行了一番演示。

赌场在随后长达数月的调查后得出了结论：不存在任何犯规行为。然而，这一结论引起了安全公司IOActive的计算机研究人员兼顾问Joseph Tartaro的不满。尤其让Tartaro生气的是这种说法：Deckmate洗牌机完全不容怀疑（尽管一些人怀疑洗牌机被做了手脚）。调查结论相当自信地声称：“Deckmate洗牌机是安全的，不可能被人做手脚。”

这番声明在安全界看来就像向一头公牛亮出红布一样。Deckmate是赌场中使用最广泛的自动洗牌机，因此进一步调查更备受关注。

于是，Tartaro及其在IOActive的两位同事开始对Deckmate进行了长达数月的调查。研究结果于周二在拉斯维加斯举行的黑帽安全大会上公布。

IOActive买来了几台Deckmate洗牌机，与经验丰富的操作员和工程师进行了交谈。值得关注的是，最新版本是Deckmate 2，通常放在扑克玩家膝盖旁边的桌子下，该设备有一个暴露的USB端口。如果黑客能碰到该设备，那么一切都完了。

几位安全研究人员发现，插入到Deckmate 2的USB端口的黑客设备可以“改变洗牌机的代码，以完全劫持洗牌机，并且神不知鬼不觉地篡改洗牌。”大多数对纸牌和赌博但凡有点了解的人都知道，在这些纸牌游戏中，知识就是力量。换句话说，如果一个人对所发的牌有更多的了解，他就能以小搏大。

IOActive在其概念验证赌场作弊演示中使用的黑客设备基于Raspberry Pi Zero，插入到了Deckmate 2 USB接口。IOActive表示，下定决心的骗子可能会设计出一款具有同样功能的专用设备，其外形尺寸只有一个典型的USB加密狗那么小。面对巨额钱财的引诱，骗子可能舍得在这种设备上下血本。

此外，你甚至不需要是纸牌游戏的天才就能解读Deckmate 2的数据，它甚至有一个内置的摄像头，用于验证整副牌。IOActive发现，可以查看摄像头拍摄的画面，实时了解整副牌的发牌顺序。一种明显的作弊方法是，可视化数据可以通过蓝牙发送到附近的智能手机上，IOActive团队也测试了这种方法。第二个人可以与坐在牌桌边的玩家串通，发出做出决定或策略的信号。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230814/1691976861143052.png "1691891825121966.png")

Tartaro提到Deckmate 2黑客攻击时说：“基本上，它允许我们多少可以做任何我们想做的事情……比如说，我们可以从摄像头读取恒定的数据，这样我们就可以知道发牌顺序，那样我们就能确切地知道每个人都会有什么样的一手牌。”

IOActive还透露了其他一些有趣的研究成果。该研究团队特别指出，最初的Deckmate没有USB端口，但可以通过其他方式做手脚，特别是如果有赌场内部人士愿意这么做的话。据说一些Deckmate还附带一个蜂窝调制解调器，以便厂商监控。这就为中间人攻击或蜂窝信号欺骗提供了更大的攻击面。

面对《连线》杂志的报道，Deckmate系列洗牌机的生产商Light & Wonder对来自IOActive的警告似乎表现出了一种逃避现实的态度。该公司表示，没有已知的证据表明他们的设备在赌场被黑客入侵。然而，负责制定赌场标准的国际博彩标准协会的一位高管建设性地谈到了组建一个技术委员会来调查IOActive的发现结果。有人已经提出了加强安全性的想法，比如移除外部USB端口，或者对软件/固件进行一些修改。我们认为，把IOActive的研究工作看作是建设性的批评可能是个好主意，而不是置之不理。

本文翻译自：https://www.tomshardware.com/news/raspberry-pi-enables-security-researchers-to-hijack-casino-card-shuffling-machine如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?MwsrTJu1)

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