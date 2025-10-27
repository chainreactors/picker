---
title: .NET 代码审计：发现某企业级 OA 系统中任意文件下载漏洞
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498871&idx=1&sn=d261fad92b90cc79e3796f377d25a658&chksm=fa59529acd2edb8c7e6332dfcada6233d17fd489271cb6a618488ca71747042ade56663166af&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-12
fetch_date: 2025-10-06T20:37:16.477205
---

# .NET 代码审计：发现某企业级 OA 系统中任意文件下载漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8MZzRIpyq46vrVWUE2BEN3oNWQOKYQ5dM9cibLbHYq0IF7SiajKeMeNcCzdgaMfL7iceThx0amXpEUw/0?wx_fmt=jpeg)

# .NET 代码审计：发现某企业级 OA 系统中任意文件下载漏洞

原创

专攻.NET安全的

dotNet安全矩阵

![图片](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

在企业级OA系统的业务交互过程中，文件上传和下载是常见的功能需求。然而，往往会在实现这些功能时忽视安全性，导致系统可能存在一些安全漏洞，特别是文件下载漏洞。

**01. 漏洞代码分析**

下面通过对某OA系统代码的审计，详细分析如何发现并利用任意文件下载漏洞，以及如何修复该漏洞。我们首先来看漏洞代码的实现逻辑

```
```
string fileName = Request.QueryString["file"];
string filePath = Path.Combine(Server.MapPath("~/Uploads/"), fileName);
FileStream fs = new FileStream(filePath, FileMode.Open);
byte[] bytes = new byte[(int)fs.Length];
fs.Read(bytes, 0, bytes.Length);
fs.Close();
Response.ContentType = "application/octet-stream";
Response.AddHeader("Content-Disposition", "attachment; filename=" + HttpUtility.UrlEncode(fileName, System.Text.Encoding.UTF8));
Response.BinaryWrite(bytes);
Response.Flush();
Response.End();
```
```

这段代码的功能是根据请求参数中的 file 字段来动态生成文件路径，然后读取该文件并通过 HTTP 响应流返回给客户端，实现文件下载。

**02. 漏洞利用过程**

假设攻击者知道或者猜测到该OA系统的文件下载功能，并且能够访问到该系统的 file 查询参数。攻击者可以通过构造恶意请求读取服务器上敏感文件

```
```
http://target.com/download.aspx?file=../web.config
```
```

攻击者构造请求，传递 file 参数为 ../web.config，由于路径拼接时没有有效的路径检查，服务器最终会读取到服务器根目录下的 web.config 配置文件。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9mv6lbnzxs2ZUdSU7jvuHbq9zrOV4f1evqAT7In6DpicLFib3ibthVoso6J9K8EKv9jtOnEibtgYfxEQ/640?wx_fmt=png)

该文件内容会作为二进制流返回给攻击者，攻击者就能直接下载敏感配置文件，进而获取数据库连接字符串、加密密钥等敏感信息。

**03. 代码审计和挖掘**

Response.**BinaryWrite** 是将文件内容或者二进制数据写入 HTTP 响应流的一个方法，在实现文件下载功能时，如果没有对文件路径或文件类型进行严格的控制，Response.BinaryWrite 可以直接发送任何文件的字节流，导致文件泄露。

从 代码安全审计 的视角来看，Response.BinaryWrite 确实是一个值得重点关注的方法。当 Response.AddHeader 一起使用时，如果代码中没有进行严格的输入验证和文件路径检查，就可能导致任意文件下载漏洞。

```
```
Response.AddHeader("Content-Disposition", "attachment; filename=" + HttpUtility.UrlEncode(fileName));
```
```

该头部指示浏览器将响应内容视为附件并提示用户下载文件。filename 字段指定了下载文件的名称。

**04. 漏洞处置修复**

确保从用户输入中获得的文件路径经过严格的验证和过滤。使用路径拼接时，要避免路径遍历攻击。可以通过以下方法来限制文件的访问范围：

```
```
string fileName = Request.QueryString["file"];
string filePath = Path.Combine(Server.MapPath("~/Uploads/"), fileName);
string fullPath = Path.GetFullPath(filePath);

// 判断文件是否在允许的目录内
if (!fullPath.StartsWith(Server.MapPath("~/Uploads/")))
{
    Response.StatusCode = 403;
    Response.End();
}
```
```

这样可以确保文件只来自于指定的 Uploads 目录，从而防止路径遍历漏洞，另外还可以限制用户可以下载的文件类型，确保只允许特定的文件类型，如图片、PDF 或文档等。这可以通过验证文件扩展名或 MIME 类型来实现。

```
```
string[] allowedExtensions = { ".jpg", ".png", ".pdf", ".txt" };
string fileExtension = Path.GetExtension(fileName).ToLower();
if (!allowedExtensions.Contains(fileExtension))
{
    Response.StatusCode = 400;
    Response.End();
}
```
```

这样，只有符合规定扩展名的文件才能被下载，避免用户通过绕过过滤规则上传和下载恶意文件。

综上，Response.BinaryWrite 配合 Response.AddHeader 可能导致 任意文件下载漏洞，如果代码没有对文件路径和文件名进行有效的验证和限制，攻击者就可能通过路径遍历和文件名欺骗等手段，访问敏感文件或下载恶意文件。

**05. NET代码审计学习**

微软的.NET技术广泛应用于全球企业级产品，包括其知名的**Exchange**、**SharePoint**等，国内如**某友的Cloud**、**某通的T系列**、**某蝶的云产品**等也广泛采用。各行业核心业务均依赖于此技术。这些基于.NET的系统频繁遭攻击，问题涵盖任意文件上传、反序列化漏洞、SQL注入、文件下载漏洞、命令执行漏洞等。

截至目前，星球已推出近**100节内容** (还在持续增加)，包括**70个视频+30份PDF文档**。我们已将内容细致划分为15个分类，并随新漏洞类型的出现持续扩展。在这里您将学到包括但不限于以下漏洞类型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8fTUcmnHC8g2WjE6SZJIjwdR00lAaNpUuDDlI6Gk1uEEPZxUMlb4FkDvOBLYq92InlzpwmzWeibjQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

详细的内容与结构，请参考下方的星球大纲版块，包括但不限于OWASP十大漏洞类型，涉及SQL注入漏洞、文件上传下载漏洞、任意文件操作漏洞、XML外部实体注入漏洞、跨站脚本攻击漏洞、反序列化漏洞、命令执行漏洞、未授权和越权漏洞、第三方组件漏洞等等。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8fTUcmnHC8g2WjE6SZJIjwMahhN19jbtUiax5UWVU0R3n4eick9XQEHyf3lhjE3wvCic9ZFD3h9tWsQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

## 专属福利

1. 学习模式: 代码审计知识星球**在线录播视频** +后续漏洞挖掘直播、内部专属交流社区答疑解惑；

2. 优享福利：加入.NET代码审计星球后**赠送永久**dot.Net安全基础入门星球。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkE3ACnPUtfbn99XZmI6ANI9DCxS2KHkqiaXBk22ZevuRm08onmEibIUvdEy5zJGCoHg4HAsrgQ22w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

欢迎对.NET代码审计关注和关心的同学加入我们 [dot.Net安全代码审计] ，目前已有近 100+ 位朋友抢先预定。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicAg36pkFaC2P1KW0L5NV1HOssmysrPnrP1fzr2rFOmy8lA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

星球门票后期价格随着内容和质量的不断沉淀会适当提高，**越早加入越划算！** 现在加入星球可享受星球早鸟价，并可**领取100元优惠券**，期待在这里能遇到有情有义的小伙伴，大家聚在一起做一件有意义的事，**可扫描下方老师二维码了解更多详情。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkE3ACnPUtfbn99XZmI6ANBJ4t8XC4ibbWjhzj0447zAJcWgwV9wcDhcibNiax3P7iagSYwn31GEkTBw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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