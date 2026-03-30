---
title: GlassWorm 第四部分：原生二进制分析——DLL注入、Chrome侧载、工作区窃取
url: https://mp.weixin.qq.com/s/DuAV091t6gCOz61rgUCj4w
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:38.621660
---

# GlassWorm 第四部分：原生二进制分析——DLL注入、Chrome侧载、工作区窃取

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0ibcazEYyMzrvDFlbHPEHJdRXicUyrJkM2Yv1g1lhOTzHqfrgn0R9FIWHr127C2SuG2ncTT7stmOLWAbznjxyNrkdXllJ14dnWT5TKSsyknys/0?wx_fmt=jpeg)

# GlassWorm 第四部分：原生二进制分析——DLL注入、Chrome侧载、工作区窃取

夯磅棱

![]()

在小说阅读器中沉浸阅读

> 在GlassWorm Wave 3攻击活动中，攻击者通过Node.js模块分发了多个原生二进制文件。深入分析揭示了其真实用途：两个配对文件（c\_x64.node + data）用于注入浏览器进程并窃取DPAPI和Chrome新版应用绑定加密密钥；w.node和m文件实为跨平台的Chrome扩展侧载工具，用于持久化恶意扩展f\_ex86.node则被证实是一个VS Code和Cursor IDE工作区项目枚举工具，为后续针对性的供应链投毒提供目标列表。文章修正了此前基于文件名的错误判断，并给出了完整的攻击链与检测指标。

## 修正第三部分的判断

在分析了所有五个从Wave 3 npm档案中提取的原生二进制文件（通过静态分析字符串、导入表、导出表和嵌入数据）后，我们修正了第三部分的结论。

当时基于文件名和JavaScript调用上下文的判断，大部分是对的，但也有两处严重错误。这里说明一下：c\_x64.node确实是浏览器凭据转储工具，w.node和m确实是Chrome扩展侧载工具。但有两个文件搞错了：

* data文件：我们之前说它是“浏览器进程检测器”，实际上它是一个完整的DPAPI和Chrome应用绑定加密密钥提取器，设计用来被c\_x64.node通过APC注入到浏览器进程中。它们是一对注入器-助手。
* f\_ex86.node文件：它不仅读取VS Code工作区，还读取Cursor IDE的工作区。

另外，之前提到led-win32和Chrome扩展background.js还没有深入分析，现在这两个我们也分析完了。

## 二进制文件的真实身份

通过内部DLL名称、PDB路径、嵌入字符串和导入表，我们确定了这些文件的真实身份：

| 文件 | 原先描述 | 反汇编发现 | 内部名称 |
| --- | --- | --- | --- |
| c\_x64.node | 浏览器凭据转储器 | 浏览器凭据转储器—13种浏览器，7类数据，APC DLL注入 | dump\_browser\_secrets.node |
| data | 浏览器进程检测器 | DPAPI + App-Bound密钥提取器，由c\_x64.node注入 | 无导出（仅用于注入） |
| w.node | Chrome扩展侧载器 | Chrome扩展侧载器（Windows） | ext\_sideloader.dll |
| f\_ex86.node | VS Code工作区读取器 | VS Code + Cursor工作区窃取器 | vscode\_env\_history.dll |
| m | Chrome扩展侧载器（macOS） | Chrome扩展侧载器（macOS） | ext\_sideloader |

简单说，c\_x64.node和data是一对，通过COM IElevator绕过Chrome的应用绑定加密。f\_ex86.node额外瞄准了Cursor IDE。

## 注入器配对：c\_x64.node + data

### c\_x64.node：浏览器秘密转储器

这是档案中最大的Windows二进制文件，有1.4MB，是个C++写的PE32+ DLL。它转储13种浏览器、7类数据的凭据。文件里保留着PDB路径：

N:\work\chrome\_current\DumpBrowserSecrets\build\Release\dump\_browser\_secrets.pdb

编译时间戳显示是2026年3月15日，UTC时间15点50分39秒，是整个档案里最新编译的二进制文件，就在攻击活动重启前一天编译的。

它导出了两个N-API函数给JavaScript调用：extractBrowserData和isBrowserInstalled。目标浏览器有13种：前7种（Chrome、Edge、Brave、Opera、Opera GX、Vivaldi、Firefox）在.rdata区段里有明文可执行文件路径。后6种（Yandex、Chromium、CocCoc、Torch、CentBrowser、Epic Privacy Browser）是通过解码一个13个case的TLS切换表里经过异或混淆的配置文件路径来发现的。

它的解密能力覆盖三种方法：AES-256-GCM（用于Chrome v80+的Cookies和密码）、AES-256-CBC（用于旧版基于Chromium的浏览器）、以及PBKDF2 + SHA1 + 3DES（用于Firefox NSS加密的密码）。提取内容包括7类Chromium数据：Cookies、登录信息、历史记录、自动填充、书签、信用卡、令牌，外加一个Opera特有的access\_tokens查询。

更厉害的是，JSON输出里包含浏览器账户元数据：邮箱、用户ID、验证状态、会话令牌、同步OAuth令牌、配置文件OAuth令牌，甚至还有发送/关闭标签页的私钥。拿到同步OAuth和发送标签页私钥，攻击者就能冒充受害者的浏览器进行Chrome同步，还不用重新认证。

#### 注入机制

在文件偏移0x12530的位置，有一个UTF-16LE格式的字符串：

%sDllExtractChromiumSecrets.dll

这就是将被注入浏览器进程的助手DLL的文件名模板。导入表证实了注入手法是APC注入。

整个流程是：

1. 使用FindResourceW等API从PE资源类型“DLLFILE”、ID 101中提取嵌入的data.dll（助手DLL就在c\_x64.node自身里面，不是从档案加载的）。
2. 用CREATE\_SUSPENDED等标志创建浏览器进程作为调试对象。
3. 在目标进程分配内存，把DLL路径写进去。
4. 调用QueueUserAPC，以LoadLibraryW作为APC函数，排队让被挂起的线程加载DLL。
5. 调用DebugActiveProcessStop分离调试器，这会刷新调试事件队列，触发APC执行。

结果通过命名管道回传。注入器创建一个命名管道，注入助手DLL，然后从这个管道读取提取到的加密密钥。

所以，同一个档案里的data二进制文件（40KB，PE32+ DLL，零导出）就是DllExtractChromiumSecrets.dll。

### data：用于提取Chromium秘密的DLL

这个40KB的DLL编译于2026年1月29日，没有任何导出。这意味着它不能通过正常的LoadLibrary和GetProcAddress加载，它就是为进程注入而生的。

它主要干两件事：

1. **提取V10密钥**

   ：也就是传统的DPAPI密钥。它会读取浏览器的Local State文件，解析JSON找到encrypted\_key字段，通过CryptUnprotectData解密出主密钥。
2. **提取V20密钥**

   ：也就是绕过Chrome 127+引入的应用绑定加密。它通过COM调用浏览器特定的IElevator接口来解密。

有个细节是文件句柄窃取。如果Local State文件被运行中的浏览器锁定了，这个DLL会通过NtQuerySystemInformation枚举全系统打开的文件句柄，找到匹配目标路径的句柄，然后用DuplicateHandle直接从浏览器进程“偷”出句柄，把文件内容复制到临时文件。

最后，无论是V10还是V20密钥，都会通过WriteFile写到那个命名管道里，传回给c\_x64.node。

## Chrome扩展侧载器：w.node 和 m

w.node（Windows版）和m（macOS版）都是Chrome扩展侧载器。它们内部的crate名字是ext\_sideloader。每个文件都在.rdata里嵌入了完整的RedExt Chrome扩展，格式是ZIP压缩包。

### Windows侧载器 (w.node)

这个文件有1.5MB大。它的导出名伪装成bz\_internal\_error，看起来像个bzip2错误处理器。

侧载过程分几步：

1. **侦察**

   ：运行whoami查询用户SID，读取LOCALAPPDATA、USERPROFILE环境变量，检查注册表里的Windows版本。
2. **发现Chrome**

   ：读取注册表项找到chrome.exe路径，验证resources.pak文件存在且大小足够。
3. **提取机器密钥**

   ：读取Chrome的resources.pak文件，提取用于计算Secure Preferences的HMAC值所需的机器密钥。找不到密钥或文件太小都会有明确错误提示。
4. **安装扩展**

   ：把嵌入的ZIP解压到%LOCALAPPDATA%\Google\Chrome\jucku\目录。枚举所有以“Default”开头的Chrome配置文件。
5. **篡改配置文件**

   ：在extensions.settings里写入预置的JSON注册块。关键标志有：location设为4（代表侧载，绕过Chrome应用商店验证），from\_webstore设为false，还有一大串权限申请。
6. **绕过完整性保护**

   ：计算Secure Preferences的super\_mac值，删除developer\_mode\_encrypted\_hash字段，强制启用开发者模式。
7. **杀死Chrome**

   ：用taskkill强制关闭Chrome及其子进程，好让配置文件变更生效。

一个确定的攻击痕迹就是Chrome安装目录下出现的`jucku`文件夹。

### macOS侧载器 (m)

macOS的逻辑类似，但适配了平台特性：在/Library/Application Support/Google/Chrome/目录下找配置文件；用pkill -9杀死Chrome；把扩展解压到每个配置文件的myextension目录下；通过system\_profiler获取硬件UUID作为机器密钥。

有意思的是，它还有个硬编码的128字符十六进制回退密钥，确保即使system\_profiler失败了侧载器也能工作。

这两个侧载器的开发环境也不一样。Windows二进制文件是在C:\Users\Administrator\下编译的，而macOS版本来自/Users/davidioasd/。

## 工作区窃取器：f\_ex86.node

这个文件内部名叫vscode\_env\_history.dll，编译于2025年9月24日——比Solana上最早的备忘录早了一天，是整个档案里最老的二进制文件。

它干三件事：

1. **访问数据库**

   ：打开VS Code和Cursor IDE的SQLite数据库，查询最近打开的项目路径列表。
2. **解析JSON**

   ：处理查询结果，提取出workspaceUri、folderUri这些字段，支持好几种版本的工作区格式。
3. **遍历目录**

   ：用walkdir这个库递归遍历每个发现的项目目录，跳过node\_modules、.idea等常见文件夹。结果会写到%TEMP%下的一个临时文件里。

文件里还有一个俄语错误字符串，这确认了它和GlassWorm其他部分是同一伙开发者。

这个工具的作用很明确：枚举受害者最近在VS Code和Cursor里打开过的所有项目目录。再结合JavaScript载荷里偷到的GitHub令牌和npm令牌，攻击者就能进行精准的供应链投毒——他们知道该攻击哪些仓库，并且有权限往里推送代码。

## 文件中的PE加载器：index\_ia32.node 和 index\_x64.node

这两个文件之前被误标为“密钥生成”二进制文件。反汇编后我们发现，它们是文件式的PE加载器。它们将data.dll从JavaScript缓冲区直接加载到内存执行，完全不会在磁盘上留下文件。

它们都用了memexec 0.2.0这个Rust库来实现内存执行，通过动态解析NtAllocateVirtualMemory和NtProtectVirtualMemory来完成PE的内存映射、导入表解析和入口点调用。

这种设计让data.dll在执行过程中没有文件系统上的实体，只能通过内存扫描或检测其行为（如创建命名管道、调用COM IElevator）来发现。

## 构建时间线与攻击链

把分析过的二进制文件的构建时间汇总起来看，顺序是很清楚的：

| 日期 | 二进制文件 | 备注 |
| --- | --- | --- |
| 2025-09-24 | f\_ex86.node | 最古老。比最早的Solana备忘录早一天 |
| 2025-11-19 | index\_x64.node | 实现文件式执行 |
| 2025-11-22 | index\_ia32.node | 同上，32位版本 |
| 2026-01-29 | data | DPAPI/应用绑定助手 |
| 2026-02-09 | Chrome扩展文件 | 扩展ZIP的日期 |
| 2026-02-10 | w.node | 紧接扩展一天后 |
| 2026-03-10 | JS载荷 | 版本2.27 |
| 2026-03-15 | c\_x64.node | 最新。活动重启前一天 |

看起来VS Code窃取器可能是一个独立的侦察工具，在攻击链完整搭建前就在用了。而浏览器凭据转储器则是最后才编译完成的。

### 完整的攻击链

修正了二进制文件的功能后，Wave 3的执行流程现在更清晰了：

1. 初始JavaScript载荷启动。
2. 下载Node.js，窃取npm和GitHub令牌。
3. 系统信息、云凭证、文档收集。
4. 如果检测到Ledger Live，则下载对应的钱包种子钓鱼工具。
5. 对每个扫描目录，解密并加载npm档案中的7个二进制文件：

1. f\_ex86.node：枚举VS Code/Cursor的工作区项目。
2. w.node 或 m：侧载恶意Chrome扩展，持久化访问。
3. c\_x64.node + data：注入浏览器进程，窃取DPAPI和应用绑定密钥，解密所有浏览器数据。

6. 将所有窃取的数据打包，发送到C2服务器。
7. 建立持久化（定时任务、注册表），通过日历C2和Solana钱包进行保活。

攻击成功后，侧载的Chrome扩展就成了攻击者的后门，能完成会话劫持、键盘记录、截屏等操作。

## 检测与应对

### 文件系统检测指标

* **Windows**

  ：检查是否存在 `%LOCALAPPDATA%\Google\Chrome\jucku\` 目录。
* **macOS**

  ：在Chrome配置目录下查找名为 `myextension` 的子目录。

此外，还可以检查PDB路径等构建环境痕迹，例如来自 `N:\work\chrome_current\DumpBrowserSecrets\...`。或者检查临时目录下是否存在vscode\_env\_history创建的痕迹。

### 供应链攻击循环

Wave 3载荷中，凭据窃取模块和工作区枚举模块结合，形成了一个完整的供应链传播闭环：

受害开发者的机器初始感染 → f\_ex86.node窃取其工作区列表，找出他贡献的核心项目 → TokenHandler等模块窃取其GitHub/npm等发布权限 → 攻击者利用这些权限向这些目标仓库注入含有恶意载荷的提交 → 依赖于这些仓库的其他开发者被感染 → 循环继续。

说实话，这种结合了精准侦察（工作区历史）和权限窃取（发布令牌）的攻击模式，在针对开发者社区的APT中越来越常见，杀伤力很大。只扫描恶意npm包可能不够，企业还得关注内部代码库的异常提交和权限管理。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8eMUeOw7iaF6r78Oo4vichG5ARUN5BVQVibCwGCbEQ7DVUDLdvIgPTqian6D6rojmzfzxXIwE5pJtjvuTDHqAYC1XQ/0?wx_fmt=png)

夯磅棱

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8eMUeOw7iaF6r78Oo4vichG5ARUN5BVQVibCwGCbEQ7DVUDLdvIgPTqian6D6rojmzfzxXIwE5pJtjvuTDHqAYC1XQ/0?wx_fmt=png)

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