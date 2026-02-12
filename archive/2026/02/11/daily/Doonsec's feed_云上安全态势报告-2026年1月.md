---
title: 云上安全态势报告-2026年1月
url: https://mp.weixin.qq.com/s/bq84YKwA7KVwn7KMHXkZQg
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:20:15.825888
---

# 云上安全态势报告-2026年1月

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MZs4aE44Gy5ibqwQsiaUPU4dohsTvpy8GsMkvVQ2VZq3nV3TJWOhia40egDc5H5QhQbntZJ0nHtiaurwC6pRYpyVRu5ASaic9VibTBicDL0BjgbdQQ/0?wx_fmt=jpeg)

# 云上安全态势报告-2026年1月

阿里云安全
阿里云安全

阿里云应急响应

![]()

在小说阅读器中沉浸阅读

### 一、平台攻防态势

#### 1. 云平台默认防御水位

默认防御是阿里云平台默认提供的基础防御能力，可基于海量云安全威胁情报，阻断恶意团伙对云上客户的规模性攻击，客户无需手动配置安全防护功能，开箱即享基础安全保护。

2026 年 1 月云平台平均每天为客户

* 防防御攻击次数：68.9 亿次，环比 12 月份 下降 4.7%
* 防御攻击IP数：2.5 万个，环比 12 月份 下降 7.1%

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MZs4aE44Gy7AxSFP9krV4EDtib7G3bAppEAhicoqRsicE96HAFC7Mw1WYLfjHibWyPDL4vib0Fz1oUft56SxtkLaEnd4ibEECzal6VAnicHF14CkfQ/640?wx_fmt=png&from=appmsg)

####

#### 2. DDoS 攻击拦截情况

阿里云平台 1 月共监测并拦截

* DDoS 攻击次数：4.5 万次，环比 12 月份下降 15.8%
* DDDoS 峰值： 2700 Gbps ，环比 12 月份上涨 35.0%

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MZs4aE44Gy7UglEFNGJA9XMYslfRKD1wIQuQicXzqLK0GSDoiaVntaiaibIoFRvvFnzPp1xrCq1UDlEc9nVydAheNc0uRfX114qzibwzpcU4OqdE/640?wx_fmt=png&from=appmsg)

### 二、近期攻击手段与趋势

#### 趋势一：恶意团伙持续攻击PHP-FPM、PostgreSQL，植入恶意程序

近期，阿里云安全团队在云上监测到一个专门针对 PHP-FPM 和 PostgreSQL 服务进行攻击的恶意团伙。攻击者利用以下两类服务的访问控制缺失风险，对云主机实施入侵并部署挖矿程序：

● PHP-FPM 服务暴露风险：未加访问控制的 PHP-FPM（FastCGI）接口可被远程执行 PHP 代码。

● PostgreSQL 未授权访问风险：配置不当的 PostgreSQL 服务允许攻击者在无需认证的情况下执行恶意 命令。

根据该团伙在攻击链和恶意脚本中的特征，我们将其命名为 “VeiMiner”。

1. 全网扫描与精准利用
   攻击者在公网范围内扫描 PHP-FPM 和 PostgreSQL 服务。如果发现可利用的服务，会立即发送恶意命令，执行预置的感染脚本。这些脚本会在目标主机中常驻，并周期性拉取、更新恶意程序。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/MZs4aE44Gy4HBGtLPkk5RJvhbvZp7yoBoAPtW2kah5NH6rzbdHLCjicibw4yHU6aI20R0NlrNyFpbwgy3HGj5cuMmK4UxmlFEKWuUH2OlbIN0/640?wx_fmt=png&from=appmsg)

   ```

   ```
2. 恶意命令及标记机制

   攻击脚本通过设置环境变量 `VEI=cg_[标识信息]`，用于标记已感染主机。其中：

1. VEI：环境变量名
2. cg或pg：应用标识，目前观察到的标识主要为cg（php-fpm）和pg（postgresql）
3. [标识信息]：攻击者所攻击目标主机的IP

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/MZs4aE44Gy5ticHNgBjj2cibduCwkHjCLqOmOlT4iaYuQ2r5D2jLYKcZdPUMICeW3Kqf7bccsticnZs7dTaqiaK4UHqBwziblnVDCukSVv0nXzvrA/640?wx_fmt=png&from=appmsg)

3. 驻留及持久化

恶意脚本在执行后，会首先确保目标环境符合运行条件（如 x86\_64 架构、`/tmp` 可执行），并通过解除只读与 noexec 限制、删除系统安全配置文件等方式为恶意程序运行创造条件；随后创建工作目录（如 `/tmp/.perf.c`、`/tmp/.xdiag`）并写入感染标识，完成持久化效果。脚本会从远程服务器下载矿工程序 `/tmp/httpd`后赋予执行权限并后台运行。为防止重复部署和被中断，恶意脚本利用 `.install.pid33` 文件和延时清理机制实现安装过程的互斥与周期性重试，从而在主机上长期稳定维持恶意进程。

```

```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MZs4aE44Gy6ibfFevQyeb2sPnjKbU7894eZVVWvhEp2gkoZ0libuEgo6P4aeETUZ62eiaibWPfVlxjuTJpeHNYuowj6EpFT5xFjWlWHEqSJcU4Y/640?wx_fmt=png&from=appmsg)

#### 防护建议：

* 立即关闭公网可访问的 PHP-FPM 与 PostgreSQL 接口，或限制访问权限
* 在主机侧检查是否存在相关IOC，包括主机文件哈希以及主机连接。

#### 恶意IOC：

06f5325811050e0e76ca40be71d045ca

69a1bcb07a506b778b3ea77ebe3513a9

b9756931ea25b05d7e08d3474bb1f672

200.4.115.1

##### 趋势二：首个AI生成的云原生恶意软件出现（VoidLink ）

VoidLink 是 Check Point Research 于 2026 年初披露的恶意软件框架，其代码结构、多态行为和部署逻辑显示出明确的 AI 辅助生成特征，是目前已知首个专为云环境设计、由生成式 AI 参与构建的攻击平台。该框架以模块化方式运行，可自动识别主流公有云（如 AWS、Azure、GCP、阿里云），并在容器或虚拟机中实现持久化、权限提升及横向移动。

VoidLink 的出现带来两项实质性挑战：

1. 恶意软件迭代速度进入秒级：利用生成式 AI，攻击者可自动化完成载荷生成、控制流混淆、API 调用伪装等操作，使恶意样本从“周/月级人工开发”转向“分钟/秒级动态生成”，大幅压缩检测与响应窗口。
2. 基于重复性特征的检测机制失效：VoidLink 不依赖 Mirai、Gafgyt 等具有固定代码结构或通信模式的传统框架，而是每次部署均生成唯一变体。这导致依赖文件哈希、YARA 规则、静态签名或网络 IOC 的检测方法因缺乏稳定特征，失效率显著上升。

VoidLink 不仅是一次技术突破，更是对现有安全范式的警示：未来的攻防对抗，将是 AI 与 AI 的较量。

### 三、近期被高频攻击的漏洞

#### （一）新增重要漏洞

n8n Webhook 致远程代码执行漏洞（CVE-2026-21858）

n8n Webhook 是 n8n 自动化工作流平台中的一种触发节点（Trigger Node），用于接收来自外部系统的 HTTP 请求（如 POST、GET 等）从而触发自动化工作流的执行。其存在远程代码执行（RCE）漏洞，未经身份验证的攻击者可构造包含恶意 JavaScript 表达式的 JSON 或 URL 参数，构造恶意 Webhook 请求，在目标服务器上执行任意代码。

影响版本：v1.42.0 以下版本

阿里云安全团队建议，立即排查是否使用低版本 n8n ，如确认使用，请采取以下措施：

1. 升级 n8n 至 v1.42.0 或更高版本
2. 临时缓解措施（若暂时无法立即升级）：利用安全组设置n8n仅对可信地址开放，禁止公网暴露 Webhook 端点

Moltbot（Clawdbot）Gateway 未授权访问漏洞（AVD-2026-1850319）

Moltbot是一款开源的AI 代理与自动化平台。Moltbot 的 Gateway 组件默认信任来自 localhost (127.0.0.1) 的连接，无需密码或令牌即可自动授权。当用户通过反向代理（如 Nginx、Caddy）将其部署到公网服务器时，所有外部请求经代理转发后源 IP 均显示为 127.0.0.1，导致 Gateway 将互联网流量误判为本地连接，从而导致跳过身份验证，攻击者可构造恶意请求利用相关功能执行任意代码控制服务器。

影响版本：v0.9.4 以下版本

阿里云安全团队建议，立即排查是否使用低版本Moltbot，如确认使用，请采取以下措施

* 升级至v0.9.4 及更高版本，并强制启用 Gateway 认证
* 临时缓解措施（若暂时无法立即升级）：

+ 通过安全组/防火墙，禁止公网直接访问 Gateway 端口（默认 18789）；
+ 若必须公网访问，仅允许可信 IP（如办公网段、跳板机）连接。

+ 显式配置可信代理：在 `moltbot.json` 中设置 `gateway.trustedProxies`，仅允许可信反向代理的 IP
+ 网络层最小化暴露

#### （二）其他漏洞列表

云安全中心已支持部分漏洞免费检测，如需更全面的检测能力，也可使用云安全中心企业版进行深度扫描与持续监控。

|  |  |  |  |
| --- | --- | --- | --- |
| 序号 | 漏洞 | 编号 | 是否支持免费检测 |
| 1 | Next.js React Server Components 远程代码执行漏洞（CVE-2025-66478） | AVD-2025-66478 | 是 |
| 2 | xxl-job远程代码执行漏洞 | AVD-2023-1678172  CVE-2024-24113 | 否 |
| 3 | Docker daemon API 未授权访问漏洞 | AVD-2021-346121 | 否 |
| 4 | PHP CGI Windows平台远程代码执行漏洞 | CVE-2024-4577 | 是 |
| 5 | php < 7.1.32 PHP-FPM缺陷配置远程代码执行漏洞 | CVE-2019-11043 | 否 |
| 6 | Redis 未授权访问漏洞 | AVD-02021-0344 | 是 |
| 7 | PostgreSQL任意代码执行漏洞 | CVE-2019-9193 | 否 |
| 8 | Apache ActiveMQ远程代码执行漏洞 | CVE-2023-46604 | 是 |

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fwNqC4xHXIqM8ZJsq2Ja8gNicGZzA8O6q0lPfCQQw64mudJwf7CUtyApwibDT3iaP5GDPxwtvRADE5H5BOsibYdWcg/0?wx_fmt=png)

阿里云应急响应

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fwNqC4xHXIqM8ZJsq2Ja8gNicGZzA8O6q0lPfCQQw64mudJwf7CUtyApwibDT3iaP5GDPxwtvRADE5H5BOsibYdWcg/0?wx_fmt=png)

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