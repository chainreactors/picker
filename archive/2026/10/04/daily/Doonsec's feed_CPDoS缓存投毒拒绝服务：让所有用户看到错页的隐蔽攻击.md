---
title: CPDoS缓存投毒拒绝服务：让所有用户看到错页的隐蔽攻击
url: https://mp.weixin.qq.com/s/MXiHE9ZkdS1jnhrKQZ4Tzw
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:55:40.866362
---

# CPDoS缓存投毒拒绝服务：让所有用户看到错页的隐蔽攻击

# CPDoS缓存投毒拒绝服务：让所有用户看到错页的隐蔽攻击

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MwicUsEszvbSm2TxbL4qjiczZfMgV3N1zgrJiaxpfEY1bKxfESKQ7M5y6u71nThO1spgzCMp6rfyRx9WnSPQN6dTfSdWsh7huZzQ/640?from=appmsg)
> **导语**：SQLi 能偷数据，XSS 能劫持会话——这两类攻击大家都熟。但 CPDoS 这种"投毒缓存让所有用户看到错页"的攻击，名气小得多，危害却能直接打瘫一整个网站。一次请求，整站缓存报废。

---

## 一、什么是 CPDoS

CPDoS（Cache Poisoned Denial of Service，缓存投毒拒绝服务）是 Web Cache Poisoning（Web 缓存投毒）家族里专门服务"拒绝服务"目标的子分支。和 SQLi 这种"立刻看到数据外泄"的攻击不一样，CPDoS 的核心动作是：**让缓存替攻击者把错误页面"合法化"**。

受害者不知道自己中毒，源站日志一切正常，但所有访问目标页面的合法用户都被挡在门外。完整资料参考 cpdos.org。

![CPDoS 攻击三种手法分类](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PCl3I8QmicaibMB1y0ocvfHakMu3sCRxD6RskJB4ElePw6zPoR4kMQDEKBHRrDHLkKwdiadJ5R1VvGcGyUnRiawIaJCBwOvicricDdI/640?from=appmsg "CPDoS 攻击三种手法分类")

---

## 二、攻击链 6 步拆解

CPDoS 的工作流非常清晰：

1. 攻击者发一个**带恶意 header** 的 HTTP 请求（任何 header 都行）

   ```
   x-mal-example: tohackthehacker
   ```
2. 请求先到**中间缓存**（CDN / 反向代理），缓存查不到目标资源的副本
3. 缓存把请求**原样转发**到源站
4. 源站因为畸形请求**返回错误页**（400 / 405 / 500）
5. 缓存把这个错误页当成"目标资源的最新副本"**存下来**
6. 后续所有合法用户访问这个资源，缓存**都**都返回错误页

源站本身没被攻破，数据也没泄露，但**整个缓存层的视图被毒化**。重启缓存才能恢复——这比 SQLi 的修复成本高得多。

---

## 三、三种 CPDoS 攻击手法

### 3.1 HHO（HTTP Header Oversize，HTTP 头超长）

HTTP 协议本身**没有规定 header 大小上限**。这给攻击者留了一个天然的"大小不一"裂缝：

* **缓存** 容忍的 header 长度：8KB / 16KB（Cloudflare 默认 16KB）
* **源站** 容忍的 header 长度：可能只有 4KB / 8KB（IIS、Nginx 默认值）

攻击者构造一个**比源站大、比缓存小**的 header，缓存收到觉得没问题，转发给源站，源站处理不了返回 `Header Size Exceeded`，缓存把 400 错误页存下来。

PoC：

```
GET / HTTP/1.1
Host: target.com
X-Oversized-Header-x: <8KB 随机字符串>
```

这种攻击对**未限制 header 大小的源站**（尤其是 IIS、Express 默认配置）几乎一击必杀。

### 3.2 HMC（HTTP Meta Characters，HTTP 元字符注入）

不靠大小，靠**元字符**让源站拒绝解析：

```
GET / HTTP/1.1
Host: target.com
X-Meta-Malicious-Header: \r\n
```

`\r\n`、`\n`、`\a` 这些元字符塞进 header，缓存接受（透传不解析），但源站严格按 RFC 解析时直接抛 `character not allowed` 错误。同样的剧本，错误页替换掉合法响应。

HMC 比 HHO 更隐蔽——头部大小看起来完全正常，单纯看大小检查根本抓不到。

### 3.3 HMO（HTTP Method Override，HTTP 方法覆写）

HTTP 标准里有一组"方法覆写"头，让代理在转发请求时把方法改成 header 里指定的值：

* `X-HTTP-Method-Override`
* `X-HTTP-Method`
* `X-Method-Override`

这三个 header 在 **Rails、Django、Express、Spring Boot** 等主流框架里都默认支持。攻击流程：

```
POST /api/users HTTP/1.1
Host: target.com
X-HTTP-Method-Override: DELETE
```

如果源站 API 没实现 DELETE 方法（很多只允许 GET/POST），就会返回 `405 Method Not Allowed`。缓存把 405 存住 → 后续所有合法 POST 请求都被挡在缓存层。

HMO 在 REST API 接口上尤其危险，因为 REST API 经常出现"某些方法没暴露但方法覆写头被启用"这种配置错位。

---

## 四、组合拳：H-b-H 头 + CPDoS

**Day-10 讲的 Hop-by-Hop 头滥用可以跟 CPDoS 联动**：

```
Connection: close, X-Oversized-Header-x
```

CDN / 反代看到 Connection 头里列出了 `X-Oversized-Header-x`，按 H-b-H 规则**把它从转发请求里剥掉**。但缓存自己那一层处理请求时已经"读到了"它的转发逻辑，把请求当成合法资源存起来。结果是：

* 缓存存的是"无恶意 header 时的正常响应"
* 但缓存实际存的内容对应的请求**和真实用户请求的语义不一样**

这种**协议层语义不一致**会让缓存行为完全不可预测，是更高级的 CPDoS 玩法。

---

## 五、实战记录（HackerOne 报告）

CPDoS 在真实漏洞赏金里已经被多次确认有效：

* #409370 — Cloudflare + 源站头大小不一致
* #728664 — Akamai + Rails 框架
* #921704 — Fastly + Spring Boot
* #326639 — Cloudflare + IIS 头大小
* #591302 — AWS CloudFront + Django

这些报告的共同点是：**头部大小或方法覆写机制差异被利用**，企业级 CDN 都在名单上。

---

## 六、防御要点

CPDoS 的根治要从**缓存层和源站层**两端同时收紧：

* **统一 header 大小限制**：缓存和源站配置相同的 `large_client_header_buffers`（Nginx）/ `MaxRequestHeadersSize`（IIS）
* **禁用方法覆写头**：除非业务明确需要，否则在反代层把 `X-HTTP-Method-Override` 系列头直接 drop
* **缓存不存错误页**：明确配置缓存**只存 2xx / 3xx**，4xx / 5xx 不缓存
* **缓存键包含 header**：避免攻击者的恶意 header 被混入缓存键
* **元字符过滤**：源站解析 header 时对 `\r\n`、`\n`、`\0` 等做严格检查
* **WAF 规则**：拦截 header 中包含元字符或长度异常的请求

CPDoS 不需要 SQLi 那种复杂利用链，也不需要 0day。一行特殊 header，整个网站就被打瘫——这是它最危险的地方，也是最容易被忽视的地方。

---

**原文出处**：learn365 Day-11 Cache Poisoned Denial of Service (CPDos) **综合参考**：cpdos.org · PortSwigger CPDoS 研究

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PsvmA4BJFbFvcCSVM6Y1MEFo6RYGrkwHGTeFXx4f5umetNnSZov7rLz16xL1Vc0ZjHtrsjDfdXlQ2zLpRqYUbfJVRibVOibn0DM/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NhJHQCd2DQicPcQXvnvFlsyEVHLjyxjibJBibHJHrPbibXep86ZIFnPtOQAlmowYuKAyrWSKEuvN86aica50VXSuEsz5r0qwj5V0RI/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PQwvbCaEicvHzS2zOGzfbjnT56HL1rvlFmWCMGOicMWCwTia1EZ8rmANeyue5fIukyASCSWHVWsbh9tP1wpv8U4kzrKOdlicfGpH8/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NicF5ia1ZXtx0UAQpAOtT4rYeFVxaE0PBY3hSlWicWJCIs5onaNwJOS5b7iaiboRFKuqDAm5Nm4yEgsDMBDYK2s424H7ZrTDtgiakAo/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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