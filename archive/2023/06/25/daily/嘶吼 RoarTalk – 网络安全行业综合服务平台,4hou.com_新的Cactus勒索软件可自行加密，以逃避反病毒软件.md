---
title: 新的Cactus勒索软件可自行加密，以逃避反病毒软件
url: https://www.4hou.com/posts/RKO0
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-25
fetch_date: 2025-10-04T11:44:16.298741
---

# 新的Cactus勒索软件可自行加密，以逃避反病毒软件

新的Cactus勒索软件可自行加密，以逃避反病毒软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的Cactus勒索软件可自行加密，以逃避反病毒软件

布加迪
[新闻](https://www.4hou.com/category/news)
2023-06-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)143855

收藏

导语：一个名为Cactus的新型勒索软件团伙一直在利用VPN设备中的漏洞，对“大型商业实体”的网络进行初始访问。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687331667136203.png "1683511791355754.png")

一个名为Cactus的新型勒索软件团伙一直在利用VPN设备中的漏洞，对“大型商业实体”的网络进行初始访问。

至少从今年3月开始，Cactus勒索软件团伙就一直处于活跃的状态，并向受害者索要大笔赎金。

虽然这伙新的威胁分子采用了勒索软件攻击中两种常见的策略：文件加密和数据窃取，但它增添了自己的手法以免被发现。

**加密配置花招**

Kroll企业调查和风险咨询公司的研究人员认为，Cactus通过利用飞塔（Fortinet）VPN设备中的已知漏洞，获得了进入受害者网络的初始访问权限。

这番结论基于以下观察结果：在调查的所有事件中，黑客都是从拥有VPN服务帐户的VPN服务器转而进入内部的。

Cactus与其他团伙的不同之处在于，它使用加密来保护勒索软件二进制文件。威胁分子使用批处理脚本，借助7-Zip获取加密器二进制文件。

原始的ZIP压缩包被删除，并使用允许其执行的特定标志部署二进制文件。整个过程不同寻常，研究人员表示这是为了防止勒索软件加密器被检测出来。

Kroll调查人员在一份技术报告中解释道，有三种主要的执行模式，每种模式都是通过使用特定的命令行参数选项符来选择的：设置（-s）、读取配置（-r）和加密（-i）。

-s参数和-r参数允许威胁分子实现持久性，并将数据存储在C:\ProgramData\ntuser.dat文件中，该文件稍后由加密器在使用-r命令行参数运行时读取。

不过，为了使文件加密成为可能，必须使用-i命令行参数，提供只有攻击者才知道的独特的AES密钥。

该密钥对于解密勒索软件的配置文件和加密文件所需的公共RSA密钥必不可少。它其实就是加密器二进制文件中硬编码的十六进制（HEX）字符串。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687331668319919.png "1683511807188912.png")

图1. 加密Cactus勒索软件配置的十六进制字符串（图片来源：Kroll）

解码十六进制字符串提供了一段用AES密钥解锁的加密数据。

Kroll网络风险副总经理Laurie Iacono告诉IT安全外媒Bleeping Computer：“CACTUS实际上对自己进行加密，使其更难被检测出来，并帮助它逃避反病毒和网络监控工具。”

如果使用-i（加密）参数来运行二进制文件（拥有正确的密钥），可解锁信息，并允许恶意软件搜索文件，启动多线程加密过程。

Kroll的研究人员提供了下面的示意图，以便更好地解释Cactus二进制文件根据所选的参数来执行的过程。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687331669297838.png "1683511818296262.png")

图2. Cactus勒索软件二进制文件的执行流程（图片来源：Kroll）

勒索软件专家Michael Gillespie也分析了Cactus加密数据的方式，他告诉BleepingComputer，该恶意软件可以根据处理状态对目标文件使用多个扩展名。

在准备加密文件时，Cactus将其扩展名更改为.CTS0。加密后，扩展名就变为了.CTS1。

然而Gillespie解释道，Cactus也可以有“快速模式”，类似进行一轮轻加密。在快速模式和正常模式下连续运行恶意软件会导致对同一文件进行两次加密，并在每个过程之后附加一个新的扩展名（比如.CTS1.CTS7）。

Kroll表示，.CTS扩展名末尾的数字在多起可以追溯到Cactus勒索软件的事件中有所不同。

**Cactus勒索软件的战术、技术和程序（TTP）**

一旦进入到了网络，威胁分子使用计划任务进行持久访问，使用可以从指挥和控制（C2）服务器访问的SSH后门。

据Kroll调查人员声称，Cactus依靠SoftPerfect网络扫描器（netscan)在网络上寻找有价值的目标。

为了进行更深入的侦察，攻击者使用PowerShell命令来枚举端点，通过在Windows事件查看器中查看成功登录来识别用户帐户，并ping远程主机。

研究人员还发现，Cactus勒索软件使用了开源软件PSnmap工具的修改版本，这是相当于PowerShell版的nmap网络扫描器。

调查人员表示，为了启动攻击所需的各种工具，Cactus勒索软件通过合法工具（比如Splashtop、 AnyDesk和SuperOps RMM）以及Cobalt Strike和基于Go的代理工具Chisel，尝试多种远程访问方法。

Kroll调查人员表示，在提升机器上的权限后，Cactus团伙成员运行批处理脚本，从而卸载最常用的反病毒产品。

与大多数勒索软件团伙一样，Cactus也会窃取受害者的数据。在此过程中，威胁分子使用Rclone工具将文件直接传输到云存储系统。

在窃取数据后，黑客使用了一个名为TotalExec的PowerShell脚本来自动部署加密过程，该脚本经常出现在BlackBasta勒索软件攻击中。

Gillespie告诉我们，Cactus勒索软件攻击中的加密程序是独一无二的。尽管如此，这似乎并不是Cactus所特有的，因为最近BlackBasta勒索软件团伙也采用了类似的加密过程。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687331670185257.png "1683511842168127.png")

图3. Cactus勒索软件的TTP（图片来源：Kroll）

目前还没有关于Cactus向受害者索要赎金的公开信息，但有知情人士告诉BleepingComputer，赎金高达数百万美元。

即使黑客确实窃取了受害者的数据，他们似乎也没有像其他从事双重勒索活动的勒索软件团伙那样建立数据泄露网站。

然而，威胁分子确实威胁受害者：除非他们拿到赎金，否则将公布被盗文件。这在勒索函中很明确：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230621/1687331671132731.png "1683511855154721.png")

图4. Cactus勒索函威胁要公布被盗数据（图片来源：Kroll）

Cactus团伙、目标受害者以及黑客在拿到赎金后是否遵守诺言并提供可靠的解密器，这些方面的大量细节目前还不得而知。

目前清楚的是，黑客的入侵到目前为止很可能利用了飞塔VPN设备中的漏洞，采用了标准的双重勒索方法，在加密数据之前窃取数据。

组织应该部署飞塔的最新软件更新，监控网络中的大型数据泄露任务，并快速响应，这应该可以保护组织免受勒索软件攻击的最后、最具破坏性的阶段。

本文翻译自：https://www.bleepingcomputer.com/news/security/new-cactus-ransomware-encrypts-itself-to-evade-antivirus/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?w4jmjWHE)

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