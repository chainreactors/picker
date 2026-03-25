---
title: 【免杀工具】ZeroEye5.0重大更新，新增.net劫持扫描及模板
url: https://mp.weixin.qq.com/s/KDOhlbZst1k1ACcXo_gGAA
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:13:00.122007
---

# 【免杀工具】ZeroEye5.0重大更新，新增.net劫持扫描及模板

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CicRuEUFbd2UBCZBUAlMwqYos16aKOxZ9HickAJ7icRW1DibYYCj0D86BePGCc0pOLlwHRrpnWib9MXBickIv09wgFP8yQHibOIQdBhTZWRJtPbH24/0?wx_fmt=jpeg)

# 【免杀工具】ZeroEye5.0重大更新，新增.net劫持扫描及模板

原创

零攻防
零攻防

零攻防

![]()

在小说阅读器中沉浸阅读

# 5.0版本（重大更新）

### 新增：.NET程序扫描与劫持

**支持.net程序，并且提供劫持的config和dll模板**

### 新增：sys扫描

**对sys的简单扫描，枚举系统上可利用的程序**

### 新增：C++类重建引擎

**针对 ？ @ # 这些类函数符号的反推，在vs中也可以定义使用**

### 新增：递归DLL依赖链解析

**查找 父目录/同目录/子目录 关联的dll，增强扫描结果**

### 改进：参数系统重构

**改进参数的使用，适配.net**

### 改进：输出优化

**好看......**

请前往 **github** 获取更多细节

# 功能概览

| 功能 | 说明 |
| --- | --- |
| **原生PE扫描** | 扫描EXE导入表，自动复制非系统DLL，生成代理DLL模板 |
| **.NET程序扫描** | 自动识别.NET程序，分析Config劫持/P/Invoke/Assembly侧加载向量 |
| **.NET Config劫持** | 自动生成AppDomainManager注入config + payload源码，即开即用 |
| **内核驱动扫描** | 扫描第三方驱动的IOCTL + 危险API（自动跳过微软签名驱动） |
| **C++类重建引擎** | 从MSVC修饰名反向重建C++类结构，生成3种代理DLL模板 |
| **类型过滤扫描** | `-t` 参数支持按类型扫描：gui/cmd/dotnet/sys，可组合 |
| **自动检测** | `-i` 和 `-d` 自动识别原生PE/.NET，无需手动判断 |

---

# 参数说明

```
用法: ZeroEye [选项]
选项:
  -h   <帮助|示例>                  显示帮助信息
  -i   <PE 文件>                    分析PE文件 (自动识别 原生/.NET)
  -p   <目录>                       扫描指定目录下的可疑程序
  -s   <签名检查>                   仅扫描有数字签名的程序
  -e   <排除EXE>                    排除仅依赖系统DLL的程序
  -d   <PE 模块>                    生成劫持模板 (自动识别 原生/.NET)
  -x   <架构>                       指定扫描架构 (64/86)
  -g   <排除列表>                   排除指定DLL (用|分隔)
  -t   <类型>                       扫描类型: gui,cmd,exe,dotnet,sys,all (默认: all)
  -IM  <PE 文件>                    查看导入表
  -EX  <PE 文件>                    查看导出表

示例:
  ZeroEye.exe -i a.exe                                          分析PE文件 (自动识别原生/.NET)
  ZeroEye.exe -d a.dll                                          生成劫持模板 (自动识别原生/.NET)
  ZeroEye.exe -p c:\                                            扫描C盘 (全类型)
  ZeroEye.exe -p c:\ -t gui                                     仅扫描GUI程序
  ZeroEye.exe -p c:\ -t dotnet                                  仅扫描.NET程序
  ZeroEye.exe -p c:\ -t sys                                     仅扫描内核驱动
  ZeroEye.exe -p c:\ -t gui,dotnet -s -x 64                     扫描已签名的64位 GUI+.NET程序
  ZeroEye.exe -p c:\ -s -x 64 -g "api-ms|ucrtbase" -e          扫描已签名64位 仅系统依赖
  ZeroEye.exe -IM/-EX a.dll                                     查看导入/导出表
```

---

# 输出目录结构

## 原生PE（白加黑）

```
Eyebin/Dll/x64/
└── notepad++[gui-5-3.2MB]/
    ├── notepad++.exe                    ← 目标程序
    ├── SciLexer.dll                     ← 可劫持DLL
    └── infos/
        └── Info.txt                     ← 分析结果
```

## .NET程序

```
Eyebin/Dll/x64/
└── GitHubProtocolHandler[dotnet-2-1.1MB]/
    ├── GitHubProtocolHandler.exe        ← 目标程序
    ├── GitHubProtocolHandler.exe.config ← 已替换为劫持config
    ├── GitHubProtocolHandler.exe.config.bak ← 原始config备份
    ├── *.dll                            ← 引用的依赖DLL
    └── infos/
        ├── Info.txt                     ← 分析结果
        ├── GitHubProtocolHandler.config ← 劫持config模板
        └── GitHubProtocolHandler_payload.cs ← payload源码
```

.NET 使用流程：

```
1. cd 到输出文件夹
2. csc /target:library /out:zeroeye_payload.dll /ref:System.Windows.Forms.dll infos\xxx_payload.cs
3. 运行 xxx.exe → 弹窗验证劫持成功
```

## 内核驱动

```
Eyebin/Sys/
└── dbutil_2_3[sys-50KB]/
    ├── dbutil_2_3.sys                   ← 驱动文件
    └── infos/
        └── Info.txt                     ← 签名者 + 危险API列表
```

---

# 文件夹命名规则

格式：`名称[类型-数量-大小]`

| 类型 | 含义 |
| --- | --- |
| `gui` | 原生GUI程序 |
| `cmd` | 原生控制台程序 |
| `dotnet` | .NET Framework |
| `dotnet-core` | .NET Core/5+ |
| `sys` | 内核驱动 |

示例：

```
notepad++[gui-5-3.2MB]          ← GUI程序，5个可劫持DLL，总大小3.2MB
cmd_tool[cmd-3-512KB]           ← 控制台程序，3个可劫持DLL
GitHandler[dotnet-2-1.1MB]      ← .NET Framework，2个劫持向量
myapp[dotnet-core-1-256KB]      ← .NET Core程序
dbutil_2_3[sys-50KB]            ← 第三方驱动，50KB
notepad++[gui-5-3.2MB](2)      ← 重复时自动编号
```

---

# 项目获取

## 公众号回复以下内容获得成品

*ZeroEye5.0*

## 开源项目地址

*https://github.com/ImCoriander/ZeroEye*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9q9BkLgdQNuBtMUMIsibLT0Qe4iajuCZKykKtIg46IDGNBme8zAOMVQBkdVUg8TG7nTvCeuDfaqJZibQfPTDMbQ6A/0?wx_fmt=png)

零攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9q9BkLgdQNuBtMUMIsibLT0Qe4iajuCZKykKtIg46IDGNBme8zAOMVQBkdVUg8TG7nTvCeuDfaqJZibQfPTDMbQ6A/0?wx_fmt=png)

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