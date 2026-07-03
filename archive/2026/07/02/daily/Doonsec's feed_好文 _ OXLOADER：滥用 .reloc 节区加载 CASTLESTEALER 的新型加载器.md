---
title: 好文 | OXLOADER：滥用 .reloc 节区加载 CASTLESTEALER 的新型加载器
url: https://mp.weixin.qq.com/s/Zu6U7jz0sqU1lvxDL5-0Ig
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:46:53.784825
---

# 好文 | OXLOADER：滥用 .reloc 节区加载 CASTLESTEALER 的新型加载器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqUsYrJIeQqDjJDRlpjmls0icV539BxT8y3gFzQI1C9WicLUsGib5LvqRb2QUq3ULzwgyIT2NWkTHhpcaaXdg0Dz3hCQicXD2kRicKKE/0?wx_fmt=jpeg)

# 好文 | OXLOADER：滥用 .reloc 节区加载 CASTLESTEALER 的新型加载器

原创

Daniel Stepanic
Daniel Stepanic

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 原文链接：https://www.elastic.co/security-labs/oxloader-malware-loader-infostealer
>
> 本文使用 Kimi-2.7 翻译。

Elastic Security Labs 发现了一种此前未被记录的 Windows 加载器 **OXLOADER**，它通过恶意 Google Ads 传播 **CASTLESTEALER** 窃密木马。该加载器在静态引擎和沙箱引爆中检出率都很低，使用了控制流平坦化、不透明谓词、MBA（混合布尔-算术）混淆、自修改解密 stub，并滥用 Windows `.reloc` 节区来暂存 shellcode。

Elastic 在针对某客户的活跃攻击活动中识别出 OXLOADER；其排除独联体（CIS）地区和俄语语言的检查，表明幕后可能是俄语系、以经济利益为动机的威胁行为者。目前尚未发现该家族的公开历史报告。

## 关键要点

* Elastic Security Labs 发现新型加载器 OXLOADER
* OXLOADER 通过恶意 Google Ads 传播 CASTLESTEALER
* 排除 CIS 地区和俄语语言，指向俄语系、以经济利益为动机的威胁行为者
* 静态引擎和沙箱引爆检出率低
* Elastic Defend 可通过高级防护能力阻断完整攻击链

# 恶意广告如何将 OXLOADER 投递给受害者

OXLOADER 通过伪装成 Node.js 的恶意 Google Ads 分发。受害者被重定向到中间域名，再下载托管在 Storj 上的批处理脚本，该脚本负责下载并执行 OXLOADER。

感染始于用户搜索 `lts version of node.js`，并点击赞助结果进入 `node-js[.]prentiva99[.]info`。这是一个恶意落地页，伪装成合法的 Node.js 部署平台。威胁行为者针对美国用户投放 Google Ads；该广告最后一次展示是在 2026 年 4 月 23 日，目前网站已下线。广告账户验证名为 `ВОЛОДИМИР ТЕРЕЩЕНКО`，注册地为乌克兰。该身份是真实运营者、掩护账号还是购买的证件，目前尚不清楚。2026 年 5 月 14 日，Google 已将该广告账户及其关联广告活动全部移除。

![Advertiser’s profile on Google Ads Transparency Center](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqXDLs6otic9uXHNYxHITWpKK1YQgwSGHxibzWoucCeEfKPt2ck1xsuWfuiajZs5UFvcm4XD7micgnIVscv3VzGpNspMlicttiaicFbGr0/640?wx_fmt=png&from=appmsg "Advertiser’s profile on Google Ads Transparency Center")

用户交互后，会通过 `app[.]miloyannopoulos[.]com/download?subid1=download` 被重定向，服务器返回 `302 Found`，指向载荷 URL `link[.]storjshare[.]io/raw/jux4e4ky5mruo4jkxsssp42sau4q/ruslan/BATPackageBuilderSetup.bat`。这是一个托管在 Storj 合法链接分享服务上的 Windows 批处理脚本，威胁行为者滥用该服务以绕过基于域名的信誉过滤。

该批处理脚本会显示一个假的软件安装向导界面，立即通过 PowerShell 从 Storj URL `link.storjshare[.]io/raw/jwwvr4oskkkjsgevt774ta62ehya/ruslan/aBsvwbdas.exe` 下载下一阶段可执行文件，并使用 `-Verb RunAs` 启动，以触发 UAC 提权提示。

![Batch script downloading and launching OXLOADER](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqW6HDfnCUiaialD3Z7IgzrIeQJX4oGacqqmU4t6SIEh34AqVT88Pr8CX3jtIS4y7eaveRJyYxib9Br20XkvrQg710CpXC6m0Tyw9E/640?wx_fmt=png&from=appmsg "Batch script downloading and launching OXLOADER")

批处理脚本执行后，Elastic Defend 检测到恶意行为（策略仅设置为检测），触发多条行为规则，包括 `Microsoft Common Language Runtime Loaded from Suspicious Memory`，暗示存在与 `CASTLESTEALER` 一致的 .NET 载荷。

![Elastic Defend alerts triggered upon script execution](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqX7jCcO1v9hc011zrsDsDGYDf4JuJz8ibia9wFRP0iaup8GcQx9GoRmLQkenRMVpia2KHzhKCKjOFDdRic0fAibdibQm4fic7ibPIPxH5ng/640?wx_fmt=png&from=appmsg "Elastic Defend alerts triggered upon script execution")

以下是从载荷下载到 CASTLESTEALER 部署的攻击链执行图（原文未提供图示）。

![Infection chain](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqWKCiaDVRFhxgWNcibxEiatAJ6ic5MjNwzyq3jJMCp5okkQwytHY3oq2d6GfkUcONpkAlwQWlb0iaclJe2r6oUHmdPibxgvgeNGkXp6A/640?wx_fmt=png&from=appmsg "Infection chain")

# OXLOADER 加载器：技术分析

我们团队分析的第一个 OXLOADER 样本伪装成流行工具 API Monitor（来自 rohitab.com）。由于大量合法代码和代码隐藏技术的存在，该加载器能够躲过静态文件分析工具的检测。

![VirusTotal showing small number of detections](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqUk1iapRaTnd8Z9Zicavhh277OeZXR2M7UOIicUOyeqiaDoZ4XpwYBxAjr4d6y4kyiaPkbqlbRp2ZiayqxibJmeoaf5QoHEqVGX1GfKng/640?wx_fmt=png&from=appmsg "VirusTotal showing small number of detections")

## OXLOADER 如何在运行时自解压

恶意代码在 CRT 初始化阶段就开始执行，早于任何用户代码。CRT 函数 `cinit()` 调用 `initterm()`，遍历 C++ 初始化器表（`__xc_a` → `__xc_z`）并调用每个入口。恶意开发者劫持了其中一个入口，使其指向一个先调用 `RegisterClipboardFormatW()` 再尾跳转到第一个解密 stub 的函数。

![Malicious code started through CRT initialization](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqWwicF0TRaDBKI6yWPajyJrib5Dxo3xibC9wpc9pGbA6jT8gdEarusiaL7KO4KpVuOcavxB4dzGJ9I9BDyk2jstOHsjDADNLic11VHw/640?wx_fmt=png&from=appmsg "Malicious code started through CRT initialization")

加载器使用自修改技术，配合多个解密 stub 逐步展开自身。原文提到“下面是运行时解密 stub 被 patch 到内存中的示例”，但页面未提供对应截图。

![Small decryption stub patched in](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqXdiahicu8EG7SWXNSYIWZZI5EPSeSAKbKchRUtnzicMKulica3GU7tzEAic5Wflezy8Juxpp3jTpEeTxXibUZ8RniaPJueDmePQzQtsI/640?wx_fmt=png&from=appmsg "Small decryption stub patched in")

patch 完成后，加载器解密一个 28,233 字节的区域。每个字节使用单字节 XOR 密钥解密，每次迭代后密钥都会更新：刚解密的明文字节会加到密钥上，再用于解密下一个字节。类似的解密例程总共运行三次，每次覆盖不同区域。

![Rolling-XOR decryption of next-stage code](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqVB9ibcEtgrWhnofePUwqic2ibv8U5WB8NNEVy7BAFn4JRIvNticY2DZ1g7NgMRl9nTdHaS16tLR5dEQuic2LSh2OUVmfrhRUyczO1c/640?wx_fmt=png&from=appmsg "Rolling-XOR decryption of next-stage code")

## 用于规避静态检测的混淆技术

OXLOADER 通过四层混淆技术破坏 IDA Pro 等二进制分析工具中的自动函数边界识别：控制流平坦化（CFF）、混合布尔-算术（MBA）、不透明谓词，以及跨非连续代码区域的函数分块。函数通过无条件跳转拼接在一起，某些区域通过运行时由 MBA 算术计算目标的间接跳转到达。结果是 IDA Pro 无法可靠重建函数边界，需要手动修复。

![Control-flow flattening with nested MBA arithmetic example](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqXhOUlqo9DKCBQFUsvNGw4Bgx2BhiaNrcy4BShTtvSGl8ZbgmzwggnTPmDDdgTkLE5DWmicjEAfGJia6zoVoWK3eVfj5pfdFgCWR8/640?wx_fmt=png&from=appmsg "Control-flow flattening with nested MBA arithmetic example")

加载器在运行时使用以下字符串解密算法解密各种字符串：

```
uint32_tobf_xor_a1_with_a2_plus_33FDA(uint32_t a1, uint32_t a2) {
return a1 ^ (a2 + 0x33FDA);
}
```

代码完全解压/解密后，恶意软件将该字符串解密函数与 Adler-32 API 哈希算法结合，动态解析其导入。

![String decryption and API resolving](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqXtyJoGv7icJicxGsfu8lCItkKhy2tanh9qAQicib3NX9tsLC1CVBGsKa3QVyqqgpvibnWKxHv7R4XW9dXQyOkwP4M1Akpw0qY2FPYI/640?wx_fmt=png&from=appmsg "String decryption and API resolving")

## OXLOADER 如何规避沙箱与虚拟机检测？

解析 API 后，OXLOADER 执行多项检查，确保机器在“干净环境”中运行，避免在沙箱环境中执行。

| 检查项 | 方法 | 阈值 |
| --- | --- | --- |
| 模拟检测 | 使用畸形资源调用 `WNetAddConnection2W` | 期望返回 `ERROR_BAD_NAME` (0x43) |
| CPU 数量 | 进程环境检查 | ≥ 3 CPUs |
| 内存 | `GlobalMemoryStatusEx` | ≥ 3 GB 物理内存 |
| 显示器刷新率 | WMI 查询 `Win32_VideoController` | ≥ 20 Hz |
| 地理区域 | `GetUserGeoID` | 排除独联体（CIS）GEO ID |

![Emulation check via WNetAddConnection2W](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqWib5RVPEKpZ1by8LuibdQXk3uU7GtsickDibiaCvKZQH9NaUCIKibIMicIVA9OSu10PHdar2zy3FzCPv6B9dtJdtgUf20wBDo8dqyxbw/640?wx_fmt=png&from=appmsg "Emulation check via WNetAddConnection2W")

第一项检查尝试使用 `mpr!WNetAddConnection2W` 连接一个故意构造为畸形的网络资源（`*72s@1s`）。该技术似乎能够击败可能会无条件 hook 或返回成功连接的模拟/沙箱。恶意开发者通过直接访问 TEB 获取 `LastErrorValue` 来验证此调用。加载器期望该错误码为 `ERROR_BAD_NAME (0x43)`；若是其他值，恶意软件将走失败分支并停止执行。

第二项检查是基于处理器数量的反沙箱测试：加载器要求主机至少拥有 3 个 CPU 才会继续运行。许多沙箱和分析虚拟机为节省资源仅配置 1 或 2 个 CPU，因此该阈值可过滤掉这些自动分析环境。

![Anti-sandbox check using CPU count](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqXViapKuyResYliaiaEia37y9rwJSjbs40QLhNTdnIxJYLbtFYZyDUYNp3b2LvfDjMBpVFth3Y1YonRvPMeY3nSHicibGgYt0GgUAw88/640?wx_fmt=png&from=appmsg "Anti-sandbox check using CPU count")

第三项检查使用 `GlobalMemoryStatusEx()` 验证主机至少拥有 3 GB 可用物理内存。

![Anti-sandbox check based on RAM](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqXsBYh6lb8oaUGic5Alb1ibjyo6QPMOU2X7tlWWXtuvIicLSmLJc3h06dQkJy2X4aN4wiandbfNYFGsYibEPhhicv0XOTunW0J4wibTNA/640?wx_fmt=png&from=appmsg "Anti-sandbox check based on RAM")

第四项检查使用 WMI 查询系统显示器刷新率，执行 WQL 语句 `SELECT CurrentRefreshRate FROM Win32_VideoController`，并将返回值（赫兹）与阈值 20 比较。物理显示器通常报告 60 Hz 或更高，而无头和默认虚拟化配置通常报告 0 或 1，低于 20 的值会导致加载器中止。

![Anti-sandbox check based on refresh rate](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqUbng7vuEZ7BJvL67fvkoicXnuPssI7Zdrl0r7qGl1xKrUo9jcJPw5CNaneLibdYia7AtvupVmvL0jicEFJPr3M8IGnlV8xWX5W7QY/640?wx_fmt=png&from=appmsg "Anti-sandbox check based on refresh rate")

## 地理与语言排除

最后两项检查在主机位于独联体（CIS）国家或系统语言为俄语时停止执行。第一类检查使用 `GetUserGeoID` 获取系统地理区域，并与硬编码的 CIS 国家 GEO ID 列表比较。

![CIS country exclusion list](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqXMOVy9qaoKlx6qSRF5LexmtGVr7dcYMWjWXvkGVtO6vsiaSoySRZOu3YwSKJibCy7SMzLF9eLOANN8q3m9UlW3VLLQzd3J1gvSA/640?wx_fmt=png&from=appmsg "CIS country exclusion list")

第二类检查使用 `GetUserDefaultUILanguage`，匹配 LANGID（`0x419 - Russian, Russia`），这是俄语版 Windows 的标准配置。

![Russian language exclusion](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqXtwu8bLdOh6uTJ9vFCdAyVZETySsx8s7ia...