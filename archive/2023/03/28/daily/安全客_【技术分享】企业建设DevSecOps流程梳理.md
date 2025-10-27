---
title: 【技术分享】企业建设DevSecOps流程梳理
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649784137&idx=1&sn=1345fab8e52229c6d40370c297666453&chksm=88934f26bfe4c630a88a44e3af3ced91ef9d2478a11c22cfb667326e236755d629ef64bc2a3c&scene=58&subscene=0#rd
source: 安全客
date: 2023-03-28
fetch_date: 2025-10-04T10:53:17.429228
---

# 【技术分享】企业建设DevSecOps流程梳理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb4JCSFibuB4EJaeMibBczAEmZE3bYvddy6mRz17Ass7OETBtAw6sgTw6uUiaXVibLDVe6BaanomqOpwaw/0?wx_fmt=jpeg)

# 【技术分享】企业建设DevSecOps流程梳理

Laon

安全客

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb7IaZmmMPmHW50md5brIXrBKHSich3rfcryrmlUWYwxwoyWVyNL3yZ6MDBY3pz6P0Fgm0nzqGEs6IA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

近些年DevSecOps的推广不断深入、很多大厂也在推进或已经完成这类标准化的升级。

本人在实施过程中，读了很多文章、看了很多乙方厂商的实施方案，最终准备以自己的角度来将一下DevSecOps。

希望可以对广大中小厂商或传统企业正在进行信息化建设的安全从业者们有一点小小的帮助。

首先我们来了解一下DevSecOps实施的目的以及会面临的问题。

DevSecOps实施的主要目的是安全问题左移，将大部分安全问题消灭于系统构建的雏形中。而左移带来的很大问题是，安全环节要穿插于系统设计、开发阶段。而这就意味着，我们需要让产品、开发、架构等角色零距离面对安全问题，而很多非互联网企业的问题是，业务最大，如果一定要强行推进实施的话，效果基本不会很理想。所以在这个过程中，我们需要做的不是让他们去学会这些知识，我们只需要让他们无感知的经过这个流程，拿到修改建议，干就完事儿了。

那么，另一个问题出现了，需要问题左移，又需要无感知，那就只能自动化了，所以，这就是DevSecOps了。

在我翻阅了无数DevSecOps的最佳实践、实施方案之后，发现一个问题，堆设备，但很多文章都没有给一个具体的实施场景和流程。

于是，这张图就出现了：

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb7IaZmmMPmHW50md5brIXrBp0SKuMX6U5jiaAgZpoHWxeZeIsCEuRz6qkFUDGxty6icLH09668NMwSg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

需求设计

对于大多数企业来讲，需求设计需要一个Demo，需要一个架构，把架构、产品、开发、测试拉在一起，碰一下头，设计一下数据结构，提几个问题，基本就可以确定开发方案了，所以如果我们也需要简单一点，威胁建模。

目前市面上的威胁建模工具有很多，开源的有 OWASP threat Dragon、Microsoft Threat modeling tool
商业版本的更多，具体就不发广告了，自己搜。

架构只需要将设计好的架构导入威胁建模工具，就可以拿到一份威胁报告，完善自己的架构。

研发

大多数研发人员都会使用代码托管平台来管理自己的代码更迭交付，有的公司会采用标准的CD/CI 模型，DevOps来管理代码，所以我们需要做的就是，加入他们，在没一个版本出现变化时，对系统代码进行扫描，怎么自动化Pull代码，自动化扫描就要靠安全人员来自己完成了。

而本阶段我们需要使用的工具就是、SCA、SAST以及安全编码规范了。
SCA和SAST相关的工具也不做赘述，而安全编码规范可以采用一些开源的SDK，亲测有效，敏感肌可以用。

而扫描完成后，安全团队拿到相关的报告，就可以根据其中国的扫描结果，删去误报，将准确的报告交给开发进行闭环。

测试

测试阶段相信各位就比较熟悉了，各种扫描一把梭。

而我们需要做的是不断自动化，减轻安全人员手工测试的比例，在功能测试人员进行测试的时候，将IAST的探针开启，DAST、MAST、各类扫描作为主要实施工具，安全人员更多的任务放在规则优化，业务逻辑上。

这个阶段会导出较多的漏洞，全部反馈给开发就可以。

预发布

相信大部分公司是没有预发布环境的，所以，这一阶段的任务可以放在生产环境开启的前夕，对于安全环境、用户隐私、上线风险、APP加固进行反复确认，这个部分的任务，算是系统上线前最后一道安检，所以我们选择以半自动化的方式，攻击检测，人工确认来完成。

用到的工具，安全环境会用到基线检查、端口扫描等工具；用户隐私会用到敏感信息监测的一些工具，对数据结构和数据处理做人工确认；上线风险是对由于业务优先而放弃修复的问题重新确认风险系数，确定弥补方案；App加固通过第三方的加固工具进行加壳处理。

最终在所有问题全部确认清晰后，批准上线。

运维

上线之后则是安全运维阶段，安全运维已经有很多成熟的防御和检测工具，这里重点将一下日志审计系统，日志审计系统一定是一个很重要的节点，不管是在时间溯源或者安全合规上，都是比较重要的。当防御系统被绕过后，我们最可以依赖的就是日志审计系统，对事件进行响应和处理。

这个阶段输出的产物是系统的轮询报告。

事件

接下来是对各类安全事件响应处理的部分，漏洞管理可以使用腾讯的开源Src平台，做一些定制化二次开发，其次就是补丁和组件升级的部分，建议以Puppet类似的系统来进行管理，在推送之前，做好升级测试，兼顾兼容性。

优化+分析

优化分析的部分，大多是靠系统的运行数据和相关的报告来进行优化，使我们的DevSecOps流程不断更新，不断适应业务系统，并提高安全性。

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb6OLwHohYU7UjX5anusw3ZzxxUKM0Ert9iaakSvib40glppuwsWytjDfiaFx1T25gsIWL5c8c7kicamxw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "虚线阴影分割线")

```
- 结尾 -

精彩推荐

【技术分享】对抗样本及其背后性质分析（实战导向）

【技术分享】人工智能的梦魇：对抗攻击

【技术分享】如何利用API对AI发动攻击？

![](https://mmbiz.qpic.cn/mmbiz_gif/Ok4fxxCpBb5ZMeq0JBK8AOH3CVMApDrPvnibHjxDDT1mY2ic8ABv6zWUDq0VxcQ128rL7lxiaQrE1oTmjqInO89xA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
```
```
戳“阅读原文”查看更多内容
```
```
```
```

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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