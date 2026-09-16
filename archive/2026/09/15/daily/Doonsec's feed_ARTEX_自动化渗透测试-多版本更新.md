---
title: ARTEX:自动化渗透测试-多版本更新
url: https://mp.weixin.qq.com/s/lGiyiP_cTNSlm7ZqKNAALw
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:02:59.328035
---

# ARTEX:自动化渗透测试-多版本更新

# ARTEX:自动化渗透测试-多版本更新

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于SecSentry
，作者Autumn52

![](https://wx.qlogo.cn/mmhead/Jiavz9UrH80lbAUVQFGppF2uqUD6VZ6Lkwzkoa3xj8wKY3rVnUxicFwAE5WsbdwdHkdgUzPIyv5QM/0)

**SecSentry**
.

漏洞分析、工具开发~

# ARTEX

```
https://github.com/Autumn-27/ARTEX
```

AI 自主渗透测试系统（Go 后端 + Next.js 前端）

**在线 Demo**： https://artex-demo.vercel.app/

自第一个版本发布以来，到目前为止，已经累计发布了多个版本。在这个过程中，也收到了很多师傅的使用反馈，以及一些非常优秀的 PR。感谢大家的参与和贡献，这些反馈也在不断推动项目变得更加完善。

这一阶段主要完成了以下几个方向的更新：

**1. 资产测试覆盖度**

现在可以更直观地了解资产的测试情况，包括：

* 哪些资产已经完成测试
* 哪些资产尚未测试
* 点击具体资产，可以进一步查看与该资产关联的测试记录和相关信息

通过资产测试覆盖度，可以更清晰地掌握当前整体测试进度，减少资产遗漏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkj2LxBYZf1xcv0H0VHibCvG55e3hNSHkKOuz4Vs2YS1fsW5vzzY1GZsr5DdQicibsOymU8RaZd9ll4IibcNH4zVzuQRLdUicAwdeHCU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkjVM8meCcUcibCHWwO6dnl6KPq6ib8HlfIZAMDNaHzPg5B1icCycHtWicjaiaAoIxKuvefyHXWVGj0PzvzT1crr1mnia9Knbia4cicrUhw/640?wx_fmt=png&from=appmsg)

**2. 任务系统**

新增并持续完善任务体系，目前支持：

* 任务模板
* 关联资产
* 关联子任务

![](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkjmBM70vGjfDNl0PE0fvl0JXISo9KeK0UdAGtXy5fQT2dicqNPj7wI0UIWl36H0XpaLQfpQVqibsTGtQEZI6oViaKya7mHeoBrWk0/640?wx_fmt=png&from=appmsg)

**3. LLM 链式故障自动切换**

LLM 配置增加了链式故障切换能力。

当当前使用的模型或服务出现异常时，可以按照预设配置自动切换到其他可用的 LLM，降低单一模型或服务故障对任务执行的影响，提高整体稳定性。

**4. “发现”页面能力增强**

“发现”页面现在支持从不同维度查看漏洞信息：

* 从**任务视角**查看任务执行过程中发现的漏洞
* 从**资产视角**查看不同资产关联的漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkiaEbGBNUvwiaN2MosEA7yjzaq9Q1zMHuN8nxHaib8jqicfaTF67CNnAM5QEPichvCqegzVO3PbZ7ibPc58IS1lAibCiazItyqnv83YAsk/640?wx_fmt=png&from=appmsg)

**5. Agent 事件触发机制**

通过不同类型的事件，自动触发 Agent 执行后续任务。

例如：

发现漏洞后，可以自动触发 Agent 对漏洞进行**二次验证**；

验证完成后，可以继续触发 Agent，根据指定的格式和要求**生成漏洞报告**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkjPRTickMOoicqVl6vXa4ytAQhWicw4VOscMxYpqfNOYqIOQKMibORYeKRG8elwXniafvjeu7BeB383OZoMnd0SmXQMkkqO6z1aX7QQ/640?wx_fmt=png&from=appmsg)

来自各位师傅的实战反馈:

下面这部分并不是想说 ARTEX有多厉害，严格来说，在测试目标和上下文准确的情况下，单独使用 Claude 或其他能力较强的 Agent，同样有机会完成类似的漏洞发现。最终效果很大程度上依赖的，依然是底层模型本身的能力。ARTEX 更多解决的是：如何让 Agent 在多资产、长流程、低人工干预的场景下，能够持续、稳定地运行，并把测试、验证、记录等环节串联起来。

```
相比漏洞本身，我觉得更值得关注的是背后的趋势：随着大模型和 Agent 能力不断增强，自动化攻击的成本、技术门槛和规模化难度，都在持续下降。以前需要安全人员投入大量时间进行信息收集、分析、验证的工作，正在逐渐被 Agent 自动完成。而当攻击侧逐渐具备低成本、持续化、规模化的自动探索能力之后，对防守方提出的要求也会越来越高。一个比较明显的感受是，目前 Agent 在攻击侧的应用已经开始不断出现实际案例，但在防守侧，真正能够进入日常安全运营、持续产生稳定效果的 Agent 应用，似乎还相对少见。这可能也意味着，AI 带来的变化并不只是“攻击效率提升”这么简单，而是在进一步放大攻防两侧在自动化能力上的差距。
```

0人工交互 黑盒测试出的金蝶0day

![](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkjzTAIGic3caDtBOrQRDb8BiamicjvWJaUlzG7Sq9Hib1F2SwhSfA2vLkdTgcvRabfNQFrvvISbLzibMAic5iaIictFAcA72xalq3R52v4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkgMeoIrPZsbszfnAOAo1cy3IN5vVux2HibejLQU1ibgiax6kOWqtib7px159zACctayLlKW2sbwK2ZpCeDiaficxpdLds8ibzB6nibaI78/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkiaG2Xn9XGkJWp4BwJwwVOgbOPCkkAaiaaNdjhQYRQgD5BU71icfjaI0ZBLeWRcn2afRDjmQWOKhr3H7f1XpuiaMAtDrOx3fsKzcTk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkh0TeoCRk0NHPsgEN9g5ZRMicvlofmk8plXn5r1u8VVzicPsJltkyKmHF1KzyFr89FnCUN8dQ1iavxoyL9wwtzVQlOcG0fVOCZHx4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkg84ficDpVTOVdYIVeoibqialmOsl3vm54qOibcJvFN9AvJnJclcajVDBEqHWQicktIUz3F1h9HqO90HejOJ16iaz8ohsECnSPnxQKy4/640?wx_fmt=png&from=appmsg)

## 截图预览

### 仪表盘

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkhW3fggSJqdaxjBbKTDX5gpCiacHCz8ocmhv5LMJSjS2mVoMFHkXib6pUicagNErVTjfhsibEAtDjs5xdKMXzal1eLFIARIXWNWNpA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

### 任务列表

![图片](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkgkLthAHcbQYO40ibr5hQSKwFpS2DcbV7LlJKibyRVePst5jOyFsZ6AoILNRpdUFfXkL5ctvaSYfZhUv8aVz0sUQ5j5TgmB5ju5I/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

### 任务 · 执行过程（会话 / 工具调用）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkhp5GiaxC1CjcrJEbBCYXyebUf46SyRzqlsLWoaRAkRckOeENkDFXD9lbXgRC9DJZ5KuOK4mO4zqU9TaYtzuLAJsbREH0MjKxQc/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

### 任务关联资产（任务测试中涉及到的资产）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkhYfsibyib7LCuFr7HVdm39a6hY57XWEV17sjClnG5HjrneLmAPw12409R4SbwiaHJSUNC7jsgqEHJXmlx2ianUTTkbP4Uc3Wjnk1s/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

### 探索链路

![图片](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkiaL77zrxgOzna663GTKEJibAuQvKb94j1BFUsrrDYCXlJtwcXVhQ4YrkrZHXThKuGxOicU3ovMl87nlaibKvsVnGUMmW9icVI4EzRc/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

### 发现

![图片](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkgTP7jCKRvGQB9eFaW2Wm3Pr1HmTXnRRrlvQ8m5mpXWePtETmFdKicgI3dX492uX8RYCacx4XlWzTDoC3ibaBW052N6hTSp607j0/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

### 资产

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkhrdYbCbKfGWqY3dTSgu0ugTBEHTKdM8xbYyuUOvOS67lSKksFkDZQG0nVAkWS2xeFibjtmFFBPZ0Pibceib9F0QdsiaVia2clsUU58/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

### 流量录制

![图片](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkj2fnjJZhjq7l883lIyRbgZVdL6tpby00Jr2FicTKVvTquAn2NfD39H9QTzCk6biaiam3Ru9zJLvYQaKNOKveY6fJEWOJibt3J9W1U/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

### 会话

![图片](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkhVCvL8DqCUuFt1NMDw5QKicN8Zl6s6CoBj475FwsAjmYN15Vaic1ugyG9PSTxVnYtjnVibLmIlzD0afB0CVn4k1xBvRMRoGuBwPQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

### Agent 管理

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkjU5XHPM3UYs2qYk7MONnMg9ibC37oicP3Zad4tU8dYT2Zw5M87vkhZVszypVqtjo9SUVnpnUlnmgUzibxEHEyGZuVY9RrcaCshiaY/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

### LLM 配置

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/MbnzxcvZqkhY4Qc9GjtzRG7jtOwfE721g67LWEs4UrQJubvTqQibG91yGjnVk8myKU0WljtnY5DxGJaEqQ6icTH8p3SvNCfFliarQNocXHnv8s/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

### 拦截审批

![图片](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkiagAhkgcbPncmw2MI93QRho3Ik34x7WvzEjAJjZTaNKvTxx8RxTE3Lj2NEk04446Lj2uAemQ2Yc2qVq3JRCGrrYPmhJIRnKMKs/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

### 后端日志

![图片](https://mmbiz.qpic.cn/mmbiz_png/MbnzxcvZqkgcO37RurHoobqX7OGW7QiaUD929YdIEhXpuibbynHicy1vJ5FHB0NBKibibAFTdkswWXEVbfhfTLFUdL07BVnDNibzpppZxUAQhXwzo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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