---
title: iPhone18 Pro 新增 Apple Reference Image，以像素签名对抗 AI 图像伪造；CNNVD发布信息安全漏洞周报第849期| 牛览
url: https://mp.weixin.qq.com/s/3iRgmnNM5CkoYSe8RXfmGw
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:44:52.211588
---

# iPhone18 Pro 新增 Apple Reference Image，以像素签名对抗 AI 图像伪造；CNNVD发布信息安全漏洞周报第849期| 牛览

# iPhone18 Pro 新增 Apple Reference Image，以像素签名对抗 AI 图像伪造；CNNVD发布信息安全漏洞周报第849期| 牛览

安全牛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wKeDC5RjIzGdEicGic8Pblxl64Dkuayl1T59skIeI3f3laY0mkRwiaRffWfwsibib4kS2nmUbjwGKAhRF3LeWdxcjlyHaIiad5MXrvibGpNJZNUicf0/640?wx_fmt=png&from=appmsg)

新闻速览

* CNNVD发布信息安全漏洞周报第849期
* 人工智能代理正在向公共服务发送大量新请求
* BlueMoon 漏洞利用工具包曝光，复用 Chrome 与 Windows 漏洞链实施攻击
* Windows Server 多版本 RDS 服务异常，9 月 Patch Tuesday 补丁引发故障
* GTA 6 发售临近，仿冒游戏诱饵催生大规模恶意软件攻击浪潮
* 英伟达给出 70% 营收增长指引，AI 算力系统订单高速攀升
* Astra 算力需求爆发，OpenAI 暂停 Pro 套餐新增订阅
* iPhone18 Pro 新增 Apple Reference Image，以像素签名对抗 AI 图像伪造
* WordPress 上线插件发布自动安全审查，高风险版本将被自动拦截
* Gartner：70%的SOC将试点AI代理，只有15%的人会看到结果

特别关注

**CNNVD发布信息安全漏洞周报第849期**

国家信息安全漏洞库（CNNVD）发布2026年第36期信息安全漏洞周报。8月31日至9月6日，CNNVD新增安全漏洞2098个，其中超危226个、高危806个、中危908个、低危158个；已有1471个漏洞发布修复补丁，整体修复率为70.11%。从漏洞类型看，授权问题占比最高，达16.49%。

本周重点通报WebPros cPanel安全漏洞（CNNVD-2026-17225915、CVE-2026-65643）。漏洞源于服务器后端处理域名相关参数时存在动态代码注入缺陷，攻击者持有普通cPanel账户并登录后，即可通过相关API触发漏洞，以root身份执行任意代码，进而完全控制服务器。WebPros cPanel 11.110.0.141之前版本受影响，官方已发布修复版本。

AI相关漏洞同样值得关注。Microsoft Azure AI Language Authoring因关键功能缺少身份验证，可能导致权限提升；vLLM 0.17.0及之前版本在获取用户提供的媒体URL时未限制响应数据大小，攻击者可耗尽服务器内存造成拒绝服务；Ollama 0.30.0至0.33.2在拉取tensor-layer模型时未验证重定向目标，可能导致敏感信息泄露。上述漏洞均已有官方修复措施。

原文链接：

https://www.cnnvd.org.cn/group1/M00/03/11/rBBlZ2qhEJOAJNdcAAVN\_dFQF9Q834.pdf

热点观察

**人工智能代理正在向公共服务发送大量新请求**

TechCrunch 于 9 月 10 日报道，研究人员提出 “agentic flooding（代理洪水）” 概念，用以描述 AI 智能代理代用户批量提交公共服务申请、投诉的新现象。AI 工具大幅降低填表、申诉的操作门槛，全球多地公共机构收到的业务请求数量显著上涨。

研究人员 Chris Schmitz 统计数据显示，自 2022 年 ChatGPT 上线后，美国消费者金融保护局（CFPB）投诉总量增长 5 倍；英国住房监察机构的申诉量从 2600 件增至 7000 件以上，规模翻番。研究强调，绝大多数新增诉求并非恶意垃圾信息，申请人本身具备合法主张权利，AI 只是消除了行政流程中的操作障碍，让原本不会发起申请的群体完成提交。

研究团队分析了 11 个司法辖区共 84 起相关案例，这类 AI 代提交请求包含信息公开申请、规划异议、赔偿诉求等多种类型。公共部门当前的人力、流程体系难以快速适配暴增的业务量，若不及时调整机制，后续可能出现处理延迟、资源耗尽等问题。

值得注意的是，该风险区别于传统网络攻击。AI 代理不是直接破坏系统，而是以大量合规请求消耗政务服务资源，属于新型资源耗尽类风险，对公共机构的业务审核、容量规划提出新挑战。

原文链接：

https://techcrunch.com/2026/09/10/ai-agents-are-flooding-public-services-with-new-requests/

**Astra 算力需求爆发，OpenAI 暂停 Pro 套餐新增订阅**

2026 年 9 月 10 日，受全新大模型 Astra 空前高涨的调用需求冲击，OpenAI 宣布暂停每月 200 美元 Pro 套餐的新增订阅，以此缓解算力基础设施负载，保障存量用户的服务稳定性。

该消息由 OpenAI 产品负责人 Thibault (Tibo) Sottiaux 在社交平台 X 对外公布。他表示，Pro 套餐是对系统资源消耗最高的服务档位，本次仅限制新用户开通，现有 Pro 订阅不受影响；Plus、Go 订阅方案以及 API 接口服务维持正常开放状态。

Astra 于 9 月 3 日正式上线，覆盖 Pro、Plus、Enterprise、Business 多个产品层级，该模型推理能力更强，算力消耗也显著高于前代模型。Sottiaux 此前已发出预警，Astra 带来的业务压力前所未有，公司正全力扩充算力容量，但尚未确定恢复 Pro 新订阅的时间节点，也未对外披露具体的需求规模数据。

OpenAI 选择仅暂停 Pro 新注册这一最小干预手段，优先保障存量付费用户的使用体验。这一事件也折射出高性能大模型落地阶段，算力供给与市场爆发式需求之间的突出矛盾。

原文链接：

https://techcrunch.com/2026/09/10/openai-puts-pro-subscriptions-on-hold-due-to-astra-demand/

**Gartner：70%的SOC将试点AI代理，只有15%的人会看到结果**

Gartner 报告指出，到 2028 年，70% 大型 SOC 会试点 AI 代理，用于辅助 Tier1、Tier2 安全运营，但如果缺少结构化评估，仅有 15% 能够获得可量化业务成效。当前 AI SOC 代理处于炒作周期的期望膨胀顶峰阶段。

结合 Prophet Security《2026 安全运营 AI 现状》调研，40% 安全团队已日常使用 AI，56% 正在评估或试点，仅 4% 无采纳计划。72% 使用 AI 的团队，调查耗时至少缩短 25%；但自建 AI 工具中 46% 最终被废弃，主要受维护、人员更迭影响。

Gartner 提出七大评估框架，帮助从业者甄别 “AI washing” 营销噱头，评估维度包括：是否切实降低团队工作负载、TDIR（威胁检测调查响应）业务指标、厂商可持续性、分析师能力提升效果、自动化权限边界、与现有安全栈互操作性、方案透明可审计与数据主权。

调研显示，现阶段行业普遍保守设置 AI 自主权限，57% 要求人工复核每一条 AI 判定，无企业授予完全无监督自主执行权限。报告强调，选型应当以实际安全成效为导向，而非单纯参考厂商功能清单。

原文链接：

https://www.helpnetsecurity.com/2026/09/09/prophet-security-evaluating-ai-soc-agents/

安全事件

**Windows Server 多版本 RDS 服务异常，9 月 Patch Tuesday 补丁引发故障**

2026 年 9 月 10 日，大量 Windows 管理员反馈，微软 9 月 Patch Tuesday 累积更新造成 Windows Server2019、2022、2025 平台的 Remote Desktop Services（RDS）出现严重故障，影响终端服务器业务运行。

受影响补丁编号分别为 KB5122876（Server2019）、KB5122882（Server2022）、KB5122871（Server2025）。服务器安装补丁后，RDS 可短暂正常运行数小时，随后发生异常：已有会话无法正常注销，新远程连接卡在握手阶段无法完成，部分场景只能强制硬重启恢复业务。

部分管理员调试推测故障原因为 RDS 与 Local Session Manager 发生死锁，但微软尚未确认该根因。服务器普通重启无法修复问题，回滚本次 9 月更新可以恢复 RDS 功能，但同时会卸载本月全部安全修复。

截至报道发布，BleepingComputer 已联系微软，尚未得到官方回应，暂无官方缓解方案。安全运维人员需要评估 RDS 业务风险，对相关服务器谨慎部署本次补丁，做好预案。

原文链接：

https://www.bleepingcomputer.com/news/microsoft/september-windows-server-updates-break-remote-desktop-services/

**GTA 6 发售临近，仿冒游戏诱饵催生大规模恶意软件攻击浪潮**

随着 Grand Theft Auto VI（GTA 6）临近正式发售，安全研究观测到以该游戏为诱饵的恶意软件与诈骗活动数量显著上升，攻击者利用玩家希望提前体验游戏的心理实施攻击。

当前并不存在公开的 GTA 6 测试版、可下载 Demo 以及 PC 端提前泄露版本。攻击者搭建高仿 Rockstar Games 的钓鱼网站，在社交平台、论坛、种子站点散布虚假资源，主要诈骗形式包括虚假 Beta 密钥售卖、伪造游戏安装包、仿冒 Android 测试版应用。

受害者下载运行伪造安装程序后，会触发信息窃取木马，该类恶意软件可读取浏览器保存的账号密码、会话 Cookie，劫持已认证会话，即便开启双因素认证也存在账号被盗风险。部分恶意 ISO 文件填充大量无效数据模拟大型游戏体积，内部仅隐藏体积很小的恶意载荷，还会尝试禁用系统安全防护组件。部分诈骗页面还诱导用户支付加密货币购买虚假抢先体验权限，造成直接财产损失。

安全人员提示，GTA 6 仅会通过官方商店发布，第三方站点提供的抢先下载、测试资格均为骗局，普通用户切勿运行来源不明的游戏安装文件，企业侧可针对该类诱饵 IOC 做好边界检测。

原文链接：

https://www.techradar.com/pro/security/fake-gta-6-malware-is-on-the-rise-as-release-date-nears-here-are-some-of-the-worst-scams-to-look-out-for

安全攻防

**BlueMoon 漏洞利用工具包曝光，复用 Chrome 与 Windows 漏洞链实施攻击**

2026 年 9 月 10 日，安全研究披露名为 BlueMoon 的共享型漏洞利用工具包，Proofpoint 研究人员观测到四个间谍威胁组织，在短短数天内复用同一套攻击链针对 Windows 平台 Chrome 浏览器开展攻击。

攻击以钓鱼邮件作为入口，受害者点击恶意链接后，访问恶意网页，依次利用 Chrome 的 V8JavaScript 引擎两处漏洞，再结合 Windows 漏洞突破浏览器沙箱防护，在主机内获取高权限执行能力。

相关 Chrome 漏洞分别于 9 月 3 日、9 月 8 日推送稳定版补丁，其中第一个漏洞在谷歌发布更新时就已被在野利用；Windows 端漏洞在 9 月 Patch 星期二完成修复，同样存在在野攻击情况。目前 CISA 已将这三处漏洞全部录入 Known Exploited Vulnerabilities（KEV）目录。

该事件凸显补丁发布到用户完成更新的时间差，会被攻击者充分利用。研究人员发现线索，但尚未确认该工具包是否由 AI 辅助开发，AI 可辅助攻击者解析代码变更、编写及修改漏洞代码。

安全团队提示，机构需优先处置 KEV 目录内漏洞；普通用户应及时更新浏览器与操作系统，不点击不明邮件链接，并启用实时反恶意软件防护能力。

原文链接：

https://www.malwarebytes.com/blog/bugs/2026/09/bluemoon-exploit-kit-turns-chrome-and-windows-flaws-into-attacks

产业动态

**英伟达给出 70% 营收增长指引，AI 算力系统订单高速攀升**

在高盛行业会议上，NvidiaCEO 黄仁勋重申，公司下一财年营收有望实现 70% 的同比增长，当前财年营收预计约 4000 亿美元，按该增速测算，下财年营收将接近 6800 亿美元。该增长预期高于市场分析师此前 44% 左右的一致预期，且该数值受供应链产能限制，真实市场需求比指引更为旺盛。

黄仁勋指出，外界容易将 Nvidia 简单理解为 GPU 芯片厂商，但如今公司交付的是整套复杂 AI 算力系统。其主力产品为搭载 36 颗 GraceCPU 与 72 颗 BlackwellGPU 的一体化算力设备，该系统订单月环比增速达到 27%。整套设备包含 200 万个零部件，单套算力硬件成本可达 850 万美元，同时对电力消耗要求极高，Nvidia 正批量对外交付这类大型 AI 集群。

他表示，Nvidia 深度嵌入 AI 产业生态，服务全球主流 AI 实验室与超大规模云厂商，同时持续布局合作伙伴生态与数据中心基础设施建设，企业、主权机构、工业端客户的算力采购正在快速扩张。AI 已经跨过技术拐点，能够产出具备实际价值的业务成果，算力本身已经转变为商业收入来源，这是驱动算力需求持续走高的底层逻辑。

原文链接：

https://techcrunch.com/2026/09/10/jensen-huang-explains-why-nvidia-will-grow-an-astounding-70-next-year/

新品发布

**iPhone18 Pro 新增 Apple Reference Image，以像素签名对抗 AI 图像伪造**

2026 年 9 月 10 日，苹果为 iPhone18 Pro、iPhone18 Pro Max 推出可选开启的 Apple Reference Image 图像鉴真功能，旨在应对图片篡改、AI 生成伪造内容等安全风险。

该功能依托主摄全新硬件，拍摄瞬间对每一个像素传感器数据进行签名，经由 Private Cloud Compute 生成不可篡改的数字底片。原始鉴真文件将与普通照片并存于相册，用户可对照比对，判断图片是否被后期修改，同时苹果向 iOS、iPadOS、macOS27 开放对应 API，支持第三方应用读取鉴真信息。

该功能面向新闻摄影从业者及普通用户，苹果计划在后续系统更新接入 SynthID 标准，识别 AI 生成与 AI 编辑图片，形成完整图像真实性校验体系Apple。

该功能将于 9 月 18 日在超 65 个国家上线，但受监管要求，首发阶段中国地区无法启用，欧盟机型也关闭拍摄鉴真数据的能力，不过欧盟设备仍可查看其他设备生成的参考图像，苹果尚未公布上述地区功能开放时间表。

原文链接：

https://www.helpnetsecurity.com/2026/09/10/apple-reference-image-iphone-18-pro/

**WordPress 上线插件发布自动安全审查，高风险版本将被自动拦截**

WordPress 正式启用自动化安全审查机制，所有插件版本在通过WordPress.org更新 API 分发前，都将接受安全检测，存在潜在安全风险的版本会被自动拦截。

WordPress 官方插件仓库联合负责人 David Perez 表示，插件当前版本安全，不代表后续更新不会引入漏洞或恶意代码，此前版本提交到推送至海量站点之间缺少统一审核环节。该机制的触发契机源于 7 月 28 日的安全事件：一款约 20000 活跃安装量的插件更新被植入后门，依靠人工响应，团队在 Wordfence 告警后的 26 分钟关闭该插件下载通道，但暴露了人工响应的局限性。

自 6 月 5 日起，全部插件、主题更新拥有 6 小时冷却期。冷却阶段，多套 AI 模型与 Jetpack Scan 会分析代码变更，交叉校验后生成安全评分，分数越高风险越大。高风险版本直接阻断，向插件提交者推送告警邮件；未收到邮件代表版本无异常，开发者无需操作。

安全高分不代表开发者主观恶意，无意漏洞与蓄意植入恶意代码会得到相同风险评分。被拦截后，开发者修复问题并重新发布，新版本评分低于阈值即可正常分发；对判定结果存疑可联系 Plugins Team，通常修复重发比申诉人工复核效率更高。团队会持续优化检测规则，降低误报率。

原文链接：

https://www.helpnetsecurity.com/2026/09/10/wordpress-automated-plugin-security-review/

**联系我们**

合作电话：18610811242

合作微信：aqniu001

联系邮箱：bd@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/wKeDC5RjIzGS9ozpBweZSdicW8ibiaKV1DPAY3XicrD68sw4sQVpoY0SCtlQ3x0F66wyUZKBKIH9tbbCDzyqBeSOpEWAnI6XcfED3RtEzMou3J8/640?wx_fmt=gif&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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