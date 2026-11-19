---
title: 开箱即用的Windows应急响应神器，还能让AI帮你自动排查
url: https://mp.weixin.qq.com/s/lRB0MOcdGLtaj3pG1RuJQg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:43:43.104948
---

# 开箱即用的Windows应急响应神器，还能让AI帮你自动排查

# 开箱即用的Windows应急响应神器，还能让AI帮你自动排查

原创

lmhsw1
lmhsw1

Hack分享吧

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

| Ima知识库名称 | 加入条件 |
| --- | --- |
| 潇湘信安协同知识库（更新~ing!） | 免费加入 |
| 潇湘信安学习资料库（更新~ing!） | ≥3年粉丝 |
| 潇湘信安内部知识库（更新~ing!） | 星球成员 |

现在只对常读和星标公众号才展示大图推送，建议大家把“Hack分享吧”设为星标，否则可能看不到了！

# 一、工具简介

在应急响应现场，时间就是生命线。每多花一分钟手动排查，攻击者就可能多完成一次横向移动或数据窃取。**SWAY\_WIN\_IR\_TOOLS** 正是为了打破这一困局而生——它是一款综合全面的 Windows 应急响应工具，凝结了作者多年一线实战经验，并融合了业内顶尖的应急响应思路，让你在图形界面中就能逐项完成浏览器、进程、持久化、日志、文件和网络等全维度痕迹排查，快速定位可疑程序、账户、启动项和外联行为。

更令人眼前一亮的是，工具同时提供 **MCP 接口**。接入后，AI Agent 可以按照排查流程自动调用各项能力收集证据、完成分析，并给出处置建议，由现场工程师确认后执行。最关键的是——**MCP 服务的所有工具都是只读的**，从根本上排除了模型误调用增删改操作的风险，让 AI 辅助应急响应既高效又安全。

---

# **二、支持的操作系统**

工具仅支持 **64 位 Windows 系统**，具体包括：

* Windows 10、Windows 11
* Windows Server 2012 R2 及以上的服务器系统

> ⚠️ 32 位 Windows 和 ARM64 Windows 不在支持范围内。部分排查功能（如安全日志读取、进程内存分析等）需要**管理员权限**才能获取完整数据，建议始终以管理员身份运行。

---

# **三、核心排查功能**

## **3.1 浏览器排查**

浏览器往往是攻击者进入内网的第一道门——钓鱼下载、恶意插件、浏览器落地样本，都可以在这里找到蛛丝马迹。

**插件视图**下，可以查看本机 Chrome 与 Edge 的全部插件记录，包括插件来源、权限、安装时间等关键信息，帮助你快速发现恶意插件和从浏览器侧落地的样本。更贴心的是，工具支持**右键隔离并删除**：点击后会将该插件从浏览器中移除，并把相关文件保存在隔离证据目录 `./evidence/browser_extensions` 下，既保留了取证证据，又清除了威胁，一举两得。![浏览器插件排查](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kBX45DgB9ZR6tDJMPg9DVhWLA8uuVia9Ek2jstMNOwOIZ9V7Uu5zXiaZ9XbfAGj7Fj150396q2MHE6WX1XHs7FgxyRKelDlUT6k4/640?wx_fmt=png&from=appmsg)

浏览器插件排查

**下载记录视图**则会自动扫描并解析系统内已安装的 Chrome 和 Edge 浏览器数据库，快速提取并展示用户的文件下载记录——包括文件名、保存路径、来源 URL 和下载时间等详细信息。在溯源攻击者恶意载荷投递路径时，这个功能简直是神器。![浏览器下载记录](https://mmbiz.qpic.cn/mmbiz_jpg/zqnzfCSS1kA56w92vWFAtdOCkib7h42bLuq4QlKZZKJy8ic40e5hWWDdRVC5aGmWqdy0TTZYx6ia1WwO7Ad7lOWjfMdHv6Q9TUeczWpKK6wdCM/640?wx_fmt=jpeg&from=appmsg)

浏览器下载记录

## **3.2 进程分析**

进程分析是应急响应的核心环节。工具会列出所有进程的名称、PID、父进程 ID、用户、启动时间、是否签名、公司、文件路径等关键信息。点击单个进程还可查看更多详情。

右键菜单更是功能强大：

* 计算进程所属文件的 **SHA256 和 MD5 哈希值**
* 查看进程加载的 **所有 DLL 模块**
* 查看 **进程树信息**
* 进行 **内存取证**（Mini Dump 或 Full Dump）
* 一键查询 **微步、VT 沙箱**，快速判断文件是否为恶意

![进程分析界面](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kBlDX9YsJQRsFAVibwVDKNE8oOZItwbJ6LiaJpflibLGqQ3x9Uz6RJz4LGC9qibRaFu136DS9hOQ7ZMRia6ziblZjBNCw3kulstjMvEs/640?wx_fmt=png&from=appmsg)

进程分析界面

说到 DLL 模块，这可是排查"白进程 + 黑 DLL"场景的关键阵地。选择某个进程右键查看 DLL 模块后，你需要重点关注那些**签名异常和未签名的 DLL**——黑 DLL 往往是未签名或者签名异常的。工具同样支持对加载的 DLL 进行微步、VT 和联网查询，全方位辅助判断。![DLL模块查看](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kA4kt3icp3uNe1giaRjANRhxQwDKmOusP08roDuF90zWfcc7tcr5cLc52MBk1mRcanDUKBstaD1MsbkvcLyaf04Gr1oSbX5QtUno/640?wx_fmt=png&from=appmsg)

DLL模块查看

## **3.3 威胁检索**

手里有 IOC（Indicators of Compromise）？威胁检索功能可以让你快速确认主机是否已被植入对应程序。支持按**进程名、路径、命令行、模块、文件哈希或内存特征**在本机进程中检索，哈希支持 MD5、SHA1 和 SHA256。

比如，在真实攻防场景中，如果态势感知设备告警有恶意外联 IP，你可以直接输入该 IP 进行内存搜索，瞬间定位恶意进程。

> 💡 内存限制默认为 256MB：如果一个进程占用 1GB 内存，工具只会扫描前 256MB，没命中就跳过该进程——这在保证覆盖面的同时兼顾了扫描效率。

![威胁检索](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kBL9LWaIVeu2F5o98EtDoa0fcmKNSjPW7VnKianXQZf5CIt2yEK4A7Ht2WyqIcljDpV7KswoB9Ju2Zahuer6NVQeuuiaBsxHUkN4/640?wx_fmt=png&from=appmsg)

威胁检索

## **3.4 Beacon 扫描**

Cobalt Strike 是红队和 APT 组织最常用的 C2 框架之一，Beacon 植入的检测一直是应急响应的重点和难点。

Beacon 扫描功能会**扫描进程堆内存，查找 Cobalt Strike Beacon 的配置**。命中后可以查看解析出的通信配置（如 C2 地址、通信间隔、密钥等），直接确认主机上是否存在 Beacon 植入。只需点击"扫描"，工具就会对所有进程进行地毯式排查，默认配置的 CS 木马进程基本无所遁形。![Beacon扫描](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kA4CZwb9WLsK3XDkibfRASeY4j2zf5n4lptAr7aiaAxXgQvsJzI8DwoJFkyiafXTicJWCsz7skWXwl4t1MGCfysEb9Zjvibb4vMBvG4/640?wx_fmt=png&from=appmsg)

Beacon扫描

## **3.5 进程扫描**

有些恶意代码只存在于内存中，磁盘上根本找不到完整文件——这就是所谓的"无文件攻击"。进程扫描功能使用 **YARA 规则**扫描全部进程的内存，返回命中的规则、威胁名称、内存地址和严重性，让内存中的恶意代码无处藏身。![进程YARA扫描](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kAFMM3c6L1h7Abc5F92AlRbu3kwhxI8spyEsZtluetIY3Keyccx190P9T3XQTibNrOgYpPAALEdTWwoCnA7QBZEbRbPkgUPooSE/640?wx_fmt=png&from=appmsg)

进程YARA扫描

## **3.6 用户排查**

攻击者入侵后，往往会新建账户或隐藏账户来维持访问。用户排查功能会列出本机账户的**启用、锁定、管理员和当前登录状态**，并自动标出**隐藏账户和 RID 劫持迹象**，帮助你第一时间发现攻击者留下的后门账户。![用户排查](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kAVU9PMLlX0oic1qeQbtFlvub5BTNQyfgZZQiclsW8sry2LicBXSw0sXXwLM3yJ87iacQqzarzU53A9ym4vC2ybgaaYeEP05qVleBs/640?wx_fmt=png&from=appmsg)

用户排查

## **3.7 计划任务**

计划任务是最常见的持久化手段之一。相比网上其他应急响应工具，这个模块的亮点在于会显示**计划任务的创建时间和是否签名**。

它的原理很巧妙：创建计划任务时会在 `C:\Windows\System32\Tasks\` 目录下生成文件，工具就利用这个文件的创建时间作为计划任务的创建时间。而签名则是根据计划任务指定运行的载荷文件来判断的——载荷文件有签名则认为有签名，没有签名就是无签名。

此外，还可以查看计划任务的程序、参数、运行身份、触发器、状态和签名，并对计划任务实际运行的程序做 **YARA 磁盘扫描**，全方位发现通过计划任务保持驻留或定时执行的恶意程序。![计划任务排查](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zqnzfCSS1kBSeX6oGqaibib0iad5Tlibuoibw0s1Qurk0SJRB6L7KicJ6LYD5acCPNxsdvV4ystdV5nAUgNPqQ3buCwaL5mRB7CknYMKkGLnWW8Gk/640?wx_fmt=jpeg&from=appmsg)

计划任务排查

## **3.8 服务排查**

服务排查模块会列出服务的**创建时间、启动类型、状态、程序路径和签名**，并对服务程序或参数中的载荷做 YARA 扫描，用于发现伪装成服务的恶意程序。

同样的逻辑，自启动服务是否有签名，看的是自启动服务指定文件路径下的所属文件是否有签名。无签名的服务项往往更可疑，优先排查准没错。![服务排查](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zqnzfCSS1kAWZWN1rCZJGibtM6TFr5cfoUUUfib1e0nGaKdlE6S9ia2icxRfLfvcNQN69AXu2m2uFp3ZFVgCIUQ0PbOCUxm41jxTOxSsqldr7AM/640?wx_fmt=jpeg&from=appmsg)

服务排查

## **3.9 驱动排查**

内核级威胁越来越常见，驱动排查也成了应急响应的必查项。工具会列出**内核驱动、文件系统驱动和已加载模块**，核对签名、路径和加载状态，并对驱动文件做 YARA 扫描，帮助你发现未签名或异常路径上的可疑驱动。![驱动排查](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kDBwhS4kkia1icj43S3LD2YcVNGDpedic8rNfnQxAtlM8NYKuTtmknKicxISRVWdZKE3edVMHupZwhxWkh04wA4WGsQaYS0ibpB7Z64/640?wx_fmt=png&from=appmsg)

驱动排查

## **3.10 自启动排查**

攻击者的持久化手法五花八门，自启动排查就是把网上大部分能持久化的地方统一扫一遍。它覆盖了：

* 登录运行（Run / RunOnce）
* 启动文件夹
* Winlogon
* 映像劫持（IFEO）
* AppInit
* WMI 订阅
* BITS 任务
* COM 劫持
* 等等常见持久化点位

每项都会核对程序、用户、签名和 YARA 扫描结果。计划任务和服务因为功能更复杂，单独在对应模块中做了更详细的排查。![自启动排查](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kAwcFDdT3fXxdFaZH81icfPrvh2R0P2zphPXrVDzicrhb7xB9IMHP0NbAVmGNbRarGBVibvSolAPCic7m8vFRe7YFFJDBSb1oDomKI/640?wx_fmt=png&from=appmsg)

自启动排查

## **3.11 文件排查**

文件排查模块会扫描**下载目录、桌面、临时目录和 C 盘非系统目录**中的可执行文件、脚本、压缩包与快捷方式，查看创建时间、签名、来源区域和异常标记，并可对选中文件做 YARA 扫描。

这个功能特别适合发现**新落地的样本、双扩展名文件和隐藏文件**——攻击者往往会把木马放在这些容易被忽略的位置。![文件排查](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kA6UXSzgC7HujqhG5w08QUuVwI9WnsXBZqKdGW4D2efrQXA275XMsS3iaJ7H8zbGX97byewT9Xf2EqBxFib67WicbxsicprcEaKMbk/640?wx_fmt=png&from=appmsg)

文件排查

## **3.12 事件日志**

Windows 事件日志是溯源的金矿，但海量日志往往让人无从下手。事件日志模块按照应急响应的实际需求，将日志按类型分类提取：

* 登录认证
* 远程桌面
* 账户变更
* 权限组
* 共享访问
* 持久化
* 进程创建
* PowerShell
* 防御规避

可以快速还原登录来源、账户改动、服务或任务安装，以及日志和防护被关闭的痕迹。![事件日志](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kCibiaUpKQRSnlO26uPwSNprHkfVnTcvmwlibjfibpd6JLFwvPeuhGXuXMMoL1fu2xNB4mAibH8TjTKibkRHzrgjB8MQ9sDYfYHUQ1icA/640?wx_fmt=png&from=appmsg)

事件日志

## **3.13 活动痕迹**

有些程序执行完就退出了，当前进程列表里根本看不到——这时候就需要历史活动痕迹来补充。

活动痕迹模块从多个来源汇总历史操作记录：

* **系统事件**
* **Prefetch**（预读取）
* **UserAssist**（用户 Assist 记录）
* **最近访问**
* **卸载记录**
* **Amcache**
* **PowerShell 控制台历史**

可以查看开机、登录、程序执行、文档访问和软件安装等活动，完美补充当前进程中已经看不到的历史执行记录。![活动痕迹](https://mmbiz.qpic.cn/mmbiz_jpg/zqnzfCSS1kDXgCGUicrx7N6NSzJyYPNy3j6q3XjOHEqfx1omiaaVqaJ9K1z1FMial16TxWVMrRERibrq3licTCS8AARMoBFITUnyC1GGNicCEyZq4/640?wx_fmt=jpeg&from=appmsg)

活动痕迹

## **3.14 网络连接**

网络连接排查有两种视图，各有侧重。

**当前连接视图**可以查看各个进程的 TCP、UDP 连接情况，并自动筛选区分**外联外网、内网和监听端口**，帮你快速确认哪个进程在连接恶意 IP。![网络连接-当前连接](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kBG00nlQw9ALPVnNO9VxbhCWWsu43ehzK5mcjXpB78U7XoHiaBzYYhne4wMEmW5p0SJiapIUJwjpYykd9KP2teVRP3kh7WK6HpsU/640?wx_fmt=png&from=appmsg)

网络连接-当前连接

**外联记录视图**则更强大——点击"开始监听"后，可以实时记录哪个进程外联了哪些 IP 地址。如果有态势感知设备告警了木马外联的恶意 IP，配合这个功能可以秒级定位恶意进程。

更有意思的是第四列的**间隔秒数**——它记录了上一次外联该 IP 和本次外联的间隔时间。熟悉木马通信的朋友都知道，木马进程大多存在定时心跳机制，通过间隔时间就能初步判断进程是否存在心跳通信规律，辅助识别 C2 行为。![网络连接-外联记录](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kDE1v9xgb8glqKje0RUxaOc8RmZHKLp2Db7V6qcoLAmxYwwLq0er5u1VmSULEeuOKL6Mia9YoQ25sHmz0MNJ35XD0icp8WZysKko/640?wx_fmt=png&from=appmsg)

网络连接-外联记录

## **3.15 域名解析监听**

域名解析监听模块的设计非常实用——点击"开始监听"后，工具会记录一段时间内本机哪些进程对哪些域名发起了解析请求。如果已知恶意钓鱼域名，可以通过这个功能快速定位是哪个进程在解析它，顺藤摸瓜找到恶意程序。![域名解析监听](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kCg7CMHcme5rkATibrlGIB5t0fUib3jq0lBIG5PXOgdqKl0NnO2T3ic2YmcicnguLjootXCdtHak4mVo9OV9kpPfCmJicWLBfmLticO8/640?wx_fmt=png&from=appmsg)

域名解析监听

---

# **四、MCP AI 自动化功能**

## **4.1 MCP 是什么？为什么它是核心亮点？**

如果说前面的功能已经足够强大，那 MCP 功能就是这款工具真正的"杀手锏"。

**MCP（Model Context Protocol）** 是一种让 AI Agent 能够调用外部工具的协议。把 SWAY IR Tools 在受害机器上作为 MCP 服务启动后，AI Agent 就可以通过 MCP 服务作为媒介，自动调用上述所有排查功能来分析受害机器。

但这里有...