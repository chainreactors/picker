---
title: 别手搓 Burp 编码了——纯 Python WAF 绕过工具 + AI Skill
url: https://mp.weixin.qq.com/s/axuHj3QzxosFv9J-MCLmDw
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:45:09.708679
---

# 别手搓 Burp 编码了——纯 Python WAF 绕过工具 + AI Skill

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eMTyD09PvaaGiaQPCPut8nibfRE5GTdbNRuvruFGyaUiaIANwg0ic5icT27V6BryEpQ4Xsmezvo1zQ2N7j5NkDU4QGa9XVaZfX8uGdicAklaPF634/0?wx_fmt=jpeg)

# 别手搓 Burp 编码了——纯 Python WAF 绕过工具 + AI Skill

原创

whoami0002
whoami0002

SecurityPaper

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## WAF 又 403 了？我让 AI 自动试了 13 种编码，EBCDIC 直接过

> 公众号回复「wafbypass」获取工具下载地址

---

做渗透的人都有这种时刻：

洞找到了，payload 在 Burp 里构造好了，一点 **Send**——

**403。**

WAF 阻断页，签名命中。

换注释、换大小写、双重 URL 编码，WAF 跟开了天眼一样，照样拦。

你以为 payload 不够强，其实问题往往在别处——

**WAF 只按它「看得懂的编码」扫描请求体。** 你发的是 UTF-8 明文，它当然认得。

但如果把 body 编成 **EBCDIC 字节流**，再在 `Content-Type` 里写上 `charset=ibm037` 呢？

很多 WAF 根本不会按 charset 去解码 body，只扫原始字节——签名对不上，**放行**。后端框架却老老实实按 charset 还原，payload 照样进应用层。

这就是经典的 **字符集编码绕过**（Charset-based WAF Bypass）。

手工在 Burp 里一个个改编码，又慢又容易漏。所以我们做了 **WAFBypassEncoder**，并且封装成了 **AI Agent Skill**——以后 payload 被挡，Agent 自己知道该怎么绕。

---

## 一、到底在绕什么？

原理就两步：

1.**把 body 换成 WAF 不解析的字符集**2.**在 Content-Type 里声明对应 charset，让后端解码还原**

**明文请求：**

```
POST /apiContent-Type: application/json{"payload":"<script>alert(1)</script>"}        ↓   WAF 拦截，403
```

**编码请求：**

```
POST /apiContent-Type: application/json; charset=ibm037body 变为 EBCDIC 字节流        ↓   WAF 放行 → 后端按 charset 解码 → payload 还原
```

不是 0day，是 WAF 和后端对编码理解不一致的老缝隙。**实战中，依然好使。**

---

## 二、13 种编码，哪几种真能打？

工具内置 13 种字符集，一条命令全部 fuzz，不用在 Repeater 里逐个手试。

### ✅ 优先打这三类，命中率最高

| 编码 | 原因 |
| --- | --- |
| **EBCDIC** （IBM037 / IBM500 / IBM1026） | 字节值完全改变，绝大多数 WAF 不会解析大型机编码 |
| **UTF-16 / UTF-32** 全系 | 宽字符打散 ASCII 签名，WAF 很难匹配 |

建议先跑这三类，命中就不用等 13 个全跑完：

```
--encodings "EBCDIC,UTF-16,UTF-32"
```

### ❌ 通常没啥用的

| 编码 | 原因 |
| --- | --- |
| UTF-7 | ASCII 子集保持不变，签名还在，常被拦 |
| ISO-8859-1 / Windows-1252 | 单字节，ASCII 范围与明文相同，基本绕不过 |

---

## 三、工具介绍

**WAFBypassEncoder** — 纯 Python，零第三方依赖，四个子命令：

| 命令 | 用途 | 联网 |
| --- | --- | --- |
| `list` | 列出 13 种编码 | ❌ |
| `encode` | 离线生成编码请求，丢 Burp 重放 | ❌ |
| `fuzz` | 批量发送全部编码，输出彩色状态表（核心） | ✅ |
| `file` | 从 Burp 导出的原始请求文件直接 fuzz | ✅ |

**几个实用功能：**

•`--json` 输出，方便脚本和 AI Agent 解析•`--detail` 打印首个 bypass 的完整请求和响应，确认不是假 200•`--save-requests` 把每个编码请求存成 `.req` 文件，批量导入 Burp Repeater•自带 `test_server`，本地模拟 WAF + 后端，不打真目标也能验证工具行为

---

## 四、三条命令上手

### 1. 看支持哪些编码

```
python wafbypass.py list
```

### 2. 核心用法：对目标一键 fuzz

```
python wafbypass.py fuzz --target https://目标地址/api \  --body '{"payload":"<script>alert(1)</script>"}'
```

跑完出一张状态表，类似：

```
IBM037 ...... 200  ✓ bypassUTF-16LE .... 200  ✓ bypassUTF-7 ....... 403  ✗ blockedISO-8859-1 .. 403  ✗ blocked
```

### 3. 离线出包，导入 Burp 手打

```
python wafbypass.py encode \  --body '{"payload":"<script>alert(1)</script>"}' \  --encoding IBM037
```

> ⚠️ **Windows 用户注意**：运行前在 PowerShell 执行 `$env:PYTHONUTF8=1`，否则控制台可能因 GBK 编码报错。

---

## 五、怎么判断「真的绕过了」？

看到 200 先别激动。

**正确打法：**

1.先发一条明文 payload，记基线（通常 403）2.跑 fuzz，找状态码发生变化的编码3.加 `--detail` 看响应体，排除 WAF 返回的假 200 阻断页4.确认 payload 真的到了应用层——绕过 WAF 只是过了门禁，漏洞还得继续验证

**状态码怎么读：**

| 状态码 | 攻击侧解读 |
| --- | --- |
| **200** | 有戏，继续验证业务影响 |
| **403** | 这类编码没用，换 EBCDIC 或 UTF-16 |
| **400** | WAF 可能已经过了，但后端不认这个 charset，换 Content-Type 或编码族再试 |
| **ERR** | 网络或目标问题，跟编码无关 |

---

## 六、接 AI Skill：让 Agent 自动绕 WAF

这个工具不只是命令行脚本——我们把它写进了 **Cursor / Claude Agent Skill**。

**实际效果：** 你在 Cursor 里做渗透，payload 被 WAF 挡了，不用翻笔记、不用手敲 13 条命令。Agent 读到 Skill 就知道——

> **403 + body 里有攻击 payload → 自动调 wafbypass fuzz**

**Skill 里封装了完整打法：**

•**什么时候该用**：SQLi / XSS / RCE payload 被 WAF 拦截•**什么时候别用**：payload 在 URL 参数里、GET 无 body 的请求•**优先试哪些编码**：EBCDIC → UTF-16 / UTF-32•**怎么读结果**：先记明文基线，结合 `--detail` 看响应体•**怎么接后续**：fuzz 出 bypass 编码 → encode 生成重放包 → 继续验证业务影响

**典型自动化流程：**

```
Burp / sqlmap 打出去 → 403        ↓Agent 调 wafbypass fuzz --json        ↓从 JSON 里筛 status_code 为 200 的 encoding        ↓encode 出原始请求 → Burp Repeater 复现 → 继续打链
```

> **WAF 绕过这种重复体力活交给工具，Agent 负责判断该不该绕、绕完怎么验。** 这才是渗透 + AI 的正确打开方式。

---

## 七、几个实战场景

### 场景 1：JSON 接口打 XSS / SQLi，一直 403

```
python wafbypass.py fuzz -t https://target/api/search \  --body '{"q":"<script>alert(1)</script>"}' \  --encodings "EBCDIC,UTF-16,UTF-32" --detail
```

### 场景 2：Burp 已经抓好包，直接 fuzz

```
python wafbypass.py file request.txt -t https://target/api --save-requests out/
```

`out/` 目录里每个编码一个 `.req` 文件，导入 Repeater 逐个看。

### 场景 3：sqlmap 被 WAF 拦

用 `encode` 生成能 bypass 的编码 body，喂回 sqlmap 的 `--data` 参数；或 `--save-requests` 批量导出后逐个试。

### 场景 4：本地验工具，不打真目标

```
# 终端 1python test_server.py
# 终端 2python wafbypass.py fuzz -t http://127.0.0.1:9090/api \  --body '{"payload":"<script>alert(1)</script>"}'
```

明文 403，EBCDIC 和 UTF-16 一串 200——工具正常，再上真目标。

---

## 八、使用边界

•**只编码请求 body**，URL 参数里的 payload 不在处理范围•**GET 无 body** 会直接报错，别硬怼•**不支持代理参数**，要走 Burp 请用 `encode` 或 `--save-requests` 导出后手重放•**绕过 WAF ≠ 打穿**，后面还得确认漏洞真实影响

---

## 九、合规声明

> 本工具仅用于已授权的安全测试，包括渗透测试、SRC、CTF、安全研究。`fuzz` 和 `file` 命令会向目标发送真实 HTTP 请求，请勿对未授权系统使用。

---

## 写在最后

WAF 挡住的往往不是没洞，是 **你和 WAF 说的不是同一种语言**。

WAFBypassEncoder 做的事很直白：把 body 翻译成 WAF 看不懂的字节，13 种方案批量试，告诉你哪种能进门。

再加上 AI Skill，Cursor 里 Agent 自动识别「该绕 WAF 了」——**fuzz → encode → 重放 → 验证，一条龙。**

下次 403，别急着改 payload。

**先换编码，让工具替你试。**

---

> 关注本公众号，回复「**wafbypass**」获取工具下载地址和使用文档。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iazag5vDeG2exlukbZwEVKyIohKDySVQPQXJw5KrBSsqITHv1B8mjkLrJ0vJlibicfsHng5MPDsIGD4biaRjziaZX8g/0?wx_fmt=png)

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