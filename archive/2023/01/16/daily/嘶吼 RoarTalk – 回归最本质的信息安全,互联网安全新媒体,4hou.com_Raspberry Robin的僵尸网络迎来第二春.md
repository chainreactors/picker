---
title: Raspberry Robin的僵尸网络迎来第二春
url: https://www.4hou.com/posts/nJw7
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-16
fetch_date: 2025-10-04T03:59:12.492443
---

# Raspberry Robin的僵尸网络迎来第二春

Raspberry Robin的僵尸网络迎来第二春 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Raspberry Robin的僵尸网络迎来第二春

布加迪
[新闻](https://www.4hou.com/category/news)
2023-01-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)1012689

收藏

导语：SEKOIA.IO的分析师通过本文演示了Raspberry Robin与许多僵尸网络和蠕虫一样，可以被其他威胁分子稍加改动，以部署自己的植入程序。

我们在2022年3月首次报告QNAPWorm后，这种恶意软件以Raspberry Robin之名登上了媒体头条。从那以后，微软、Secureworks和Avast等几家安全供应商调查了这种恶意软件，认为它与臭名昭著的俄罗斯网络犯罪团伙EvilCorp有关，这个团伙对Dridex木马及其他恶意软件以及至少自2014年以来的几次以牟利为目的的高调活动负责。

**Raspberry Robin简介**

先简单介绍一下，Raspberry Robin是一种恶意软件，通过受感染的U盘下载，还可能通过网络共享下载。攻击想法很简单：受感染的设备含有LNK文件（Windows快捷方式）。用户插入U盘、启动伪装成U盘或网络共享的LNK后，它会启动Windows实用程序msiexec。

一旦执行，由于参数中指定的URL, msiexec随后会从受攻击的QNAP实例中下载在MSI（Windows安装包）中打包的Raspberry Robin的主组件。这个过程可以用下图来表示：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230113/1673559737161210.png "1673559737161210.png")

图1

Raspberry Robin的主组件是一个复杂的恶意软件变种，SEKOIA.IO的分析师在2022年初曾试图进行逆向工程分析，但未能如愿以偿。据Avast的研究显示，它有14层混淆机制，使用TOR聚合（rendez-vous）进行通信，并使用创新的方法在受攻击系统上保持不被检测出来。只有几个特别之处让防御者得以揪出网络中的Raspberry Robin，比如所投放文件的文件扩展名、与可供辨别的URL模式相关的MSI执行、rundll32参数或从特定工作站连接到TOR节点。

正如我们的少数客户最初假设的那样，Raspberry Robin似乎是一种按安装付费的僵尸网络，很可能被网络犯罪分子用来在受感染传统上传播其他恶意软件，比如挖币软件以及其他后门程序（比如SocGholish、Bumblebee、TrueBot或IcedID），这些最终导致需要操作键盘（hands-on-keyboard）的勒索软件部署。

去年，SEKOIA.IO的分析师观察到Raspberry Robin在多个场合部署SocGholish。SocGholish是微软JScript验证器，通过借助恶意广告活动的网络浏览器虚假更新来广泛部署。然而在这些场合下，Raspberry Robin在知名的客户网络中完成MSI执行后，SocGholish直接部署，如下图所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230113/1673559749147815.png "1673559749147815.png")

图2

微软研究人员报告遇到了一条类似的感染链，并声称这些SocGholish实例导致通过C2框架在网络内部横向移动，然后是需要操作键盘的勒索软件部署。在SEKOIA.IO的分析师确认的场合下，感染在SocGholish执行阶段就停止了，因为它被反病毒引擎检测了出来。

**Raspberry Robin基础设施**

自我们的第一份网络威胁情报Flash报告（FLINT）发布之后，我们决定将研究重点放在msiexec联系以下载含有Raspberry Robin主组件的恶意MSI包的基础设施上。从第一份FLINT发现的十几个域名开始，我们在2022年底检索到自2021年7月该僵尸网络创建以来这种入侵手法使用了270多个域名。

Raspberry Robin使用通过域名解析的受攻击的QNAP网络附加存储（NAS），作为其第一个C2级别。每个受攻击的QNAP似乎都充当了验证器和转发器。如果收到的请求有效，请求被重定向到基础设施的上层。

感谢CYMRU S2团队的同仁，我们得以发现了基础设施的第二层。这层由至少8个VPS组成，托管在Linode上。SEKOIA.IO的分析师估计，这些VPS很可能被用作转发代理，转发到基础设施的下一层。然而截止本文发稿时，我们无法确定这下一层。这些VPS有相同的配置，其中两个VPS由受攻击的QNAP通过端口20001来联系。SEKOIA.IO的分析师认为它们与同一套基础设施有关联，把握很大。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230113/1673559769133996.png "1673559769133996.png")

图3

在调查过程中，在通过QNAP配置和相关的\*.myqnapcloud.com域名识别出其中一家受攻击的组织后，我们还考虑使用物理设备（比如与Raspberry Pi）来复制法国境内其中一个受攻击的QNAP的流量。即使确定了受害者的身份，并成功联系上了对方，我们观察到攻击者没过几天就丢弃了这个受攻击的QNAP实例：解析这个QNAP实例的所有域名转而解析其他受攻击的QNAP实例。

这是Raspberry Robin的一个特别之处：其基础设施的域名解析不断变化，从一个受攻击的QNAP变成另一个。每天都完成几十次新的解析，新的受攻击QNAP每天都在出现，从运营团伙的角度来看，这减少了它被察觉的风险。

下图显示了基础设施在2022年12月15日至2022年12月31日期间的变化。在此期间，有80个新的QNAP实例受攻击，活动域名对DNS解析进行了1154次更改。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230113/1673559783164510.png "1673559783164510.png")

图4

**局部端掉**

值得注意的是，在2022年10月26日，该僵尸网络被局部端掉，导致通过namecheap.com注册的大约80个域名被停用，这些域名约占Raspberry Robin使用的域名总量的30%。这些域名的DNS区域被删除，标记clientHold和clienttransferbanned被添加到了状态码中，导致僵尸网络运营团伙完全不知所措。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230113/1673559803125431.png "1673559803125431.png")

图5

**Raspberry Robin迎来第二春**

已发现的Raspberry Robin蠕虫的弱点之一是依赖msiexec下载和执行主载荷，并没有实施控制机制来确保载荷来自可信来源。因此，任何能够劫持msiexec执行的请求的人都可以让受害者下载另一个非法的MSI载荷。这主要可以通过DNS劫持攻击来实现，比如QUANTUM DNS，或者只要在域名过期后购买与该威胁相关的域名就能实现。

由于大约有数千只U盘被Raspberry Robin污染，SEKOIA.IO的分析师猜想，即使在域名过期后，这个威胁几乎肯定会继续处于活跃状态，可能导致这个僵尸网络迎来第二春，被其他网络犯罪分子另作他用。

为了证明这个假设，我们试图将恶意LNK用来下载和执行MSI包的其中一个首批域名的流量引到sinkhole服务器。我们的研究侧重于tiua[.]uk和gloa[.]in，这两个域名都是在2021年7月26日Raspberry Robin活动的最初几天注册的。

几个月前，我们很幸运，那时域名tiua[.]uk可供出售。这个域名在2021年9月22日至2022年11月30日期间被用作C2，直到英国域名注册中心暂停了它，可能是由于注册人联系信息不准确。

通过将这个域名指向我们的sinkhole服务器，我们得以从Raspberry Robin运营团伙使用的首批域名之一获得遥测数据。果然不出我们所料，由于它是这个蠕虫使用的首批域名之一，这个特定域名的遥测数据很有限。此外，指向该域名的快捷方式来自第一代分布式LNK，因此可以被如今的大多数反病毒解决方案检测出来。

然而，我们仍能够观察到几个受害者，这表明在Raspberry Robin域名创建一年后，仍然有可能对这个域名稍加改动，用于从事恶意活动。果不其然，我们还发现了几只U盘从一台计算机传递到另一台，这表明单单一个LNK就可能感染多台计算机。

值得一提的是，由于受攻击的组织或特定行业部门在互联网服务提供商自治系统中使用通用IP地址，因此识别它们特别复杂。SEKOIA.IO之所以能够识别出一所欧洲大学的管理网络，是由于Via: HTTP报头中泄露了其内部代理。

我们试图对所有这些感染绘制一张图，以验证Raspberry Robin的这些首批受害者是否来自特定的国家，常常可以从RETADUP等USB蠕虫观察到这种情况。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230113/1673559822115991.png "1673559822115991.png")

图6

值得一提的是，首批感染并非出现在世界上的某个特定地区。不像RETADUP或其他USB蠕虫，Raspberry Robin的传播器（spreader）并不嵌入在主载荷中，而是充当独立的可执行文件，它可以自动执行，也可以由攻击者通过操作键盘来执行。SEKOIA.IO的分析师估计，首批Raspberry Robin USB感染很可能是手动完成的，依赖其他恶意软件和初始访问。我们进一步评估，Raspberry Robin运营团伙可能使用了另一个僵尸网络来传播该蠕虫的第一个版本。微软发现的Raspberry Robin . net传播器可以证实这个假设。

在这次研究期间，SEKOIA.IO的分析师将僵尸网络使用的另一个域名ynns[.]uk引到了sinkhold服务器，它也被英国域名注册中心封禁。因此，它解析受攻击的QNAP C2不到一个月，即从2021年10月25日到2021年11月19日。这个域名让我们得以识别另外几个国家的受害者，包括美国、德国、罗马尼亚、阿曼、摩洛哥、巴林和哈萨克斯坦。

那么，下一步是什么？

本文阐明了僵尸网络如何有多个用途，如何可以被其运营团伙重用及/或改造，甚至久而久之被其他团伙劫持。正如最近Mandiant披露TURLA团伙稍加改动Andromeda僵尸网络的几个域名那样，稍加改动僵尸网络和访问（比如webshell）不是什么新鲜事，威胁分子在过去早已有了这么做的能力。

这进一步增强了SEKOIA.IO分析师的信心：必须持续监测、调查和重新评估该威胁，以提供实用的网络威胁情报。

除了将威胁记入文档外，创建定制规则以检测Raspberry Robin生成的LNK或在网络外通信的msiexec进程似乎至关重要。到目前为止，尽管多家安全供应商针对这两方面提供了强大的检测，SEKOIA.IO的分析师估计，Raspberry Robin运营团伙可能会更新感染链以逃避检测，在中长期内继续攻击全球各地的组织。

因此，SEKOIA.IO的分析师会继续监测和报告这个威胁，将其作为值得关注的网络犯罪案例加以跟踪研究。

本文翻译自：https://blog.sekoia.io/raspberry-robins-botnet-second-life/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?awnhAUH8)

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
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/p...