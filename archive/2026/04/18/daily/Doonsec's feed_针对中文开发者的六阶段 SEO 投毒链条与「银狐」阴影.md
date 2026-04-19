---
title: 针对中文开发者的六阶段 SEO 投毒链条与「银狐」阴影
url: https://mp.weixin.qq.com/s/wDwa3BhWvyCs6cer8azmYw
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:49:39.121768
---

# 针对中文开发者的六阶段 SEO 投毒链条与「银狐」阴影

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAiaHGm1FdLMfygJuXiakPI7zcWuk8wFvytWhKia0niaic2a0x1VN7icn4cjtw1dickZibibWg01BuLaocbjq1tY0AkzXKe1StNgTjMNzGQc/0?wx_fmt=jpeg)

# 针对中文开发者的六阶段 SEO 投毒链条与「银狐」阴影

原创

独眼情报
独眼情报

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 长话短说

* 2026 年 3 月,eSentire 威胁响应部门(TRU)在客户环境中捕获一条针对**中文开发者和运维人员**的六阶段感染链,将其命名为 **Kong RAT**——样本中注册表键、文件路径、环境变量大量使用「Kong」字符串,这是命名依据。
* 入口是 **SEO 投毒**:攻击者抢注 `finalshell-ssh[.]com`、`xshell-cn[.]com`、`quickq-cn[.]com`、`clash-cn[.]com`、`letsv-vpn[.]com` 等仿冒域名,针对中国开发者常用的 SSH 客户端、VPN、代理工具做假官网,通过搜索引擎排名把中毒站推到真官网之前。
* 六阶段链路如下:SEO 投毒 → .NET 10 NativeAOT 投放器 → 内存中 DLL 调度器 → 合法签名微软二进制 DLL 侧加载 → Shellcode 加载器 → Kong RAT 主体。**手法的工程化程度明显高于常见黑产样本**。
* 初始样本的 PDB 路径残留了开发者用户名 `52pojie`——这是中文破解论坛「52 破解」的直接引用。配合阿里云香港 OSS 作为载荷宿主、CSDN 引导受害者的记录、Kong RAT 自带中文错误消息(`读取插件数据失败`、`解密插件数据失败`、`加载 DLL 失败`),**现有证据指向一名中文母语开发者**,但 PDB 路径可被刻意伪造,**研判**不等于结论。
* 与 eSentire 此次披露**高度相似**的仿冒 FinalShell 活动,安天 CERT 在 2025 年 9 月已归因给中国**「银狐(SwimSnake/Silver Fox)」黑产家族**。eSentire 在报告最后也把安天这篇文章列为参考文献。**研判**:Kong RAT 大概率是银狐生态下的一个新工具族或新分支,并非独立新组织。
* Kong RAT 的 C2 框架支持 16 种确认的指令类型,涵盖远程执行、文件投送、热插拔 DLL 模块、远程迁移 C2、自毁、远程打标签等,**是一个「可扩展平台」而非固定能力的单体木马**。对防守方来说,这意味着「捕获一份样本不等于知道它能干什么」,后续能力可在运营期被动态下发。
* 决策者视角:如果组织内有中文开发者或运维在公网环境下载 FinalShell / Xshell / Clash / QuickQ,建议立即扫描本文末尾的五项主机 IOC(`Bvasted` 目录、`SimpleActivityScheduleTimer_*` 计划任务、`Software\Kong\` 注册表树、`C:\ProgramData\Kong\Keylogger\` 日志、`Plugins` 注册表值)。

---

## 一、事件时间线

下表节点精确到月,日期以 eSentire 报告披露内容为准,时区按报告默认(未显式标注,推测为 UTC)。

| 节点 | 事件 |
| --- | --- |
| 2025-05 | 首个仿冒域名 `xshell-cn[.]com` 注册,托管商 Dominet (HK) Limited,**研判**这是活动首个公开可见的基础设施痕迹 |
| 2025-07 | `finalshell-ssh[.]com` 、`quickq-cn[.]com` 相继注册 |
| 2025-08 | `clash-cn[.]com` 注册 |
| 2025-10 | `letsv-vpn[.]com` 注册,域名池持续扩展 |
| 2026-03-12 | Kong RAT 嵌入 EXE 编译时间戳 |
| 2026-03-21 | 侧加载 DLL `rcdll.dll` 编译时间戳 |
| 2026-03 | eSentire TRU 在客户环境中检测到完整感染链 |
| 2026-04-16 | eSentire 公开发布完整技术分析与 IOC 清单 |

从首个域名注册到公开披露**横跨约 11 个月**,说明攻击活动在被 eSentire 公开之前已经运转了相当长的时间,这期间真实感染规模尚无公开数据。**待证实**:活跃期内的感染量级。eSentire 只报告了客户侧的单点触发,没有给出总体统计。

## 二、初始入口:SEO 投毒 + 仿冒官网

攻击的起点不是邮件、不是漏洞、不是社工,而是搜索引擎。

![图 1:仿冒的 xshell-cn 与 quickq-cn 站点,模仿合法的中文开发者工具,通过 SEO 投毒投递被植入木马的安装包](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAjPdOskP7jHR3j7pyuib8lRV4gTeyAKSMeT7jFo3Np8xzYTmCAGSQPBnf6rqETiaxUdysTHEg7icM7XvV1RCOPHhVYMXhMxEfDNtQ/640?wx_fmt=png&from=appmsg)

图 1:仿冒的 xshell-cn 与 quickq-cn 站点,模仿合法的中文开发者工具,通过 SEO 投毒投递被植入木马的安装包

攻击者的逻辑很直接:中国开发者习惯在百度、Google 上搜「FinalShell 下载」「Xshell 中文版」「Clash 官网」,真官网本身 SEO 并不强(FinalShell 是国内小团队维护的跨平台工具,官网权重一般),攻击者通过抢注带有 `-cn`、`-ssh` 后缀的仿冒域名 + 付费 SEO,把中毒站推到真官网之前并不难。

以 `finalshell-ssh[.]com` 为例,整个页面用**简体中文**撰写,同时挂出「Windows 版下载」和「Mac 版下载」两个按钮——但无论点哪个,**下发的都是 Windows x64 恶意安装包**(`finalshell-SetupX64.exe`)。页面甚至嵌入了真实的 FinalShell 4.2.4 界面截图和中文终端会话截图,外观上几乎看不出破绽。

![图 2：finalshell-ssh.com 冒充合法的 FinalShell SSH 客户端下载页,整站简体中文,针对中文开发者](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAj2MXqzamR7lp7fwbHMtrExBIy5IrdCfXQD6eJjqRzNTfycha62cB81995IET7GZVEVbjlSMQav9uib5URtAV9PkXBmWxFDUSBQ/640?wx_fmt=png&from=appmsg)

图 2：finalshell-ssh.com 冒充合法的 FinalShell SSH 客户端下载页,整站简体中文,针对中文开发者

![图 3:平台「伪选择」——不管你是什么系统都给你 Windows 恶意包](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAgzJRVfRz5WBJ4tE44xDqjVTMMdU1NQV9JKmUbpgSul51CR8JJnicaLibXibjCAly9eTKImft43GiaNwk0ydKfRRUwaJnZ7KCMve7s/640?wx_fmt=png&from=appmsg)

图 3:平台「伪选择」——不管你是什么系统都给你 Windows 恶意包

### 基础设施同源

根据 eSentire 的 DNS 基础设施分析,下列域名共享同一个 51LA 统计证书(`51LA-3JTC2JD0CXBQHRSX`),注册商大多为 Dominet(HK),载荷宿主统一为阿里云香港 OSS:

| 域名 | 首次出现 | 注册商 | 仿冒目标 |
| --- | --- | --- | --- |
| xshell-cn[.]com | 2025-05 | Dominet (HK) Limited | Xshell SSH 客户端 |
| finalshell-ssh[.]com | 2025-07 | Dominet (HK) Limited | FinalShell SSH |
| xshell-38m.pages[.]dev | 2025-05 | Cloudflare | Xshell SSH |
| quickq-cn[.]com | 2025-07 | Dominet (HK) Limited | QuickQ VPN |
| clash-cn[.]com | 2025-08 | Dominet (HK) Limited | Clash 代理 |
| letsv-vpn[.]com | 2025-10 | Dominet (HK) Limited | 乐视 VPN |

![图 4:51LA 统计证书把五个仿冒域名聚合到同一攻击者](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAjncOp4ObOicwXHYaYyOaW7EaJJbibO4FuSBVshQicZGGBsjACvMa9ppXKo1NYUdZ7wcTwEOT0oS33fxcK523JWU8tBEWSwZr3ibsA/640?wx_fmt=png&from=appmsg)

图 4:51LA 统计证书把五个仿冒域名聚合到同一攻击者

这个目标池选得极其精准:**SSH 客户端用于触达生产环境,VPN 与代理工具被国内开发者广泛用于访问 GitHub / 境外资源,本身就天然承载身份凭据和跳板能力**。一旦中招,受害者对攻击者的价值远高于普通家用电脑——这决定了这一类活动的收益率,也解释了为什么攻击者愿意长期维护这套基础设施。

## 三、技术链条拆解

整个链条有六个阶段,每一阶段的设计都有明确的绕检目的。

### 3.1 Stage 1:NativeAOT 投放器 Setup.exe

假官网下发的 `Setup.exe`(5.36 MB,SHA256 `D6620D...F1AEA`)使用 **.NET 10.0 NativeAOT** 编译。这是一个关键选择:NativeAOT 把 C# 直接编译成原生机器码,**dnSpy、ILSpy 这些主流 .NET 逆向工具全部失效**——拿到样本也看不到托管字节码,只能当 C++ 二进制分析,大幅抬高了逆向门槛。

这个投放器的 PDB 路径残留了一条关键痕迹:

```
C:\Users\52pojie\Desktop\bin\bin\Release\net10.0\win-x64\native\APP3.pdb
```

`52pojie` 直接指向中文破解论坛「52 破解」(52pojie.cn)。这一条如果单独看只是弱证据——PDB 路径可以随便改——但结合整个链路中的阿里云香港 OSS、CSDN 引导、Kong RAT 本体中的中文错误消息、针对中文开发者工具的精准仿冒,**研判**:开发者一方为中文母语者的概率很高,但**这并不足以断定是 APT 还是黑产,也不足以归因到具体组织或个人**,因为所有这些指标都可以作为假旗使用。

投放器的执行流很朴素但效率很高:先检查自身是否拥有管理员权限,如果没有就通过 `ShellExecute("runas")` 触发 UAC 弹窗让用户点一下——这是公开已知的最老套的提权手法,但**对普通开发者而言,装个 SSH 工具弹出 UAC 完全符合预期,几乎没人会起疑**。

![图 5:Setup.exe 的执行流](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAjYf9hbfXuZo9IcwlSGgqxibib9DQlW4Rjso5Nhw3bzkJ5RQibqHz52hgiaLztCvtSfsC37Z568218Gpv9mPAx9XUSdmPHiakHCNNWE/640?wx_fmt=png&from=appmsg)

图 5:Setup.exe 的执行流

取得管理员权限后,投放器从阿里云香港 OSS 下载载荷:

```
hxxps://kkwinapp.oss-cn-hongkong.aliyuncs.com/dow/zj[.]mp4
```

扩展名 `.mp4` 是障眼法——这个「视频文件」其实是一个 Windows DLL,用标准 MP4 扩展名把可执行流量伪装成媒体流量,绕过那些按扩展名判定的代理检查和 DLP 策略。下载后通过**反射式 PE 加载器**在内存中映射并执行,不落盘、没有正常的导入链路,端点防护产品很难在下载这一步下结论。

### 3.2 Stage 2:zj.mp4——内存中的调度器

`zj.mp4`(2 MB,SHA256 `3A1DD7...6C820`)是一个 64 位 DLL。Setup.exe 通过反射加载调用它导出的 `run` 函数——**注意这个 `run` 导出约定贯穿整个感染链后续所有模块**,这是攻击者为自己设计的一种「插件接口」,每一级模块都暴露同名导出,便于上层调度器热拔插。

`zj.mp4` 做了几件事:

1. **构造四条下一阶段下载 URL**,全部指向同一个阿里云香港 OSS bucket,文件扩展名继续伪装(`.1x1`、`.d11`、`.bin`)以规避内容检查。
2. **枚举进程,特别关注 Telegram.exe**。如果发现 Telegram 在运行,会尝试调用 `tg://setlanguage/?lang=classic-zh-cn` 把 Telegram 界面悄悄切成中文。这个功能在当前样本中受一个内部标志位控制,**该标志位默认为 0**,eSentire 标注为「休眠功能」,**研判**这是为后续社工阶段预留的接口,当前版本未启用。
3. **落地三个文件到 `%LOCALAPPDATA%\Programs\Bvasted\`** 并全部设置 `HIDDEN | SYSTEM` 属性,让它们在标准资源管理器视图中隐形。
4. **向阿里云 OSS 的 `/dow/upload?log=` 端点上报安装遥测**——即`kkwinapp[.]oss-cn-hongkong[.]aliyuncs[.]com`**同时承担载荷分发和 C2 回传两个角色**,这个双用途设计让运维成本降到最低。
5. **通过直接 RPC 调用 `NdrClientCall3` 创建计划任务**`SimpleActivityScheduleTimer_{GUID}`,**绕过标准的任务计划器 COM 接口(ITaskService)**,这是为了规避那些监控 COM 调用的 EDR 钩子。

![图 6:zj.mp4 构造的四条下一阶段 URL](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAjDzV0z7Opm2myoD9sDtmcvZgT9hbpw09MXzeFD09AnAHgLo2XD5E4GHuvqbXvuQCibmUqibN7Z5cx6AENS26azqziaLb8ibhOZXrA/640?wx_fmt=png&from=appmsg)

图 6:zj.mp4 构造的四条下一阶段 URL

![图 7:绕过标准 COM 的计划任务创建](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAhj48Ak9MocZZVsj00UXRuzQSvsibqMLUYkuXEiblOxKib3LgJpTgGR1X2us3mlwiaVyuQ3h4r6wnYtP5MDNouS1SFsoR60K1CNwVA/640?wx_fmt=png&from=appmsg)

图 7:绕过标准 COM 的计划任务创建

计划任务的名称前缀固定为 `SimpleActivityScheduleTimer_`,GUID 每次安装重新生成——**这是一个高质量的主机侧 IOC**,蓝队可以直接用这个前缀做清单检索。

### 3.3 Stage 3:DLL 侧加载,借微软的壳

安装目录 `%LOCALAPPDATA%\Programs\Bvasted\` 下有四个文件:

* `Setupexe.exe`——**合法签名的微软 Resource Compiler(rc.exe)**,Windows SDK 自带工具
* `rcdll.dll`——恶意的 shellcode 加载器
* `oob.xml`——带 PEB 游走 shellcode 和嵌入 PE 的载荷
* `msvcr100.dll`——运行时依赖

这是经典的 **DLL Sideloading**:当 `Setupexe.exe` 被计划任务拉起,Windows 按 DLL 搜索顺序优先从可执行文件所在目录加载 `rcdll.dll`,于是恶意 DLL 被以微软签名进程的身份加载进来。选 `rc.exe` 是有考虑的——它的导入表只依赖 Kernel32 和一个额外 DLL,**攻击面极小,被 EDR 信任的可能性极高**。

![图 8:rcdll.dll 在 DllEntryPoint 中通过 QueueUserAPC 调度延迟执行](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAiaKcgiaLeWUU7SWFpqlk7oQIAup2ELk3QsuwLheDGUG22WiacVNZt0x1DdZIibScicVaw6LT4vw8I9heTmRJzz1VFhwyKbofzw9icbs/640?wx_fmt=png&from=appmsg)

图 8:rcdll.dll 在 DllEntryPoint 中通过 QueueUserAPC 调度延迟执行

`rcdll.dll` 没有在 `DllMain` 里直接跑恶意代码,而是通过 `QueueUserAPC` 把 `pfnAPC` 塞进 APC 队列,等宿主线程进入可警告(alertable)等待状态才执行。这一步的目的很单一:**规避专门监控 DLL 加载事件的安全产品**。

### 3.4 Stage 4:PEB 伪装 + COM UAC 绕过

如果 `pfnAPC` 检测到当前进程未提权,它会执行 `mw_RelaunchElevated`,**这段逻辑是整个链条里最值得注意的技术细节**,因为它**不需要任何用户交互就能完成提权**:

* **PEB 伪装**:函数在 `FastPebLock` 临界区内...