---
title: 红队视角：用 DeadMatter 做「离线凭据提取」并规避 AV/EDR
url: https://mp.weixin.qq.com/s/cbYgKNNd7C9jfE7UmD7rvw
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:55:15.257923
---

# 红队视角：用 DeadMatter 做「离线凭据提取」并规避 AV/EDR

# 红队视角：用 DeadMatter 做「离线凭据提取」并规避 AV/EDR

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

## 一句话速览

在授权红队演练里，**直接 dump LSASS** 或 **拆 SAM/SYSTEM** 早已是 EDR 重点盯防的动作。DeadMatter 的思路是：**不跟 EDR 在 LSASS 上正面交锋**，而是先用合法 DFIR 工具采集一份全内存镜像，再把解析动作搬到 EDR 看不见的地方——最终从镜像中雕刻出 NTLM 哈希、DPAPI 密钥等凭据。本文按红队视角拆解这套「离线提取 + 两阶段降噪」打法。

## 红队场景：直接摸 LSASS 为什么越来越难

授权渗透测试里，拿到一个域成员或普通管理员会话后，下一步通常是 **Credential Access**。常见打法包括：

* `procdump -ma lsass.exe`

  或自定义 LSASS minidump
* `reg.exe save`

  导出 SAM/SYSTEM
* Mimikatz `sekurlsa::logonpasswords`

这些方法的问题是：**EDR 对 LSASS 读取、进程注入、异常内存访问有专门 hook**，一碰就告警，演练直接翻车。

DeadMatter 提供的替代路径是：

> **用「合法取证工具」做内存采集（EDR 统计上更宽容），再把凭据提取挪到离线主机完成。**

这样，红队在目标机上留下的不是「LSASS 读取」痕迹，而是「DFIR 内存镜像采集」痕迹——后者在不少环境里被视为正常应急响应动作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0Fob2jTvBxMqNGOoFwyBlbxSGWNVluojqicd7VLrQ7q5ZTypkU5iaMpgFE6iakscEPr4dIIGKcmLlLZA6Rbfq6u1sqClbFH4YdBBM/640?wx_fmt=png&from=appmsg)

## 工具简介：DeadMatter 是什么

* **语言**

  C#（.NET Framework）
* **定位**

  偏移无关（offset-independent）凭据提取工具
* **输入**

  全内存 raw dump、LSASS minidump、解压后的休眠文件、VM 内存文件等
* **输出**

  NTLM 哈希、DPAPI 主密钥/预密钥、登录会话元数据
* **核心能力**

+ **结构化解析**

  模仿 Mimikatz 的 MSV 结构解析，按 Windows 版本定位结构体
+ **签名雕刻（carving）**

  不依赖地址布局，在原始字节中按凭据模式找 blob，残缺镜像也能跑
+ **离线运行**

  把「危险动作」从被 EDR 保护的目标机移到红队可控环境

---

## 环境要求与编译

### 1. 编译方式（推荐从源码审计）

DeadMatter 仓库不发布预编译二进制，需要自行构建：

```
PS > git clone https://github.com/qsecure-labs/DeadMatter.gitPS > cd DeadMatterPS > dotnet build -c release
```

编译完成后，产物位于：

```
DeadMatter\bin\Release\Deadmatter.exe
```

### 2. 预编译版本（仅限临时测试）

Hackers-Arise 作者提供了自己编译的版本，存放于 `soupbone89/Compiled-Binaries`。从第三方来源运行二进制有供应链风险，**正式演练建议只使用自行编译的可执行文件**，并在隔离环境中做哈希校验。

---

## 红队操作流程

### 阶段一：目标机上的采集

#### 步骤 1：确认 Credential Guard 状态

这一步决定后面是否值得一做：

```
PS > Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard
```

复制

* 返回 `{0}` → Credential Guard 关闭，继续。
* 返回非零/启用 → 凭据被隔离到 LsaIso.exe（VTL1），标准内存镜像里取不到，此路不通。

> 企业里大量 Windows 10 Pro 和 2025 年之前的 Windows Server 仍默认关闭 Credential Guard，所以这个前置条件在实践中经常成立。

#### 步骤 2：采集全内存

**方案 A：带 GUI —— FTK Imager**

1. 打开 FTK Imager。
2. 点击 **Capture Memory**。
3. 指定文件名和保存路径，默认设置即可。

**方案 B：纯 CLI —— DumpIt**

如果目标机没有图形界面，可用 DumpIt 命令行采集（GitHub 上可获取）。

#### 步骤 3：压缩与外移

服务器内存动辄 16–32 GB，完整 raw 镜像非常大。用 7z 压缩后可从 32 GB 降到约 12 GB，再通过红队通道外传到离线解析主机。

```
7z a memory_dump.7z memory_dump.raw
```

### 阶段二：离线解析

#### 默认模式：结构化 + 雕刻双管齐下

```
PS > .\Deadmatter.exe -f memory_dump.raw
```

这条命令先跑 Mimikatz 风格的结构化解析，再对未命中的区域做签名雕刻，结果会列出与活动/近期登录会话关联的凭据。

#### 纯雕刻模式

如果镜像不是标准 minidump、LSASS 进程边界不可定位，或只想做「无结构」恢复：

```
PS > .\Deadmatter.exe -f memory_dump.raw -m carve
```

#### minidump + 显式 Windows 版本

手上只有 LSASS minidump 时，可以指定解析器和系统版本，减少偏移错误：

```
PS > .\Deadmatter.exe -f lsass.dmp -m mimikatz -w WIN_10_1507 -v
```

* `-m mimikatz`

  ：使用 Mimikatz 结构解析路径
* `-w WIN_10_1507`

  ：锁定 Windows 10 1507 的 LSASS 布局
* `-v`

  ：verbose，输出更详细

#### 提取 DPAPI 密钥 + IV 爆破

要尽量扩大覆盖范围（凭据 + DPAPI + 初始化向量）：

```
PS > .\Deadmatter.exe -f memory_dump.raw -b -d
```

* `-d`

  ：启用 DPAPI 密钥提取
* `-b`

  ：对镜像做 IV 爆破搜索

这两个标志相互独立，组合使用可提升恢复率。

---

## 为什么能规避 EDR/AV

传统打法的风险在于「危险动作」和「目标主机」重叠：直接读取 LSASS → EDR hook 拦截 → 告警。DeadMatter 打法把风险拆成两段：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0HZVRhNkaLeK2tNIpD0m659aWmUb6noTaxsMgVXibvUt5eb61ficEkT8ezw1PicrHq2443eUcBxQTTdkNm2o88wh8txpB35d4qkss/640?wx_fmt=png&from=appmsg)

1. **采集阶段用合法 DFIR 工具**

   ：FTK Imager / DumpIt 是事件响应工具，EDR 一般不会一刀切地拦截；即便拦截，告警语义也是「取证工具运行」，不是「LSASS 被 dump」。
2. **解析阶段离线完成**

   ：DeadMatter 在攻击机或隔离沙箱里跑，EDR 完全不在路径上。
3. \*\* footprint 小\*\*：不需要把 LSASS 单独导出为 minidump，也不需要在目标机上执行高敏感解析工具；如果直接在目标机跑 DeadMatter，它体积轻、当前不被多数 AV 签名标记。

**但请注意**：「更少被检测」不等于「不可检测」。成熟 EDR 会对不在白名单上的取证工具告警；大文件外传本身也是可疑行为。

---

## 关键限制：Credential Guard 是硬门槛

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0GpiaqNlZQU67icuR4EsXialmLI2WkgzbSgv5WE39StqtfCicibBK8mElfRcHb0g2wAXlKCNtBNZPaOtDescmxAhh02EaFmAm8rq4oY/640?wx_fmt=png&from=appmsg)

| 状态 | 凭据位置 | DeadMatter 效果 |
| --- | --- | --- |
| 关闭 | 主存中，结构可解析 | 可恢复 NTLM/DPAPI |
| 开启 | VBS/LsaIso.exe（VTL1 隔离区） | 镜像里没有，无法恢复 |

所以红队标准操作纪律是：**采集前必须先查 Credential Guard**。开着就别浪费时间，要么换路径（如 CredGuard 绕过，超出本文范围），要么换目标。

---

## 蓝队反向启示

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0EpMSyzicfpK5HFE6DWgezyvcoicarWFf4sMUVucCfDHaxY0eVdbgKg3yOazq0edWHe0amncBic3Iibcia1KnaNTTomYBiaMpEtG26Kw/640?wx_fmt=png&from=appmsg)

红队视角的每个「便利点」，反过来都是蓝队加固时最值得优先考虑的点：

1. **开启 Credential Guard**

   ：凭据不可见，整条链直接失效。
2. **取证工具白名单**

   ：不要一刀切封禁 DFIR 工具，而是只允许清单内工具，其余告警。
3. **监控异常内存采集**

   ：盯 FTK Imager、DumpIt 等进程的启动，以及异常大文件落盘、外传。
4. **EDR 规则调优 + 行为基线**

   ：LSASS 访问、异常进程注入、凭证导出行为仍需持续覆盖。
5. **定期红队演练**

   ：用本文打法自测，验证告警链路真的会响。

---

## 参考来源

* Co11ateral. *Digital Forensics: Evading AV/EDR During Credential Extraction with DeadMatter*. Hackers-Arise, 2026-08-12. https://hackers-arise.com/digital-forensics-evading-av-edr-during-credential-extraction-with-deadmatter/
* QSecure. *QSecure at BlackHat USA 2025: Introduced DeadMatter at Arsenal*. 2025. https://www.qsecure.global/qsecure-at-blackhat-usa-2025-introduced-deadmatter-at-arsenal
* GitHub: `qsecure-labs/DeadMatter`. BSD-3-Clause. https://github.com/qsecure-labs/DeadMatter
* gengstah. *DeadMatter — Offline Credential Extraction from Memory Dumps*. https://gengstah.github.io/wiki/tools/deadmatter

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FVsicLIFGnlHARVu9oibTLBD8zFXQFFuYia7eru1cqqOplMeTZPrKhszicQyxTxIM9Nq9oY9bbN4FVLXb7nhoCQzBybxs1nyXJc6M/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外等平台- 搜索的内容通过结合编写 -

公众号 | AnQuan7 (Ots安全)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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