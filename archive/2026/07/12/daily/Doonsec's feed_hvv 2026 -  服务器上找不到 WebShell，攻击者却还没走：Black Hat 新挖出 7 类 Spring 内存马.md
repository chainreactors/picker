---
title: hvv 2026 -  服务器上找不到 WebShell，攻击者却还没走：Black Hat 新挖出 7 类 Spring 内存马
url: https://mp.weixin.qq.com/s/bvlic2gZPzWGYpmsDvN4WA
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:26:49.457292
---

# hvv 2026 -  服务器上找不到 WebShell，攻击者却还没走：Black Hat 新挖出 7 类 Spring 内存马

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMBibLCUnOaSGPw4NA17PQjVQZo4BTAic5waNjnxE6DA7Z9RHIdlxQ1e8ia2xXW1lnCqnVQUPMlxG8zc6qhLf61lUwCbOBeic4NbRq4/0?wx_fmt=jpeg)

# hvv 2026 - 服务器上找不到 WebShell，攻击者却还没走：Black Hat 新挖出 7 类 Spring 内存马

原创

messfree
messfree

MessFreeSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

护网应急里有一种很危险的“处置完成”：服务器上发现了可疑 JSP，文件删掉了，Web 目录重新扫了一遍，没有新增文件，工单于是写上——WebShell 已清理。

但 JVM 内存马本来就不需要 JSP。

它只需要借一次已经存在的代码执行机会，把 Spring 或 Tomcat 正在使用的某个运行时对象换掉。后面的请求继续走 80/443，URL 可以是正常业务路径，磁盘上也不必留下新的 WebShell 文件。只要 JVM 进程还在、那个对象还活着，被修改的请求处理链就可能继续工作。

今年 Black Hat Asia 上有份 29 页的材料，《JVM Memory Shell Auto Searching Program》。研究团队在已知 2 类 Spring 内存马的基础上，又验证了 7 类新的家族，总覆盖达到 9 类。

但我看完之后觉得，真正值得蓝队警惕的不是“又多了 7 个名字”。

是内存马发现这件事，正在从少数研究员靠经验翻源码，变成一条可以反复运行的流水线：先用 SAST 压缩候选面，再用 Java Agent 和真实流量证明候选对象会被触发；从 JVM 对象关系里搜索反射可达路径，最后让 AI 在真实源码、精确签名和运行证据的约束下补齐候选 PoC，再重新编译、部署、人工确认。

**以后框架每升级一次，攻击者和防守方都可以把这条流水线再跑一遍。**

先讲内存马为什么删不掉，再拆这 29 页是怎么把 7 类新入口挖出来的。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMCibDX0L1k05PYTAZyboCYRlu72ia2YKdxibgiavXR8ZfP4icFnsUjO7f2tRibqPt6HAQOvMDdrrw8ibzfck0z2vOqTmRllb85y6R55d8/640?wx_fmt=png&from=appmsg)

*图：Black Hat Asia 2026《JVM Memory Shell Auto Searching Program》原版议题页。*

两位作者的背景也解释了这套方法为什么同时带着攻防视角：Wan Litong 长期从事 Java 应用安全与漏洞利用研究，Yu Fanghai 则有 SAST 引擎和 RASP 防护经验。整份材料不是单纯发布几个攻击样例，而是在尝试把研究和防守验证做成同一条工程流水线。

---

## 先说清楚：内存马不是“藏在内存里的 JSP”

传统 JSP WebShell 的逻辑比较直观：攻击者把文件写进 Web 目录，容器加载并执行。防守方可以盯文件创建、哈希、目录变更、敏感 API，也可以直接在磁盘上把它找出来。

JVM 内存马换了一个思路。它不一定新增一个可见文件，而是改变当前进程里的对象、组件注册表、请求映射或者已加载字节码。

报告给出的典型前提是：攻击者已经通过反序列化、表达式注入、脚本引擎或其他漏洞获得了一次 Java 代码执行能力。随后再利用反射、动态注册或 Java Instrumentation，把恶意逻辑挂到 Java Web 框架的请求处理链上。

这两步不能混为一谈：

1. **初始漏洞负责让攻击者进入 JVM；**
2. **内存马负责把一次性的代码执行变成更隐蔽、更稳定的后续入口。**

所以内存马本身通常不是“无需前置条件的远程漏洞”。没有初始代码执行、没有足够的进程内权限，就不能凭空修改 Spring 的运行时对象。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMDzsCTxib8iciaOeibR467Jkea8DuSsylrqIfElh87PgZbVQ28NtV5g4V3GpCr7UvicZTnSA4O1GcyNQPmGPtXibHpXeqd9O5th45QLw/640?wx_fmt=png&from=appmsg)

*图：PPT 将 JVM 内存马概括为无文件落地、流量隐蔽，以及复用正常 HTTP 端口。*

经典的 Tomcat Filter 内存马最适合解释这个模型。

Filter 原本是正常的 Servlet 组件，用来在业务处理前后做认证、日志、编码、跨域等工作。攻击者获得代码执行后，通过反射进入 Tomcat 的 `StandardContext`，动态塞入一个恶意 Filter，再调整 `FilterMap` 顺序，让它比正常 Filter 更早接触请求。

此后，新的请求不需要访问某个 JSP 文件。它只要进入这条 Filter Chain，就会先经过攻击者控制的对象。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMB6sarhGCkQGiczpO6BEyIDxtb6RsA4zH4CBAMh2tmkiaLwBXXhf3nN0iadr481h3yRWbrNNoukAzfLd3JECwZRUDAiaEsSYO3z8t0/640?wx_fmt=png&from=appmsg)

*图：经典 Filter 内存马修改的是请求处理链，而不是简单写入一个 JSP 文件。*

一句话概括：

**内存马不是把 WebShell 文件搬进内存，而是把应用原本信任的一段处理链，换成攻击者控制的对象。**

这也是为什么“JSP 已删除”和“后门已消失”之间没有等号。

不过也要补一个边界：纯内存对象通常会随着干净的 JVM 进程退出而消失。如果攻击者另外留下了启动项、恶意 Agent、修改后的 JAR、计划任务或仍可利用的初始漏洞，它才可能在重启后被重新注入。因此，**只删文件不够，只重启也不够**：前者清不掉现存对象，后者如果没封入口，攻击者还能再打一遍。

---

## 现有检测为什么总是慢一拍

PPT 第 8～11 页回顾了这条技术的演进：从早期 Java Timer 和“删掉 JSP 后代码仍在运行”的概念，到 Tomcat Filter、Servlet、Listener，再到 Spring Controller、Interceptor、WebSocket，以及冰蝎、哥斯拉等工具链集成。

类型越来越多，防守也逐渐形成两条路线。

第一条是 **注入时拦截**。RASP 沿初始漏洞的调用栈往后看，监控 `defineClass`、动态注册、字节码修改等敏感行为，再根据调用来源和注入类特征决定是否阻断。

第二条是 **驻留后扫描**。枚举 JVM 已加载类，寻找“内存中存在、磁盘上找不到对应 Class/JAR”的对象，把可疑字节码 Dump 出来，再匹配已知 Filter、Servlet、Listener 或工具特征。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMC6mGGeM1j8iaUiaZP3MKbfM04pC5icMR9gwwt6iarDTaIYTjmR2Br0U1xdd9PQZhib7W6Qk9h0KVKt9ULh0JdYVBhLqIf9WaVmdlWg/640?wx_fmt=png&from=appmsg)

*图：驻留检测通常从已加载类、磁盘来源和已知字节码模式入手。*

这些方法不是没用。对常见内存马，它们非常重要。

问题在于，它们很容易围绕“已经见过的内存马”建立规则：熟悉的接口、熟悉的注册位置、熟悉的类结构、熟悉的 Header 和加密流量。如果攻击者不再注册一个显眼的 Filter，而是替换 Spring 本来就会持有和调用的标准组件，老规则就可能失焦。

另一方面，新类型过去主要靠研究员手工翻 Spring、Tomcat 源码。Filter、Listener、Controller 这些明显的请求入口被研究多年以后，继续人工寻找的投入越来越大，回报却越来越不确定。

**两年没出现新类型，不一定说明框架里没有新入口。也可能只是人已经翻不动了。**

---

## 转折点：一个 FlashMapManager 改变了搜索思路

研究团队先手工发现了一类 FlashMap 内存马。

`FlashMap` 是 Spring MVC 用来在两次请求之间暂存属性的机制，常见场景是 Post/Redirect/Get。`DispatcherServlet` 内部持有一个 `FlashMapManager`，在处理映射给它的 MVC 请求时，会调用 `retrieveAndUpdate(request, response)` 取出并清理相应状态。

研究者的思路不是再注册一个 Controller，而是沿 JVM 工作线程、Tomcat 内部对象和 Spring 上下文进行多层反射，找到 `DispatcherServlet` 当前使用的 `flashMapManager`，再用一个保留原有接口的恶意实现替换它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMCiap4rv6ngGJicRvCWqI748KLTg7kvMWvf2fnmcpGaiclx0Zy7zQOm9zBwhUsichpjibwgpc579L6mHAJcKjgGsgiaSRCnSCeIHzDO0/640?wx_fmt=png&from=appmsg)

*图：FlashMap 家族展示了“替换标准组件”这条路线，而不只是动态注册新的请求入口。*

为什么这个点重要？

因为 `FlashMapManager` 是标准组件，接口稳定，又处在 MVC 请求处理的早期阶段。只要恶意实现继续调用原逻辑，业务表面上可能仍能工作；攻击逻辑则可以藏在组件被调用的那一瞬间。

PPT 把它概括为“每个 HTTP 请求、认证前触发”。更严谨地说，它覆盖的是进入相应 `DispatcherServlet` 映射的请求；外层 Servlet Filter——包括常见的 Spring Security Filter Chain——可能早已执行，因此不能笼统写成“绕过所有认证”。实际顺序取决于部署和安全链配置。

真正的启发不是 FlashMap 本身，而是研究者从中抽象出了三项共同特征：

1. 目标是 Spring 的标准组件，最好有标准接口，替换后仍能维持业务逻辑；
2. 目标类型可被构造或继承，例如是 `public`、非 `final`；
3. 目标对象确实处在请求或关键运行路径上，能够稳定触发。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMDKCPcTrGbpuhhUtrqBfcicDPEmAiaOsicPib1K0NseyicrWIHrhlwhJzKRQMkPiaMV1DrZblH3y7joX7bTTmcUibhzBobCexg7pgyic0w/640?wx_fmt=png&from=appmsg)

*图：研究目标从“再找一个 Filter”转成“寻找可替换、会触发、又不会立刻破坏业务的标准组件”。*

问题于是被重新定义：

> Spring MVC 里，还有哪些对象既能被替换，又会在真实请求中运行，并且替换后不会马上把应用打挂？

一旦问题变成结构特征，就可以自动化了。

---

## 四段流水线：不是直接让 AI 去“找内存马”

这套系统的整体链路可以压缩成四段：

```
Spring 源码 / JAR        ↓SAST 静态分析：压缩出候选组件        ↓Java Agent + HTTP 流量：证明候选真的会运行        ↓JVM 对象搜索：找到从线程到目标对象的可达路径        ↓AI 基于源码、签名和运行证据合成候选 PoC        ↓重新编译、部署、触发、人工确认
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMDqGEWYQO7iczrSWKVMa1gaqyYfgcE2RXExNeg26X5p3U6htXdMLwtkWlzia6Wnp4Y8qGxwXfRuTxFsGoicVQicRwPnS6wX31HqaBw/640?wx_fmt=png&from=appmsg)

*图：内存马是运行时实体，所以研究团队用 Java Agent 和测试流量把“看起来可疑”变成“确实被触发”。*

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMBlPYgiaFUv4FJk0ibSYpPicK8GfwyzmZTKo6fxYia2ycVt7dPLjc0N7y6osiasUPX39otuaI4Y971rDMRFLnqnPJsgUxgHnxDFLug4/640?wx_fmt=png&from=appmsg)

*图：静态筛选、动态验证、内存搜索、AI 合成和人工确认组成完整闭环。*

这里有两个很重要的“不是”。

**SAST 不是直接判定漏洞。** 它只负责把 Spring 巨大的代码面压缩成值得继续观察的候选池。

**AI 也不是在自由发挥。** 到它出场时，前面的模块已经提供了候选类、精确方法签名、真实调用栈、堆内对象路径和反编译源码。AI 更像是在证据围栏里完成最后一公里的代码拼装。

---

## 第一层：SAST 找的不是 `Runtime.exec`，是“哪些对象可以被换掉”

传统恶意代码扫描喜欢找危险函数、命令执行、硬编码密钥或已知恶意字符串。但这项研究在静态阶段并不寻找最终恶意行为。

它寻找的是一种结构画像：

* 类是 `public`，不是 `final`、`abstract` 或匿名类；
* 位于 Spring 相关命名空间，排除 `java.*`、`javax.*`、`sun.*` 等噪声；
* 对象会被实例化，并作为另一个长期对象的字段持有；
* 这个字段不只是存在，后续确实会调用它的方法；
* 更聚焦的查询还会观察方法参数是否出现 Request、Response 等请求相关类型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMCBpK8ticwOic6iaTr3IRtOzSoNygR1g9ibb0Dbbic45ZcoYU5lEnz7fNq977iaoR9OVrZDETH7ZhRKhHhO0PQzUZpRG3fIpk8upak54/640?wx_fmt=png&from=appmsg)

*图：可扩展、被长期持有、处于调用链上，是比恶意字符串更稳定的候选特征。*

用蓝队熟悉的话说，它问的不是“这段代码现在是不是木马”，而是：

**这个对象能不能被换掉？换掉之后，框架会不会继续主动调用它？**

CodeQL 把这些关系建成语义查询，最终得到类、字段、持有者、被调用方法等结构化结果。

但静态分析仍然有大量噪声。PPT 给出的数字是 374 条去重候选记录，其中包含 `FlashMapManager`、`SimpleApplicationEventMulticaster`、`MultipartResolver` 等已知或潜在位置。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMD4ibicaQXLFuZd5ic17M3oBcPRQfqMtETYGeQOKuY81GKDmyBz9zLuSiajDZ6jMCoKibiaCua5CAicmXrdJvPEL9YlYTWnaRz93yDFUA/640?wx_fmt=png&from=appmsg)

*图：374 是待验证候选，不是 374 个漏洞，更不是 374 类内存马。*

有些对象只在应用启动时出现，有些属于测试路径，有些虽然可替换，却根本不会接触业务请求。静态结构只能证明“像入口”，不能证明“能成为稳定入口”。

**SAST 在这里像漏斗，不像法官。**

---

## 第二层：Java Agent 让候选对象在真实流量里自证

下一步，研究团队把 SAST 产出的候选方法做成 Hook 规则，通过 Java Agent 加载到测试 JVM 中，然后重放正常 HTTP 流量。

候选方法如果在真实请求中被调用，就留下运行证据；始终不触发，或者只出现在启动和无关流程里的，就继续降级或丢弃。

Agent 同时支持两种模式：

* `premain`：JVM 启动时加载；
* `agentmain`：进程运行后动态 Attach。

它还把自身追加到 Bootstrap ClassLoader 的搜索路径，并用统一的 Transformer 管理 Hook 和断点规则，尽量降低容器类加载隔离带来的影响。

每次命中不只记一个“方法被调用”。系统还记录：

* 类名、方法名；
* 谁持有这个对象、字段叫什么；
* 参数摘要；
* 调用栈和线程；
* 可选的对象引用关系。

到这里，候选已经从“源码结构上像入口”，升级成：哪条流量触发了它、在哪个线程执行、谁持有这个对象、调用栈从哪里来的运行时证据。

对蓝队来说，这一段也很有启发：同样的动态观测可以反向用于建立 Spring 核心组件基线。但不能简单把“加载了 Java Agent”直接判恶——APM、性能诊断、热修复、RASP 和测试工具也会使用 Instrumentation。真正应该关联的是 Agent 来源、Attach 时间、目标进程、修改类、调用栈和之后的异常行为。

---

## 第三层：会被调用还不够，攻击者还要走得到那个对象

一个方法会在请求里触发，不代表攻击者就能修改它。

内存马成立还差一个关键问题：在只有当前 JVM 执行上下文的情况下，怎样找到那个已经被 Spring 创建、持有并反复使用的对象实例？

研究团队把 JVM 对象搜索器嵌进 Java Agent。在断点命中时，从 `Thread.currentThread()` 这个运行时锚点出发，对当前可达对象图执行受限 BFS，寻找名称包含 Request、Response、Session 或目标框架组件的对象，同时排除无价值或风险较高的类型。

PPT 给出的一个示例路径有 7 跳：

```
Thread.currentThread()
  → ThreadGroup
  → threads[]
  → NioEndpoint$Poller
  → NioEn...