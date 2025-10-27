---
title: 微星UEFI签名密钥泄露，引发“末日”供应链攻击恐慌
url: https://www.4hou.com/posts/z465
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-18
fetch_date: 2025-10-04T11:37:04.695058
---

# 微星UEFI签名密钥泄露，引发“末日”供应链攻击恐慌

微星UEFI签名密钥泄露，引发“末日”供应链攻击恐慌 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 微星UEFI签名密钥泄露，引发“末日”供应链攻击恐慌

布加迪
[新闻](https://www.4hou.com/category/news)
2023-05-17 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)125076

收藏

导语：由于无法轻松吊销泄露的密钥，微星及其客户如今陷入了困境。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230517/1684293303161107.jpeg "1684197816173482.jpeg")

一位研究人员表示，一起针对硬件制造商微星（MSI）的勒索软件入侵引发了人们对毁灭性供应链攻击的担忧。这种攻击可能会注入恶意更新，而这些更新已使用受大量最终用户设备信任的公司签名密钥进行签名。

安全公司Binarly的首席执行官、研究主管兼创始人Alex Matrosov在接受采访时说：“这有点像世界末日的场景，很难同时更新众多设备，它们会在一段时间内保持非最新状态，会使用旧密钥来验证身份。这个问题很难解决，我认为微星没有任何后备方案来实际阻止泄露的密钥。”

**泄露的密钥+未吊销密钥=招致灾难**

据Bleeping Computer媒体首次报道，入侵事件于 4 月曝光，当时Money Message 勒索软件组织的勒索门户网站将微星列为新的受害者，并发布了屏幕截图，声称显示的文件夹含有私密的加密密钥、源代码及其他数据。一天后微星发布了一份简短的公告，称其“部分信息系统遭到了网络攻击。”该公告敦促客户只从微星官网获取更新，对泄露的密钥只字未提。

自那以后，Matrosov分析了暗网上Money Message网站上发布的数据。令他震惊的是，这些信息中居然含有两个私密的加密密钥。第一个是签名密钥，对微星固件更新进行数字签名，以加密方式证明它们是来自微星的合法更新，而不是来自威胁分子的冒名顶替的恶意更新。

这加大了这种可能性：泄露的密钥发布的更新可能会在不触发警告的情况下感染计算机的最底层区域。更为糟糕的是，微星没有像戴尔、惠普和许多大牌硬件制造商那样的一套自动化补丁程序。因此，微星并不提供相同类型的密钥吊销功能。

这很糟糕。这种情况并不经常发生。微星需要对这一事件给予高度关注，因为这里存在非常严重的安全隐患。

更令人担忧的是，微星迄今为止一直对此事保持缄默。媒体发电子邮件请求置评，询问该公司是否计划向客户发布指导性建议，公司代表并没有回复。

在过去的十年中，基于云的网络管理服务SolarWinds的软件构建和分发系统在2019年遭到了攻击，这类供应链攻击在一次事件中向数千名用户发送了恶意攻击载荷，当时受害者只是安装了一个有效签名的更新，仅此而已。

通过控制用于验证合法更新的私钥，名为APT29和Cozy Bear 的俄罗斯黑客组织（据信隶属俄罗斯对外情报局）用恶意软件的第一阶段感染了18000多个客户。10家联邦机构和大约 100家私营公司收到了后续阶段的攻击载荷，从而安装了用于间谍活动的后门。

3月，电话公司3CX披露了其软件构建系统遭到攻击，该公司开发的流行VoIP软件被190个国家地区的600000多家组织使用。据研究人员声称，这次入侵背后的黑客为朝鲜政府效力，闯入3CX的系统后向数量不详的客户提供恶意更新。

安全公司Mandiant后来声称，3CX 被攻击是因针对软件开发商Trading Technologies的供应链攻击而受到感染，3CX使用了这家公司开发的X\_Trader 金融交易程序。

目前没有关于针对微星客户的供应链攻击的报告。获得破坏软件构建系统所需的这种控制通常并非易事，需要高超的技能，可能还需要一番运气。不过，由于微星没有自动化更新机制或吊销流程，因此对攻击者来说门槛可能比较低。

无论难度如何，如果获得微星用于以加密方式验证其安装程序文件真实性的签名密钥，都会大大减少成功策划有效供应链攻击所需的精力和资源。

Matrosov说：“最糟糕的场景是，攻击者不仅可以获得密钥，还可以使用这些密钥来分发该恶意更新。”

总部位于荷兰的国家网络安全中心（NCSC）在一份公告中并未排除这种可能性。

NCSC的工作人员写道：“由于成功的滥用在技术上很复杂，原则上需要本地访问易受攻击的系统，因此NCSC认为滥用的风险很小。然而，泄露的密钥将被滥用于针对性攻击并非不可想象。NCSC尚未发现任何滥用泄露密钥的迹象。”

使威胁更加复杂的是，Money Message黑客还获得了用于微星分发给其客户的英特尔Boot Guard版本的私密加密密钥。其他许多硬件制造商使用不受影响的不同密钥。

英特尔发言人在一封电子邮件中写道：“英特尔已获悉这些报告，正在积极调查。有研究人员声称，数据中含有私密签名密钥，包括用于英特尔BootGuard的微星OEM签名密钥。值得一提的是，英特尔BootGuard OEM密钥是由这家系统制造商生成的，这些不是英特尔签名密钥。”

**范围广泛的访问权**

英特尔Boot Guard内置于现代英特尔硬件中，旨在防止通常加载UEFI bootkit这种形式的恶意固件。这种恶意软件驻留在嵌入到主板的芯片中，即使并非不可能检测出来，也很难检测出来，每次打开计算机时就先执行恶意软件。UEFI感染允许在操作系统开始运行之前加载恶意软件，从而可以绕过保护机制，更隐蔽地躲避安全端点保护。

在最坏的情况下，同时拥有这两个密钥会进一步加剧威胁。NCSC 周三的公告中解释：

“英特尔Boot Guard是英特尔开发的技术。英特尔Boot Guard在系统启动过程中验证主板固件是否已由供应商进行数字签名。微星泄露Intel Boot Guard和固件密钥使攻击者能够对恶意固件进行自签名。（原则上本地）访问高危系统的攻击者随后可以安装并运行该固件。

这为攻击者提供了影响广泛的访问权以访问系统，绕过了所有了层层添加的安全措施。比如说，攻击者获得了对存储在系统上的数据的访问权，或者可以利用该访问权实施进一步的攻击。

芯片制造商英特尔已通知NCSC，泄露的私钥是微星专用的，因此只能用于微星系统。然而，微星主板可能会集成到其他供应商的产品中。因此，滥用泄露的密钥也可能发生在这些系统上。”

目前，使用受影响硬件的人迄今为止似乎仅限于微星客户或转售微星硬件的第三方，他们

应格外警惕任何固件更新，即使更新已经过有效签名。

本文翻译自：https://arstechnica.com/information-technology/2023/05/leak-of-msi-uefi-signing-keys-stokes-concerns-of-doomsday-supply-chain-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?9esTUXoh)

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