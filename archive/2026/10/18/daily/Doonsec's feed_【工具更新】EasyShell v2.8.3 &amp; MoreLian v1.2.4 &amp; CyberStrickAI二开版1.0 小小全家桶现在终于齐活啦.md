---
title: 【工具更新】EasyShell v2.8.3 &amp; MoreLian v1.2.4 &amp; CyberStrickAI二开版1.0 小小全家桶现在终于齐活啦
url: https://mp.weixin.qq.com/s/KEG85BlA_5l-WJYIfk6Xqg
source: Doonsec's feed
date: 2026-10-18
fetch_date: 2026-10-19T07:06:54.185944
---

# 【工具更新】EasyShell v2.8.3 &amp; MoreLian v1.2.4 &amp; CyberStrickAI二开版1.0 小小全家桶现在终于齐活啦

# 【工具更新】EasyShell v2.8.3 & MoreLian v1.2.4 & CyberStrickAI二开版1.0 小小全家桶现在终于齐活啦

原创

沐寒
沐寒

渗透云记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**免责声明**

由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJZJ4pVQHOicqtkQntqLduTfPaVvVnZ4iaGc0DaBeQqNoicYUrzzyOpIsJWbSgNUqV3SodRwKFOIq3Lw/640?wx_fmt=png&from=appmsg)

欢迎关注本公众号，长期推送技术文章

## 前言

经过好一段时间的更新，总算是把CyberStrikeAI的一键信息收集调试的差不多了，虽然还是有点瑕疵，这个就逐步进行优化吧。

然后很长一段时间没有更新MoreLian(webshell)的原因是一直在磨洋工，改来改去发现还是1.0版本使用起来最舒坦，这次主要就是加了mcp，配合CyberStrikeAI进行使用；

EasyShell小版本更新，主要就是修复了大家反馈的一些bug

这次三个工具算是真正串起来了：**CyberStrikeAI 当大脑**，负责任务编排、信息收集和资产沉淀；**EasyShell 管 C2 这条线**；**MoreLian 管 WebShell 这条线**。后两者都通过 MCP 注册给 CyberStrikeAI，控制台用 SSO 直接内嵌，不用再在几个窗口之间反复登录、反复复制凭据。

先给个更新速览，后面再逐个展开：

* **EasyShell v2.8.3**

  以修 bug 为主。内存/协程泄漏、下载队列、WS 心跳、监听器状态这些"挂久了才出事"的地方集中处理了一遍，另外补了非交互式终端行编辑和文件管理常用的"复制到/移动到"功能。
* **MoreLian v1.2.4**

  把欠的账还了。D盾 ASP 全族复扫 0 命中，伏魔/河马/阿里云模板全绿；Web 端补齐 SSO、多账号和四平台打包；新增 morelian MCP，AI 可以直接管 WebShell。
* **CyberStrikeAI 二开版 1.0**

  基于上游 v1.7.17 二开。完整集成 EasyShell + MoreLian；新增一键信息收集、本地 CVE 语料仓、实战 POC 沉淀和一整套资产/任务/工作流。

## 一、EasyShell v2.8.3

2.8.3 以修 bug 为主，顺手补了几个一直想要的小功能。

### 1. 稳定性：先把"挂久了会出事"的坑填了

服务端长时间运行被 OOM killer 干掉、浏览器刷新几次就卡死，这类问题上一版修了一部分，这一版继续往深里挖：

* **无界容器统一收口**

  shellcode/Stage 缓存、SOCKS 队列、DNS 预认证表、文件浏览缓存这些按 uid 建表却从不删除的容器，统一加了 TTL 和容量上限；主机离线时由 command/proxy/link 三层统一触发清理钩子。
* **截图历史导出改流式**

  原来是内存里拼 zip，最坏情况瞬时占用接近 2GB，现在改成临时文件流式回传。
* **下载管理重做**

  植入体回失败时只回错误文本，旧逻辑的 active 永不清空，该 uid 后续下载会永久卡在"排队"；现在成功/失败终态都会出队，下载进度按实际落盘字节计数，删主机时同步清理按 uid 常驻的下载状态。
* **下载宽限三端统一**

  TCP/WS/KCP 都补上了下载在飞宽限。分片落盘的背压会阻塞上行读循环（连心跳都读不到），目录打包 ZIP 阶段零上行时原来没有任何保护，现在这个窗口也算在飞。
* **日志降噪**

  首包前断开按来源 IP 限流，良性断开只记 DEBUG，可疑断开保留完整错误原文、其余降噪，持续刷屏时每个来源每分钟最多一行。内存采样和 GOMEMLIMIT 提示改成"仅落盘"，不再刷控制台和 Web 日志面板，被 OOM 杀掉后翻 `logs/easyshell.log` 复盘即可。

### 2. 终端：非交互式 shell 终于能正常改命令了

用 Windows 目标比较多的师傅应该都被这个恶心过：非交互式终端只能 ↑/↓ 翻历史，想改中间一个字符只能删了重打，光标还会自己跳。这版把输入行做成了真正的行编辑器：

* 支持 ←/→、Home/End/Delete，外加 readline 风格的 Ctrl+A/E/U/K/W；
* 修复 `ESC[3~` 这类 `~` 结尾的序列被当普通字符写进命令行的问题；
* 长命令折行、在行中间插入删除都能正确重绘，光标跳动一并修掉；
* 交互式 shell 上下切换历史失败的问题也修了。

### 3. 文件管理：补上"复制到/移动到"

* 右键新增「复制到…」「移动到…」，可以填目标目录，也可以从目录树点选，支持改名并实时显示最终路径；客户端和服务端双侧校验非法字符、源和目标相同、目录不能放进自己里面。
* 大目录复制/移动时 listing 等待超时按"指令已下发，请稍后刷新"提示，不再误报失败。
* 顶部路径框支持回车/按钮直接跳转，兼容 `d:\xxx`、带引号粘贴、`file:///`、裸盘符和相对路径。
* 文件表格双击进目录不再选中文字，文件夹改成单击打开；配合已有的批量下载和文件夹压缩下载，日常搬文件顺手不少。
* 主机详情页的 IP 口径改了：直连主机默认取公网 IP，级联主机（有上级跳板）改取内网 IP——横向的时候要看的是后者。

### 4. 上线与链路：不再"看起来在跑"

* **WebSocket 心跳补了零长度 keepalive ack**

  单边断链时（服务端已把连接判死、客户端 socket 还在、心跳照发），客户端读写都不会立刻报错，只有"对端不再发脉冲"才能发现。TCP/KCP 早有这套，WS 一直缺，这次补齐，植入体侧的下行静默看门狗才算真正生效。
* **监听器绑定改成同步可见**

  原来 `go server.ListenAndServe()` 会把绑定失败吞进日志，控制台显示"运行中"，端口上其实一个 socket 都没有。WS/HTTP Beacon/HTTPS Beacon/DoH 现在同步绑定 + 30 秒短重试，失败直接标"已停止"并打清晰日志。
* 修复 WS/KCP 一键上线下载超时、WS 一键上线下载失败。
* 级联桥默认不再监听 `0.0.0.0`，改成直接监听具体网段，少一点暴露面。

## 二、MoreLian v1.2.4

MoreLian 从 1.0 到 1.2.4 隔了挺久，中间不是没写，是一直在磨免杀和 Web 化这两块。这次把欠的账一次还了，重点三件事：**免杀、Web/SSO、MCP**。

### 1. 免杀：这次是真下功夫了

上一版只有 PHP 比较稳，其余语言还会告警。这一版是逐个签名定位、逐个改加载方式，不是靠堆混淆碰运气：

* **D盾**

  ASP 全族复扫 **0 命中**（`Adodb.Stream` 那条签名被拆成 `Chr(46)` 拼接 + `ChrW` 赋值）；JSP/JSPX 改成直写加载器，页面里不出现类加载器、反射、动态造类，目标上不留常驻文件；C# 装配加载改成反射拆名 + 落盘 `LoadFile` + 直接 `Equals` 分派，避开 `Assembly.Load(byte[])` 这条必中规则。
* **伏魔**

  C# 全族（aspx/ashx/asmx × 12 变体）和 JSP 全族（jsp/jspx × 5 线族）全部通过；**河马**门禁同步通过，默认形态伏魔/河马 10/10全绿。
* **阿里云**

  ：内置的 22 个模板全绿。
* **生成物结构随机化**

  PHP 的函数名改由 `pack/hex2bin/strrev/chr` 随机构造（D盾会把 `base64``.``_decode` 折叠，直接写就中），切点随机；ASP 的 `ADODB.Stream` ProgID 拆开拼；JSP 混淆 6 档 + 字符集重编码。同配置连续生成两次，行差异 PHP 约 63%、ASP 约 36%、JSP 约 79%。
* **compact 精简形态**

  PHP 常规形态 1KB 上下（最小 28B 的 eval 形态），JSP 从 13KB 降到 1.3KB，C# 从 5.6KB 降到 1.4KB，落地存活和功能都实测过。
* 另外补了 ASMX XOR 图片马、JSPX 纯 Java AES（去掉 `javax.crypto` 调用）、双向 TLS 客户端证书（PEM/PKCS#12）。

具体测试效果如下：

d盾最新版扫描基本上就是aspx单文件报毒

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNrTagkKgnsAat0dOFTCyWb6wT1icd5J1f4hJqvlxl1BHS2GlRyuE9xg2SUEjH3XJlbdFYBMCiaNaiaNOVHFEI4m3mzV1OGcVx62Ng/640?wx_fmt=png&from=appmsg)

阿里云伏魔除php可疑，其余的均为全绿

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNpdtKgUia502xqeKyIPRhLa9N0JnWzdSItDuTs6Y8l8PSRrMQvzKxyCI1BdcPjQVF4TJZ9e6xXuWcFA8hxrUEkcguu7sqsQbmL8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNpy4sdPoRpa51Rjicrcy3gjnnJqI4SKKJ8fTfPIz4OoiahoViaKQed2PiaXYIiaEJq1N5bqTNTiaibbLwQic0GOicvvUTbht0JwwxdKqFYk/640?wx_fmt=png&from=appmsg)

### 2. 会话侧：从"能用"到"好用"

* **命令历史**

  按目标持久化到本机，每条命令的输出也能展开查看/复制，失败条目高亮；断线状态一样能看。文件管理目录列表和会话头都能直接打开历史抽屉，点一下自动切到命令终端。
* **离线缓存**

  连不上目标时不再只弹一个报错，而是进入离线面板，目标信息和本机命令历史只读可查，能复制、能重连。
* **文件投递**

  上传脚本后可以直接向目标推送任意文件，落地点做成会话内的内置 Tab，按 Payload 过滤语言，填目录和文件名即可。
* **协议与载荷**

  协议侧切到新版 GSL5（旧版哥斯拉的升级版），原有插件继续兼容；新增 5 个加密器（PHP\_AES\_XOR\_BASE64、JAVA\_GZIP、JAVA\_XOR\_IMAGE、CSHAP\_GZIP、CSHAP\_XOR\_IMAGE）；大文件分片收发、文件属性、目标自助 URL 下载补齐；PHP 目标禁用 exec 时可以走 fpm-sendmail 回环。
* **内存马**

  直写加载器绑定 HttpSession，修好了 include→run 的插件链路；favicon.ico 注入、直连、删页后复连在 Tomcat9/10 × jsp/jspx 上都实测通过。
* **数据库面板**

  7 类方言 × 6 个动作下沉到后端，库表树、分页、行数统计、CSV 导出、表结构页签都齐了；连接配置按目标隔离保存，并记住"最近使用"。
* 操作审计、批量测试历史、多选批量、IP 归属地这些零碎能力也都补上了。

### 3. Web 化与 SSO：一个 exe，浏览器也能用

* 桌面端「设置 → 网页访问」可以随时启停内置 Web 服务，和 `-web` 共用同一套实现与鉴权。
* Windows 仍然只有一个 `morelian.exe`，GUI 和 `-web` 都是它；四平台打包脚本一键出 zip/tar.gz/dmg。
* **SSO 单点登录**

  对齐 EasyShell：共享 token + IP 白名单 + Bearer 会话，名单外/错 token/过期一律 404 伪装；支持 `redirect=` 站内相对路径，配合平台同源反代，HTTPS 平台也能嵌 HTTP 控制台；轮换 token 立即作废旧链接和旧会话。
* **访问账号支持多账号**

  （同权限）：新增/重置/禁用/删除、改自己的密码、至少保留一个可用账号、审计按人记；headless 包没有桌面端，这些操作在浏览器里就能做。
* Web 端启动页去掉了产品名、图标和 favicon，未认证只回通用 401；启动打印 ASCII 横幅 + 版本号 + 授权状态，双击启动不会窗口一闪而过。

注：linux只支持命令行启动，未打包gui版本。

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNqJjYULMVICXM38rW5uDWOksMuVpdCsd3eS752Y09MNNtmDIVLUJ0dTbusLP1XZcap2qISpsWHUbPib2ibIicRptXrEF0OGAEKqKA/640?wx_fmt=png&from=appmsg)

### 4. MCP：让 AI 直接管 WebShell

CyberStrikeAI 仓库的 `plugins/morelian-package/` 里带了 morelian 的 MCP 服务器，支持 Basic 和 Web 登录 Cookie 双认证。AI 客户端可以直接调用 `morelian_*` 工具完成"列目标 → 建会话 → 执行命令 / 读写文件 / 侦察 / 隧道 / 生成载荷"，不用人肉在界面上点。CyberStrikeAI 启动时会自动把它登记成外部 MCP，侧栏「C2 → Morelian 控制台」内嵌的就是 morelian 本体。

## 三、CyberStrikeAI 二开版 1.0

这个才是这次的主角。上游是 Ed1s0nZ/CyberStrikeAI，Apache-2.0，Go + Eino 的单/多智能体交战框架，知识库、HITL 审批、审计这些核心能力都是上游的。二开版没有推翻上游的智能体 / 工具 / 审批架构，主要做三件事：**接自家工具、补信息收集、沉淀漏洞情报**。

### 1. C2 交给 EasyShell，WebShell 交给 MoreLian

原来平台自带一套 C2 和一套 WebShell 管理，二开版直接把这两块整体移除（相关代码、路由、MCP 工具都不存在了），改成：

* **C2 通道 = EasyShell**

  启动时自动把本机 `easyshell-mcp/server.py` 登记为外部 MCP（条目名 `easyshell`，工具前缀 `easyshell_*`）。「系统设置 → C2 设置」填控制台地址和账号，点「保存并登录」后后端按控制台协议（RSA-OAEP + AES-GCM）加密登录换 JWT，写回 MCP 的 `EASYSHELL_TOKEN`。侧栏「C2 → 控制台」整页内嵌 EasyShell 本体，页头带 MCP 状态 / 工具数 / token 有效期。
* **WebShell 通道 = MoreLian**

  同理自动登记 `morelian` 外部 MCP，工具前缀 `morelian_*`；侧栏「C2 → Morelian 控制台」内嵌。
* 两个控制台都优先用 **SSO 登录 URL** 内嵌，不用再配反向代理；只有平台 HTTPS、控制台 HTTP 这种 Mixed Content 场景才自动走同源反代（`/c2/morelian/` 或 EasyShell 对应路径），并原样透传 Bearer。
* 内嵌和 MCP 是两条独立通道：内嵌是给人看的，MCP 是给 AI 用的。填了 SSO 也不影响 MCP 用账号密码登录。

这样三个工具的分工就清楚了：EasyShell 负责植入体、监听器、隧道、钓鱼；MoreLian 负责 loader、WebShell 会话、数据库、目标侧隧道；CyberStrikeAI 负责任务编排、资产和情报。

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNrlGY5XabkaJIAygmiay8c1NUeiawrqhFibkems9gr3qH1gL1vTxiaAkWDbICRKdicSib4YGm4u8cSPN4XnuBGicEmnlwFnDzCRkYDYAk/640?wx_fmt=png&from=appmsg)

### 2. 一键信息收集

这是二开版花时间最多的模块。输入只要一个单位名称 / 域名 / IP，平台自动识别类型，然后按步骤编排：

* 搜索引擎（Bing / 百度 / 360 / DuckDuckGo 等，按需勾选）
* 资产测绘、证书透明（CT）、DNS（A/CNAME/MX/NS/TXT + 泛解析检测）
* 同 C 段扩展、历史域名、股权穿透、备案反查、供应链、公众号/小程序
* 存活与站点标题复核（状态码 / 标题 / Server / 页脚 ICP / 服务指纹）
* 去噪后分类入库，同一单位或同一主域自动归入同一个项目

两种跑法：**AI 逐步收集**（每一步由 AI 根据上一步结果决定查什么，适合没打过的单位）和**固定流程收集**（按勾选步骤跑，适合批量、可复现）。收集完还能直接存成定时任务，按天/周自动跑增量。

说实话这块目前还有瑕疵：搜索引擎的结果质量、测绘 API 的限流、部分站点的 WAF 拦截，都会影响最终入库的数量。我的建议是先用"标准"深度跑一遍，人工看一眼误报，再把有效的步骤固化成定时任务，别一上来就拉满。

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNozicicWKia5DezcR742Uo8EvHvj83icH9A7J6kh55Od8Z2rBwYW3ocv7MQTROHQsgNsIHYCgviaUhJAhmSwGict3DZN6Qp5wZEI1oibI/640?wx_fmt=png&from=appmsg)

### 3. 增加执行节点

以往扫描测试均为主机自身进行执行，这样很容易就会导致主机被标记，现在通过执行节点进行渗透测试，有利于保护管理端。

支持多节点绑定，以及一键安装工具和直接进...