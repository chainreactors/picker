---
title: 一款基于 Pi 的 CTF 自动化解题工具 CTF-BTFly，多模型灵活接入，AI 自主分析 Web/Pwn/ 逆向类题目
url: https://mp.weixin.qq.com/s/eBuuG1jTjgH_VQSbGBKumQ
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:58:07.665068
---

# 一款基于 Pi 的 CTF 自动化解题工具 CTF-BTFly，多模型灵活接入，AI 自主分析 Web/Pwn/ 逆向类题目

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibrevicNauKAV6as5AAJnb1hGJyTaDM2XE04micyqPSy3tk4dQibAvNNBz8FNOOFdhj64ACvrDibPjVfGAicKZHY45yvKl8OOOfICd7b6OVOhAHug/0?wx_fmt=jpeg)

# 一款基于 Pi 的 CTF 自动化解题工具 CTF-BTFly，多模型灵活接入，AI 自主分析 Web/Pwn/ 逆向类题目

huihuilikaile
huihuilikaile

渗透安全HackTwo

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

0x01 工具介绍

CTF-BTFly 是一款开源容器化 AI 自动化 CTF 解题 Agent 工具，采用 Wails 桌面前端搭配 Go 守护进程架构。依托 Docker 沙箱隔离环境，针对 Web、Pwn、逆向、密码学等题型提供专项镜像。接入兼容 OpenAI 协议的大模型，可拖拽附件启动任务，Agent 自主分析文件、调用工具、编写脚本，全程可视化运行日志，解题结束自动生成可复现中文 Writeup。内置短期令牌机制隔离 API 密钥，支持多模型动态配置，适合 CTF 备赛与安全研究场景，仅可在授权靶场环境使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXVFm4uTKxncwMc66XwiaTg2MdtDnKQm0SuA7L7wkaDRjlRZoTWn1qVv781B3W8l1PYwYBRgXan8yPHqdOQee08uT209MvyZXEI/640?wx_fmt=png&from=appmsg)

注意：现在只对常读和星标的公众号才展示大图推送，建议大家把**渗透安全HackTwo**"**设为****星标****⭐️******"**否****则可能就看不到了啦！**

**下载地址在末尾 #渗透安全HackTwo**

0x02 功能介绍

✨核心特点

TF-BTFly 将 GUI 与高权限控制平面分离：

* **Wails + React 桌面端**负责题目管理、状态展示、事件时间线、文件预览、Writeup 和模型用量；
* **独立 Go daemon**负责 SQLite、Docker、任务状态机、模型凭据和 Agent 生命周期；
* **每题一个 Docker 沙箱**，根据题型加载 Web、Crypto、Pwn、Reverse、Forensics 或 Misc 专项工具；
* **Pi RPC Agent**在容器内自主分析附件、执行命令、编写脚本并生成中文 `WRITEUP.md`；
* **本地模型网关**把题目级短期 Token 替换为真实上游 Key，真实密钥不会进入容器或前端。

> 任务事件会先写入 SQLite，再通过 WebSocket 实时推送。前端断线或切换页面后，可以根据单调递增的 sequence 补齐历史。

## 图文说明与更新记录

**使用时需要启动docker desktop，配置镜像文件(下文有教程)，配置env文件(模型baseurl+key+id等信息),打开右上角显示绿色提示灯,模型连接正常，即可开始使用**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXVFm4uTKxncwMc66XwiaTg2MdtDnKQm0SuA7L7wkaDRjlRZoTWn1qVv781B3W8l1PYwYBRgXan8yPHqdOQee08uT209MvyZXEI/640?wx_fmt=png&from=appmsg)

## **拖动题目附件到对应的区域会启动创建题目窗口**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXfALqm2WwDyJ5hBlRic8Zp17ib2Hj6gGzmR8OG300ZHRwQicKDw3K7p5SibiafOc2zmwQ6cvr5dXQJbVyEUgTfcs1lA52XSj7xwcBw/640?wx_fmt=png&from=appmsg)

## ****填入题目信息，选择已经配置的模型，web/pwn/...配置远程地址，flag格式默认是flag{...}****

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVFGXdQV8qcoFtKtfrvxfuBPlPNt2lkgSQFHzTtdJLHtHJ3VAT8zM3o31x9SCVBTo5DaJv9MESmibTTzibkAo9s8WNDibib2QiboUDc/640?wx_fmt=png&from=appmsg)

## ****题目创建好启动agent即可****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWPd05icvCrab1FiaS5swhib0D0r5mj3uI1u5uao45LMbAv94yTJz56kgArsicFg7TCUKI5OTMNZhHerLgCBpsqFTUkG5utpDUfjlo/640?wx_fmt=png&from=appmsg)

## ****提示词 可以在这里暂停增加新的提示****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWNBIFYAPYJoP9nP2CaiaOIrHHEEyvnHdAQr7nD2dkN37OuFEAE0pGaVLh7LELA1LGyKF2MPCgvnd2ianAiajFWOmeLjyLB9xaibHQ/640?wx_fmt=png&from=appmsg)

## ****解题过程 显示ai执行的一系列操作和思考过程 右上角可以暂停和中止 显示解题时间****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAV7YMBXKPS4tCia5BDF6vluwGFAumZYU5nu7UxPPP20v3oWn8kvFkibcsdt4KpUd3CQg4Jo5Uy16zjicNENSfk1qCGfsdazR26GRw/640?wx_fmt=png&from=appmsg)

**终端和文件会显示工具执行的信息，产生的文件，文件允许下载**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXCRw8eyOIddXbkkl44FG3qw6SSg0lloq7UW6ME8H5VGR5xDXuPncianyR8uCnAYUSjf8ticjUuicp52QpBjxA3wP0u6LHT6KZtPU/640?wx_fmt=png&from=appmsg)

## ****wp 解题成功后会自动编写wp 允许下载****

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAX7MKls5rmCdhOYBXtaFWy8BOUFgXSjn4j4abvQ20roQsKDyr8iaibWraywOUwy2RCwooZ7z5wU2bqiazFicJYPxDj3uMIhk0Z1KAA/640?wx_fmt=png&from=appmsg)

## **题目卡片可以删除题目 可以选择是否保存wp**

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXosfzqichOEQANsAXdAMHI9s9uAQRvrgxOh8tr99gPuf7qIibEn1DeCYL6zB6iaJqQiaLIWRoMcwzxWOAicic5Ib5MJIV0tibgmgqp8A/640?wx_fmt=png&from=appmsg)

## 0x03 更新介绍

```
优化体验
```

0x04 使用介绍

📦安装与使用指南

### 安装 Docker Desktop

* 下载并安装 Docker Desktop
* 启动 Docker Desktop，确保 Docker 引擎正常运行
* 建议配置国内镜像加速，以提升镜像构建速度

### 获取程序文件

构建完成后，程序位于 `bin/` 目录

```
bin/├── CTF-BTFly.exe          # GUI 桌面端└── ctfagent-daemon.exe    # 后台守护进程
```

> GUI 启动时会自动检测并连接已有 daemon；未检测到可用实例时，将自动启动同目录下的 `ctfagent-daemon.exe`。

## 配置模型网关

在 `CTF-BTFly.exe` 所在目录创建 `.env` 文件（开发构建默认产物位于 `bin/`，因此通常创建 `bin/.env`）：

### 单模型配置

```
CTF_UPSTREAM_MODEL_BASE_URL=https://your-openai-compatible-endpoint/v1CTF_UPSTREAM_MODEL_API_KEY=your-real-provider-keyCTF_MODEL_ID=your-model-idCTF_MODEL_INCLUDE_STREAM_USAGE=trueCTF_MODEL_SUPPORTS_IMAGES=false
```

### 多模型配置（推荐）

```
CTF_MODELS=deepseek,visionCTF_DEFAULT_MODEL=deepseekCTF_MODEL_DEEPSEEK_BASE_URL=https://api.deepseek.com/v1CTF_MODEL_DEEPSEEK_API_KEY=your-deepseek-keyCTF_MODEL_DEEPSEEK_ID=deepseek-chatCTF_MODEL_DEEPSEEK_SUPPORTS_IMAGES=falseCTF_MODEL_VISION_BASE_URL=https://your-vision-endpoint/v1CTF_MODEL_VISION_API_KEY=your-vision-keyCTF_MODEL_VISION_ID=your-vision-modelCTF_MODEL_VISION_SUPPORTS_IMAGES=true
```

> ⚠️ **安全提醒**：`.env` 包含真实模型密钥，**不要**提交到 Git、复制进 Docker 镜像或放入题目工作区。

### 可选环境变量

| 环境变量 | 必填 | 默认值 | 作用 |
| --- | --- | --- | --- |
| `CTF_UPSTREAM_MODEL_BASE_URL` | 是 | — | OpenAI-compatible API 基础地址 |
| `CTF_UPSTREAM_MODEL_API_KEY` | 是 | — | 真实上游 API Key，仅 daemon 持有 |
| `CTF_MODEL_ID` | 是 | — | Agent 使用的模型 ID |
| `CTF_MODEL_INCLUDE_STREAM_USAGE` | 否 | `true` | 流式请求加入 `stream_options.include_usage` |
| `CTF_MODEL_SUPPORTS_IMAGES` | 否 | `false` | 仅在上游兼容 OpenAI `image_url` 时设为 `true` |
| `CTF_AGENT_ENV_FILE` | 否 | 程序同目录 `.env` | 显式指定 daemon 配置文件 |
| `CTF_AGENT_DATA_DIR` | 否 | 程序同目录 `data/` | 覆盖 SQLite、日志和工作区目录 |
| `CTF_DAEMON_ADDRESS` | 否 | `127.0.0.1:18731` | daemon 监听地址 |
| `CTF_DAEMON_TOKEN` | 否 | 自动安全生成 | 覆盖本地控制平面 Token |

## 构建专项镜像

打开 PowerShell，执行构建脚本：

```
.\images\build.ps1 -Version 0.1.0
```

* 首次构建需下载 Node、Python、Debian 软件包及各题型工具
* 构建耗时取决于网络环境与 Docker 缓存
* 构建完成后将生成以下题型镜像：

| 题型 | 镜像名称 | 代表工具 | 目标运行时 |
| --- | --- | --- | --- |
| Web | `ctf-agent-pi-web:0.1.0` | Nmap、SQLMap、Gobuster、WhatWeb | gVisor |
| Crypto | `ctf-agent-pi-crypto:0.1.0` | John、gmpy2、PyCryptodome、SymPy、Z3 | gVisor |
| Pwn | `ctf-agent-pi-pwn:0.1.0` | GDB、QEMU、Pwntools、Ropper、Checksec | Kata/VM |
| Reverse | `ctf-agent-pi-reverse:0.1.0` | Apktool、angr、GDB、Strace、Ltrace | gVisor/Kata |
| Forensics | `ctf-agent-pi-forensics:0.1.0` | Binwalk、Tshark、Yara、Sleuth Kit、Volatility | gVisor/Kata |
| Misc | `ctf-agent-pi-misc:0.1.0` | FFmpeg、ImageMagick、Steghide、ZBar、SciPy | gVisor |

> 镜像详细说明见 `images/README.md`。

## 启动与验证

### 1. 启动程序

```
双击运行 CTF-BTFly.exe，桌面端将自动连接 daemon。
```

### 2. 验证模型连接

* 打开程序后，查看右上角状态指示灯
* **绿色** = 模型连接正常，可以开始使用
* **红色/灰色** = 请检查 `.env` 配置及网络连接

### 3. 模型管理（可选）

在「系统概况 → 模型连接 → 管理模型」中：

* 新建或编辑多模型配置
* 界面仅显示 URL、模型 ID、能力开关和"密钥已设置"状态，**不会回显 API Key**
* 保存或点击"重新读取并检测"将原子热更新模型池
* 新配置立即出现在检测模型和新建题目下拉框中
* 运行中题目仍保留原连接和短期 Token，无需重启 daemon/桌面程序

**0x05 内部VIP星球介绍-V1.5（福利）**

如果你想学习更多**渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等**欢迎加入我们**内部星球**可获得内部工具字典和享受内部资源和内部交流群，****每天更新1day/0day漏洞刷分上分******([2026POC更新至12922+](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect))****，**包含全网一些**付费扫描****工具及内部原创的Burp自动化漏****洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等**。shadon/Hunter/0zone/Zoomeye/Quake/Fofa高级会员/AI账号/CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复" **星球** "有优惠券名额有限先到先得**❗️**啥都有**❗️**全网资源最新最丰富**❗️****（🤙截止目前已有3000+多位师傅选择加入❗️早加入早享受）**

最新漏洞情报分享：https://t.zsxq.com/DSAvv

**👉****[点击了解加入-->>内部VIP知识星球福利介绍V1.5版本-1day/0day漏洞库及内部资源更新](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect)**

结尾

# 免责声明

# 获取方法

**公众号回复**20260804**获取下载、回复 加群 获取交流群**

# 最后必看-免责声明

文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！

---

# 往期推荐

**1.[内部VIP知识星球福利介绍V1.5（AI自动化）](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect)**

**2.[CS4.8-CobaltStrike4.8汉化+插件版](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247483949&idx=1&sn=cae68096be06be4f0ea746ee5908dc79&scene=21#wechat_redirect)**

**3.[全新升级BurpSuite2026.4专业(稳定版)](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247498687&idx=1&sn=61c2f88f87221eb2b9316bdedf6c0b33&scene=21#wechat_redirect)**

**4.[最新xray1.9.11高级版下载Windows/Linux](http:...