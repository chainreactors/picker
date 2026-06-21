---
title: 新型无代码攻击曝光：AI结合Telegram，普通攻击者也能远程控制肉鸡
url: https://mp.weixin.qq.com/s/MKFH_Kk0p4vVrneoXgEkCA
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:49:02.306015
---

# 新型无代码攻击曝光：AI结合Telegram，普通攻击者也能远程控制肉鸡

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PDTkxnOsuNBicTrILV86p472vQynnF8zzHHW3oIf306FjM8QGGf0ywssFicxRfLGPPegAuPQVWUTUKXO9QjdJehtKXFYhEKR0to/0?wx_fmt=jpeg)

# 新型无代码攻击曝光：AI结合Telegram，普通攻击者也能远程控制肉鸡

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MKR5uVA8JarEwEqp3DUoqlmnXajicJjGicUVicHt7kibGzapRt0L27WUFVNkGoEKLiaC6NQkjVw9NHpp4qib2OpVbufTOokXcPTS0h4/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618185&idx=1&sn=e7a4ddec94c9af10451bca515c67e228&scene=21#wechat_redirect)

> **导语**：传统网络攻击需要攻击者具备编程能力，能写代码、懂命令——但现在，连一行代码都不会写的人，也能当黑客了。Palo Alto Networks威胁情报团队Unit42近日披露一起新型攻击：攻击者只需在Telegram里输入"下载这个文件"，AI就会自动把它翻译成具体的命令，在受害者电脑上执行。整个过程攻击者不需要任何技术背景，杀毒软件也完全检测不到。

---

## 一、攻击原理：AI当翻译， Telegram当指挥中心

这种攻击的核心思路非常巧妙，用大白话说就是：**攻击者不需要会写代码，AI帮他翻译**。

传统黑客攻击，攻击者需要自己写恶意程序、懂命令行语法。而这套攻击框架完全颠覆了这个模式：

**攻击者的操作界面，就是我们每个人都在用的 Telegram（电报）。** 攻击者只需要在 Telegram 里给机器人发文字指令，比如"查看主机名"、"扫描网络"，这个机器人会把指令发给 AI（这里用的是 Groq 的 Llama 大模型），AI 瞬间把文字翻译成真正的 shell 命令（比如 `hostname` 或 `nmap`），然后在受害者电脑上执行，结果再通过 Telegram 返回给攻击者。

整个过程：

* 攻击者输入：**"帮我扫一下内网有哪些机器"**（自然语言）
* AI 翻译成：`for ip in $(seq 1 254); do ping -c 1 192.168.1.$ip; done`（命令行）
* 受害者电脑执行：真的去扫描
* 结果返回：攻击者在 Telegram 里看到扫描结果

**不需要懂任何代码。** 这就像给一个完全不懂外语的人配了个同声传译，他说什么，AI 就帮他翻译成目标语言执行。

![Telegram + AI 无代码攻击原理图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NjzXRxFktJN0ck2ytibqibFXDrhiargnHZ1QRuNt7UM6to65mL6pesNHFdGRbqZVAqCk761icMXmRY5oIjxsExTjibIn6Ddocpx4r8/640?wx_fmt=png "Telegram + AI 无代码攻击原理图")

---

## 二、为什么这个攻击如此隐蔽？

### 1. 流量完全"正常"，根本拦不住

传统木马需要自己建立"指挥控制通道"（C2），比如连接攻击者自己的服务器。这种流量是独一无二的，安全设备很容易识别。

但这个木马的 C2 通道就是 **Telegram 本身**。所有通信都是 HTTPS 流量发往 `api.telegram.org`——你每天刷微信、发消息的流量和这个一模一样。安全设备看到的是用户在用 Telegram，看不出任何异常。

**根本没有域名或 IP 可以封禁。** 总不能把 Telegram 的域名加黑名单吧？

### 2. 杀毒软件完全失效

截至 2026 年 6 月 8 日，这枚木马的 SHA256 哈希值在 VirusTotal（全球最大恶意文件检测平台）上 **0/63 检测**——63 款主流杀毒软件，没有一个能发现它。

原因是：传统的杀毒软件靠"病毒特征码"识别恶意程序，但这枚木马根本没有固定特征——每次 AI 生成的命令都不同，特征码无法匹配。

### 3. 文件窃取像"发文件"一样自然

从受害者电脑偷文件时，文件是通过 Telegram 的 **文件上传功能** 发回来的。在 Telegram 对话里，你给朋友发一个文件，和攻击者通过木马发回一个偷来的文件，从技术上看完全一样。

---

## 三、攻击四个阶段详解

### 阶段一：上线即暴露——机器一中毒，攻击者就知道了

木马在受害者电脑上首次运行时，会立即收集以下信息：

* **公网 IP 地址**（通过 ipify.org 查询）
* **操作系统名称和版本**
* **当前登录的用户名**
* **主机名**

这些信息在攻击者还没发出任何命令之前，就通过 Telegram 发给了攻击者。这让攻击者在正式行动前，对"目标是谁、在哪、什么系统"了如指掌。

### 阶段二：Telegram 机器人——唯一的 C2 通道

木马每隔 5 秒向 Telegram 机器人轮询一次，看攻击者有没有发新指令。30 秒超时。

**关键点：只有预设的那个"操作者 Chat ID"发来的消息才会被执行。** 这相当于一个最简单的身份验证——只有持有正确 ID 的人才能控制这台肉鸡。

所有通信走的是 Telegram 官方 API，流量和普通用户使用 Telegram 没有任何区别。

### 阶段三：AI 翻译层——把大白话变成命令

攻击者的每条消息都会被转发给 Groq 平台上的 Llama-3.1-8B 大模型，AI 返回一个**动作令牌**（action token），本质上就是一条 shell 命令，或者内置动作如 `DOWNLOAD_FILE`、`SCAN_NETWORK`、`SCAN_PORTS`。

AI 返回的只有命令本身，不带任何解释或说明。

**Unit42 特别指出一个危险细节**：目前 AI 只被限制在 5 种固定格式内，但只要简单改一下提示词，这个限制就能解除。解除后 AI 可以**随意生成任意代码**，彻底绕过所有基于静态特征的检测。

### 阶段四：执行与数据窃取

* **Windows** 用 PowerShell 执行，**Linux/macOS** 用 bash 执行
* 标准输出和错误信息通过 Telegram 发回给攻击者
* 文件窃取通过 Telegram 的 `sendDocument` 接口上传，单个文件最大 50MB
* 网络扫描覆盖所有 RFC 1918 私有地址段（也就是常见的 192.168.x.x、10.x.x.x 等内网 IP），另外还包括 Docker、APIPA、VPN、iPhone 热点等地址段

---

## 四、关键入侵指标（IOC）

| 类型 | 值 |
| --- | --- |
| **文件 SHA256** | `d85a5c2cf466d01e17110ee39ca456b1be0b6514e669d0095d1f77c84a8d98c1` |
| **LLM API 端点** | `hxxps://api.groq[.]com/openai/v1/chat/completions` |
| **Telegram 轮询端点** | `hxxps://api.telegram[.]org/bot<token>/getUpdates` |
| **Telegram 消息发送** | `hxxps://api.telegram[.]org/bot<token>/sendMessage` |
| **Telegram 文件上传** | `hxxps://api.telegram[.]org/bot<token>/sendDocument` |
| **公网IP查询** | `hxxps://api.ipify[.]org` |
| **LLM 模型** | `llama-3.1-8b-instant` |

> **注**：以上 URL 本身并无恶意，Telegram 和 Groq 都是合法服务，仅当配合特定木马行为时才构成威胁，**不建议仅凭这些 URL 进行封锁**。

---

## 五、这个攻击意味着什么？

这起事件的本质意义，不仅仅是"又多了一个木马"，而是**标志着网络攻击的门槛正在急剧下降**。

过去，做网络攻击需要：

* 会写代码（Python、PowerShell、bash 等）
* 懂操作系统原理
* 能分析流量、免杀、免查

现在，你只需要：

* 有 Telegram 账号
* 会打字
* 花几十块钱买个 Groq API Key

**攻击者不需要任何技术背景，AI 替他做所有技术工作。** 这意味着地下黑产会迅速出现"出租 Telegram 僵尸网络"的服务——买家不需要懂技术，付钱就能用，AI 自动完成所有操作。

对于防守方来说，形势也更严峻：

* 流量完全正常（TLS + Telegram），传统检测手段失效
* 命令每次不同，静态特征无法匹配
* 即使发现异常，也无法封禁 Telegram 这种合法平台

---

## 六、普通人如何自保？

1. **不要下载来源不明的可执行文件**（.exe、.ps1、.sh 等）
2. **开启系统防火墙**，限制非必要的外网连接
3. **关注系统自带安全工具**（Windows Defender 等），保持实时防护开启
4. **警惕 Telegram 上陌生人发的文件**，即使来自"熟人"也要确认身份

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Puc8HNiaVFMibMWyXuRCjam9iat0x1rCpsp1iatD7HveaKn7X0FMG8AlYEYZQbWQjAzjbYJjgdDQYTxLsn3W66vehH9V8LV2z9XnE/640?wx_fmt=jpeg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MjRfVmbtIg1wGprLuiasN8HPIntn1Wc4aJnibIKDrP4LdTrRHHiaFgRKRelgibk10nug8Jcyd64PBN7x2P4ibuc2mERibOZ5PmLP0l8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618370&idx=1&sn=04062f6f20b8c24755eb711f63e2101b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6O1MFqiadPibEFn9dUSxK80IrrA939wuQibKjHfguldRav81hQfCPM7Xtiafac0cnkGEcdnKJQVQ2yu0fEprVl6vYTBveibgAPMNylU/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618166&idx=3&sn=42d553ae19e05e17a57425bafd32452d&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MF50ZvgzStcZwuF3u9D1rVh0MMTueyB0ZZLB39emVRFfPEGicCw7IjPgicCxC3D7hKPDeB3v4dl68ABiarb95h8dTILFSCLZ8n54/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618370&idx=4&sn=17496d177d3e9f5a0bcb209cd40975dc&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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