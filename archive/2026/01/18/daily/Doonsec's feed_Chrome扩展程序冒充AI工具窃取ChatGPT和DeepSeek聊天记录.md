---
title: Chrome扩展程序冒充AI工具窃取ChatGPT和DeepSeek聊天记录
url: https://mp.weixin.qq.com/s/u5fk1VF_8RstUBa3QH0UpA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:42:25.625693
---

# Chrome扩展程序冒充AI工具窃取ChatGPT和DeepSeek聊天记录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0HlywncJbB3dJBicLwCT1qkDbh6vz1M5wPkyySnqbP8bjY2NMRQ783ob5oury2FtUIAxiaHYKfnO0M01kTalOA5A/0?wx_fmt=jpeg)

# Chrome扩展程序冒充AI工具窃取ChatGPT和DeepSeek聊天记录

TtTeam

![]()

在小说阅读器中沉浸阅读

安全研究人员发现两款Chrome浏览器扩展程序，它们旨在悄无声息地收集用户信息并将其传输到攻击者控制的外部服务器。这两款扩展程序在Chrome网上应用商店的下载量超过90万次，表明在恶意行为曝光之前，它们已被广泛使用。

这两款扩展程序都标榜自己是生产力工具，允许用户直接通过浏览器侧边栏与多个人工智能模型进行交互。实际上，它们的界面和行为与AITOPIA开发的合法人工智能侧边栏扩展程序极为相似，使用户感觉熟悉且值得信赖。虽然其核心功能看似合法，但隐藏的逻辑却能在用户不知情的情况下持续收集数据。

涉及哪些 Chrome 扩展程序？

此次宣传活动的核心是两款以人工智能为主题的Chrome扩展程序：

* 使用 GPT-5、Claude Sonnet 和 DeepSeek AI 开发的 Chrome 版聊天 GPT，拥有约 60 万用户
* AI 侧边栏集成了 Deepseek、ChatGPT、Claude 等工具，拥有约 30 万用户。

这些扩展程序在品牌形象和行为上都与正规的AI侧边栏产品极为相似。这种相似性降低了用户的疑虑，帮助它们赢得了用户的信任，甚至在Chrome网上应用商店中获得了显著的排名。

恶意扩展程序是如何收集数据的？

安装完成后，系统会提示用户授予所谓的匿名或非身份识别分析权限。一旦接受，扩展程序就会激活一段代码，用于监控所有已打开的 Chrome 标签页中的浏览行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB3dJBicLwCT1qkDbh6vz1M5wuiatC8pgSRnGnDhROOeyqvZ1icoU0nfo3CUVN4ToHPnXcVUrXPFibXrQw/640?wx_fmt=png&from=appmsg)

当用户访问人工智能聊天机器人网站时，这些扩展程序会检查网页的DOM结构，定位与聊天对话相关的特定元素。然后，它们会提取用户输入和人工智能生成的回复，以及嵌入在页面中的会话相关元数据。这些信息，连同打开标签页的完整URL，都会存储在本地，并每30分钟分批传输到远程服务器。

收集过程在获得初步同意后无需额外交互，允许扩展程序在后台持续运行。

此次攻击活动之所以成功，很大程度上是因为这些扩展程序在外观和功能上都与合法的AI侧边栏工具极为相似。攻击者通过提供用户期望的体验，同时以模糊的分析语言悄悄请求广泛的权限，使恶意行为与正常的浏览器活动融为一体，从而避免了立即引起怀疑。此外，攻击者还利用人工智能驱动的Web开发平台Lovable发布隐私政策并托管支持基础设施组件。

泄露了哪些类型的信息？

这些扩展程序收集的数据不仅限于基本的使用指标。研究表明，泄露的信息可能包括以下内容：

* 人工智能聊天对话可能包含专有代码、商业讨论或个人数据
* 所有打开的 Chrome 标签页（包括内部或受限资源）的完整 URL
* 搜索查询揭示了研究主题或调查活动
* 可能暴露标识符或会话相关信息的 URL 参数

由于许多用户依赖人工智能工具来完成与工作相关的任务，因此泄露的数据可能会对职业或组织产生重大影响。

虚假Chrome扩展程序的状态

这两款扩展程序于 12 月下旬被举报至谷歌。披露时，这两款扩展程序仍可在 Chrome 网上应用商店下载，但其中一款已被移除推荐状态。

完整的技术分析报告（包括基础设施详情和入侵指标）

对用户和组织的关键建议

对于个人用户而言，定期检查已安装的扩展程序并移除不必要或不熟悉的程序可以降低风险。对于企业而言，研究结果凸显了监控基于浏览器的威胁、控制扩展程序使用以及保持对客户端数据流可见性的重要性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB3dJBicLwCT1qkDbh6vz1M5wen414zJwVl5eDL6iaxlsJfBbyiab0ENRG83zqh9H9ADg1uKtHkic4JmYA/640?wx_fmt=png&from=appmsg)

IOC

恶意Chrome扩展程序

Chat GPT for Chrome with GPT-5, Claude Sonnet & DeepSeek AI

Extension ID: fnmihdojmnkclgjpcoonokmkhjpjechg

Version: 1.9.6

SHA-256: 98d1f151872c27d0abae3887f7d6cb6e4ce29e99ad827cb077e1232bc4a69c00

AI 侧边栏，包含 Deepseek、ChatGPT、Claude 等插件

扩展 ID：inhcgfpbfdjbjogdfjbclgolkmhnooop

版本：1.6.1

SHA-256：20ba72e91d7685926c8c1c5b4646616fa9d769e32c1bc4e9f15dddaf3429cea7

已知的命令与控制 (C2) 域和端点

* deepaichats[.]com
* chatsaigpt[.]com
* chataigpt[.]pro
* chatgptsidebar[.]pro
* deepseek[.]ai
* chatgptbuddy[.]com

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

TtTeam

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

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