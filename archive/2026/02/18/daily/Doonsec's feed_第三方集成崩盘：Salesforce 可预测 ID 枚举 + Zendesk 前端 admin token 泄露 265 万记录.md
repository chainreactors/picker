---
title: 第三方集成崩盘：Salesforce 可预测 ID 枚举 + Zendesk 前端 admin token 泄露 265 万记录
url: https://mp.weixin.qq.com/s/V8vJ_7IwPqJasFk3DdSDFg
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:16:32.173505
---

# 第三方集成崩盘：Salesforce 可预测 ID 枚举 + Zendesk 前端 admin token 泄露 265 万记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jow1el0IZibxqUicwxduiaZlc78SzEr8F7IFKiaMFFr9wnoFaRN1LpySlnd8sxjHN9BWFJhwJTwDgU4kJfkUJN3hnITBzL8XheJRUtB3UqE1v0Y/0?wx_fmt=jpeg)

# 第三方集成崩盘：Salesforce 可预测 ID 枚举 + Zendesk 前端 admin token 泄露 265 万记录

原创

Pwn1
Pwn1

漏洞集萃

![]()

在小说阅读器中沉浸阅读

> **免责声明**
> 本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。

来源:

https://www.catchify.sa/post/leaking-2m-records-third-party-misconfiguration

在 Catchify，我们非常重视 **Salesforce** 和 **Zendesk** 等第三方平台，它们用于客户关系管理 (**CRM**)、支持和运营工作流程。

虽然这些服务默认是安全的，但**集成层配置错误**可能会完全绕过这些保护措施。以下案例展示了即使没有利用核心应用程序本身，不当暴露第三方 **API** 也会导致：

* 个人身份信息 (**PII**) 直接泄露
* 完全的管理权限丧失

我们发现了两个案例：

1. 一个发生在 **Salesforce** 系统中，使我们能够窥探 **PII** 和敏感文档
2. 另一个使我们能够获取 **Zendesk** 超级管理员的密钥令牌，从而访问 **WhatsApp**、**X** 和电子邮件渠道

这些配置错误并未被开发团队察觉，但却影响了整个基础架构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibwVS2t2ZGXvcmfaLkmib7WzdqhFIzUfKB9IZ7xqZYUomvKYDWicNkNOenn9a8iap0dicic2yLDTgbhZzzhibMgbn4aTQQzvqsZCJkgLQ/640?wx_fmt=png&from=appmsg)

## Salesforce 事件

### 调查起点

我们遵循最直接的路径：

由于 **Salesforce Aura** 端点通常位于 `<root>/aura`，第一步是直接在根域上测试端点。

我们向 `<root>/aura` 发送了一个标准的 **POST** 请求，并附上了精心构造的 **Aura** 消息负载。

不出所料，**Salesforce** 返回了 **403 Forbidden** 错误，表明对根 **Aura** 端点的直接访问受到限制。

```
POST /aura HTTP/1.1
→ 403 Forbidden
```

此时端点似乎已得到妥善保护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibxglCwr6p7hkD2vy5kAUeFtnJ8RvK5lLCoQaoiaCOA2CRobFCh9r3WztZrKb07PvDuC7K9lF8iaFMq7OrkwacOOrwlFHeN7A92Xk/640?wx_fmt=png&from=appmsg)

### 模糊 Aura 路径

我们将注意力转移到 **Salesforce 社区站点** 的结构上。

社区部署通常会将 **Aura** 端点暴露在应用程序特定的路径下，而不是根级别。

我们没有直接针对目标进行测试，而是先对 **Aura** 端点之前的 **URL** 结构进行模糊测试：

```
/FUZZ/aura
```

思路很简单：如果允许社区前端从内部访问 **Aura**，那么 **Salesforce** 预期这些请求必须来自一个有效的路径。

**结果**：我们发现了可访问的路径

```
POST /client/aura HTTP/1.1
→ 200 OK (成功)
```

### 打造 Aura 有效载荷

确定路径后，我们重新发送相同的 **POST** 请求，这次包含 **Salesforce Aura** 用于定义后端操作的参数（`message`）。

该参数的值是 **URL** 编码的 **JSON**。解码后结构如下：

```
{
  "actions": [
    {
      "id": "123;a",
      "descriptor": "serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems",
      "callingDescriptor": "UNKNOWN",
      "params": {
        "entityNameOrId": "user",
        "layoutType": "FULL",
        "pageSize": 100,
        "currentPage": 0,
        "useTimeout": false,
        "getCount": false,
        "enableRowActions": false
      }
    }
]
}
```

关键点在于：

* `descriptor` 指向 `SelectableListDataProviderController.getItems`
* 最敏感的参数：`"entityNameOrId": "user"`

未经身份验证的请求竟然能查询内部 **user** 对象，泄露了员工 **PII** 数据。

![](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibwd2bKApa5YATpj7YJraSVQrAaWF0UM8En9QT5VI0icoBVjd1b9liah8Gc7mL3eEYib2MAAvgEwL2HobUiaJvHVkW6WPd9FEE6nCaY/640?wx_fmt=png&from=appmsg)

### 通过可预测 ID 进行文档枚举

我们进一步发现可公开访问的文档下载 **URL** 模式：

```
GET /sfc/servlet.shepherd/document/download/{DocumentId}
```

这些端点**不需要身份验证**，仅依赖 **DocumentId** 的有效性。

**Salesforce ID** 遵循 **Base62** 顺序结构，具有很强的可预测性：

```
069GH0000001APmAA
069GH0000001APnAA
069GH0000001APoAA
...
069GH0000001APzAA
069GH0000001AQ0AA
069GH0000001AQ1AA
...
069GH0000001AQ9AA
069GH0000001AQAAA
069GH0000001AQBAA
```

通过递增/递减，我们获得了数千份敏感文件（护照、银行文件等）。

### Salesforce 事件关键要点

真正危险的并非单一端点被破坏，而是多个看似合理的假设累积：

* 一个“受保护”的 **Aura** 端点实际未受保护
* 内部标识符意外泄露
* **Salesforce** 可预测的 **ID** 结构让枚举变得 trivial

无需破坏身份验证或触及核心应用，仅一个泄露的 **ID** 即可导致数千份文档泄露。

## Zendesk 事件

### 发现暴露的token

在浏览某个子域名时，我们注意到与嵌入式聊天机器人关联的支持工作流程。

![](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibyNxMlh0PnMPIHXwRPNK01GI7w0HIDpNIrp4xU5FxHhwiclibnaxIicHeogEHnJg1VZ2DrSbibzWMJGCHliaFrNWsbZOsUwYPqzurAU/640?wx_fmt=png&from=appmsg)

通过追踪前端交互，我们识别出底层 **Zendesk** 实例。

登录 **Zendesk** 应用后，发现自定义嵌入式下拉列表：

点击下拉列表 → 立即发出带有**授权令牌**的请求！

```
GET /api/v2/...  (带有 Authorization: Bearer <leaked_token>)
```

令牌直接暴露在浏览器网络请求中。

### 验证管理员访问权限

使用 **Burp Suite** 重放该令牌：

```
GET /api/v2/ticket_fields HTTP/1.1
Authorization: Bearer <leaked_token>
→ 200 OK
```

再请求关键端点验证：

```
GET /api/v2/users.json?page=1 HTTP/1.1
Authorization: Basic <leaked_token>
→ 200 OK
```

### 影响

* 检索到 **2,650,000** 条用户记录
* 包含 **姓名、电子邮件、电话号码、角色** 等 **PII**
* 泄露文件包括护照、政府证件、许可证等
* 完全接管支持渠道：**Zendesk**、**电子邮件**、**WhatsApp**、**X**

### 为什么会发生

**Zendesk** 组件直接嵌入客户端应用，并以**提升权限**运行。

前端**直接调用**特权 **API**，且令牌暴露给浏览器，而没有后端中转。

## 结论

这两个案例都是**人为配置错误**造成的，并非 **Salesforce** 或 **Zendesk** 本身的故障。

它们完全按照配置预期运行。

真正的问题在于：**集成点**上的细微配置决策，在没有强制校验的情况下被公开和信任。

在 Catchify，我们认为：

现代安全漏洞很少由技术缺陷造成，而往往源于**集成点**的细微配置失误。

我们的工作重点是尽早发现这些问题，防患于未然。

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[注册功能漏洞检查清单](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484879&idx=1&sn=16cbb0a02931f172a8b7aea7877debe0&scene=21#wechat_redirect)

[一种利用 HTTP 重定向循环的新型 SSRF 技术](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484872&idx=1&sn=085b9ed569eefc9a96122fd164da9707&scene=21#wechat_redirect)

[API 渗透实战：从 JSON 响应倒推隐藏的高危路由](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484828&idx=1&sn=376a99fecd6210283cc43c2a79633b26&scene=21#wechat_redirect)

[使用 Frida 在运行时拦截 OkHttp - 实用指南](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484910&idx=1&sn=9c0e1ee6b39d754de6da5b30355a4ca0&scene=21#wechat_redirect)

[一种利用 HTTP 重定向循环的新型 SSRF 技术](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484872&idx=1&sn=085b9ed569eefc9a96122fd164da9707&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

漏洞集萃

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