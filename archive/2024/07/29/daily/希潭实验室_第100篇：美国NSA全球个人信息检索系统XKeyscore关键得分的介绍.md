---
title: 第100篇：美国NSA全球个人信息检索系统XKeyscore关键得分的介绍
url: https://mp.weixin.qq.com/s?__biz=MzkzMjI1NjI3Ng==&mid=2247486904&idx=1&sn=60b3717d14f151dc19429c56a6635665&chksm=c25fc2c3f5284bd55ad250c5c4506deffac8505efcaa9689117e7a9a66d5d34f7e7696280744&scene=58&subscene=0#rd
source: 希潭实验室
date: 2024-07-29
fetch_date: 2025-10-06T17:41:29.455079
---

# 第100篇：美国NSA全球个人信息检索系统XKeyscore关键得分的介绍

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUFWsueAvop3m4yeSZmzVFJPs3nrbllwelRq6o5Vsd0PVVI3pH839MYQ/0?wx_fmt=jpeg)

# 第100篇：美国NSA全球个人信息检索系统XKeyscore关键得分的介绍

原创

abc123info

希潭实验室

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcCCMJ6Af2WYicgMPA32IwibF8mI2ibC9h8jaHkhxnZzZuqctMLRTxDudicA/640?wx_fmt=png)

## **Part1 前言**

**大家好，我是ABC\_123**。公众号已经更新两年多了，这是我个人的第100篇原创。前面很长时间，ABC\_123阅读了大量的国外资料，给大家总结分享了美国NSA的几款网络攻击武器：主动防御系统TUTELAGE、Turmoil被动监听系统、Turbine任务逻辑控制系统、顶级后门UnitedRake联合耙、量子注入攻击手法、攻击伊朗核设施的震网病毒等等。本期继续给大家介绍，近几年来国外一直被媒体报道的**美国NSA秘密研发的一款全球流量信息检索与分析系统——XKeyscore关键得分系统**。

该系统由美国NSA于2003年开始研发，2013年时由斯诺登公开，它基本上汇聚了前面ABC\_123所介绍的那些流量监控系统采集的所有流量信息，经过处理和筛选存储在XKeyscore的分布在全球各地的分布式数据库中。美国NSA情报人员输入一个IP、用户名、邮箱、手机号或sessionId，就可以检索这个人的很多上网记录，包括个人账号密码、网络设备密码等等。

**建议大家把公众号“希潭实验室”设为星标，否则可能就看不到啦！**因为公众号现在只对常读和星标的公众号才能展示大图推送。操作方法：点击右上角的【...】，然后点击【设为星标】即可。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450Dq1Q8s4COc7InkMO0jIGjiaGho1fcJicpibWB4vzvIM1wAib9TiakVECbIM5S0mHCTTeGJJibWtCe25vXw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## **Part2 XKeyscore关键得分系统**

* ### **基本介绍**

XKeyscore是美国国家安全局（NSA）开发的一个庞大的情报收集和分析系统，国内被翻译为“**关键得分**”系统，它也被称为美国NSA的谷歌搜索系统。它通过各种手段收集互联网上的海量信息，并提供便捷的图形用户界面，允许情报人员通过输入电子邮件地址、姓名、电话等身份识别关键字，对目标个人进行全面的信息检索、实时监控和实时网络追踪。该系统通常部署在Red Hat服务器上，使用Apache Web服务器并将收集到的数据存储在MySQL数据库中。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLU83qNaH9GDgeGibUrfRQ9WokEqfuxYDAnMowgcM74246S3ersEWwgYKA/640?wx_fmt=png&from=appmsg)

如下图所示，该系统提供了GUI操作界面，因而使用非常简单，很多场景下，只需要输入域名关键字、邮箱地址，点击回车键，就会将系统中的存有用户名密码显示出来，攻击瞬间就完成。美国NSA可以在一天之内完成对分析师使用XKeyscore系统的培训，培训内容还包括相关的法律和道德准则，每次搜索都是完全可审计的，以确保他们是正当使用并且符合法律规定，防止分析人员滥用此系统。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLU8LcSndgIjiaGXaAPYYnucMwiauqQysz3d10h4Pjib8NOwVa52h3lKxyCg/640?wx_fmt=png&from=appmsg)

* ### **全球分布式监控集群**

如下图展示了XKeyscore系统在2008年时的全球分布图，在全球五大洲的多个国家建立了150个站点，这些国家包括美国、英国、日本、俄罗斯、墨西哥、巴西、西班牙、索马里、巴基斯坦、澳大利亚、尼日利亚等等，当年服务器规模已超过700台，共同组成一个分布式的信息处理和查询系统，通过大规模分布式计算机集群，极大增强了其数据存储和处理能力。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUll2z7UY0lhVxendeynibmKDRsXYM89vqEPZwKk1ejUibqDvF4AfwIgNQ/640?wx_fmt=png&from=appmsg)

如下图所示，美国NSA泄露文档给出了XKeyscore的查询层次结构。当情报人员开始搜索的时候，查询任务会逐级下发到不同的地区的站点进行查询，然后将查询结果反馈回来。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUy4pOn2LrqKQOaLme3YtrvtZic0fe5VBzgQbwtvRYEniaKcxibuWsL8AkA/640?wx_fmt=png&from=appmsg)

* ### **XKeyscore流量数据来源**

如图所示，泄露的文档展示了XKeyscore的流量数据来源，具体包括CIA/NSA特别收件服务（F6）、NSA监听项目（如“棱镜门”、MUSCULAR和INCENSER）、外国卫星数据（FORNSAT）、MARINA元数据存储库、TRAFFICTHIEF元数据存储库等。此外，美国NSA还借助XKeyscore系统与其他情报机构的合作获取其本国数据，例如德国情报部门曾向美国国家安全局提供德国公民的元数据，作为交换条件获得了XKeyscore系统的副本和部分XKeyscore系统的使用权限，宣称其用于分析本国公民数据。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUs1VxiaD7AwHJicqcscdAKJe77wrv8kGIAPP9V6Bo7UEPp8votibRRp62g/640?wx_fmt=png&from=appmsg)

此外，XKeyscore通过全球各个监听节点收集了大量流量记录，涵盖网络用户的谷歌搜索、网页浏览、社交媒体互动、在线PDF文档、僵尸网络流量，以及特定平台如Facebook聊天记录、雅虎搜索记录和Twitter互动等。它还获取网络用户名和密码、谷歌地图等应用中的个人身份信息、后门键盘记录，并监控数据传输与文件共享，包括上传下载的文件、网盘传输文件、广告流量分析。此外，XKeyscore关注中间件和系统安全，收集漏洞利用情况、浏览器版本、中间件指纹及操作系统版本信息。这些数据使得XKeyscore能够全面监控和分析全球网络活动和用户行为。

* ### **网络流量采集及元数据索引构建**

情报人员可以通过使用不同的插件（Email地址插件、文件提取插件、日志处理插件、HTTP解析器插件、电话号码插件、用户活动信息插件等）将网络用户的手机号、电子邮件地址、Log日志、用户活动信息建好索引存储在指定的数据库中。除此之外，还可以存储电子邮件内容、邮件附件、照片图片、聊天记录、语音视频、语音通话记录、VoIP通话数据、Skype会话、网络摄像头照片等等。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUd4ia3oMKnXoXp4Z9ZVI31ULeVmaJ4quesCTd2ArOmHX70FOiaxPaW0Yg/640?wx_fmt=png&from=appmsg)

* ### **网络电话VoIP与VPN流量的解密与存储**

如下图所示，XKeyscore系统可以解密VoIP网络电话及部分VPN加密流量，并将流量解析还原存储在XKeyscore分布式数据库中进行分析，其技术实现原理后续再给大家讲解。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUhq34XcZShiapic6NBqkZxxSoYhicWcbFK6Z52m5Q0Lwm7w8Yuz4MMJJqg/640?wx_fmt=png&from=appmsg)

如下图所示，这是美国NSA的文档中讲解的关于VoIP监听的技术实现。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLU6SfHYFZasFeCB7HEmLPMDTJt3AhL4NnZ9CSYfVJUqpSlTKQaibbuqGw/640?wx_fmt=png&from=appmsg)

如下图所示，这是美国NSA的文档中讲解的关于VPN流量监听的技术实现（其实现原理后续再给大家分享）。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUPRE4wtS4yodxJmWrQhSxnn2HsYfVEZ2xZcic1uqLng4FfTYibgsHylicQ/640?wx_fmt=png&from=appmsg)

* ### **监视欧洲盟友及各国政要**

美国国家安全局（NSA）通过XKeyscore系统大规模监听欧洲政客的移动通信，包括电子邮件内容、电话语音、手机短信和社交媒体活动等信息。仅在2009年，就有122名外国领导人遭到美方的监听。俄罗斯、伊朗等被美国视为长期对手的国家，其领导人也成为NSA的监听目标。此外，一些国际组织的高级领导人，如联合国秘书长，亦被纳入监控范围。不仅如此，美国的重要合作伙伴新西兰政府也曾利用XKeyscore监视世界贸易组织总干事职位的候选人，并对所罗门群岛进行过大规模的间谍活动。据国外媒体报道，美国情报专家在XKeyscore的帮助下，在联合国秘书长潘基文与奥巴马总统正式会晤之前，成功获取到了会谈内容的要点。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUJX0iby04k0AYo8vXYx961zddtI3SicY8Cfd2ib5YgRL2OID1G1p0SwibfA/640?wx_fmt=png&from=appmsg)

* ### **监视黑客组织及0day工具**

黑客论坛同样是美国国家安全局（NSA）需要监视的目标之一。许多黑客在论坛中出售或使用各种黑客工具。NSA需要了解这些黑客的技术水平及其技术的获取途径。借助XKeyscore系统，NSA能够提取在网络中传输过的黑客工具及0day漏洞的POC。

* ### **监控及追踪恐怖分子**

XKeyscore是一种能够分析大量监视数据并识别可疑行为模式的系统。美国情报人员利用XKeyscore监视基地组织高级领导人的网络活动和电话通信。例如，美国特工曾使用该系统监视基地组织高级领导人本·拉登的心腹Shaykh Atiyatallah，获取了他的操作信息和搜索数据记录。根据NSA泄露的文档显示，该系统在2008年前帮助美国抓捕了300名恐怖分子。

## **Part3 XKeyscore的使用案例**

* ### **辅助美国及盟友网络入侵**

XKeyscore系统可以展示某个国家或地区内所有存在漏洞、可被利用的网络设备。通过提供目标计算机系统的一些信息，如中间件版本、浏览器User-Agent痕迹、操作系统版本等，XKeyscore系统能够辅助美国国家安全局（NSA）的人员评估目标计算机系统的难易程度，并有针对性地实施远程漏洞利用。美国NSA曾与英国情报部门合作，通过APT渗透的方式获取某手机通信的加密密钥，从而劫持该手机用户流量，并向目标手机投放间谍软件以收集敏感数据。XKeyscore系统为APT成员提供了入侵该手机公司电子邮件的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUjvX0Lt5aYY97qQdApCDl7RicmpHxdKH5NwUGVhfxD2IGSurVjyZTxJQ/640?wx_fmt=png&from=appmsg)

如下图所示，XKeyscore会对流量中的关键字段进行提取并进行索引，包括请求包和返回包，这些数据可以作为APT攻击前期的信息收集使用。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUnnOgIqCGiaRjSbsVDh2XmhQdOQnarbMF0pjjL8pZdV0cZba6kwauFPg/640?wx_fmt=png&from=appmsg)

* ### **查询网络设备的账号密码**

根据美国NSA泄露的文档，美国NSA情报人员可以使用XKeyscore关键得分系统查询网络设备的账号密码，包括网络设备的配置文件，从而直接接管网络设备的权限。下面这张图片给出了其原理，部分网络设备是由telnet的23端口远程登录的，其整个过程是明文流量，因而美国NSA在全球各个监听节点可以抓取这些telnet的明文流量，将其账号密码截获。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUJODjkFExpBgAdeNrMYRu7iaGwvWB96lQodDWaPFX6WPY37hFuTECaOQ/640?wx_fmt=png&from=appmsg)

借助XKeyscore关键得分系统，美国NSA情报人员可以输入路由器设备的IP地址和登录端口，如telnet的23端口进行查询。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUFyqYCibFd17EYPkiaVK6WCJ8y2u2icUE22enBddlWt4nghukMyNL9fFxg/640?wx_fmt=png&from=appmsg)

点击搜索之后，XKeyscore系统显示出了其数据库记录的该设备的账号密码。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLU5QgK5wWtHp8fjXK7Jnzrg55rX8BlqLCzribTtzd9IzuhEPdgjwibic0Xw/640?wx_fmt=png&from=appmsg)

下面这张PPT展示了美国NSA情报人员通过XKeyscore系统，查看指定IP路由设备的配置文件内容。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUIb75ibbibfZibE3IVk1tjTtyvfsWfuMaTNHEtgXM3dBFKnQRV7rXAJKicA/640?wx_fmt=png&from=appmsg)

* ### **查询邮箱账号密码及邮件内容**

如下图所示，PPT展示了美国NSA可以从网络流量的各个角落提取邮箱地址，从而关联并提取出该邮件的网络通信内容，暂存在后台数据库中。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLU8kjXgicvDkHicdfyEbKKkIdcdy54ll3ibjIIScQe1sQka0zDxjHYv8aOA/640?wx_fmt=png&from=appmsg)

如下图所示，美国NSA的情报人员通过输入指定的邮箱地址，从XKeyscore的分布式数据库中查询与查看私人邮箱内容信息。NSA 有一款名为"DNI Presenter"的工具，能够帮助情报人员更好地阅读邮件内容。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUvgS5Aqn5Kqjk6SAO9F81ACymicDJaEVH3WsYVTDwnIKftohIibQvLJ9w/640?wx_fmt=png&from=appmsg)

如ppt展示，成功从HTTP流量的POST数据中检索到指定邮箱的账号密码。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUBRK6rOuj5n0Oibx3b7G46SM0WqVjUFticO2OrTvn4a577jFBjGvhia60w/640?wx_fmt=png&from=appmsg)

如ppt展示，成功从HTTP流量的Cookie内容中检索到指定邮箱的账号密码。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUacW1IQes3ByibKuDiaZakPXKxibUkrWenDyOdAz2c3ewDojZ8Q2entLfg/640?wx_fmt=png&from=appmsg)

* ### **查询Web网站的账号密码**

如下所示，美国NSA的情报人员成功检索到指定用户的账号密码信息。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUf4DAr0KsqD9rsGjW0icE6XOf5c8Ztw4cBmnRZgDHtIqVFvXIKe7RvaQ/640?wx_fmt=png&from=appmsg)

如下所示，美国NSA的情报人员成功检索到指定用户的账号密码信息。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BiaRPJXnNic37auh8niaXUMLUbxLyIFxK9ZZGCCLwwhj4v6Tm4OQIicx...