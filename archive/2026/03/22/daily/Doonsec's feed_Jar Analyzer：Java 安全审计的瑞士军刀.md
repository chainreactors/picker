---
title: Jar Analyzer：Java 安全审计的瑞士军刀
url: https://mp.weixin.qq.com/s/YGGNDNdjFo6fcM-1ZcFh3Q
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:19:39.927518
---

# Jar Analyzer：Java 安全审计的瑞士军刀

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0zk3Ye7cp02Z7M1mfbcOa9NFO25GpnOYL2icibGxFrm1q2fN1EIjc0CvwwhCVEMKRhtyEEDNwm4ukVPfkTPPSWtcBfibV3JjGskibFRVyt9vTJQ/0?wx_fmt=jpeg)

# Jar Analyzer：Java 安全审计的瑞士军刀

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于攻防录
，作者攻防路

![](http://wx.qlogo.cn/mmhead/iahdQicCC5VBQr884mDGLmrJyT8p86wvGly4LfZtLl6Zkl5nptrOmJsEw4UwzUXMZpx5zLZyTmRxc/0)

**攻防录**
.

聚焦红队实战攻防技术，分享内网渗透、提权纵横、漏洞复现、代码审计等。

#

项目地址：https://github.com/jar-analyzer/jar-analyzer

JAR 包分析这件事，做 Java 安全的人都绕不开。反编译看代码、搜方法调用、追调用链、找危险函数——每次都要在 IDEA、JD-GUI、codeql 之间来回切换，效率很低。

Jar Analyzer 把这些需求全塞进了一个 GUI 工具里。拖进去一堆 JAR，直接点点鼠标就能完成大部分代码审计工作。截至 2026 年 3 月，这个项目在 GitHub 已经有约 2k star，连续更新 5 年，发布了 59 个版本，完全开源免费。

---

## 它能做什么

先说最直接的——你手里有一堆 JAR 包，想快速搞清楚里面的代码结构和潜在风险。Jar Analyzer 覆盖的场景非常广：

**基础分析能力**

* 支持 Jar/War/Classes 三种输入格式，支持多文件批量加载，也能处理嵌套的 FatJar
* 内置 Fernflower 改进版反编译引擎，双击即可查看反编译代码
* 使用 JavaParser 精确定位方法位置，类似 IDEA 的代码跳转体验
* 黑白名单过滤，构建数据库和搜索都支持按类名/包名过滤

**方法调用分析**

这是 Jar Analyzer 的看家本领：

* 构建方法调用关系数据库，可以正向搜"谁调了这个方法"，也可以反向搜"这个方法调了谁"
* 支持精确搜索和模糊搜索
* 基于 DFS（深度优先搜索）算法的调用链分析，能自动追踪从 source 到 sink 的完整路径
* 5.7 版本之后加入了模拟 JVM 的污点分析，可以验证 DFS 推导出来的调用链是否真的可达

![Jar Analyzer 暗色主题界面，左侧文件树+右侧功能面板](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp00detTG06XibKQr0icSYRJUmvutJ5icCKUmKiaJH86p8hwyYJt6wR25BZlq0KolH2TNheBtPXHDHiaNead5WC9fiaLg8G47jJFyQ6UbY/640?wx_fmt=png&from=appmsg)

Jar Analyzer 暗色主题界面，左侧文件树+右侧功能面板

**安全分析功能**

| 功能 | 说明 |
| --- | --- |
| 漏洞调用搜索 | 一键搜索 JNDI、Runtime.exec、readObject、SpEL.getValue 等常见危险调用 |
| SCA 分析 | 匹配 Log4j2、Fastjson 47/68/80 等已知漏洞版本 |
| 信息泄露检查 | 检测 IP 地址、手机号、邮箱、API Key、JWT、数据库连接串等敏感信息 |
| Gadget 分析 | 辅助筛选符合条件的反序列化 Gadget 链 |
| 应急响应 | 一键提取序列化数据中的恶意 class、一键反编译 BCEL 代码 |

---

## 工作原理

Jar Analyzer 的底层引擎用 ASM 框架解析字节码，用 SQLite 做数据持久化。

加载 JAR 的时候，引擎遍历所有 .class 文件，解析出每个类的方法签名、字段信息、继承关系，以及每个方法内部的 invoke 指令（invokevirtual、invokestatic、invokeinterface 等），再把这些调用关系存进数据库。这一步就是"构建数据库"，你在 GUI 上点 Start 按钮触发的就是这个过程。

数据库建好之后，所有的搜索和分析操作其实都是 SQL 查询。方法定义搜索、方法引用搜索、字符串搜索（基于 LDC 指令），底层都是数据库操作。

**DFS 调用链分析**是整个工具最有价值的部分。它的逻辑是这样的：

1. 你指定一个 source（起点，比如 Spring Controller 的入口方法）和一个 sink（终点，比如 `Runtime.exec`）
2. 引擎从 sink 出发，通过方法调用关系做反向 DFS 搜索
3. 找到从某个 source 到 sink 的所有可达路径，按调用链长度排序输出

5.7 版本以后还加了**污点分析验证**。因为 DFS 只看调用关系，不管参数是否真的传递到了危险位置。污点分析会模拟 JVM 栈帧，追踪参数在方法调用链中的流动，验证这条链是不是真的"通"的。

![DFS 漏洞链分析 + 反编译代码联动](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp00fJgKeHPDl1MlSC7wDdKuUJe6Bap5hTo3fcibpM1U40m3O8alSWBpWBl8CEkQOnOI4Fd1AvvibETNS6EflRjiaN8MEhgKMXo6vbQ/640?wx_fmt=png&from=appmsg)

DFS 漏洞链分析 + 反编译代码联动

**SpEL 表达式搜索**是另一个亮点。传统搜索只能按类名、方法名这些固定字段搜。表达式搜索基于 Spring Expression Language，支持多条件组合。举个例子，搜 CVE-2023-21939 对应的漏洞模式：

```
#method
    .startWith("set")
    .paramsNum(1)
    .isStatic(false)
    .isPublic(true)
    .paramTypeMap(0,"java.lang.String")
    .isSubClassOf("java.awt.Component")
```

这段表达式的意思是：找到所有以 set 开头、只有一个 String 参数、非静态、公开的方法，且所在类是 `java.awt.Component` 的子类。用普通搜索你根本没法表达这种复合条件。

![SpEL 表达式搜索功能](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp017Zhz9cAPQDw5KP2CMrbjYPHve1XlKdFhrx9tOZQu9tTU5nlo8ibqNGgbd27mVg0KktI4baGgPuat1ib0fytBh4XH6o2eAzI6Pk/640?wx_fmt=png&from=appmsg)

SpEL 表达式搜索功能

---

## 安装和使用

Jar Analyzer 提供开箱即用的发布包，不需要自己编译。

1. 前往 Release 页面下载最新版本：https://github.com/jar-analyzer/jar-analyzer/releases/latest
2. 解压后运行启动脚本（Windows 双击 bat，macOS/Linux 执行 sh）
3. 在 GUI 右上角选择要分析的 JAR 文件或目录
4. 配置黑白名单（可选），点击 Start 按钮开始构建数据库
5. 等进度条走完，就可以开始搜索和分析了

注意几个点：

* 分析大量 JAR 时，临时目录和数据库文件可能会很大，确保磁盘空间充足
* 表达式搜索如果跑得慢，可能是默认内存不够，修改启动脚本里的 `-Xms` 参数，比如：

```
set "java_args=-XX:+UseG1GC -Xms2g -XX:MaxGCPauseMillis=200 %other_args%"
```

* 支持 10 种 UI 主题，启动时用 `-t` 参数切换：

```
java -jar jar-analyzer.jar gui -t win-classic
```

---

## 实战场景

### 场景一：从 JAR 包里找危险调用

你拿到一个 Java 应用的所有依赖 JAR，想快速扫一遍有没有 `Runtime.exec`、`ProcessBuilder.start`、`readObject` 这些常见的危险调用。

直接在 GUI 里切到漏洞搜索面板，按风险等级筛选，点一下就出结果。每个结果会精确到类名和方法名，双击直接跳到反编译代码。

![Java 漏洞一键搜索面板](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp03fLvgCIw4gJPUsWGqsQCwYdmybhnxpbOlOYVPImQnuP37icpGHbibeSty28UD7Nn2WsfL1ftQKE8m5oUb0p8TlEQt3tF2EvtFTI/640?wx_fmt=png&from=appmsg)

Java 漏洞一键搜索面板

### 场景二：追一条完整的漏洞利用链

比如你在审计一个 Spring Boot 应用，想知道从 Controller 入口到 `Runtime.exec` 有没有可达路径。

1. 在 chains 面板里配置好 Source（Spring Controller）和 Sink（Runtime.exec）
2. 设好最大深度（建议 10 左右）
3. 勾选"污点分析验证"
4. 点"分析"

工具会列出所有可达路径，右侧显示污点分析的详细过程——参数是怎么从第一个方法一路传到最后的 exec 调用的。

### 场景三：排查信息泄露

用信息泄露检查功能，一键扫描 JAR 包中硬编码的 AK/SK、数据库密码、API Key、JWT 密钥等。支持 Base64 编码检测，结果按类型分类展示。

![信息泄露检查功能](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp01VBftmBb89MMuHgozpoHvJypJ1zRicMfvaJujlGCFfWqm5slSIIuR4jOxTYcicFwscTHeDf5MEK10MhrOfsnBrMiaicibfyWvzwfFs/640?wx_fmt=png&from=appmsg)

信息泄露检查功能

### 场景四：接入 AI 工作流

5.10 版本之后，Jar Analyzer 支持 MCP（Model Context Protocol）。你可以把它接到 Claude、Cursor 这些 AI 工具里，让 AI 直接调用 Jar Analyzer 的分析能力。

另外也支持 n8n 工作流平台，把 JAR 分析集成到 CI/CD 流水线里，实现自动化的安全扫描。

MCP 文档：https://github.com/jar-analyzer/jar-analyzer/blob/master/mcp-doc/README.md

项目地址：https://github.com/jar-analyzer/jar-analyzer

官方文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

欢迎关注“攻防录”✨

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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