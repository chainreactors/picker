---
title: TOCTOU 与信任链断裂:DNS Rebinding
url: https://mp.weixin.qq.com/s/hWV18NkjGn4-hgXI2rXazw
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:31:07.422294
---

# TOCTOU 与信任链断裂:DNS Rebinding

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y5LD4fX7WOJFeH3yNiceUhcRicfqgic0xRNj8A2NveInGWVaqcENs4yCwB0kWM7WibeLt3kPe24PLT4g3AwUkGKa8A/0?wx_fmt=jpeg)

# TOCTOU 与信任链断裂:DNS Rebinding

原创

Pwn1
Pwn1

漏洞集萃

![]()

在小说阅读器中沉浸阅读

> **免责声明**
> 本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。

介绍一个很早之前就出现了的 Tips，最近在项目上遇到了，于是简单整理一下，分享给各位大佬。

**DNS Rebinding** 攻击的本质是利用 **TOCTOU (Time of Check, Time of Use)**。

它主要是利用了应用在 **“检查”** 与 **“连接”** 两个步骤之间存在的微小时间差，并且配合 DNS 协议中的 `TTL (Time To Live)` 机制，欺骗服务器。

这里我们假设已经发现了 **SSRF 漏洞** 并且目标存在 **WAF**，不限制访问内网，于是尝试突破。

## 正常流程

在没有攻击的情况下，服务端防御 SSRF 的逻辑通常如下：

1. **解析**：目标接收用户提供的 URL (如 `http://example.com`)，进行 DNS 解析，获取 IP `1.2.3.4`。
2. **验证**：目标判断 `1.2.3.4` 是否属于内网黑名单 (如 `127.0.0.1`, `192.168.x.x`)。如果是外网 IP，则放行。
3. **连接**：目标使用 HTTP 客户端向 `example.com` 发起请求。

## DNS Rebinding 的攻击逻辑

攻击者通过控制 DNS 服务器，打破了我们上述流程的信任假设：

1. **设置陷阱**：攻击者配置恶意一个 DNS 服务器，然后使得域名 `exp.attacker.com` 拥有两个 A 记录：一个合法的公网 IP (`IP_A`) 和另外的一个目标内网 IP (`IP_B`)。
   > **关键在于设置 TTL 为 0 秒（注意⚠️）**。
2. **第一次解析**：目标服务器为了验证安全性，查询 `exp.attacker.com`。攻击者的 DNS 返回公网 `IP_A`。防火墙检查通过。
3. **缓存失效**：由于 `TTL=0`，操作系统或应用层的 DNS 缓存立即失效。
4. **第二次解析**：目标服务器准备发起 HTTP 连接。由于缓存失效，它被迫再次发起 DNS 查询。这次，攻击者的 DNS 返回内网 `IP_B`。
5. **建立连接**：目标服务器误以为还是在访问合法的域名，实际上已经建立起了通往内部网络 (如 `127.0.0.1`) 的 TCP 连接。

这种手法在处理一些限制内网访问的场景下是有奇效的。

---

### 局限性

但是，这种手法也很有限制。

它主要是针对于 **"Resolve-Check-Connect"** 模式。比如很多开发语言的标准库 or 一些第三方组件（比如 Python 的 `requests` 结合自定义检查逻辑、以及 PHP 的 `curl`）在实现的时候，如果逻辑上把 **“检查 IP”** 和 **“发起请求”** 分成了两步来操作，并且没有固定第一次解析的 IP，那么就会导致漏洞的存在。

**但是**

如果是类似于 **Java JVM** 这种默认安全策略 (`networkaddress.cache.ttl`) 通常被设置为 `-1` (**永久缓存**) 的话。这就意味着只要第一次解析成功了，那么 JVM 就会一直使用那个公网 IP，不会再次查询 DNS，导致重绑定失败。

除非管理员手动修改配置或代码显式禁用了缓存。

## 一些工具

### 1. rbndr.us

rbndr.us 是一个广泛使用的公共 DNS 重绑定服务，它不需要攻击者自建 DNS，只需构造特定格式的域名。

* **IP 编码**：该服务要求将 IP 地址转换为 16 进制格式，以避免直接在 URL 中暴露敏感 IP 特征。

+ 公网 IP (用于绕过): `1.2.3.4` -> Hex: `01020304`
+ 内网 IP (用于攻击): `127.0.0.1` -> Hex: `7f000001`

* **域名构造**：格式为 `<IP_A_Hex>.<IP_B_Hex>.rbndr.us`。

+ **Payload**:

  ```
  http://7f000001.01020304.rbndr.us
  ```

* **解析逻辑**：该域名的 DNS 服务器被配置为随机或轮询返回这两个 IP，且 `TTL` 极短。

### 2. 其他类似工具

也可以直接搜索下，如：

```
https://lock.cmpxchg8b.com/rebinder.html
```

![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOJFeH3yNiceUhcRicfqgic0xRN5lOSkGP0yNU6rDlRPSGa9ibxBfvgwdNkkCAHQlE20ceEnxncibLUaKuQ/640?wx_fmt=png&from=appmsg)

## 参考

```
https://gitlab.com/gitlab-org/gitlab/-/issues/353018
https://www.freebuf.com/articles/network/355788.html
https://lock.cmpxchg8b.com/rebinder.html
https://infosecwriteups.com/the-12-500-dns-trick-that-hacked-snapchats-cloud-servers-0cb299ec1d37
https://project-zero.issues.chromium.org/issues/42450491
```

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[攻防演练中的“降维打击”：逃逸出内网边界的影子资产与SaaS供应链挖掘](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484699&idx=1&sn=9455a5c988e2a477fec61e266b526aac&scene=21#wechat_redirect)

[【深度复盘】Trust Wallet 惊魂24小时：当官方插件变成“内鬼”，一行代码如何盗走600万美元？](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484821&idx=1&sn=536c93469a243550135bc70144e4c973&scene=21#wechat_redirect)

[【漏洞挖掘Tips】一种新的 GraphQL 绕过角度](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484785&idx=1&sn=82c963c67a9089d124addd85890c4c34&scene=21#wechat_redirect)

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