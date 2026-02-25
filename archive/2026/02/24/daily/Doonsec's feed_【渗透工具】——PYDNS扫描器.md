---
title: 【渗透工具】——PYDNS扫描器
url: https://mp.weixin.qq.com/s/pNLL8nZ8eiwKQd8KXP6EnQ
source: Doonsec's feed
date: 2026-02-24
fetch_date: 2026-02-25T04:13:13.837932
---

# 【渗透工具】——PYDNS扫描器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T0ibbhsCmribQTLSxlBHe1r5cWC5g99eYbQTOjHlLoZxSialUlr6mBCibnXHTiatcd1pJTLfXurjbhAukvnu3rhllt6wL73b4iceqM5S0MiayRtnfw/0?wx_fmt=jpeg)

# 【渗透工具】——PYDNS扫描器

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器中沉浸阅读

**一款现代化的高性能 DNS 扫描器，拥有美观的终端用户界面 (TUI)，采用 Textual 语言编写。**
该工具可以扫描数百万个 IP 地址，查找可用的 DNS 服务器，并可选配 Slipstream 代理测试和自动多平台客户端下载功能。

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribT6MbUZawZwZwhIvh6mj6r79Gw3uaT2MKZicJs6zyRNx4qf4uNtOiaI5nYrXY8Gl2DdtvNvEmgP8uTYx4SIk26KYoAEqMx95r5Tk/640?wx_fmt=png&from=appmsg)

## 🎉 v1.2.0 版本新增功能

### 🎨 视觉和用户体验改进

* **小屏幕支持**- 修复了小屏幕设备上可滚动表单的高度问题
* **增强状态跟踪**- 实时显示通过/失败/找到的统计信息，并以颜色编码显示（白色=找到，绿色=通过，红色=失败）
* **失败的服务器位于末尾**- 失败的代理测试现在显示在结果列表的底部

### 🔐 代理身份验证

* **代理身份验证支持**- 新增代理身份验证切换复选框
* **用户名/密码字段**- 默认隐藏，启用代理身份验证后显示。
* **HTTP 和 SOCKS5 身份验证**- 身份验证同时应用于 HTTP 和 SOCKS5 代理测试

### ⌨️ 键盘快捷键

* **S** - 开始扫描（从配置屏幕）
* **问**：退出应用程序
* **C** - 将结果保存到文件
* **P** - 暂停扫描（扫描时）
* **R** - 恢复扫描（暂停后）
* **X** - 重新排列剩余 IP 地址（暂停时）

### 🔔 音频效果提升

* **单枚硬币音效**- 代理测试成功时，发出清晰的单枚硬币闪光/通知

---

## 📦 v1.1.0 版本更新内容

### 🎨 视觉和用户体验改进

* **GitHub 深色主题**- 漂亮的深色模式，采用 GitHub 风格的颜色（#0d1117 背景色，#58a6ff 强调色）
* **全屏开始菜单**- 配置表单现在使用终端的全部高度/宽度
* **改进下拉菜单**- 修复了下拉菜单的样式，使其高度和文本可见性均符合预期。
* **精简复选框**- 所有选项（随机子域名、代理测试、铃声）显示在同一行

### ⚡ 性能提升

* **5 项并发代理测试**- 从 3 项并行 Slipstream 测试增加到 5 项（端口 10800-10804）
* **更好的退出处理**- 正确恢复退出时的终端状态，包括光标恢复和输入恢复

### 🌍 CIDR 管理

* **捆绑式伊朗IP地址**- 预加载约1000万个伊朗IPv4地址（iran-ipv4.cidrs）
* **CIDR下拉菜单**- 轻松选择伊朗默认文件和自定义文件
* **域名缓存**- 跨会话记住上次使用的域名

## ✨ 特点

* 🎨**美观的 TUI 界面**- GitHub 深色主题终端界面
* ⚡**高性能**- 异步扫描，并发性可配置
* ⏸️**暂停/恢复/随机播放**- 完全扫描控制
* 📊**实时统计**- 实时进度跟踪和扫描指标
* 🔍**智能 DNS 检测**- 即使出现错误响应（NXDOMAIN、NODATA），也能检测出可用的 DNS 服务器
* 🎲**随机子域名支持**- 使用随机子域名避免缓存响应
* 🌐支持**多种 DNS 类型**- 支持 A、AAAA、MX、TXT、NS 记录
* 🔌 **Slipstream 集成**- 可选的代理测试，支持 5 个并行执行
* 🌍**多平台自动下载**- 自动下载适用于您平台的正确 Slipstream 客户端
* 📥**断点续传**- 网络中断时智能断点续传，并带有重试逻辑
* 💾**自动保存结果**- 自动将扫描结果导出为 JSON 格式
* 📁 **CIDR 管理**- 内置伊朗 IP 地址 + 自定义文件选择器
* ⚙️**可配置**- 可调节并发数、超时时间和过滤器
* 🚀**内存高效**- 无需将所有 IP 地址加载到内存即可流式生成 IP 地址
* 📝**可选日志记录**- 默认禁用，可轻松启用以进行故障排除
* 🔔**音频提示**- 代理测试成功时可选择发出闪光音效

## 📋 要求

### Python 版本

* Python 3.11 或更高版本

### 依赖关系

```
# Core dependenciestextual>=0.47.0       # TUI frameworkaiodns>=3.1.0         # Async DNS resolverhttpx[socks]>=0.25.0  # HTTP client with SOCKS5 support for proxy testingorjson>=3.9.0         # Fast JSON serializationloguru>=0.7.0         # Advanced loggingpyperclip>=1.8.0      # Clipboard support
```

### 选修的

* **Slipstream 客户端**- 用于代理测试功能（5 个并发测试）

+ Linux (x86\_64):`slipstream-client-linux-amd64`
+ Windows (x86\_64)：`slipstream-client-windows-amd64.exe`
+ macOS（ARM64）：`slipstream-client-darwin-arm64`
+ macOS（Intel）：`slipstream-client-darwin-amd64`

+ **自动下载**：应用程序会自动检测您的平台并下载正确的客户端。
+ **智能检测**：检测现有安装（包括旧式文件名）
+ **支持断点续传**：部分下载将被保存，重试时可以继续下载。
+ 支持的平台：
+ 可从以下位置下载手动版本：slipstream-rust-deploy releases

### 📦 捆绑式 Slipstream 客户端

`slipstream-client/`文件夹中包含了适用于所有平台的预编译 Slipstream 客户端二进制文件：

| 平台 | 小路 | 描述 |
| --- | --- | --- |
| **Linux** | `slipstream-client/linux/slipstream-client-linux-amd64` | Linux x86\_64 二进制文件 |
| **视窗** | `slipstream-client/windows/slipstream-client-windows-amd64.exe` | Windows x86\_64 可执行文件 |
| **macOS ARM** | `slipstream-client/mac/slipstream-client-darwin-arm64` | macOS 苹果芯片（M1/M2/M3） |
| **macOS 英特尔** | `slipstream-client/mac/slipstream-client-darwin-amd64` | macOS Intel x86\_64 |

> **⚠️Windows 注意：** Windows 客户端需要 OpenSSL DLL 文件（`libcrypto-3-x64.dll`和`libssl-3-x64.dll`），这些文件包含在`slipstream-client/windows/`文件夹中。使用自动下载时，这些 DLL 文件会与 Windows 可执行文件一起自动下载。

#### 📥 一体化存档

为方便起见，我们提供了包含所有平台二进制文件的压缩包：

* **`slipstream-client/slipstream-client-all-platforms.tar.gz`**- 最佳压缩（推荐）
* **`slipstream-client/slipstream-client-all-platforms.zip`**- Windows 兼容格式

这些压缩包包含 Linux、Windows 和 macOS 客户端，只需一次下载即可获得。

## 🚀 安装

### 方法一：从 PyPI 安装（推荐）

安装 PYDNS Scanner 的最简单方法：

#### 使用 pip

```
pip install pydns-scanner
```

#### 使用紫外线（速度更快）

```
uv pip install pydns-scanner
```

#### 使用镜像（适用于 PyPI 访问权限有限的用户）

```
# Runflare Mirrorpip install pydns-scanner -i https://mirror-pypi.runflare.com/simple/ --trusted-host mirror-pypi.runflare.com# Or Alibaba Cloud Mirrorpip install pydns-scanner -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com# Or TUNA Mirrorpip install pydns-scanner -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 安装后运行

```
pydns-scanner
```

---

### 方法二：从源代码运行（手动）

如果您想直接从代码库运行代码：

#### 第一步：克隆代码库

```
git clone https://github.com/xullexer/PYDNS-Scanner.gitcd PYDNS-Scanner
```

#### 步骤二：安装依赖项

**使用紫外线（推荐 - 快速！）**

```
uv pip install -r requirements.txt
```

**使用 pip**

```
pip install -r requirements.txt
```

**使用镜像（适用于 PyPI 访问权限有限的用户）**

```
# Runflare Mirrorpip install -r requirements.txt -i https://mirror-pypi.runflare.com/simple/ --trusted-host mirror-pypi.runflare.com# Or Alibaba Cloud Mirrorpip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com# Or TUNA Mirrorpip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 步骤 3：运行应用程序

```
python -m python
```

---

## 🎮 用法

### 基本用法

**来自 PyPI：**

```
pydns-scanner
```

**来源：**

```
python -m python
```

这将启动交互式用户界面 (TUI)，您可以在其中进行配置：

* **CIDR 文件**：包含 IP 地址范围（CIDR 表示法）的文件路径
* **域名**：要查询的域名（例如，google.com）
* **DNS 类型**：记录类型（A、AAAA、MX、TXT、NS）
* **并发数**：并行工作进程数（默认值：100）
* **随机子域名**：添加随机前缀以避免缓存响应
* **Slipstream 测试**：启用已找到的 DNS 服务器的代理测试

### CIDR 文件格式

创建一个文本文件，每行包含一个 CIDR 范围：

```
# Comments start with #
1.1.1.0/24
8.8.8.0/24
178.22.122.0/24
185.51.200.0/22
```

### 示例工作流程

1. **启动应用程序**：

   ```
   python dnsscanner_tui.py
   ```
2. **配置扫描参数**：

* 点击“📂浏览”选择您的CIDR文件
* 输入域名（例如，`google.com`）
* 设置并发数（建议：100-500）
* 根据需要启用选项

3. **开始扫描**：

* 点击“🚀 开始扫描”
* 实时查看进度和结果
* 随时使用“⏸ 暂停”暂停扫描
* 使用“▶ 继续”从上次暂停的地方继续。

4. **查看结果**：

* 按响应时间排序（最快排在最前面）
* 绿色 = 快速（<100毫秒）
* 黄色 = 中等 (100-300毫秒)
* 红色 = 慢（>300毫秒）

5. **保存结果**：

* 结果会自动保存。`results/TIMESTAMP.txt`
* 按`s`或点击“💾 保存结果”手动保存。

## ⌨️ 键盘快捷键

| 钥匙 | 什么时候 | 行动 |
| --- | --- | --- |
| `s` | 配置屏幕 | 开始扫描 |
| `q` | 随时 | 退出应用程序 |
| `c` | 扫描时 | 保存结果 |
| `p` | 扫描时 | 暂停扫描 |
| `r` | 暂停时 | 恢复扫描 |
| `x` | 暂停时 | 重新排列剩余的IP地址 |

## 🎮 控制按钮

在进行扫描过程中：

* **⏸ 暂停**- 暂停扫描而不丢失进度
* **▶ 继续扫描**- 从上次暂停的地方继续扫描
* **💾 保存结果**- 手动保存当前结果
* **🛑 退出**- 退出应用程序

## 🎛️ 配置

### 日志记录

**默认情况下禁用**日志记录，以保持界面简洁并避免不必要的磁盘写入。

**要启用日志记录**，请编辑`dnsscanner_tui.py`：

```
# Configure logging (disabled by default)logger.remove()  # Remove default handler to disable logging# Uncomment the line below to enable file logginglogger.add("logs/dnsscanner_{time}.log",    rotation="50 MB",    compression="zip",    level="DEBUG",)
```

启用后：

* 日志保存到`logs/dnsscanner_TIMESTAMP.log`
* 自动旋转，文件大小为 50 MB
* 自动压缩（zip）
* 包含调试级别详细信息

### 并发设置

请根据您的系统和网络情况进行调整：

* **低（50-100）**：保守，适用于速度较慢的系统。
* **中等（100-300）**：均衡性能
* **高（300-500）**：扫描速度快，需要性能良好的硬件。
* **非常高（500+）**：最高速度，可能达到资源限制

### 滑流测试

该扫描器支持并行 Slipstream 代理测试，并可自动下载：

```
# In __init__ methodself.slipstream_max_concurrent=3# Max parallel proxy testsself.slipstream_base_port=10800# Base port (uses 10800, 10801, 10802)
```

**自动下载功能：**

* 平台检测（Windows/Linux/macOS + 架构）
* 进度条显示下载速度
* 中断后恢复（保留`.partial`文件）
* 使用指数退避策略重试（最多尝试 5 次）
* 旧式文件名检测（`slipstream-client.exe`）

### DNS超时

DNS 查询超时时间为 2 秒：

```
# In _test_dns methodresolver=aiodns.DNSResolver(nameservers=[ip], timeout=2.0, tries=1)
```

## 📊 输出格式

结果以JSON格式保存：

```
{"scan_info":{"domain":"google.com","dns_type":"A","slipstream_test":true,"total_found":50,"total_passed_proxy":42,"total_saved":42,"elapsed_seconds":300.5,"timestamp":"2026-01-26_10-30-45"},"servers":["8.8.8.8","1.1.1.1","..."]}
```

## 🔍工作原理

### DNS检测逻辑

如果满足以下条件，扫描器会将服务器视为“正常工作的 DNS 服务器”：

1. **响应成功**：在 2 秒内返回有效的 DNS 应答
2. **DNS 错误响应**：在 2 秒内返回 NXDOMAIN、NODATA 或 NXRRSET。

* 这些错误意味着 DNS 服务器运行正常，只是记录不存在。

这种方法比只接受成功响应的工具能捕获更多可用的 DNS 服务器。

### 性能优化

* **流媒体 IP 生成**：IP 地址根据 CIDR 范围动态生成。
* **分块处理**：以 500 个 IP 地址为一批进行处理
* **异步 I/O**：使用 aiodns 进行非阻塞 DNS 查询
* **信号量控制**：限制并发操作以防止资源耗尽
* **内存映射**：尽可能使用 mmap 快速读取 CIDR 文件

### 随机子域名功能

启用此功能后，查询将使用随机前缀：

```
orig...