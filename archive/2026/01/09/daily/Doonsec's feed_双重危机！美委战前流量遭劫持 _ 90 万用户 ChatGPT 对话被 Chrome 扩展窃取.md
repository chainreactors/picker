---
title: 双重危机！美委战前流量遭劫持 | 90 万用户 ChatGPT 对话被 Chrome 扩展窃取
url: https://mp.weixin.qq.com/s/wRSE6dAGQwmtz7U1pB33Cw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:25:48.319114
---

# 双重危机！美委战前流量遭劫持 | 90 万用户 ChatGPT 对话被 Chrome 扩展窃取

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7C6EF0N3kgicF7ovujxIIqIjicibF83H1PMQhsorxahD2YiaVtNsOTTBExg/0?wx_fmt=jpeg)

# 双重危机！美委战前流量遭劫持 | 90 万用户 ChatGPT 对话被 Chrome 扩展窃取

易云安全应急响应中心

![]()

在小说阅读器中沉浸阅读

**点击蓝字，立即关注**

**关键词**

网络攻击

网络安全博客 Low Orbit Security 日前在发布的每周安全通讯中探讨美国政府在进入委内瑞拉展开特别军事行动前，当地国有电信公司 CANTV 发生的 BGP 路由异常事件。

BGP 协议是互联网基础设施赖以运行的地图，主要工作是负责引导数据在不同的自治系统 (AS) 间传输，而 BGP 协议天生缺乏完善的安全机制，极易受到路由泄露或路由劫持攻击 (即常见的 BGP 劫持)。

![美军进攻委内瑞拉前当地电信公司BGP路由发生异常 流量被引导至不安全的路线](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljCiaBs266N3yUHtjyakZzFblz50LQrDD9NLa3kVdQUJiaABzqa05H2h8moCaKUlR3sPZGfAF938jYA/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic#imgIndex=1)

**在当地时间 2026 年 1 月 2 日左右，委内瑞拉国家电信公司 CANTV (自治系统编号 AS8048) 发生明显的异常：**

异常路径：当时有 8 个 IP 地址块 (Prefixes) 在本身不应该出现的路径中被路由，涉及到意大利传输商 Sparkle 和哥伦比亚运营商 GlobeNet。

公告波动：在发生停电事件前 BGP 公告出现了剧增，随后由于出现网络中断，已公告的 IP 地址空间出现断崖式下跌。

以上数据均来自 Cloudflare Radar。

**异常特征包括：**

流量到达委内瑞拉主要交换节点 AS21980 前被不寻常的转发，AS8048 公告中被执行了 10 次路径填充，这通常是试图隐藏特定路由优先级或者误导流量工程的手段。

安全分析师认为 10 次重复路径填充可能是用于误导自动化流量分析系统，强制流量绕道进入某些特定的中间人节点例如 Sparkle。

**Sparkle 的安全性：**

这家数据传输服务商在 isbgpsafeyet.com (由 Cloudflare 发起的监测项目)上被列为不安全，原因是他们没有强制执行 RPKI 过滤，这是一种防止 BGP 劫持的安全标准，这使得这个路径成为潜在攻击或路由泄露的薄弱点。

目前没人知道 AS8048 路由异常的原因所在，但如果是美国执行的攻击，则可以在劫持 BGP 这段时间里可以收集大量流量用于情报目的，不过具体是否是这样就不得而知了。

**关键词**

恶意软件

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljCiaBs266N3yUHtjyakZzFbrqtuia7f34P7gW7fzoVtg5l1VJqk2NHVGhYWj9NpEC3eeJjfF9nbicLA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&tp=wxpic&wx_lazy=1#imgIndex=1)

网络安全研究人员在Chrome应用商店发现两款新型恶意扩展程序，专门窃取用户与OpenAI ChatGPT的对话内容，并将浏览数据外传至攻击者控制的服务器。这两款累计用户超90万的扩展分别为：

* Chat GPT for Chrome with GPT-5, Claude Sonnet（ID: fnmihdojmnkclgjpcoonokmkhjpjechg，60万用户）
* AI Sidebar with ChatGPT, Claude, and more.（ID: inhcgfpbfdjbjogdfjbclgolkmhnooop，30万用户）

此次发现距相关扩展（在Chrome和Edge平台拥有数百万安装量）被曝监控用户与AI聊天机器人对话仅数周。Secure Annex将这种通过浏览器扩展窃取AI对话的技术命名为**Prompt Poaching**。

OX Security研究员Moshe Siman Tov Bustan指出："这两款扩展每30分钟就会将用户对话内容和所有Chrome标签页URL外传至远程C2服务器。恶意软件通过请求获取'匿名、不可识别分析数据'的权限，实则窃取ChatGPT会话中的完整对话内容。"

## 恶意扩展的运作机制

这两款恶意扩展仿冒了AITOPIA开发的合法扩展"Chat with all AI models (Gemini, Claude...) & AI Agents"（约100万用户）。截至发稿时仍可在Chrome应用商店下载，不过"Chat GPT for Chrome with GPT-5, Claude Sonnet"已失去"精选"标识。

安装后，恶意扩展会要求用户授予收集匿名浏览行为的权限，声称用于改进侧边栏体验。一旦用户同意，内嵌恶意软件便开始收集打开的浏览器标签页信息和聊天机器人对话数据。具体实现方式包括：在网页内查找特定DOM元素、提取聊天消息并本地存储，随后外传至远程服务器（"chatsaigpt[.]com"或"deepaichats[.]com"）。

攻击者还利用AI驱动的网页开发平台Lovable托管隐私政策等基础设施组件（"chataigpt[.]pro"或"chatgptsidebar[.]pro"），试图掩盖其行为。

## 潜在危害范围

安装此类扩展可能导致严重后果，攻击者可窃取包括ChatGPT对话内容、搜索记录及企业内部URL在内的多种敏感信息。OX Security警告："这些数据可能被用于企业间谍活动、身份盗窃、定向钓鱼攻击，或在暗网论坛出售。员工安装此类扩展的企业可能已无意间泄露知识产权、客户数据和商业机密。"

## 合法扩展涉足Prompt Poaching

Secure Annex披露，Similarweb和Sensor Tower旗下Stayfocusd等合法扩展（分别拥有100万和60万用户）也涉及Prompt Poaching行为。据悉Similarweb在2025年5月新增对话监控功能，2026年1月1日的更新添加了完整的服务条款弹窗，明确声明会收集AI工具输入数据以"提供流量和参与指标的深度分析"。

技术分析显示，Similarweb通过DOM抓取或劫持fetch()、XMLHttpRequest()等原生浏览器API收集对话数据，其远程配置文件包含针对ChatGPT、Anthropic Claude、Google Gemini和Perplexity的定制解析逻辑。

Secure Annex的John Tuckner向The Hacker News表示："Prompt Poaching已明确成为窃取敏感对话的新手段，浏览器扩展成为攻击载体。目前尚不清楚这种行为是否违反谷歌关于扩展应单一用途且禁止动态加载代码的政策。这只是趋势的开端，更多企业将意识到这些数据的商业价值。"

安全专家建议已安装相关扩展的用户立即卸载，并避免安装来源不明的扩展程序，即使它们标有"精选"标识。

文章来源 ：安全圈

免责声明

本文素材(包括内容、图片)均来自互联网，仅为传递信息之用。如有侵权，请联系我们删除。

**END**

![图片](https://mmbiz.qpic.cn/mmbiz_png/6aVaON9Kibf6qHRdibQTh7Bic33HXRicZowtjiavqOsjjNTNWNtssMJtfSYn6uT1PgnaWWnMlSPevI96XXRdM4tibYqQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**淮安易云科技有限公司**-******网络安全部**

我们致力于保障客户的网络安全，监控事件并采取适当措施，设计和实施安全策略，维护设备和软件，进行漏洞扫描和安全审计,团队协调处理网络攻击、数据泄露等安全事故，并负责安全服务项目实施，包括风险评估、渗透测试、安全扫描、安全加固、应急响应、攻防演练、安全培训等服务，确保客户在网络空间中的安全。

**易云安全应急响应中心**

专业的信息安全团队，给你最安全的保障。定期推送漏洞预警、技术分享文章和网络安全知识，让各位了解学习安全知识，普及安全知识、提高安全意识。

![图片](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQHDte6ZzXiclrYUTCQHiak0k38kaD0O6NSfpyrRicr2rspyQicXCp6I4iagSbNbaKt2IiboYfRyUpnDZrtQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7oAq9B6tbfCpcDvtYfWPlG03Hr87Tsf9j4zaRb1j2ibulJYCgoqtKEXQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7oibuePlakD9icaH2ozR4wiasyhcQbNky6opUjDMxibXZBTFysBibU90NXnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gMiabmiaticAtSia0prnfkWIj7vlIkbFPGibN2sUrBbqFSpgHDHhz9s0ic6smsEy0Dae8bnOUPibYNuuj4gwOyqjiac9ow/640?wx_fmt=jpeg&from=appmsg)

**扫码关注**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7mPyXcR4CK7icjm5Clrknfjk8FtgROsooicPv4Fn0j86Y1JSd4HpZCpBg/640?wx_fmt=png&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ74J64EPqEoKhW1SL84NWmdpWnqiafIGB7QfXbI66RRMfg4yxrsyXxM4w/640?wx_fmt=png&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7Zp2MmPiaPx4KBhq65h82Eu6Qra2YJdiawRaHZflNZMxo6hfU7VLjlfzw/640?wx_fmt=png&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7fiarX4RzpFNDFpoEbQuuADrspNGrBrupPjTX4iasHwzuetrWRJZzAuzA/640?wx_fmt=png&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtQNic2Y9ibWKk80qFIHFdG7FjqbiajSPgxjqbTRFvXArqibRHTqKwnW5MFTdpMlh3kVuz7V7452xJ6Z8g/0?wx_fmt=png)

易云安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtQNic2Y9ibWKk80qFIHFdG7FjqbiajSPgxjqbTRFvXArqibRHTqKwnW5MFTdpMlh3kVuz7V7452xJ6Z8g/0?wx_fmt=png)

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