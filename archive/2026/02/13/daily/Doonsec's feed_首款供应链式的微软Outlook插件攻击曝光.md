---
title: 首款供应链式的微软Outlook插件攻击曝光
url: https://mp.weixin.qq.com/s/-qy7B7vQPkHJtIBIXDfJUg
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:03:21.909895
---

# 首款供应链式的微软Outlook插件攻击曝光

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoFQMA37pubwVrY4yJlWMWicA6N541V1zxgqF2u6sffrPKE04c1aIKOSZ7sjpHXOB57e0T94M0n21jXOia7wxICVib4FRVErq4CHU/0?wx_fmt=jpeg)

# 首款供应链式的微软Outlook插件攻击曝光

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

# 2026 年 2 月 11 日，Koi Research 发布的一份安全研究报告，揭开了首个在野生环境中被发现的恶意 Microsoft Outlook 插件：AgreeToSteal

#

# 这款由一款废弃的合法办公插件被攻击者恶意劫持改造而来的插件，已造成超 4000 名用户的微软账户凭证、信用卡信息、银行安全答案等敏感数据被盗，且截至报告发布时，相关攻击基础设施仍处于活跃状态，新的受害者还在持续增加。

#

# 这起事件并非一次简单的钓鱼攻击，其背后暴露出的微软 Office 插件生态的结构性安全缺陷，更是为整个办公软件生态的安全防护敲响了警钟。

#

AgreeToSteal 的前身，是 2022 年开发者推出的一款名为 AgreeTo 的会议调度插件，彼时这款插件凭借实用的功能收获了用户的认可，不仅成功上架微软 Office 插件商店，其配套的 Chrome 扩展程序也拥有 1000 名用户，斩获了 4.71 星的良好口碑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpvQnOgbO3obthSvBAkDX2d7wInQ2RMbczGhQmrplia0JO2ibYG9kbah9LibHUfX90txIrAWfb8dpKjFudOAtMc8z7r7HBnL03Tss/640?wx_fmt=png&from=appmsg)

开发者为其搭建了完整的技术架构与商业体系，包含 Microsoft Graph API 集成、谷歌日历支持、Stripe 计费等功能，是一款真正投入商业开发的产品。

但好景不长，这款插件的开发进程突然中断，2023 年 5 月，其 Chrome 扩展停止更新；2024 年，开发者的官方域名 agreeto.app 过期，用户开始反馈插件无法正常使用；2025 年 2 月，谷歌终于移除了这款失效的 Chrome 扩展。

令人遗憾的是，AgreeTo 的 Outlook 插件版本却一直留在微软 Office 插件商店中，其指向的 Vercel 子域名 outlook-one.vercel.app 因项目废弃成为无主可认领状态，而更关键的是，这款插件在上架时被微软授予了**ReadWriteItem 权限，** 可直接读写用户的邮件内容，这一为满足会议调度功能设置的权限，也为后续的恶意攻击埋下了致命伏笔。

此次攻击的发生，核心源于微软 Office 插件的底层运行机制缺陷。与传统的本地安装代码不同，Office 插件本质上是通过加载远程 URL 在 iframe 中运行，微软仅在插件提交时对其 XML 清单文件进行审核并签名，后续便不再对 URL 指向的实际内容进行任何检查。整个过程既无静态包审计，也无哈希验证，URL 控制权的变更会直接改变插件的运行内容，且插件被授予的权限不会随内容的变更而失效。这一机制让攻击者有机可乘，也让微软的官方审核体系沦为 “一次性门槛”。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqKMriaMyhmZZKpWYmhAHiaeAcZXLsqzWjq58ShUESzLoDC9M5cOUzhus0xNYHGOe0oy6SLsnvqlmpibDXqQu3bibPMtmNXricianNGc/640?wx_fmt=png&from=appmsg)

攻击者并未花费过多精力突破微软的安全防线，而是简单认领了无主的 outlook-one.vercel.app 域名，部署了一套包含伪造微软登录页、凭证收集脚本、数据泄露程序和重定向页面的钓鱼工具包。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDquK8tZI2mO65vuKszCv1ssXAjknoXW9GIhAyLGUFribtS1Lb5C3pKgwDqZCTmNOFP78LubFBF4yMF55icgYXdOcdjYerPDIm5cA/640?wx_fmt=png&from=appmsg)

整个过程中，攻击者无需向微软提交任何内容，也无需通过任何二次审核，直接利用微软已签名的插件清单，就让恶意内容在 Outlook 的可信侧边栏中顺利运行。当受害者打开这款看似合法的插件时，看到的并非会议调度界面，而是以假乱真的微软登录页，在输入邮箱和密码后，相关信息会与受害者的 IP 地址一起被 JavaScript 脚本收集，通过 Telegram Bot API 直接发送给攻击者。随后页面会无缝跳转到真实的微软登录页，受害者往往会误以为只是正常的重新登录，全程对信息被盗毫无感知。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrhfGfj02Ybu6TPgGY3mIEW97H25mqe6HibiarKghLR3WbpuVywQL6eJh07MFe1aHQomn2DMjiakqZOQeqzgN5BQxp4sy3rhqOhpA/640?wx_fmt=png&from=appmsg)

这起攻击的规模与攻击者的专业性，远超普通的钓鱼行为。因攻击者的信息泄露渠道防护极为薄弱，Koi Research 成功攻破并恢复了完整的被盗数据，确认超 4000 名用户遭受损失，被盗信息不仅包括微软账户的邮箱和密码，还涵盖信用卡号、CVV、PIN 码、银行安全答案等核心金融信息。经调查，该攻击者并非个人，而是一个专业的钓鱼团伙，其运营着至少 12 个针对不同品牌的钓鱼工具包，涉及加拿大的互联网服务提供商、银行、网页邮箱等多个领域，AgreeToSteal 只是其众多攻击分发渠道中的一个。截至报告发布时，攻击者仍在主动测试被盗的用户凭证，攻击活动持续发生，每小时都有新的受害者出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpyoAibkumvPHWiccwlCRrj1iaibBkic2EW8jiaNHUSBIza9uicrGvTRZfO9tIyFBa1tn4nLxmTFlItz9bVJN9iaSe0mVjX5dQdgymW6gk/640?wx_fmt=png&from=appmsg)

更值得警惕的是，面对这场攻击，现有网络安全防护体系几乎全面失效。邮件安全网关无法识别该攻击，因为恶意内容并非通过邮件传播；终端防护软件没有任何预警，因为恶意脚本运行在合法的微软进程中；URL 过滤工具也难以察觉，因为恶意页面托管在 vercel.app—— 这个承载着数百万合法应用的平台上。攻击技术本身极为基础，但依托微软官方插件基础设施的 “可信背景”，让其成功绕过了所有常规防护。

而这起事件暴露的最深层问题，是微软 Office 插件生态的**结构性漏洞**。Office 插件属于远程动态依赖程序，其内容可随时通过 URL 进行变更，微软的单点审核模式在这种架构下完全失效。

更可怕的是，此次攻击者仅将插件用于简单的钓鱼页面，而该插件拥有的 ReadWriteItem 权限，本可让攻击者部署恶意脚本，悄无声息地读取受害者的收件箱、窃取敏感邮件，甚至以受害者的身份发送钓鱼邮件，引发连锁式的攻击，其潜在危害远不止于信息被盗。

事实上，早在 2019 年，MDSec 的安全研究人员就已预警 Office 插件的攻击面风险，指出微软插件商店的模式存在巨大安全隐患，而七年之后，这一预警竟精准成为现实。

针对此次 AgreeToSteal 攻击事件，已采取了一系列处置行动：公布了攻击的核心指标（IOCs），包括钓鱼域名 outlook-one.vercel [.] app、插件 ID WA200004949；分别向微软、Vercel、Telegram 提交滥用报告，要求下架恶意插件、关停钓鱼域名，并封禁攻击者的机器人和账户；同时尽可能通知了可联系到的受影响用户，提醒其及时修改密码、保护金融信息。但此次事件带来的行业思考，却远未结束。

AgreeToSteal 事件是一次典型的 “供应链式” 网络攻击，攻击者并未使用复杂的技术手段，而是利用了办公软件生态的架构漏洞和平台的审核疏漏，实现了低成本、高隐蔽性的恶意攻击。

这也让整个行业意识到，对于浏览器扩展、Office 插件、IDE 插件等自部署软件，其动态变更的特性决定了单点审核模式已无法满足安全需求，平台方需要建立**持续的监控与审计机制**，定期复检插件的实际运行内容，及时回收废弃插件的权限，建立域名变更的预警体系。

同时，企业和个人也需提高安全警惕，谨慎安装和使用各类办公插件，及时关注插件的运营状态，避免因使用废弃插件陷入信息泄露的风险。

对于微软等科技厂商而言，此次事件是一次深刻的警示：

生态的繁荣不能以牺牲安全为代价，基础设施的安全缺陷，远比单一的恶意攻击更具破坏性。唯有正视自身的架构问题，完善安全审核与监控体系，及时弥补生态漏洞，才能真正为用户构建起安全的使用环境，避免类似的恶意攻击事件持续上演。

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