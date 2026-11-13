---
title: Java内存马如何排查？
url: https://mp.weixin.qq.com/s/SahY3Ge6_zlS4lWfy5xq2g
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:04:22.785392
---

# Java内存马如何排查？

# Java内存马如何排查？

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

Java内存马如何排查？

导读 · CONTENTS

01前景回顾--Java内存马分类

02如何上传内存马？

03Java 内存马排查：日志、JSP 扫描、Arthas 与自动化工具

04 Java 内存马分析与清除：从可疑类到运行时组件

⚠️ 免责声明：本文所涉技术与工具仅限授权环境下的安全排查与防御研究。请勿用于非法用途。在生产环境执行任何动态 Attach、内存 Dump 或卸载操作前，务必做好证据保全与回滚准备。

01

前景回顾--Java内存马分类

JAVA

网上都将内存马分为以下类别：传统 Web 应用型、框架型、中间件型、其他中间件型和 Agent 型。但这种分类能帮助入门，但存在交叉：例如 Tomcat Filter 既是容器组件型，也可能通过动态注册实现；Agent 则更多描述实现机制，而不是某个固定的请求入口。为了排查时不漏项，建议从三个维度理解。

网上内存马分类

![](https://mmbiz.qpic.cn/mmbiz_jpg/qkajCoyKpkBViclY2UG4HoBxuWOYZA7OnNFfAgRibYDVlnibeuz6ffw8tZfTRE7ktbjJ4d3dITqlia5FuRb1ibCnH3YfjpEyDlPequC4U3iaibGSKk/640?wx_fmt=jpeg&from=appmsg)网上内存马分类

按运行时挂载位置分类

| 类别 / 类 | 核心机制 | 排查关注点（专业版） | 排查关注点（小白版） |
| --- | --- | --- | --- |
| Servlet 型 | 动态注册 Servlet，并建立 URL 映射 | ServletMapping、Servlet 实例、URL pattern、load-on-startup、对应类来源和 service 方法 | 动作：看 URL 映射表。找：有没有多出来的、你没配过的 URL（比如 /api/hack），或者类名很奇怪的 Servlet 实例。 |
| Filter 型 | 动态注册 Filter，并加入过滤器链 | FilterMap、FilterConfig、URL pattern、Dispatcher 类型、过滤顺序、doFilter 逻辑 | 动作：看过滤器链。找：应用启动时，系统原本应该只有 3 个 Filter，现在跑出来 4 个。看新多出来的那个类的 doFilter 方法，里面是不是在偷看请求参数。 |
| Listener 型 | 动态注册监听器，响应应用、会话或请求生命周期事件 | 监听器列表、接口类型、注册时间、是否执行异常文件/命令/网络操作 | 动作：看监听器列表。找：正常监听器只在系统启动时打印几行日志，如果某个监听器一启动就去连外部 IP 或偷偷写文件，直接拿下。 |
| Tomcat Valve 型 | 向 Engine / Host / Context 等 Pipeline 添加 Valve | Pipeline 中的 Valve 列表、前后顺序、invoke 方法和非预期代理对象 | 动作：检查 Tomcat 的 Pipeline 管道。找：Tomcat 默认只有 StandardEngineValve，如果出现自定义的 Valve 类，且名字在源码里搜不到，盯紧它。 |
| Spring Controller 型 | 运行时向 HandlerMapping 注册处理器与映射 | RequestMappingHandlerMapping、mappingRegistry、路径和方法、控制器实例与代码来源 | 动作：看业务映射表。找：去 Spring 的 HandlerMapping 里翻，有没有不认识的 Controller 在被调用。 |
| Spring Interceptor 型 | 动态添加 HandlerInterceptor | adaptedInterceptors、拦截路径、preHandle / postHandle / afterCompletion 行为 | 动作：看拦截器列表。找：看拦截器的 preHandle 方法，是不是在拦截特定带有 cmd 参数的请求。 |
| WebFlux / WebFilter 型 | 注册 WebFilter、WebHandler、HandlerFunction 等响应式处理链 | WebFilter 链、HandlerMapping、WebHandler、Reactor Netty pipeline | 动作：看响应式过滤器链。找：排查 WebFilter 列表中是否有异常的响应式处理类。 |
| WebSocket 型 | 注册 WebSocket Endpoint 或消息处理器 | Endpoint 注册表、路径、握手与消息回调、连接来源和消息内容 | 动作：看连接端点。找：检查系统是不是建立了非预期的 WebSocket 连接，通常黑客用它来搞交互式命令执行。 |
| Netty Handler 型 | 向 ChannelPipeline 插入 ChannelHandler 或修改 pipeline 配置 | Pipeline 前后节点、Handler 顺序、注册时机、异常转发或隧道行为 | 动作：看 ChannelPipeline。找：中间件底层被插了 Handler，只要网络有数据进出，都要经过它，查异常的网络转发逻辑。 |

按运行时修改机制分类

| 实现机制 | 说明 | 检测思路（专业版） | 检测思路（小白版） |
| --- | --- | --- | --- |
| 动态类加载 / 动态定义 | 通过 ClassLoader 等机制将字节码加载进当前 JVM | 检查类加载器、CodeSource、类的生成时间、字节码、类与磁盘产物是否一致 | 用 Arthas 查可疑类的来源（CodeSource），如果发现来源是空的（null）或在临时目录等非正常路径，就是马。 |
| 运行时注册组件 | 把新对象添加到容器或框架维护的注册结构 | 直接检查 Filter、Servlet、Valve、HandlerMapping、WebSocket 等运行时注册表 | 用扫描器或 Arthas 列出所有组件，如果发现多出未知的 Filter/Servlet 或绑定了奇怪的 URL（如 /cmd），就是马。 |
| Java Agent / Instrumentation | 通过 Agent、Instrumentation、ClassFileTransformer 等技术增强或改写方法 | 检查已加载 Agent、Transformer、类字节码变化、关键方法调用链和进程启动参数 | 用 jps -lv 查进程参数或对比内存与磁盘代码，如果发现陌生的 -javaagent 参数或代码被篡改，就是马。 |
| 动态代理 / 反射 Hook | 包装或替换已有组件、方法调用目标或管线对象 | 检查代理对象、被替换字段、调用链、对象实际类型及代理 InvocationHandler | 用 Arthas 反编译带 $Proxy 的代理类，如果发现它在偷偷拦截请求并执行危险指令，就是马。 |
| 线程 / 定时任务驻留 | 创建后台线程、TimerTask 或其他异步执行对象 | 检查异常线程名、线程栈、目标 Runnable、TimerTask 和周期性网络活动 | 用 thread 命令或网络监控查后台，如果发现名字奇怪且疯狂对外连接的线程，就是马。 |

其他类型

| 实现机制 | 说明 | 检测思路（专业版） | 检测思路（小白版） |
| --- | --- | --- | --- |
| Executor / Poller / Upgrade | 替换底层线程池、连接器执行器或处理 HTTP Upgrade 的对象，影响全局请求路径。 | 检查核心组件源码，排查线程池配置及 Upgrade 处理器是否被非法替换。 | 用 Arthas 查 Tomcat 内部执行器类，如果发现未知对象接管了请求分发，或 WebSocket 升级请求被劫持，就是马。 |
| 线程型 / Timer 型 | 恶意逻辑不依赖 URL，由后台线程或定时任务触发，常被用作“复活机制”。 | 排查线程名、线程栈和任务对象，必须与正常的线程池、调度框架做对比。 | 用 thread 命令或 top 查后台，如果发现名字乱码、一直死循环、或规律性向外发包的线程，直接标红。 |
| RMI 型 | 动态启动 RMI Registry 或远程对象服务，形成独立的远程访问入口。 | 监控 JVM 运行时远程服务注册表，检查 RMI 绑定对象和非预期端口监听。 | 用 netstat 查端口监听，如果发现非预期端口被 java.exe 占用，或日志有异常反序列化请求，重点排查。 |
| JSP 相关动态类 | JSP 本身会在运行时编译为 Servlet 类，需区分正常编译和恶意注入。 | 核对 JSP 生成类是否对应磁盘实际文件、生成目录及访问记录。 | 用 Arthas 查 \_jsp 结尾的类，如果它在磁盘上找不到对应的源文件，或者访问记录异常，高度疑似内存马。 |
| Grizzly 等其他容器 | 非 Tomcat 的其他中间件，有自己特有的组件结构。 | 针对具体容器（如 Grizzly）分析其特定的 Filter Chain 或 Handler 结构。 | 别硬套 Tomcat 的查法，使用针对该容器的专用扫描器，或者查阅官方文档，查它特有的组件注册表。 |

02

如何上传内存马？

SECTION

第一层：常规操作

这是很多新手最爱用，也是目前最基础的植入方式。

1直接通过漏洞利用

攻击者发现了一个高危漏洞（比如文件上传、命令执行），直接通过这个漏洞向服务器发送恶意 Payload，瞬间完成内存马的注入。

特点：速度快，不需要落地其他文件，只要漏洞验证成功，马就进去了。

2先传普通webshell，再“二次加工”

这是非常经典的组合拳。攻击者先通过漏洞上传一个普通的木马文件（如 1.jsp），用工具（比如中国菜刀）连上之后，获得了基本的命令执行权限。然后再利用这个权限，通过脚本或插件，在内存里注册一个更隐蔽的内存马。

常见工具：哥斯拉（Godzilla）、冰蝎（Behinder） 都有现成的内存马注入插件，点一下按钮，马就进去了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDyKBA1JxQksIEpYCgomswfnlBVic0shSgEVTFfN0EGxCa6dib4GIl66AGyHl8SDBdowG6gYxqwsqm3eicCys1J1LdP3hNlSJVzxY/640?wx_fmt=png&from=appmsg)

植入普通木马

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDdNexYqfS71ngwIb3yKOZ8nQbsFuvfJ9WQNPAicH3kaDBqxia2gQSmBKAWREvP7V3nYLptjlbypbueiaFfsy7fqMxmUHujxbK7sc/640?wx_fmt=png&from=appmsg)

植入成功

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkAn856mWE5OGXoDpkfMric09nMnHE4TpmnzMAMe8Buz39rQK4afIezWPGl5p0qpxibljibYVR8OEmwvjuUn8jHGUJAx6PmTyKJ1Q4/640?wx_fmt=png&from=appmsg)

使用哥斯拉连接，测试连接成功

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCb90QZ2g32INkyuInaG77MUzQQmMb1OcxXn9hwGZpHvTDKicia2PROka282wLREajDmw17BnXsnOU8FDrRDRaxS9G2Kdaibq4RpI/640?wx_fmt=png&from=appmsg)

植入内存马

第二层：进阶操作（利用反序列化和表达式注入）

真正的高手，往往不屑于上传文件，他们更偏爱“借刀杀人”，利用应用本身的逻辑漏洞来注入。

1反序列化漏洞（最经典）

利用 Fastjson、Shiro、WebLogic 等组件的反序列化漏洞，构造一条恶意的利用链（Gadget Chain）。当服务器反序列化这个数据时，就会在不知不觉中执行攻击者的代码，把内存马加载进去。

2表达式/模板注入（SSTI）

利用 Spring 的 SpEL、或者是 FreeMarker、Thymeleaf 等模板引擎的漏洞。攻击者不需要上传任何文件，只需在输入框里输入一段恶意表达式，就能让服务器直接实例化恶意类，完成注入。

特点：这类攻击往往伴随着极高的技术门槛，且流量特征很难被传统 WAF 拦截，但对防守方来说，往往会在 Web 日志里留下极度异常的畸形请求。

第三层：底层魔法（Agent 动态附加）

这是目前最隐蔽、最高级的植入方式之一。

1Attach API 动态注入

攻击者在获得了服务器的执行权限后（比如通过弱口令、运维通道），使用 jattach 等工具，直接在外部向目标 Java 进程发送指令，动态加载一个恶意的 Agent 包。

2Instrumentation 改字节码

Agent 进去之后，利用 Instrumentation 接口，直接修改运行中代码的字节码。

特点：不新增任何组件！它不添加 Filter，也不添加 Servlet，而是直接把一个正常业务的代码逻辑给“替换”了。这种手法，一般的扫描器根本扫不出来，必须通过对比内存字节码和磁盘源码的差异才能发现。

第四层：暗度陈仓（供应链与凭据滥用）

这类手法属于“降维打击”，防不胜防。

1供应链投毒

攻击者入侵了上游的软件供应商，或者污染了开源组件（比如 npm、Maven 上的第三方包）。开发人员正常拉取依赖，结果系统一启动，恶意代码就自动注入内存了。

2运维凭据滥用

攻击者窃取了运维人员的 VPN 账号、或者服务器的后台管理权限。通过合法的管理通道，大摇大摆地走进去，利用 JMX 等接口直接向 JVM 注入恶意组件。

03

Java 内存马排查：日志、JSP 扫描、Arthas 与自动化工具

TOOLS

先摸清当前运行环境

不要一上来就运行工具。先回答四个问题：目标进程是什么、应用由什么容器承载、使用什么框架、运行时组件主要在哪里注册。

CODE

::
Windows

jps-lv

tasklist /fi "imagename eq java.exe"

netstat -ano

::
Linux

ps -ef|grep java

ss -lntp

上述命令用于确定进程、启动参数和监听端口。实际环境中还应核对服务管理器、systemd、容器编排平台和启动脚本中的进程关系。容器环境下，宿主机 PID 与容器内部 PID 可能不同，应确认工具运行在哪个命名空间。

日志排查：寻找“路由和行为不匹配”

POINT 1查看 Web 访问日志：关注异常 URI、非常规请求方法、长时间重复访问的路径、异常 User-Agent、来源 IP 和请求参数。

POINT 2把访问 URI 与正式路由清单对照，重点查看上线基线中没有出现、却持续返回 200 / 302 的路径。

POINT 3检查静态文件不存在但返回成功的情况，同时排除 SPA 前端路由回退、统一错误页、反向代理重写和认证跳转。

POINT 4将可疑请求时间与应用日志、认证日志、漏洞扫描告警、文件写入、进程命令执行和出站网络连接关联。

POINT 5注意隐藏入口不一定体现为新 URL。若攻击者 Hook 了已有 Filter、Valve 或 Controller，日志里可能只看到正常业务路径。

方法一：JSP 脚本扫描——java-memshell-scanner

项目地址：https://github.com/c0ny1/java-memshell-scanner

项目信息：通过JSP脚本扫描并查杀各类中间件内存马

POINT 1优点：使用简单，只需要把jsp文件放到网站目录即可

POINT 2缺点：功能少，只支持Filter和Servlet，不支持其他类型查杀（说是增加Listener型内存马检测，如果不存在Listener则不显示该项）

注意事项：

POINT 1把 JSP 放到网站目录，本身就会增加一个可访问的动态脚本入口。生产环境不要未经审批直接上传。

POINT 2如果确实要在生产环境使用，必须确认工具来源、代码内容、访问控制、部署位置和删除步骤，最好先在同版本隔离副本验证。

POINT 3扫描结束后移除扫描脚本，并检查访问日志、文件哈希和目录状态，避免把检测工具变成新的暴露面。

POINT 4它有覆盖范围限制，不能因为 JSP 扫描没有结果，就排除 Valve、Spring、WebFlux、Agent 或其他类型内存马。

使用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkA9T4MRvI2zVDvSiaswKpNhgjAhYPqHQr1Xy83jRmQ7qeVibyX7nj3Fn0W4W6qAKt6rLtUWbjMN2y3Nu8iaaQxKOdeagWNFoiaRCTE/640?wx_fmt=png&from=appmsg)

植入内存马之前

之后植入内存马：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCT9SLvm56seW2LDEMVEZL1pznxZhJYW6G14Fq5cu4um8MCA8UTqic5I1QyXQMlLjc2s3knw1TTPAS7p8efpEHcjTfyvmzoMnEw/640?wx_fmt=png&from=appmsg)

植入内存马

之后去刷新页面，发现内存马：

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDHGJTOD6geqRcvNAwLr7TXvlHCM50DOFHr8mKyOrzTLNEMQoRtYvBeS4g5qvNs62tFzvov4ZMTkAfqk5xStEhia2VkUjjRWDLo/640?wx_fmt=png&from=appmsg)

查看内存马

可下载内存马进行分析（这里没下载成功，不确定什么原因，因为功能有限，所以没去太深究），然后杀掉内存马

![](https://mmbiz.qpic.c...