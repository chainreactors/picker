---
title: 钓鱼不用假网站了？拆解 EvilTokens：一个把\"盗号\"做成订阅制的设备码钓鱼平台
url: https://mp.weixin.qq.com/s/8hfSoyolJWCfIClbB5YNFA
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:03:57.193575
---

# 钓鱼不用假网站了？拆解 EvilTokens：一个把\"盗号\"做成订阅制的设备码钓鱼平台

# 钓鱼不用假网站了？拆解 EvilTokens：一个把"盗号"做成订阅制的设备码钓鱼平台

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

威胁研判 · 钓鱼即服务（PhaaS）· 身份攻击

钓鱼不用假网站了？拆解 EvilTokens
把"盗号"做成订阅制的设备码钓鱼平台

受害者访问的是微软官网，完成的是真实的多因素认证，账号却照样沦陷——2026 年最值得关注的身份攻击手法。基于 Microsoft Threat Intelligence 最新披露，结合 Sekoia、Huntress 等机构的独立研究完整复盘。

· EvilTokens / Storm-2992 / 设备码钓鱼　· PhaaS / BEC / AiTM　· 2026 年 9 月

01 事件速览：12000 个邮箱背后的产业化钓鱼

2026 年 9 月 22 日，Microsoft Threat Intelligence 发布深度报告，披露了一个名为 **EvilTokens** 的钓鱼即服务（Phishing-as-a-Service, PhaaS）平台，并将其幕后开发与运营者追踪为 **Storm-2992**。

几个关键点：

* 该平台自 **2026 年 2 月**出现，迅速成为使用最广泛的 PhaaS 平台之一；
* 全球范围内，依托该平台发起的商业邮件入侵（BEC）活动共攻陷了 **超过 10,000 家组织中的 12,000 余个邮箱**；
* 受害组织覆盖批发分销、建筑、金融服务、房地产、高等教育、医疗等行业，受害活动最集中的国家为美国、加拿大、英国、澳大利亚、印度和法国；
* 微软数字犯罪部门（DCU）已联合多方合作伙伴，对支撑 EvilTokens 运营的基础设施实施了协调打击。据外媒报道，此次行动获得美国弗吉尼亚东区联邦地区法院授权，Cloudflare、Railway、SpyCloud、OpenAI、Coinbase、The Shadowserver Foundation、TRM Labs 及 Health-ISAC 等参与协作；英国伦敦警察厅亦于 9 月 11 日逮捕了两名与该犯罪运营相关的男子。

与传统钓鱼不同，EvilTokens 的核心武器不是仿冒登录页，而是**滥用微软合法的 OAuth 设备码认证流程（Device Code Flow）**——受害者全程在真实的微软页面上操作，MFA 也正常通过，但令牌却落入了攻击者手中。

02 先补一课：什么是设备码钓鱼？

要理解 EvilTokens 的危害，必须先理解它滥用的协议设计。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqicoiaFicVAry4hU0MAdnYiaBBgokcwAORjx1FI0Pcz4jV2SS8jrvG06jujl7GKj2vp5AhGQbKG1Xpb64R0LmiaNiaOsvCjicsv6sGOd0/640?wx_fmt=png&from=appmsg)

**图1 | 设备码认证流程：合法用途 vs 钓鱼滥用对比**（图源：本文根据 Microsoft Threat Intelligence 报告内容绘制）

合法的设备码流程

设备码认证（Device Authorization Grant，RFC 8628）是为**输入能力受限的设备**设计的 OAuth 流程，典型场景包括智能电视、打印机、Teams 会议室设备、会议终端等——这些设备无法完成标准的交互式登录。其工作方式是：设备上显示一个短代码，用户在另一台设备（如手机或电脑）的浏览器中访问验证页面并输入该代码，即可完成认证。

安全折衷点在哪里

这个流程存在一个天然的安全折衷：**发起认证的会话与用户实际完成认证的会话，并不强绑定在同一上下文中**。换句话说，服务器无法确认输入代码的用户，授权的到底是不是他自己想登录的那台设备。

攻击者正是利用这一点，把"发起请求"和"完成认证"两个环节解耦，从而绕开传统的 MFA 保护——因为 MFA 验证的是"你是谁"，而不是"你在为谁开门"。

设备码钓鱼的攻击模型

设备码钓鱼发生时，攻击者将自己插入这个流程：

1. 由**攻击者**（而非合法设备）发起设备码认证请求；
2. 攻击者把拿到的代码通过钓鱼诱饵发送给受害者；
3. 受害者在真实的微软验证页面输入代码、完成认证（包括 MFA）；
4. 受害者在这一过程中**不知不觉地授权了攻击者的会话**——全程无需窃取任何密码或验证码。

令牌到手后，攻击者即可以受害者身份访问其账户。微软建议：凡是不必要的场景，应直接封禁设备码流程；如组织确需使用（如 Teams 设备），应将例外范围限定到特定的 Teams 设备资源账户，并在条件访问策略中排除设备注册服务（Device Registration Service）资源。

03 平台解剖：1500 美元"入门费"的犯罪订阅生意

EvilTokens 的运营模式几乎照搬了正规 SaaS 的商业套路。

销售渠道与定价

Storm-2992 通过 **Telegram 频道**向网络罪犯宣传和售卖 EvilTokens 服务——Telegram 提供的匿名性、跨平台访问、文件共享与频道广播能力，使其成为这类灰色生意的首选阵地。运营者在 Telegram 上推广钓鱼工具包、发布更新公告、与订阅者协调，甚至提供"客户支持"。

定价结构如下：

* **初始购买费：1,500 美元**；
* **月度订阅费：500 美元**，用于持续访问工具包和控制面板；
* 另有按 30 天计费的附加产品线，包括 **Antibot 重定向器、B2B Sender、Office 365 Capture Link 和 SMTP Sender** 等。

平台甚至还设有"推荐返佣"机制——订阅者向他人推荐该服务，可获得加密货币奖励。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq84fqUSS8N1icMn5nMYIgz4lk6Ig0fXaTJpSKY0gTLvEibSPj9a2jlr1HPAOPibvOlpqDUfW4qUbvQIcLic70F9p3FdGxYISjIIiaicM/640?wx_fmt=png&from=appmsg)

**图2 | EvilTokens Telegram 商店机器人界面**，可见 1,500 美元初始购买费、500 美元/30 天续费等定价信息（图源：Microsoft Security Blog）

客户面板：钓鱼活动的"一站式控制台"

订阅者登录面板后，可以看到支撑钓鱼活动所需的全部核心组件：预置模板、常见诱饵格式的附件文件、域名与托管配置、重定向逻辑和受害者追踪。

部署时，订阅者首先选择部署方式（Cloudflare Workers/Bunny 或 PHP 托管），然后可以高度自定义以下选项：

* 捕获模式（Capture Mode）
* 布局与模板（Layout & Template）
* 代码展示样式（Code Display Style）
* 页面语言（Page Language）
* CAPTCHA 验证
* AI 模式（AI Mode）
* 捕获文本（Captured Text）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqibjibRvyx40TmHdakElr1gjMHT8h73TFPmS9tichTfVhMd7OMvzq17IQpTpmS5D40yVUcWPezWwiaozCKpGHuJvIMBia9gEeDKks5Q/640?wx_fmt=png&from=appmsg)

**图3 | EvilTokens 平台欢迎页**：订阅者可选择 Cloudflare Workers/Bunny 或 PHP 托管，并自定义捕获模式、模板、CAPTCHA、AI 模式等部署选项（图源：Microsoft Security Blog）

平台共提供 **44 种主题**用于定制邮件模板和落地页（包括文字与配色），诱饵主题涵盖发票、招标书（RFP）、共享文件，以及文档签署服务、微软云服务、第三方云身份/文件托管/支付平台、语音信箱和 eFax 等。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq8qcLIicFnhicxY7W4H7JQ5sAShYB7w7wJWmwQZnicCJCHdiaESwIBkkPeGvYHzfgBllibsC1bycqxF1SY47QfmROcDPQfcbpdibDI6g/640?wx_fmt=png&from=appmsg)

**图4 | EvilTokens 模板定制界面**：内置 DocuSign、微软云服务、语音信箱、eFax 等多种仿冒主题，可自定义落地页与邮件模板（图源：Microsoft Security Blog）

令牌管理与 AI 能力

令牌捕获后，EvilTokens 为订阅者提供对受害者邮箱的完整访问，并附赠一系列"增值服务"：

* **管理员检测**（admin detection）；
* **令牌自动刷新**（token auto-refresh）；
* **收件箱自动扫描**：通过关键词告警筛选高价值内容，经 Telegram 推送给攻击者；
* **AI 助手**：基于受害者邮箱中可访问的内容，帮助攻击者量身定制针对特定目标的钓鱼邮件，并筛选高价值目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq992QL7svG7xN76Nfb1Q5bR06EmVicTiaN833BZiaXOnc1zbbfGZTKezAr6r0ro5hKtkTFB4KjNiczvHs8FQiaT5cU5tbXfjxVftbBI/640?wx_fmt=png&from=appmsg)

**图5 | EvilTokens 令牌管理面板**：提供邮箱完整访问、管理员检测、令牌自动刷新、关键词告警等功能，并附机器人防护、管理员标记等辅助说明（图源：Microsoft Security Blog）

04 攻击链复盘：从一封"密码到期"邮件开始

结合微软披露的样本分析，EvilTokens 的完整攻击链可以还原为以下阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqibEsn6GZbDbOGsLEF5xHc2g0OYOGd9Zu0l8icoMQs0SFMx4RgvbBySzIHDcafPmAUjMSrAMqhGYdDm6Y5TEM6s1hXNnQHJiaFKUA/640?wx_fmt=png&from=appmsg)

**图6 | EvilTokens 设备码钓鱼攻击链全景**：从诱饵投递、实时生成设备码、轮询监听、令牌窃取到后渗透的五个阶段，以及贯穿全程的检测规避手段（图源：本文根据 Microsoft Threat Intelligence 报告内容绘制）

第 1 阶段：诱饵投递

攻击始于一封高压话术邮件（例如"**Action Required: Password Expiration**"——立即处理：密码即将到期）。邮件载体包括恶意 URL、PDF 附件和 HTML 文件。据 Huntress 研究人员观察，相关诱饵还包括建筑投标书、商业合作协议、员工薪酬福利通知、密码到期提醒等内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq8f7eq77icGiaGgbP7DqI53kPvQyic3AW6cKgbEicVeGlcEHOoQq9uibiaqiaX7WWy1E77eTY8ztnia0DULjPlG0AnYo6jwQ8srkCCcPTw/640?wx_fmt=png&from=appmsg)

**图7 | EvilTokens 钓鱼邮件样本**：以招标书（RFP）为诱饵引导受害者打开链接（图源：Microsoft Security Blog）

第 2 阶段：实时生成设备码

用户点击恶意链接或附件后，被引导至一个运行后台自动化脚本的网页。该脚本**实时与微软身份提供方交互，现场生成一个活的设备码**，随后将代码显示在屏幕上，并配以"Copy Code"按钮，以及"Continue / Continue with Microsoft"按钮——点击后跳转到微软官方的 microsoft.com/devicelogin 门户。

值得注意的是：页面上的一切看起来都指向微软的真实域名，**这正是该手法最具迷惑性的地方。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq9q5CiayZvK78IAT4CMZhFib1lrZedibEkUpjlLyYAxql6PBQATwTeY3icYcLnr2JGib6BEESWx6tlMOkHFNElYSbj9aic2GlJKeDAkc/640?wx_fmt=png&from=appmsg)

**图8 | EvilTokens 钓鱼落地页**：仿冒 Adobe Acrobat Sign 身份验证界面，实时生成设备码并附"Copy Code"与"Continue to Microsoft"按钮（图源：Microsoft Security Blog）

第 3 阶段：轮询等待受害者"自投罗网"

展示代码并打开官方验证页后，脚本通过 checkStatus() 函数进入轮询状态，实时监控 **15 分钟的有效窗口**：每 3 至 5 秒（setInterval），脚本向攻击者的 /state 端点发起请求，发送秘密会话标识码，校验用户是否已完成认证。在受害者输入代码期间，该循环持续返回"pending"状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq82z4GxMsA7gWPw4XP90icNaAYQeEgvSXWumFKrN8PfLMH8fYCQmAvf525YaoVoMxKKezKgic1msMiaWO0ddibQrdDtcbux8xxtQwI/640?wx_fmt=png&from=appmsg)

**图9 | 微软官方设备码登录页（microsoft.com/devicelogin）**：页面明确提示"不要输入来自不可信来源的代码"，受害者在此粘贴钓鱼页提供的代码即完成授权（图源：Microsoft Security Blog）

第 4 阶段：最小化用户操作成本

为了最大限度提高成功率，攻击者脚本通常会**自动把设备码复制到受害者的剪贴板**。受害者到达官方登录页后只需粘贴即可：

* 如果受害者**没有活跃会话**，会被提示输入密码并完成 MFA；
* 如果受害者**已经处于登录状态**，只需粘贴代码并确认请求，攻击者的会话便在后台瞬间完成认证。

第 5 阶段：分化的后渗透节奏

最终阶段因攻击者目标而异，微软观察到两种典型节奏：

* **快速固化型**：部分案例中，攻击者在突破后 **10 分钟内**就注册新设备，生成主刷新令牌（Primary Refresh Token, PRT），实现长期持久化；
* **低调潜伏型**：另一些案例中，攻击者会等待数小时后才创建恶意收件箱规则或窃取敏感邮件，以规避即时检测。

05 绕过检测：多阶段投递管线与"合法云"掩护

EvilTokens 采用多阶段投递管线，专门针对传统邮件网关和终端安全产品设计。常见规避技术包括但不限于：

* **图片链接**：用嵌入了 URL 的图片替代明文链接；
* **多阶段重定向**：不直接指向最终钓鱼站点，而是经由被攻陷的合法域名层层跳转；
* **附件多级投递**：附件本身即包含多阶段投递逻辑；
* **假 CAPTCHA 验证**：落地页先展示需要用户交互的"人机验证"，以此阻拦自动化 URL 扫描器和沙箱。

尤其值得警惕的是其对**高信誉"serverless"平台的滥用**。微软观察到，EvilTokens 重度依赖 Vercel（.vercel.app）、Cloudflare Workers（.workers.dev）和 AWS Lambda 托管重定向逻辑——这些域名承载的钓鱼流量与正常企业云流量混杂在一起，简单的域名黑名单策略基本失效。

2026 年 4 月，微软还追踪到一波与 EvilTokens 特征吻合的钓鱼活动：攻击者利用自动化平台**批量启动数千个独特的、短生命周期的轮询节点**，借此部署复杂的后端逻辑（Node.js），绕过基于签名或模式的传统检测。这套基础设施被端到端地用于整个攻击流程——从动态生成设备码，一直到后渗透阶段。

06 拿到令牌之后：AI 加持的精准收割

窃取令牌只是开始。EvilTokens 真正的"护城河"，在于其把后渗透环节做成了自动化流水线：

**1. 高价值目标筛选。**利用平台的 AI 能力，攻击者在已沦陷账户池中快速筛选出财务、高管、行政岗位的受害者。

**2. 加速侦察。**令牌到手的瞬间，攻击者即通过 Microsoft Graph 以编程方式绘制组织内部架构、识别敏感权限，为持续访问和潜在横向移动铺路（令牌有效期内均可进行）。

**3. 定向金融数据窃取。**最具侵入性的行为专门留给拥有财务权限的用户：攻击者会对其邮件通信做深度挖掘，搜寻电汇信息、待处理发票、高管往来信件等高价值内容。

**4. 信任链滥用。**攻陷的账户还会被用于向组织内部和外部联系人发送钓鱼邮件——来自"可信联系人"的邮件，成功率自然更高。

此外，通过恶意收件箱规则隐藏通信、或将新设备授权接入受害者邮箱，都是常见的持久化手段；后者尤其难以清除。

可以说，EvilTokens 让攻击者具备了仅凭自身能力本无法完成的钓鱼与操作水平——**大规模群发、后渗透操作，皆可"从容进行"。**

07 防御与处置建议

防御设备码钓鱼及其同类 AiTM 威胁，需要技术控制与安全意识相结合的纵深策略。

源头封堵

* **尽可能封禁设备码流程。**微软建议在条件访问（Conditional Access）策略中阻止设备码认证流程；确需保留的（如 Teams 设备），仅对特定设备资源账户开放例外。
* **强制使用抗钓鱼认证方式。**优先采用 FIDO2 安全密钥或带通行密钥（passkey）的 Microsoft Authenticator，避免基于电话网络的 MFA（存在 SIM 劫持风险）。
* **封禁旧式认证协议。**旧式协议无法强制 MFA，应通过条件访问予以阻止。
* **部署登录风险策略。**基于登录风险级别（高/中/低）自动阻断访问或强制重新认证，并定期审阅风险登录报告。

邮件与终端防线

* 配置反钓鱼策略，检测仿冒发件人与冒充攻击；将高级钓鱼阈值（Ad...