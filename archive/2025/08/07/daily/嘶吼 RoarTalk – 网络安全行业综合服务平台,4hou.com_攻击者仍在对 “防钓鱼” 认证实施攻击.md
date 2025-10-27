---
title: 攻击者仍在对 “防钓鱼” 认证实施攻击
url: https://www.4hou.com/posts/LGkw
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-07
fetch_date: 2025-10-07T00:15:49.079147
---

# 攻击者仍在对 “防钓鱼” 认证实施攻击

攻击者仍在对 “防钓鱼” 认证实施攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 攻击者仍在对 “防钓鱼” 认证实施攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)64504

收藏

导语：真正安全的账户只有两类：一类是仅启用通行密钥、未设置任何备用认证方式的账户；另一类是通过条件访问策略禁止非通行密钥认证的账户。

随着人们逐渐意识到许多多因素认证（MFA）方法存在 “易受钓鱼攻击” 的问题（即不具备防钓鱼能力），基于 FIDO2 标准的认证方式（又称 “通行密钥”）正得到越来越多的推广，例如 YubiKey、Okta FastPass 和 Windows Hello 等。

最常用的多因素认证（MFA）验证方式（如短信验证码、推送通知和基于应用的一次性密码）经常被绕过，而现代反向代理 “中间人” 钓鱼工具包是最常见的手段（也是如今钓鱼攻击的标准选择）。

这类工具的工作原理是拦截受害者输入密码并完成多因素认证检查后创建的已验证会话。具体来说，钓鱼网站会在用户与真实网站之间传递信息 —— 这也是 “中间人” 名称的由来。

相比之下，基于通行密钥的登录方式不会遭受钓鱼攻击。由于基于通行密钥的登录与域名绑定，即便通过中间人工具包进行代理，在钓鱼网站（phishing.com）上尝试使用微软网站（microsoft.com）的通行密钥也无法生成通过认证检查的正确数值。但攻击者并未轻易放弃。

随着通行密钥的普及，我们发现他们开始使用多种技术来降级认证流程或通过其他方式规避认证过程，使其重新面临钓鱼攻击的风险。以下是迄今为止攻击者用于绕过通行密钥的所有技术手段。

**降级攻击**

降级攻击是攻击者绕过防钓鱼多因素认证（MFA）的常用手段。目前已在多款恶意中间人（AitM）工具包中发现多因素认证降级功能，甚至连 Evilginx 这类大众化工具包也能实现该操作。

在实施中间人钓鱼攻击时，攻击者无需精准转发 100% 的信息，而是可以对部分内容进行篡改。例如，正规应用可能会询问用户：“您需要进行多因素认证 —— 请问您选择使用密钥，还是备用验证码？” 但钓鱼网站可能会篡改该页面，仅显示 “您需要进行多因素认证 —— 请使用备用验证码”，从而剥夺用户选择更安全密钥的权利。这就是所谓的降级攻击。

这种攻击手段也适用于默认采用单点登录（SSO）的账户。在这种情况下，钓鱼工具包会选择用户名和密码作为备用登录方式，以便继续实施钓鱼攻击。

因此，即使存在防网络钓鱼的登录方法，但由于存在安全性较低的备份方法，帐户仍然容易受到网络钓鱼攻击。

**设备代码钓鱼**

为绕过防钓鱼认证机制，攻击者还会利用设备代码钓鱼攻击——这种攻击借助了不支持基于密钥登录的设备所采用的替代认证流程，例如那些没有网页浏览器或输入功能有限的设备。

这种替代登录流程的运作方式是：向用户提供一个唯一代码，并指示用户在另一台设备的浏览器中访问某个网页，输入该代码以完成设备授权。

攻击者可利用这一点对目标实施钓鱼攻击：诱骗目标访问其认证提供商的网站，并输入攻击者提供的代码，进而获取目标账户的访问权限。此类攻击的优势在于，它会将目标引导至合法URL，除输入设备代码和登录外，不会提示用户同意任何明确的权限请求。此外，在某些情况下，经过验证的应用也可能被仿冒。

近期已有多起攻击活动采用了这种技术，包括俄罗斯支持的势力对M365账户的多次攻击。

**愿者上钩式网络钓鱼**

愿者上钩式网络钓鱼（Consent phishing）是最早被纳入SaaS攻击矩阵的技术之一，虽已存在一段时间，但近期恶意活动呈上升趋势。

OAuth允许用户向第三方应用授予访问其数据的权限。攻击者可通过诱骗用户授权恶意OAuth应用，滥用这一功能。在愿者上钩式钓鱼攻击中，攻击者会向目标发送钓鱼链接，该链接会请求获取访问敏感数据的权限或执行危险操作的权限。

若目标同意授予这些权限，攻击者就能获得对目标账户的相应访问权限。这种访问权限可绕过多因素认证（MFA），且即便目标更改密码，该权限也依然有效。

愿者上钩式钓鱼最常与针对微软Azure或谷歌Workspace租户的攻击相关联。不过，如今越来越多的SaaS应用会自行部署基于OAuth认证的API和应用商店，而这些也可能成为同样的攻击目标——近期针对GitHub用户的攻击案例就体现了这一点。

![authorize-security-account.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250806/1754449999116964.png "1753859247209795.png")

GitHub恶意OAuth应用程序

一旦获得授权，攻击者就可以广泛访问该帐户。在影响GitHub的例子中，攻击者将能够修改存储库以对用户进行进一步

的攻击（例如通过恶意软件感染他们），毒害与存储库连接的存储库和服务，并泄露帐户有权访问的任何敏感数据。

**验证网络钓鱼**

邮件验证有时会被用作一种安全控制手段，例如在注册新账户时。其典型实现方式是向目标用户发送邮件，内含可供点击的验证链接，或需要用户输入的验证码。

验证钓鱼指的是攻击者通过钓鱼或其他类型的社会工程学手段，诱骗用户点击验证链接或将验证码提供给他们，以此绕过这种安全控制。

这种技术被用于绕过多因素认证（MFA）的一个例子是跨身份提供商（IdP）冒充。具体来说，攻击者会用受害者的企业邮箱域名注册一个新的身份提供商账户。在很多情况下，这使得攻击者能够通过这个新的身份提供商进行单点登录（SSO），且无需经过任何额外验证 —— 事实上，有五分之三的应用被发现存在这种允许此类行为的漏洞。

考虑到有大量应用可作为单点登录的身份提供商，潜在的攻击目标其实相当多（具体取决于应用本身及其支持的登录方式）。

![managed-vs-unmanaged.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250806/1754450001115492.png "1753859315322833.png")

受管理的IdP可以由组织（拥有和操作IdP及其上的身份）集中管理，而未受管理的“社会”IdP由供应商控制，身份由用户拥有和管理。

**应用专用密码钓鱼**

应用专用密码钓鱼是一种社会工程学攻击手段，攻击者通过诱骗用户为自己的账户生成“应用专用密码”，并设法获取该密码。这类传统密码是部分主流SaaS服务提供商（如谷歌、苹果）推出的功能，旨在让不支持现代认证方式（如OAuth 2.0）的老旧应用能够访问账户数据。

攻击流程通常是这样的：攻击者伪装成可信实体（例如技术支持人员、服务提供商），以某个借口引导用户进入自己的账户安全设置页面，接着一步步诱导用户创建新的应用专用密码，并要求用户将该密码粘贴到攻击者控制的表单或聊天窗口中。

由于应用专用密码的设计初衷是供不支持多因素认证（MFA）的环境使用，因此一旦落入攻击者手中，他们就能通过API以程序化方式持续访问用户的账户数据（如电子邮件、联系人、文件），且这种访问往往不会像陌生设备的传统交互式登录那样触发同等级别的安全警报。

这使得此类访问比会话令牌更隐蔽、更持久，因为应用专用密码在用户手动撤销前通常始终有效。近期曝光的一个案例就属于这种攻击：一名研究俄罗斯信息操作的专家成为目标，遭遇了一场精心策划且针对性极强的社会工程学攻击。攻击者通过应用专用密码登录邮件客户端，成功获取了受害者邮箱的持久访问权限。

具体过程是，攻击者伪装成美国国务院发送诱骗信息，指导受害者创建应用专用密码并分享给他们，进而获得了其谷歌邮箱的访问权限。

![phishing-email.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250806/1754450002154159.png "1753859350642199.png")

一个高度可信的ASP网络钓鱼诱饵，用于有针对性的攻击

**补充：针对不使用密钥的本地账户**

不过，绕过密钥可能最简便的方法，是直接攻击那些本身不支持密钥的应用。密钥通常与单点登录（SSO）配合使用：你先通过受密钥保护的安全方式登录主身份提供商（IdP），再通过单点登录进入关联的应用。但许多应用并不支持直接用密钥登录。

因此，Slack、Mailchimp、Postman、GitHub等常用商业应用正日益成为直接攻击目标——这就绕开了通常配备更完善认证控制的身份提供商（如微软、谷歌、Okta等）。

就像备用多因素认证方式常与密钥同时注册一样，本地“幽灵登录”方式也常与单点登录并存，这意味着账户存在多个可能的登录入口。

很多情况下，这些应用根本没有部署多因素认证，因此同样容易遭受凭证盗用攻击——去年的Snowflake攻击和今年的Jira攻击就是例证。这给企业带来了庞大且脆弱的身份攻击面，亟待管理。

![how-many-vulnerable.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250806/1754450003982920.png "1753859404117013.png")

一个拥有1000个用户的组织拥有超过15000个帐户，这些帐户具有各种配置和相关漏洞

**结论**

大多数情况下，攻击者无需采取特殊手段即可绕过通行密钥。只要目标账户注册了备用的非通行密钥多因素认证方式，他们只需使用平时惯用的钓鱼工具和技术，就很可能得手。

真正安全的账户只有两类：一类是仅启用通行密钥、未设置任何备用认证方式的账户；另一类是通过条件访问策略禁止非通行密钥认证的账户。

但细节中仍潜藏风险（比如最近有案例显示，微软提供的条件访问模板会将 “高风险” 登录误判为正常情况，并允许其继续进行）。

此外，考虑到安全团队对不同应用的可见性和控制权限存在差异，且许多应用根本未纳入集中管理或不为安全团队所知，要审计应用和身份体系的混乱状况绝非易事。

文章翻译自：https://www.bleepingcomputer.com/news/security/how-attackers-are-still-phishing-phishing-resistant-authentication/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?hEPWka2j)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https...