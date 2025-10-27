---
title: WiFi协议曝出漏洞，攻击者可以轻松劫持网络流量
url: https://www.4hou.com/posts/YYpp
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-01
fetch_date: 2025-10-04T11:19:42.117525
---

# WiFi协议曝出漏洞，攻击者可以轻松劫持网络流量

WiFi协议曝出漏洞，攻击者可以轻松劫持网络流量 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# WiFi协议曝出漏洞，攻击者可以轻松劫持网络流量

布加迪
[新闻](https://www.4hou.com/category/news)
2023-03-31 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)176049

收藏

导语：网络安全研究人员近日在IEEE 802.11 WiFi协议标准的设计中发现了一个基本的安全漏洞，这个漏洞让攻击者可以诱骗接入点泄露明文格式的网络帧。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680229038239246.png "1680041913935338.png")

WiFi网络帧如同数据容器，由报头、数据载荷和报尾组成，含有源和目的地MAC地址、控制和管理数据之类的信息。

这些帧在队列中排序，在受控制的材料中传输以免碰撞，并通过密切关注接收端的繁忙/空闲状态来最大限度地提升数据交换性能。

研究人员发现，队列/缓冲帧并没有得到充分的保护，攻击者可以采取多种手段：操控数据传输、客户端欺骗、帧重定向和捕获。

美国东北大学的Domien Schepers和Aanjhan Ranganathan以及比利时鲁汶大学imec-DistriNet的Mathy Vanhoef在昨天发表了一篇技术论文《对帧做手脚：通过操控传输队列绕过WiFi加密机制》，他们在论文中写道：“我们的攻击有其广泛的影响，因为它们可以影响各种不同的设备和操作系统（Linux、FreeBSD、iOS和安卓），还因为它们可以用来劫持TCP连接或拦截客户端和互联网流量。”

**节电漏洞**

IEEE 802.11标准包括节电机制，允许WiFi设备通过缓冲或队列发给睡眠模式设备的帧来达到节电效果。

当客户端站（接收设备）进入睡眠模式时，它向接入点发送一个帧，该帧的报头含有节电位，因此发给该接入点的所有帧都进入队列。

然而，该标准并没有为管理这些队列帧的安全性提供明确的指导，也没有设置限制，比如帧可以在这种状态下逗留多长时间。

一旦客户端站由睡眠模式进入工作模式，接入点将缓存的帧从队列中取出，采用加密，并将它们传输到目的地。

攻击者可以欺骗网络上设备的MAC地址，并向接入点发送节电帧，从而迫使它们开始将发送给目标的帧列入队列。然后，攻击者发送唤醒帧来检索帧堆栈。

传输的帧通常使用在WiFi网络中所有设备之间共享的组地址加密密钥或成对加密密钥进行加密，这个加密密钥对每个设备而言都具有唯一性，用于加密两个设备之间交换的帧。

然而，攻击者可以通过向接入点发送验证帧和关联帧来改变帧的安全上下文，从而迫使接入点以明文形式传输帧或使用攻击者提供的密钥对其进行加密。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680229039133094.png "1680041927160188.png")

图1. 攻击图（图片来源：papers.mathyvanhoef.com）

这种攻击可以使用研究人员创建的名为MacStealer的自定义工具来实现，该工具可以测试WiFi网络的客户端隔离旁路，并在MAC层拦截发给其他客户端的流量。

研究人员报告，来自Lancom、Aruba、思科、华硕和友讯的网络设备型号已知受到这些攻击的影响，完整的设备列表如下。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230331/1680229040194134.png "1680041944102033.png")

图2. 测试后发现易受攻击的设备（图片来源：papers.mathyvanhoef.com）

研究人员警告，这些攻击可能被用来将JavaScript等恶意内容注入到TCP数据包中。

研究人员警告：“攻击者可以使用他们自己的与互联网连接的服务器，通过注入带有受欺骗的发送者IP地址的路径外TCP数据包，将数据注入到这个TCP连接中。”

“比如说，这可能被用来通过明文HTTP连接向受害者发送恶意JavaScript代码，目的是利用客户端浏览器中的漏洞。”

虽然这种攻击也可以用来窥视流量，但由于大多数互联网流量都是使用TLS加密的，因此造成的影响有限。

技术细节和研究内容可在USENIX Security 2023论文中获得（https://papers.mathyvanhoef.com/usenix2023-wifi.pdf），该论文将于2023年5月12日在即将召开的黑帽亚洲大会上发表。

**思科承认漏洞**

第一家承认WiFi协议漏洞影响的供应商是思科，它承认论文中概述的攻击可能会成功攻陷思科无线接入点产品和具有无线功能的思科Meraki产品。

然而思科认为，检索到的帧不太可能危及适当安全的网络具有的整体安全性。

思科声称：“这种攻击被视为伺机作案的攻击，攻击者获得的信息在安全配置的网络中几乎没有多少价值。”

不过，该公司还是建议用户采取缓解措施，比如通过思科身份服务引擎（ISE）等系统使用策略执行机制，该系统可以通过实施思科TrustSec或软件定义访问（SDA）技术来限制网络访问。

思科的安全公告写道：“思科还建议尽可能实施传输层安全，以便对传输中的数据进行加密，因为这将使攻击者无法使用获取的数据。”

目前，还没有有人恶意利用研究人员发现的漏洞的已知案例。

参考及来源：https://www.bleepingcomputer.com/news/security/wifi-protocol-flaw-allows-attackers-to-hijack-network-traffic/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?VJbSfuHS)

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