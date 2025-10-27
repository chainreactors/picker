---
title: 最新出现的CatB勒索软件采用2年前的DLL劫持技术来逃避检测
url: https://www.4hou.com/posts/50Y8
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-13
fetch_date: 2025-10-04T03:44:20.546145
---

# 最新出现的CatB勒索软件采用2年前的DLL劫持技术来逃避检测

最新出现的CatB勒索软件采用2年前的DLL劫持技术来逃避检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 最新出现的CatB勒索软件采用2年前的DLL劫持技术来逃避检测

gejigeji
[技术](https://www.4hou.com/category/technology)
2023-01-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)141683

收藏

导语：最新发现的勒索软件CatB，该软件通过处理器内核检查，物理内存大小检查和硬盘大小来检查自己是否是在虚拟机中，然后执行MSDTC 服务的DLL劫持绕过杀毒软件。

![微信截图_20230104102636.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672800987167826.png "1672800987167826.png")

最新发现的勒索软件CatB，该软件通过处理器内核检查，物理内存大小检查和硬盘大小来检查自己是否是在虚拟机中，然后执行MSDTC 服务的DLL劫持绕过杀毒软件。

我们最近发现了一个新型勒索软件，它执行MSDTC服务DLL劫持以静默执行其有效负载。我们根据勒索软件组使用的联系电子邮件将此勒索软件命名为CatB。该样本于2022年11月23日首次上传至VT，并被VT社区标记为Pandora勒索软件的可能变体。Pandora组织首次出现于2022年2月中旬，主要以企业网络为目标进行针对性攻击，主要通过钓鱼邮件、漏洞利用、RDP爆破等方式进行传播，采用Raas双重勒索的策略，在对用户系统进行加密导致工作无法正常运作的情况下，利用窃取的数据胁迫用户支付赎金，否则就外泄。该组织使用Tor站点或者Email邮箱方式与受害者联系。

Pandora 勒索软件最重要的功能就是应用了先进的反逆向技术，虽然在恶意软件中反逆向技术很常见，但Pandora的这一功能颇为突出。与潘多拉勒索软件的联系仅限发出的勒索信。CatB勒索软件实现了几种反虚拟机技术，以验证在真实设备上的执行情况，然后释放恶意DLL和劫持DLL以逃避检测。

CatB勒索软件包含两个文件，包含UPX的 dropper (version.dll)和勒索软件有效负载(oci.dll)。 dropper处理反vm检查，释放勒索软件负载并执行它。

**反虚拟机（Anti-VM）**

CatB dropper实现了三种反虚拟机/沙盒规避技术：

处理器内核检查：现如今的真实计算机都至少有两个处理器，所以如果勒索软件只检测到一个CPU内核，这将是一个很强的信号，表明它当前驻留在沙盒中。勒索软件通过GetSystemInfo API函数检索系统信息并检查处理器数量。如果少于两个处理器，则退出立即中断执行。

![figure-1-check-number-of-processors.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801009176671.jpeg "1672801009176671.jpeg")

处理器检查

总物理内存检查：与虚拟机不同，现在的虚拟机都至少有2GB RAM，通常在4GB和32GB之间。CatB勒索软件通过检查物理内存大小来检测虚拟机/沙盒。这是通过使用GlobalMemoryStatusEx API函数检索有关物理和虚拟内存的信息来完成的。在本文的示例中，如果即将运行的物理内存少于2GB，勒索软件会退出。

![figure-2-RAM-check.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801027207771.jpeg "1672801027207771.jpeg")

物理内存检查

硬盘大小：恶意软件可以检查设备的硬盘大小，并根据该参数继续执行。这可以通过使用DeviceIoControl Api函数实现，其中“0x70000”作为dwIoControlCode参数传递。CatB勒索软件只能在至少有50GB硬盘的设备上执行。

![figure-3-anti-vm-disk-size.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801044199500.jpeg "1672801044199500.jpeg")

硬盘大小检查

**DLL劫持**

如果所有反VM检查都通过，则 dropper将继续执行，并将勒索软件负载（oci.dll）放入C:\Windows\System32文件夹。接下来，它将查找MSDTC服务（分布式事务协调器Windows服务，负责协调数据库（SQL Server）和web服务器之间的事务）并更改其配置。

![figure-4-open-service.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801062649781.jpeg "1672801062649781.jpeg")

MSDTC服务

更改的配置包括运行服务的帐户名称（从“网络服务”更改为“本地系统”）和服务启动选项（如果重新启动，则从“按需启动”更改为自动启动以实现持续性）。

![figure-5-services.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801079201536.jpeg "1672801079201536.jpeg")

服务配置更改

运行服务的帐户已更改为授予服务管理员权限，因为网络服务帐户使用用户权限运行。更改启动类型将授予勒索软件在每次系统重新启动时执行的能力。

dropper在更改其配置后启动服务。此服务启动时，默认情况下会尝试从System32文件夹加载几个DLL。这使它有机会将任意DLL（在本例中为oci.DLL）植入此文件夹中，以执行恶意代码。

**勒索软件**

此时恶意oci.dll文件被加载到msdtc.exe进程中，然后加密进程启动。CatB枚举并加密特定的硬编码磁盘和文件夹：

![6.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801095401462.png "1672801095401462.png")

![6.2.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801105800365.jpeg "1672801105800365.jpeg")

硬编码磁盘

CatB避免使用带有.msi、.exe、.dll、.sys、.iso扩展名和NTUSER.DAT的文件。CatB勒索软件的一个有趣之处是，勒索通知被添加到每个加密文件的开头，而不是像大多数勒索软件那样作为一个单独的文件添加到每个文件夹中。它也不改变文件扩展名。这可能会在一开始使用户感到困惑，他们可能没有注意到加密，并且文件将看起来已经被攻击，因为二进制内容被破坏，他们无法打开它。勒索通知本身看起来与Pandora和Crypt赎金通知非常相似，其中一部分甚至是复制/粘贴的。

![7.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801122471670.jpeg "1672801122471670.jpeg")

加密文件

通知中没有官方的赎金名称，也没有tor网站的URL。联系勒索软件运营商的唯一方法是通过电子邮件。

目前像Minerva Armor这样的勒索软件保护平台会通过模拟勒索软件积极试图避免的环境数据，轻松防止CatB勒索软件。例如，当勒索软件查询处理器的数量时，Minerva Armor会让它相信自己所处的环境只有1个CPU，从而自动退步并终止运行。

![8.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801145177831.jpeg "1672801145177831.jpeg")

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672801170167654.png "1672801170167654.png")

本文翻译自：https://minerva-labs.com/blog/new-catb-ransomware-employs-2-year-old-dll-hijacking-technique-to-evade-detection/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KssrHJYb)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/FpAB1n2wt6I0zw18n_Sz-3Nj9Ctg)

# [gejigeji](https://www.4hou.com/member/mqy0)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/mqy0)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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