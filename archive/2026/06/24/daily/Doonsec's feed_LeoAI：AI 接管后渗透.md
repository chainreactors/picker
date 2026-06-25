---
title: LeoAI：AI 接管后渗透
url: https://mp.weixin.qq.com/s/U3pkId8Tw_MXgq68nZDSbw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:01:50.134544
---

# LeoAI：AI 接管后渗透

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0zk3Ye7cp022HBCkoZibMXo5U6zfbYolf4XxlnU9WWhgia7Jm6jfh8oF92vcUibrlXFpeQeWj30BkXxNicpclk9O0kknKtEfp7HoJBMEgVjwI8k/0?wx_fmt=jpeg)

# LeoAI：AI 接管后渗透

攻防路
攻防路

攻防录

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 简介

LeoAI 是一款给红队用的后渗透管理平台，定位接近冰蝎、哥斯拉这类 WebShell 管理工具，但把 LangChain4j 的 Agent 能力做进了主流程：节点拿下之后，侦察、提权、凭据收集、横向移动这些动作可以交给 AI 自动跑，而不是手动一条条敲命令。

底层是 Spring Boot 3.5 + LangChain4j 1.16，内置 SQLite，Web 界面打包进 JAR，下载一个 jar 包就能起来；同时提供 18 种中间件的内存马生成、HTTP / HTTP Chunked / WebSocket 三种通信通道、流量伪装、SOCKS5 与反向隧道这些 C2 级别的能力。

项目地址：https://github.com/cha0upup/LeoAI

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp01dwskC9hUNXKbCQGA8hWZGH2gd4ZXSKObj2KOyfiaW7m0FqlQJgCI6vrdzGicialBELiaGMopjOqOO2ib5wVfcQpLf3h8RO3AlO4LU/640?wx_fmt=png&from=appmsg)

LeoAI 节点管理主界面

## 技术原理

LeoAI 的设计可以拆成三层来看：通信端（节点 / puppet）、平台端（管理 UI + AI Agent）、能力端（Tools 与 Skills）。

### Agent + Tools：175 个原子能力当函数调用

LeoAI 把后渗透常见操作全部抽象成可被 LLM 调用的 Tool，目前合计 175 个，覆盖文件、进程、网络、凭据、扫描、HTTP 发包等场景。Agent 拿到任务后按 ReAct 风格做多轮工具调用，把每一轮结果写进上下文，逐步推进。

在此之上还有 8 个预置 Skill，本质是经过验证的提示词模板，把一类完整任务（比如「拿下一台 Linux 主机后做基础侦察」）做成一键启动：

| 类别 | Skill | 作用 |
| --- | --- | --- |
| 侦察 | recon-basic-info | 系统信息、网络、进程、服务全量摸底 |
| 凭据收集 | hunt-credentials | 浏览器、系统、WiFi、应用配置一把梭 |
| 权限提升 | escalate-linux-privilege | SUID / Capability / 内核版本组合排查 |
| 持久化 | persistence-linux | cron、systemd、SSH key 等手段评估 |
| 横向移动 | lateral-move-ssh | 复用凭据扫内网、尝试 SSH 横向 |

另外平台层还有 3 个 Skill 偏开发辅助：develop-disguise 帮你写流量伪装模板，develop-fingerprint 帮你写指纹规则，exploit-suggest 根据命中的指纹反推可能的利用方式。

所有 Skill 都是 Markdown + YAML frontmatter 存在 VFS 里，可以在界面上改 prompt、加标签、按需禁用，改完立即生效不用重启。这点比把 prompt 写死在代码里友好得多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp001lnKcxDVyrxLia0pXGrrxK1TibvtKuqTEfH7uuSWAVSvJcwn8he5icibjUwnUXmMryk6lib4icrUQ86W89xbKsdPJibDaXoRwQVxYzw/640?wx_fmt=png&from=appmsg)

AI 助手自动调用侦察工具

### 通信层：协议三选一，伪装即密钥

LeoAI 没有单独的密钥字段，管理端和 shell 端跑的是同一套 encode / decode 逻辑，对不上就解不开请求。等于把伪装和鉴权合二为一：换伪装等于换密钥。

三种通信协议覆盖不同场景：

| 协议 | 适合做什么 |
| --- | --- |
| HTTP | 通用场景，过 WAF 兼容性最好 |
| HTTP Chunked | 大文件上传下载、长日志拉取 |
| WebSocket | 终端类低延迟交互 |

流量层做了 TLS 指纹伪装、Header 噪声注入、URL 随机化，配合自定义 encode / decode，目的是让流量在外观上贴近正常业务。

### 代理与隧道：四种 forward 模式

拿下节点之后通常要往内网里钻，LeoAI 内置四种转发模式，基本覆盖 ssh 隧道能干的事：

| 模式 | 用法 |
| --- | --- |
| SOCKS5 代理 | 节点侧开监听，C2 端用 proxychains / Burp 上游 |
| HTTP 代理 | CONNECT 隧道，浏览器手动挂代理也走得通 |
| 本地端口转发（ssh -L） | C2 端口 → 节点 → 内网某 IP:Port，直连内网单服务 |
| 反向隧道（ssh -R） | 节点开监听 → 内网机回连 → C2 拨号取走 |

每条隧道都带连接数、上下行流量统计，一键停。

### 内存马与 WebShell 生成

Shell 生成模块支持 7 类内存马（Filter、Servlet、Listener、Valve、Interceptor、Controller、WebSocket），适配 18 种中间件，从 Tomcat、Jetty、Resin、Undertow 到 WebLogic、WebSphere、Apusic、TongWeb 都覆盖到。

表达式注入打包器列表也很长，OGNL、SpEL、EL、Groovy、Freemarker、MVEL、BeanShell、Velocity、Thymeleaf、JEXL、Jinjava、BCEL、Translet、XmlDecoder 等合计 41 种 Packer，基本能对上常见 Java 漏洞场景。

### Puppet 端的硬骨头：idle 容器也能拿到面板

v0.0.6 改的几个组件直接说明了这套架构在实战里踩过的坑。

独立 Tomcat 部署 + puppet 注入到 commonLoader、且 webapp 处于 idle 状态时，过去依赖活跃请求或 contextClassLoader 的组件会全部扑空。这一版把 TomcatCatalinaManageComponent、WeblogicCatalinaManageComponent、SpringFrameworkManageComponent 重构成「公开 API → MBean → 字段反射」三层降级，覆盖 Tomcat 6/7/8/9/10/11、WebLogic 全版本，以及 Spring 5/6（含 Tomcat 10+ 的 jakarta.servlet 切换）。

几个具体对比：

| 场景 | 0.0.5 | 0.0.6 |
| --- | --- | --- |
| Idle Tomcat 容器面板列表（无活跃请求） | 拿不到 | 可用 |
| Idle Spring Boot 凭据采集 / 框架信息 | 拿不到 | 可用 |
| WebLogic 普通 CL 注入下的容器列表 | 拿不到 | 可用 |
| Tomcat 6 卸载 Listener | 不支持 | 可用 |
| Filter 卸载即时生效 | 要等下一次请求 | 立即生效 |
| 跨 ClassLoader 使用 webapp 内 JDBC driver | 不支持 | 可用 |
| 查看 webapp 内的 class 字节码 | 不支持 | 可用 |

这些细节平时不显眼，但在生产环境用过类似工具的就知道，「拿不到」往往直接决定能不能往下走。

## 快速上手

下面以 Docker 方式启动为例，本机连 Java 都不用装。

1. 安装 Docker Desktop（macOS / Windows）或 Docker Engine + Compose 插件（Linux）。
2. 拉代码：

```
git clone https://github.com/cha0upup/LeoAI.git
cd LeoAI
```

3. 在项目根目录执行：

```
docker compose up -d --build
```

首次构建会从 Release 拉 JAR，国内网络大约 3 到 10 分钟。

4. 浏览器打开 http://localhost:8082 ，初始账号 admin / 54ikun，登录后立刻改密码。

如果不想用 Docker，下 Release 里的 jar 直接跑也行：

```
java -jar --add-opens java.base/java.lang=ALL-UNNAMED LeoAi-0.0.6-SNAPSHOT.jar
```

`--add-opens` 这段不能省，模块系统不开就启动不起来。

5. 配 AI 通道。进「管理后台 → AI 配置」添加一个 OpenAI 兼容通道，常见的几个 Base URL：

| 提供商 | Base URL |
| --- | --- |
| OpenAI | https://api.openai.com/v1 |
| 通义千问 | https://dashscope.aliyuncs.com/compatible-mode/v1 |
| DeepSeek | https://api.deepseek.com |
| Ollama 本地 | http://localhost:11434/v1 |

填完点「测试连接」过了就保存。

6. 配节点。进「节点管理 → 添加节点」，填目标 URL、选通信协议、绑定一套流量伪装模板（强烈建议自己写一份 encode / decode，别用内置模板）。保存后就能进控制台。

![](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp02UkMk3C84eic6vbxcmialesXVqiclExaCG4KQhnw6bTYRHgZTFbnsgS05vOrt82kciaHOhvfLyk0HY0N2RcoOVCicAmFR5wK8z5HSg/640?wx_fmt=png&from=appmsg)

操作控制台与 AI 技能面板

## 使用场景

### 拿下 webshell 后第一轮侦察

控制台右侧 AI 面板发一句「先把这台机基础信息摸一遍」，或者直接点 Skill 快捷按钮启动 recon-basic-info。

Agent 会按预设流程跑：系统版本、内核、网卡、监听端口、关键进程、已安装软件、计划任务，结果分类汇总写回侦察上下文。后续问「这台机上有没有 Java 进程」「跑了哪些 Web 服务」时，AI 已经知道前面摸过什么，不会重新跑一遍。

### 凭据收集与提权评估

hunt-credentials 一键把浏览器密码、系统凭据、WiFi 配置、常见应用的配置文件全捋一遍。之后跑 escalate-linux-privilege，会检查 SUID / Capability、计划任务、内核版本对应的已知提权漏洞，给出按可行性排序的建议。

Windows 环境下可以直接调 WebLogic 密码获取、堆转储分析这类内置插件，不用临时手写脚本。

### 内网穿透与横向移动

在节点的代理面板挂一个 SOCKS5 监听，C2 这边配 proxychains，nmap、ldapsearch、impacket 全部走这条隧道。出网严格的内网用反向隧道更顺：节点开监听，让内网机器主动回连 C2 拨号转发。

lateral-move-ssh 则会把前面侦察到的凭据组合起来，挑可达主机做横向尝试，结果回写到上下文里，方便后续接着扩面。

### 内存马 + 流量伪装的组合拳

如果目标是 Java 应用，可以先用 Shell 生成器按目标中间件生成一份 Filter / Listener / Controller 内存马（选好对应的表达式 Packer），落地后把节点协议挂到对应伪装模板上。配合 v0.0.6 的 idle 容器支持，即便目标 webapp 没人访问，也能正常列出 Filter / Servlet / Listener 并按需卸载，做完事不留东西。

## 需要注意的点

LeoAI 默认开在 8082 端口，自带 admin / 54ikun 账号，部署后第一件事是改密码、限来源 IP。流量伪装模板不要直接复用内置那两套，自己写一份 encode / decode，等于换一把密钥。审计日志默认开着，团队多人协作时方便回溯，但也意味着所有动作都会被记录，自用时心里要有数。

往期推荐 📚

[BurpMCP-Ultra：AI 驱动 Burp](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247485063&idx=1&sn=9d26aa44853d31a1e05abcc7850a1755&scene=21#wechat_redirect)

[Shannon：白盒 AI 渗透测试](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247485036&idx=1&sn=9253daeeb1e5b7ad389b231c168253ce&scene=21#wechat_redirect)

[AntiDebug MCP：AI 前端逆向助手](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247485058&idx=1&sn=b2278907ec3f2b5ae499bdee02bbd84b&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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