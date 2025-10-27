---
title: API BOM - ASPM数据关联分析纽带
url: https://mp.weixin.qq.com/s?__biz=MzI2NTExNzcxNQ==&mid=2247484361&idx=1&sn=8e472a7a51b24dacdf95759c0a58c4a8&chksm=eaa30ab5ddd483a3ebf52abba4056a525450dc0dd3cd0a1a1aef253b5339b066093ed268e076&scene=58&subscene=0#rd
source: 代码审计SDL
date: 2025-01-19
fetch_date: 2025-10-06T20:08:55.850811
---

# API BOM - ASPM数据关联分析纽带

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/a4tp2b7vTo5w6G3Qx05qUF3m73reT8PM0pvGic8Rh7ErvnRN176iamyJ1edXDO2bavmhic2svf4QwwvvA7D2XbdKg/0?wx_fmt=jpeg)

# API BOM - ASPM数据关联分析纽带

原创

sanduo

代码审计SDL

# API BOM

API物料清单(API BOM)，这个概念是之前调研ASPM厂商OX Security提出的一个概念，目前没有统一的定义，可以参考软件物料清单(SBOM)。

笔者在做ASPM数据分析调研的时候，主要的目的是需要寻求一种合理的方式对多个安全平台收集的数据进行去重分析，早期可以通过制定统一的漏洞分类分级标准，使用CWE编号或者支持统一的漏洞编号，比如：CVE，CNNVD，CNVD等，进行统一划分或者去重分析，但是实际实践效果就会差很多，主要原因有很多，最主要的原因是xAST产品种类繁杂，检出的结果标准不一，中间关联关系较弱，检出的风险无法进行有效的关联分析和漏洞优先级排序(VPT)。这次调研发现OX Security提出API BOM的理念和落地实践，为漏洞数据关联分析和漏洞优先级排序方面增加了新的可能。

## API BOM 获取方式

获取应用程序公开的所有 API 端点的详细列表，将检测到的安全风险映射到公开的 API（受支持的语言编写的 API）。API BOM，为用户提供应用程序代码中定义的 API 端点（内部和外部）的详细清单，相关的平台可以识别以下来源的API信息：

* 由用户的代码直接声明定义的。
* 由存储库中的 OpenAPI 规范文件定义的。
* 通过API管理平台(比如：ApiPost，Postman)等获取。
* 通过前置的WAF、RASP、API网关获取。
* 使用EBPF或者流量镜像设备获取。
* 使用IAST等Agent插桩的方式获取。
* 可以通过日志或者其他可以获取API信息的平台获取。
* 利用被动代理平台或者工具来收集(burpsuite、API Parrot等)。

其中前两点是目前OX Security已经实现的，后面几点是笔者的观点，如果有欠缺可以一起讨论。

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo5w6G3Qx05qUF3m73reT8PMDYkmtsnwDwV6zk4mmEhSOgGgsF2fnwMl4c8ibocRkjGHPPiaveciaA60A/640?wx_fmt=png&from=appmsg)

ox security api bom

## API BOM重要性

API BOM让用户能够更好地了解用户的应用对外暴露情况，进而更轻松地：

* 确保用户的所有 API 都经过适当的安全审查程序。这对于管理新添加的 API 的审核特别有帮助。
* 管理 API 中危险的请求方式，即使它们是合法且有意包含在代码中的。比如：一个包含 `DELETE` 方法可能会改变用户的应用程序配置或用户数据。安全人员要意识到代码中存在此方法，这可能存在潜在的风险。
* 方便安全运营人员优先考虑 `API` 暴露的风险（攻击者可以利用暴露的API，优先进行利用）。

## API BOM 数据分析实践

将源代码、开源组件、漏洞、情报等信息关联映射到API上，通常从以下两个维度将API和源代码进行关联 • API 是通过源代码检测发现的。 • API 是用支持此功能的语言或者框架编写的。 当 API 处理程序函数和包含问题的函数之间存在函数调用路径时，就可以认为该 API 的暴露进一步增加检出风险的威胁等级。

此处说的可能有些模糊，我举个例子来说明：

1、通过分析源代码，发现对外暴露的接口，此处目前有部分Jetbrians插件(Apipost-Helper、Cool Request)可以支持，目前这两个插件都是闭源产品，忍不住分析了一下，重新逆向实现后发现都是利用Jetbrians psiClass来解析api接口，效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo5w6G3Qx05qUF3m73reT8PMXKbCsvCzTwtOicoSrLsZicaIxVVYzRicCLkICFlibmianlbofWhlHicdrNxw/640?wx_fmt=png&from=appmsg)

Api Post效果

也可以使用JavaParser来实现，实现效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo5w6G3Qx05qUF3m73reT8PMHfLmnjCDTGfWOmqiaBq49xZQoJLQibxP2Os6VIwxj4moq19Jhs6Yl92A/640?wx_fmt=png&from=appmsg)

以上两种API解析，对于参数声明复杂参数，暂时解析不准，可以和API管理平台或者声明文件进行关联和补全。

2、将所有的数据存储到数据库或者数据湖当中，然后进行关联分析，利用API进行汇总分析，可以关联xAST分析结果，如果SCA支持漏洞可达性分析，可以将组件漏洞通过代码和API进行关联。当安全事件发生时，可以通过API迅速定位漏洞位置，及时止损。

3、利用漏洞优先级排序(VPT)模型或者平台，对所有检出结果进行排序，根据排序结果分配工单依次进行修复。其中，对外暴露的API在VPT计算模型的权重较高，修复优先级也越高。

注意：以上笔者目前只预研完成了第一步，后续关联分析都只是设想，如果哪位同学成功运营实现，请不吝赐教。

OX API BOM信息汇总效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo5w6G3Qx05qUF3m73reT8PMqvytuMlUWLZwsD5uW2IYh55PZld64icmVQVpY7M8BicjUWicetiatShz0A/640?wx_fmt=png&from=appmsg)

目前OX Security 攻击路径实现效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo5w6G3Qx05qUF3m73reT8PMEibvLWLWC23VMcHy1ibCIIJdGejBA4ma9PKLC5W0HkOrNlfJg26L9gbg/640?wx_fmt=png&from=appmsg)

可以直观分析受影响的应用、请求API、源代码提交信息、源代码路径、漏洞信息、情报等信息，提高安全运营人员的效率。此处使用的是理想的测试数据，但是在日常的安全运营工作当中，可以尽可能的关联有效信息，减少海量告警信息，优化工单分配，这就极大的提升运营效率。

## 总结

1、API BOM可以将代码和xAST工具的检测结果进行关联，拉通API和 Source Code之间关联，进而拉通所有数据之间的关系。

2、丰富ASPM管理的维度。

3、丰富VPT计算因素，如：暴露的API，URL请求路径可达等

 4、可以进行漏洞去重，并不局限于必须有漏洞编号、必须有统一的漏洞评价标准，可以通过API及关联的漏洞类型进行去重

 5、降低运营人员排查难度，通过API关联数据，一个统一的平台可以检测所有受影响的系统、代码、组件，利用AI或者人工研判灵活处置分析漏洞，根据实际情况进行漏洞修复。

## 参考

* https://docs.ox.security/a-tour-of-ox/api-bom
* https://www.apipost.cn/
* https://coolrequest.dev/
* https://apiparrot.com/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo5Zjccyeib7HeeeiaxwPjoVjaZklGM6lC9ku7HSkXQe72wGgA03a0mLZugZUpokLZbs8UVibq71Mx6OQ/0?wx_fmt=png)

代码审计SDL

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a4tp2b7vTo5Zjccyeib7HeeeiaxwPjoVjaZklGM6lC9ku7HSkXQe72wGgA03a0mLZugZUpokLZbs8UVibq71Mx6OQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过