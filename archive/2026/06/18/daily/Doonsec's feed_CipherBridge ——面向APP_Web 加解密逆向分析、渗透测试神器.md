---
title: CipherBridge ——面向APP/Web 加解密逆向分析、渗透测试神器
url: https://mp.weixin.qq.com/s/SZ22dKTCwK25OZFZ64vDxw
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:00:21.771910
---

# CipherBridge ——面向APP/Web 加解密逆向分析、渗透测试神器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qqiaD4wiajgFwT1Ha1CU6defuHYREYeC7VWTgwBbhtBlr85QDiadzIPtDAuBlXJejwvdq0Hr77VPYNCZ4gzSyGjibsLO41XPtSOgvaLvFbZBEFQ/0?wx_fmt=jpeg)

# CipherBridge ——面向APP/Web 加解密逆向分析、渗透测试神器

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 项目地址：

https://github.com/CuriousLearnerDev/CipherBridge

## 项目作者

##

## 项目概述

**CipherBridge（密桥）** 是一款面向 APP/Web 加解密逆向分析与渗透测试人员的**可视化解密框架**。它基于 mitmproxy 构建，能够在流量代理层实现自动化加解密拦截、Hook 注入、AI 辅助分析以及 Burp Suite 联动，极大简化了移动端和 Web 端加密通信的逆向分析流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFygW8y8R5IhMwYs69ejK5nloCnEDWGQHtvxpqkwPETEULhqicVNoxZNeMjc74Fs2yO2I9KJETbZQvyQ20akkwyDOrVLzsjYgZHw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFwJBBrmFTSOTpgibNFyib2zYSypcqavjuZasibl0Zb5XH47pyEBTById5eOwMzRvhiaX0XlG8icCFYIc8h2ZavnEFBic6fatWH3zqpicg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFxiaFwGTj7jeuUKOczK041iaRtpibibSNeco4PN8oicgqXJKsl4HEdzXNIIUeVqIl15EnDtVWLpZ0q1dLnrrkbhhz5cEm1p3fwFle7k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFxqLl5rOM9yLfvJcicmOBDpSskVHRic8qial7qLmn07QciazD1sFNaKFBlbBmMD4T1Y83oEGlWYrqG3v0fFxtGoysfZ8c7flNK4Qgo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFzKFjVO7JwP6ic0ia2FnTicswp8D598kgP7JgTiaa2bjvgTr2vYd0ib1BmUOzdfCgwDFNYyo3L8ibibTLJvH07qaNrJQ59vb1OczMPEMs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFxh8tfibLXrTLHdART5vRKvMZgnOI7VSGPfT8S5PEaACpMsgK1rhvJuMsr6fznV6u8HBYYpY5kaeqVYAwkNqHPkHLecJjIicfXeY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFygkHt3IzLdvy6T5XbM11FGnEuia1aNXHJ9MvVk7OBZxDueYwHng3Q09pREJOicGazccHs9hllmHp6ZZIibjbJYe04afIPpGC7Mgs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFzLndqnBVVZsBX30kb7gpN8znS5VPUB9iaRO9Wflbw01QODh87vQlHD6YLGGkAX9HqzQWlsaAILtOWj23RcFpc6OFVdRXUeJ1UU/640?wx_fmt=png&from=appmsg)

### 核心定位

| 维度 | 说明 |
| --- | --- |
| **目标用户** | 移动安全工程师、渗透测试人员、逆向分析工程师 |
| **核心能力** | 流量代理加解密、Hook 脚本注入、AI 自动化分析、Burp Suite 联动 |
| **技术栈** | Python 3.10+ / PyQt6 / mitmproxy / Playwright |
| **支持平台** | Windows / macOS / Linux |

### 核心特性

* **可视化插件构建器**：通过 GUI 界面拖拽配置加解密规则，无需手写代码即可生成 mitmdump 插件
* **AI 自动化分析**：集成 AI 大模型，自动分析加密算法、生成 Hook 脚本、逆向 JS 加密逻辑
* **多算法支持**：AES / DES / 3DES / SM4 / RSA / MD5 / SHA256 / HMAC / SM3 等国密与国际标准算法
* **Burp Suite 联动**：将解密后的明文流量自动转发至 Burp Suite 进行进一步渗透测试
* **Hook + AI 智能注入**：结合 Playwright 浏览器 Hook 与 AI 分析，自动捕获前端加密逻辑
* **编码转换**：支持 Base64 / Hex / JWT 等常见编码格式的自动识别与转换
* **插件化架构**：支持 `.cbproj.zip` 格式的插件包导入导出，便于团队协作与复用

---

## 系统架构

### 整体架构图

```
┌─────────────────────────────────────────────────────────────┐
│                        用户界面层 (GUI)                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  插件构建器  │  │  AI 分析面板 │  │  流量监控 / 历史回放 │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                      核心引擎层 (Core)                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  配置管理器  │  │  插件加载器  │  │  AI 调用引擎        │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                    代理与处理层 (Proxy)                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  mitmproxy   │  │  加解密处理器│  │  流量转发器         │  │
│  │  (HTTP/HTTPS)│  │  (AES/SM4等)│  │  (Burp/本地)        │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                    扩展与工具层 (Extensions)                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Hook 脚本   │  │  签名生成器  │  │  编码/解码工具      │  │
│  │  (JS/Python) │  │  (HMAC/RSA) │  │  (Base64/Hex/JWT)   │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 数据流图

```
[客户端 APP/Web] ──加密流量──> [CipherBridge 代理]
                                      │
                                      ▼
                            [流量解析 / Body 解析]
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
              [AI 分析]      [插件加解密]    [Hook 注入]
                    │                 │                 │
                    └─────────────────┼─────────────────┘
                                      ▼
                            [明文流量输出]
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
           [GUI 展示]      [Burp Suite]      [本地转发]
```

---

## 项目结构

```
CipherBridge/
├── gui.py                    # GUI 主程序入口 (PyQt6 可视化界面)
├── main.py                   # 命令行代理入口 (mitmdump 脚本模式)
├── config.yaml               # 主配置文件 (框架模式)
│
├── core/                     # 核心引擎模块
│   ├── __init__.py
│   ├── config.py             # 配置解析与管理
│   ├── plugin_loader.py      # 插件动态加载器
│   └── ai_engine.py          # AI 分析引擎
│
├── algorithms.py             # 加解密算法库 (AES/DES/SM4/RSA 等)
├── sm_crypto.py              # 国密算法实现 (SM2/SM3/SM4)
├── signers.py                # 签名算法库 (HMAC/RSA-SHA 等)
├── encoding_utils.py         # 编码转换工具 (Base64/Hex/JWT)
├── body_parser.py            # HTTP Body 解析器
├── handler.py                # 请求/响应处理核心
├── forwarder.py              # 流量转发器 (Burp/本地)
├── codegen.py                # 代码生成器 (Hook/插件代码自动生成)
│
├── analyzer/                 # 流量分析模块
│   └── ...
│
├── plugins/                  # 用户插件目录
│   └── {app_name}/
│       ├── plugin.py         # mitmdump 插件脚本
│       └── state.json        # 插件状态与配置
│
├── profiles/                 # 应用配置文件目录
│   └── {name}.yaml           # 应用加解密配置
│
├── hooks/                    # Hook 脚本目录
│   └── ...                   # JS/Python Hook 脚本
│
├── extensions/               # 扩展模块
│   └── ...
│
├── sdk/                      # SDK / 加解密封装库
│   └── ...
│
├── replay/                   # 流量回放目录
│   └── ...
│
├── scripts/                  # 辅助脚本
│   └── ...
│
├── img/                      # 截图与文档图片
├── config/                   # 配置模板
│   ├── settings.yaml         # 主题/界面设置
│   └── ai.yaml               # AI API 配置
│
├── requirements.txt          # Python 依赖清单
└── README.md                 # 项目说明文档
```

---

## 核心模块详解

### 加解密算法模块 (`algorithms.py`)

该模块封装了所有主流加解密算法的统一调用接口，支持对称加密、非对称加密和哈希算法。

**支持的算法清单**:

| 算法类型 | 算法名称 | 模式/变体 |
| --- | --- | --- |
| 对称加密 | AES | ECB / CBC / CTR / GCM |
| 对称加密 | DES | ECB / CBC |
| 对称加密 | 3DES | ECB / CBC |
| 对称加密 | SM4 | ECB / CBC / CTR (国密) |
| 非对称加密 | RSA | PKCS#1 v1.5 / OAEP |
| 哈希 | MD5 | 标准 |
| 哈希 | SHA256 | 标准 |
| 哈希 | SM3 | 国密哈希 |
| 消息认证 | HMAC | HMAC-SHA256 / HMAC-MD5 |

**调用示例**:

```
from algorithms import CipherEngine

# AES-256-CBC 解密
engine = CipherEngine("AES", mode="CBC", key=b"32-byte-key-here", iv=b"16-byte-iv----")
plaintext = engine.decrypt(ciphertext)

# SM4-ECB 加密 (国密)
engine = CipherEngine("SM4", mode="ECB", key=b"16-byte-sm4-key")
ciphertext = engine.encrypt(plaintext)
```

### 国密算法模块 (`sm_crypto.py`)

纯 Python 实现的国密算法套件，不依赖外部 C 扩展，保证跨平台兼容性。

| 算法 | 功能 | 说明 |
| --- | --- | --- |
| SM2 | 非对称加密/签名 | 基于椭圆曲线密码 |
| SM3 | 哈希函数 | 256-bit 输出，类似 SHA-256 |
| SM4 | 分组对称加密 | 128-bit 分组，类似 AES-128 |

### 签名算法模块 (`signers.py`)

处理各类请求签名验证场景，常见于 API 接口防篡改设计。

* **HMAC-SHA256**: 密钥型消息认证码
* **RSA-SHA256**: 非对称数字签名
* **自定义签名**: 支持拼接参数 + 盐值 + 时间戳的复合签名

### 编码转换模块 (`encoding_utils.py`)

自动识别并转换常见编码格式：

| 编码 | 功能 |
| --- | --- |
| Base64 | 标准 / URL-Safe / 带换行 |
| Hex | 大写 / 小写...