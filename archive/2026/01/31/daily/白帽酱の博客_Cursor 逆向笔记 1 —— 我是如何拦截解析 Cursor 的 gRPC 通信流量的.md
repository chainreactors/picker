---
title: Cursor 逆向笔记 1 —— 我是如何拦截解析 Cursor 的 gRPC 通信流量的
url: https://rce.moe/2026/01/31/cursor-reverse-notes-1/
source: 白帽酱の博客
date: 2026-01-31
fetch_date: 2026-02-01T04:26:43.477701
---

# Cursor 逆向笔记 1 —— 我是如何拦截解析 Cursor 的 gRPC 通信流量的

Toc

1. [前言](#%E5%89%8D%E8%A8%80)
2. [从 Burp 开始，然后被 CA 打脸](#%E4%BB%8E-Burp-%E5%BC%80%E5%A7%8B%EF%BC%8C%E7%84%B6%E5%90%8E%E8%A2%AB-CA-%E6%89%93%E8%84%B8)
3. [SSE 把 IDE 卡死了](#SSE-%E6%8A%8A-IDE-%E5%8D%A1%E6%AD%BB%E4%BA%86)
4. [自己写 SSL 中间人](#%E8%87%AA%E5%B7%B1%E5%86%99-SSL-%E4%B8%AD%E9%97%B4%E4%BA%BA)
   1. [MITM 的核心原理](#MITM-%E7%9A%84%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86)
   2. [动态证书签发](#%E5%8A%A8%E6%80%81%E8%AF%81%E4%B9%A6%E7%AD%BE%E5%8F%91)
   3. [TLS 握手与双向转发](#TLS-%E6%8F%A1%E6%89%8B%E4%B8%8E%E5%8F%8C%E5%90%91%E8%BD%AC%E5%8F%91)
   4. [KeyLog 输出](#KeyLog-%E8%BE%93%E5%87%BA)
   5. [最终的代码结构](#%E6%9C%80%E7%BB%88%E7%9A%84%E4%BB%A3%E7%A0%81%E7%BB%93%E6%9E%84)
5. [GRPC 的流量分析](#GRPC-%E7%9A%84%E6%B5%81%E9%87%8F%E5%88%86%E6%9E%90)
   1. [这并不是常见的 REST](#%E8%BF%99%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%B8%B8%E8%A7%81%E7%9A%84-REST)
   2. [没有 .proto 怎么办](#%E6%B2%A1%E6%9C%89-proto-%E6%80%8E%E4%B9%88%E5%8A%9E)
   3. [从 JS 还原 .proto](#%E4%BB%8E-JS-%E8%BF%98%E5%8E%9F-proto)
   4. [循环导入的处理](#%E5%BE%AA%E7%8E%AF%E5%AF%BC%E5%85%A5%E7%9A%84%E5%A4%84%E7%90%86)
   5. [类型自动匹配](#%E7%B1%BB%E5%9E%8B%E8%87%AA%E5%8A%A8%E5%8C%B9%E9%85%8D)
6. [WebUI](#WebUI)
   1. [为什么不用 Burp / Yakit](#%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%8D%E7%94%A8-Burp-Yakit)
   2. [四栏布局](#%E5%9B%9B%E6%A0%8F%E5%B8%83%E5%B1%80)
   3. [实时推送](#%E5%AE%9E%E6%97%B6%E6%8E%A8%E9%80%81)
   4. [代码结构](#%E4%BB%A3%E7%A0%81%E7%BB%93%E6%9E%84)
7. [流量分析](#%E6%B5%81%E9%87%8F%E5%88%86%E6%9E%90)
   1. [服务调用分布](#%E6%9C%8D%E5%8A%A1%E8%B0%83%E7%94%A8%E5%88%86%E5%B8%83)
   2. [双通道通信模型](#%E5%8F%8C%E9%80%9A%E9%81%93%E9%80%9A%E4%BF%A1%E6%A8%A1%E5%9E%8B)
      1. [InteractionUpdate 完整类型](#InteractionUpdate-%E5%AE%8C%E6%95%B4%E7%B1%BB%E5%9E%8B)
   3. [代码仓库云索引同步](#%E4%BB%A3%E7%A0%81%E4%BB%93%E5%BA%93%E4%BA%91%E7%B4%A2%E5%BC%95%E5%90%8C%E6%AD%A5)
      1. [Merkle 树增量同步](#Merkle-%E6%A0%91%E5%A2%9E%E9%87%8F%E5%90%8C%E6%AD%A5)
      2. [文件增删改同步](#%E6%96%87%E4%BB%B6%E5%A2%9E%E5%88%A0%E6%94%B9%E5%90%8C%E6%AD%A5)
      3. [路径加密](#%E8%B7%AF%E5%BE%84%E5%8A%A0%E5%AF%86)
      4. [文件内容与隐私](#%E6%96%87%E4%BB%B6%E5%86%85%E5%AE%B9%E4%B8%8E%E9%9A%90%E7%A7%81)
      5. [索引配置](#%E7%B4%A2%E5%BC%95%E9%85%8D%E7%BD%AE)
      6. [与 AI 对话的关系](#%E4%B8%8E-AI-%E5%AF%B9%E8%AF%9D%E7%9A%84%E5%85%B3%E7%B3%BB)
   4. [RunSSE 通信格式分析](#RunSSE-%E9%80%9A%E4%BF%A1%E6%A0%BC%E5%BC%8F%E5%88%86%E6%9E%90)
      1. [请求格式](#%E8%AF%B7%E6%B1%82%E6%A0%BC%E5%BC%8F)
      2. [响应格式](#%E5%93%8D%E5%BA%94%E6%A0%BC%E5%BC%8F)
      3. [Streaming 特性](#Streaming-%E7%89%B9%E6%80%A7)
      4. [System Prompt](#System-Prompt)
   5. [BidiAppend 数据格式](#BidiAppend-%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F)
      1. [数据结构](#%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)
   6. [工具调用详解](#%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8%E8%AF%A6%E8%A7%A3)
   7. [服务端执行通道 (execServerMessage)](#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E6%89%A7%E8%A1%8C%E9%80%9A%E9%81%93-execServerMessage)
   8. [KV 存储机制](#KV-%E5%AD%98%E5%82%A8%E6%9C%BA%E5%88%B6)
      1. [完整的请求-响应结构](#%E5%AE%8C%E6%95%B4%E7%9A%84%E8%AF%B7%E6%B1%82-%E5%93%8D%E5%BA%94%E7%BB%93%E6%9E%84)
      2. [请求-响应匹配](#%E8%AF%B7%E6%B1%82-%E5%93%8D%E5%BA%94%E5%8C%B9%E9%85%8D)
      3. [完整的 KV 交互流程](#%E5%AE%8C%E6%95%B4%E7%9A%84-KV-%E4%BA%A4%E4%BA%92%E6%B5%81%E7%A8%8B)
      4. [Blob 数据内容](#Blob-%E6%95%B0%E6%8D%AE%E5%86%85%E5%AE%B9)
      5. [云端 KV 与客户端 KV](#%E4%BA%91%E7%AB%AF-KV-%E4%B8%8E%E5%AE%A2%E6%88%B7%E7%AB%AF-KV)
      6. [用户消息的两种发送方式](#%E7%94%A8%E6%88%B7%E6%B6%88%E6%81%AF%E7%9A%84%E4%B8%A4%E7%A7%8D%E5%8F%91%E9%80%81%E6%96%B9%E5%BC%8F)
      7. [BidiAppend 消息类型](#BidiAppend-%E6%B6%88%E6%81%AF%E7%B1%BB%E5%9E%8B)
   9. [对话检查点](#%E5%AF%B9%E8%AF%9D%E6%A3%80%E6%9F%A5%E7%82%B9)
      1. [消息组装流程](#%E6%B6%88%E6%81%AF%E7%BB%84%E8%A3%85%E6%B5%81%E7%A8%8B)
   10. [AI 向用户提问](#AI-%E5%90%91%E7%94%A8%E6%88%B7%E6%8F%90%E9%97%AE)
   11. [完整对话时间线](#%E5%AE%8C%E6%95%B4%E5%AF%B9%E8%AF%9D%E6%97%B6%E9%97%B4%E7%BA%BF)
   12. [代码补全 (StreamCpp)](#%E4%BB%A3%E7%A0%81%E8%A1%A5%E5%85%A8-StreamCpp)
       1. [补全配置 (CppConfig)](#%E8%A1%A5%E5%85%A8%E9%85%8D%E7%BD%AE-CppConfig)
   13. [Subagent 机制](#Subagent-%E6%9C%BA%E5%88%B6)
   14. [对话摘要机制](#%E5%AF%B9%E8%AF%9D%E6%91%98%E8%A6%81%E6%9C%BA%E5%88%B6)
   15. [Skills 系统](#Skills-%E7%B3%BB%E7%BB%9F)
   16. [用量限制](#%E7%94%A8%E9%87%8F%E9%99%90%E5%88%B6)
   17. [指标上报](#%E6%8C%87%E6%A0%87%E4%B8%8A%E6%8A%A5)
       1. [用户行为事件 (Batch)](#%E7%94%A8%E6%88%B7%E8%A1%8C%E4%B8%BA%E4%BA%8B%E4%BB%B6-Batch)
   18. [模型选择](#%E6%A8%A1%E5%9E%8B%E9%80%89%E6%8B%A9)
   19. [补全结果追踪 (RecordCppFate)](#%E8%A1%A5%E5%85%A8%E7%BB%93%E6%9E%9C%E8%BF%BD%E8%B8%AA-RecordCppFate)
   20. [AI 生成 Git 提交消息 (WriteGitCommitMessage)](#AI-%E7%94%9F%E6%88%90-Git-%E6%8F%90%E4%BA%A4%E6%B6%88%E6%81%AF-WriteGitCommitMessage)
   21. [Feature Flag 系统 (BootstrapStatsig)](#Feature-Flag-%E7%B3%BB%E7%BB%9F-BootstrapStatsig)
   22. [自动 Tab 命名 (NameTab)](#%E8%87%AA%E5%8A%A8-Tab-%E5%91%BD%E5%90%8D-NameTab)
   23. [@Docs 文档索引 (AvailableDocs)](#Docs-%E6%96%87%E6%A1%A3%E7%B4%A2%E5%BC%95-AvailableDocs)
   24. [服务端全局配置 (GetServerConfig)](#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E5%85%A8%E5%B1%80%E9%85%8D%E7%BD%AE-GetServerConfig)
   25. [隐私模式 (PrivacyMode)](#%E9%9A%90%E7%A7%81%E6%A8%A1%E5%BC%8F-PrivacyMode)
8. [结语](#%E7%BB%93%E8%AF%AD)

Toc

**0** results found
![](/images/logo.jpeg)

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

白帽酱

白帽酱

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

Cursor 逆向笔记 1 —— 我是如何拦截解析 Cursor 的 gRPC 通信流量的

2026/01/31

[AI](/categories/AI)
[WEB](/categories/WEB)

[逆向](/tags/%E9%80%86%E5%90%91)
[Cursor](/tags/Cursor)
[AI](/tags/AI)
[MITM](/tags/MITM)
[gRPC](/tags/gRPC)
[SSE](/tags/SSE)
[protobuf](/tags/protobuf)

# 前言

某天我在打算自己写一个安全agent。为了学习一下Cursor的成熟流程，想搞清楚它到底给模型发了什么东西。

结果发现 Cursor 这里藏了一个黑盒。你以为你配了自定义 API，请求应该直接走你的 endpoint，实际上它还是会按 Cursor 自己的协议组包，经过 Cursor 的服务器转发出去。也就是说，不管你怎么配，流量都要先过它一手。

那这事就有意思了。如果我能把它的请求和响应完整抓出来，就等于把这个黑盒的前端拆开了一半。

本文记录整个折腾过程。最终目标是在不中断 Cursor 正常使用的前提下，完整解密 TLS 流量，从压缩打包好的js文件还原protobuf结构，识别并解析 gRPC 和 Connect Protocol 通信，最后做一个 WebUI 用来检索和回放流量。

* 本文章中的涉及到的全部代码都已经在github上公开 <https://github.com/burpheart/cursor-tap>

# 从 Burp 开始，然后被 CA 打脸

最开始的想法很简单。BurpSuite 或者 Yakit 这种开箱即用的 HTTPS 代理，开起来把系统代理指过去就完事了。几百年前就有的成熟方案，没什么技术含量。

打开 Burp，导出 CA 证书，双击安装到系统根证书存储。设置系统代理指向 127.0.0.1:8080。启动 Cursor。

然后 Cursor 直接报证书不信任。

这一步其实很常规，但 Cursor 这类 Electron/Node 应用有它自己的一套证书验证机制。Electron 应用的网络请求走的是 Chromium 内核，理论上应该读系统证书库，但实际情况比这复杂得多。

首先试了最基础的方案：把 Burp 的 CA 证书导入 Windows 的「受信任的根证书颁发机构」。重启 Cursor，还是不信任。

最后发现 Node.js 有个 `NODE_EXTRA_CA_CERTS` 环境变量，可以指定额外的 CA 证书文件路径。把 Burp 的 CA 证书导出为 PEM 格式，设置环境变量指向这个文件，重启 Cursor，终于过了。

|  |
| --- |
| ``` # Windows set NODE_EXTRA_CA_CERTS=C:\path\to\burp-ca.pem  # Linux/macOS export NODE_EXTRA_CA_CERTS=/path/to/burp-ca.pem ``` |

CA 的问题解决之后，又出来一个更恶心的坑。

# SSE 把 IDE 卡死了

用 Burp 抓包的时候，Cursor 的agent会一直卡住。一开始我以为是自己代理配置的问题，后来才发现问题出在 SSE 上。

Cursor 有一类 streaming 流量，Content-Type 写的是 `text/event-stream`，看起来像是标准的 Server-Sent Events。但实际上它根本不是在传 SSE 文本事件。

它利用了一个现实世界里的工程事实：很多中间件、代理、调试工具看到 `text/event-stream` 这个 Content-Type 会倾向于不缓存、不聚合、直接转发。于是 Cursor 借这个头建立了一个无缓冲的长连接，然后在这个连接里塞二进制流。

所以用 Burp 或者 Yakit 这种对流量会有加工处理的工具去抓，很容易出问题。要么代理对流做了缓冲和阻塞导致看不到实时数据，要么直接把 Cursor 的流式通道搞挂，Cursor 等不到数据界面就各种抽风。

到这里我就意识到不能再用传统拦 HTTP 的方式了。得自己写一个不阻塞的中间人。

# 自己写 SSL 中间人

目标很明确：代理层必须零阻塞，能稳定转发所有流量。同时要能拿到 TLS 会话密钥方便 Wireshark 解密。最好还能把流量记录下来给后面的 WebUI 用。

## MITM 的核心原理

SSL/TLS 中间人的本质是「两段 TLS」。客户端以为自己在和真正的服务器握手，实际上握手对象是中间人。中间人再和真正的服务器建立另一个 TLS 连接。两边的加密是独立的，中间人能看到明文。

|  |
| --- |
| ``` Cursor ←─TLS─→ MITM Proxy ←─TLS─→ api2.cursor.sh          ↑                    ↑     假证书(我们签的)      真证书(Let's Encrypt) ``` |

关键在于让客户端信任中间人签发的「假证书」。这就是为什么前面要折腾 `NODE_EXTRA_CA_CERTS`——把我们的 CA 加到 Cursor 的信任列表里。

## 动态证书签发

不能提前准备好所有域名的证书，因为你不知道 Cursor 会连哪些 host。必须在运行时动态签发。

流程是这样的：客户端发起 HTTPS 请求，代理收到 `CONNECT api2.cursor.sh:443` 后，先不急着握手。用 `Peek` 偷看客户端发来的 TLS ClientHello，从里面提取 SNI（Server Name Indication）字段，这个字段告诉我们客户端想连的是哪个域名。

|  |
| --- |
| ``` // internal/mitm/detect.go func extractSNI(reader *bufio.Reader) (string, error) {     // Peek 前 5 字节，拿到 TLS record header     header, _ := reader.Peek(5)     //...