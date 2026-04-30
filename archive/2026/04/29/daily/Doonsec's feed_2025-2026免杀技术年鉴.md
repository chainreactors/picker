---
title: 2025-2026免杀技术年鉴
url: https://mp.weixin.qq.com/s/PupDKHBbyP1ZKlaaAOoKow
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:27:42.017849
---

# 2025-2026免杀技术年鉴

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GEVYW8ofHic1Kznrj1LMJTS6QGt9dGalic6PdAFtpTDDHz6INAfYAUY2lROtWBNVylhD1lRXayhLiaDN9TaPh3bY7fOohl7iao2pj0wO3Z7VJME/0?wx_fmt=jpeg)

# 2025-2026免杀技术年鉴

原创

老鑫安全
老鑫安全

老鑫安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 2025年主流免杀技术观测：

| 技术 | 观测到的案例 | 来源 |
| --- | --- | --- |
| 自带易受攻击驱动程序（BYOVD） | Black Basta, ALPHV/BlackCat | Recorded Future，2025上半年恶意软件与漏洞趋势 |
| JIT Hooking与EDR静默 | LummaC2, Rhadamanthys | Check Point，《2026年美国网络安全威胁展望》 |
| AI驱动的多态恶意软件 | PrivateLoader变种 | 无公开报告 |
| ClickFix社会工程学 | 信息窃取程序 | Kaspersky SecureList，BlueNoroff GhostCall活动 |
| 通过PNG/WebP的隐写C2 | AsyncRAT, QuasarRAT | Trend Micro，《2025年网络风险报告》 |
| **Post-Quantum** C2 | 新兴APT组织 | 美国国家安全局，后量子网络安全资源 |

## 2025年免杀技巧：实现与防御

### 1. 自带易受攻击的驱动程序 (BYOVD)

工作原理：恶意软件加载已签名但存在漏洞的驱动程序（例如，来自华硕、微星或旧版英伟达的驱动程序），以禁用 EDR 内核回调。

案例：Black Basta 勒索软件

检测：

* • 监控具有异常映像路径的 NtLoadDriver 调用
* • 使用微软的驱动程序阻止列表（通过 Windows LAPS）
* • 部署 HVCI（虚拟机监控程序保护的代码完整性）

🔗 MITRE：T1068：利用驱动程序进行权限提升的漏洞利用

**Sigma 规则示例：检测 BYOVD 驱动程序加载（Black Basta、ALPHV）**

```
title: BYOVD Driver Load via NtLoadDriver
id: 9f3a1d2e-8b4c-4a1f-b5e0-7c9d2a1e8f3b
status: experimental
description: Detects non-standard driver loading via NtLoadDriver, typical in BYOVD ransomware (Black Basta, Dec 2025)
author: "Data Encoder TI Unit"
date: "2025-12-20"
logsource:
    category: process_creation
    product: windows
detection:
    selection_img:
        Image|endswith:
            - '\drvinst.exe'
            - '\hwpsetup.exe'
            - '\msiosup.exe'
            - '\atkexComSvc.exe'  # ASUS vulnerable driver loader
    selection_cmd:
        CommandLine|contains:
            - 'NtLoadDriver'
            - '\??\'
    filter_legit:
        Image|endswith:
            - '\csrss.exe'
            - '\winlogon.exe'
    condition: (selection_img or selection_cmd) and not filter_legit
fields:
    - CommandLine
    - Image
    - User
falsepositives:
    - Legitimate driver installers (rare; verify via hash)
level: high
references:
    - https://www.recordedfuture.com/byovd-2025
    - https://data-encoder.com/byovd-detection-guide/
tags:
    - attack.privilege_escalation
    - attack.t1068
```

### 2. JIT 挂钩和 EDR 进程静默

工作原理：恶意软件使用即时编译动态覆盖内存中的 EDR DLL 钩子。

案例：LummaC2

检测：

* • 监控 dllhost.exe 或 msedge.exe 中的 VirtualProtect + WriteProcessMemory
* • 启用 AMSI 进行 .NET 脚本扫描
* • 使用带有钩子完整性验证的EDR（例如，CrowdStrike、SentinelOne）

**YARA 规则示例：通过 .NET CLR 滥用检测 JIT 钩子（LummaC2 模式，2025）**

此规则用于识别以下有效载荷：

* • 滥用 InstallUtil.exe 或 RegSvcs.exe
* • 加载具有高熵的反射型 .NET 程序集
* • 包含用于修补 EDR 钩子的 JIT 相关 API 字符串

```
rule JIT_Hooking_EDR_Silencing_2025 : evasion memory_injection
{
    meta:
        author = "Data Encoder Threat Intel | Dec 2025"
        description = "Detects JIT-based EDR hook patching via .NET CLR (LummaC2, Rhadamanthys)"
        reference = "https://data-encoder.com/antivirus-comparison-detection-rates-and-algorithms/"
        license = "CC BY-NC-SA 4.0"

    strings:
        // Common parent processes
        $parent1 = "installutil.exe" ascii nocase
        $parent2 = "regsvcs.exe" ascii nocase
        $parent3 = "msbuild.exe" ascii nocase

        // JIT/CLR hooking indicators
        $jit_api1 = "VirtualProtectEx" wide
        $jit_api2 = "WriteProcessMemory" wide
        $jit_api3 = "GetModuleHandleA" wide
        $jit_str1 = "clr!MethodDesc::JITCompile" ascii

        // LummaC2 reflective loader pattern (entropy + section)
        $refl_pat = { 48 89 5C 24 08 48 89 74 24 10 57 48 83 EC 20 48 8B DA }

    condition:
        (uint16(0) == 0x5A4D) and // PE file
        filesize < 3000KB and
        (
            ($parent1 or $parent2 or $parent3) in (0..filesize) or
            (
                2 of ($jit_api1, $jit_api2, $jit_api3) and
                $jit_str1 and
                $refl_pat
            )
        )
}
```

### 3. AI生成的多态恶意软件

工作原理：恶意软件嵌入一个微小的 LLM，在执行之前重写自己的有效载荷——动态地更改哈希值和字符串。

案例：PrivateLoader 活动

检测：

* • 标记嵌入机器学习模型的二进制文件（高熵 + onnxruntime.dll）
* • 使用行为聚类归因分析而非静态哈希
* • 部署运行时间大于 5 分钟的沙箱

### 4. ClickFix 和虚假错误提示社会工程学

工作原理：用户会看到虚假的“Microsoft .NET 错误”或“缺少打印机驱动程序”提示，点击这些提示后，即可执行 PowerShell 或 MSI 有效负载。

减轻：

* • 通过组策略对象 (GPO) 阻止来自 Internet 区域的未签名 .msi 和 .ps1 文件。
* • 模拟ClickFix 网络钓鱼攻击对用户进行意识培训。
* • 使用应用程序控制（例如 WDAC）阻止未签名的脚本。

### 5. 无文件 .NET 和 PowerShell 滥用

工作原理：有效载荷通过 InstallUtil.exe、RegSvcs.exe 或 PowerShell AMSI 绕过（[Ref].Assembly.GetType(…)）驻留在内存中。

案例：RedLine Stealer

检测：

* • 记录 svchost.exe 的所有子进程
* • 为 PowerShell 启用受限语言模式
* • 通过 ETW 监控 CLR 组件加载情况

### 6. 隐写术 C2

工作原理：恶意软件从公共论坛下载 PNG/WebP 图像，然后通过 LSB（最低有效位）提取出 C2 IP地址。

案例：AsyncRAT

检测：

* • 分析图像熵异常
* • 阻止通往非商业图片主机的出站流量
* • 使用网络数据防泄漏 (DLP) 和隐写检测规则

## 2025 年制裁各杀毒软件厂商的最有效免杀手段

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GEVYW8ofHic24QhGvRJSkdXbbwfdNEwqoiccGbkiambC8axlQJ1BecMIDjGesNu0GAEDSFufoqAhk99R4byeVNCt8icvgtP8q0588trpKia944OU/640?wx_fmt=jpeg&from=appmsg)

**学习交流社区：**

![图片](https://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2caia1TibUgBtianj99mWACqBUDg0zaXuqBSAagQsAfTCSZ6qiap0ueQNcLYAzsYU9BPuGBDDx0sRLz0Q/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

**培训：**

[26老鑫安全培训](https://mp.weixin.qq.com/s?__biz=MzU0NDc0NTY3OQ==&mid=2247488853&idx=1&sn=befb7a3dc680411f0b86eff7349ff31b&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2ceUKiaEJfG0L5ZJtpCjuISeOmHuvZZbpibNciacvzGib2W6jibSJPwQnuibB9SIic18Eiafy2LZicYLiarnFtA/0?wx_fmt=png)

老鑫安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2ceUKiaEJfG0L5ZJtpCjuISeOmHuvZZbpibNciacvzGib2W6jibSJPwQnuibB9SIic18Eiafy2LZicYLiarnFtA/0?wx_fmt=png)

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