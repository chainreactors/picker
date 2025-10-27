---
title: App漏洞可远程解锁启动汽车，影响现代、捷尼赛思汽车
url: https://www.4hou.com/posts/JXpy
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-05
fetch_date: 2025-10-04T00:30:39.791034
---

# App漏洞可远程解锁启动汽车，影响现代、捷尼赛思汽车

App漏洞可远程解锁启动汽车，影响现代、捷尼赛思汽车 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# App漏洞可远程解锁启动汽车，影响现代、捷尼赛思汽车

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-12-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)138203

收藏

导语：​汽车APP漏洞可远程解锁启动汽车，影响2012年之后部分型号汽车。

汽车APP漏洞可远程解锁启动汽车，影响2012年之后部分型号汽车。

Yuga Labs安全研究人员发现了现代汽车APP中的安全漏洞，并在丰田、宏达、尼桑、英菲尼迪等汽车制造商使用的SiriusXM "smart vehicle"平台中发现了类似的攻击面。截止目前，安全研究人员尚未公开漏洞的技术细节，但在推特分享了相关的信息。

**现代汽车问题**

现代汽车和捷尼赛思汽车的移动APP名为MyHyundai和MyGenesis，允许认证用户启动、停止、锁定、解锁其汽车。

![MyHyundai app interface](https://www.bleepstatic.com/images/news/u/1220909/Software/myhyundai-app.jpg)

图 MyHyundai app接口

在拦截者2个APP生成的流量经过分析后，研究人员发现可以从中提取出API调用用于进一步分析。

研究人员发现，其所有者的验证是基于用户的电子邮件地址的，而电子邮件地址包含在POST请求的json中。

而且MyHyundai APP在注册时并不需要邮件确认，只使用用户注册时的邮件地址和额外的控制字符来创建账户。

最后，发送JSON token中包含欺骗地址、JSON body中包含受害者地址的HTTP请求到Hyundai终端，就可以成功绕过有效性验证。

![Response to the forged HTTP request](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/hyundai-response.png)

图 伪造的HTTP请求的响应

为验证是否可以攻击汽车，研究人员尝试解锁了一辆现代汽车。几秒钟后，被攻击的汽车成功解锁了。

在现实攻击中需要多个步骤，研究人员将攻击过程封装进了一个Python脚本，只需输入目标邮件地址，就可以执行所有命令，并成功接管受害者汽车。

**SiriusXM问题**

SiriusXM 是一家车载服务提供商，有超过15个汽车厂商使用，有超过1200万连网汽车使用该服务。

Yuga Labs 安全研究人员发现宝马、本田、英菲尼迪、尼桑、丰田、雷克萨斯、路虎等都汽车厂商都使用SiriusXM 技术来实现远程车辆管理功能。

研究人员拦截了尼桑APP的网络流量，发现只需要知道目标车辆的ID（VID）就能发送伪造的HTTP请求到车辆。

对非授权的请求的响应中包含目标车辆名、手机号码、地址和车辆详细信息。

考虑到根据VIN很容易获取，比如在车上、卖车网站上都有。除了信息泄露外，这些请求也可以在其他汽车上执行命令。

![Python script that fetches all known data for a given VIN](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/VIN-python.png)

图 Python脚本输入VIN提取数据

BleepingComputer也联系了Hyundai和SiriusXM来确定漏洞是否被利用用于攻击现实用户。厂商回应称截止目前未发现有现实用户被攻击。

Yuga Labs研究人员已经通知了Hyundai和SiriusXM的漏洞和相关风险。目前，厂商也已经修复了相关的漏洞。

研究人员Sam Curry确认漏洞影响2015年之后使用SiriusXM的汽车品牌。攻击者利用该漏洞在只需要知道VIN号的请求下可以在SiriusXM平台上实现远程追踪、车辆锁定、解锁、启动、停止、开启车前灯。

本文翻译自：https://www.bleepingcomputer.com/news/security/hyundai-app-bugs-allowed-hackers-to-remotely-unlock-start-cars/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mvEAUSso)

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

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

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

[查看更多](https://www.4hou.com/member/e7OO)

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