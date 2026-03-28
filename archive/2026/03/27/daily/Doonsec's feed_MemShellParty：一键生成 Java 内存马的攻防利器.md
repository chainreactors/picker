---
title: MemShellParty：一键生成 Java 内存马的攻防利器
url: https://mp.weixin.qq.com/s/6tLA6vBQmTPrqcuUEDKp4Q
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:17:01.963570
---

# MemShellParty：一键生成 Java 内存马的攻防利器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0zk3Ye7cp00Q3vTaptdv20WHnr8X8yclyv6siczIzhqia8ibibRjsUgfOgAiarbtIFtMeGjS3ZdM9AlsO9SB0LPxibsbjWFXqUzeFLDt33ciazNRN8/0?wx_fmt=jpeg)

# MemShellParty：一键生成 Java 内存马的攻防利器

原创

攻防路
攻防路

攻防录

![]()

在小说阅读器中沉浸阅读

MemShellParty——一个可视化的 Java 内存马生成平台，选好中间件类型、Shell 功能和打包方式，点一下就出载荷。Tomcat、Jetty、WebLogic、WebSphere、东方通、宝兰德这些全覆盖，JDK6 到 JDK21 都能打。

截至 2026 年 3 月，这个项目在 GitHub 上已经拿到约 1.4k star，MIT 协议开源，当前版本 2.0.0。

项目地址：https://github.com/ReaJason/MemShellParty

在线体验：https://party.mem.mk

---

## 它解决了什么问题

做渗透测试或红队演练时，内存马注入是拿权限后维持访问的常用手段。但实际操作中痛点不少：

* 不同中间件注入方式完全不同，Tomcat 用 Valve、WebLogic 用 Filter、Jetty 用 Handler，每个都得单独研究
* JDK9+ 引入的模块系统（JPMS）把很多反射操作给限制了，载荷代码得做额外绕过
* 传统工具生成的字节码体积大，Base64 编码后塞表达式里动不动就超长度限制
* 国产中间件（东方通、宝兰德、金蝶、普元）虽然底层二开自 Tomcat/GlassFish，但改了包名，通用载荷直接打不通

MemShellParty 把这些全抹平了——选个中间件类型，勾个功能，一键出载荷。

---

## 核心机制

### 中间件适配矩阵

这是 MemShellParty 最硬的地方。它对每种中间件的每个版本都做了精细化适配，不是简单的"支持 Tomcat"，而是具体到 Tomcat 5.x 到 11.x、Jetty 6.x 到 12.x 各版本支持哪些挂载类型：

| 中间件 | 适配版本 | 挂载类型 |
| --- | --- | --- |
| Tomcat | 5.x ~ 11.x | Servlet/Filter/Listener/Valve/ProxyValve/WebSocket/Upgrade |
| Jetty | 6.x ~ 12.x | Servlet/Filter/Listener/Handler/Customizer |
| Undertow | 1.x ~ 2.3.x+ | Servlet/Filter/Listener |
| WebLogic | 10.3.6 ~ 14.x | Filter/Listener |
| WebSphere | 7.x ~ 9.x | Filter/Listener |
| GlassFish | 4.x ~ 6.x+ | Filter/Listener/Valve |
| Resin | 3.x ~ 4.x | Filter/Listener |
| JBoss | AS 4.x ~ EAP 6.x | Filter/Listener/Valve |
| TongWeb（东方通） | 6.x ~ 8.x | Filter/Listener/Valve |
| BES（宝兰德） | 9.5.x | Filter/Listener/Valve |
| InforSuite（中创） | 9 ~ 10 | Filter/Listener/Valve |
| Apusic（金蝶） | 9.0 ~ 10 | Filter/Listener |
| SpringWebMVC | 3.x ~ 6.x | Interceptor/ControllerHandler |
| SpringWebFlux | — | WebFilter/HandlerFunction |
| XXL-JOB | — | Netty Handler |

Tomcat 10.x 以上和 Spring Boot 3.x 使用了 Jakarta 命名空间，MemShellParty 对 javax.\* 和 jakarta.\* 都做了适配，不用再纠结 Servlet API 版本问题。

对于国产中间件的包名魔改也逐一适配。比如东方通三个大版本的包名全不一样：TongWeb6 用 `com.tongweb.web.thor.`，TongWeb7 改成了 `com.tongweb.catalina.`，TongWeb8 又换成 `com.tongweb.server.`。这些在 MemShellParty 里全都处理好了。

### Agent 内存马

除了常规的 Filter/Listener/Servlet 方式，MemShellParty 还支持 Java Agent 注入。Agent 方式通过 Instrumentation API 直接修改已加载类的字节码，比常规方式更隐蔽。

工具提供三种 Agent 打包方式：

* **AgentJar**：标准 Java Agent jar 包
* **AgentJarWithJDKAttacher**：自带 JDK attach 工具
* **AgentJarWithJREAttacher**：适配只有 JRE 环境的场景

使用流程也不复杂：

1. 把 MemShellAgent.jar 和 jattach 工具上传到目标机器
2. 用 `jps` 或 `ps` 找到目标 JVM 的 PID
3. 执行 `/path/to/jattach pid load instrument false /path/to/agent.jar`
4. Agent 注入完成，内存马生效

![Agent 内存马生成界面](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp00EPq6iaClCwd1To25E4nlAmDm9y5ic5f1ibKBIHmHeuj81wxMniaNbSt2nQL4mns9dFcck2xVcDU7SZEkkibYdKmB2ThUuAEpN0NCY/640?wx_fmt=png&from=appmsg)

Agent 内存马生成界面

### 字节码体积优化

体积是实战中绕不开的问题。很多漏洞利用场景（表达式注入、SSTI）对载荷长度有严格限制。

MemShellParty 做了两个层面的优化：

* 常规内存马采用深度优化的字节码生成策略，体积比 JMG 等传统工具缩小约 30%
* Agent 内存马直接用 ASM 框架生成字节码，绕过了 Javassist 和 ByteBuddy 的额外开销，体积缩小约 80%

界面上有个"缩小字节码"的开关，开了之后会启用更激进的优化策略。

### 探测马

打内存马之前，得先知道目标跑的啥中间件。MemShellParty 内置了探测马生成功能，支持 DNSLog 和 HTTP 两种外带方式。

用法也很简单：填入 DNSLog 地址或者 HTTP 回显服务器地址，选好打包方式，生成探测载荷打过去，就能收到目标的服务类型信息。

探测马探测出来的服务类型，直接对应 MemShellParty 里的生成选项。比如金蝶 Apusic10 探测出来结果是 GlassFish，因为它底层就是 GlassFish 二开的。

![探测马生成器界面](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp03COibzIsOalSWklt4TfvywtsShuOYWRVte4a6uljWxwhFgsya1w1OwDz3QWsocVGlp6N9XwWHYLQQ1pDqBn5dV5km9icPGADfLg/640?wx_fmt=png&from=appmsg)

探测马生成器界面

### 内置 Shell 功能

MemShellParty 原生支持这些常用管理工具的协议：

* **哥斯拉（Godzilla）**：加密 Webshell 管理
* **冰蝎（Behinder）**：动态二进制加密通信
* **蚁剑（AntSword）**：开源 Webshell 管理
* **Command**：简单命令执行
* **Suo5**：基于 HTTP 的 SOCKS5 代理隧道
* **NeoreGeorg**：改进版 reGeorg 隧道代理
* **Custom**：自定义内存马功能

每种 Shell 工具都有对应的密码、密钥、加密方式等配置项，一键生成后直接用对应客户端连接就行。

---

## 部署和使用

### 在线体验

在线站点（master 分支）：https://party.mem.mk

开发版（dev 分支）：https://dev-party.mem.mk

**注意**：在线站点适合尝鲜体验。实际使用建议本地部署，避免生成的内存马被中间人截获。

### 本地部署

推荐 Docker 一键部署：

```
# Docker Hub 源
docker run --pull=always --rm -it -d -p 8080:8080 --name memshell-party reajason/memshell-party:latest

# GitHub Container Registry 源
docker run --pull=always --rm -it -d -p 8080:8080 --name memshell-party ghcr.io/reajason/memshell-party:latest

# 网络不好？用南大镜像源
docker run --pull=always --rm -it -d -p 8080:8080 --name memshell-party ghcr.nju.edu.cn/reajason/memshell-party:latest
```

部署完访问 http://127.0.0.1:8080 就能用了。

### 生成一个内存马

拿最常见的 Tomcat + 哥斯拉组合举例：

1. 服务类型选 **Tomcat**，服务版本按实际目标选（不确定就选 Unknown）
2. Shell 工具选 **Godzilla**
3. 内存马挂载类型选 **Filter**（兼容性最好）
4. 密码和密钥可以自定义，也可以用默认随机生成的
5. 打包方式按利用场景选：Base64 用于表达式注入，Jar 用于反序列化，BCEL 用于 BCEL ClassLoader 场景
6. 点击"生成内存马"

![常规内存马生成界面](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp00dljFmOHVajkpoZYdleZN6Z6ofd0ia577g4XRhgpVlRsZFyaaUYqS7vSQG2UrJCH72jX9CHuPX8mIMWL8KIricuRxFnFVHicxQ4E/640?wx_fmt=png&from=appmsg)

常规内存马生成界面

右侧会显示生成结果，包括注入器类名、内存马类名和字节码大小。生成结果可以直接复制到利用链中使用。

---

## 实战场景

### 场景一：表达式注入打内存马

发现目标存在 SpEL/OGNL/EL 表达式注入漏洞，需要注入内存马维持权限。

1. 先用探测马确认目标中间件类型
2. 在 MemShellParty 中选对应中间件和版本
3. 打包方式选 **Base64**（适合表达式注入场景）
4. 开启"缩小字节码"减小载荷体积
5. 如果目标 JDK 版本 ≥ 9，打开"绕过 Java 模块限制"
6. 生成后把 Base64 载荷塞到表达式注入点

MemShellParty 会自动处理模块限制的绕过，不用手动拼 `--add-opens` 参数。

### 场景二：反序列化漏洞利用

目标存在 Java 反序列化漏洞（如 Commons Collections 链），需要通过反序列化载荷注入内存马。

MemShellParty 内置了 20+ 种打包方式，覆盖主流反序列化利用链：

| 打包方式 | 适用场景 |
| --- | --- |
| JavaCommonsBeanutils19 | Commons Beanutils 1.9.x |
| JavaCommonsBeanutils18 ~ 16 | 老版本 CB 链 |
| JavaCommonsCollections3 ~ 4 | CC 链 |
| HessianDeserialize / Hessian2 | Hessian 反序列化 |
| JavaDeserialize | 原生 Java 反序列化 |
| BCEL | BCEL ClassLoader |

选好打包方式，一键生成反序列化载荷。

### 场景三：隧道代理内网穿透

拿到 Webshell 后需要进内网。选 **Suo5** 或 **NeoreGeorg** 功能，生成对应的内存马注入后，直接在本地建立 SOCKS5 隧道。

相比文件落地的代理脚本，内存马方式不会留下文件痕迹，更难被主机安全产品检测到。

### 场景四：国产中间件攻防

HW 场景下经常会遇到东方通、宝兰德、金蝶、中创这些国产中间件。这些中间件底层虽然是 Tomcat 或 GlassFish 二开的，但改了包名，通用工具生成的载荷打不通。

MemShellParty 的探测马能准确识别这些国产中间件的真实底层类型，生成器也对每种国产中间件的包名做了精确适配。比如：

* BES 9.5.1 直接当 Tomcat 打
* BES 9.5.2+ 选 BES 类型
* Apusic10 底层是 GlassFish，选 GlassFish 类型
* TongWeb 6/7/8 选 TongWeb 类型，工具自动处理包名差异

欢迎关注“攻防录”✨

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

攻防录

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

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