---
title: Rust 开发的 Web 安全扫描器 Lonkero：智能模式、OOBZero 和现代 Web 适配详解
url: https://mp.weixin.qq.com/s/kxv6dRkLh7c_55iiDR2NUQ
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:26:11.342366
---

# Rust 开发的 Web 安全扫描器 Lonkero：智能模式、OOBZero 和现代 Web 适配详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IkpoxULsr9em9DXPib1s8glo0kBpSK7IAJDRewT8zr8AEsnAgNwVKiaGkZiaMYpAeBOIVuQmAIfyiagaKp828wiaC8Q/0?wx_fmt=jpeg)

# Rust 开发的 Web 安全扫描器 Lonkero：智能模式、OOBZero 和现代 Web 适配详解

原创

Norsea
Norsea

泷羽Sec-Norsea

![]()

在小说阅读器中沉浸阅读

做渗透测试，最头疼的不是找漏洞，而是扫描器误报一堆，还要手动验证半天，真正的漏洞反而被淹没在噪音里。

最近看到 `Lonkero` 这个开源安全扫描器，采用贝叶斯假设引擎和智能过滤，误报率只有 `5%`，比行业平均水平低了好几倍。

基于 `Rust` 构建，内置`125+`专业扫描器，覆盖注入、认证、`API` 安全、现代框架等各个方面，还能自动识别技术栈并调整测试策略。(项目地址见文末)

![](https://mmbiz.qpic.cn/mmbiz_jpg/IkpoxULsr9em9DXPib1s8glo0kBpSK7IADYvPoSvo3e8zibnv46E2FFcBsxiayfvMO6rgjNkLqfks5Fxz366wRKuw/640?wx_fmt=jpeg)

## Lonkero 是什么？

`Lonkero` 是一款生产级 Web 安全扫描器，专为专业安全测试设计：

* **v3.0 智能模式** - 上下文感知扫描，包括技术检测、端点去重和每个参数的风险评分
* **ML 自动学习** - 从每次扫描中学习，以降低误报率（支持联邦学习）
* **扫描器智能系统** - 实时扫描器通信、贝叶斯假设测试、多步攻击规划和语义响应理解
* **接近零误报率**（5% vs 行业 20-30%）
* **智能测试** - 跳过框架内部，专注于真实漏洞
* **现代栈覆盖** - Next.js、React、GraphQL、gRPC、WebSocket、HTTP/3
* **扫描速度提升 80%** - 智能参数过滤消除噪声
* **高级盲漏洞检测技术**
* **当技术检测失败时，我们运行更多测试，而不是更少** - 后备层包含 35+ 扫描器

与其他通用扫描器不同，后者会发送数千无用负载，`Lonkero` 使用上下文感知过滤，仅测试重要内容。

---

## v3.3 新功能

### XSS 扫描器改进

对 XSS 检测准确性和覆盖范围进行了重大改进：

**Chromium XSS 扫描器（高级版）**

* **增加负载覆盖** - 智能模式现在使用所有可用负载，而不是每个参数仅 5 个
* **放宽参数过滤** - 现在测试像 user\_id、product\_id、name 这样的参数（ID 可能在 XSS 上下文中反射）
* **仅跳过不可注入上下文** - CSRF 令牌、纯分页字段和布尔标志

**新增：反射 XSS 扫描器（免费版）**

* **无需 Chrome** - 基于 HTTP 响应的 XSS 检测
* **测试 6 种负载类型** - 脚本注入、img onerror、svg onload、body onload、input autofocus、属性突破
* **自动后备** - 当 Chromium 扫描器不可用时运行

### 参数过滤改进

* **XSS 过滤扩展** - 现在测试以 id、count、weight 等结尾的参数（这些可能在 HTML 中反射）
* **更好的误报预防** - 仍然跳过 CSRF 令牌、分页和布尔标志，其中 XSS 不可能

---

## v3.2 新功能

### Zero OOB：无需外部回调的盲 SQL 注入

传统盲 `SQLi` 需要带外回调。`Collaborator、Interactsh`、自定义 `DNSLog`。需要部署和维护基础设施。

还有另一种方式。

**测试** SLEEP(0)、SLEEP(1)、SLEEP(2)、SLEEP(5)。计算 Pearson 相关性。

如果 r > 0.95，那不是噪声 - 那是数据库在响应您的命令。

**更好的是**：提取数据。二分搜索 ASCII 值，每个字符 7 个请求。当您逐字节从数据库中提取 "admin" 时，那不是推理。那是证明。

使用`贝叶斯加权`结合信号。定时、内容长度、引号振荡、布尔差分。每个通道单独都很弱。结合在一起，它们趋向于确定性。

**权衡**：比单个 OOB 回调更多请求。但零外部依赖。

**新检测技术：**

* **校准 SLEEP 相关性** - 多值定时分析，使用 Pearson 相关性（r > 0.95 = 确认）
* **布尔数据提取** - 逐字符提取实际数据库内容（证明，而不是推理）
* **真正单包攻击** - 原始 TCP/TLS 套接字控制，用于微秒精度定时
* **引号振荡检测** - 对 '、''、'''、'''' 响应的模式匹配
* **HTTPS 支持** - TLS 流处理，用于单包定时攻击

---

## v3.1 新功能

### 检测改进

* **修复静态/SPA 跳过逻辑** - Cloudflare Workers、Vercel Functions 和 Netlify Functions 现在正确测试（它们是动态的，不是静态的）
* **修复 Node.js 命令注入** - 移除 Node.js 无法执行 shell 命令的错误假设（child\_process 存在）
* **SSRF POST 主体测试** - 现在测试 POST JSON 和表单编码主体，而不仅仅是查询参数
* **增强端点发现** - 244+ 新端点模式，用于 API、管理、调试和工具路径

### 新扫描器

* **二阶注入** - 在一个端点存储负载，在另一个端点检测执行（XSS、SQLi、CMDi）
* **认证流程测试器** - 会话固定、密码重置 IDOR、MFA 绕过、可预测会话令牌

### 增强扫描器

* **JWT** - 扩展弱密钥词表（21 个密钥），修复 alg:none 令牌格式
* **竞态条件** - 注册、库存、投票和单次使用令牌 TOCTOU 测试
* **WebSocket** - 主动端点发现，使用 9 个来源绕过的 CSWSH 测试
* **信息泄露** - 基于模式的內容检测（即使 404 相同也不会跳过）

---

## 核心能力

### v3.0 智能扫描架构

```
┌─────────────────────────────────────────────────────────────────┐
│  第一层：通用扫描器（始终运行）                                 │
│  CORS、Headers、SSL、OpenRedirect、HttpSmuggling、HostHeader    │
├─────────────────────────────────────────────────────────────────┤
│  第二层：核心扫描器（始终运行）                                 │
│  XSS、SQLi、SSRF、CommandInjection、PathTraversal、IDOR、JWT    │
├─────────────────────────────────────────────────────────────────┤
│  第三层：技术特定（检测到时）                                   │
│  NextJs、React、Django、Laravel、Express、WordPress...          │
├─────────────────────────────────────────────────────────────────┤
│  第四层：后备（当技术未知时）                                   │
│  35+ 额外扫描器                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 扫描模式（v2.x 遗留）

* **快速**：每个参数 5 个负载，适合快速评估
* **正常**：每个参数 50 个负载，默认平衡
* **彻底**：每个参数 500 个负载，深度测试
* **疯狂**：所有负载，穷举式

### 漏洞类型覆盖

**注入**：

* SQLi（时间/布尔/联合/错误/堆叠）
* XSS（反射/存储/DOM/突变）
* XXE（内部/外部/盲）
* NoSQL 注入（MongoDB/Firebase/Cassandra）
* 命令注入（shell/无shell）
* LDAP/XPath 注入
* SSRF（云元数据/AWS/Azure/GCP）
* 模板注入（SSTI - Twig/Jinja/ERB）
* 原型污染（Node.js）
* Host Header 注入
* Log4j/JNDI 注入
* DOM Clobbering
* 二阶注入

**认证/授权**：

* JWT（弱密钥/alg:none/alg:HS256-RS256/密钥重用）
* OAuth/OIDC/SAML 漏洞
* MFA 绕过
* 会话固定/劫持
* IDOR/BOLA/BFLA
* 授权绕过（客户端路由/角色）
* 密码重置漏洞
* 可预测会话令牌

**配置/误配置**：

* 安全标头缺失（CSP/HSTS/XFO/Referrer）
* CORS 绕过（通配符/null/子域）
* SSL/TLS 误配置（弱密码/过期/链）
* 云容器泄露（Docker/K8s/Compose）
* WAF 绕过（Cloudflare/WAF/Akamai）
* CSRF 缺失
* DNS 重新绑定
* Web 缓存欺骗
* PostMessage 漏洞
* 框架特定漏洞（Next.js 中间件绕过/IDOR）

**业务逻辑**：

* 竞态条件（TOCTOU/注册/支付）
* 支付绕过（负数/小数）
* 工作流操纵（状态/步骤跳过）
* 海量赋值
* 时序攻击
* 滥用功能（无限重试/速率限制绕过）

**信息泄露**：

* 敏感数据暴露（PII/API密钥/密码）
* 调试泄露（栈跟踪/环境变量）
* 源代码泄露（.git/.svn/.DS\_Store）
* JS 秘密提取（变量/令牌）
* 源地图泄露
* Favicon 哈希
* HTML 注释注入
* 目录列表

**其他**：

* CVE 检测（Log4Shell/Spring4Shell 等）
* 版本映射/指纹识别
* ReDoS 漏洞
* Google Dorking 集成
* 攻击面枚举
* 子域接管检测

### GraphQL 安全

* 内省禁用绕过
* 批量 DoS 攻击
* 别名滥用
* 深度/宽度限制绕过
* 成本分析漏洞
* 递归/循环查询
* 认证绕过

### gRPC/REST 特定

* 反射文件描述符泄露
* 枚举方法
* 无效 protobuf 注入
* 认证绕过

### WebSocket

* 主动端点发现
* CSWSH（跨站点 WebSocket 劫持）
* 9 个来源绕过
* 注入/泄露测试

### HTTP/3 特定

* 请求走私
* 优先级滥用
* 连接合并漏洞

### 表单重放

* 多步向导表单记录
* 动态令牌处理
* 完整交互重放

### SPA/现代框架

* 路由提取（Next.js App Router/动态段）
* 软 404 处理（200 响应但页面不存在）
* 状态追踪（cookies/localStorage/CSRF）
* headless 浏览器 XSS 执行

### 性能比较

| 指标 | 传统扫描器 | Lonkero |
| --- | --- | --- |
| 负载测试 | 5,000 | 800 |
| 首次发现时间 | 45s | 8s |
| 误报率 | 8% | 2% |
| 发现攻击链 | 0 | 3 |
| 上下文感知 | 无 | 完整 |

---

## 合规映射

### OWASP Top 10 2025

| OWASP 类别 | Lonkero 扫描器 |
| --- | --- |
| A01: 破坏访问控制 | IDOR、权限提升、客户端路由绕过 |
| A02: 加密失败 | JWT 弱密钥、SSL/TLS 误配置 |
| A03: 注入 | SQLi、XSS、XXE、NoSQL、CMD、LDAP、XPath、SSTI |
| A04: 不安全设计 | 业务逻辑、竞态条件、工作流绕过 |
| A05: 安全误配置 | Headers、CORS、调试模式、CDN 绕过 |
| A06: 易受攻击组件 | 框架扫描器（Next.js、Laravel、Django） |
| A07: 认证失败 | JWT、OAuth、SAML、MFA、会话固定 |
| A08: 数据完整性失败 | 文件上传、缓存中毒、海量赋值 |
| A09: 安全日志失败 | 信息泄露扫描器 |
| A10: SSRF | SSRF 扫描器，包含云元数据检查 |

### PCI DSS 4.0

* 要求 6.5.1: 注入缺陷（SQLi、XSS、XXE）
* 要求 6.5.3: 不安全加密存储（JWT 扫描器）
* 要求 6.5.4: 不安全通信（SSL/TLS 扫描器）
* 要求 6.5.8: 不当访问控制（IDOR、权限提升）
* 要求 6.5.10: 破坏认证（JWT、OAuth、SAML）

### GDPR / NIS2 / DORA

* 数据暴露检测（敏感数据扫描器）
* 加密验证（SSL/TLS、JWT）
* 访问控制验证（IDOR、授权绕过）
* 日志与监控（信息泄露）

---

## CI/CD 集成

### v3.0 - 无需模式选择

Lonkero v3.0 默认使用 **智能模式** - 无需指定 --mode。扫描器自动：

* 检测技术栈
* 端点和参数去重
* 按风险评分参数
* 为每个目标选择适当扫描器
* 当技术未知时运行后备扫描器

遗留模式（--mode fast/normal/thorough/insane）仍可用作向后兼容。

### GitHub Actions

YAML

```
name: Lonkero Security Scan

on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install Rust
        uses: dtolnay/rust-action@stable

      - name: Install Dependencies
        run: sudo apt update && sudo apt install build-essential pkg-config libssl-dev -y

      - name: Clone and Build Lonkero
        run: |
          git clone https://github.com/bountyyfi/lonkero.git /tmp/lonkero
          cd /tmp/lonkero
          cargo build --release
          sudo cp target/release/lonkero /usr/local/bin/

      - name: Run Lonkero Scan
        env:
          LONKERO_LICENSE_KEY: ${{ secrets.LONKERO_LICENSE }}
        run: |
          # v3.0: Intelligent mode is default - no --mode needed
          lonkero scan https://staging.example.com \
            --format sarif \
            -o results.sarif

      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: results.sarif
```

### GitLab CI

YAML

```
lonkero-scan:
  stage: security
  image: rust:1.85.1
  variables:
    LONKERO_LICENSE_KEY: $LONKERO_LICENSE
  script:
    - apt update && apt install -y build-essential pkg-config libssl-dev
    - git clone https://github.com/bountyyfi/lonkero.git /tmp/lonkero
    - cd /tmp/lonkero && cargo build --release
    # v3.0: Intelligent mode is default
    - /tmp/lonkero/target/release/lonkero scan $CI_ENVIRONMENT_URL --format json -o gl-sast-report.json
  artifacts:
    reports:
      sast: gl-sast-report.json
```

### 遗留模式（可选）

如果需要特定用例的老行为：

```
# Use legacy modes when needed
lonkero scan https://example.com --mode fast      # 50 payloads globall...