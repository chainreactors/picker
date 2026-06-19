---
title: 【AI渗透工具】——AI驱动的MCP网络安全自动化平台（HexStrike AI ）
url: https://mp.weixin.qq.com/s/gsAV2nSq5QSpPh1yPyYylQ
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:00:46.614777
---

# 【AI渗透工具】——AI驱动的MCP网络安全自动化平台（HexStrike AI ）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T0ibbhsCmribQCSgez6NB0ALuTNAYlL1YW3bWgLakq5qbMy4IXp1dzwqb16iatu6GT8EuAGkFO7FTbhUIGIXp0djY4k5cZCKW6ibhY8KSJ7NJNM/0?wx_fmt=jpeg)

# 【AI渗透工具】——AI驱动的MCP网络安全自动化平台（HexStrike AI ）

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 架构概述

HexStrike AI MCP v6.0 采用多智能体架构，具有自主 AI 智能体、智能决策和漏洞情报功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribTPvtOKS1obic9ZsfJeUXG7Q3tibIR3bqibu7z3uSicsxicKprtY68iaoweKcenO966laQ87EsyV4FC2O1OPPbF2ia0hYccs7oyMl12E0/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribTjpnBvx046icvYtEsnMibibecezb3nywtME0ibQBAkXCMT5oAibzSYzB176nVbn1YPZczSHGfPEh8TP8OZKyToH5eOpLySUyiaOgqlQ/640?wx_fmt=png&from=appmsg)

### 工作原理

1. **AI 代理连接**

   - Claude、GPT 或其他兼容 MCP 的代理通过 FastMCP 协议连接
2. **智能分析**

   ——决策引擎分析目标并选择最佳测试策略
3. **自主执行**

   ——人工智能代理执行全面的安全评估
4. **实时适应**

   ——系统根据结果和发现的漏洞进行调整。
5. **高级报告**

   - 以可视化方式输出漏洞卡片和风险分析

---

## 安装

### 快速设置运行 Hexstrike MCPs 服务器

```
# 1. Clone the repositorygit clone https://github.com/0x4m4/hexstrike-ai.gitcd hexstrike-ai# 2. Create virtual environmentpython3 -m venv hexstrike-envsource hexstrike-env/bin/activate  # Linux/Mac# hexstrike-env\Scripts\activate   # Windows# 3. Install Python dependenciespip3 install -r requirements.txt
```

### 适用于各种人工智能客户端的安装和设置指南：

#### 安装和演示视频

观看完整的安装和设置演示视频：YouTube - HexStrike AI 安装与演示

#### 支持运行和集成的 AI 客户端

您可以使用各种 AI 客户端安装和运行 HexStrike AI MCP，包括：

* **5ire（目前不支持最新版本 v0.14.0）**
* **VS Code Copilot**
* **代码**
* **光标**
* **克劳德桌面**
* **任何MCP兼容剂**

请参考上面的视频，获取这些平台的详细步骤说明和集成示例。

### 安装安全工具

**核心工具（必备）：**

```
# Network & Reconnaissancenmap masscan rustscan amass subfinder nuclei fierce dnsenumautorecon theharvester responder netexec enum4linux-ng# Web Application Securitygobuster feroxbuster dirsearch ffuf dirb httpx katananikto sqlmap wpscan arjun paramspider dalfox wafw00f# Password & Authenticationhydra john hashcat medusa patator crackmapexecevil-winrm hash-identifier ophcrack# Binary Analysis & Reverse Engineeringgdb radare2 binwalk ghidra checksec strings objdumpvolatility3 foremost steghide exiftool
```

**云安全工具：**

```
prowler scout-suite trivykube-hunter kube-bench docker-bench-security
```

**浏览器代理要求：**

```
# Chrome/Chromium for Browser Agentsudo apt install chromium-browser chromium-chromedriver# OR install Google Chromewget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.listsudo apt update && sudo apt install google-chrome-stable
```

### 启动服务器

```
# Start the MCP serverpython3 hexstrike_server.py# Optional: Start with debug modepython3 hexstrike_server.py --debug# Optional: Custom port configurationpython3 hexstrike_server.py --port 8888
```

### 验证安装

```
# Test server healthcurl http://localhost:8888/health# Test AI agent capabilitiescurl -X POST http://localhost:8888/api/intelligence/analyze-target \  -H "Content-Type: application/json" \  -d '{"target": "example.com", "analysis_type": "comprehensive"}'
```

---

## AI客户端集成设置

### Claude桌面集成或光标

编辑`~/.config/Claude/claude_desktop_config.json`：

```
{  "mcpServers": {    "hexstrike-ai": {      "command": "python3",      "args": [        "/path/to/hexstrike-ai/hexstrike_mcp.py",        "--server",        "http://localhost:8888"      ],      "description": "HexStrike AI v6.0 - Advanced Cybersecurity Automation Platform",      "timeout": 300,      "disabled": false    }  }}
```

### VS Code Copilot 集成

在以下位置配置 VS Code 设置`.vscode/settings.json`：

```
{  "servers": {    "hexstrike": {      "type": "stdio",      "command": "python3",      "args": [        "/path/to/hexstrike-ai/hexstrike_mcp.py",        "--server",        "http://localhost:8888"      ]    }  },  "inputs": []}
```

---

## 特征

### 安全工具库

**150多种专业安全工具：**

**🔍 网络侦察与扫描（25+ 工具）**

* **Nmap**

  - 具有自定义 NSE 脚本和服务检测功能的高级端口扫描
* **Rustscan**

  - 具有智能速率限制功能的超高速端口扫描器
* **Masscan**

  - 高速互联网规模端口扫描及横幅抓取
* **自动侦察**

  - 包含 35 个以上参数的全面自动化侦察
* **Amass——**

  高级子域枚举和开源情报收集
* **Subfinder**

  - 快速被动式子域名发现，支持多种来源
* **Fierce**

  - DNS侦察和区域转移测试
* **DNSEnum**

  - DNS 信息收集和子域名暴力破解
* **TheHarvester**

  - 从多个来源收集电子邮件地址和子域名
* **ARP扫描**

  - 使用ARP请求进行网络发现
* **NBTScan**

  - NetBIOS 名称扫描和枚举
* **RPCClient**

  - RPC 枚举和空会话测试
* **Enum4linux**

  - SMB 枚举，支持用户、组和共享发现
* **Enum4linux-ng**

  - 具有增强日志记录功能的高级 SMB 枚举
* **SMBMap**

  - SMB 共享枚举和利用
* **响应器**

  - LLMNR、NBT-NS 和 MDNS 凭证窃取攻击
* **NetExec**

  - 网络服务漏洞利用框架（原名 CrackMapExec）

**🌐 Web应用程序安全测试（40多种工具）**

* **Gobuster**

  - 使用智能字典进行目录、文件和 DNS 枚举
* **Dirsearch**

  - 高级目录和文件发现功能，并具有增强的日志记录功能
* **Feroxbuster**

  - 具有智能过滤功能的递归内容发现
* **FFuf**

  - 具有高级过滤和参数发现功能的快速网络模糊测试工具
* **Dirb**

  - 具有递归扫描功能的综合性网页内容扫描器
* **HTTPx**

  - 快速 HTTP 探测和技术检测
* **Katana**

  - 支持 JavaScript 的新一代爬虫和蜘蛛工具
* **Hakrawler**

  - 快速发现和抓取 Web 端点
* **Gau**

  - 从多个来源（Wayback Machine、Common Crawl 等）获取所有 URL
* **Waybackurls**

  - 通过 Wayback Machine 发现历史 URL
* **Nuclei**

  - 拥有 4000 多个模板的快速漏洞扫描器
* **Nikto**

  - 具有全面检查功能的 Web 服务器漏洞扫描器
* **SQLMap**

  - 高级自动化 SQL 注入测试，支持篡改脚本
* **WPScan**

  - WordPress 安全扫描器，带有漏洞数据库
* **Arjun**

  - 基于智能模糊测试的HTTP参数发现
* **ParamSpider**

  - 从网络存档中挖掘参数
* **X8**

  - 利用先进技术发现隐藏参数
* **Jaeles**

  - 具有自定义签名的高级漏洞扫描
* **Dalfox**

  - 具有 DOM 分析功能的高级 XSS 漏洞扫描
* **Wafw00f**

  - Web应用程序防火墙指纹识别
* **TestSSL**

  - SSL/TLS 配置测试和漏洞评估
* **SSLScan**

  - SSL/TLS 密码套件枚举
* **SSLyze**

  - 快速全面的 SSL/TLS 配置分析器
* **Anew**

  - 向文件追加新行，以提高数据处理效率
* **QSReplace**

  - 用于系统测试的查询字符串参数替换
* **Uro**

  - 用于高效测试的 URL 过滤和去重
* **Whatweb——**

  利用指纹识别进行网络技术识别
* **JWT-Tool**

  - 存在算法混淆的 JSON Web Token 测试
* **GraphQL-Voyager**

  - GraphQL模式探索和内省测试
* **Burp Suite 扩展程序**

  - 用于高级 Web 测试的自定义扩展程序
* **ZAP Proxy**

  - OWASP ZAP 集成，用于自动化安全扫描
* **Wfuzz**

  - 具有高级有效载荷生成的 Web 应用程序模糊测试工具
* **Commix**

  - 一款带有自动检测功能的命令注入攻击工具
* **NoSQLMap**

  - 用于 MongoDB、CouchDB 等的 NoSQL 注入测试。
* **Tplmap**

  - 服务器端模板注入利用工具

**🌐 高级浏览器代理：**

* **无头 Chrome 自动化**

  - 使用 Selenium 实现完整的 Chrome 浏览器自动化
* **屏幕截图捕获**

  - 用于视觉检查的自动屏幕截图生成
* **DOM 分析**

  - 深度 DOM 树分析和 JavaScript 执行监控
* **网络流量监控**

  - 实时网络请求/响应日志记录
* **安全标头分析**

  - 全面的安全标头验证
* **表单检测与分析**

  - 自动表单发现和输入字段分析
* **JavaScript 执行**

  - 提供完整 JavaScript 支持的动态内容分析
* **代理集成**

  - 与 Burp Suite 和其他代理的无缝集成
* **多页面爬取**

  - 智能 Web 应用程序爬取和映射
* **性能指标**

  ——页面加载时间、资源使用情况和优化洞察

**🔐 身份验证和密码安全（12+ 工具）**

* **Hydra**

  - 支持 50 多种协议的网络登录破解工具
* **John the Ripper**

  - 使用自定义规则进行高级密码哈希破解
* **Hashcat——**

  全球速度最快的密码恢复工具，具备GPU加速功能
* **Medusa**

  - 快速、并行、模块化登录暴力破解器
* **Patator**

  - 具有高级模块的多用途暴力破解工具
* **NetExec——**

  网络渗透测试领域的瑞士军刀
* **SMBMap**

  - SMB 共享枚举和利用工具
* **Evil-WinRM**

  - 集成 PowerShell 的 Windows 远程管理 shell
* **哈希标识符**

  - 哈希类型识别工具
* **HashID**

  - 具有置信度评分的高级哈希算法标识符
* **CrackStation**

  - 在线哈希查找集成
* **Ophcrack**

  - 使用彩虹表的 Windows 密码破解工具

**🔬 二进制分析与逆向工程（25+ 工具）**

* **GDB**

  - 支持 Python 脚本编写和漏洞利用开发的 GNU 调试器
* **GDB-PEDA**

  - GDB 的 Python 漏洞利用开发协助
* **GDB-GEF**

  - GDB 增强功能，用于漏洞利用开发
* **Radare2**

  - 具有全面分析功能的先进逆向工程框架
* **Ghidra——**

  美国国家安全局的软件逆向工程套件，具备无头分析功能
* **IDA Free**

  - 具有高级分析功能的交互式反汇编器
* **Binary Ninja**

  - 商业逆向工程平台
* **Binwalk**

  - 固件分析和提取工具，支持递归提取
* **ROPgadget**

  - 具有高级搜索功能的 ROP/JOP 设备查找器
* **Ropper**

  - ROP 小工具查找器和漏洞利用开发工具
* **One-Gadget**

  - 在 libc 中查找一次性远程代码执行 (RCE) 小工具
* **Checksec**

  - 具有全面分析功能的二进制安全属性检查器
* **字符串**

  提取 - 从二进制文件中提取可打印字符串并进行过滤
* **Objdump**

  - 使用 Intel 语法显示对象文件信息
* **Readelf**

  - 带有详细文件头信息的 ELF 文件分析器
* **XXD**

  - 具有高级格式化功能的十六进制转储工具
* **Hexdump**

  - 具有可自定义输出的十六进制查看器和编辑器
* **Pwntools**

  - CTF 框架和漏洞利用开发库
* **Angr**

  - 具有符号执行功能的二进制分析平台
* **Libc数据库**

  - Libc识别和偏移量查找工具
* **Pwninit**

  - 自动化二进制漏洞利用设置
* **Volatility**

  - 高级内存取证框架
* **MSFVenom**

  - 具有高级编码功能的 Metasploit 有效载荷生成器
* **UPX**

  - 用于二进制分析的可执行打包/解包程序

**☁️ 云和容器安全（20+ 工具）**

* **Prowler**

  - AWS/Azure/GCP 安全评估及合规性检查
* **Scout Suite**

  - 适用于 AWS、Azure、GCP 和阿里云的多云安全审计
* **CloudMapper**

  - AWS 网络可视化和安全分析
* **Pacu**

  - 具有全面模块的 AWS 漏洞利用框架
* **T...