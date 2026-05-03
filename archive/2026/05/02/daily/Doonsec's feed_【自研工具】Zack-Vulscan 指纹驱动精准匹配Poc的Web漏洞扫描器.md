---
title: 【自研工具】Zack-Vulscan 指纹驱动精准匹配Poc的Web漏洞扫描器
url: https://mp.weixin.qq.com/s/TXhust1HL_dEtKZPltwyCQ
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:27:01.322653
---

# 【自研工具】Zack-Vulscan 指纹驱动精准匹配Poc的Web漏洞扫描器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D5oXMbxlRk0arYFBKtChQjsv9tTn7jnS2ia3UXKVHAoicciceNXicia2ictErA6alGPG3VSjyARMWxCia4g6NYhLyazDTu6eicOjr9qkPs8eRslOpeE/0?wx_fmt=jpeg)

# 【自研工具】Zack-Vulscan 指纹驱动精准匹配Poc的Web漏洞扫描器

原创

ZackSecurity
ZackSecurity

ZackSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

---

# 不是另一个"全Poc扫描器"——而是一台精准的漏洞猎杀引擎。

![version](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6lBk71FuyDBjGemvtic1c1aqyGugWPYCsbIgb6P36biaKThUJ1mwWEffUYGv0wXI13kfbuyF5sr9ruC37TI8ojeFwbibOpYon7oibKd0M9zETcGw/640?wx_fmt=svg&from=appmsg)

---

## 工具概况

Zack-Vulscan 是一款基于**指纹驱动精准匹配**的 Web 漏洞扫描器。它在发起任何攻击之前，先通过 11,158 条指纹规则识别目标的技术栈，再利用倒排索引将 6,465 个 PoC 精确匹配到对应的技术组件，最终执行并发漏洞扫描并输出交互式 HTML + XLSX 双份报告。

```
Zack-Vulscan v1.0
├── 11,158 条指纹规则（覆盖主流 CMS、框架、中间件、IoT 设备、安全产品）
├── 6,465 个 PoC（兼容 Nuclei YAML 格式）
│   ├── 3,966+ CVE PoC（2000-2026）
│   ├── CNVD 国内漏洞库
│   ├── 产品专项（WordPress / Spring / ThinkPHP / VMware / Jenkins / ……）
│   ├── 通用漏洞（XSS / SQLi / LFI / 命令注入 / SSRF / SSTI / ……）
│   └── 信息泄露 / 配置缺陷 / 管理面板 / 默认口令 / 子域名接管
├── 35 条指纹黑名单（过滤 jQuery / Bootstrap / Nginx 等泛化框架）
├── 22 个动态函数（rand / hash / encode / string）
├── 5 种匹配器（word / regex / status / dsl / binary）
├── 5 种提取器（regex / dsl / json / kval / xpath）
├── 3 种 Payload 爆破模式（batteringram / pitchfork / clusterbomb）
└── 批量 OOB 验证 + 自定义 XPath 引擎 + DSL 求值器
```

> 全部编译为单个可执行文件（~15MB）。无需 Python 环境，无需 `pip install`，无需 Docker。
>
> **支持平台**：`windows-amd64` · `linux-amd64` · `darwin-arm64` (Apple Silicon)

### 核心工作流

```
┌───────┐    ┌────────┐   ┌───────┐   ┌───────┐
│Phase 1     │   │   Phase 2    │   │  Phase 3   │   │  Phase 4  │
│资产存活      ─▶   指纹→PoC  ─▶  并发漏洞    ─▶  报告生成 │
│检测           │   │  精准匹配   │    │  执行        │   │                 │
└───────┘    └────────┘   └───────┘   └───────┘
 HTTP探测              倒排索引             并发执行            双份报告
+TLS证书             +关键词提取       +DSL匹配          HTML+XLSX
+favicon哈希       +噪声过滤          +OOB批量验证
+指纹布尔匹配     +变体生成          +Flow多步链
```

| 参数 | 说明 |
| --- | --- |
| `-u` | 单个目标 URL / IP / 域名（必填，与 `-f` 二选一） |
| `-f` | 资产文件路径，每行一个目标（与 `-u` 二选一） |
| `-t` | 并发线程数（默认 50） |
| `-timeout` | HTTP 请求超时秒数（默认 5） |
| `-o` | 报告输出目录（默认 `./output`） |

---

## 技术亮点

1. **倒排索引 + 噪声过滤的指纹→PoC 匹配**：不是简单的字符串包含，而是词边界感知的双向匹配 + 30% 噪声阈值 + 单复数变体生成。匹配精度远超同类产品。
2. **自研布尔表达式求值器**：递归下降解析，正确实现 AND > OR 优先级，支持任意嵌套括号，正则缓存优化。
3. **批量 OOB 验证**：注册所有 OOB 子域名 → 等待 10 秒 → 一次 API 调用完成所有验证。对比逐 POC 轮询，API 调用量从 O(n) 降为 O(1)。
4. **完整 DSL 引擎**：18+ 内置函数，支持 `contains()` / `starts_with()` / `ends_with()` / `regex()` / `len()` 以及 `==` / `!=` / `>=` / `<=` / `>` / `<` 比较操作符。
5. **自定义 XPath 提取器**：无需第三方 XML 库，纯 Go 实现的 HTML 节点遍历引擎，支持绝对路径、后代搜索、属性选择器、位置索引。
6. **复合多请求匹配**：一个 PoC 多个 raw 请求时，所有响应合并后统一匹配——捕获单请求无法确认的漏洞模式。
7. **智能协议探测**：HTTP/HTTPS 自动切换，非标准端口多策略回退。
8. **连接池复用**：HTTP 客户端按配置缓存，`MaxIdleConns: 100`，避免 TCP 握手开销。

---

## 适用场景

* 🛡️ **红队打点**：快速识别目标技术栈，只打精准 PoC
* 🔍 **安全评估**：批量资产漏洞巡检，自动生成双份报告
* 🏗️ **SDL 集成**：CI/CD 流水线中的自动化安全测试节点
* 🎓 **安全研究**：6,465 个 PoC 库，涵盖 20 年的 CVE 历史

---

## 痛点：传统扫描器为什么让你白等半小时？

市面上的漏洞扫描器，工作方式大同小异：拿到一个目标 → 把所有 PoC 逐个往上怼。你有 6000 个 PoC，它就发 6000 个请求；你有 100 个目标，那就是 60 万次 HTTP 交互。

**问题是**：一个 WordPress 站点的 Log4j PoC 能打出什么？什么都打不出。它只是浪费了一个 HTTP 往返，还拖慢了整个扫描流程。

这就是所谓的 **"盲扫"困境**——扫描器不知道目标是什么，所以它必须假设目标是一切。

**Zack-Vulscan 从根本上改变了这个公式。**

---

## 核心理念：先认识，再攻击

Zack-Vulscan 的工作流程可以概括为一句话：

> **先搞清楚你是谁，再决定用什么武器对付你。**

这不是一个"发现漏洞"的工具，而是一个**四阶段漏洞猎杀流水线**。

---

## Phase 1：资产存活检测 —— 给你的目标拍一张"CT 扫描"

在你对目标发起任何攻击之前，Zack-Vulscan 已经在默默地收集目标的多维度特征：

| 维度 | 收集方式 | 用途 |
| --- | --- | --- |
| **HTTP 状态码** | GET 请求返回 | 匹配 `status="200"` 指纹 |
| **响应体内容** | 读取前 2MB | 匹配 `body="keyword"` 指纹 |
| **响应头** | 全量散列表 | 匹配 `header="X-Powered-By"` 指纹 |
| **页面标题** | `<title>` 正则提取 | 匹配 `title="管理后台"` 指纹 |
| **Server 头** | `Server` header | 匹配 `server="nginx"` 指纹 |
| **TLS 证书** | Subject + Issuer | 匹配 `cert="Let's Encrypt"` 指纹 |
| **favicon.ico** | MurmurHash3(Base64) | 匹配 `icon_hash="1142584645"` 指纹 |

对，Zack-Vulscan 连目标网站的 favicon 都不会放过。很多 CMS / 框架的 favicon 哈希是独一无二的——一个哈希值就能精确识别"这是用友 NC"还是"泛微 OA"。

### 智能协议探测

目标没写协议？先试 HTTP，不通自动切 HTTPS。非标准端口也给你安排好：

* 80 端口上 HTTP 不通 → 自动尝试同端口 HTTPS → 再尝试 443
* 非标准端口 HTTP 不通 → 先切同端口 HTTPS → 再试 443

整个过程对用户透明。你丢一个 IP:8080 进去，它自己会判断这到底是个 HTTP 服务还是 HTTPS 服务。

### 布尔表达式指纹引擎

Zack-Vulscan 内置了 11,158 条指纹规则，每条规则都是一个完整的布尔表达式。这不是简单的字符串匹配——这是一个**递归下降表达式求值器**，支持：

```
Apache-Log4j → body="log4j"
瑞捷 NGFW  →  ((body="ruijie" || body="锐捷") && (title="NGFW" || title="下一代防火墙"))
Spring Boot →  header="X-Application-Context" && status="200"
```

支持的操作符：

| 操作符 | 含义 | 示例 |
| --- | --- | --- |
| `=` / `==` | 精确/包含匹配 | `body="hello"` |
| `~=` | 正则匹配 | `header~="X-.*"` |
| `!=` | 不匹配 | `status!="404"` |
| `!~=` | 正则不匹配 | `body!~="error"` |
| `&&` | 逻辑且（高优先级） | `body="a" && title="b"` |
| `\|\|` | 逻辑或（低优先级） | `status="200" \|\| status="301"` |
| `()` | 分组 | `(a \|\| b) && (c \|\| d)` |

关键设计：**AND 天然比 OR 优先级高**，不需要背诵优先级表。正则表达式自动缓存到 `sync.Map`，同一模式不重复编译。

---

## Phase 2：指纹→PoC 精准匹配 —— 这才是核心壁垒

Phase 2 是 Zack-Vulscan 的**灵魂**。

### 别人怎么做？

```
目标 → 6000+ PoC 全部无脑跑一遍
      → 耗时 = 6000 × 请求延迟
      → 带宽 = 6000 × 请求大小
      → 误报率 = 高（因为 PoC 会被发到不相关的目标）
```

### 我们怎么做？

```
目标 → 指纹匹配（匹配到 3 个指纹）
      → 倒排索引检索（针对 3 个指纹名称的关键词）
      → 候选验证（多字段双向匹配）
      → 噪声过滤（去掉 >30% PoC 都会命中的泛词）
      → 最终匹配 8 个 PoC（精准、可控）
```

这个流程背后有三层精妙设计：

### 第一层：倒排索引

在 PoC 加载阶段（不是扫描阶段），Zack-Vulscan 对 6,465 个 PoC 的**所有元数据**建立倒排索引：

```
PoC 文件名    → 关键词列表
PoC 标签      → 关键词列表
产品名称      → 关键词列表
厂商名称      → 关键词列表
CPE 字符串    → 组件拆分 → 关键词列表
PoC ID        → O(1) 精确查找表
```

索引结构是 `map[keyword][]POCIndex`。当你匹配到 `Apache-Druid` 这个指纹时，只需要查 `apache` 和 `druid` 两个 key，就能瞬间拿到所有包含这些词的 PoC 候选列表。

### 第二层：噪声过滤

这是最关键的一步。有些词太"通用"了——比如 `web`、`server`、`platform`。如果不过滤，一个通用指纹会让你匹配到 80% 的 PoC。

**Zack-Vulscan 的解决方案**：30% 噪声阈值。

如果一个关键词出现在超过 30% 的 PoC 中，它被视为**噪声词**，直接跳过。这个阈值是精心调试的结果——太高会漏报，太低会误报。30% 正好卡在"有区分度"和"不太苛刻"的平衡点上。

加上 28 个内置停用词（`the`、`and`、`web`、`http`、`system`……），确保了只有真正有辨识度的技术关键词才会触发 PoC 匹配。

### 第三层：双向词匹配 + 单复数变体

关键词 `druid` 怎么匹配到 PoC？Zack-Vulscan 不是简单地做字符串包含，而是做**词边界感知的匹配**：

```
PoC 文件名: apache-druid-rce.yaml → 拆词: [apache, druid, rce]
关键词: druid → 匹配 "druid" 词 → ✓
```

更精妙的是**单复数变体生成**：

```
关键词 "technologies"
  → 检测到尾缀 "ies"
  → 生成变体 "technology"
  → 用 "technology" 再次检索倒排索引
  → 匹配到 tagged "technology" 的 PoC ✓
```

支持的变体规则：

* `-ies` → `-y`（`technologies` → `technology`）
* `-es` → 去掉，再试 `-s`（`services` → `service`，再试 `servic`）
* `-s` → 去掉（`servers` → `server`）

这就是为什么你匹配到 `Apache-Tomcat-Servers` 时，也能找到 tag 为 `tomcat` 的 PoC。

### 验证环节：六字段任意命中

倒排索引给了你一组候选，但候选可能有几十个。最终验证时，关键词会与 PoC 的**七个字段**进行任意匹配（OR 策略）：

1. **PoC ID**：精确匹配（比如 `CVE-2021-44228`）
2. **文件名**：词边界匹配
3. **标签**：双向词包含（`tag` 含 `kw` 或 `kw` 含 `tag`）
4. **产品名**：双向词包含
5. **厂商名**：双向词包含
6. **CPE**：字符串包含
7. **PoC 名称**：词边界匹配

七个字段中**任意一个**命中就算匹配。这意味着：

* 指纹名是 `Spring` → 产品名为 `Spring Framework` 的 PoC 能匹配到 ✓
* 指纹名是 `华为-USG6000` → 厂商名含 `huawei` 的 PoC 能匹配到 ✓
* 指纹名是 `CVE-2023-3452` → ID 精确为 `CVE-2023-3452` 的 PoC 能匹配到 ✓

### 通用漏洞补充：不放过任何一个盲点

指纹匹配精准，但有一个问题：有些漏洞跟产品无关——XSS、SQL 注入、目录遍历、备份文件泄露，它们可能出现在任何 Web 应用上。

所以 Zack-Vulscan 在指纹匹配之后，会**自动追加 ~85 个通用 PoC**。这些 PoC 满足三个条件：

1. 没有产品/厂商绑定
2. 所有标签都是漏洞类型关键词（`xss`、`sqli`、`ssrf`……共 140+ 词）
3. 位于通用漏洞分类目录下

这意味着即使目标指纹匹配不上任何特定 PoC，基本的 XSS、敏感文件泄露、管理面板暴露等通用检查**一个都不会少**。

---

## Phase 3：并发漏洞执行 + OOB 带外验证

匹配到精确的 PoC 后，执行引擎**完全对标 Nuclei 规范**：支持 `raw:` 原生 HTTP 请求和结构化请求，3 种爆破模式（batteringram / pitchfork / clusterbomb），22 个动态函数（`rand_int`、`md5`、`base64_encode` 等），5 种匹配器（word / regex / status / dsl / binary），均支持反向匹配。变量替换引擎自动注入 `{{BaseURL}}`、`{{Hostname}}`、`{{Port}}` 等内置变量，**5 种提取器**（regex / dsl / json / kval / xpath）可在多步请求间传递数据。

### Flow 多步执行链 + 复合匹配

Zack-Vulscan 支持 **881 个多步 PoC**，通过 `flow: http(1)&&http(2)||http(3)` 布尔表达式串联步骤——比如先登录提取 Token，再携带 Token 访问敏感接口。同一 PoC 的多个 `raw` 请求还会进行**复合匹配**：所有响应合并后统一检查，捕获单请求无法确认的漏洞模式。

### 批量 OOB 带外验证

Log4j、SSRF、JNDI 等无回显漏洞依赖 DNSLog 验证。传统做法是每个 PoC 逐次轮询 cEye API——6000 个 OOB PoC 就是 6000 次 API 调用。**Zack-Vulscan 的做法**：所有 PoC 并发执行时，OOB 子域名统一注册到 `BatchTracker`；全部执行完毕后等待 10 秒，**一次 API 调用**同时查询 DNS 和 HTTP 记录，O(1) 哈希匹配回注册表，批量产出已验证的漏洞结果。API 调用量从 O(n) 降为 O(...