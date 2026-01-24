---
title: WindowsBaselineAssistant——Windows安全基线核查加固助手
url: https://mp.weixin.qq.com/s/Lo-s_AjFYNDf8QvESkrdGg
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:24:36.229524
---

# WindowsBaselineAssistant——Windows安全基线核查加固助手

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AGUhPQZ04zx7RGQS4xf0ms95F2Qn9DFQlV4Iv7Pf8XDeW3vXY0dd7cYKxo2tsc05KHHT1iaNribR2tUshMvr5p2w/0?wx_fmt=jpeg)

# WindowsBaselineAssistant——Windows安全基线核查加固助手

原创

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

# WindowsBaselineAssistant 技术文档

## 1. 项目概述

### 1.1 项目简介

WindowsBaselineAssistant（WBA）是一款专为Windows操作系统设计的安全基线检测与加固自动化工具。通过预设的安全规则库，WBA能够快速扫描系统配置项，识别不符合安全基线标准的配置，并提供一键加固功能，显著提升系统安全加固效率。

![](https://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zx7RGQS4xf0ms95F2Qn9DFQOlWLkCjVHJfHicrJzX7DuZuib0VQHr5dT7n6LqvBJQ82oCN0p6oJNwYQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zx7RGQS4xf0ms95F2Qn9DFQiavibYFI8MvicYl5oicInianhjPY3e3crMTT0DOfyOcIQ83pIibdOUzlicFJw/640?wx_fmt=png&from=appmsg)

### 1.2 核心优势

* **自动化检测**：告别繁琐手工检查，实现一键式基线扫描
* **规则可定制**：支持灵活的XML规则配置，适配不同环境需求
* **结果可导出**：支持Excel格式报告导出，便于审计与归档
* **双模式操作**：独立检测模式与检测加固一体化模式
* **低环境依赖**：.NET 8版本已集成运行时，无需额外安装

### 1.3 版本演进

表格

| 版本范围 | 开发框架 | 运行环境要求 | 备注 |
| --- | --- | --- | --- |
| v1.0-v1.2.2 | .NET Framework 4.0 | 需安装.NET Framework 4.0+ | 传统版本 |
| ≥ v1.2.3 | .NET 8 with R2R | 已自包含运行时，开箱即用 | 推荐版本 |

---

## 2. 系统架构

### 2.1 技术架构图

```
┌─────────────────────────────────────────────────────────┐
│                     WindowsBaselineAssistant           │
├─────────────────────────────────────────────────────────┤
│  UI层: SunnyUI框架                                      │
│  ├─ 主控制台                                            │
│  ├─ 规则配置界面                                        │
│  ├─ 结果展示视图                                        │
│  └─ 日志监控窗口                                        │
├─────────────────────────────────────────────────────────┤
│  业务逻辑层                                             │
│  ├─ 检测引擎 (Registry/Secutedit)                      │
│  ├─ 加固执行器                                          │
│  ├─ 规则解析器                                          │
│  ├─ 报告生成器 (NPOI)                                  │
│  └─ 日志管理 (Log4Net)                                 │
├─────────────────────────────────────────────────────────┤
│  数据访问层                                             │
│  ├─ item.xml 规则库                                    │
│  ├─ config.cfg 安全配置模板                            │
│  └─ 系统注册表API                                       │
└─────────────────────────────────────────────────────────┘
```

### 2.2 核心组件说明

* **检测引擎**：双模式检测（注册表 + 安全配置模板）
* **规则解析器**：基于XML的灵活规则解析，支持六种判定逻辑
* **加固执行器**：自动应用安全配置，支持回滚机制
* **报告生成器**：基于NPOI生成标准化Excel报告

---

## 3. 功能特性

### 3.1 核心功能模块

表格

| 功能模块 | 子功能 | 技术实现 | 输出结果 |
| --- | --- | --- | --- |
| **基线检测** | 注册表项扫描 | Registry API读取 | 符合/不符合/手动检查 |
|  | 安全策略检查 | secedit.exe导出分析 | 数值比对结果 |
| **自动加固** | 注册表修复 | Registry API写入 | 加固成功/失败 |
|  | 策略配置应用 | secedit.exe导入 | 应用状态 |
| **报告管理** | 结果导出 | NPOI Excel生成 | .xlsx格式报告 |
|  | 日志记录 | Log4Net框架 | 运行时日志 |
| **规则管理** | 自定义规则 | XML动态加载 | 规则验证状态 |

### 3.2 检测类型详解

#### 3.2.1 Registry检测模式

* **适用场景**：Windows注册表配置项检查
* **技术路径**：`HKEY_LOCAL_MACHINE` 和 `HKEY_CURRENT_USER` 主键
* **支持类型**：String、ExpandString、DWord、QWord、MultiString
* **示例**：TCP/IP参数、安全选项、审计策略

#### 3.2.2 Secedit检测模式

* **适用场景**：本地安全策略、账户策略、用户权限分配
* **技术实现**：调用`secedit.exe`导出安全配置到config.cfg文件
* **解析方式**：INI格式键值对提取
* **示例**：密码策略、账户锁定策略、审核策略

---

## 4. 规则系统详解

### 4.1 规则文件结构

规则库文件：`item.xml`（位于程序同目录）

xml

```
<?xml version="1.0" encoding="utf-8"?>
<root>
<item>
<!-- 规则基本属性 -->
<name>规则名称</name>
<description>详细描述</description>

<!-- 检测配置 -->
<type>registry|secedit</type>
<registry>注册表路径</registry><!-- registry类型专用 -->
<regitem>注册表项名</regitem><!-- registry类型专用 -->
<mark>策略键名</mark><!-- secedit类型专用 -->

<!-- 判定标准 -->
<standard>标准值</standard>
<assessment>判定规则</assessment>
<valuetype>数据类型</valuetype><!-- registry类型专用 -->

<!-- 附加标识 -->
<manual>1</manual><!-- 手动加固标识 -->
<ignore>1</ignore><!-- 忽略检测标识 -->
</item>
</root>
```

### 4.2 判定规则类型

表格

| 判定规则 | 适用场景 | 判定逻辑 | 结果输出 |
| --- | --- | --- | --- |
| **enum** | 枚举类型配置 | 检测值 ∈ 标准值集合 | 符合/不符合 |
| **greaternumber** | 数值下限控制 | 检测值 > 标准值 | 符合/不符合 |
| **lessnumber** | 数值上限控制 | 检测值 < 标准值 | 符合/不符合 |
| **array** | 多值配置项 | 检测值数组 = 标准数组 | 相同/不同 |
| **equals** | 精确匹配 | 检测值 == 标准值 | 相同/不同 |
| **fixed** | 非固定值 | 标准值动态变化 | 需手动检查 |

### 4.3 数据类型映射

表格

| 注册表类型 | XML配置值 | 说明 |
| --- | --- | --- |
| REG\_SZ | string | 普通字符串 |
| REG\_EXPAND\_SZ | expandstring | 含环境变量的字符串 |
| REG\_DWORD | dword | 32位无符号整数 |
| REG\_QWORD | qword | 64位无符号整数 |
| REG\_MULTI\_SZ | multistring | 多字符串值（\0分隔） |
| REG\_BINARY | 暂不支持 | 二进制数据 |

### 4.4 规则配置示例

#### 示例1：注册表检测（源路由保护）

xml

```
<item>
<name>检查源路由配置</name>
<description>源路由攻击有源地址欺骗、IP欺骗等，需要检查是否启用正确配置源路由攻击保护。</description>
<type>registry</type>
<registry>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters</registry>
<regitem>DisableIPSourceRouting</regitem>
<standard>2</standard>
<assessment>enum</assessment>
<valuetype>dword</valuetype>
</item>
```

#### 示例2：安全策略检测（密码最长使用期限）

xml

```
<item>
<name>检查密码最长使用期限</name>
<description>长期不修改密码会提高密码暴露风险，需要检查密码最长使用期限。</description>
<type>secedit</type>
<mark>MaximumPasswordAge</mark>
<standard>90</standard>
<assessment>greaternumber</assessment>
</item>
```

#### 示例3：手动加固标识

xml

```
<item>
<name>检查屏幕保护程序密码保护</name>
<description>此配置需手动验证图形界面设置</description>
<type>registry</type>
<registry>HKEY_CURRENT_USER\Control Panel\Desktop</registry>
<regitem>ScreenSaveActive</regitem>
<standard>1</standard>
<assessment>equals</assessment>
<valuetype>dword</valuetype>
<manual>1</manual>
</item>
```

---

## 5. 部署与运行

### 5.1 环境准备

#### 5.1.1 .NET Framework版本（v1.0-v1.2.2）

powershell

```
# 检查.NET Framework版本
Get-ChildItem'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full\'|
Get-ItemPropertyValue-Name Release

# 安装.NET Framework 4.0
# 下载地址：https://dotnet.microsoft.com/download/dotnet-framework
```

#### 5.1.2 .NET 8版本（≥v1.2.3）

* **绿色部署**：直接运行`WindowsBaselineAssistant.exe`
* **无需安装**：运行时已通过R2R（Ready-to-Run）技术集成
* **兼容性**：支持Windows 10/11/Server 2016+

### 5.2 目录结构

```
WindowsBaselineAssistant/
├── WindowsBaselineAssistant.exe    # 主程序
├── item.xml                        # 规则库文件
├── config.cfg                      # 安全配置模板
├── NPOI.dll                        # Excel操作库
├── SunnyUI.dll                     # UI框架库
├── log4net.dll                     # 日志库
├── Log/                            # 日志目录
│   ├── WBA-20240101.log
│   └── ...
└── Reports/                        # 报告输出目录
    ├── Report_20240101_120000.xlsx
    └── ...
```

---

## 6. 使用指南

### 6.1 主界面功能

操作步骤：

1. **启动工具**：以管理员身份运行`WindowsBaselineAssistant.exe`
2. **加载规则**：程序自动加载`item.xml`规则库
3. **选择模式**：

* 仅检测：生成基线符合性报告
* 检测并加固：自动修复不符合项

4. **执行扫描**：点击"开始检测"按钮
5. **结果处理**：

* 查看实时日志
* 导出Excel报告
* 查看加固结果（如执行加固）

### 6.2 规则自定义流程

1. **备份原文件**：`copy item.xml item.xml.bak`
2. **编辑规则**：使用文本编辑器或XML编辑器修改
3. **语法验证**：

   powershell

   ```
   # PowerShell验证XML格式
   [xml]$xml = Get-Content.\item.xml
   $xml.Validate({throw$args[1].Exception})
   ```
4. **规则测试**：在测试环境中验证新规则
5. **正式部署**：替换生产环境规则文件

### 6.3 批量部署方案

powershell

```
# PowerShell批量部署脚本示例
$computers = Get-Content servers.txt
foreach($computer in $computers){
# 复制程序文件
Copy-Item-Path "C:\WBA\*"-Destination "\\$computer\C$\WBA\"-Recurse -Force

# 远程执行检测
Invoke-Command-ComputerName $computer-ScriptBlock {
        & "C:\WBA\WindowsBaselineAssistant.exe"/silent /export:"C:\WBA\Reports\$env:COMPUTERNAME.xlsx"
}

# 收集报告
Copy-Item"\\$computer\C$\WBA\Reports\*.xlsx""C:\Reports\"
}
```

---

## 7. 二次开发

### 7.1 开发环境搭建

bash

```
# 克隆仓库
git clone https://github.com/DeEpinGh0st/WindowsBaselineAssistant.git
cd WindowsBaselineAssistant

# 安装依赖（使用NuGet）
dotnet restore

# 编译项目
dotnet build -c Release
```

### 7.2 核心类结构

csharp

```
// 规则实体类
publicclassCheckItem{
publicstring Name {get;set;}
publicstring Description {get;set;}
publicCheckType Type {get;set;}// registry/secedit
publicstring RegistryPath {get;set;}
publicstring RegistryKey {get;set;}
publicstring SeceditMark {get;set;}
publicstring StandardValue {get;set;}
publicAssessmentType Assessment {get;set;}// enum/greaternumber/...
publicRegistryValueKind...