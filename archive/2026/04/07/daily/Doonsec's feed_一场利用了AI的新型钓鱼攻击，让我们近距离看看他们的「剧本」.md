---
title: 一场利用了AI的新型钓鱼攻击，让我们近距离看看他们的「剧本」
url: https://mp.weixin.qq.com/s/p-8iKxgSTcI4NXc0sn7gXA
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:32:28.909692
---

# 一场利用了AI的新型钓鱼攻击，让我们近距离看看他们的「剧本」

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibe5bpnUia9H5RZPibJiabVchiafuGV0L5KFib4t90bIgodgmibsJ2ibv66Vx4dzokjkNUQiasKrtUNIXibYk8NRUgvJmDGUbZm4oBVSXicUk/0?wx_fmt=jpeg)

# 一场利用了AI的新型钓鱼攻击，让我们近距离看看他们的「剧本」

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 微软安全团队披露了一场大规模、高度自动化的网络钓鱼活动。攻击者利用「设备代码认证」流程，结合AI生成个性化诱饵和动态后端基础设施，有效绕过多因素验证和传统防御，针对企业账户发起攻击。这是一场手法成熟的剧本式攻击，以下是其全链条拆解和防御建议。

微软Defender安全研究团队最近逮住了一场大范围的钓鱼攻击。这场攻击的核心，是利用微软Azure的「设备代码认证」流程来批量攻破企业账户。

你可能听说过设备代码钓鱼（Device Code Phishing），但这次的玩法升级了。它不再是那种范围有限、手动脚本为主的攻击。攻击者搞了一套AI驱动的自动化基础设施，从前到后，全是自动化。这标志着攻击者的技术实力有了一个明显的跃升，让人想起今年2月份那个Storm-2372攻击活动，但手法更精进。

这次攻击的新套路主要有这么几点：

* **先进的后端自动化：**攻击者用Railway.com这类平台，轻轻松松就能拉起成千上万个临时构建的「轮询节点」。这套后端（用的是Node.js）能绕过基于签名或模式的传统检测。整个攻击链，从生成动态设备码到攻击成功后的活动，都靠这个基础设施。
* **高度个性化的诱饵：**他们用生成式AI来写钓鱼邮件，内容精准匹配受害者的工作角色，比如RFP投标、发票单据、生产流程这些主题，用户上当的几率自然就高了。
* **动态代码生成：**关键是干掉那个15分钟的有效期限制。攻击者不是预先生成好一个码，而是等你点开钓鱼链接的瞬间，才现场生成。这样倒计时才真正开始，确保你看到的码是热乎的。
* **侦查与持久化：**尽管攻破了很多账户，但攻击者后续主要盯着那些高价值的目标。他们用自动化手段，比如分析公开资料和公司通讯录，快速找出财务或高管角色的人。然后就是火速侦查权限、创建恶意收件箱规则，为长久潜伏和数据窃取做准备。

一旦拿到认证令牌（token），攻击者就进入「赛后」阶段：维持访问、窃取数据。他们会用偷来的令牌去偷邮件、设规则，同时，还会动用微软Graph API来侦察公司的组织结构和权限，方便接下来的横向移动。

## 攻击链条：一场精心编排的戏

> 「设备代码认证」本是好意，为了让智能电视、打印机这种没法显示完整登陆界面的设备也能登陆。它会给你一个短码，让你去另一个设备（比如手机）的浏览器上输入。但这也给攻击者留了后门——认证过程和发起请求的设备是「松耦合」的。

设备代码钓鱼，就是攻击者插入到这个流程里。不是你的设备在申请，而是攻击者发起流程，然后通过钓鱼邮件给你一个码。你输入这个码，就相当于亲手批准了攻击者的会话，把账户访问权交了出去，还没暴露自己的密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcxrBQRPdtlbtP5YBbU9h7vNaaxVukMxvjfPsuuuH1FlNh8XjQOQGooMSBcz6Fo2IkTqmvicBJEn8FdFO5ZMet5FYnHuaXD9guQ/640?wx_fmt=png&from=appmsg)

### 第一阶段：情报与目标验证

攻击第一步，先确认账户是不是活靶子。他们用一个叫GetCredentialType的微软接口去查，目标邮箱是不是存在、是不是在用。通常，这个侦查会发生在真正的钓鱼攻击前10到15天。

攻击链设计得很刁钻，用来绕过传统的邮件网关和终端安全。用户得先和一个高压诱导的附件或链接互动，比如“密码即将过期，请立即操作”。

为了躲开自动URL扫描器和沙箱，钓鱼链不是直通最终网站的，中间会有多次跳转。攻击者特别喜欢用一些信誉高的「无服务器」平台来托管跳转逻辑，比如Vercel (\*.vercel.app)、Cloudflare Workers (\*.workers.dev)和AWS Lambda。因为这些域名流量很大，和正常的企业云流量混在一起，简单拉黑域名就没用了。

最终，用户被带到登录页面。这个页面要么是用的“浏览器套浏览器”技术（在一个网页里模拟一个假浏览器窗口），要么是直接在一个模糊的文档预览页里显示一个“验证身份”按钮，这个按钮会把用户带到官方的“microsoft.com/devicelogin”，并显示一个设备码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibduU1vu5tB4t0rXCBxMuyOd1abDMA7IqdNLiaibWVLng3rjRWktH20t6M5B4XwR40vYHyicMzbsDP8dgmDgg7hicVmsL1jzROiaxOSA/640?wx_fmt=webp&from=appmsg)

钓鱼邮件的主题花样很多：文档访问、电子签名、语音邮件通知。有时还会先让你输入邮箱地址，方便给你「定制」一个恶意设备码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcxTPHc9nTwbn74XDicB12hUy4hrZeVamGsCvtKmJBW9b2f6iaw8PsqN4l2WmqzGRJvpCDomLmxMwfSdUYTUt6IzKiaBWo03kUaKQ/640?wx_fmt=webp&from=appmsg)

和传统网页直接要密码不同，这个前端页面主要负责“交接”。点击“继续到微软”按钮的那一刻，后台脚本就开始干活，为下一幕的“设备码提示”做准备。

攻击者用「域名影子」技术和仿冒品牌子域名来绕过信誉过滤器。有些域名专门模仿技术或管理服务，比如graph-microsoft[.]com, portal-azure[.]com。他们也用大量随机生成的子域名，这样就算一个URL被标记，整个域名也不会立刻被全封。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcEjH5UsrtRdb4O1w5jNGvLDkwbc1icVoiawStV1sjOmJ1OPssnjShc2UesfGfvx5bhfBwicAyZ9vG3zVjvddHOibMRAZqbol47ibEM/640?wx_fmt=webp&from=appmsg)

### 第二阶段：初始访问

攻击者向目标投递精心设计的钓鱼邮件，主题包括发票、RFP投标、共享文件等。邮件里要么是直接链接，要么是PDF、HTML附件，目的就一个：诱使你去点那个链接，最终到达一个看起来像模像样、实则被控制的页面。

### 第三阶段：动态设备码生成

点开链接，你就会被带到一个运行后台脚本的网页。这个脚本会实时和微软的身份服务交互，现场生成一个活的设备码，并在你的屏幕上显示出来，同时还有一个按钮，会把你重定向到官方的microsoft.com/devicelogin门户。

这招「动态设备码生成」是关键创新，它专门用来对付OAuth 2.0设备授权流程里那个要命的15分钟时限。

在以前那种静态钓鱼里，攻击者会在邮件里放一个预先生成的码。这就意味着用户必须在15分钟内完成被骗、打开邮件、经历多次跳转、走完多步登录的全过程。邮件晚开20分钟，攻击就自动失效了。

而动态生成解决了这个问题。通过把生成环节挪到跳转链的最后一环，那个15分钟倒计时，从你点击钓鱼链接、落地到恶意页面才开始。这就保证了用户输入时，那个码永远都在有效期内。

具体怎么生成呢？当你到达最终页面时，上面的脚本会向攻击者后端（/api/device/start/ 这类地址）发起一个POST请求，后端服务器会作为代理，去调用微软官方的设备授权接口，并带上你的邮箱地址作为提示。服务器会返回一个包含设备码（满额15分钟寿命）和一个隐藏会话标识符的JSON对象。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdzR70nVEawV3EhKq0kYmh7qf4sO67moAlJyCao7gXtTGUI63piaDsdvzJpsGkcQKodWY0jlzS749CZ10s1JCtx4icFK6OyTy32Y/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdAfDtCfwPxbs20txicibH33joH8RBlviciaXAaonCA4lcLt9YKX2NibAic2JppMCBczHiaQPdUJsYyibzNPOS1PCsbWIQJd06nPiaUyiaN0/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibffkBoebMpeUMq0XhtqiaN6vqxg8WTH9f9Z8kqHt8QicOhMcsOqHDDdKSG5qGUdRRqScwnZbiczCGub0mvse6duTVKaW2gnZamVhw/640?wx_fmt=webp&from=appmsg)

### 第四阶段：利用与认证

为了省时间、提高成功率，攻击者的脚本通常会**自动替你复制**生成的设备码到剪贴板。你到了官方登录页，直接粘贴就行。如果你还没登录，它会让你输密码和MFA；如果你已经登陆了，那么粘贴、确认一下，瞬间就替攻击者完成了后端会话认证。

这招“剪贴板劫持”挺损的，目的就是在宝贵的15分钟窗口里帮你省几秒钟。脚本直接用 `navigator.clipboard.writeText` 这个API，把刚生成的设备码塞进你Windows的剪贴板。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibf8I2RyqzhmZ2eu7icgmrC1XLstR4he7wkWs65hRESgcs0NseLIx8NwHPnD7jKkfAyqJiaphXtp7pzkR8ceV3mYNqNfaZSInvclE/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfTea4fBibaSbkzZ73X7NzicYDiaZZCdyBggV43iaBeV0ySpOat0GxFevx0A1NIceuSxZ09hkmg9cc5EiaZCrribS3SaogJqPPiasEG8Y/640?wx_fmt=webp&from=appmsg)

### 第五阶段：会话验证

攻击成功后，攻击者会立刻进行验证检查，确保拿到的令牌是有效的，而且成功取得了目标的访问权限。

这个过程叫“轮询”。在给你显示完设备码、打开官方登录页后，脚本就开始通过 `checkStatus()` 函数进行轮询，实时监控那15分钟。每3到5秒，它就去ping攻击者的/`state`端点，发送那个秘密会话标识符，验证用户是否已经认证。当你在真正的微软网站上输入代码时，这个循环会返回“待处理”状态。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibf1iaSL9tBxgia6SsKHQ9laKyiatMvxAMMqAxtyT4mic9XGl9BoyWBbpg6mOnXqDUQB1W8y7pSOFSfjvWd0jQhKk9U8jB5m7RrSTBQ/640?wx_fmt=webp&from=appmsg)

一旦你完成了MFA登录，下一轮轮询就会返回成功状态。这时，攻击者的服务器就拿到了你账户的有效访问令牌，并且因为用了设备码流程，绕过了MFA。之后，你可能会被重定向到一个障眼法网站（比如DocuSign或Google）。

### 第六阶段：建立持久存在与后续利用

最后这步花样就多了，看攻击者的具体目标。有的案例里，在入侵10分钟内，攻击者就注册新设备来生成主刷新令牌（PRT），以求长期潜伏。有的则会等上几小时，再创建恶意收件箱规则或窃取邮件，避免立刻被发现。

攻击成功后，常见的后续动作是设备注册和Graph API侦查。

> 在精选的案例中，攻击会发展到使用微软Office应用程序创建收件箱规则来进行邮件窃取和账户持久化。攻击者会筛选高价值角色（财务、高管），用Graph API快速绘制组织结构图，定位敏感权限。财务授权用户是他们重点深度侦察的对象，翻查邮件寻找电汇细节、待付发票、高管通信等高价值信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcE9jMQN9mAs2AfK1TJTicRBwUw699mHialGibTcqrolNOib8sJ6HF8GB6g6HObFyB7gX5WRZyavt9bQYWJ898pq0ia6ftbrJvicDj1A/640?wx_fmt=webp&from=appmsg)

## 我们该怎么防？

面对这种设备代码钓鱼，我们可以从这几方面加固防御：

* **收紧设备码流程：**非必要不开启设备码流，能禁就禁。在Microsoft Entra ID的条件访问策略中对其进行配置。相关文档：阻止身份验证流程[1]
* **用户教育：**告诉员工钓鱼常用技俩。注意登录提示中的应用名称，警惕包含可疑链接的“[外部]”邮件。
* **配置防护策略：**在Microsoft 365 Defender中配置反钓鱼策略和安全链接保护。反钓鱼策略[2]安全链接[3]
* **及时响应：**怀疑有设备代码钓鱼活动？立即吊销用户的刷新令牌，方法是调用revokeSign-inSessions接口[4]。考虑设置条件访问策略强制重新认证。
* **用好风险策略：**实施登录风险策略[5]，自动响应有风险的登录尝试。高风险用户的访问可以被直接阻断或要求重新认证。
* **启用持续访问评估：**当用户处于高风险时，利用此功能可以使其访问立即被撤销。

还有几个更宏观的最佳实践：

* **强制执行多因素认证：**这是基石。尽量用防钓鱼的认证方式，比如FIDO令牌、带密码的Microsoft Authenticator，少用基于电话的MFA，防SIM卡劫持。
* **阻断旧式认证：**用条件访问来阻断不支持MFA的旧协议。
* **统一身份管理：**把身份管理集中到一个平台。如果是混合环境，做好本地目录和云端目录的集成。这有助于实现单点登录，并让AI模型全面学习用户行为。
* **做好凭证卫生：**坚持最小权限原则，审计特权账户活动。

## 攻击指标与检测

攻击者的基础设施建在Railway.com、Cloudflare、DigitalOcean这些名声还不错的服务上，这让恶意脚本能和正常的业务流量混在一起。他们还攻陷了一些合法域名来托管钓鱼页面，利用这些网站的原有信誉来绕过过滤系统。

**部分已知的恶意IP范围：**

* 160.220.232.0 （Railway.com）
* 160.220.234.0 （Railway.com）
* 89.150.45.0 （HZ Hosting）
* 185.81.113.0 （HZ Hosting）

微软的多款安全产品（Defender XDR, Defender for Identity, Entra ID Protection等）已有相应的检测规则，可以覆盖从初始访问、凭据窃取到防御规避等多个攻击环节。例如，检测异常的OAuth设备码认证活动、来自匿名IP的登录、以及与已知威胁情报基础设施相关的登录模式等。

对于使用Microsoft Sentinel的安全团队，文中也提供了若干高级搜寻查询，可用于检测可疑的设备码钓鱼活动、后续的异常设备注册和收件箱规则创建行为。

说到底，鱼钩上的诱饵越像真虫子，鱼越容易上钩。现在这诱饵是AI现做的，鱼钩的机关也全自动化了。防御者不能只盯着老式的鱼漂看了，了解整个新式垂钓流水线，才能知道该在哪里下网拦截。

---

### 参考资料

[1] https://learn.microsoft.com/entra/identity/conditional-access/policy-block-authentication-flows

[2] https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-about

[3] https://learn.microsoft.com/en-us/defender-office-365/safe-links-about

[4] https://learn.microsoft.com/graph/api/user-revokesigninsessions

[5] https://learn.microsoft.com/azure/active-directory/identity-protection/howto-identity-protection-configure-risk-policies

[6] https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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