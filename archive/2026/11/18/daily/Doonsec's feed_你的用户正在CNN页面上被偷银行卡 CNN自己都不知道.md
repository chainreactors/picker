---
title: 你的用户正在CNN页面上被偷银行卡 CNN自己都不知道
url: https://mp.weixin.qq.com/s/EhwmBGeUjxp5l9_NOpwjwg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:38:33.749980
---

# 你的用户正在CNN页面上被偷银行卡 CNN自己都不知道

# 你的用户正在CNN页面上被偷银行卡 CNN自己都不知道

原创

紫禁
紫禁

紫禁玄科

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

SECURITY ? INTELLIGENCE

# 你的用户正在 CNN 的页面上被偷银行卡

2026年11月17日 ? 8 min ? #供应链安全 #WebSkimming #反诈

昨天（2026年11月16日 UTC），如果你是周一用 iPhone 打开过 CNN、BBC 或 Zoom 官网的用户，你看到的每一个页面里，都藏着一段不属于这些网站的代码。它在你输入卡号的那一刻抄走卡号和 CVV，在你复制加密货币地址的时候把地址换成攻击者的，如果你的手机系统够旧，它还试图直接接管设备。

而这些网站的主站没有中毒，服务器没有被攻破。恶意代码是从一个几乎每个营销团队都在用的服务里，光明正大、带着合法证书加载进来的。

这个服务叫 Optimizely。这次事件在研究圈已经被叫做 OPTIMJACK。我把 Report URI、Cynet、StepSecurity 三家的一手分析翻了个底朝天，这篇文章讲清楚三件事：**它是怎么发生的；如果你运营一个用了第三方脚本的网站，今天该做哪五件事；如果你是普通用户，周一访问过这些网站意味着什么。**

## 一、一个"做 A/B 测试"的服务，为什么能投毒半个互联网

先给不了解的读者补一句背景：Optimizely 是做网页实验的——同一个页面，一半访客看到红色按钮，另一半看到蓝色，统计谁点得多。全球大量网站靠它跑这种实验。

它的接入方式是一段叫 snippet 的脚本，从 `cdn.optimizely.com` 加载。关键在snippet 里有个字段叫 **Project JavaScript**：允许客户往里塞自定义代码，而且**每次 snippet 更新时这段代码都会原样执行**。

攻击者利用了 Web Experimentation 的一个漏洞，拿到了对大量互不相关的客户项目的写入权限，然后在这些项目的 Project JavaScript 字段里写入了一个加载器。Report URI 的技术分析说得很明白：**snippet 本体一个字没动，照样由官方 CDN 用官方证书分发**——所以任何依赖"域名白名单"的防御全部失效，包括 CSP 里写了 `script-src cdn.optimizely.com` 的站点：代码就是从这个"合法"主机长出来的。

加载器有三种变体轮换投放：

* 直接版：明文加载 `1688360[.]cc/track.js`
* 隐蔽版：把域名藏在 base64 字符串里，纯文本搜域名搜不到
* 冗余版：payload 全文内嵌，外网封了 C2 域名也照样发作

这就是供应链攻击最阴的地方：你的 CDN 是干净的，你的证书是对的，你的安全设备看到的是可信域名——而 payload 就住在业务功能字段里。

![图2 ? 投毒链路：合法 CDN，功能字段藏毒](https://mmbiz.qpic.cn/sz_mmbiz_png/Ah5NAr7MJFjrdwAra58CicBziajY2yBGVsUqPvr9yfgfOFmGL8AkIdPAU9Dkk4260K3lcic6bqghrPJ4M8GnCRKU8yI4FUpvQiaFR4xGic8fkQY0/640?from=appmsg)

▲ 图2 ? 投毒链路：合法 CDN，功能字段藏毒

## 二、时间线：从 BBC 第一条注入到全网红清，不到 24 小时

以下时间均为北京时间（原始报告为 UTC）：

| 时间 | 发生了什么 |
| --- | --- |
| 11-16 12:21 | 首次注入出现在 BBC 的 snippet，加载器来自 webshell[.]lol |
| 11-17 上午 | 扩散至 CNN、Zoom、Salesforce、GitLab、IKEA、HSBC、Equifax、Ledger 等，连 Optimizely 自己的主站和登录页也带毒 |
| 11-17 21:43 | 卡信息窃取模块上线：拦截表单提交的卡号、有效期、CVV，发往 /card.php |
| 11-17 凌晨 | Optimizely 发布事故通告：漏洞已修复、恶意代码已移除。但通告没说漏洞原理、改了多少项目、攻击者是否还有访问权 |
| 清理开始后 | Smartsheet 的脚本被清理干净后**再次感染**——说明此刻攻击者仍持有写入权限 |
| 11-17 03:13–03:57 | 对 iOS ≤18.6 的访客强行加载 Coruna 漏洞利用 iframe，页面每 60 秒自动重载重试 |
| 11-17 05:52 | 大规模清理完成，仅剩 TalkTalk 一家还挂着毒 |

Report URI 检查了 1,611 个 Optimizely snippet，在 188 个里发现了恶意代码，分属 **178 家机构**——并强调真实数字更高，因为它只能检查来得及抓到的那部分。

## 三、payload 干的三件坏事，每件都很专业

**第一件：偷换加密货币地址。** track.js 不是无差别替换地址——按 StepSecurity 的分析，它只替换"通过对应链校验和验证、且出现在 wallet/deposit/send 等支付关键词附近"的地址。你在页面上选中地址按 Ctrl+C 的那一刻，剪贴板里已经是攻击者的了。截至 11-17 凌晨，攻击者钱包九小时内收到约 $7,040。已有受害者，只是链上数据无法区分哪些转账本应属于他们。

**第二件：抄银行卡。** 11-17 追加的模块直接从站点表单字段截获卡号、有效期、CVV。有个重要的技术边界值得所有网站方知道：**它读不到跨域 iframe 里的卡号**——Stripe Elements、Adyen 托管字段这类隔离在独立 origin 的支付组件，浏览器同源策略挡住了它。这等于给了"结账页禁用第三方 tag"一个教科书级的论据（第五节展开）。

**第三件：打 iPhone。** 命中 iOS 设备时加载 boot.js，按版本分发两套公开文档化的漏洞利用套件：Coruna（iOS 13.0–17.2.1）、DarkSword（iOS 18.4–18.7），iOS 26 有一条目前只做设备信息采集的链路。Cynet 用模拟 iPhone 环境复现了投递，明确定性："条件化投递，不等于真机已被控破。"Optimizely 自己也报告没有 iPhone 实际沦陷。Kit 注释显示 iOS 18.7.3+ 与 26.3+ 已封堵。

另外它在完成地址替换后，还会回传访客 cookie 和整页截图（HttpOnly cookie 拿不到，跨域限制还在）。

![图1 ? OPTIMJACK 攻击时间线（北京时间）](https://mmbiz.qpic.cn/mmbiz_png/Ah5NAr7MJFjTgRKoicGhqyYz0VKYfzIllXgtpwOLVjAxwoPbIRRib5ic27xlHdfJyBdibPibWwhIMoGYG7Lkbej6wGmoRL6hhFqmKTDDmLibfQq68/640?from=appmsg)

▲ 图1 ? OPTIMJACK 攻击时间线（北京时间）

## 四、我做了两个脚本，一个查自己、一个留证据

光看别人报告不算实测。我写了两个 Python 脚本，第一个可以自查**任意站点当前**加载的第三方脚本是否含本次 IOC（注意：查不出"周一曾带毒"的历史状态，那是另一回事，见文末取证建议）：

```
#!/usr/bin/env python3 """check_thirdparty.py — 抓取页面全部外部脚本并扫描本次 OPTIMJACK 的 IOC 用法: python3 check_thirdparty.py https://example.com """ import re, sys, urllib.request from html.parser import HTMLParser  IOC = ["1688360", "track.js", "card.php", "hit.php", ".icu/",        "webshell.lol", "atob(", "coruna", "darksword"]  class SrcGrab(HTMLParser):     def __init__(self):         super().__init__(); self.srcs = []     def handle_starttag(self, tag, attrs):         if tag == "script":             d = dict(attrs)             if d.get("src"): self.srcs.append(d["src"])  def fetch(url):     req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})     return urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "ignore")  page = fetch(sys.argv[1]) grabber = SrcGrab(); grabber.feed(page) print(f"[+] {len(grabber.srcs)} 个外部脚本源") hits = 0 for s in grabber.srcs:     url = urllib.parse.urljoin(sys.argv[1], s)     try:         body = fetch(url)     except Exception as e:         print(f"[!] 拉取失败 {url}: {e}"); continue     found = [k for k in IOC if k.lower() in body.lower()]     status = "命中 " + ",".join(found) if found else "干净"     hits += bool(found)     print(f"[{'X' if found else 'O'}] {url[:70]} -> {status}") print(f"[=] 结论: {'存在可疑脚本' if hits else '当前未见已知IOC（不代表历史清白）'}")
```

第二个更简单但更重要——**留证据**。payload 当天改了多次，单个文件哈希抓不住所有版本，所以要在清理完成前持续快照：

```
#!/usr/bin/env bash # snapshot_snippets.sh — 每小时存档一次本站 snippet 原文与元数据 mkdir -p snap && ts=$(date +%Y%m%d-%H%M%S) curl -s "https://cdn.optimizely.com/js/你的PROJECTID.js" \   -D "snap/${ts}.headers" -o "snap/${ts}.js" sha256sum "snap/${ts}.js" >> snap/manifest.txt
```

（示例中 C2 域名已做防误触处理，`[.]` 需自行还原后才能访问。）

## 五、如果你运营网站：今天做完这五件事

综合 Report URI、StepSecurity、Cynet 三份建议，按优先级排：

1. **翻出所有项目的 Project JavaScript 和实验自定义代码**

   ，搜 `1688360`、`atob(`，以及任何不是你写的代码。base64 变体专门防文本搜索，所以 `atob(` 必须查。
2. **轮换所有能写入账号的凭据**

   ：成员、API token、集成。Smartsheet 清完再中毒说明攻击者一度仍有写入通道。同时向 Optimizely 索要：你的哪些 project ID 被改过、何时改的、怎么改的。
3. **日志回溯到 11-16 20:00 UTC**

   （即首次注入之前），检索对这些 IOC 的访问记录。Cynet 特意提醒：不要把 `cdn.optimizely.com` 本身当恶意指标去封——它是被寄生的合法宿主，封它等于自断业务。
4. **收紧 CSP**

   ：严格的 `script-src` + `connect-src`。但注意两个坑——放行 cdn.optimizely.com 没用（代码就来自那里）；`strict-dynamic` 和 `unsafe-eval` 会让本次 payload 在某些站点照样跑起来。
5. **结构性整改**

   ：checkout 页去掉一切第三方 tag，卡号采集只走支付服务商的跨域 iframe 托管字段。第三节已经证明了原因：这次唯一没被抄走卡号的，恰恰是躲在同源策略后面的那部分。

如果确认曾带毒：评估通知你的用户。若站内表单直采卡号，周一提交的卡应视为可能泄露；非 HttpOnly 的会话令牌同理，轮换。

![图3 ? 网站运营方今日五查](https://mmbiz.qpic.cn/sz_mmbiz_png/Ah5NAr7MJFjdhjTeuC4r9afS5JXjYNOgQPx4YSibiap2Hcib2JOAZNv5eEI1ypdfN6d81QwgPaSnNwprP5YRY3IopABmfW2UcRSxq5ghcK4kpc/640?from=appmsg)

▲ 图3 ? 网站运营方今日五查

## 六、如果你是普通用户

周一访问过上述 178 家站点（完整名单在 Report URI 原文，含 CNN、BBC、Zoom、Salesforce、IKEA、HSBC、Equifax、Air France-KLM、Ledger、Peacock……）的话：

* **iPhone/iPad 立刻升到 iOS 18.7.3+/26.3+**

  。升级前，如果页面每分钟自己刷新一次，那就是 Coruna iframe 在工作，关掉浏览器别再访问。
* **核对周一付过的每一笔链上转账**

  ：到账地址和你当时想付的是否一致。硬件钱包签名时以设备屏显为准，不要信复制来的文本。
* **盯一周账单**

  。用这些网站表单输过卡号的，考虑让发卡行换卡重发。
* 不用恐慌的部分：cookie 有 HttpOnly 标记的没被拿走；iOS 无实际沦陷报告；Optimizely 已修复。

## 七、这事真正该记住的一条

OPTIMJACK 不是"某大厂被黑了"，而是**信任模型被绕穿**：CDN 域名可信、证书有效、代码躺在一个"本来就该放自定义代码"的功能字段里。我们过去十年教用户的防御——看域名、看小锁图标——在这类攻击面前全部失灵。

判断标准要换一层：**这个页面能不能读到我的输入，取决于代码从哪个 origin 来，而不是它挂在谁的域名下。** 对网站方，这句话的落地就是第 5 条；对用户，这句话的落地就是敏感输入尽量走支付网关的独立 iframe——那些弹窗式、跳转到 pay.xxx.com 的流程，反而是这次风暴里最安全的。

---

\*信源（均为一手报告，检索日期 2026-11-17）：Optimizely 官方事故通告（01:02 UTC）；Report URI《Hijacked Optimizely snippets serve card skimmer to CNN, BBC and Zoom visitors》及 178 家受害机构清单；Cynet Research 端点调查与 iOS 二段载荷模拟复现；StepSecurity payload 技术分析。本文数据细节以上述报告为准。\*

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ah5NAr7MJFgsJVJaWtQWT91yiaiamRUadMsnMic0LbgkAdUkYst4Ziaz6lclmn95ickibdZxnp72aTaJuXKjZvMYmeobnPyQpN7LeuZhOHpKqXOV0/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过