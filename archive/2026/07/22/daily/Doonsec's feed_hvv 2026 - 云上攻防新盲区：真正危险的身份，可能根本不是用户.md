---
title: hvv 2026 - 云上攻防新盲区：真正危险的身份，可能根本不是用户
url: https://mp.weixin.qq.com/s/7guWyWyY04FZ1RkPnpSYrQ
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:09:48.992647
---

# hvv 2026 - 云上攻防新盲区：真正危险的身份，可能根本不是用户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMAnkUwqIxkL7TQ7Kq31liborD7g0Bx9aV7a6UibXAaicONGhfVTgxjib1Zqj73zZzpib31K8V9iaMbkAQ0iap8fkDBOQH1Fvulo5qp25I/0?wx_fmt=jpeg)

# hvv 2026 - 云上攻防新盲区：真正危险的身份，可能根本不是用户

天黑说嘿话

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于MessFreeSecurity
，作者MessFeel

![](https://wx.qlogo.cn/mmhead/VNMic85jx3X5dte5sgSqnGasCCFV3OXmqyy7yLfibj8bsjFmqwTxibmHhEHxI9jhMW1muwyfFicibvHU/0)

**MessFreeSecurity**
.

提供社区优质咨询服务

如果你在国内做过云上 HVV 值守，下面这些东西大概率已经被盯得很紧：主账号异地登录、RAM/CAM/IAM 子账号提权、AK/SK 泄露、新增访问密钥、陌生 IP 调 OpenAPI。

但 Dirk-jan Mollema 这次挖到的链路，偏偏绕开了这些最熟悉的信号。

目标全局管理员没有登录，MFA 没有弹窗，Conditional Access 没有放过一台陌生设备。攻击者拿的是自己实验租户里的一张服务 Token，却曾经可以跑到另一个 Entra ID 租户里，替那里的任意用户说话。把 `nameid` 换成全局管理员对应的 `netId`，Azure AD Graph 返回的就是管理员权限下的数据。

我第一次翻完这 74 页，印象最深的不是“Impersonating the Global Admin”那张成功截图，而是前一页的报错：

> User not found... but token accepted?

用户没找到，Token 却先被认了。

这句话几乎把整个漏洞说透：微软验了 Token 的签名，也认出了发起方是一项受信服务，但它没有把“这张 Token 从哪个租户来”与“它正准备替哪个租户的用户办事”牢牢锁在一起。

![AREA41 2026 原版演讲稿封面](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMAGGW2VZ7AcQYmFHlX7jpmSmDR4eicwTpUicorRrw8lA0QBMBMKucxphe7xIXNiaHVHTw53FanqCpNSeZl0NXMmQsEicvD876JQWico/640?wx_fmt=jpeg&from=appmsg)

*图 1：AREA41 2026《Hacking Every Entra ID Tenant With Actor Tokens》原版封面。报告共 74 页，本文按研究过程还原，而不是逐页翻译。*

2026 年 6 月，Dirk-jan 在 AREA41 公开了《Hacking Every Entra ID Tenant With Actor Tokens》。研究从 Exchange Hybrid 服务器上的一张证书开始，沿着微软旧式 Service-to-Service 身份链一路往里走，最后碰到 Azure AD Graph 的跨租户校验缺口。微软给它分配了 **CVE-2025-55241**，核心问题已在 2025 年 7 月修复。

这不是一篇“复现一个过期 CVE”的文章。真正值得国内云上团队细看的，是它揭出的那类问题：

**当云服务、云主机、混合组件或第三方平台可以代表账号获得临时身份时，安全边界已经从“谁拿到了密码”移到了“谁被允许替谁办事”。**

阿里云 RAM 角色、腾讯云 CAM 角色、华为云 IAM 委托的协议与微软 Actor Token 各不相同，公开资料也没有显示三家存在 CVE-2025-55241 这一实现缺陷。这里要类比的是信任形状：可信主体、角色或委托、临时凭证、目标资源之间，只要有一处绑定过宽、对象认错或旧接口少验了一个关系，攻击者拿到的就可能不是一台云主机，而是一段跨账号、跨服务的控制面权限。

国内云上演练经常把“账号是否登录”当成起点。这份 PPT 提醒我们，还有另一种起点：

```
服务凭据 / 实例身份 / 第三方委托
              ↓
       申请临时服务身份
              ↓
      代表用户或账号访问资源
```

接下来就沿着作者的原始研究路线，看清 Actor Token 到底是什么、Azure AD Graph 少验了哪层关系，以及这件事换成 RAM、CAM、IAM 的语言后，国内云上攻防该查什么。

---

## 74 页 PPT 其实只追了一个问题：云的安全边界到底画在哪

Dirk-jan 的研究不是从 Actor Token 开始，而是从 Entra Connect 和 Exchange Hybrid 这些“本地系统替云端做事”的组件开始。

传统认知里，本地 AD 与 Entra ID 中间有一道清晰边界：本地管理员权限很高，但云端租户仍有独立身份、独立策略和独立密钥。早期 Entra Connect 的高权限同步账号让这道边界变得很薄；微软持续收紧同步账号权限后，研究似乎走到了尽头。

![本地 AD 与 Entra ID 的安全边界假设](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8qOq10zFicMAS0hS6oY9QeZQGmdCGxXvrZNWBAVjMp7uCPGNa6QArBmT1ibjTMwBk90DH5hYAyxJUrZnZ74d59zSOg4q7ibsc4Kpk3HqIL57IQ/640?wx_fmt=jpeg&from=appmsg)

*图 2：PPT 第 6 页的原始假设——本地 Active Directory 与云端 Entra ID 之间应存在一条可验证的安全边界。后续研究不断追问：哪些混合组件仍横跨这条线？*

于是研究视角换了一个方向：除了同步服务，还有什么本地组件会以微软云服务的身份说话？

答案是 Exchange Hybrid。

整份 PPT 大致可以压缩成五段：

| 页码 | 研究阶段 | 真正要回答的问题 |
| --- | --- | --- |
| 4—18 | Entra Connect 旧权限回顾 | 本地同步身份是否仍能改写云端关键策略 |
| 19—28 | Exchange Hybrid 与共享服务主体 | 本地 Exchange 证书能代表哪个云端服务 |
| 29—43 | ACS、Actor Token 与 S2S 委派 | 微软后端如何替用户访问另一个服务 |
| 44—71 | Azure AD Graph 跨租户校验 | 为什么租户 A 的服务 Token 会被租户 B 接受 |
| 72—74 | 披露、修复与后续收口 | 微软最终在哪几层切断了这条链路 |

作者先从一台混合 Exchange 服务器上的证书入手。在旧式混合配置中，本地 Exchange 会持有与 Exchange Online 服务主体相关的证书凭据，用于 OAuth 与“丰富共存”场景。

![导出 Exchange Hybrid 证书的研究截图](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMA7BSHqeibQ5zPntJNWWiaUCpZHUsFxL0a0XsfyiaP4QEcCMZpEY2QyibuElECFoEUYzqg8Z1jpic4Ft3OAwtZamdzicdODBnghwwnVI/640?wx_fmt=jpeg&from=appmsg)

*图 3：PPT 展示的 Exchange Hybrid 证书导出界面。它是研究的起点：本地私钥一旦代表云端一方服务，边界就不再只是“本地账号同步到云”。*

这张图的重点不是“证书可以导出”，而是证书背后的身份语义：

> 一台本地 Exchange 服务器保存的私钥，曾经可以让持有者向云端证明“我是 Exchange Online 这个微软一方应用”。

从红队视角看，这是典型的控制面升级。拿到服务器权限只是主机失陷；拿到能代表一方服务的凭据，触碰的却是云身份信任。

![从 OAuth 入口追到服务凭据的思考链](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMBb40BMWhfJML4bqGxKiaT5h88uPFIZvsvUgFWnF64LZQTWwFBlAZjHbqwpeL6zQgXsFZrUoqdO6fUIMgL0ozNMtACY7EPHfdbg/640?wx_fmt=jpeg&from=appmsg)

*图 4：作者的研究推导：共享 Exchange Online 服务主体存在本地重定向地址，本地 Exchange 可执行 OAuth，完成应用身份认证需要证书或密钥，因此继续追踪这些凭据还能用于哪些客户端凭据流程。*

不过，把这段历史直接总结成“攻破一台 Exchange，就能拿下所有租户”仍然失真。

作者后来明确说明：跨租户漏洞验证时，Actor Token 来自他自己的实验租户；在实验环境中，他也可以直接给 Exchange Online 服务主体添加凭据，并不依赖完整的混合 Exchange 部署。Exchange Hybrid 是他找到协议的入口，**不是 CVE-2025-55241 横跨任意目标租户的必要前置条件**。

这一区分很关键：

* **Exchange Hybrid 风险**

  解释了攻击者怎样接触一方应用凭据和 Actor Token 机制；
* **Azure AD Graph 租户校验缺口**

  解释了为什么攻击者自有租户生成的 Token 会穿透到另一个租户。

两段接起来，才是完整故事。

---

## Actor Token 不是用户门票，而是“微软服务替用户办事”的委托书

正常用户访问云服务时，Token 里会写清楚谁登录、面向哪个资源、由哪个租户签发、拥有哪些权限。资源端再校验签名、受众、签发者、租户和主体。

Actor Token 处理的是另一类场景：Exchange Online 需要代表某个用户去访问 SharePoint、Azure AD Graph 或其他微软后端服务。用户本人不一定再次参与认证，于是后端服务需要一套 Service-to-Service，简称 S2S 的委派机制。

PPT 第 29 页把签发方指向旧式 Access Control Service，也就是 ACS。

![ACS 签发 Actor Token 的服务间通信流程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8qOq10zFicMBaFckRd3xpo8wkrfSNcTibft6wGev0ZopQfbkt5MiaVYPKmicKO30yN9dmwgGia7BTtrBhJicpT4wOHpZwC9KxhiadA14YHjW0nUR2s/640?wx_fmt=jpeg&from=appmsg)

*图 5：本地 Exchange 向 ACS 请求 Actor Token，云端服务再把 Actor Token 与一个用户模拟身份组合起来访问其他资源。*

这套机制里实际叠了两层 JWT。

外层是 **Actor Token**：

* 由 Entra ID/ACS 使用 RS256 签名；
* `aud`

  指向要访问的微软资源，例如 Azure AD Graph；
* `iss`

  和 `aud` 中都能看到签发租户信息；
* 有效期精确到 24 小时；
* `trustedfordelegation=true`

  表示持有它的一方服务可以代表用户行动。

![解码后的 Actor Token](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8qOq10zFicMCqx1uoibhQx8Kv3nCw09X1ynDIIYoTvLIqCVvHGHs43ezASjjJY9zJuenTxc4h5kRpYEgTKmWHsTuicLQbD4iaC85fuyoKkykw5E/640?wx_fmt=jpeg&from=appmsg)

*图 6：PPT 中的 Actor Token。红框标出了 Azure AD Graph 受众、签发租户以及 `trustedfordelegation=true`。外层 Token 本身带有微软签名。*

内层是 **Impersonation Token**，也就是模拟身份 Token：

* JWT 头部是 `alg: none`；
* 内部嵌入已经签名的 Actor Token；
* `nameid`

  指向将被模拟的用户；
* `upn`

  、`smtp`、`sip` 等字段由发起服务在本地填写；
* 这层没有独立签名。

![本地生成的未签名用户模拟 Token](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMCyBHqeORbmxlXFhMDJF7iakKFricpmmGo3UHpKInC5gkJs5OpnYt0PnJ0TtH7vYZo91TcjZkhicufNtvcb6fGich03OJc8N1Y5epY/640?wx_fmt=jpeg&from=appmsg)

*图 7：Exchange Online 使用的未签名 Bearer Token。外层红框是嵌入的 Actor Token，下面的 UPN、SMTP、SIP 与 `nameid` 描述被模拟用户。*

看到 `alg: none`，很多人第一反应是“JWT 未签名漏洞”。这个判断只说对了一半。

设计者的信任模型是：**内层身份描述虽然未签名，但它被一个已经签名、且允许委派的一方服务 Token 包裹。** 资源端信任的不是任意人提交的明文，而是“拥有合法 Actor Token 的微软服务有资格选择它要代表的用户”。

所以问题不只是少了一段签名。真正危险的是下面四件事叠在一起：

```
一方服务拥有广泛委派资格
        +
模拟用户的字段可在本地构造
        +
Token 24 小时内缺少即时撤销能力
        +
资源端没有把来源租户与目标租户牢牢绑定
```

![S2S Actor Token 的关键属性](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8qOq10zFicMClf8ia0W5VjarxHktaTwIZN7M8T2mlTibPCJrJjib1OkDr61G1NFCp41ZMQ5uLN310l3m0iakm7OdkH5Kq2j0LWwFE6PFVicUylRI4/640?wx_fmt=jpeg&from=appmsg)

*图 8：PPT 总结的 S2S Token 属性：24 小时有效、本地生成模拟身份、签发侧缺少有用日志、可代表租户内用户，并绕开普通用户的 Conditional Access 检查。*

在单租户模型里，这已经是一项高权限后端能力；一旦资源端把租户边界验松，影响就会从“这个服务可代表本租户用户”瞬间变成“这个服务可代表别的租户用户”。

---

## 真正致命的不是 Token 权限高，而是 Azure AD Graph 把两本户口簿串错了

2025 年 7 月，作者为了准备 Black Hat 与 DEF CON 演示，开始改动模拟身份 Token 里的不同字段，观察 Azure AD Graph 会拒绝什么。

他先为 Azure AD Graph 申请了 Actor Token。

![面向 Azure AD Graph 的 Actor Token](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMCcb7qUT20jfHCqBuDibekT4y1IbHlcJGfumm5jXH2y3Yuibkw6yq0AEEw2lY29pQNj8m2lTxkdsicFsfAE5iakzrkFLDpPjv5ibJz0/640?wx_fmt=jpeg&from=appmsg)

*图 9：PPT 中面向 `graph.windows.net` 的 Actor Token，受众已经从 Exchange 等资源切换到旧式 Azure AD Graph。*

接着，他没有改动带微软签名的外层 Actor Token，只把未签名模拟身份里的租户 ID 换成另一个测试租户。

![只修改内层模拟身份 Token 的租户 ID](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMADF4lrbibmpHnhoFHfbEjQJqSuyKiaSia9lrPtOqaibMcfuFVdNJzO6SOxQPbkMu1bFw2mJWFENuBOoJ1TtKybg8PZwKibrB5dD9c0/640?wx_fmt=jpeg&from=appmsg)

*图 10：外层签名 Token 仍来自租户 A，内层模拟身份却写成租户 B。按正常租户隔离逻辑，这里应直接因来源与目标不匹配而终止。*

预期结果应该是“租户不匹配”或“Token 无效”。实际返回却是：**用户不存在。**

![跨租户 Token 被接受后的用户不存在报错](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMBkG1dLLvrKBGUWEznxSfUiaSlNxDNjCwBMkw4p8nic3P68HiasiaicCI8dNqnDesCk3ia2j3Zbe9Yn8ZpoJVBWaMbHleCTibQdM0Kb5U/640?wx_fmt=jpeg&from=appmsg)

*图 11：错误信息的危险之处在于，它没有否定 Token，而是在目标租户里查找用户。换句话说，认证层已经接受了来自另一个租户的 Actor Token。*

这条报错几乎把漏洞根因直接写了出来：

```
预期校验：
签名有效
AND Actor Token 的来源租户 == 模拟身份的目标租户
AND 用户属于该租户

实际效果：
签名有效
AND 在“模拟身份指定的租户”里能找到对应 nameid/netId
```

中间最关键的绑定丢了：

```
actor_token.origin_tenant == impersonation_token.target_tenant
```

这不是“完全没验 Token”。Azure AD Graph 验证了微软签名，识别出这是可委派的一方服务，也尝试解析目标用户；它只是没有把**谁获得了这张服务通行证**与**这张通行证正准备进入哪个租户**锁成同一件事。

安全工程里最棘手的漏洞往往正是这种“每个字段都验了...