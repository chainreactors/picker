---
title: 用 AI 做代码审计，长亭送你一套完整落地方案！
url: https://mp.weixin.qq.com/s/wY1YoZh2KYE4nkkjsPg6Fg
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:41:49.779434
---

# 用 AI 做代码审计，长亭送你一套完整落地方案！

# 用 AI 做代码审计，长亭送你一套完整落地方案！

原创

夺旗猫
夺旗猫

长亭安全观察

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![长亭安全观察首图.gif](https://mmbiz.qpic.cn/mmbiz_gif/uX9TOlqibIRvj2ub1MWLpicrGY28iaTeGsHic9fVSRVJFo8lzgUCcsHtmkKibxibaL02SOlv6bdKbRuXoicuibvGoIOGKR5lOibcia5wOJevlSxIohVaE/640?from=appmsg)

AI 辅助开发让代码提交更快，攻击者也在用 AI 加快漏洞分析和探测。安全团队面对的压力随之增加：**新代码不断上线，谁来及时查出那些功能正常、权限却有漏洞的地方？**

**0****1**

**防守方的战场**

攻击者关注暴露在外的资产、未修复的已知漏洞、外泄凭据和配置错误；而业务逻辑、越权、租户隔离这类缺陷存在于业务代码之中。

黑盒与灰盒测试能覆盖其中一部分，但判断某个入口是否缺少鉴权、某处判断是否可被绕过，回到代码本身仍是最直接的方式。

**0****2**

**规则读不懂的四类问题**

静态分析靠语法树加预置规则批量发现固定危险写法，稳定可重复，但只能发现能写成规则的风险。它的边界主要体现在四处：

* 能识别“这里有校验”，判断不了“校验是否正确”。 一段租户 ID 比对代码，规则能识别出这里存在判断、并给出越权相关线索，但这段判断是否覆盖所有入口、比较对象是否为本次请求实际访问的资源、是否可被绕过，须结合业务与数据流才能回答。
* 调用链一旦跨出代码边界就会中断。 网关、RPC、消息队列和中间件把执行路径切分为多段，鉴权究竟由上游统一实现还是被漏掉，问题往往出现在这类衔接处。
* 鉴权往往隐含在框架约定之中。 注解、拦截器、过滤器或 AOP 统一实现鉴权，规则要理解就得逐个框架适配；企业自研的框架和公共组件，则无现成规则可依。
* 最难覆盖的是“应当实现而未实现”。 未做校验、未做租户隔离、未做服务端复核，缺失本身不具备语法形态，规则无从匹配。

这四项很难靠扩充规则库消除，因为业务规则由各家企业自定义、难以穷举成通用规则集。缺少上下文又会让告警里混入大量噪声，人工排除误报要花很多时间。

**0****3**

**AI 生成代码带来的新责任**

AI 生成代码已非零散个案。AI 能够生成功能代码，但不能稳定保证代码符合企业的鉴权、租户隔离、敏感数据和安全编码要求；训练语料中的不安全代码模式，也可能被生成的代码复制。

这类缺陷不会引发运行报错，只在特定入口被绕过，而评审与检查又难以同步覆盖产出的速度。

**0****4**

**确定性与 AI 的分工**

长亭科技《**面向安全部门的 AI 代码安全审计与治理解决方案**》，把确定性检测与 AI 能力放在一起，各自做擅长的事。

确定性静态分析提供稳定、广覆盖、可重复的检测基线，AI 原生审计补充业务逻辑、复杂调用和规则库之外的发现，AI 告警研判通过降噪和深度分析减少人工成本，治理与沉淀则把规则、模板、缺陷和报告变成组织资产。

具体能力有**两种形态**。

算力资源有限、希望快速验证提效价值的，用确定性静态分析加 AI 增强。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uX9TOlqibIRufGY4brRoY4XbrdYnHof9I8Jy4a9eiaU2eagJlrwbQUZK5oiccMWjzW304muKHT3c2QzNO21K3NzpELYrDDfHoqbrm2PUeLWUcE/640?wx_fmt=png&from=appmsg)

算力条件较好、关注重点系统的，用 AI 原生审计。

![](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRsrvc3V3YLWiaJtKl60Tx0soC4xRbfxFRmRPckicTibKJXwbCuVxo1pepRu0NyibvWEWiaib0fNYktX5wswQI1M3wWib9ASZibz8bDDfpg/640?wx_fmt=png&from=appmsg)

审计结论再通过研发协同能力回到 IDE、CLI、MR 和缺陷平台，由研发人员或 AI 员工完成修复。

**0****5**

**每条结论都能查到行号**

代码审计的输入是源码、构建产物或代码变更，任务是安全漏洞、业务逻辑、编码规范或合规检查，证据是文件、行号、调用关系和数据流，输出是风险等级、审计结论和修复建议。四要素齐全，每条结论都能落到具体位置，对错可以逐条核对。

在代码审计里，AI 的效果无需依赖描述佐证，在真实项目中执行一次即可验证。对安全部门来说，这一点尤其有价值。相较于泛化问答类应用，代码审计与现有安全职责直接关联，能形成从“发现风险”到“形成报告”的可度量建设方向，这是可以由安全部门自主验证效果的 AI 场景。

本方案支持私有化部署，满足源码不出域、权限控制与审计留痕要求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uX9TOlqibIRsk9CqLcephjzOL6NsKIQnFf4SdCh2oAW0pkG7WkuVwXGULodZTGxXciaSVMTibYmzSJOsUluiaGPuasNC6RXJAM9NP3xK982o7q8/640?wx_fmt=png&from=appmsg)

👆扫描文中二维码或点击下方「阅读原文」，免费获取完整版方案原文。

![长亭安全观察尾图.png](https://mmbiz.qpic.cn/sz_mmbiz_png/uX9TOlqibIRv4wibwpRb3DqnZzCkVrfd4mKYu9juP3re0yR5Ofj0GN8jSRUvqgNYXhD5yiaqgVSicibEeXfAxXHlphtR4x8PDULcfdX9SyibNeYoY/640?from=appmsg)

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NCzpaOPov3N5yAlpsNymmdInF4KibIIE3jw5ia8hFSctjBqgeVBic5zBdVpe6rTWiaL9hEsh0eSibNPVlBWrSnNJpPg/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过