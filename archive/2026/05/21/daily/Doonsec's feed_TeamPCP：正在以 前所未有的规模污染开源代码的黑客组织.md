---
title: TeamPCP：正在以 前所未有的规模污染开源代码的黑客组织
url: https://mp.weixin.qq.com/s/jkqt2bsBpZsWhOXIgYoW0A
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:57:28.294945
---

# TeamPCP：正在以 前所未有的规模污染开源代码的黑客组织

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrlzYrnzOyPaiaArWX7fBphuOtkQdEuR2ayicKNYric7ccibxEicPVxNT4gbKFm9Tg5pSoCs4yTzE4EXzSL9eJLmc9Pf4hRcsTvrgdg/0?wx_fmt=jpeg)

# TeamPCP：正在以 前所未有的规模污染开源代码的黑客组织

原创

2号员工
2号员工

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

软件供应链攻击曾经相对罕见，黑客通过篡改合法软件植入恶意代码，能将任何无辜应用变成入侵受害者网络的危险跳板，这种隐蔽威胁一直让网络安全界如鲠在喉。

如今，一个网络犯罪组织已将这种偶发噩梦变成了几乎每周上演的常态，他们篡改了数百个开源工具，通过勒索受害者获利，并在全球软件开发所依赖的整个生态系统中播下了新的不信任。

本周二晚间，开源代码平台 GitHub 宣布遭遇典型的软件供应链攻击，一名内部开发者安装了被投毒的 VSCode 扩展。VSCode 是微软旗下全球开发者广泛使用的代码编辑器。此次攻击的幕后黑手是日益臭名昭著的组织 TeamPCP，该组织声称已经访问了大约 4000 个 GitHub 代码仓库。GitHub 的声明证实，他们已发现至少 3800 个被入侵的仓库，同时指出根据目前的调查结果，这些仓库仅包含 GitHub 自身代码，不涉及客户代码。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoFrFEo9zdOx9Q4oXEPfTn7IVBhzP3fTx7iaFOkiceudum8q2t4E7nSCcErC2bLvhHFSb7cEmnzq4lR77sRnEjWGs8F8n3ibTXkJE/640?wx_fmt=png&from=appmsg)

"我们今天在这里出售 GitHub 的源代码和内部组织信息，"TeamPCP 在网络犯罪论坛 BreachForums 上写道，"主平台的所有内容都在这里，我非常乐意向感兴趣的买家发送样本，以验证信息的绝对真实性。"

这次 GitHub 被入侵只是冰山一角，它只是这场史上持续时间最长且仍在持续的软件供应链攻击狂潮中的最新一起。

数据显示，仅在过去几个月里，TeamPCP 就发动了 20 波供应链攻击，在超过 500 个不同的软件中隐藏了恶意软件，如果算上所有被劫持的代码版本，这个数字已经超过一千。

这些被污染的代码已经让 TeamPCP 入侵了数百家安装相关软件的公司。GitHub 只是该组织一长串受害者名单中的最新一个，这份名单还包括人工智能公司 Anthropic 和数据外包公司 Mercor。

TeamPCP 之所以能在短时间内发动如此大规模的攻击，核心在于他们形成了一套针对软件开发者的循环利用攻击模式。

黑客首先获得某个网络的访问权限，而这个网络正在开发一款被程序员广泛使用的开源工具，例如导致 GitHub 被入侵的 VSCode 扩展，以及本周早些时候被 TeamPCP 劫持的数据可视化软件 AntV。

黑客在该工具中植入恶意软件，这些恶意软件最终会出现在其他软件开发者的机器上，其中一些开发者正在编写其他供程序员使用的工具。恶意软件允许 TeamPCP 窃取凭证，这些凭证又让他们能够发布这些软件开发工具的恶意版本。这个循环不断重复，TeamPCP 入侵的网络数量也随之滚雪球式增长。

最近，该组织似乎已经使用一种名为 Mini Shai-Hulud 的自我传播蠕虫实现了许多攻击的自动化。

这个名字来源于蠕虫创建的 GitHub 仓库，这些仓库包含从受害者那里窃取的加密凭证，每个仓库都包含短语 "A Mini Shai-Hulud Has Appeared" 以及其他一些科幻小说《沙丘》的引用。

这条信息不仅指向《沙丘》中的沙虫，还指向 2025 年 9 月出现的另一个类似的供应链入侵蠕虫 Shai-Hulud，不过目前没有证据表明 TeamPCP 是那个早期自我传播恶意软件的幕后黑手。

研究人员认为，他们绝对追求大规模曝光，非常在意获得广泛关注。

该组织的一个暗网站点链接到可能用于赎金谈判的商业联系方式，站点背景是《黑客帝国》风格的瀑布式数字流，播放着雷鬼融合音乐，并显示文字 "TEAMPCP: The Cats Hijacking Your Supply Chains"。

事实上，TeamPCP 并非一开始就采用这种供应链攻击策略，他们的演变过程清晰地展示了威胁行为者如何快速迭代战术。

在采用当前的供应链攻击策略之前，TeamPCP 于 2025 年底首次出现，当时他们利用云配置错误和 Web 应用开发工具 Next.js 中的一个漏洞部署僵尸网络，进行凭证窃取和加密货币挖矿等攻击。在此期间，该组织开始依赖蠕虫技术，并越来越成功地获取静态凭证和身份验证令牌，从而深入受害者系统。

TeamPCP 似乎以经济利益为主要动机，他们经常对目标部署勒索软件或数据勒索活动，同时也愿意向任何买家出售受害者数据。

例如在最近的 GitHub 事件中，他们在 BreachForums 网站上写道 "这不是赎金，我们不在乎勒索 GitHub，只要有一个买家，我们就会销毁我们这边的数据。" 他们还添加了一句对 GitHub 的隐晦威胁，可能是为了迫使公司付款："看起来我们很快就要退休了，所以如果找不到买家，我们将免费泄露所有数据。"

情况变得越来越复杂，TeamPCP 在 2026 年 4 月开始转向勒索软件即服务模式，与网络犯罪平台 BreachForums 和 DragonForce 建立了合作伙伴关系。

该组织有时似乎也涉足地缘政治，他们部署了一个地理针对性的擦除器，被研究人员命名为 CanisterWorm，这个恶意软件会感染所有 Kubernetes 云基础设施，但只对伊朗目标部署破坏性擦除器。

一个自称是 TeamPCP 的实体还泄露了原始 Shai Hulud 蠕虫的源代码以及详细文档，不过其泄露动机尚不清楚。

2026 年 3 月以来，TeamPCP 的攻击规模急剧扩大，形成了连锁反应式的供应链入侵，造成了极其严重的后果。该组织在开源安全扫描器 Trivy 中嵌入了信息窃取程序，然后利用这次攻击窃取的凭证入侵了托管在流行 Python 软件仓库 PyPI 上的人工智能应用程序编程接口工具 LiteLLM 的某些版本。

该组织还污染了 Web 应用安全公司 Checkmarx 的基础设施，攻击了开发服务器 pgserve，入侵了 Web 应用库 TanStack 以及企业人工智能平台 Mistral AI。除了 GitHub 之外，TeamPCP 对软件服务提供商的攻击还导致欧盟委员会公共网站被入侵，Anthropic 的 Claude 源代码泄露，OpenAI 的两名员工设备被入侵，数据外包公司 Mercor 被攻破以及许多其他事件。

使这次行动如此成功的最大机会因素是这些环境中存在的长期有效凭证，即使没有使用 LiteLLM 或任何其他已被入侵的软件包，更换你的令牌也至关重要。如果你有 Gitlab 和 GitHub 个人访问令牌，请立即轮换它们。

AWS、Azure、GCP、阿里巴巴、甲骨文所有这些云服务的凭证都在被窃取。

面对 TeamPCP 掀起的这场污染代码的浪潮，如何在供应链攻击日益增多的时代安全使用开源软件，成为了整个行业必须面对的核心难题。

建议采取一些保护措施，例如对开源工具的更新进行分级管控，也就是优先审查并安装安全更新，但在其他情况下推迟安装新发布的代码，因为这些新代码可能是恶意的。

在最近一次 TeamPCP 的恶意更新事件中，一些公司的杀毒软件在几分钟内就检测到了供应链入侵并警告了客户，但许多软件用户启用了自动更新，已经下载了恶意版本。

"你不应该总是安装最新版本"

这句话成为了网络安全界最讽刺的一句话。

往期：

[住宅代理网络背后的僵尸网络故事](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186762&idx=1&sn=60bb41f1dd03b3a0982bd0f9b51c031e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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