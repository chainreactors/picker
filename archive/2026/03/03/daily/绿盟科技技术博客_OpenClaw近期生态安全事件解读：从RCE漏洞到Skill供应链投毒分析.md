---
title: OpenClaw近期生态安全事件解读：从RCE漏洞到Skill供应链投毒分析
url: https://blog.nsfocus.net/openclaw%e8%bf%91%e6%9c%9f%e7%94%9f%e6%80%81%e5%ae%89%e5%85%a8%e4%ba%8b%e4%bb%b6%e8%a7%a3%e8%af%bb%ef%bc%9a%e4%bb%8erce%e6%bc%8f%e6%b4%9e%e5%88%b0skill%e4%be%9b%e5%ba%94%e9%93%be%e6%8a%95%e6%af%92/
source: 绿盟科技技术博客
date: 2026-03-03
fetch_date: 2026-03-04T04:02:52.035330
---

# OpenClaw近期生态安全事件解读：从RCE漏洞到Skill供应链投毒分析

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# OpenClaw近期生态安全事件解读：从RCE漏洞到Skill供应链投毒分析

### OpenClaw近期生态安全事件解读：从RCE漏洞到Skill供应链投毒分析

[2026-03-03](https://blog.nsfocus.net/openclaw%E8%BF%91%E6%9C%9F%E7%94%9F%E6%80%81%E5%AE%89%E5%85%A8%E4%BA%8B%E4%BB%B6%E8%A7%A3%E8%AF%BB%EF%BC%9A%E4%BB%8Erce%E6%BC%8F%E6%B4%9E%E5%88%B0skill%E4%BE%9B%E5%BA%94%E9%93%BE%E6%8A%95%E6%AF%92/ "OpenClaw近期生态安全事件解读：从RCE漏洞到Skill供应链投毒分析")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 63

### **引言**

2025年底至2026年初的技术演进历程中，AI领域经历了一场从对话式向自主式智能代理的转变。在这一技术浪潮中，由开发者Peter Steinberger发起并主导的开源项目OpenClaw（其早期曾用名为Clawdbot与Moltbot）无疑成为了整个行业内最具颠覆性与标志性的核心技术[1]。作为一个完全开源的AI智能体框架，OpenClaw在2026年1月下旬迎来了历史性的爆发式增长。在短短数周的时间内，该项目在GitHub上获得了超过14.5万颗Star，吸引了超过10万名活跃用户进行本地部署与二次开发，成为GitHub历史上用户基数与关注度增长最快的开源代码仓库之一[3]。

OpenClaw之所以能够在极短时间内引发全球范围内的追捧，核心逻辑在于它彻底打破了传统SaaS化大模型，如ChatGPT、Claude网页端的封闭交互边界，赋予了大模型真正在物理世界中的行动执行能力。架构设计上，OpenClaw将复杂的AI底层调用逻辑与用户日常使用的即时通讯软件，如WhatsApp、Telegram、Slack、飞书等进行了深度整合。这使得OpenClaw不仅是一个被动回答问题的聊天机器人，而是一个能够24小时在线、具备持续记忆能力，并能代为执行复杂系统级任务的全能个人助理[3]。

然而，OpenClaw赋予AI模型极高系统特权的架构设计，那么当AI代理能够直接调用操作系统API时，任何逻辑缺陷或配置错误都将带来破坏性后果。据网空引擎Censys和Bitsight的探测数据显示，在2026年1月至2月期间，全球范围内暴露在公网上的OpenClaw实例高达42000余个，这些未受保护的节点吸引着大量的自动化漏洞扫描与定向攻击[6]。 在2025年12月至2026年2月期间，OpenClaw生态系统遭遇了全方位、多维度的安全挑战，涵盖了从因Vibe Coding导致的Moltbook敏感数据泄露事件、针对本地敏感配置文件的定制化窃密木马Vidar Infostealer事件、核心网关组件gateway的1-Click远程代码执行高危漏洞CVE-2026-25253，再到ClawHub供应链投毒攻击[2]。

本文将对上述四起相关安全事件进行技术剖析、逻辑还原与复盘。通过对真实攻击链路的深度分析，帮助读者深刻理解OpenClaw及其底层大模型在工程实践中所面临的安全脆弱性。

**Openclaw相关安全事件时间线**

2025年11月 – 12月：项目以Clawdbot/Moltbot名称进行早期孵化与内测，早期采用者开始探索本地优先的Agent架构，安全防护完全依赖底层操作系统的默认权限控制。

2026年1月24日 – 28日：项目更名为OpenClaw， Moltbook社交平台上线， 首批28个恶意Skill被上传至ClawHub。GitHub Star数以每日29%的速度激增；大量未配置网络隔离的网关实例暴露于公网；供应链投毒初见端倪。

2026年1月30日 – 31日: Wiz安全团队发现并通报Moltbook平台严重的数据库配置失误； OpenClaw紧急发布v2026.1.29补丁修复CVE-2026-25253；Moltbook平台因Vibe Coding导致的150万核心凭证泄露事件全面爆发。

2026年2月1日 – 13日: ClawHavoc供应链投毒达到顶峰，超800个恶意skill泛滥；Hudson Rock首次捕获针对OpenClaw配置文件的Vidar窃密木马变种。社区紧急推出Clawdex与Skill Evaluator等扫描工具；攻击者战术从传统浏览器窃密正式转向Agent AI认证窃密。

2026年2月中旬 – 至今：创始人Peter Steinberger加入OpenAI，OpenClaw转入独立基金会运作；SecureClaw等OWASP标准防护工具发布。确立了VirusTotal扫描机制；行业开始系统性构建针对Agentic AI的防御架构与行为审计规则。

### **一.  事件分析**

#### **事件一：OpenClaw核心AI Agent社交平台Moltbook因Vibe Coding缺乏安全审计导致150W Agent凭据泄露，零代码不应等同于零审计**

在OpenClaw生态快速扩张过程中，作为其核心第三方AI Agent社交平台的 Moltbook最为瞩目。然而，2026年1月31日爆发的严重数据泄露事件，不仅使 150 万个Agent凭据面临失控，更暴露了业界推崇的Vibe Coding模式所蕴含的系统性风险。对于AI原生应用而言，自动化安全扫描与人工代码审计不是可选的附加项，而是维持平台信任的根本。

**1.1.1事件背景**

Moltbook在业内被广泛定义为“专为AI Agent设计的Reddit”。其创新之处在于，允许那些运行在用户本地设备上的OpenClaw智能体拥有独立的社交网络身份，并在平台上进行自主发帖、评论、点赞与相互协调互动，甚至有超过一百万个人工智能代理在此平台上进行人类难以完全理解的自主社交。2026年1月31日，云安全研究团队Wiz的研究员发现了Moltbook后端基础设施存在的配置错误[8]。该平台的后端数据库不仅对所有持有前端公开密钥的用户开放了完全的读取权限，更暴露了不受限制的写入权限。这意味着任何发现该API端点的网络监听者或恶意攻击者，均可对整个平台的数据库进行拖库、篡改甚至删除操作[7]。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片1-300x195.png)

图1.Moltbook平台页面

**1.1.2事件根因溯源**

经过Wiz的技术溯源与取证分析表明，此次重大数据泄露的根本原因并不在于某种复杂的0 Day漏洞，而在于最基础的访问控制机制问题，这直接指向了其开发模式Vibe Coding。Moltbook的创始人Matt Schlicht在社交媒体上公开承认自己没有为Moltbook写过一行代码，仅仅构思了技术架构的愿景，而所有的全栈代码实现均由AI代码生成工具全自动完成。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片2-300x162.png)

图2. Moltbook是Vibe-Coding的产物

Moltbook采用了后端即服务平台Supabase作为其数据存储与API路由层。正常的Web应用架构设计中，前端的JavaScript打包文件中包含Supabase的公共匿名密钥是标准且合法的做法[9]。但这种架构的安全前提是：后端数据库必须启用并严格配置行级安全策略（Row Level Security, RLS）。RLS策略的作用在于充当最后一道防线，确保即便前端发来了携带Anon Key的请求，数据库层面也会核实该请求所属的用户身份，并严格限制其只能读取或修改user\_id字段与当前验证身份相符的数据行。

导致该事件的根因在于，AI模型在生成功能完备的CRUD代码时，虽然实现了业务逻辑，但默认没有生成任何关于RLS的安全策略代码。对于缺乏底层架构理解的开发者而言，系统能跑就意味着开发完成，完全忽视了Supabase在未配置RLS时的默认行为，即对所有携带Anon Key的请求授予公共访问的最高读写权限[8]。Wiz研究团队通过最简单的浏览器F12开发者工具抓取该密钥后，仅需构造基础的REST API请求，即可直接访问底层的所有数据表。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片3-300x191.png)

图3. 事件受影响的数据库表

**1.1.3泄露数据分析与影响**

Wiz团队对泄露的数据库进行了盘点，虽然Moltbook宣称拥有150万个注册的AI Agent，但在对暴露的数据库表进行深度分析后，研究人员发现实际控制这些Agent的真实人类账号仅有约17000个。这意味着平均每个人类用户控制着约88个Agent，且系统中充斥着大量利用自动化脚本批量注册的僵尸粉。平台在追求用户量增长的过程中放弃了对Agent真实性的验证机制，如人机验证码或API速率限制。更值得注意的是核心凭据资产的以明文方式进行存储并遭到泄露。根据安全审计，以下数据资产遭到了完全暴露：

* 150万+ Agent API Tokens: agents表中存储的完整认证令牌，攻击者利用这些Token可以直接接管任何Agent的身份。
* 1.7万+人类所有者数据: owners表中包含真实用户的电子邮件地址。
* 2.9万+待发布产品预约邮箱: 通过GraphQL发现的observers表，暴露了早期注册用户的隐私。
* 4000+私信记录: agent\_messages表中存储Agent之间的私密聊天记录。严重的是，这些记录未加密存储，Wiz在审查中发现部分消息内包含了用户通过私信分享的OpenAI API Key等第三方服务明文凭据。
* 写权限暴露: 攻击者不仅能读取数据，还能任意修改或删除平台上的帖子。Wiz团队演示了修改置顶帖子的能力，理论上攻击者可以利用此权限注入恶意Prompt，对阅读帖子的其他Agent发起大规模的间接提示注入攻击。

该事件最严重的资产损失是存储在agents表中的近150万个API身份验证令牌。这些令牌是受害者连接到OpenAI、Anthropic、AWS、GitHub以及Google Cloud等高价值第三方基础设施的访问凭证。 Moltbook的开发者将这些高权限密钥以纯明文的形式存储在数据库中，未进行任何加密处理。这意味着攻击者一旦获取数据库的读取权限，便可直接复制这些密钥并用于接管受害者的AI Agent，或在暗网出售这些密钥以供他人盗刷计算资源，给受害者带来巨大经济损失。

```
#通过窃取泄露Key可通过rest api 执行select操作，从而获取用户api_key信息curlhttps://ehxbxtjliybbloantpwq.supabase.co/rest/v1/agents?select=name,api_key&limit=3" -H "apikey: sxxxxxxx"
```

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片4-300x141.png)

图4. 通过前端泄露的Key进一步获取存储在Moltbook中的用户API Key信息

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图片5-300x137.png)

图5. Moltbook后端数据库存储API Key等敏感数据没有进行任何加密

**1.1.4威胁升级：写权限暴露**

Wiz研究团队在测试中确认，即使在Moltbook进行第一轮紧急修复之后，针对公共帖子表的写入访问仍然保持完全开放。研究人员通过发送PATCH请求，成功演示了无需任何身份验证即可修改平台上现有帖子的能力。

```
curl -X PATCH "https://ehxbxtjliybbloantpwq.supabase.co/rest/v1/posts?id=eq.74b073fd-37db-4a32-a9e1-c7652e5c0d59" -H "apikey: sb_pubxxxx-" -H "Content-Type: application/json" -d '{"title":"@galnagli - responsible disclosure test","content":"@galnagli - responsible disclosure test"}'
```

在以Agent为主要受众的社交网络中，这构成了极度危险的攻击向量。攻击者不仅可以任意篡改内容、发布虚假信息，更可以利用此权限将恶意的提示词注入到置顶或高流量的帖子中。

**1.1.5漏洞响应与时间线**

* 2026年1月31日21:48: Wiz安全团队通过 X私信联系Moltbook维护者，通报漏洞；
* 2026年1月31日22:06: Moltbook确认漏洞核心点在于其Supabase数据库未启用 RLS，前端JS文件中硬编码的API Key可直接读写数据库。
* 2026年1月31日23:29: Moltbook进行了第一轮修复，锁定了agents、owners 和site\_admins 表的读取权限；
* 2026年2月1日00:31: Wiz研究人员复测发现仍有写权限，并尝试成功篡改了平台上的帖子内容；
* 2026年2月1日 01:00: 最终修复完成，所有表包括私信、通知、投票等的 RLS策略部署完毕，漏洞彻底堵死；
* 后续: 社区发布公告，建议所有用户重置Agent密钥，并提出“Vibe Coding”必须配合自动化安全扫描。

#### **事件二：OpenClaw本地配置文件明文存储致Infostealer变种狩猎，超过百万终端AI身份面临接管风险，开源软件切勿“开源”机密数据**

**1.2.1事件背景**

2026年2月中旬，传统窃密木马Infostealer Vidar的变体被捕获，标志着攻击者的目标已从传统的浏览器Cookie转向了AI Agent的核心资产。从本质上看，这依然是传统窃密手段的延伸。攻击者只需在原有的木马扫描项中增加对 OpenClaw配置文件目录的抓取，便能以低成本实现从账号窃取到接管智能体的跨越。过去黑客关注的是登录凭证，现在通过窃取本地存储的认证令牌与设备私钥，攻击者可以轻易获取受害者的AI身份。

**1.2.2攻击目标转移：从浏览器Cookie到AI Agent**

2026年2月13日，网络安全公司Hudson Rock在监控全球受感染设备的数据回传流量时，检测到一个包含完整.openclaw目录的ZIP压缩包，从而首次确认了活跃在野外针对该AI工具配置文件的定向窃密攻击。安全专家进行了逆向分析得知该恶意软件是窃密木马Vidar的新变种。

此次攻击的威胁在于攻击者并不需要去挖掘OpenClaw代码本身的复杂0 Day漏洞，仅仅需要更新木马配置文件中的“文件抓取器（File Grabber）”规则模块，将token和private key等高价值关键字以及默认存储目录~/.openclaw加入扫描列表即可。当受害者因安全意识薄弱而执行了携带木马的程序时，木马便会利用当前操作系统赋予该用户的默认读写权限，在后台扫描并迅速打包整个OpenClaw的本地配置目录，完成数据外传。

该事件也说明过去的窃密焦点集中在浏览器的历史记录、Cookie和保存的密码上，而现在黑客正致力于窃取受害者的AI数字身份与智能体的配置上下文。

**1.2.3泄露数据分析与影响**

OpenClaw的本地优先架构设计为了追求响应速度与用户自定义自由度，默认将大量极其敏感的配置文件与持久化记忆数据以纯明文的形式存储在宿主机的文件系统中。Hudson...