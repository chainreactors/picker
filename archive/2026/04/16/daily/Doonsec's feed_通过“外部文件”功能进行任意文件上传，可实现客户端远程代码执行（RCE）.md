---
title: 通过“外部文件”功能进行任意文件上传，可实现客户端远程代码执行（RCE）
url: https://mp.weixin.qq.com/s/KWsTNIOfcggyq0JTdzgatQ
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:48:47.901041
---

# 通过“外部文件”功能进行任意文件上传，可实现客户端远程代码执行（RCE）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnvIwpmwUddyL3uSJ9h4eTYBmNwIav4KFEfmiaKphPd7p91W3ibJSTlwzWiaCiavZ63meA0ViaWO0WMxCWnwic2ZjasW5D2iauoiamIKkKk/0?wx_fmt=jpeg)

# 通过“外部文件”功能进行任意文件上传，可实现客户端远程代码执行（RCE）

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsKGQUytQQMDapcfkMtfb8mmgTkJkx2o5TlIm8H8xCRAoVCOE9aUmxmMia0oe56TX5JUoUFI88U595StSKricx8yryWb2Xd5nNC0/640?wx_fmt=png&from=appmsg)

## 概括

在对一个基于网络的平台（以下简称[**已编辑**]）进行评估时，我发现项目控制面板中“外部文件”功能的文件上传机制存在一个严重漏洞。该功能旨在允许已认证用户导入补充文档（例如[`.txt`此处应填写`.md`文件类型]），以丰富项目需求。

用户界面明确强制执行以下约束：

> *仅允许 .txt 和 .md 文件格式 · 最多 5 个文件 · 每个文件最大 10KB*

然而，这些限制仅存在于客户端。后端对文件扩展名、MIME 类型或内容主体不做任何验证。攻击者可以通过拦截上传请求并篡改相关字段，提交任意文件类型，包括那些下载并执行后可在客户端计算机上执行代码的格式。此类漏洞正式编号为CWE-434：不受限制地上传危险类型的文件。

按回车键或点击查看完整尺寸的图片

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntpQsxHJlcu3Pp0dpKvsm0WhApsPloNNNL0U20ud5AsibD8EJy6GryIMBZno2SGCHp8oRu9LIPd3SCN0ibRPj78tqWsrtlWhUOs0/640?wx_fmt=png&from=appmsg)

为了展示此漏洞的严重性，我精心制作并上传了一个`.hta`包含基于 ActiveX 的有效载荷的文件。该文件在 Windows 系统上下载并打开后，会被程序处理`mshta.exe`，并作为无害的执行证明启动`calc.exe`。其他可执行文件格式，包括 .NET Framework`.html`和 .NET Framework `.exe`，也都经过测试，并且都能正常执行。

## 技术分析

### 上传机制和仅客户端验证的差距

**“外部文件”**部分位于项目控制面板中，用作项目补充文档的存储库。文件上传通过`POST`向以下端点发送请求来执行：

```
/api/app/uiengine/odata/[已编辑]/modules/projectDashboard/pages/components/InputsTab/ExternalTools/$batch批次
```

请求体是一个 JSON 结构，其中包含文件元数据和内容：

```
{
"requests" : [
{
"method" : "POST" ,
"body" : {
"projectId" : [已编辑] ,
"fileName" : "sample.txt" ,
"fileType" : "text/plain" ,
"uploadData" : {
"content" : "Lorem Ipsum." ,
"uploadDate" : "2025-07-15T22:58:51.555Z"
}
} ,
"id" : "86" ,
"atomicityGroup" : "86" ,
"url" : [已编辑]"
}
]
}
```

上传行为受以下三个因素控制：

* `fileName`：决定显示的名称和文件扩展名。
* `fileType`：声明 MIME 类型。
* `uploadData.content`：以字符串形式携带完整的文件内容。

这些字段均未经过服务器端清理或验证。后端直接接受客户端提供的任何内容，保存文件，并将其作为可下载资源显示在用户界面中。无需任何询问。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/R98u9GTbBnsVr2u6DTQaV3XiaM5gHnRKAnnkLr8sSoMwl75cZoM6RleLftk34IHs7bGYIfr8Ozh8J1p4roPQZ1kRpfuosicVXzETvZy0DGbzg/640?wx_fmt=gif&from=appmsg)

这是一个典型的过度信任客户端控制的案例。用户界面中显示的限制（文件类型允许列表、大小上限、文件数量限制）完全由浏览器的 JavaScript 代码执行。任何使用 Web 代理的用户，甚至使用浏览器内置的开发者工具，都可以轻松绕过这些限制。客户端验证作为可用性层，其作用是合理的：它提供即时反馈并防止意外滥用。但它绝不能成为安全相关限制的唯一执行机制。如果没有相应的服务器端允许列表来独立验证文件扩展名、检查 MIME 类型，并且最好还能根据预期签名验证内容的“魔数”，那么上传端点实际上就不受任何限制。

## 利用服务器端验证的缺失来将`.hta`有效载荷武器化

坦白说，这种利用方式非常简单。`.txt`攻击者只需使用 Web 代理拦截合法的上传文件，就能在 JSON 有效载荷到达服务器之前完全控制它。只需将 `<json-payload>` 替换为 `<json-payload>`，将`<json-payload>` 替换`fileName`为`<json-payload> `，并将可执行的 HTA 标记注入到 `<json-payload>` 中即可：`payload.hta``fileType``application/hta``uploadData.content`

```
{
"requests" : [
{
"method" : "POST" ,
"body" : {
"projectId" : [已编辑] ,
"fileName" : "payload.hta" ,
"fileType" : "application/hta" ,
"uploadData" : {
"content" : "<html><head><script>var shell = new ActiveXObject(\"WScript.Shell\");shell.Run(\"calc.exe\");</script></head><body></body></html>" ,
"uploadDate" : "2025-07-15T22:58:51.555Z"
}
} ,
"id" : "86" ,
"atomicityGroup" : "86" ,
"url" : [已编辑]"
}
]
}
```

上传成功。恶意`.hta`文件与可供下载的合法文档一起出现在用户界面中，等待用户打开。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/R98u9GTbBnu6ZofbPPaBXDgicH00ZaosXxd5ib6zJtic66Il3gsNWicCJU2VB1eWWNry8UfIGW6Z8JlXmAShhXl6S83rria78OWNibibYVPZzS80ak/640?wx_fmt=gif&from=appmsg)

## 我为什么选择`.hta`进行概念验证？理由如下。

按回车键或点击查看完整尺寸的图片

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBntA5y2WFyibuUcF3qW6FqAGaPFx9TcB5K4Oyr2Dv3zXjZqzP9GHGmXMUzXFvB4ia40Mwx1BpzwibOAqZOtvUSowlRccKfDHlhbqIk/640?wx_fmt=jpeg&from=appmsg)

我`.hta`特意选择了 HTML 应用程序 (HTA) 格式，因为它在 Windows 系统上具有独特的执行模型。HTA 文件在结构上与 HTML 文档完全相同，但它的运行机制却截然不同。当用户打开文件时`.hta`，Windows 会将执行权委托给`mshta.exe`Microsoft HTML 应用程序主机 (Microsoft HTML Application Host)，这是一个位于 [此处应填写具体地址] 的已签名本地二进制文件`C:\Windows\System32\mshta.exe`。与在浏览器沙盒环境中呈现的标准`.html`文件不同，HTA 文件作为独立应用程序在浏览器的安全上下文之外运行。这意味着它不受 Internet Explorer 区域限制、保护模式限制或浏览器对 Web 脚本施加的任何沙盒控制的约束。

因此，嵌入在 HTA 文件中的脚本以当前用户的完整权限运行。它们可以实例化 COM/ActiveX 对象、与 Windows 脚本宿主交互、读写文件系统、修改注册表以及生成任意进程。在我的概念验证中，有效载荷利用了这一功能实例化了一个`WScript.Shell`ActiveX 对象并调用了 `execute``calc.exe`命令，这是一个标准的、无害的任意命令执行演示。

从攻击性安全角度来看，`mshta.exe`它被归类为“本地二进制文件”（Living off the Land Binary，简称LOLBin），这是一类合法的、由厂商签名的系统实用程序，攻击者通常会利用它们来代理恶意代码的执行。由于`mshta.exe`它是随每个Windows系统安装一起提供的可信微软二进制文件，因此它的执行可以无缝地融入正常的系统活动中，并且不太可能触发端点检测产品的行为启发式规则。它在MITRE ATT&CK框架中拥有自己的条目，技术编号为T1218.005（系统二进制文件代理执行：Mshta），并且被众多威胁行为者和恶意软件家族在实际攻击活动中积极利用。

就这么简单。

## 影响

虽然客户端远程代码执行 (RCE)`.hta`是此漏洞最直观的演示，但其根本风险是系统性的。上传机制对进入平台的文件没有任何服务器端限制，这意味着“**外部文件”**功能实际上是一个嵌入在可信接口中的不受限制的文件分发通道。

这会带来两个直接后果。首先，任何经过身份验证的用户都可以利用此功能，向从同一项目下载文件的任何人传播可执行文件或其他有害内容。其次，在协作或多用户环境中，攻击者无需通过外部渠道进行网络钓鱼、重定向或社会工程攻击。有效载荷已存在于平台内部，位于共享工作区中，由应用程序本身提供服务。

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx

##

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBns0d8QwbHTnYHJTtWVKPXdz9LyDdg1OLRibHhZcqA6W7mhw3OzwBKYN7TKwGLSVFtspNNjnOmTAonyoD91iaKvOLEanZVdxUzebo/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsNUop1xm6mAk7KzKpd5Rc68ibM0icgSbe19Snot40Zib0RhuAb4pia8KBXA5vQRNLQRfvDmuPOFpkpibW0MyQnhqkTibGcaNSLb2lbY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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