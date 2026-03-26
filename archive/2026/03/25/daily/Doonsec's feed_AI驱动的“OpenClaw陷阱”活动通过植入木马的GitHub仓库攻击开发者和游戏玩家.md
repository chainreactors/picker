---
title: AI驱动的“OpenClaw陷阱”活动通过植入木马的GitHub仓库攻击开发者和游戏玩家
url: https://mp.weixin.qq.com/s/JRV_MmwjosBUeHzr14rsQg
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:28:04.709296
---

# AI驱动的“OpenClaw陷阱”活动通过植入木马的GitHub仓库攻击开发者和游戏玩家

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7Ncvo2xJLia3BW4j5QMGRfGrQ3Uqm7ib5wiadCvs41B1OW5skJ2UFnXgFrM5GxNEuCYecb0DT6R9HtOWiaLVyibJb6icIxkTvM04eoec/0?wx_fmt=jpeg)

# AI驱动的“OpenClaw陷阱”活动通过植入木马的GitHub仓库攻击开发者和游戏玩家

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

大规模恶意软件攻击利用 GitHub，通过看似可信但已被植入木马的存储库，向开发者、游戏玩家和普通用户传播基于 LuaJIT 的定制木马。

该活动被追踪为“TroyDen 的诱饵工厂”，涉及 300 多个投递包裹，并使用了人工智能辅助诱饵，包括 OpenClaw 部署工具、游戏作弊程序、Roblox 脚本、加密机器人、VPN 破解程序以及 Telegram 推广的手机追踪器。

该活动的核心是一个虚假的存储库 AAAbiola/openclaw-docker，它伪装成合法的 OpenClaw AI 项目的 Docker 部署助手。

该仓库看起来很可信：它重用了真正的上游 OpenClaw 源代码，提供了功能齐全的 Dockerfile 和安装脚本，列出了多个贡献者，甚至还有一个匹配的 GitHub Pages 站点和 SEO 优化的标签，例如 ai-agents、docker、openclaw、LLM 和 security。

为了进一步增强信任，运营者使用 TroyDen 的身份，通过一次性帐户添加星标和分支来制造社会认同，然后悄悄地将恶意 Diatrymiformes 目录插入到一个看似无害的“更新 README.md”提交中。

来自此 OpenClaw 部署程序的同一个 771 KB 木马二进制文件再次出现在其他诱饵中，包括“电话号码位置跟踪工具”存储库和“钓鱼星球增强菜单”作弊程序，所有这些诱饵都会同步轮换其活动有效载荷链接。

Netskope Threat Labs发现了一个与恶意软件活动相关的线索，该活动在多个 GitHub 存储库中运行，涉及 300 多个分发包，其中包括 OpenClaw 部署。

在更广泛的集群中，诱饵名称混合了工具状标签和晦涩的生物学、拉丁语和医学术语（例如 Diatrymiformes 和 Chelydridae），这种模式强烈表明这是人工智能生成的命名，而不是大规模的人工编辑。

这与之前关于利用人工智能辅助的虚假 GitHub 存储库来传播 LuaJIT 加载器和信息窃取程序（如 Lumma Stealer）的研究相呼应。

## **AI驱动的OpenClaw陷阱**

TroyDen 工具链的核心是一个双组件 LuaJIT 加载器，其设计目的就是为了绕过自动分析。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7N9o9G7TBLE8sgib6kYhblftwbgAU0WxGrF9KvBIicLY8VobPav103DZWicOfS2Zic5N6tpx5VGXbF9R3AfS1RhB8kibUzLehZAKTJU/640?wx_fmt=png&from=appmsg)

受害者下载一个 ZIP 文件，其中 Launch.bat 只是简单地运行 unc.exe 并将 license.txt 作为参数，其中 unc.exe 是一个经过剥离的 LuaJIT 2.1 解释器，而 license.txt 是一个经过 Prometheus 混淆的加密 Lua 有效载荷。

单独提交的每个文件看起来风险都很低：解释器看起来像一个通用的 Lua 运行时，脚本类似于不透明数据，这使得它们能够绕过许多单独分析文件的静态和行为沙箱。

早期版本使用更明显的 lua.exe 文件名，但当前的 1.8 有效载荷隐藏在通用的 unc.exe 名称背后，同时保持相同的行为。

脚本执行完毕后，会执行五项反分析检查，包括调试器检测、低内存和短运行时间过滤器、权限检查和主机名检查，然后调用相当于大约 29,000 年的 Sleep 调用来耗尽有时限的沙箱。

Netskope 分析师通过修补睡眠漏洞绕过了这一问题，结果显示，在真实环境中，该恶意软件会在不到 30 秒的时间内完成其核心活动。

该设计与自 2024 年以来记录在案的不断壮大的 Prometheus 混淆 LuaJIT 加载器家族相符，这些加载器使用类似的防篡改技巧、基于 FFI 的 Windows API 调用和先截屏后发送的信标，尤其是在以游戏为中心的活动中。

一旦反分析检查通过，有效载荷就会通过四个注册表编辑来关闭 WinINet 代理自动检测，从而绕过企业检查代理，然后通过 ip-api.com 执行地理位置查找，以记录受害者的 IP、国家/地区和 ISP。

它立即捕获完整的桌面屏幕截图，格式为 24 位 BMP，并通过 HTTP 使用 multipart/form-data 将其上传到托管在法兰克福基础设施上的命令与控制 (C2) 服务器，在所有观察到的执行过程中都使用硬编码的多部分边界和静态文件名字段。

由“分发的二进制文件 `AAAbiola/openclaw-docke`”也出现在第二个GitHub存储库中：  `mikenob39wang/phone-number-location-tracking-tool`，该存储库宣传了一种声称可以从电话号码中提取GPS坐标的工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7O9FXlHftsSSI1NYbEiciaQaLvklbvVpWSq0iaYVZdj1YaDib3hrkSibBZbVFVtOUDOqCnmC2jianeqoCa3ibiaorkibH2kMo4wuNOXOHBw/640?wx_fmt=png&from=appmsg)

C2 服务器会以 JSON 格式响应，其中包含加密的任务和加载器 blob，这些内容会保存到用户的“文档”文件夹中，并通过 nginx 负载均衡在前端添加其他节点，从而在同一 ASN 上提供至少八个活动的 HTTP 端点。

动态分析显示，该加载器在启动时引入了 DPAPI 和 advapi32 加密 API，这种行为与浏览器凭证收集一致，并且与之前最终推出 Lummastealer或 RedLine 的 LuaJIT 加载器活动相一致。

尽管 TroyDen 的基础设施所交付的最终有效载荷尚未被恢复，但其 XOR 密钥是在 Lua VM 内部运行时组装的，共享的代码库、C2 共置以及类似信息窃取者的行为都表明，窃取凭证是其主要目标。

## **以数量为先的AI辅助恶意软件**

VirusTotal 遥测数据将 300 多个不同的分发包与 TroyDen 的法兰克福 C2 节点关联起来，涉及的受众群体从开发者和人工智能爱好者到 Roblox 玩家以及寻求破解版 VPN 和手机追踪器的用户。

这种广度，再加上反复使用类似人工智能的命名词汇和精心制作但具有欺骗性的文档，印证了人工智能辅助的诱饵工厂追求的是产量，而不是精准定位。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NHtcv5NGb80hB4M8d1JPafBpw90Xt2mDiaMtWiaLggH7xn9l0cMTVmMxpLv5m3pwtqrlrN1P4TXEZoBrhngYZbEJvbfKlo7Hmyo/640?wx_fmt=png&from=appmsg)

Netskope 指出，该攻击链经过精心设计，旨在突破自动化防御：分割文件加载器、极端的睡眠延迟、解释器加数据配对以及基于 GitHub 的社会证明，所有这些都确保只有当人类分析师在上下文中执行整个链时，威胁才会完全暴露出来。

Netskope 高级威胁防护最终通过行为启发式方法而非签名检测到了伪造的 OpenClaw 部署程序和相关软件包，在造成损害之前阻止了客户，并在 2026 年 3 月 20 日将关键存储库报告给了 GitHub 。

对于防御者而言，任何将重命名的脚本运行时与不透明的“数据”文件（尤其是在 AI 工具或游戏作弊代码库中）相结合的 GitHub 托管下载，都应被视为高优先级分类候选对象，并密切监控 LuaJIT、Prometheus 混淆的有效载荷和先截图的 C2 信标。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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