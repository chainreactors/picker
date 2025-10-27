---
title: 勒索攻击和数据擦除攻击的证书签名都是哪来的？
url: https://www.4hou.com/posts/LBor
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-10
fetch_date: 2025-10-04T06:12:12.290128
---

# 勒索攻击和数据擦除攻击的证书签名都是哪来的？

勒索攻击和数据擦除攻击的证书签名都是哪来的？ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索攻击和数据擦除攻击的证书签名都是哪来的？

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-02-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)127440

收藏

导语：我们将比较和讨论第一波和第二波勒索程序和擦除式恶意程序之间的区别。

![abstract-binary-code-ok-signed-sl-1200.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675909618128759.jpeg "1672596044171985.jpeg")

2022年7月17日，阿尔巴尼亚新闻媒体报道了一次大规模网络攻击，该攻击影响了阿尔巴尼亚政府的电子政务系统。后来经过调查，这些网络攻击是一个威胁活动的一部分，其目的可能是瘫痪该国的计算机系统。2022年9月10日，阿尔巴尼亚当地新闻报道了针对阿尔巴尼亚TIMS、ADAM和MEMEX系统的第二波网络攻击。

大约在同一时间，我们发现了勒索程序和擦除程序样本与第一波中使用的类似，尽管有一些有趣的修改，可能允许规避安全控制和提高攻击速度。在这些变化中，最主要的是嵌入一个原始磁盘驱动程序，在恶意程序内部提供了直接的硬盘访问，修改了元数据，并使用Nvidia泄露的代码签名证书对恶意程序进行签名。

在这篇文章中，我们介绍了：

1.用于针对阿尔巴尼亚个机构的第一波和第二波勒索程序和擦除式恶意程序，并详细说明了与之前已知的ROADSWEEP勒索程序和ZEROCLEARE变体的联系。

2.攻击者使用英伟达(Nvidia)和科威特电信公司(Kuwait Telecommunications Company)的证书来签署他们的恶意程序，前者已经泄露，但我们不确定他们是如何得到后者的。

3.我们发现了使用不同语言的不同攻击组织之间的潜在合作关系，以及可能使用AnyDesk作为启动勒索程序/擦除攻击感染的初始入口点。

4.在第二波攻击中实现自动化和加速擦拭的变化让人想起中东臭名昭著的Shamoon擦除攻击攻击。

下面，我们将比较和讨论第一波和第二波勒索程序和擦除式恶意程序之间的区别。

**初始感染——不同攻击组织之间合作关系和使用AnyDesk实用程序的证据**

虽然我们无法在分析的攻击中确定攻击者的初始入口点，但在第二波攻击后的几天，我们注意到有攻击者可以访问另一个非政府但重要的阿尔巴尼亚机构的AnyDesk帐户，并建议说波斯语的黑客使用它来部署勒索程序或清除恶意程序。由此我们推测，第二波攻击的初始入口点是通过合法的远程访问程序(如AnyDesk)，特别是使用的擦除攻击修改仅限在驱动程序安装时自动执行，由于时间/访问窗口有限，可能需要紧急执行。攻击者和访问提供者似乎属于不同的攻击组织，使用不同的语言。

使用科威特电信公司签名证书的勒索程序如下所示：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675909619271558.png "1672596062253667.png")

第二波样本与第一波样本具有相同的签名证书参数，该样本与科威特电信公司有关。目前尚不清楚攻击者如何能够使用科威特电信公司的证书签署其恶意程序，但我们怀疑它是被盗的。在本文发布时，该证书已不再有效并已被撤销。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675909620147400.png "1672596074625635.png")

在初始执行后，第二波勒攻击中使用的索程序检查攻击者提供的任意六个或更多参数，而第一波样本则检查五个参数或更多，这是一个有助于防御逃避检测的小修改。然而，在一台受影响的计算机上进行的攻击分析表明，在第二波攻击中，攻击者在提供类似于第一波攻击的七位数时，没有使用BAT文件调用勒索程序，而是使用六个零“000000”从命令行立即调用第二波攻击中使用的勒索程序。如果由于没有提供正确的参数而导致勒索程序执行失败，则第二波攻击示例将显示与第一波攻击不同的消息，第二波攻击消息类似于由PDF到DOC转换器显示的错误消息。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675909622129129.png "1672596090636580.png")

第一波攻击示例，执行失败后的消息

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675909624211684.png "1672596107114888.png")

第二波攻击示例，执行失败后的不同消息

第二波攻击勒索程序样本继续执行并检查互斥锁Screenlimitsdevices#77!;，这个值与第一波攻击样本的互斥锁不同：

abcdefghijklmnoklmnopqrstuvwxyz01234567890abcdefghijklmnopqrstuvwxyz01234567890

尽管我们根据其行为将这种恶意程序称为勒索程序，但加密文件实际上是无法恢复的。当比较第二波勒索程序样本和第一波勒索程序样本时，我们注意到两者都有相同的，并且都使用CreateFile和WriteFile api来覆盖文件。在执行过程中，第二波攻击勒索程序试图解密并执行嵌入式脚本、恶意程序设置或API函数名。在第一波攻击和第二波攻击中使用的加密算法都是RC4。但是，在第二波中用于解密的RC4密钥已被更改，这是另一种逃避检测的尝试。

第一波攻击中的RC4密钥：8C E4 B1 6B 22 B5 88 94 AA 86 C4 21 E8 75 9D F3

第二波攻击中的RC4密钥：F0 B4 ED D9 43 F5 C8 43 C9 D0 A2 4F 22 9B BC 3A

值得注意的是，在这两波攻击中，RC4解密方法都使用CryptoAPI (CryptDecrypt)而不是通常的S盒方法。在密码学中，S盒(Substitution-box)是对称密钥算法执行置换计算的基本结构。S盒用在分组密码算法中，是唯一的非线性结构，其S盒的指标的好坏直接决定了密码算法的好坏。对第二波分析表明，勒索程序可能是通过内部网络部署的，可能来自另一台受感染的设备。在勒索程序执行之前，我们没有看到任何其他东西被删除或执行，并且勒索程序可执行文件名称是随机生成的，这可能是由攻击者用来通过网络部署它的工具(例如Mellona.exe)生成的。

尽管在第二波勒索程序与第一波攻击中的完全不同，但勒索信的功能仍然保持了下来，包括反映阿尔巴尼亚和伊朗之间地缘政治紧张局势的政治信息。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675909625163225.png "1672596125157652.png")

第一波和第二波勒索程序中的勒索信

**使用Nvidia签名证书的擦除攻击**

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675909626163102.png "1672596146700559.png")

与第二波攻击勒索程序样本类似，攻击者对第二波攻击擦除程序进行了几次修改，可能是为了逃避检测。变化主要有三个：

修改的恶意程序签名；

在擦除程序中嵌入EldoS RawDisk驱动程序；

驱动安装后自动擦除命令；

在2019年的ZEROCLEARE（ZeroCleare和恶意程序Shamoon同宗，都是出自伊朗资助的顶级黑客组织之手）和DUSTMAN（该程序以删除设备的数据为目的，瞄准的是中东的能源和工业部门）事件中，擦除程序和原始磁盘驱动程序均没有签名，因此无法直接访问原始磁盘进行快速数据擦除。因此，擦除攻击器必须使用第三方加载器，如TDL(用于无签名驱动程序的签名加载器)来安装无签名原始磁盘驱动程序，允许擦除程序直接访问原始磁盘，使用DeviceControl API方法擦除数据。然而，在针对阿尔巴尼亚的第一波攻击中，攻击者使用科威特电信公司的证书对第一波攻击擦除攻击进行了签名，从而消除了对第三方加载器的需求。速度和自动化的改进让我们想起了之前在中东的Shamoon攻击。

由于第一波攻击使用的擦除程序是在2022年7月被曝光的，而且可能会避免静态检测，攻击者在2022年9月使用英伟达泄露的签名证书对第二波攻击使用的擦除程序进行了签名，再次取消了对原始磁盘驱动程序的第三方加载器的需求。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675909627463382.png "1672596161170965.png")

在第一波攻击中，擦除程序希望在执行目录或系统目录中找到原始磁盘驱动程序。但驱动程序并没有被擦除，攻击者可能用了其他方法。相反，在第二波攻击中，攻击者将签名的原始磁盘驱动程序嵌入到擦除攻击可执行文件中，先删除它，然后安装。此外，第二波中攻击者使用的驱动程序似乎复制了微软的diskdump.sys崩溃转储驱动程序（版本10.0.19041.682）中的元数据和一些函数，作为避免检测的另一种方法。驱动程序安装命令后擦除活动自动启动，与第一波攻击擦除攻击不同，安装是第一步，执行擦拭是第二步。

不过在大多数情况下，第一波攻击和第二波攻击的擦除程序是一样的，包括依赖相同的身份验证密钥来访问原始磁盘驱动程序，以及使用相同的DeviceControl API方法，但有一个例外，如下所示。值得注意的是，IOCTL\_DISK\_GET\_LENGTH\_INFO方法仅适用于讲波斯语的APT攻击。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675909627196807.png "1672596176483722.png")

我们怀疑攻击第二波攻击目标是阿尔巴尼亚的执法机构，因为它与2022年7月网络攻击浪潮中针对阿尔巴尼亚政府的网络攻击一致。

**总结**

我们在本文讨论了针对阿尔巴尼亚各机构的第二波勒索和擦除攻击样本的变化，其最终目的都是逃避检测并造成最大损失。

除了在第二波中为逃避检测所做的更改外，我们怀疑攻击者需要一个自动和快速的擦除攻击执行。在第二波攻击中，原始磁盘驱动程序被嵌入到恶意程序中，并且在驱动程序安装后立即启动擦除程序，这与第一波攻击的过程相反。

最后，对于防御者来说应从以下两方面入手进行防御：

监控远程程序活动(如AnyDesk)情况，以防未经授权使用；

始终寻找和监控过期或泄露的签名证书，因为攻击者可以使用它们来加载和执行恶意程序。

本文翻译自：https://securelist.com/ransomware-and-wiper-signed-with-stolen-certificates/108350/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Yxi0nQal)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

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

[查看更多](https://www.4hou.com/member/bo2j)

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

[公司简介](https:/...