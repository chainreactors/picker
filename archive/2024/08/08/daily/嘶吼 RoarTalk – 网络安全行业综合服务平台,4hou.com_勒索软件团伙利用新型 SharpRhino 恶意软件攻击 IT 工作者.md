---
title: 勒索软件团伙利用新型 SharpRhino 恶意软件攻击 IT 工作者
url: https://www.4hou.com/posts/gyZY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-08
fetch_date: 2025-10-06T18:03:51.745007
---

# 勒索软件团伙利用新型 SharpRhino 恶意软件攻击 IT 工作者

勒索软件团伙利用新型 SharpRhino 恶意软件攻击 IT 工作者 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索软件团伙利用新型 SharpRhino 恶意软件攻击 IT 工作者

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-08-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)87410

收藏

导语：为了减轻勒索软件攻击的影响，请制定备份计划，执行网络分段，并确保所有软件都是最新的。

Hunters International 勒索软件组织正利用一种名为 SharpRhino 的新型远程访问木马 (RAT) 攻击 IT 工作者，侵入公司网络。

该恶意软件可帮助 Hunters International 实现初始感染，提升他们在受感染系统上的权限，执行 PowerShell 命令，并最终部署勒索软件负载。

Quorum Cyber 的研究人员观察到勒索软件攻击中使用的恶意软件是由一个冒充 Angry IP Scanner 网站的域名抢注网站传播的，Angry IP Scanner 是 IT 专业人员使用的合法网络工具。

2024 年 1 月，网络安全公司 eSentire 和研究员 0xBurgers 就曾发现该恶意软件通过一个假冒的 Advanced IP Scanner 网站传播。

Hunters International 是一个在 2023 年底开始活跃的勒索软件组织，由于其代码相似性而被标记为可能是 Hive 的品牌重塑。著名的受害者包括美国海军承包商 Austal USA、日本光学巨头 Hoya、Integris Health 和弗雷德哈金森癌症中心。

到目前为止，2024 年该威胁组织已宣布对全球各个组织（CIS 除外）发动了 134 起勒索软件攻击，在该领域最活跃的组织中排名第十。

**SharpRhino RAT**

SharpRhino 利用数字签名的 32 位安装程序进行传播，其中包含自解压的受密码保护的 7z 存档以及用于执行感染的附加文件。

![archive.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240807/1722995748798252.png "1722995748798252.png")

存档内容

安装程序会修改 Windows 注册表以实现持久性，并创建 Microsoft.AnyKey.exe 的快捷方式，该快捷方式通常是 Microsoft Visual Studio 二进制文件，在本例中被滥用。

此外，安装程序还会释放“LogUpdate.bat”，它会在设备上执行 PowerShell 脚本，将 C# 编译到内存中，以隐秘地执行恶意软件。

为了实现冗余，安装程序会创建两个目录“C:\ProgramData\Microsoft: WindowsUpdater24”和“LogUpdateWindows”，这两个目录都用于命令和控制 (C2) 交换。恶意软件中硬编码了两个命令，分别是“delay”（延迟）和“exit”（退出），前者用于设置下一个 POST 请求的计时器，后者用于终止通信。

分析表明，该恶意软件可以在主机上执行 PowerShell，可用于执行各种危险操作。Quorum 通过 SharpRhino 成功启动 Windows 计算器，测试了这一机制。

![command-exec.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240807/1722995813186537.png "1722995813186537.png")

负责 PowerShell 执行的 QFunction

他们采用的新策略是部署网站来冒充合法的开源网络扫描工具，他们将目标瞄准 IT 工作者，希望能够窃取具有提升权限的账户。

因此，用户应谨慎对待搜索结果中的赞助结果，以避开恶意广告，激活广告拦截器以完全隐藏这些显示，并收藏已知可获取安全安装程序的官方项目网站。

为了减轻勒索软件攻击的影响，请制定备份计划，执行网络分段，并确保所有软件都是最新的，以减少特权提升和横向移动的机会。

文章翻译自：https://www.bleepingcomputer.com/news/security/hunters-international-ransomware-gang-targets-it-workers-with-new-sharprhino-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?7gTW9WIU)

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