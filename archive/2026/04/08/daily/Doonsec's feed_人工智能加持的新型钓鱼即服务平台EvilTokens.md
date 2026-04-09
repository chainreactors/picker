---
title: 人工智能加持的新型钓鱼即服务平台EvilTokens
url: https://mp.weixin.qq.com/s/gSpc3uorRDgNo4RC4Pd4zg
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:25:29.264137
---

# 人工智能加持的新型钓鱼即服务平台EvilTokens

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDo5KLDPzpIwtHUGawNpysbyMZK9eAXnQvEn0BSMSKnY6RWtq3MrfdtxyIvib8QaGIo3Wj2AgDgoVmYyAXKcz4wtQYpQU7uicXjfQ/0?wx_fmt=jpeg)

# 人工智能加持的新型钓鱼即服务平台EvilTokens

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

近日，网络犯罪社区中发现了一款名为 EvilTokens 的新型钓鱼即服务平台。钓鱼即服务（Phishing-as-a-Service，简称 PhaaS），是网络犯罪领域成熟的商业化模式，攻击者无需掌握复杂的技术开发能力，只需付费购买平台服务，即可快速发起大规模钓鱼攻击。

该平台主打微软账号设备码钓鱼能力，自 2026 年 2 月中旬上线以来，迅速被大量专攻中间人攻击和商业邮件欺诈的网络犯罪分子采用，已在全球范围内发起大规模攻击，影响遍及美洲、欧洲、中东、亚太等多个地区。

EvilTokens 的攻击逻辑，主要是利用了OAuth 2.0 设备授权许可协议。

设备码钓鱼的底层，是 OAuth 2.0 设备授权许可协议。该协议原本是为智能电视、物联网设备、打印机这类输入能力有限的终端设计的身份验证方案。它不需要用户在设备上直接输入账号密码，而是将登录操作委托给手机、电脑等二级设备完成。

微软对该协议的实现分为三个核心步骤：

1. 设备向微软身份平台发起请求，获取一组设备码、用户验证码，以及官方验证地址。
2. 用户在二级设备的浏览器中打开官方验证地址，输入用户验证码，完成账号登录与授权。
3. 设备持续向微软平台轮询状态，用户授权完成后，设备将获取到访问令牌和刷新令牌，建立长期有效的登录会话。

###

设备码钓鱼攻击，正是利用了 OAuth 2.0 设备授权流中 “待验证设备” 与 “用户登录终端” 的分离特性，发起的无凭证、可绕过多因素认证的账号劫持攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDryY7GXTibLEW5XjGSDshNwhyCTzOc4qeGSx9H8ibsS6JDHlErD3yLibibTEnh0vI8y7OK4NWmwv0kqTJ8s2CI9jR1EcQuPHzANibgY/640?wx_fmt=png&from=appmsg)

和常规仿冒登录页面的中间人攻击不同，这种攻击全程使用微软官方的认证地址，用户不会进入仿冒域名，因此隐蔽性和欺骗性极强。

完整攻击流程分为五步：

1. 攻击者以合法微软应用的身份，向微软平台发起设备授权请求，获取有效的用户验证码、设备码和官方验证地址。
2. 攻击者通过社交工程诱饵，诱导受害者打开微软官方验证地址，输入攻击者提供的用户验证码。
3. 受害者在微软官方页面完成账号登录与授权，全程不会向攻击者泄露账号密码和多因素认证信息。
4. 攻击者通过轮询微软接口，获取到受害者账号的访问令牌和刷新令牌。
5. 攻击者利用窃取的令牌，直接访问受害者的微软 365 账号资源，实现账号完全接管。

###

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp4aAGHGH2WG94fGpfwcfNcBEFdPJHtdE8HBVTuVPUHWalvY7dAuCAl4Jzu9wQgKCFecpicD3rKibN3l5a0qibZURrEfVjqK8unVQ/640?wx_fmt=png&from=appmsg)

###

整个攻击的核心是窃取三类令牌，不同令牌对应不同的攻击危害：

* **访问令牌**

  由微软 Entra ID 签发的短期有效令牌，有效期 60 至 90 分钟。攻击者拿到后，无需再次认证即可直接访问受害者的 Exchange Online 邮箱、SharePoint Online 与 OneDrive 文档、Teams 聊天记录等核心资源。
* **刷新令牌**

  有效期长达 90 天，每次使用都会生成新的 90 天有效期令牌并作废旧令牌。攻击者可通过持续刷新令牌，长期维持对受害者账号的访问权限，实现攻击持久化。
* **主刷新令牌**

  有效期 90 天的设备绑定单点登录凭证。攻击者可通过刷新令牌在 Entra ID 中注册恶意设备，进而申请主刷新令牌，实现对微软 365 全应用的静默登录，绕过所有凭证校验和多因素认证，甚至在企业内网横向移动。

##

EvilTokens 的流行，主要是因为它成为了首个提供开箱即用的微软设备码钓鱼套件，同时配套完整账号劫持与攻击后处置工具链的 PhaaS 平台。

市面上主流的 PhaaS 平台大多依赖中间人攻击仿冒登录页面，而 EvilTokens 另辟蹊径，将隐蔽性极强的设备码钓鱼做成了标准化、低门槛的商业化服务。

该平台通过功能完整的 Telegram 机器人完成全流程运营，包括产品销售、钓鱼页面部署、受害者信息实时推送、功能更新与技术支持。平台运营方还在持续迭代功能，未来计划扩展对 Gmail 和 Okta 账号的钓鱼支持。凭借完善的功能和极低的使用门槛，EvilTokens 上线后迅速被网络犯罪社区接纳，成为商业邮件欺诈领域的新兴威胁。

EvilTokens 不只是一个简单的钓鱼页面生成工具，而是覆盖 “钓鱼诱饵制作、账号令牌窃取、攻击后持久化、商业邮件欺诈自动化” 全流程的完整攻击平台，核心能力分为四大模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrIkaCKxeu0PuOUZ9KgcwToEkcicNhFpLSM52boJfBUYRsFhbckuPNUKeEsToGmQDOF2qYNRD1OuQibSqtKEW1B8otzTXdJWfr84/640?wx_fmt=png&from=appmsg)

###

EvilTokens 为付费用户提供可自行托管的钓鱼页面，所有页面都围绕设备码钓鱼流程设计，通过仿冒用户信任的服务，降低受害者的警惕性。

平台内置了多套成熟的钓鱼模板，覆盖绝大多数高频社交工程场景，包括仿冒 Adobe Acrobat Sign 与阅读器、DocuSign 电子签名、邮件隔离通知、日历会议邀请、SharePoint 访问请求、语音邮件通知、密码过期提醒、OneDrive 共享文档、电子传真通知等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqhjyP1WysUwAQd2HYKwn4OT0ichsM1q6pnF0u0Kic8pia8oiaLgZzTuNibgoaqmjlIpIYpEceRWXicg9KNaYAicKjZmQkISuib4ghib8Vw/640?wx_fmt=png&from=appmsg)

这些钓鱼页面的设计逻辑高度统一：

* 以文档访问、身份验证、安全提醒为诱饵，引导用户完成身份核验。
* 页面自动生成并展示微软官方的用户验证码，附带详细的操作指引。
* 提供 “前往微软验证” 按钮，点击后直接弹出微软官方的设备登录页面。
* 全程通过加密方式加载页面内容，使用 AES-GCM 算法对页面核心代码进行加密解密，规避安全检测。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDq72ne69D4Lfg0HRwGE5xQTulMpkekkqiaibGCmLaBjNfMcq2cnjrTtRiaGcJBruyMM46c8WvBYB4ibElGUUG4ZibYXzKaaGO4HzCHU/640?wx_fmt=png&from=appmsg)

用户验证码由平台后端向微软 API 申请生成，受害者加载钓鱼页面后有效期为 15 分钟。页面会持续轮询后端接口，一旦用户完成授权，立即自动将用户重定向到预设的正常页面，消除受害者的怀疑。

EvilTokens 的核心能力集中在后端，通过一套完整的 REST API 接口，实现设备码流管理、令牌窃取与武器化、账号侦察与资源访问等全流程自动化操作。即使是技术能力有限的攻击者，也能通过简单的接口调用，完成复杂的账号劫持操作。

核心后端能力包括：

* 自动化设备码流管理：一键发起微软设备授权请求，实时监控用户授权状态，授权完成后自动捕获并存储访问令牌与刷新令牌，同时通过 Telegram 向攻击者推送受害者邮箱、IP 地址等信息。
* 令牌持久化与升级：自动将窃取的刷新令牌转换为主刷新令牌，存储到数据库中，为长期访问和横向移动提供基础。
* 一键会话劫持：基于令牌生成浏览器单点登录 Cookie，攻击者无需账号密码和多因素认证，即可一键登录受害者的微软账号，实现浏览器会话劫持。
* 内置邮箱访问接口：直接通过令牌获取 Outlook Web App 会话 Cookie，无需复杂的 Cookie 注入操作，即可访问受害者的完整邮箱内容。
* 全方位侦察枚举：自动调用微软 Graph API 和 Azure 管理接口，获取受害者的个人信息、企业组织架构、邮箱规则、联系人、日历事件、Azure 订阅与资源信息，为后续的商业邮件欺诈攻击提供完整的上下文数据。

|  |  |  |
| --- | --- | --- |
| **API 端点** | **目的** | **主要行动** |
| POST/ *api/device/start* | 启动设备代码流 | – 向 */common/oauth2/devicecode* 发送 POST 请求，Microsoft Office 客户端 ID 和资源设置为 *hxxps://outlook.office365[.]com/* |
| GET */api/device/status/：sessionId* | 通过轮询Microsoft的令牌来检查设备代码状态 | – 向 */common/oauth2/token* 发送带有客户端 ID、设备代码及其他参数 的 POST 请求 – 将捕获的访问和刷新令牌保存到数据库 – 发送带有受害者邮箱和 IP 地理定位的 Telegram 通知 – 使用捕获的刷新令牌*呼叫 prt.convertToPRT（）* 自动转换为 PRT –当令牌转换为 PRT 时发送 Telegram 通知 |
| GET */api/device/sessions* | 列出所有活跃设备代码会话 | – 运行 *cleanupExpiredSessions（）* 以移除过期条目 – 遍历数组 *deviceCodeSessions* 并返回会话 |
| POST/ *api/prt/convert* | 将刷新令牌转换为PRT | – 调用函数 *prt.convertToPRT（），*将提供的刷新令牌自动转换为 PRT – 将 PRT 数据存储到 PostgreSQL 数据库 |
| POST/ *api/prt/刷新* | 获取任何资源的新访问令牌 | – 调用*函数 prt.refreshWithPRT（）* 以获取任意目标资源的访问令牌 |
| POST/ *api/prt/exchange* | 获取一个新的访问令牌以简化资源 | – 调用函数 *prt.refreshWithPRT（）* 以获取资源简写的访问令牌（Outlook、Graph、Azure、Substrate、SharePoint） |
| POST/ *api/prt/cookie* | 生成一键浏览器 SSO 劫持的 cookie： *x-ms-RefreshTokenCredential* | – 调用*函数 prt.convertToPRT（），*如果尚未完成 自动转换为 PRT– 首先调用 *prt.getServerNonce（）* 获取服务器 nonce，然后调用 *prt.createPRTCookie（）* 生成 *x-ms-RefreshTokenCredential* JWT cookie，无需密码或多重身份验证即可访问实时浏览器会话。 – 如果设备密钥材料可用 ，尝试生成 *x-ms-DeviceCredential* Cookie – 返回 *x-ms-RefreshTokenCredential* Cookie 值及其他会话数据 |
| POST/ *api/prt/owa-session* | 获取 OWA 会话 Cookie | – 向 */common/oauth2/v2.0/token* 发送 POST 请求，Microsoft 认证代理和 Microsoft Office 的客户端 ID 以获取访问令牌和 ID 令牌 – 向 *hxxps://outlook.office365[.] 发送 POST 请求com/owa/* 与 ID 令牌和访问令牌共获得 OpenID Connect Cookie – 尝试获取持有者令牌头以收集更多 Cookie – 返回所有收集的 Cookie |
| POST/ *api/prt/recon* | 获取图API令牌并进行侦察 | – 通过调用*函数 exchangeRefreshToken（）* 获得新的图 API 访问令牌 – 并行发送全部 7 个侦察查询，获取来自 */me*、*/organization*、*/users*、*/groups*、*/applications*、*/domains* 和 */directoryRoles* 的信息 – 返回结果 |
| POST */api/prt/azure* | 获取一个Azure令牌并进行枚举 | – 通过调用*函数exchangeRefreshToken（）* 获得Azure管理的新访问令牌——枚举来自 *hxxps://management.azure[.]的订阅。com/订阅*，以及每个订阅的资源组和最多50个资源 ——返回结果 |

EvilTokens 采用标准化的商业化运营模式，全程基于 Telegram 生态完成用户管理与产品交付，运营架构包括官方服务账号、产品更新公告频道、销售管理机器人、钓鱼页面一键部署机器人、反机器人页面销售机器人，以及付费客户专属私域群。截至 2026 年 3 月 19 日，该私域群已有约 280 名付费用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqSNUibMmOYIlCaNyX9lE7Ua9oFicG3CyNyT44ureuoC7r7bhTiaUjmF9YatlaqpEF2ct8RNaw7kbBxwwvOczsvFQbdNh2COLxfDM/640?wx_fmt=png&from=appmsg)

平台采用 “一次性付费 + 月度订阅” 的定价模式：

* 设备码钓鱼套件一次性付费 1500 美元，用户可获得管理面板的终身访问权限。
* 月度许可费 500 美元，用户可获取钓鱼页面完整代码和活跃 API 密钥，使用平台核心的设备码钓鱼与后端接口能力。
* 配套工具单独付费，包括售价 600 美元的 B2B 发件工具、1000 美元的 SMTP 发件工具，以及售价 500 美元终身授权的定制浏览器 Portal Browser。

其中 Portal Browser 是专为商业邮件欺诈设计的定制工具，支持同时登录多个被盗的微软 365 账号，自动刷新令牌维持登录状态，可直接访问微软管理后台、Azure、Office、OneDrive、SharePoint、Teams 等全量应用，大幅降低了攻击者的账号管理成本。

EvilTokens 为付费用户提供了中心化的管理面板，除了监控活跃攻击会话、管理窃取的账号令牌等基础功能外，还支持多用户管理与角色分配，方便攻击团队内部协作。

面板内置了仿冒 Outlook 的网页邮箱界面，直接通过窃取的令牌访问受害者邮箱，无需任何额外的会话劫持操作，大幅降低了商业邮件欺诈的技术门槛。同时面板还提供了邮箱内容关键词搜索、批量邮件扫描、大语言模型分析等功能，形成了从账号劫持到欺诈攻击的完整闭环。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoqfAQS7GyjWIrOP8PGg8TEUbaRqmleEkIeX7h2zb1J7V9NxVibCMaeKdS9WlCI5AbiaLiawj4QGW2zibV2tcNfl1sABibau8uuO7MM/640?wx_fmt=png&from=appmsg)

EvilTokens 最具颠覆性的能力，是它成为了首个集成 AI 增强攻击后工具链的 PhaaS 平台。它通过大语言模型，将原本需要攻击者手动完成的邮箱分析、风险识别、欺诈邮件撰写等工作完全自动化，大幅降低了商业邮件欺诈的技术门槛，同时显著提升了攻击效率与成功率。

传统的商业邮件欺诈攻击，需要攻击者具备极强的社交工程能力，手动翻阅受害者的数千封邮件，识别可利用的财务支付线索，模仿受害者的写作语气，撰写高度仿真的欺诈邮件。整个过程耗时耗力，对攻击者的能力要求极高。而 EvilTokens 的 AI 驱动分析管道，将这个过程压缩到了几分钟内，全程无需人工干预。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrO95b3RPOk4iauueaveluQO8GiafrD2HR7W1acUB6s9EljsqQ80icQsWvYAdibDY4ibFfd06frxlicTsvttjxIsCnfqiaNJcW52nr5gg/640?wx_fmt=jpeg&from=appmsg)

全自动化 AI 分析攻击管道

EvilTokens 的 AI 攻击流程分为六个完整步骤，形成了从令牌捕获到欺诈攻击方案生成的全闭环：

1. 钓鱼页面诱导受害者完成设备码授权，后端捕获受害者的微软访问令牌与刷新令牌。
2. 基于窃取的令牌，自动获取 Outlook、微软 Graph、Azure、SharePoint 等核心服务的访问权限，同时将刷新令牌转换为主刷新令牌，建立账号持久化访问。
3. 并行调用微软 Graph API 执行全方位侦察，提取受害者的邮箱规则、联系人信息、日历事件、已发送邮件、邮箱文件夹结构、上下级组织架构、企业基础信息等所有高价值数据，生成完整的侦察报告。
4. 第一阶段大语言模型分析，通过 Groq API 调用 llama-3.1-8b-instant 模型，以 250 封邮件为一批，分批处理最多 5000 封邮件，结合侦察报告，识别邮箱内所有可利用的财务风险点，同步提取受害者的写作风格、邮件签名、常用话术等信息。
5. 第二阶段大语言模型分析，通过 Groq API 调用 llama-3.3-70b-versatile 模型，整合第一阶段的所有分析结果，生成完整的风险评估报告、定制化商业邮件欺诈攻击场景，以及...