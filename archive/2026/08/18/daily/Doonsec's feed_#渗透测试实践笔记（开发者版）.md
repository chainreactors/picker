---
title: #渗透测试实践笔记（开发者版）
url: https://mp.weixin.qq.com/s/yBx555I8fIPJkgpzxMuMWw
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:53:22.867076
---

# #渗透测试实践笔记（开发者版）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AjSHgfLXVrqJVzicFqQq5LbbDKvQrBDtXkJFXDWgVnSybic1Vl1VogVTA2Uhuwf57EA3jFrRRUoO1vqSibksEe2r55EjgsX1xMNPcsekK7RRDk/0?wx_fmt=jpeg)

# #渗透测试实践笔记（开发者版）

红客攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ZKURiabKFyfPqvqVk1ndN5hv4jt86AJhguTGEcYiaLKC2Tgxmw3ZnqgEUJgkFGcGCsPz0oSrjlIggHzrvKrWekvqmSenbPFlLrjXqgxHVNbTk/640?wx_fmt=jpeg#imgIndex=0)

**一、概述**

渗透测试（Penetration Testing，简称 pen-testing）是一种主动安全评估方法——通过模拟真实攻击，在攻击者利用漏洞之前主动暴露注入缺陷、弱身份验证、配置错误等问题。

合规实践中，通常还会配合两类正式评估：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZKURiabKFyfPLibWYLxxH4PCy303CMFjSKHibWvMRWIYrCzces0G7ibTDgXT6W1ZZ1pSuaNuhX500CmyJ7DwiclYicTLpXjD4HRj7bznO6eLEtib6s/640?wx_fmt=png#imgIndex=1)

**二、常见 Web 攻击速查表**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKURiabKFyfP0rzibGVEzHGcLl93Ewx5rBKwutrvxV0bD7V8jbnIBj9a4jj9Rl2HqoVIibVTrc22nYZ0Sgj7iaseNndjC1jNFasI6WS9cC63cAA/640?wx_fmt=png#imgIndex=2)

**三、渗透辅助工具：PenTestingHelper**

**01.**

**设计思路**

构建一个可复用的 C# 工具类，覆盖渗透测试的五个核心环节：

```
侦察 → 安全头检查 → Cookie 标志验证 → CSRF 保护测试 → 模糊测试
```

**02.**

**完整代码**

```
using System.Net.Http.Json;using System.Text;using System.Text.Json;
namespace MyPlaygroundApp.Utils{    publicclassPenTestingHelper    {        private readonly HttpClient _httpClient;
        publicPenTestingHelper(string baseUrl){            _httpClient = new HttpClient { BaseAddress = new Uri(baseUrl) };        }
        // ① 侦察：探测常见端点，收集信息        public async Task RunReconnaissanceAsync(){            Console.WriteLine("\n[Reconnaissance]");            var endpoints = new[] { "/robots.txt", "/.well-known/security.txt", "/favicon.ico" };            foreach (var ep in endpoints)            {                var res = await _httpClient.GetAsync(ep);                Console.WriteLine($"{ep} -> {(int)res.StatusCode} {res.ReasonPhrase}");            }        }
        // ② 安全头检查：确认关键安全头是否存在        public async Task CheckSecurityHeadersAsync(){            Console.WriteLine("\n[Security Header Check]");            var res = await _httpClient.GetAsync("/");            var headers = new[] { "X-Frame-Options", "X-Content-Type-Options", "Content-Security-Policy", "Referrer-Policy" };            foreach (var header in headers)            {                Console.WriteLine($"{header}: {(res.Headers.Contains(header) ? "Present" : "Missing")}");            }        }
        // ③ Cookie 标志验证：检查 HttpOnly / Secure 是否设置        public async Task CheckCookieFlagsAsync(string loginUrl){            Console.WriteLine("\n[Cookie Flags Validation]");            var res = await _httpClient.GetAsync(loginUrl);            if (res.Headers.TryGetValues("Set-Cookie", out var setCookies))            {                foreach (var cookie in setCookies)                {                    Console.WriteLine($"Set-Cookie -> {cookie}");                    if (!cookie.Contains("HttpOnly")) Console.WriteLine("  Warning: Cookie missing HttpOnly");                    if (!cookie.Contains("Secure")) Console.WriteLine("  Warning: Cookie missing Secure");                }            }            else            {                Console.WriteLine("No cookies found in the response.");            }        }
        // ④ CSRF 保护测试：无令牌的 POST 应被拒绝        public async Task TestCsrfProtectionAsync(string endpoint){            Console.WriteLine("\n[CSRF Protection Test]");            var res = await _httpClient.PostAsync(endpoint, new StringContent("{\"dummy\":\"x\"}", Encoding.UTF8, "application/json"));            Console.WriteLine($"{endpoint} -> {(int)res.StatusCode} {res.ReasonPhrase}");        }
        // ⑤ 模糊测试：用恶意/超大负载探测输入验证        public async Task FuzzEndpointAsync(string endpoint){            Console.WriteLine("\n[Fuzzing Endpoint]");            var payloads = new[]            {                new { name = "normal" },                new { name = "' OR '1'='1" },                        // SQL 注入探测                new { name = "" },          // XSS 探测                new { name = newstring('A', 5000) }                 // 超大输入 / DoS 探测            };
            foreach (var payload in payloads)            {                var res = await _httpClient.PostAsJsonAsync(endpoint, payload);                Console.WriteLine($"Payload: {JsonSerializer.Serialize(payload)} -> {(int)res.StatusCode} {res.ReasonPhrase}");            }        }    }}
```

**03.**

**调用方式**

```
using MyPlaygroundApp.Utils;
classProgram{    static async Task Main(string[] args){        var baseUrl = "https://your-app-url.com";        var helper = new PenTestingHelper(baseUrl);
        await helper.RunReconnaissanceAsync();        await helper.CheckSecurityHeadersAsync();        await helper.CheckCookieFlagsAsync("/login");        await helper.TestCsrfProtectionAsync("/bank/transfer");        await helper.FuzzEndpointAsync("/api/test");    }}
```

**04.**

**运行命令**

```
dotnet run
```

**四、安全 vs 脆弱应用——结果对照**

**01.**

**侦察**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZKURiabKFyfN4xlqiaS6BiaiaJTJGaq9Rhx4418NZe7M15dl63D99dDrZJNd42YvY0Gh82kWjdH7UIu96JqdE7Zqm5h7OozF85UQqpK9l72peeY/640?wx_fmt=png#imgIndex=3)

**02.**

**安全头检查**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKURiabKFyfMqhJNBsb6VJtFMPkiaNvm3J7Ks7Qj581jD7GfeL4wBENGIdYAnibVKyWPL3kecauEicrtiaL05ibRIicDqIBibVFXqueJ1LBbzZhq39M/640?wx_fmt=png#imgIndex=4)

**03.**

**标志验证**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZKURiabKFyfOveVibRLWpVQq9Xa42mrfY0dcZ7rSPMDTfSUgYDPKNw51kSfNIC2rxDzqM5Lw7HH5sKvMB9fnl6ERyl0lHV6OBA1QSna47FbfM/640?wx_fmt=png#imgIndex=5)

**04.**

**CSRF 保护测试**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZKURiabKFyfP355SDLHjoic7SGYeTUvnUehvQ4QfJeKL2uwickt20aXUotAibexXJ9zjhejySIp6VVQNBiaj2dVE1FZq1mm1cKUBL18s9w7lAGjc/640?wx_fmt=png#imgIndex=6)

**05.**

**模糊测试**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ZKURiabKFyfNWAHCpFY1eLDaXD6ia2JmXEVmic7esiaxXXfbJrebPmr3KCIZRW5znO0icu15S8L2vU5icZRUVNxjZhNo6DOAqeDcxv0puZPdZDpgo/640?wx_fmt=png#imgIndex=7)

**五、安全响应头中间件**

在 Program.cs 中添加以下中间件，可以一键配置全部推荐安全头：

```
app.Use(async (context, next) =>{// 防 MIME 嗅探    context.Response.Headers.Append("X-Content-Type-Options", "nosniff");
// 防点击劫持    context.Response.Headers.Append("X-Frame-Options", "DENY");
// 控制 Referrer 信息    context.Response.Headers.Append("Referrer-Policy", "strict-origin-when-cross-origin");
// 旧版浏览器 XSS 保护    context.Response.Headers.Append("X-XSS-Protection", "1; mode=block");
// 限制浏览器功能    context.Response.Headers.Append("Permissions-Policy","camera=(), microphone=(), geolocation=(), payment=(), usb=()");
// CSP：定义允许加载的资源    var connectSrc = app.Environment.IsDevelopment()        ? "'self' ws: wss: http://localhost:* https://localhost:* https://cdnjs.cloudflare.com https://cdn.jsdelivr.net https://ajax.googleapis.com https://ajax.aspnetcdn.com"        : "'self' https://cdnjs.cloudflare.com https://cdn.jsdelivr.net https://ajax.googleapis.com https://ajax.aspnetcdn.com";
    var csp = "default-src 'self'; " +"script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdnjs.cloudflare.com https://cdn.jsdelivr.net https://ajax.googleapis.com https://ajax.aspnetcdn.com; " +"style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com https://cdn.jsdelivr.net https://ajax.googleapis.com https://ajax.aspnetcdn.com; " +"font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com https://cdn.jsdelivr.net https://ajax.googleapis.com; " +"img-src 'self' data: https:; " +              $"connect-src {connectSrc}; " +"frame-ancestors 'none'; " +"base-uri 'self'; " +"form-action 'self'; " +"upgrade-insecure-requests";
    context.Response.Headers.Append("Content-Security-Policy", csp);
// 生产环境强制 HTTPSif (!app.Environment.IsDevelopment())    {        context.Response.Headers.Append("Strict-Transport-Security","max-age=31536000; includeSubDomains; preload");    }
// 移除服务器标识信息    context.Response.Headers.Remove("Server");    context.Response.Headers.Remove("X-Powered-By");
    await next();});
```

**01.**

**各安全头作用对照**

```
;0x0a ou \n (caractère du saut à la ligne)$()
```

![图片](https:/...