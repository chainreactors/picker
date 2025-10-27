---
title: 僵尸网络在 LockBit Black 勒索软件活动中发送了数百万封电子邮件
url: https://www.4hou.com/posts/jgyv
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-05-25
fetch_date: 2025-10-06T17:15:25.175673
---

# 僵尸网络在 LockBit Black 勒索软件活动中发送了数百万封电子邮件

僵尸网络在 LockBit Black 勒索软件活动中发送了数百万封电子邮件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 僵尸网络在 LockBit Black 勒索软件活动中发送了数百万封电子邮件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-05-24 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)191025

收藏

导语：这是 Proofpoint 研究人员第一次观察到 LockBit Black 勒索软件样本通过 Phorphiex 大量传播。

自 4 月份以来，恶意分子通过 Phorpiex 僵尸网络发送了数百万封钓鱼电子邮件，以开展大规模的 LockBit Black 勒索软件活动。

网络安全和通信集成小组 (NJCCIC) 警告说，攻击者使用包含部署 LockBit Black 有效负载的可执行文件的 ZIP 附件，该有效负载一旦启动就会对接收者的系统进行加密。

这些攻击中部署的 LockBit Black 加密器很可能是开发人员于 2022 年 9 月在 Twitter 上泄露的 LockBit 3.0 构建器构建的。不过，据悉该活动与实际的 LockBit 勒索软件操作没有任何关系。

这些网络钓鱼电子邮件带有“您的文档”和“您的照片”主题时使用“Jenny Brown”或“Jenny Green”别名从全球 1500 多个唯一 IP 地址发送。

当收件人打开恶意 ZIP 存档附件并执行其中的二进制文件时，攻击链就开始了。然后，该可执行文件从 Phorphiex 僵尸网络的基础设施下载 LockBit Black 勒索软件样本，并在受害者的系统上执行。启动后，它将尝试窃取敏感数据、终止服务和加密文件。

![Phishing-email-sample.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240514/1715673475199135.jpg "1715671940191277.jpg")

网络钓鱼电子邮件样本

LockBit Black 勒索字条 Phorpiex 僵尸网络（也称为 Trik）已经活跃了十多年，它是由一种通过 r 传播的蠕虫进化而来的。

网络安全公司 Proofpoint 自 4 月 24 日以来一直在调查这些攻击，该公司表示，威胁分子的目标是全球各个垂直行业的公司。

尽管这种方法并不新鲜，但发送大量电子邮件来传递恶意负载以及用作第一阶段负载的勒索软件使其格外突出，尽管它缺乏其他网络攻击的复杂性。

Proofpoint 安全研究人员表示，从 2024 年 4 月 24 日开始，Proofpoint 观察到由 Phorpiex 僵尸网络发起的大量活动，其中包含数百万条消息，并传播 LockBit Black 勒索软件。

这是 Proofpoint 研究人员第一次观察到 LockBit Black 勒索软件（又名 LockBit 3.0）样本通过 Phorphiex 大量传播。

![LockBit Black ransom note.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240514/1715673476140457.jpg "1715671993171766.jpg")

LockBit Black 勒索信

Phorpiex 僵尸网络（也称为 Trik）已经活跃了十多年。它从通过可移动 USB 存储和 Skype 或 Windows Live Messenger 聊天传播的蠕虫演变为使用垃圾邮件传递的 IRC 控制的木马。

经过多年的活动和发展，该僵尸网络慢慢发展壮大，控制了超过 100 万台受感染的设备，该僵尸网络的运营商在关闭 Phorpiex 基础设施后，试图在黑客论坛上出售恶意软件的源代码。

Phorpiex 僵尸网络还被用来发送数百万封勒索电子邮件（每小时发送超过 30000 封垃圾邮件），并且最近使用剪贴板劫持者模块将复制到 Windows 剪贴板的加密货币钱包地址替换为攻击者控制的地址。

在添加加密剪裁支持后的一年内，Phorpiex 的运营商劫持了 969 笔交易，并窃取了 3.64 比特币（172300 美元）、55.87 以太币（216000 美元）和价值 55000 美元的 ERC20 代币。

为了防御推送勒索软件的网络钓鱼攻击，NJCCIC 建议实施勒索软件风险缓解策略，并使用端点安全解决方案和电子邮件过滤解决方案（如垃圾邮件过滤器）来阻止潜在的恶意消息。

文章翻译自：https://www.bleepingcomputer.com/news/security/botnet-sent-millions-of-emails-in-lockbit-black-ransomware-campaign/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OkCzR7sz)

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