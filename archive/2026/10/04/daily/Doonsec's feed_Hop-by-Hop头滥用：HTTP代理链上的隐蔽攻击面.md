---
title: Hop-by-Hop头滥用：HTTP代理链上的隐蔽攻击面
url: https://mp.weixin.qq.com/s/8On1DsZIzRqhuJJSM9b6rw
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:55:43.448764
---

# Hop-by-Hop头滥用：HTTP代理链上的隐蔽攻击面

# Hop-by-Hop头滥用：HTTP代理链上的隐蔽攻击面

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OqTsia24eLmPISQcSqicg5NH8pzkeb0mgtIjzyicEJa6vmACaBliaicbpHdibfbfLs4cvp3GpD9FeQM22s0TT1LYKBNhQibxWHNEffaI/640?from=appmsg)
> **导语**：HTTP/1.1规范里规定，Connection头可以声明一组"只对单跳连接有效"的自定义头，下游代理会把它们从请求里剥掉。听起来像规范细节，攻击者却把它玩成了绕过认证、隐藏源IP、打穿WAF的万能钥匙。

---

## 一、什么是 Hop-by-Hop 头

RFC 9110（HTTP Semantics）把 HTTP 头分成两类：

* **End-to-End 头**（端到端）：从客户端一路传到后端，中间所有代理都必须原样转发，比如 `Cookie`、`Authorization`、`X-Forwarded-For`
* **Hop-by-Hop 头**（逐跳）：只在单次传输连接内有效，不能被缓存或代理转发

HTTP/1.1 规范明确规定的 H-b-H 头只有 8 个：

```
Connection、Keep-Alive、Proxy-Authenticate、Proxy-Authorization、
TE、Trailers、Transfer-Encoding、Upgrade
```

其余全是 HTTP 头。但 Connection 头有个特殊能力——**声明自定义 H-b-H 头**：

```
Connection: close, X-Foo, X-Bar
```

按规范，下游代理看到 Connection 头里列出的字段名，就该把同名头从请求里剥离再转发。

![Hop-by-Hop 攻击流程图](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OKv3NMhRJugbE0xmMzqnkGlEwiciaRnP0wE7ZfTyP3bsf77Nw9ow6zjyL1pOP9f6JsptaNperFUALvziaMZu6Pw0vqkibF7DwKGu4/640?from=appmsg "Hop-by-Hop 攻击流程图")

---

## 二、攻击原理：规范与实现的裂缝

RFC 写得很清楚：兼容代理**必须**把 Connection 头里列出的字段从转发请求里剥掉。但现实里很多代理实现是糊的：

* 反向代理 Nginx 在某些版本下会**原样转发** Connection 头
* HAProxy 默认透传整个 Connection 头
* 部分 CDN（Cloudflare、Akamai）行为也未必一致

这就让"逐跳代理"理解出现了裂缝：上游代理往 Connection 里塞个 `Cookie`，下游代理没按规范剥离，原封不动转给后端——但有些场景下，下游代理又**真的会**剥离。

攻击者要做的就是：**赌一把规范实现**，把本该端到端的关键头塞进 Connection，看中间哪一跳会把它吃掉。

---

## 三、攻击链条拆解

假设架构：用户 → CDN → WAF → Nginx 反代 → 后端应用

1. 应用要求必须有 `Cookie` 才能访问
2. 攻击者在请求里写 `Connection: close, Cookie`
3. CDN 把 Connection 透传给 WAF
4. WAF 看到 Connection 里列了 `Cookie`，按 H-b-H 规则剥离这个头
5. 请求到达 Nginx 时已经**没有 Cookie**
6. Nginx 把"无 Cookie 的请求"转发给应用
7. 应用如果没强制校验，直接放行 → **未授权访问**

实际场景下不同位置剥头，攻击效果不一样：

* **CDN 剥头**：客户端真实 IP 在请求链上消失，源站看到的 `X-Forwarded-For` 缺失，便于**指纹探测** + **源站暴露**
* **WAF 剥头**：WAF 自己"看不见"Cookie，规则匹配失效，相当于**绕过 WAF**
* **反代剥头**：Nginx 上配置的限流、IP 黑名单全部失效，便于**绕过认证**

---

## 四、六类实战用途

### 4.1 指纹识别

往 Connection 里塞随机头名，看哪一跳报错、从错误信息里推断代理类型和版本。Nginx 和 HAProxy 对未知 H-b-H 头的处理方式不一样。

### 4.2 访问认证端点 / 保护资源

最直接的攻击——把 `Cookie`、`Authorization`、`X-Auth-Token` 塞进 Connection：

```
GET /admin/dashboard HTTP/1.1
Host: target.com
Cookie: session=abc123
Connection: close, Cookie
```

如果中间代理"听话"剥掉 Cookie，后端拿不到会话标识，攻击者就能用**任何人都能访问的请求**触发**只有登录后才有的逻辑漏洞**（比如找回密码接口返回他人邮箱）。

### 4.3 隐藏源 IP

CDN 后面的真实 IP 一般通过 `X-Forwarded-For` 头传给源站。攻击者把 `X-Forwarded-For` 塞进 Connection，让 CDN 在转发给源站前剥掉它——**源站日志里就只剩 CDN 的出口 IP**，溯源难度上升一档。

### 4.4 CPDoS（Cache Poisoned Denial of Service，缓存投毒拒绝服务）

通过 Connection 头让 CDN 缓存错误的响应（HTTP 400 / 405），让后续所有合法用户都拿到错误页。这是一种"低成本 DoS"，把 H-b-H 滥用玩到了 DoS 层面。

### 4.5 SSRF（Server-Side Request Forgery，服务端请求伪造）

部分云环境（AWS metadata、Aliyun metadata）的访问控制依赖 `X-Forwarded-For` 判断"内网调用"。把 `X-Forwarded-For` 塞进 Connection 让代理剥掉，后端以为请求来自内网 → metadata 服务被未授权访问。

### 4.6 WAF 绕过

WAF 一般检查 `Cookie`、`User-Agent`、`Referer` 这些常见攻击载荷出现的位置。把这些头塞进 Connection，WAF 在自己的逻辑层"看不到"这些字段，规则全部失效。这是 2020 年 PortSwigger 报告里专门提到的一类 WAF 盲点。

---

## 五、工具和实战 PoC

官方推荐的两个工具仓库：

* mrtc0/abusing-hop-by-hop-header — 一键 Fuzz 整套 HTTP 头
* ndavison gist — Burp 插件 + Burp 请求模板

实战 Fuzz 脚本（一行就跑遍所有头）：

```
for HEADER in $(cat headers.txt); do
  python http://poison-test.py -u "https://target.com" -x "$HEADER"
  sleep 1
done
```

字典来源：SecLists 的 `lowercase-headers`（BurpSuite-ParamMiner/lowercase-headers）。

进一步阅读：

* 0xn3va GitBook Cheat Sheet
* Nathan Davison 原文

---

## 六、防御要点

* **代理层规范化处理**：Connection 头必须严格按 RFC 解析，列出 H-b-H 后必须真正剥离
* **不要把鉴权头当成 H-b-H 转发**：Cookie / Authorization / X-Auth-\* 必须保留到源站
* **强制应用层鉴权**：哪怕 Cookie 被剥掉，后端也要校验 IP 白名单、CSRF Token、设备指纹
* **WAF 配置 X-Forwarded-For 信任链**：明确告诉 WAF 哪一跳是可信的，避免被前端靠 Connection 头骗过

逐跳头本来是 HTTP 协议留给代理栈的"性能优化"机制。攻击者用一句话（Connection 头里多塞个名字），就能让整个链路翻车。

---

**原文出处**：learn365 Day-10 Abusing Hop-by-Hop Headers **参考**：Nathan Davison《Abusing HTTP Hop-by-Hop Request Headers》

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Mrv8JRn2ocmYVECft2mcpcHsTj42SQBnC5qdgs5BxP2HGYQ6icZEDpFpomcMXXJcA7mCADrGz77hvacAKLpEtHveC1gvibqIFkQ/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OhEsoXQKTF5C0rNBlTtUjg8tTnQ73y4zXAlB5o0aCT1niaW1AZywbWY5GxNzZn9fhYOw832zHV2NXmgIvc9LYicQZIj1vLSx0CU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OyOksCULNtib0ydKf7kic5SAnyqHs8viaUvjIicnUyXkJicHvVvicA9fkkOmfe8JMAGGWT01fDKibmib5pxx4nCicJiagUvaCnyZia8IVrbM/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OU1QiaaJ6ib6RQ4SE6YZpskxxp2hIPRXZS8Wh9SiaONxobUnftNcialWV7MBrzYs33HwdRw11NzqZHBTTfnxNvqDBRh4w4cBaNqOI/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

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