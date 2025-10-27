---
title: 攻击者试图窃取AWS EC2的访问密钥和令牌
url: https://www.4hou.com/posts/zlg5
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-05
fetch_date: 2025-10-03T21:44:29.211160
---

# 攻击者试图窃取AWS EC2的访问密钥和令牌

攻击者试图窃取AWS EC2的访问密钥和令牌 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者试图窃取AWS EC2的访问密钥和令牌

luochicun
[新闻](https://www.4hou.com/category/news)
2022-11-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)168213

收藏

导语：作为防御者，我们需要了解攻击者在进入后的目标是什么，以及需要使用哪些方法来禁用、解除和遏制这些威胁。

趋势科技的研究人员最近发现了一个恶意程序，它试图通过拼写错误和滥用合法工具窃取Amazon Elastic Compute Cloud（EC2）Workload的访问密钥和令牌。

最近，研究人员遇到了一个利用监控和可视化工具Weave Scope的攻击尝试，它通过环境变量和IMDS终端从Elastic Compute Cloud(EC2)实例中枚举Amazon Web Services(AWS)实例元数据服务(IMDS)。Weave Scope是 Docker 和 kubernetes 可视化监控工具。Scope提供了至上而下的集群基础设施和应用的完整视图,用户可以轻松对分布式的容器化应用进行实时监控和问题诊断。滥用此工具可以将访问密钥和令牌泄露到攻击者可能拥有的域，并在aws拥有的域amazonaws.com上使用一种过时的技术，称为误植域名（Typosquatting）。

误植域名（Typosquatting），也称作URL劫持，假URL等，是一种域名抢注的形式，常常会导致品牌劫持。这种劫持的方式通常有赖于用户在浏览器中输入网址时，犯下诸如错误拼写等错误。用户一旦不小心输入了一个错误的网址，便有可能被导向任何一个其他的网址（比如说一个域名抢注者运营的网站）。

接下来使用masscan和zgrab来查找Weave Scope用户界面(UI)实例，并导出找到的IP地址和端口。研究人员建议用户加强、强化和定制各自的云安全策略、以开发人员为中心的工具和措施，以缓解威胁和攻击带来的危害。

**执行流程**

我们以前曾报道过合法工具的滥用，特别是滥用Weave Scope，以达到攻击的目的。在这个针对我们的蜜罐的尝试中，我们观察到攻击者通过一个公开的Docker REST API服务器获得了攻击入口，众所周知，这是由TeamTNT等攻击者利用的。

在这个示例中，攻击者创建了一个容器，并将底层主机的根目录挂载到容器中的路径。之后，在创建容器时执行名为init.sh的脚本，即使没有提供任何其他命令来执行。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928265185433.png "1666928265185433.png")

环境变量是为从执行的init.sh脚本中产生的子进程设置的

HOME环境变量被设置为/root，这样来自该脚本的其他进程将认为/root目录是HOME变量。命令历史记录不会被记录，之后环境变量本身也会被删除。PATH变量还包含路径，设置了特定于语言本地化的参数，以强制语言在整个脚本执行进程中保持一致。

之后，使用Alpine Package Keeper或apk安装某些使攻击者脚本能够执行的工具，以便在基于Alpine的容器映像的基础映像中安装wget、curl、jq、masscan、libpcap dev和docker。声明以下两个变量：

1.SCOPE\_SH，安装Weave SCOPE的Base64编码字符串；

2.WS\_TOKEN，一种可用于将主机包括在 fleet中的秘密访问令牌；

**脚本函数**

在分析脚本时，我们观察并分解了为攻击中的各种实现设计的四个函数：main、wssetup、checkkey和getrange。

**main**

main函数依次调用其他三个函数。最初，nohup执行Docker守护进程(dockerd)以保持进程在退出shell后仍在运行。流STDOUT和STDERR通过管道传输到/dev/null，以在执行时在屏幕上显示任何输出。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928274113353.png "1666928274113353.png")

main函数

**wssetup**

此函数使用实用程序base64解码变量SCOPE\_SH的内容。wssetup还静默地执行命令行 scope launch –service-token=$WS\_TOKEN，使主机成为攻击者Weave scope fleet的一部分。

早些时候，我们观察了Docker REST API的利用，其中范围令牌是从攻击者的基础设施中获取的。然而，在本例中，令牌本身是在脚本中硬编码的。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928284534351.png "1666928284534351.png")

函数wssetup

**checkkey**

此函数检查文件“/host/root/.aws/credentials”。有趣的是，容器中的path /host映射回主机上的根目录“/”。如果文件存在，则通过curl请求将其发送到攻击者的终端。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928292661124.png "1666928292661124.png")

函数checkkey

如果该函数在本地文件系统和远程文件共享(Mitre ID T1552.001非安全凭据：文件中的凭据)中没有找到凭据，则使用curl或wget查询IMDS终端是否可用。通过一系列grep和sed操作处理输出，并将输出累积在隐藏文件“.iam”和“.ec2”（Mitre ID T1564.001隐藏工件：隐藏文件和目录)。

收集完凭据后，将它们合并到一个名为“.aws”的隐藏文件中，并用两行新行分隔，同时删除原始文件。稍后，通过“AWS”或“EC2”搜索每个进程的环境变量，并将其添加两行附加到文件“.AWS”中。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928303155359.png "1666928303155359.png")

在每个进程的环境变量中搜索AWS或EC2

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928312139230.png "1666928312139230.png")

泄漏收集的凭据

**getrange和rangescan**

这个函数有一个参数RANGE，它稍后会被传递给另一个名为rangescan的函数。第二个功能使用zgrab扫描RANGE中的IP地址，以便在端口80、443和4040 (Weave Scope UI使用的默认端口)上访问Weave Scope UI。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928321137188.png "1666928321137188.png")

函数getrange和rangescan

我们的观察表明，getrange没有提供任何值。相反，它从ipranges.txt中获取IP地址，其中包含要扫描的无类别域间路由（CIDR）以查找Weave Scope UI实例。masscan和zgrab等网络枚举工具用于查找IP地址和UI实例。当发现Weave Scope UI的可访问实例时，将使用curl将相应的IP地址和端口泄漏到攻击者控制的服务器amazon2aws.com。

**域转移**

在分析攻击者控制的服务器时，我们发现了亚马逊科技公司(亚马逊公司的研究和开发子公司)对注册者Nice IT Services Group Inc./Customer Domain Admin(恶意typosquat域的前所有者)提出的投诉。统一域名争议解决政策(UDRP)是解决注册人之间域名争议的法律框架。我们注意到该域名后来于2022年6月转让给了亚马逊科技公司(Amazon Technologies, Inc.):

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928331157714.png "1666928331157714.png")

通过VirusTotal检查用于解析域的IP地址，我们发现amazon2aws[.]com和teamtnt[.]red的记录历史可能与TeamTNT组织有关。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928341581895.png "1666928341581895.png")

解析到的公共IP地址的两个域

**总结**

尽管根据Shodan的扫描结果，Docker REST API的泄漏事件已经减少了很多，但随着攻击技术的发展，上述技术和进程可以与目标系统中其他已知或未知的漏洞相结合。攻击者一直在开发他们的武器库，测试和构建不同的工具，经常滥用合法的工具和平台。2021年12月，我们发布了一篇关于Apache HTTP Server漏洞CVE-2021-40438的文章，该漏洞允许在被利用时进行服务器端请求伪造(SSRF)。我们还观察到有人试图查询AWS IMDS。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666928350804782.png "1666928350804782.png")

Shodan对泄漏的Docker REST API的扫描结果

随着越来越多的公司采用云平台，攻击者也构建了利用这些云服务和基础设施的工具。作为防御者，我们需要了解攻击者在进入后的目标是什么，以及需要使用哪些方法来禁用、解除和遏制这些威胁。由于开发人员使用环境变量来存储机密和凭据，我们发表了关于可能的威胁场景和缓解步骤的研究。

本文翻译自：https://www.trendmicro.com/en\_us/research/22/j/threat-actors-target-aws-ec2-workloads-to-steal-credentials.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?5iwlB9Jk)

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

![](https://img.4hou.com/wp-content/uploads/2017/07/6cfb327dad8fe371f6fa.jpg)

# [luochicun](https://www.4hou.com/member/aOZG)

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

[查看更多](https://www.4hou.com/member/aOZG)

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
[我要投稿](https://www...