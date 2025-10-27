---
title: iClicker网站遭遇网络攻击 通过假验证码向学生分发恶意软件
url: https://www.4hou.com/posts/xyx3
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-15
fetch_date: 2025-10-06T22:23:38.175748
---

# iClicker网站遭遇网络攻击 通过假验证码向学生分发恶意软件

iClicker网站遭遇网络攻击 通过假验证码向学生分发恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# iClicker网站遭遇网络攻击 通过假验证码向学生分发恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-14 17:52:13

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)59953

收藏

导语：知名学生互动平台iClicker的网站遭到ClickFix攻击，该攻击使用假的CAPTCHA提示来欺骗学生和教师在他们的设备上安装恶意软件。

知名学生互动平台iClicker网站遭到ClickFix攻击，该攻击使用假的CAPTCHA提示来欺骗学生和教师在他们的设备上安装恶意软件。

iClicker是一种数字课堂工具，教师可以使用它来记录出勤情况，提出现场问题或调查，并跟踪学生的参与情况。它被美国各地的5000名教师和700万名学生广泛使用，包括密歇根大学、佛罗里达大学和加利福尼亚大学。

根据密歇根大学安全计算团队的安全警报，iClicker网站在2025年4月12日至4月16日期间遭到黑客攻击，显示了一个假的CAPTCHA，指示用户按“我不是机器人”来验证自己。

然而，当访问者点击验证提示时，PowerShell脚本被悄无声息地复制到Windows剪贴板中，这就是所谓的“ClickFix”社会工程攻击。

然后CAPTCHA会指示用户打开Windows运行对话框（Win + R），将PowerShell脚本（Ctrl + V）粘贴到其中，并按Enter键执行以验证自己。

![example-captcha-clickfix.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250513/1747118369141385.png "1747116980155106.png")

一个假的CAPTCHA在ClickFix攻击的例子

当ClickFix攻击不再在iClicker的网站上运行时，Reddit上的一个人在Any上发起了这个命令。Run，显示要执行的PowerShell有效负载。

iClicker攻击中使用的PowerShell命令被严重混淆，但在执行时，它会连接到位于http://67.217.228[.]14:8080的远程服务器，以检索要执行的另一个PowerShell脚本。

![obfuscated-powershell-command.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250513/1747118370103748.png "1747117028233510.png")

在iClicker ClickFix攻击中使用的模糊PowerShell脚本

但人们无法知道最终安装了什么恶意软件，因为根据访问者的类型，检索到的PowerShell脚本是不同的。

对于目标访问者，它会发送一个脚本，将恶意软件下载到计算机上。密歇根大学表示，恶意软件允许威胁者完全访问受感染的设备。

对于那些不是目标的，比如恶意软件分析沙箱，脚本将下载并运行合法的Microsoft Visual c++ Redistributable，如下所示。

```
iwr https://download.microsoft.com/download/9/3/f/93fcf1e7-e6a4-478b-96e7-d4b285925b00/vc_redist.x64.exe -out "$env:TMP/vc_redist.x64.exe"; & "$env:TMP/vc_redist.x64.exe"
```

ClickFix攻击已成为广泛的社会工程攻击，已被用于许多恶意软件活动，包括假装为Cloudflare CAPTCHA，谷歌Meet和web浏览器错误的攻击。

从过去的攻击来看，攻击可能会分发一个信息拦截器，它可以从谷歌Chrome、Microsoft Edge、Mozilla Firefox和其他Chromium浏览器窃取cookie、凭据、密码、信用卡和浏览历史记录。

这种类型的恶意软件还可以窃取加密货币钱包、私钥和可能包含敏感信息的文本文件，例如名为seed.txt、pass.txt、ledger.txt、trezor.txt、metamask.txt、bitcoin.txt、words、wallet.txt、\*.txt和\*.pdf的文件。

这些数据被收集成存档并发送回攻击者，在那里他们可以在进一步的攻击中使用这些信息，或者在网络犯罪市场上出售这些信息。

被盗的数据也可以用来进行大规模的破坏，从而导致勒索软件攻击。由于此次攻击的目标是大学生和教师，其目的可能是窃取证书，然后对大学网络进行攻击。

值得一提的是，有人发现iClicker于5月6日在其网站上发布了一份安全公告，但在页面的HTML中包含了一个标签，从而阻止了该文档被搜索引擎索引，从而使查找有关该事件的信息变得更加困难。

![noindex.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250513/1747118371700055.png "1747117150204005.png")

带有noindex标签的点击器安全公告

“我们最近解决了一个影响iClicker登陆页面（iClicker.com）的事件。重要的是，iClicker的数据、应用程序或操作都没有受到影响，iClicker登陆页面上发现的漏洞已经得到解决，”iClicker的安全公告写道。

出于考虑，iClicker建议在网站被黑客入侵时访问iClicker.com并遵循虚假CAPTCHA指令的用户应立即更改其iClicker密码，如果执行了该命令，则应将存储在计算机上的所有密码更改为每个网站的唯一密码。此外，通过移动应用程序访问iClicker或没有遇到假CAPTCHA的用户不会受到攻击的风险。

文章翻译自：https://www.bleepingcomputer.com/news/security/iclicker-hack-targeted-students-with-malware-via-fake-captcha/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?1CCrYtwU)

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