---
title: 思科Talos报告：威胁分子使用已知的Excel漏洞
url: https://www.4hou.com/posts/6VEO
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-31
fetch_date: 2025-10-04T02:46:47.397298
---

# 思科Talos报告：威胁分子使用已知的Excel漏洞

思科Talos报告：威胁分子使用已知的Excel漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 思科Talos报告：威胁分子使用已知的Excel漏洞

布加迪
[漏洞](https://www.4hou.com/category/vulnerable)
2022-12-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)244138

收藏

导语：威胁分子使用.XLL Excel文件用恶意软件感染计算机的现象日益猖獗。本文深入介绍了这种比较新颖的攻击技术以及如何防范。

![1.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221229/1672303875747875.jpeg "1671878049209370.jpeg")

在大多数情况下，用户在这些应用程序中执行代码时，仍然需要点击“同意”，但一些社会工程伎俩诱使毫不知情的受害者点击并允许执行恶意宏本身。也有可能在没有任何用户交互的情况下直接利用漏洞，以启动恶意软件。

**外面的.XLL恶意利用情况**

思科Talos的一项新研究显示，威胁分子可能会利用Excel文件中的事件处理函数来自动启动.XLL文件。最常见的方法是在Excel Add-In管理器调用xlAutoOpen或xlAutoClose函数时执行恶意代码。

思科Talos研究人员利用VirusTotal中的特定查询来查找恶意的.XLL文件，并提供YARA规则来查找此类文件。他们将使用常用的微软.XLL SDK构建的原生.XLL样本和使用ExcelDNA框架生成的样本分开来，因为ExcelDNA框架是免费的，往往是最常被威胁分子所使用的框架（见下图）。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221229/1672303876105349.png "1671878068173180.png")

图2. VirusTotal中.XLL文件的提交数量（图片来源：思科Talos）

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221229/1672303876640666.png "1671878078213381.png")

图3. VirusTotal中.XLL文件的提交数量（图片来源：思科Talos）

上面两个图表显示，早在微软开始阻止包含VBA宏的文档之前，威胁分子就一直在利用.XLL文件漏洞了。

思科Talos的研究人员查明，在2017年7月之前，没有提交任何潜在恶意的样本。在VirusTotal平台上发现的第一个.XLL攻击载荷启动了calc.exe，这是渗透测试人员和网络犯罪分子常用的测试方法。同月提交的第二个样本启动了Meterpreter反向shell，可能用于渗透测试或恶意用途。

在那次活动之后，.XLL文件零星出现，但直到2021年底，Dridex和FormBook等臭名昭著的恶意软件家族开始使用，利用.XLL文件的活动才有所增加。

**哪些威胁分子在利用.XLL文件？**

一些威胁分子现正在使用.XLL文件来感染计算机。

据美国司法部声称，APT10（又叫Red Apollo、menuPass、Stone Panda或Potassium）是一伙网络间谍威胁分子，自2006年以来一直在运作。

2017年12月，研究人员发现了一个文件利用.XLL注入了APT10专有的名为Anel的恶意软件

TA410是另一伙针对美国公用事业和外交机构下手的威胁分子，与APT10有着松散的联系。他们使用的工具包也包括2020年发现的.XLL阶段。

针对克什米尔非营利组织和巴基斯坦政府官员的DoNot团队似乎也使用了这种方法：一个.XLL文件包含两个导出函数，一个导出函数名为pdteong，第二个导出函数名为xlAutoOpen，使其成为功能齐全的.XLL攻击载荷。pdteong导出函数名称仅由DoNot团队使用。

FIN7是一伙来自俄罗斯的网络犯罪威胁分子。2022年，这伙威胁分子开始在恶意电子邮件活动中使用.XLL文件作为附件来发送。这些文件被执行后，它们充当了下一个感染阶段的下载器。

然而，VirusTotal中.XLL检测出现高峰主要来自Dridex恶意软件活动。这些.XLL文件被用作下一个感染阶段的下载器，该阶段是从通过Discord软件应用程序访问的大量攻击载荷中选择出来的。

第二种最常见的载荷是FormBook，这是一种在网上可以低价买到的信息窃取服务。它使用电子邮件活动来传播.XLL下载器，从而获取下一个感染阶段，即FormBook恶意软件本身。

最近针对匈牙利的AgentTesla和Lokibot活动通过电子邮件利用了.XLL文件。电子邮件假装来自匈牙利警察局（见下图）。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221229/1672303877952933.png "1671878141110166.png")

图4. AgentTesla活动中的欺诈邮件内容（图片来源：思科Talos）

思科Talos将文本翻译如下：

“我们是布达佩斯第七区警察局。我们已听说贵公司的优秀业绩。我们中心需要您对我们的2022年预算（附上）给一个报价。预算由我们匈牙利政府的内政部共同出资。请于2022年8月25日前提交报价。请查收附件，如果您需要更多信息，请告知我们。”

此外，Ducktail恶意软件是一种信息窃取恶意软件，由越南运营的威胁团伙运行，它也利用了.XLL。这伙威胁分子使用一个名为“项目营销计划细节和Facebook谷歌广告结果报告.xll”的文件，用Ducktail恶意软件感染目标。

**默认的微软Office行为往好的方向转变**

为了通过使用VBA宏来帮助对抗感染，微软决定改变其Office产品的默认行为，阻止从互联网下载的文件中的宏。

Office Add-In是可以添加到Office应用程序中以改进功能或增强应用程序外观的可执行代码段。Office Add-In可能包含VBA代码或在.NET字节码中嵌入已编译功能的模块。这可能表现为COM服务器，也可能表现为用特定的文件扩展名重命名的动态链接库。

面向微软Word应用程序的Add-In需要放在由注册表值指定的位置，具体取决于Office版本。文件扩展名为. WLL的文件将被加载到Word进程空间中。

对于微软Excel，用户点击的任何具有.XLL扩展名的文件都将自动尝试运行Excel作为.XLL文件的打开器。在任何情况下，Excel软件都会触发有关潜在恶意软件或安全问题的显示消息，但这对普通用户无效，他们往往忽视此类警告。

.XLL Add-in通常使用微软Excel .XLL软件开发工具包由C/C++编程语言开发，但Add-In Express和Excel-DNA等一些框架允许使用C#或VB.NET之类的.NET语言。

**如何防范.XLL安全威胁？**

使用.XLL文件在企业环境中并不普遍；不需要它的企业应该阻止试图在其环境中执行.XLL文件的任何活动。如果贵公司确实允许使用.XLL文件，必须在端点和服务器上进行密切的监视，以便检测并调查任何可疑活动。

电子邮件网关不应该默认接受.XLL文件，并增强企业用户的意识。如果他们从Excel中看到关于运行Add-In的警告消息，又不知道为什么会出现这种情况，就不应该允许执行，并打电话给IT/安全部门。

本文翻译自：https://www.techrepublic.com/article/cisco-talos-xll-excel-vulnerability/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?NN6J54bO)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/VGrO)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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