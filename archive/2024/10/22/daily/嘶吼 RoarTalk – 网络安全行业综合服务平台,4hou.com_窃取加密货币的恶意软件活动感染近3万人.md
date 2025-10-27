---
title: 窃取加密货币的恶意软件活动感染近3万人
url: https://www.4hou.com/posts/omON
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-22
fetch_date: 2025-10-06T18:47:29.135322
---

# 窃取加密货币的恶意软件活动感染近3万人

窃取加密货币的恶意软件活动感染近3万人 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 窃取加密货币的恶意软件活动感染近3万人

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-10-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)80561

收藏

导语：为避免意外的经济损失，请用户仅从该项目的官方网站下载软件，并阻止或跳过 Google 搜索上的推广结果。

目前，来自俄罗斯、土耳其、乌克兰和欧亚地区其他国家的超过 28,000 人正受到大规模加密货币窃取恶意软件活动的影响。

该恶意软件活动将自己伪装成通过 YouTube 视频和欺诈性 GitHub 存储库推广的合法软件，受害者在其中下载受密码保护的档案，从而引发感染。

据网络安全公司 Dr. Web 称，该活动使用盗版办公相关软件、游戏作弊和黑客行为，甚至自动交易机器人来欺骗用户下载恶意文件。

据悉，这次恶意软件活动总共影响了 28,000 多人，其中绝大多数是俄罗斯居民。另外。白俄罗斯、乌兹别克斯坦、哈萨克斯坦、乌克兰、吉尔吉斯斯坦和土耳其也发现了大量感染病例。

![site.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241014/1728888877977516.jpg "1728888755682420.jpg")

宣传 Microsoft Excel 本地化（俄语）下载的恶意网站

**感染链**

感染首先打开一个自解压存档，该存档在下载时会逃避防病毒扫描，因为它受密码保护。受害者输入提供的密码后，存档会释放各种混淆的脚本、DLL 文件和用于启动主有效负载的数字签名加载程序的 AutoIT 解释器。

该恶意软件会检查调试工具是否存在，以查看它是否在分析人员的环境中运行，如果发现任何工具，则会终止。

接下来，它提取攻击后续阶段所需的文件，然后使用图像文件执行选项 (IFEO) 技术修改 Windows 注册表以实现持久性。

简而言之，它利用恶意服务劫持合法的 Windows 系统服务以及 Chrome 和 Edge 的更新进程，因此恶意软件文件会在这些进程启动时执行。

Windows 恢复服务被禁用，并且恶意软件文件和文件夹的“删除”和“修改”权限被撤销，以防止尝试清理。

从那时起，Ncat 网络实用程序用于与命令和控制 (C2) 服务器建立通信。该恶意软件还可以收集系统信息，包括运行的安全进程，并通过 Telegram 机器人窃取这些信息。

![attack-chain.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241014/1728888879139386.png "1728888844298179.png")

完整的攻击链

**财务影响**

该活动将两个关键有效负载传送到受害者的机器上。第一个是“Deviceld.dll”，这是一个经过修改的 .NET 库，用于执行 SilentCryptoMiner，它使用受害者的计算资源来挖掘加密货币。

第二个有效负载是“7zxa.dll”，这是一个经过修改的 7-Zip 库，充当剪辑器，监视 Windows 剪贴板中复制的钱包地址，并将其替换为攻击者控制下的地址。

Dr. Web 没有在报告中具体说明 28,000 台受感染机器的潜在挖矿利润，但发现仅 Clipper 就劫持了价值 6,000 美元的交易，并将金额转移到攻击者的地址上。

为避免意外的经济损失，请用户仅从该项目的官方网站下载软件，并阻止或跳过 Google 搜索上的推广结果。此外，请小心 YouTube 或 GitHub 上的共享链接，因为这些平台的合法性并不能保证下载目的地的安全。

文章翻译自：https://www.bleepingcomputer.com/news/cryptocurrency/crypto-stealing-malware-campaign-infects-28-000-people/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Shno5k8m)

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