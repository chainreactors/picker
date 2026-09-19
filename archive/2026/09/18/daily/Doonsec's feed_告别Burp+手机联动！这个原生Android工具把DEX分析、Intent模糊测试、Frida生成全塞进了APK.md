---
title: 告别Burp+手机联动！这个原生Android工具把DEX分析、Intent模糊测试、Frida生成全塞进了APK
url: https://mp.weixin.qq.com/s/YERb5Xj7PIGyjIJrj9gBcA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:54:45.402666
---

# 告别Burp+手机联动！这个原生Android工具把DEX分析、Intent模糊测试、Frida生成全塞进了APK

# 告别Burp+手机联动！这个原生Android工具把DEX分析、Intent模糊测试、Frida生成全塞进了APK

原创

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 专为漏洞赏金猎人与移动安全研究员打造的 All-in-One Android 渗透测试工具箱。零依赖、全原生、大多数功能无需 Root，覆盖静态分析、动态测试、运行时分析与网络拦截四大攻击面。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFG3iaY8ibMhfKqND0txZE9qwkVStLvkYWmWBibFLUpicmejehly8QoLO8X7aJibIybtr8HQZ9thubMNXDhOpaxclx2TdUQBNY8K96CI/640?wx_fmt=png&from=appmsg)

## 核心定位

| 维度 | 特性 |
| --- | --- |
| **目标用户** | 漏洞赏金猎人（HackerOne/YesWeHack/Intigriti）、移动安全工程师、渗透测试人员 |
| **核心优势** | 全功能设备端运行，摆脱 PC 依赖，随时随地即开即测 |
| **权限要求** | 大多数功能无需 Root，部分高级功能需 `run-as` 或 ADB 调试 |
| **架构理念** | 原生 Kotlin 开发，零第三方库依赖，APK 体积极致精简 |

---

## 快速开始

### 构建安装

```
# 克隆仓库
git clone https://github.com/ynsmroztas/AndroHunter.git
cd AndroHunter

# 环境要求：Java 17 + Gradle 8.9
./gradlew assembleDebug

# 安装到设备
adb install app/build/outputs/apk/debug/app-debug.apk
```

### 系统要求

| 功能 | 说明 |
| --- | --- |
| 应用枚举 | 列出所有已安装应用及其元数据（包名、版本、权限、目标 SDK） |
| 智能筛选 | 系统应用 / 用户应用快速切换 |
| 快速入口 | 从应用详情一键跳转至任意分析模块（DEX/Manifest/Intent 等） |

### 2. DEX 分析器（DEX Analyzer）

#### 核心能力：

* 从 APK 中提取并分析 .dex 文件（支持多 DEX 应用）
* 硬编码密钥扫描：API Key、Token、密码、URL、私钥
* 字符串模式匹配 + 熵值分析
* 严重性三级分类：🔴 VULN（漏洞）/ 🟡 SUSP（可疑）/ 🟢 SAFE（安全）

#### 交互特性：

* 弹出式类与方法枚举器
* 每个 DEX 文件独立分析视图

#### 3. 清单查看器（Manifest Viewer）

| 标签 | 内容 |
| --- | --- |
| **组件** | Activity/Service/Receiver/Provider 导出状态分析 |
| **权限** | 危险权限高亮、权限组分类 |
| **原始 XML** | 完整 Manifest 源码查看 |

#### 4. 意图模糊测试器（Intent Fuzzer）

* 构造自定义 Intent（Extras、Data URI、Category 任意组合）
* 路径遍历载荷注入：file:///data/... 通过 Intent Data 传递
* 与 Payload 引擎联动，实现自动化模糊测试

#### 5. 载荷引擎（Payload Engine）

| 特性 | 说明 |
| --- | --- |
| **实时监控** | 基于 Logcat 的测试结果实时回显 |
| **自动投递** | Payload 自动发送至目标组件，无需手动复制 |
| **视觉分级** | VULN（红色确认漏洞）/ SUSP（黄色可疑）/  SAFE（绿色安全） |
| **专项测试** | 深度链接利用、OAuth 重定向劫持、文件 URI 泄露 |

#### 6. 内容提供程序模糊测试器（ContentProvider Fuzzer）

| 类型 | 载荷策略 |
| --- | --- |
| 基于错误 | 触发 SQL 语法错误回显 |
| 基于布尔 | 条件真/假响应差异判断 |
| 基于 UNION | UNION SELECT 数据提取 |
| 基于时间 | `SLEEP()` /`BENCHMARK()` 延时判断 |

#### 7. 文件提供程序路径分析器（FileProvider Path Analyzer）

| 路径类型 | 配置风险 | 等级 |
| --- | --- | --- |
| `root-path` 路径为空 | 完整文件系统访问权限 | **严重** |
| `external-path` 路径为空 | SD 卡全局访问 | **高危** |
| `cache-path` / `external-cache-path` | 缓存目录遍历 | **中危** |

#### 8. 活动启动器（Activity Launcher）

| 功能 | 说明 |
| --- | --- |
| 活动枚举 | 列出所有已安装应用的 Activity，标记导出状态 |
| 一键启动 | 支持附加数据 / 深度链接注入 |
| ADB 生成 | `adb shell am start -n pkg/activity --es data "payload"` |
| 快速筛选 | 仅显示导出 Activity，快速定位攻击面 |

#### 9. 广播模糊器（Broadcast Fuzzer）

| 类别 | 攻击场景 | 载荷示例 |
| --- | --- | --- |
| **身份验证绕过** | 登录绕过、会话劫持 | 空凭证 Intent |
| **SQL 注入** | 通过 Intent Extras 注入 | `selection` 参数污染 |
| **LFI/路径遍历** | 文件路径附加信息遍历 | `file:///data/...` |
| **开放重定向** | 深度链接劫持、OAuth 重定向 | 恶意 callback URL |
| **权限提升** | 组件启用、特权接口调用 | 启用被禁组件 |
| **数据泄露** | 备份意图、隐式 Intent 拦截 | 敏感数据外发 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHBLcgwVFzRyEJLoTGfjfedkDMBwd0IsAHQr9bk5VFIZjA09Uo8D6wB0AVa6IkgDqTIMnjAbBPXAI1ex3TpyND6jr4VcbMSbA4/640?wx_fmt=png&from=appmsg)

### 项目地址

```
https://github.com/ynsmroztas/AndroHunter
```

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

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