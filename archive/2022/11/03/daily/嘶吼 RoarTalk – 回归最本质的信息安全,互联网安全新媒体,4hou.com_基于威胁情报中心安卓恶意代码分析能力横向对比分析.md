---
title: 基于威胁情报中心安卓恶意代码分析能力横向对比分析
url: https://www.4hou.com/posts/nJAY
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-03
fetch_date: 2025-10-03T21:36:47.338251
---

# 基于威胁情报中心安卓恶意代码分析能力横向对比分析

基于威胁情报中心安卓恶意代码分析能力横向对比分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 基于威胁情报中心安卓恶意代码分析能力横向对比分析

LianSecurity
[技术](https://www.4hou.com/category/technology)
2022-11-02 17:09:02

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)194491

收藏

导语：本文主要以各家威胁情报中心/在线沙箱在安卓恶意代码自动化分析能力与基于逆向引擎 Reactor 所研发 incinerator 逆向工具进行对比

**前言**

本文主要以各家威胁情报中心/在线沙箱在安卓恶意代码自动化分析能力与基于逆向引擎 Reactor 所研发 incinerator 逆向工具进行分析能力的对比，从而让大家更加清晰直观的了解到彼此之间的区别，文章所测试的威胁情报中心均为公开版本（免费），并不代表各个能力平台的实际状态，不以偏概全。

测试平台列表如下：

* 360 威胁情报中心（包括其沙箱）
* 安恒威胁分析平台（包括其沙箱）
* 安天威胁情报中心
* 绿盟科技 NTI 威胁情报中心（包括其沙箱）
* 启明星辰 VenusEye 威胁情报中心
* 奇安信威胁情报中心（包括其沙箱）
* 天际网盟 RedQueen 安全智能服务平台
* 微步在线恶意软件分析平台（包括其沙箱）
* VirusTotal（包括其沙箱）

测试恶意代码样本如下：

* 样本名称： ERMAC

* 哈希值

+ MD5:16e991d73049f1ef5b8f5fa0c075ef05
+ SHA-256:f4ebdcef8643dbffe8de312cb47c1f94118e6481a4faf4166badfd98a0a9c5d3

#

> ERMAC 是由 BlackRock 移动恶意软件背后的攻击者操作的。8 月 17 日，名为“ermac”和“DukeEugene”的论坛成员开始宣传该恶意软件。ERMAC 和其他银行恶意软件一样，被设计用来窃取联系信息、短信、打开任意应用程序，并触发针对大量金融应用程序的覆盖攻击，以刷取登录凭据。此外，它还开发了新功能，允许恶意软件清除特定应用程序的缓存并窃取存储在设备上的帐户。

---

摘自 安恒威胁情报平台

* 样本名称：FurBall

* 哈希值

+ MD5:6151b1e2e5035a8eb596ce1c37565e87
+ SHA-256:0d09d5e46e779d796a8d295043e5bbd90ac43705fa7ff7953faa5d8370840f93

#

> Domestic Kitten，也称 APT-C-50，据称是伊朗的一个黑客组织，主要是从受损的移动设备获取敏感信息，至少从 2016 年起，就一直非常活跃。 趋势科技（Trend Micro）在 2019 年一项分析报告中表示，APT-C-50 可能与另一个名为“弹跳高尔夫”（Bouncing Golf）的黑客组织有联系。（Bouncing Golf 主要针对中东国家进行网络间谍活动）。

---

摘自 Freebuf

**横向分析对比**

本文将会从安卓恶意代码分析的多个维度进行相关分析对比，鉴于部分平台不存在基于安卓的云沙箱功能（或并未在公开/免费版本出现），所以对比的结果基于各个平台呈现的相关静态化分析数据进行横向对比。而 LianSecurity（链安科技）的 incinerator 作为一个综合性 Apk 逆向工程产品，并不带有任何基于恶意代码特征库、威胁情报源、沙箱等功能，所以横向分析对比内容仅仅基于 incinerator 的 Apk 静态分析能力。

鉴于我们在进行相关能力对比的时候，要有一个比较具象化的理解，究竟什么叫好呢？或者说什么样的分析能力所呈现出来的分析报告会更加适合恶意代码和威胁溯源的研究之用呢？所以我们选择了一个比较得到大家公认的“VirusTotal”，以 VirusTotal 的分析报告来看各自在安卓恶意代码分析上面的细节以及颗粒度究竟是如何的。

#

![VT.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221102/1667382607924786.png "1667379004620692.png")

图 1

从两个样本的静态化分析结果来看（如图 1 左右所示），VT 对于 Apk 各项信息的检测以及呈现都是非常完善的，能够准确的分析出样本当中的所有关键信息，作为恶意代码分析以及威胁溯源的角度来说，首先，一个专业的分析服务能够精准详细的把以下罗列清楚的情况下，我认为这已经是一份优秀的分析报告。

* Apk 基础信息

  HASH

  TrID

  文件大小等
* Apk 包名以及相关的信息

  Apk 名称

  Apk 签名信息
* Apk 应用权限分析

  风险等级划分以及排列
* Apk 行为分析
* Apk 应用网络请求
* Apk 软件成分分析

所以，接下来我们会以 VT 的报告所呈现的，一一对于上面所提到的厂商进行分析能力的横向对比，从而深度的去了解现在国内在这方面的发展以及相关技术是如何的。

**360 威胁情报中心**

![](https://liansecurity.com/ucenterapi/upload/file/c00ad03bc0eda1664d568e8baf2f1ce5)

图2

很可惜，我们从样本 1 与样本 2（如图 2 上下所示）的分析内容我们可以得知，360 的分析报告里面只显示样本的 HASH、包名以及对应的 IOC 信息，而对于样本的应用行为、应用权限、网络请求、成分分析都没有，并且动态分析也完全没有的，对于恶意代码以及威胁情报研究来说，360 威胁情报中心的呈现几乎没有什么帮助的。

注：360 安全大脑沙箱云检测失败，Android 部分需要相关的积分以及收费，所以就此作罢。

**安恒威胁分析平台**

## ![](https://liansecurity.com/ucenterapi/upload/file/51ddad030efac39e354040cdbf138cd4)

图3

安恒在两个样本的分析上（如图 3 上下所示），与 360 一样能够准确判断出样本的家族以及相关的归属，并且安恒在基础信息方面增加了关于样本的 Hexdump，使得样本基础信息部分看似很丰满，但是作为静态分析结果来讲，Hexdump 既不是一个总结性的结果呈现，也不能给分析人员任何定性的信息，不应该呈现在这里。可能是因为免费/公开版本，动态分析部分并没有任何的资料，但依然是基于恶意代码以及威胁情报研究来说帮助微乎其微的，和 360 所呈现的信息基本相同。

**安天威胁情报中心**

![](https://liansecurity.com/ucenterapi/upload/file/5ce0891288b4e9a0087d778ecacc819d)

图4

我们所抽样的样本哈希提交到安天威胁情报中心后（如图 4 所示），显示的检测结果是为空。所以也无法对于安天威胁情报中心的安卓分析能力进行任何的对比分析了，估计是安天威胁情报中心没有样本数据，但是武汉安天的杀毒引擎是可以正确识别出样本为恶意代码的。

**绿盟 NTI - 威胁情报中心**

![](https://liansecurity.com/ucenterapi/upload/file/437a8adb7bccf10c616e4c348a8b21cd)

图5

绿盟科技 NTI-威胁情报中心在基于 ERMAC 样本分析能够显示对应的 HASH 信息（如图 5 所示），除此以外什么都没有了，而基于 APT-C50 的样本分析是并没有任何数据显示的，与安天威胁情报中心一样，应该是他们没有对应的样本记录，当我们改为威胁分析中心并提交样本进行分析后，看到分析中心对于两个样本都进行有效的检测，其中哈希值为“16e991d73049f1ef5b8f5fa0c075ef05”的样本呈现出相关的基础信息（样本哈希、元数据）并没有任何静态分析报告，而哈希值为“6151b1e2e5035a8eb596ce1c37565e87”的样本，基础信息呈现上比较简单，杀毒引擎检测没有结果、分析结果采用的是绿盟自己的检测策略，与常见的检测呈现不一样，比较杂乱，所以需要一定学习才可以比较明白。

**VenusEye 威胁情报中心**

![](https://liansecurity.com/ucenterapi/upload/file/cd444bd07ed693df69963af82fc8958c)

图6

VenusEye 基于样本 1（如图 6 上所示）的基础信息呈现较为完整，也是属于比较弱化的，没有任何静态化分析可言，而基于样本 2（如图 6 下所示）来说，VenusEye 并没有对应的数据。

**奇安信威胁情报中心**

![](https://liansecurity.com/ucenterapi/upload/file/f4c64f95543f1d918c18cfb3f9f35296)

图7

国内这么多家威胁情报中心或者沙箱检测的细节程度来说，从样本 2（如图 7 下所示）的威胁研判分析来看，因为有了沙箱检测的完整补充，使得整体的分析详细程度非常完整，奇安信无疑是国内厂商提供公开可以查阅的威胁情报中心/沙箱的天花板，而样本 1（如图 7 上所示）的分析来看，我们提交测试很多次，不管是以登陆/非登陆状态下，沙箱检测永远都是检测中的状态，不知道是不是出现卡死的情况，所以样本 1 从纯静态化的状态与其他厂商并无太大的区别。

**天际网盟 RedQueen**

![](https://liansecurity.com/ucenterapi/upload/file/89b6c3b8317556ccd76baffca6a3eb53)

图8

天际网盟 RedQueen 基于样本 1（如图 8 所示）的哈希值并无数据，并且无法上传样本进行测试，而基于样本 2 的哈希值查询后，发现有相关数据记录，基础信息与其厂商大同小异，而其余的信息并无。

**微步在线恶意软件分析平台**

![](https://liansecurity.com/ucenterapi/upload/file/28c784351bf7026820bf9f27062b1ca7)

图9

在众多国内威胁情报中心/沙箱的厂商里面，微步在线曾经是唯一一家能够准确识别出样本 1（如图 9 左所示）该恶意代码的家族，但是当我重跑多次样本 1 去获取最新检测报告之后，它的家族检测就开始改变了，这个让我觉得疑惑的，并且从检测报告来看（如图 9 右所示），检测的逻辑问题也很多，例如：

* 沙箱环境是 Win7+Office2013
* 多维检测与检测样本无关
* 多引擎检测结果不准确

当我在上传样本进行检测时，上传的文件格式并没有 Apk 可选，所以只能够以其识别的压缩文件格式进行上传，并且沙箱的环境注定了对于安卓应用是无法解释的，而在基于沙箱环境下的多维检测 Sigma 规则是完完全全的误报，在多引擎检测结果里面，微步在线显示“基于 2022-10-29 19:36:04 的时间状态下，只有三个杀毒引擎发现该样本为恶意代码”，但是从多方数据来看，微步在线所显示并未检测恶意代码的引擎当中，早已可识别样本 1 为恶意代码，例如卡巴斯基之类、小红伞、DrWeb。

而从样本基础信息的数据来看，在没有任何的沙箱检测下，微步在线的检测结果比起奇安信的要好，样本的基础信息、元数据、权限分析之类的都是有的，但是对于需要看着报告的研究人员来说，报告很明显在呈现上并没有考虑太多这种需求，特别是如果在没有 IOC、杀毒引擎之类的辅助数据支撑下，不管是流行的 ERMAC 还是隐秘性更高的 APT 样本都会出现很严重的漏报的情况出现。

**基于 incinerator 的 Apk 基础检测能力**

incinerator 作为一款国产自主的安卓 Apk 逆向工具分析工具，用来与威胁情报、恶意代码分析平台或者动态沙箱进行对比，在任何人眼中看起来都很好笑，而我们要对比的仅仅是 incinerator 在 Apk 分析时，呈现给用户的基础信息（如图 10 所示），当我们要进行 Apk 分析的时候，incinerator 会通过自主研发的高效准确的逆向技术，首先会对 Apk 进行全面基础分析，分析结果包含了包名、HASH、签名等基础信息（如图 11 所示），再通过静态单赋值与交叉引用结合找出全流程执行路径, 并对应用行为进行源码级深度检测，以及权限进行分类标注，突出强调高危和敏感权限，检查应用内网络请求以及目标地址特征信息， 抽取依赖库指纹信息分析软件成分组成。

#

* Apk 基础信息呈现

#

![](https://liansecurity.com/ucenterapi/upload/file/92e9ad4d434f4597e5360b25e7578d07)

图10

* 签名信息

#

![](https://liansecurity.com/ucenterapi/upload/file/634a49f3b0bf609d049690bbc3bfaf6b)

图11

* 权限信息

#

![](https://liansecurity.com/ucenterapi/upload/file/d529e3328c3f5a93f7ca960a8775ba7d)

图12

上图是样本 1 ERMAC 中抽取的部分权限信息（如图 12 所示），可以看到 incinerator 对权限进行了详细的检测以及分类，对于 Apk 进行申请“短信发送”、“拨打电话”等权限声明都标注了高危。

注：在 Android 官方文档中，“短信发送”以及“拨打电话”是被标注为危险权限 \*

#

* 行为分析

#

![](https://liansecurity.com/ucenterapi/upload/file/d7ff8313783684fb61294159cd7b0f62)

图13

![](https://liansecurity.com/ucenterapi/upload/file/c8845076a815c05af257d1298658b412)

图14

Incinerator 对 Apk 行为分析有多个分类，如下（如图 13-14 所示）：

* 加密安全

主要是检测采用的加密的方式是否正确、是否有采用不够安全的配置，导致加密失效或者容易被破解等。

* 应用安全

查看当前应用是否有安全风险，包括是否有日志泄露、是否动态加载 Dex、是否使用高危函数等。

* 组件安全

动态注册 Receiver 危险、Fragment 注入、组件导出风险、Intent 隐式调用风险、Intent 调用反射风险等。

* 数据安全

外部存储风险、剪贴板泄露、应用数据备份风险等。

* 隐私安全

应用是否有使用录音、拨打电话、摄像头、地理位置、电话监听、发短信等行为。这里会结合权限申请情况给出最终结果，如果有敏感 API 调用，但是没有申请权限，则报告中不会指出，因为调用不会成功的。防止误报给用户造成困扰。

* WebView 安全

WebView 任意代码执行漏洞、WebView 启用 Javascript 风险、WebView 明文存储密码等风险。

* 通讯安全

未验证 CA 证书、HTTP 协议传输、Webview 忽略证书、端口开放检测等。

当检测出相关问题时，incinerator 会按照严重程度进行分类排列、给予对应的安全建议，并且定位...