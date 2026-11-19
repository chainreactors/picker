---
title: 一夜之间，178 家国际大牌网站被集体\"投毒\"：Optimizely 供应链攻击全解析
url: https://mp.weixin.qq.com/s/afhqWeyM9Lh3hjCNLpTPlg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:38:48.577253
---

# 一夜之间，178 家国际大牌网站被集体\"投毒\"：Optimizely 供应链攻击全解析

# 一夜之间，178 家国际大牌网站被集体"投毒"：Optimizely 供应链攻击全解析

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

**↓**以下为文字阅读版

> 攻击者没有入侵 CNN，没有入侵 BBC，也没有入侵 Zoom。他们只在一个 A/B 测试平台的项目字段里，写下了几行 JavaScript——然后，全球 178 家组织的网站访问者，都在周一那天加载了这段代码。

2026 年 11 月 16 日，一个再普通不过的周一。但这一天，至少 178 家组织网站的访问者，从这些网站"自己信任的域名"上加载了一段恶意 JavaScript。Optimizely 今天凌晨发布通告确认：攻击者利用了其 Web Experimentation 产品中的一个漏洞，把恶意代码写进了部分客户项目 [1][3]。据监测网站脚本运行的公司 Report URI 统计，受影响名单里包括 CNN、BBC、Zoom、Salesforce、GitLab、IKEA、HSBC、Equifax、法荷航集团、硬件钱包厂商 Ledger、流媒体服务 Peacock——甚至 Optimizely 自己的官网和登录页 [1][2]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZhuVaZsDBHEw422ThQ85T2AT4dDEibbbIR5nvZVLh2jn7u9JtOpTqbicEcqNJkKbFADDHpm2MehHsJ7TibqTU6k9qbW3IVoEI3eak/640?wx_fmt=png&from=appmsg)

这不是一次 CDN 缓存投毒，也不是针对某家网站的黑客入侵。它揭示的问题更扎心：**你信任的第三方脚本，随时可能不再值得信任。**

## 完美的投毒点：一个字段，全站沦陷

要理解这次攻击的精妙（或者说恶劣）之处，得先看 Optimizely Web 的工作方式。

使用 Optimizely 做 A/B 测试的网站，会在页面里放一个 script 标签，从 `cdn.optimizely.com` 加载一段属于自己项目的"snippet"脚本。这段脚本里除了 Optimizely 的运行时代码和实验配置，还有一个可选字段——Project JavaScript：客户在 Optimizely 后台自己写的自定义代码，**每次页面加载 snippet 时都会执行** [2]。

攻击者做的事非常简单：把恶意加载器写进了大量互不相关的客户项目的这个字段里。snippet 的其余部分原封未动，文件依然从 `cdn.optimizely.com` 下发，依然带着 Optimizely 的 TLS 证书 [2]。Report URI 的创始人 Scott Helme 在分析中特意强调了一句：

> "Optimizely 的 CDN 只是如实下发了它被给予的内容；这不是一次 CDN 缓存投毒攻击。"（来源：Report URI 博客）

这句话的分量在于：**攻击没有触碰"分发"环节，只篡改了"内容"本身。** 对于每一个受影响的网站来说，域名是对的、证书是对的、加载路径也是对的——任何基于"这个脚本来自可信域名"的信任判断，在这里全部失效。哪怕网站把自家服务器防护得固若金汤，访客的浏览器照样执行了恶意代码，因为代码根本不来自网站自己的基础设施 [2]。

更有意思的是，有些客户选择从自己的域名代理下发 snippet（比如 `opt.scheels.com`、`www.vodafone.com.au`），它们同样中招——因为内容归根结底还是来自同一个 Optimizely 项目 [2]。

## 一个 UTC 日内的完整攻击剧本

Report URI 根据自己的爬虫数据和 urlscan 公开记录，还原了一条罕见完整的攻击时间线 [2]。它读起来几乎是教科书级的：

* **04:21** — 首次注入出现在 BBC 的 snippet 中，此时加载的还是 `webshell[.]lol`（研究者认定与本次攻击者同源）；
* **05:23** — 攻击者当天下单注册了载荷域名 `1688360[.]cc`，一小时前刚签好证书；
* **08:10** — 载荷 track.js 首个版本构建完成，是一个加密货币地址替换器（clipper）；
* **08:28** — track.js 首次出现在 bbc.com 的页面上；
* **13:03** — 攻击者把已窃取的加密货币转移至交易所；
* **13:43** — 载荷"升级"，加入银行卡信息窃取功能；
* **17:13 起** — 面向旧版 iOS 设备的第二阶段投递上线；
* **~20:40–21:10** — 大规模清理开始（Ledger 20:41、Smartsheet 20:56、BBC 21:07）；
* **21:52** — 188 个被感染 snippet 中只剩 TalkTalk 一家还带代码；
* **23:11** — 全部清理完毕 [2][4]。

对多数网站而言，暴露窗口约 16–19 小时 [4]。还有一个细节值得注意：Smartsheet 的脚本曾被清理，随后又被一种隐藏版本的代码重新感染——Report URI 据此判断，在那一刻攻击者依然保有访问权限 [1][2]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZhenrKSiceLGOI0mpO1vpvXyfIvlBLNnTsLX2PmzgBYXa77ty4HibDIkVad2aOZjz1IcL3OTLY9g18ywM83KxYoK2MxOJicU1AqVk/640?wx_fmt=png&from=appmsg)

当天，攻击者把 payload 重建了 26 次，只增加收款钱包，从不删除旧的 [2]。这不是一次性手工作案，而是一个持续调优的攻击程序。

## payload 四件套：换币、掠卡、偷会话、打 iPhone

Report URI 保存了感染文件的完整副本，StepSecurity 随后对最终版 track.js（约 30KB）做了文本级分析。这个脚本由几个相互独立的功能块组成，对每个访客**同时生效**，具体遭遇到什么取决于设备类型和页面上的行为 [2][4]。

**第一件：加密货币地址替换。** 脚本内置了对比特币、以太坊及 EVM 链、TRON、Solana、TON、莱特币、BCH、狗狗币等主流链的地址识别。它只替换通过链上校验和验证的"真实地址"——这一点很关键，替换出去的地址同样是合法格式，受害者的钱包会照常接受 [2][4]。替换范围覆盖页面文本、表单、链接和图片属性、复制事件、剪贴板 API、`fetch`/XHR 请求的 URL 和请求体，甚至 iOS 的分享面板；StepSecurity 还发现它 hook 了 `Function.prototype.call` 和 `apply`——只要一个字符串长得像钱包地址，在进入任何函数之前就会被改写 [4]。只有当替换目标附近出现 wallet、deposit、send 这类支付相关词汇时，脚本才会动手，以降低暴露风险 [1][4]。换句话说：你在受影响页面上复制一个收款地址，粘贴进钱包的很可能已经是攻击者的地址。

**第二件：银行卡窃取。** 13:43 UTC 加入。脚本监听表单提交和所有 `fetch`/XHR POST 请求，一旦凑齐卡号（经 Luhn 算法校验）、有效期和 CVV 三要素，就用 `navigator.sendBeacon` 把它们发送到 `1688360[.]cc/card.php` [2]。不过它受浏览器同源策略限制：**填在托管支付 iframe（如 Stripe、Adyen 的托管表单）里的卡不在其触达范围内；填在网站自己表单字段里的卡则难逃一劫** [1][2]。这个区别，直接决定了不同网站的访客风险天差地别。

**第三件：Cookie 与页面截图窃取。** 当脚本成功替换了一个紧邻支付措辞的地址时，它会把页面 URL、非 HttpOnly 的 Cookie（`document.cookie` 能读到的部分）、被替换的原始地址，以及用 html2canvas 渲染的整页截图，发送到 `1688360[.]cc/hit.php` [2]。HttpOnly Cookie 读不到——这是浏览器最后的防线之一。

**第四件：iOS 利用工具包。** 在 iPhone 和 iPad 上，脚本会从两个 `.icu` 域名加载 `boot.js`，读取 iOS 版本后在隐藏 iframe 里打开对应的利用链：iOS 13–17 走 Coruna，iOS 18.x 走 DarkSword，iOS 26 则走一条目前只做设备指纹采集的独立链。利用工具包自带的注释显示，iOS 18.7.3 及以上、26.3 及以上版本已修补 [1][2]。值得注意的是：Cynet 的研究人员是通过模拟 iPhone 浏览器环境获取第二阶段的，他们明确将其描述为"条件化投递"，**并非对实体 iPhone 或 iPad 的成功攻陷**，目前也没有真实 iOS 设备被接管的证据 [1][5]。一个可供普通用户自查的可见症状是：iOS 18.6 及更早版本的页面会每 60 秒自动重载一次以重试利用 [2]。

**已经到手的钱呢？** Report URI 统计，截至 11 月 16 日 19:25 UTC，攻击者的钱包在约 9 小时内收到了数千美元（不同研究机构的统计口径略有差异），并在 13:03–13:05 UTC 转移至交易所 [2][4]。但两家机构都强调：链上数据无法证明这些转账来自本次攻击的受害者，也**无法统计有多少卡号和 Cookie 真正到达了攻击者的服务器** [1][4]。StepSecurity 还注意到，其中一个 TRON 钱包自 2026 年 3 月起就在使用——这名攻击者在本次活动之前早已活跃 [4]。11 月 17 日凌晨 4 点到 5 点半之间，所有钱包被清空 [4]。

## 官方回应，和一个未解之谜

Optimizely 于 11 月 17 日 01:02 UTC 在状态页发布事件通告：未授权方"利用了 Experimentation 中的一个漏洞"，向部分客户项目添加了恶意 JavaScript；公司已修复漏洞、移除受影响项目中的注入代码，并对受影响账户采取了安全措施、增加了防止未授权代码下发的防护 [3]。

随后，Optimizely 向 BleepingComputer 表示，漏洞**位于 Experimentation 的账户注册流程**，公司已封锁易受攻击路径、终止活跃会话、吊销令牌、重置受影响账户的访问权限，并已通知所有受影响客户 [4][7]。

但这里留下了一个所有人都想知道答案的问题：**一个注册流程的漏洞，是如何让攻击者获得对大量互不相关客户项目的写权限的？** 通告没有说明漏洞的技术细节、有多少项目被修改、修复何时上线，也没有回答攻击者是否还留有访问通道 [1][6]。Scott Helme 的原话是："我们不知道攻击者是怎么拿到这么多互不相关客户项目的写权限的——这得由 Optimizely 来解释。" [2] 截至本文发稿，这个问题仍然没有公开答案。

另一个好消息是：载荷服务器已经下线——注册局于 11 月 17 日 00:37 UTC 将 `1688360[.]cc` 置于 hold，域名停止解析 [4]。

## CSP 的现实检验：159 家网站，只有 24 家挡住了

这次事件最发人深省的部分，也许是 Report URI 对受影响网站 Content Security Policy（CSP）的统计 [2][6]。

在评估的 159 个组织中：

* **68 家根本没有 CSP**；
* **50 家的 CSP 形同虚设**——策略同时放行了恶意代码和数据外传；
* **17 家拦下了一半**——`connect-src` 限制挡住了卡号、Cookie 和截图外传，但恶意代码照常执行，而且页面内的钱包地址替换发生在页面内部，`connect-src` 根本管不着；
* **只有 24 家（15%）完全拦截了恶意代码**——它们的共同点是有一条限制性的 `script-src` [2][6]。

为什么白名单几乎全军覆没？因为常规做法是在 `script-src` 里允许 `cdn.optimizely.com`——而恶意代码恰恰就来自这个域名。Report URI 的结论一针见血："把 cdn.optimizely.com 加进白名单，从来都帮不上忙。" [2] 更尴尬的是两个常见的 CSP 宽松配置：`strict-dynamic` 会让经可信脚本插入的代码自动获得放行，`unsafe-eval` 则允许那段内联后备 payload 执行——而 Optimizely 官方文档的 CSP 示例，本身就推荐包含 `strict-dynamic`，完整示例里还有 `unsafe-eval` [6]。

CSP 能管的是"代码从哪来"，管不了"代码是否诚实"。当恶意代码与合法代码同源时，唯有把白名单收紧到"确实需要的少数域名"，才有可能在投递链条的下一环把它截住 [2][6]。

## 现在该做什么

**如果你运营使用 Optimizely Web 的网站**，Report URI 和 StepSecurity 给出的建议相当具体 [1][4]：

* 逐个打开每个项目的 Project JavaScript 和每个实验的自定义代码，搜索 `1688360`、`atob(` 以及任何不是你们写的脚本——注意 `atob(` 才能找出 base64 隐藏版本，单搜域名会漏；
* 审查哪些用户、API 令牌和集成拥有写权限，并轮换凭据；
* 如果你的表单自己收集卡信息，周一（11 月 16 日）输入的卡应视为可能已暴露；
* Cookie 里未加 HttpOnly 的会话令牌或敏感信息，一律轮换；
* 部署带严格 `script-src` 和 `connect-src` 的 CSP——但别指望放行 `cdn.optimizely.com` 能起作用；
* 结账页不放第三方标签，卡信息一律走支付服务商的跨域托管 iframe。

**如果你在 11 月 16 日访问过受影响网站**：

* 把 iPhone/iPad 更新到 iOS 18.7.3 或 26.3 以上 [1]；
* 核对当天的加密货币支付地址是否与你打算支付的地址一致 [1]；
* 在受影响网站刷过卡的，留意账单 [1]。

Cynet 特别提醒：`cdn.optimizely.com` 是合法的投递主机，不建议对它或相关新闻网站做粗暴封禁 [1]。另外，现在 snippet 干净了，不代表周一它没发过恶意代码——暴露窗口内的访客仍然需要按上述清单处理。

## 结语：信任链条上的每一环，都需要自己的防线

复盘这次攻击，它其实没有用到任何惊天动地的技术：一段几十行的加载器、一个当天下单的域名、一个约 30KB 的 JavaScript 文件。真正可怕的是它的杠杆率——写入一个 SaaS 平台的项目字段，就能覆盖上百家网站的所有页面，而且全程披着"可信域名 + 有效证书"的外衣。受影响网站自身的代码和基础设施，从头到尾都是干净的。

对从业者来说，至少有四条教训值得写进值班手册：第一，第三方脚本的"可信"是动态的，供应链上的任何一环被改写，你的信任模型就作废；第二，CSP 白名单要收紧到真正需要的最小集合，别让 vendor 文档里的宽松示例替你做决定；第三，支付环节尽量隔离——托管支付 iframe 和 HttpOnly 这类"最后一道防线"，在这次事件里确实挡住了一部分攻击；第四，SaaS 平台账户里的自定义代码字段（projectJS、API 令牌、集成授权）应该和你的生产服务器放在同一张审计清单上。

Optimizely 说漏洞已经修复、代码已经清除，这很好。但"攻击者如何获得跨客户项目的写权限"这个问题的公开答案还没出现。在它出现之前，最好假设：任何你能往里贴代码的第三方平台，都可能成为下一个投毒点。

## 参考资料

1. Hijacked Optimizely Scripts Served Card Skimmer and iOS Exploit Kits to CNN, BBC and Zoom Visitors
2. World's Largest Brands Infected With Malware Via Optimizely
3. Optimizely Service Status — Web Experimentation Security Incident来源：
4. OPTIMJACK: Optimizely-Hosted Scripts Loaded a Crypto Clipper and Card Skimmer on 178 Organizations
5. OPTIMJACK: Malicious web injection across CNN, Zoom, Salesforce, Fox and more
6. Lessons From the Optimizely Web Experimentation Compromise
7. Optimizely Says Attacker Used A Signup Flaw To Inject Malware

- END -

**感谢阅读，如果觉得还不错的话，动动手指给个三连吧～**

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZj0vZ4HI9JCibQwzj9ZHia88e3thicG9MD8BG7hfmbSq8EeqG0WRO...