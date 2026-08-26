---
title: RegPwn：Github再现exp投毒？
url: https://mp.weixin.qq.com/s/LmNR-zDC4J6ZVgfpjpJT1g
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:02:09.917915
---

# RegPwn：Github再现exp投毒？

# RegPwn：Github再现exp投毒？

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于潇湘信安
，作者3had0w

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM6fpNgxJic72iaxuNHwNA0BooiblUaaQuiavCyr7GWWPulUHw/0)

**潇湘信安**
.

一个不会编程、挖SRC、代码审计的安全爱好者，主要分享一些安全经验、渗透思路、奇淫技巧与知识总结。

早上起来闲着没事，本想复现测试下 RegPwn 提权漏洞写插件，在 github 搜索看到有两个几小时前刚更新过的项目：RegPwn、RegPwnBOF。

```
hxxps://github[.]com/tracyliving606/RegPwnhxxps://github[.]com/Snowyheronmusculusadductorlongus456/RegPwnBOF
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNIib9EibBazCZlvnl4trlcvJIg7Iq0lmKXT7iaMzsm4mibcR41aKCL6GYeDqGzQSWzS0LnzmURhElyoDcZY5nq1ib4jdR4wgon2UCYc/640?wx_fmt=png&from=appmsg)

第一眼看头像就感觉不太正常，两个账号下都只有这一个项目，而且注册时间均为2026年3月新建起开始活跃，正是 RegPwn 漏洞曝出的月份。

```
curl https://api.github.com/users/tracyliving606 | findstr _at  "created_at": "2026-03-07T23:08:29Z",  "updated_at": "2026-03-07T23:08:31Z"
curl https://api.github.com/users/Snowyheronmusculusadductorlongus456 | findstr _at  "created_at": "2026-03-01T08:02:32Z",  "updated_at": "2026-07-09T09:50:49Z"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNLnPGaKR4FP45mSt3ImmdnQ76dFYvAdJFMrb7I9gXTAJdPgibhtYlCfyNTIaPDKM0vfbvYVFJTSsZvyNGZscBKAjWibxP511W4II/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNISYIGNsbwtpGxTNh0R0icSUFVjBJWDy9GmIicEicq9EVLlrmlP1ib6O9SgmO0gM3CIAw3QPX0V68ZlnoFH7q5b5G5k6V8XcR73UgU/640?wx_fmt=png&from=appmsg)

RegPwn、RegPwnBOF两个源码传的都挺早，最近才更新的Reg\_Pwn恶意文件包和README.md，并会在README.md中引导受害者下载运行...！

```
Reg_Pwn_1.5.zipBOF_Reg_Pwn_v3.8.zip
```

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNJNLPXObmwdwkNqs9picNLzVkdgOzWVm4Yjw3NEYicNPgeyDLicMzG5PoGcVWiaXq0sND1xVyGt3R0X43EFegOLLG0lf4urastswUU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNLwAJeGm68aQn0YjaxEWPrglf5ZZZNWuw9UXpqCZauFpfnDOxuZrbrZuYwvhXBGmMnM07ZdsTTZA19jVNY3qSK5VOBuXWWhxn0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNLpaic4OS8CHruMhEGvTbs6DjDx1G6zIo5RbKpPicyR4ds1RT2mPDph5AmBXkfCEs1W3cF16j3LwbeBfaibflA73KTib1JKDXbrjnI/640?wx_fmt=png&from=appmsg)

注意：近几年在Github上投毒的很多，我们做安全研究时还得注意检查下项目的安全性，现在有了AI也方便很多，直接丢给AI去分析就行。。。

---

以下内容是我用AI对"RegPwn"投毒项目进行的静态分析报告，另一个"RegPwnBOF"投毒项目也差不多的，大概率为同一人或组织，这里我就不再去重复分析了，感兴趣的师傅可以自己去看下...。

# RegPwn 项目木马化供应链攻击分析报告

> **分析日期**：2026-08-23
>
> **威胁等级**：高危（trojan.lazy/convagent + trojan.mldk/ravartar）
>
> **分析结论**：RegPwn 源码本身为正常提权漏洞 PoC，但项目副本被植入了多层木马载荷，通过隐藏在 NuGet 依赖包目录中的 ZIP 文件进行投递。

---

## 目录

1. 项目背景与概况
2. 源代码分析：正常的漏洞利用工具
3. 木马发现：隐藏在 NuGet 包中的恶意载荷
4. 编译安全性分析：编译过程是否会中招
5. 触发机制：什么情况下才会中招
6. rest.txt 深度分析：VM 混淆与后门触发
7. C2 基础设施与攻击链路
8. 完整 IOC 列表
9. 攻击者画像与威胁评估
10. 防护建议与处置措施

---

## 1. 项目背景与概况

RegPwn 是一个针对 **CVE-2026-24291**（Windows 辅助功能基础设施本地提权漏洞）的 .NET 4.7.2 C# 漏洞利用工具。该漏洞由 Google Project Zero 安全研究员 James Forshaw 报告，MDSec 的 Filip Dragovic 公开了利用技术细节[^1]。

### 项目文件结构

```
RegPwn/
├── App.config
├── Config.cs                    # 配置类（用户输入参数存储）
├── Confuser.crproj              # ConfuserEx 代码混淆配置
├── packages.config              # NuGet 包引用
├── Program.cs                   # 主程序（漏洞利用逻辑）
├── RegPwn.csproj                # 项目文件
├── RegPwn.sln                   # 解决方案文件
├── WindowsApi.cs                # Windows API P/Invoke 声明
├── Properties/
│   └── AssemblyInfo.cs
└── packages/
    ├── dnMerge.0.5.15/          # 程序集合并工具
    │   └── ...
    └── NtApiDotNet.1.1.33/      # NT API .NET 库
        ├── NtApiDotNet.1.1.33.nupkg
        ├── .signature.p7s
        ├── lib/
        │   ├── net461/
        │   │   ├── NtApiDotNet.dll     # 未被篡改
        │   │   └── NtApiDotNet.xml
        │   └── netstandard2.0/
        │       ├── NtApiDotNet.dll     # 未被篡改
        │       ├── NtApiDotNet.xml
        │       └── Reg_Pwn_1.5.zip     # ★ 恶意文件（不属于官方包）
        └── ...
```

### 漏洞原理

CVE-2026-24291 的根源在于 Windows 对注册表符号链接的创建和解析缺乏严格的权限验证[^2]。攻击者在用户可写的 `HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility\Session<id>\ATConfig\osk` 键上创建符号链接，当 SYSTEM 权限进程复制该键时，跟随链接将攻击者控制的值写入任意注册表位置，从而实现本地提权[^3]。

---

## 2. 源代码分析：正常的漏洞利用工具

### 2.1 Program.cs — 漏洞利用主逻辑

程序接受四个命令行参数：`--regKey`、`--regValueName`、`--regValueData`、`--regValueType`，执行以下流程：

1. **读取目标注册表值**：检查 HKLM 下目标键是否存在
2. **获取会话路径**：通过 `GetTokenInformation` 获取当前会话 ID，构造 ATConfig 路径
3. **启动隐藏 OSK 进程**：通过 `ShellExecuteEx` 以隐藏窗口模式启动 `osk.exe`
4. **写入注册表值**：在 `HKCU\...\ATConfig\osk` 下写入攻击者控制的值
5. **设置 Oplock**：对 `oskmenu.xml` 文件设置独占锁
6. **锁定工作站**：调用 `LockWorkStation()` 触发辅助功能流程
7. **竞争窗口利用**：当 Oplock 被触发时，删除原注册表键并创建符号链接指向目标
8. **清理**：删除符号链接，验证提权是否成功

### 2.2 WindowsApi.cs — API 声明

声明了所需的 Windows API 函数，包括 `NtDeleteKey`、`RegCreateKeyExW`、`RegSetValueExW`、`ShellExecuteEx`、`LockWorkStation` 等，以及相关常量（`REG_OPTION_CREATE_LINK`、`REG_LINK` 等）。

### 2.3 源码结论

**源代码本身是正常的安全研究工具**，不含任何恶意网络通信、文件下载、持久化或数据窃取行为。所有逻辑均围绕注册表符号链接竞争条件提权展开。

---

## 3. 木马发现：隐藏在 NuGet 包中的恶意载荷

### 3.1 异常文件发现

在 `packages\NtApiDotNet.1.1.33\lib\netstandard2.0\` 目录下发现了一个名为 `Reg_Pwn_1.5.zip` 的文件（580,808 字节，创建时间 2026/3/29）。

### 3.2 官方包验证

通过检查 `.nupkg` 原始归档内容，确认 **官方 NtApiDotNet 1.1.33 包中不包含此文件**。官方包的 `lib/netstandard2.0/` 目录仅包含：

| 文件 | 大小 | 说明 |
| --- | --- | --- |
| `NtApiDotNet.dll` | 2,832,896 | 程序集 |
| `NtApiDotNet.xml` | 2,580,492 | XML 文档 |

`Reg_Pwn_1.5.zip` 是在 NuGet 包恢复后被**人为注入**的。

### 3.3 NtApiDotNet.dll 完整性验证

对 DLL 进行哈希比对，确认未被篡改：

```
官方 nupkg 内 DLL SHA256: 7600888EA1AD6C61D67F1BC221D17E6F5D1D6C88EE4531148241B55A2EC22C79
本地解压 DLL SHA256:      7600888EA1AD6C61D67F1BC221D17E6F5D1D6C88EE4531148241B55A2EC22C79
```

哈希完全一致，DLL 内部不存在加载 zip 的逻辑。

### 3.4 ZIP 内容分析

| 文件 | 大小 | 说明 |
| --- | --- | --- |
| `Launcher.cmd` | 26 字节 | 启动器 |
| `lua51.exe` | 872,448 字节 | 木马化 LuaJIT 解释器 |
| `rest.txt` | 299,679 字节 | VM 混淆 Lua 载荷 |

#### Launcher.cmd 内容

```
start lua51.exe rest.txt
```

#### VirusTotal 验证结果

**lua51.exe**（SHA256: `3EE51B5F9579B775E87EDB23C238650A512C2FE46EFC06694CD906A771727F97`）：

* **48/69** 个安全厂商标记为恶意
* 威胁标签：**trojan.lazy/convagent**
* 威胁类别：trojan + PUA
* 编译器：Microsoft Visual C/C++ 19.36.35724 (Visual Studio 2022)
* 实际为 **LuaJIT 2.1.0-beta3** 编译的 PE64 可执行文件

**rest.txt**（SHA256: `58448CB79F50CF71408E7EABFE7E0718E77A09910FD59963F83840B67FAA245F`）：

* **26/60** 个安全厂商标记为恶意
* 威胁标签：**trojan.mldk/ravartar**

**VT 社区标签**：`#cobalt-strike #icedid #luca-stealer #njrat #satacom`[^4]

---

## 4. 编译安全性分析：编译过程是否会中招

### 结论：编译过程不会触发木马，编译产物不包含恶意代码。

### 4.1 逐环节验证

#### 环节 1：C# 编译器引用范围

`.csproj` 中对 NtApiDotNet 包的唯一引用：

```
<Reference Include="NtApiDotNet, Version=1.0.0.0, ...">
  <HintPath>packages\NtApiDotNet.1.1.33\lib\net461\NtApiDotNet.dll</HintPath>
</Reference>
```

编译器只引用 `net461\NtApiDotNet.dll`，而 `Reg_Pwn_1.5.zip` 位于 `netstandard2.0\` 目录下，路径不在编译器引用范围内。

#### 环节 2：构建事件检查

| 检查项 | 结果 |
| --- | --- |
| `.csproj` PreBuildEvent | 空（`<PreBuildEvent></PreBuildEvent>`） |
| `.csproj` PostBuildEvent | 空 |

#### 环节 3：dnMerge 构建目标

`dnMerge.targets` 在 `AfterTargets="CopyFilesToOutputDirectory"` 时执行，仅处理 `ReferenceCopyLocalPaths`（即被复制到输出目录的 .NET 程序集 DLL）。`.zip` 文件不是 .NET 程序集，不在处理列表中。

#### 环节 4：NuGet 包机制

NuGet 的 `lib/` 目录约定：只有 `.dll`（引用程序集）和 `.xml`（文档）会被 MSBuild 识别和处理。其他类型的文件（如 `.zip`）被完全忽略，不会被复制到输出目录，也不会被嵌入程序集。

`.nupkg` 中不存在 `content/`、`contentFiles/`、`tools/install.ps1`、`init.ps1` 等自动执行机制。

#### 环节 5：源代码引用检查

对项目所有源文件（`.cs`、`.csproj`、`.sln`、`.config`、`.targets`、`.props`）进行字符串搜索，查找 `Reg_Pwn`、`zip`、`Launcher`、`lua51`、`rest.txt` 等关键词——**无任何匹配结果**。

### 4.2 编译产物内容

编译 + dnMerge 后，`RegPwn.exe` 中包含：

| 组件 | 来源 |
| --- | --- |
| RegPwn 的 IL 代码 | `Program.cs` 、`WindowsApi.cs`、`Config.cs` 编译 |
| NtApiDotNet.dll 的 IL 代码 | dnMerge 合并 |

**不包含** `Reg_Pwn_1.5.zip`、`lua51.exe`、`rest.txt`、`Launcher.cmd` 中的任何内容。

### 4.3 编译安全性总结

| 行为 | 是否安全 |
| --- | --- |
| 编译项目（`msbuild` / `dotnet build`） | **安全** |
| 运行编译后的 `RegPwn.exe`（基于此源码） | **安全** |
| 手动解压并运行 `Reg_Pwn_1.5.zip` | **中招** |
| 使用攻击者分发的预编译版本 | **可能中招** |
| 将此 `packages` 目录重新打包分发 | **传播风险** |

---

## 5. 触发机制：什么情况下才会中招

### 5.1 核心结论

`Reg_Pwn_1.5.zip` 是一个被"放置"在 NuGet 包目录中的**静态文件**。编译器不引用它，dnMerge 不处理它，NuGet 机制不复制它，DLL 也不加载它。**唯一的感染途径是手动解压并运行 zip 中的 `Launcher.cmd`。**

### 5.2 攻击者的投放策略

```
攻击者的设计思路：

1. 将木马嵌入正常安全工具的项目中
2. 借助 RegPwn/CVE-2026-24291 的知名度，...