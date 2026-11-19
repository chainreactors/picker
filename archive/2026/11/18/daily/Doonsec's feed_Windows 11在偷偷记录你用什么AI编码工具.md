---
title: Windows 11在偷偷记录你用什么AI编码工具
url: https://mp.weixin.qq.com/s/PytA8Az5Q4x2zREi2oX8ew
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:43:35.270089
---

# Windows 11在偷偷记录你用什么AI编码工具

# Windows 11在偷偷记录你用什么AI编码工具

零日手记
零日手记

随笔漫记安全路

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 本文基于公开安全研究（xusheng.dev，2026年11月16日），分析Windows 11诊断数据收集机制中针对AI编码Agent的开发者工具监控功能。所有技术细节来自逆向分析和实测验证。

## 一、发现背景

2026年11月16日，安全研究员 xusheng 在用AI辅助逆向分析Windows 11最新系统二进制文件时，在一个名为 `MissionControlAggregator.dll` 的系统组件中发现了一组不寻常的字符串：`codex.exe`、`claude.exe`、`copilot.exe`、`cursor.exe`——当下最热门的AI编码Agent可执行文件名。

这些名字不是随意出现的。顺着引用追踪下去，他发现了一个完整的监控系统：**Windows 11 在后台记录你使用了哪些AI编码Agent和开发工具，把信息保存到本地，然后通过诊断数据通道上传给Microsoft。**

除非你在系统设置中手动关闭了"可选诊断数据"（默认开启），否则这些数据正在被上传。

## 二、被监控的工具清单

| 类别 | 被监控的可执行文件 | 说明 |
| --- | --- | --- |
| CLI编码Agent | codex.exe、claude.exe、copilot.exe、agy.exe | 命令行AI编码工具 |
| 桌面编码Agent | github.exe、claude.exe、codex.exe、cursor.exe、antigravity.exe | 桌面GUI AI编码工具 |
| 运行时/SDK | node.exe、python.exe、dotnet.exe | 附带发布者验证 |
| 编译器/调试器 | gcc.exe、clang.exe、gdb.exe、javac.exe | 无发布者验证 |
| IDE | devenv.exe、code.exe | Visual Studio / VS Code |

**值得注意的是**：对部分工具，系统还会验证数字签名发布者。Node.js槽位期望"Node.js Foundation"，Python期望"Python Software Foundation"，.NET和Visual Studio期望"Microsoft Corporation"。但GCC/Clang那组没有发布者检查——只看文件名。

这意味着：**把 cmd.exe 改名为 codex.exe 运行，就能触发检测。** 研究者实测验证了这一点。

## 三、技术拆解：数据是怎么收集的

![遥测数据流](https://mmbiz.qpic.cn/mmbiz_png/6mib2NemUDMA7RfjEmBiasm0HibeFZiccAOmI3AgXcjibOVx8WxCBNIB603N74UNrKb7l53sN4ibuUIdicZovuQdF0QJELt1kApR53OtQSM39Zsr1U/640?wx_fmt=png "遥测数据流")

### 3.1 监控组件：MissionControlAggregator

`MissionControlAggregator.dll` 是Windows诊断系统的一部分，由 `DiagTrack`（Connected User Experiences and Telemetry服务）启动的 `AggregatorHost.exe` 进程加载。

```
DiagTrack 服务 (PID: 10148)
  └─ AggregatorHost.exe (PID: 1500)
      └─ MissionControlAggregator.dll
```

该组件在加载时订阅了三类Windows事件：

| 事件源 | 用途 |
| --- | --- |
| KernelProcess.AppStateChangeSummary | 捕获Windows程序启动/状态变化 |
| Win32kTraceLogging.AppInteractivitySummary | 捕获桌面应用交互 |
| Microsoft.Windows.Lxss.Manager.Exec | 捕获WSL中运行的程序 |

### 3.2 匹配机制

组件内部有一组"可执行文件名匹配器"（executable-name matchers）。当上述事件携带一个进程名时，匹配器会逐个比对：

```
事件触发 → 提取 imageName → 匹配器比对
  ├─ codex.exe?     → 设置 CLI Agent bit 2
  ├─ claude.exe?    → 设置 CLI Agent bit 1
  ├─ cursor.exe?    → 设置 Desktop Agent bit 3
  ├─ python.exe?    → 设置 Dev Tool bit (运行时类)
  ├─ gcc.exe?       → 设置 Dev Tool bit 3 (编译器类)
  └─ ... (共12+4+5个槽位)
```

匹配成功后，对应的bit位被设置到聚合器的内部状态中。报告生成时，这些bit位被打包成一个位图（bitset），通过ETW（Event Tracing for Windows）发出。

### 3.3 报告内容

最终发出的ETW事件名为 `Segments.SubCohorts`，包含：

```
{
  "name": "Microsoft.Windows.MissionControlAggregator.Segments.SubCohorts",
  "ext": { "privacy": { "isRequired": false } },
  "data": {
    "Version": "0.1.5",
    "CliAgentSubCohorts": [4],
    "DesktopAgentSubCohorts": [0],
    "FlushedFromSave": true
  }
}
```

| 字段 | 含义 |
| --- | --- |
| CliAgentSubCohorts | CLI Agent使用位图（4位：codex/claude/copilot/agy） |
| DesktopAgentSubCohorts | 桌面Agent使用位图（5位：github/claude/codex/cursor/antigravity） |
| isRequired: false | 被归类为"可选诊断数据" |

**注意**：报告不包含提示词内容、源代码、文件路径或使用时长。只记录"这个工具被使用过"这一个bit的信息。但即便是工具使用事实本身，已经有显著的隐私含义——尤其对企业开发团队而言，使用哪些AI编码工具可能属于商业敏感信息。

### 3.4 数据持久化与上传

聚合器的状态保存在本地磁盘：

```
C:\ProgramData\Microsoft\Diagnosis\AggregatorStorage\MissionControlAggregator$
```

报告按大约每天一次的周期生成。`DiagTrack` 服务通过 `Diagtrack-Listener` ETW会话订阅这些报告，将其放入 `EventStore.db` 的上传队列。

研究者在上传队列中直接找到了Agent使用事件，确认数据确实被标记为上传。

## 四、关键问题：默认开启

这是整个发现中最关键的细节：

| 设置项 | 默认值 | 说明 |
| --- | --- | --- |
| AllowTelemetry | 3 | 包含可选诊断数据 |
| 可选诊断数据 | 开启 | 美国区域设置下默认开启 |
| CLICodingAgentUsage (Feature ID: 62580080) | 已启用 | 在测试VM中作为服务实验自动启用 |

研究者在干净的Windows 11 Home ARM64官方ISO安装中验证：完成初始设置后，未修改任何隐私设置，"诊断数据"开关已经处于启用状态，标签为"Include Optional"。

**换言之：如果你在美国区域设置下安装Windows 11，一路点"下一步"完成设置，你的AI编码工具使用数据就已经在被上传了。**

官方ISO的基线VM中该Feature默认关闭，但研究者的ARM64 VM中它作为"服务实验"被自动启用——说明Microsoft可能正在灰度推送这个功能。

## 五、如何关闭

### 方法一：系统设置（普通用户）

```
设置 → 隐私和安全 → 诊断和反馈
  → 关闭"发送可选诊断数据"
```

| 选项 | 效果 |
| --- | --- |
| 必需诊断数据 | 无法关闭，始终上传 |
| 可选诊断数据 | **关闭后，Agent使用数据不再上传** |

**注意**：Windows更新后该设置可能被重置。建议每次大版本更新后检查。

### 方法二：组策略（企业用户，更可靠）

```
# 打开组策略编辑器
gpedit.msc

# 导航到：
计算机配置 → 管理模板 → Windows组件
  → 数据收集和预览版本
    → "允许诊断数据" → 设置为 0（仅安全级别）
    → "限制转储收集" → 设置为 0
```

组策略设置的优先级高于用户界面设置，Windows更新不会覆盖。

### 方法三：注册表（高级用户）

```
# 设置为仅必需诊断数据
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\DataCollection" `
  -Name "AllowTelemetry" -Value 0

# 禁用DiagTrack服务（极端方案，影响其他诊断功能）
Set-Service -Name "DiagTrack" -StartupType Disabled
Stop-Service -Name "DiagTrack"
```

### 验证是否生效

```
# 检查当前遥测级别
Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\DataCollection" `
  -Name "AllowTelemetry"

# 检查DiagTrack服务状态
Get-Service DiagTrack | Format-Table Name,Status,StartType

# 检查MissionControlAggregator是否在运行
tasklist /m MissionControlAggregator.dll
```

## 六、这个功能合理吗？

### 支持方观点

| 理由 | 说明 |
| --- | --- |
| 产品改进 | Microsoft需要了解开发者使用哪些工具，以优化Windows开发体验 |
| 已有披露 | 可选诊断数据的说明中已包含"应用使用活动" |
| 可关闭 | 用户可以手动关闭，不影响系统功能 |
| 数据粒度低 | 只记录工具名称，不记录提示词或代码 |

### 反对方观点

| 理由 | 说明 |
| --- | --- |
| 默认开启 | 大多数用户不会主动关闭，等于事实上的强制收集 |
| 商业敏感 | 企业使用哪些AI编码工具属于商业策略信息 |
| 竞争情报 | Microsoft自家有Copilot，监控竞品（Claude/Cursor/Codex）使用情况有利益冲突 |
| 灰度推送 | 作为"服务实验"静默启用，用户不知情 |
| 更新重置 | Windows更新可能重置隐私设置，用户以为关了实际又开了 |

**核心争议**：Microsoft既是操作系统提供方，又是AI编码工具（Copilot）的竞争者。由操作系统层面收集竞品工具的使用数据，即使目的是"产品改进"，也难以消除商业监控的嫌疑。

## 七、总结

| 维度 | 事实 |
| --- | --- |
| 监控对象 | 7个AI Agent + 9个开发工具 |
| 监控组件 | MissionControlAggregator.dll |
| 数据内容 | 工具使用位图（不含提示词/代码） |
| 上传条件 | 可选诊断数据开启时（默认开） |
| 关闭方法 | 设置/组策略/注册表 |

**这不是阴谋论，是逆向分析确认的事实。** Windows 11确实在系统层面记录你使用了哪些AI编码工具，并且默认将这些数据上传给Microsoft。

作为开发者，你可以接受这个事实，也可以花30秒关掉它。但至少你应该知道它的存在。

## 参考

* 原始研究报告：https://xusheng.dev/posts/windows-coding-agent-telemetry/[1]
* HN讨论（485+ points）：https://news.ycombinator.com/item?id=50524736[2]
* Microsoft诊断数据隐私指南：https://learn.microsoft.com/en-us/windows/privacy/[3]

### 引用链接

[1]*https://xusheng.dev/posts/windows-coding-agent-telemetry/*

[2]*https://news.ycombinator.com/item?id=50524736*

[3]*https://learn.microsoft.com/en-us/windows/privacy/*

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/euBEasB1QK1mSyV63n51RYwjUnANgONCBIoG7rlnVw75VBa0K8ZtSh9RmNQBsX1ibHXx1Gw8emQgIjJAeNmdJGg/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过