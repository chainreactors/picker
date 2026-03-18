---
title: HIDS AWD Platform
url: https://mp.weixin.qq.com/s/JN54w2LSuBxmY8fNeIbubQ
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:16:38.520114
---

# HIDS AWD Platform

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VCJKZk7RleP2AXjuicRK6FSOGvBrR0Gg4Jr7chjEMVTgeqexhp8noB7w1VHefeicGy3EaNHmC1Tk3pGaN7DTrON8mOHV4xXfpRhGAALia2msP8/0?wx_fmt=jpeg)

# HIDS AWD Platform

攻防训练营

![]()

在小说阅读器中沉浸阅读

## HIDS AWD Platform

面向 AWD 比赛的轻量级 HIDS 平台，包含：

* **Builder（管理端）**：构建 Agent、管理多台靶机、代码审计、自动修复、WAF 流量查看等。
* **Agent（靶机端）**：文件基线监控、自动备份/还原、进程监控、Web 目录流量记录（WAF）、远程文件/终端等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VCJKZk7RleMmEJZS6wmmicRZ7a81NsrpA6oqRENTicadx71ZIbRaDSJheCvNk67wYLpvSAjc7aEXiaiaJeEr19AdKVBuchQLXZyJO1vrI0aNduc/640?wx_fmt=png&from=appmsg)

**Agent 构建与管理**

* Web 界面一键生成适配目标系统的 Agent（二进制）。
* 自动嵌入配置。
* 多靶机在线状态、开放端口展示。
* Web 端远程终端、远程文件管理、下载 Web 目录源码 ZIP。

![](https://mmbiz.qpic.cn/mmbiz_png/VCJKZk7RleNNaicMcibGCZySXibx3EBIs1r4PVqNokYmHvPydlZdnuG5iaNFY4nAJuRx9yJDtSKZUl1FolMQORnXsKAOo3sBHgdbqCMLwBqRIZM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/VCJKZk7RleNZ9M3UrlrVAQ6xh6hycezKvYqhHWib6CdB8tZHu4J42es8b2Bib6xcDiapibuj4z6JwnPMZebv62lkcxuQVcJOQJficYYpVefc8cTk/640?wx_fmt=png&from=appmsg)

**文件/进程 HIDS（适配 AWD）**

* 文件基线：首轮扫描生成基线，后续变更触发告警。
* 自动备份/还原：开启「全面防护」后，新增文件删除、被改文件回滚到干净版本。

![](https://mmbiz.qpic.cn/mmbiz_png/VCJKZk7RlePPibmhnIgV7xrSwE3rzKVeRZPkhl5aZMebJpIJxCVZuSExtGum33sLIzCPOTJ9bCg0wJazHyrrBpic9MgF9fib7B0QLg4cAvPgps/640?wx_fmt=png&from=appmsg)

**PHP 代码审计 & 自动修复**

* 静态扫描常见 PHP 漏洞：SQL 注入、RCE、XSS、文件包含/下载、XXE、反序列化等。
* **参数可控分析**：基于 source-sink 链路（`$_GET/$_POST/$_REQUEST/$_COOKIE/$_FILES`），跨文件追踪变量赋值，尽量避免“幻觉 source”。
* AI 审计（可选）：接入 OpenAI / DeepSeek / Qwen / Ollama，给出风险分析和修复建议。
* 自动修复 + 回退：

+ XSS → `htmlspecialchars` / 输出过滤
+ SQL 注入 → 参数化/转义
+ RCE / system 调用 → `escapeshellarg` 等
+ 文件包含/下载 → `basename`/白名单
+ 所有修复操作都有「修复记录」面板，可一键回滚。

![](https://mmbiz.qpic.cn/mmbiz_png/VCJKZk7RleOS46uEeMyK4HEeiam9ubkN7v0NeKFJfXibSk9pGG836iagja72w2ibpYIyab70icEhuu7myKaU0MnC48sianMVeVL5lzuSl2s5eibqRc/640?wx_fmt=png&from=appmsg)

**WAF 流量记录（只记录不阻断）**

* 兼容 **PHP 5.4+ / 老框架（含 ThinkPHP）** 的注入方式。
* 自动在 Web 目录下生成随机命名的 WAF PHP 文件（伪装 session 文件），并在入口 PHP 中注入 `@include_once`。
* 强保证：

+ 不输出任何内容（`ob_start` + `ob_end_clean`）。
+ 不污染业务变量（`$_waf__` 前缀 + `unset`）。
+ 不用 `??`、`\Throwable` 等新特性，避免 parse error。

* 记录内容：

+ 方法 / URI / 查询参数
+ 客户端 IP
+ Header（`Host`、`USER-AGENT`、`ACCEPT`、`ACCEPT-LANGUAGE`、`COOKIE` 等）
+ 部分/全部 POST Body（长度限制）
+ 自动标签：`sql` / `rce` / `lfi` / `xss` / `webshell`

* Builder 通过 WebSocket 实时收集，前端提供 **Burp 风格 HTTP 请求包** 查看界面：

+ 左侧请求列表（时间、IP、方法、URI、标签）
+ 右侧完整 HTTP 包，支持手动复制。

![](https://mmbiz.qpic.cn/mmbiz_png/VCJKZk7RlePzU3pNnej5a2bECpicwF51kmC5eaEx6lx1BMiaAQ2ZiaSLOYDAP7MicQ2QHYQC7a8Bc8CPO6qlYn7nbSNM0ynmuhareveiaxUrVXL0/640?wx_fmt=png&from=appmsg)

* **AWD 友好设计**

+ 针对非 root 账号、`www-data` 权限做最小侵入设计。
+ 目录/文件自动排除（`.git`、`vendor`、`node_modules`、`cache` 等）。
+ 所有自动注入的文件/修改路径都登记在 Agent 内部，文件监控不会错误回滚这些「自家代码」。

---

## 各操作系统的运行方式

### Windows

1. **管理端（Builder）**在管理机上解压 `release/windows` 目录，命令行运行：

   ```
   hids-builder.exe-addr:8080
   ```

   然后在浏览器访问：

   ```
   http://127.0.0.1:8080
   或 http://<本机局域网 IP>:8080
   ```

### Linux

1. **管理端（Builder）**

   ```
   chmod+x hids-builder-linux-amd64
   ./hids-builder-linux-amd64 -addr :8080
   ```

   管理机浏览器访问：

   ```
   http://<Linux 管理机 IP>:8080
   ```

### macOS

1. **管理端（Builder）**

   ```
   chmod+x hids-builder-darwin-amd64
   ./hids-builder-darwin-amd64 -addr :8080
   ```

   在浏览器访问：

   ```
   http://127.0.0.1:8080
   ```

## 使用 WAF / 流量面板

### 开启 WAF 流量记录

1. 在「管理」面板的 Agent 卡片，开启功能开关里的「流量记录」。
2. Agent 会自动：

* 在 `monitor_dir` 下生成随机 `.sess_xxxxx.php` WAF 文件。
* 在主要入口 PHP 文件中插入 `@include_once('/绝对路径/.sess_xxxxx.php');`。
* 将这些路径标记为受管路径，文件监控不会回滚或删除。

> WAF 只记录、不阻断，不会主动中断业务请求。

### 查看流量

1. 点击侧边栏的「流量」图标，或在 Agent 卡片点「📡 流量」。
2. 顶部筛选：

* 靶机
* IP（区分不同队伍）
* 仅显示「可疑流量」（有 `sql/rce/xss/webshell` 等标签）

3. 左侧列表显示时间（浏览器本地时间）、IP、方法、URI、标签。
4. 点击一条流量，右侧展示完整 HTTP 请求包（Burp 风格），可手动选择复制用于复现/攻击。

---

## 远程文件 & 下载源码

* 「文件」标签页：

+ 切换靶机、浏览 `monitor_dir`。
+ 在线查看/编辑文件，保存时通过 Agent 的 `AuthorizedSave` 更新基线+备份，避免被自动还原。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VCJKZk7RlePCvBTqzfDXib0pwyZW1UbBFyNJleksJDkn72s6ClenkdDqArMNF9RMrRjfHsDQ2Atuyh0ibLTqH9AdHnTkcicdL7dolO1lasfiatc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/VCJKZk7RleM63AhGOz2QP0oIhyNrJo0PXZOfjKpZuYKKSlcOq9KG9Bxsaw7BG76sx4ia6mLYJIU7WTUrdouQqpbJqyfHiavWricBVVCSezcHlQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HKQyIxgrd4m0Wl7JVxjwvFwWVaNboDZkNSpV1TYaUydSxDnXUHOicQGT1W0licOMxaichMbYBqOBHFzVqBQma6vlQ/0?wx_fmt=png)

攻防训练营

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HKQyIxgrd4m0Wl7JVxjwvFwWVaNboDZkNSpV1TYaUydSxDnXUHOicQGT1W0licOMxaichMbYBqOBHFzVqBQma6vlQ/0?wx_fmt=png)

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