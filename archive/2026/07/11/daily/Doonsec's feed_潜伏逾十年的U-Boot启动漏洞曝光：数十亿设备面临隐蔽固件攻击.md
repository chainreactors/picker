---
title: 潜伏逾十年的U-Boot启动漏洞曝光：数十亿设备面临隐蔽固件攻击
url: https://mp.weixin.qq.com/s/Bi8JpkH7bBdU80Du5_Utkg
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:10:42.445778
---

# 潜伏逾十年的U-Boot启动漏洞曝光：数十亿设备面临隐蔽固件攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d2NyicKB5lccuwEABiaW4vXsKnxwuxriaYeAOPm6lRXgSwnpjVgQOhOYBCRQQ65GPoKLzkbSXgzicICkCff3MaryOBaqKicMsibU2lps/0?wx_fmt=jpeg)

# 潜伏逾十年的U-Boot启动漏洞曝光：数十亿设备面临隐蔽固件攻击

原创

网空闲话
网空闲话

网空闲话plus

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

全球最广泛使用的开源引导加载程序U-Boot，近日被曝存在六个严重漏洞，可能使从家用路由器、智能摄像头到数据中心服务器基板管理控制器在内的海量嵌入式设备，面临拒绝服务崩溃乃至启动阶段任意代码执行的严重威胁。2026年7月9日，固件安全公司Binarly研究团队在其官方博客发布题为《无法启动：破坏U-Boot的FIT签名验证》的长篇技术报告。网安媒体BleepingComputer、The Hacker News与Cybersecurity News亦于7月10日相继报道，引发行业对固件供应链安全的再度高度警觉。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/lQ1jXOMq3d1AhibzXf3nxcJ5MhfFPVnVy4WlPeJUX2szNq2aS0vjlQqfB6dXicNve3Iic3pE1GH37gMZ210ZQABPRVVicwnib3cjFOfbpKgG1qGk/640?wx_fmt=gif&from=appmsg)

**研究背景：瞄准最关键的启动防线**

U-Boot是系统上电后最早执行的软件组件之一，负责初始化CPU、内存和关键外设，并将控制权移交至下一启动阶段。因其先于操作系统运行的特殊地位，该阶段的任何安全缺陷都可能危及随后加载和执行的整个软件栈。Binarly研究团队在博客中阐述，其之所以将研究聚焦于U-Boot的Verified Boot机制、尤其是FIT签名验证逻辑，正是因为该环节一旦失守，已验证启动或硬件可信根的概念便形同虚设。

FIT是U-Boot用于打包启动镜像的标准格式，构建于扁平设备树格式之上，单个FIT镜像可捆绑内核、设备树、ramdisk及固件blob等多个组件，同时嵌入这些组件的哈希值与签名。FIT签名验证即在镜像被执行前检查其是否可信的关键步骤。值得注意的是，该逻辑此前已多次遭受安全挑战，相关CVE包括CVE-2020-10648、CVE-2021-27097、CVE-2021-27138以及近期披露的CVE-2026-33243。Binarly基于2026年4月6日发布的最新稳定版U-Boot v2026.04展开审计，最终发现六个此前未知的漏洞：两个可导致任意代码执行，四个可导致拒绝服务。所有问题均在处理不可信FIT镜像时、签名验证完成之前即被触发。

**六个漏洞详解**

为清晰呈现各漏洞的核心特征，下表汇总了六个漏洞的编号、类型、触发位置、成因与影响：

| 漏洞编号 | 类型 | 触发函数 | 成因摘要 | 潜在影响 |
| --- | --- | --- | --- | --- |
| BRLY-2026-037 | 代码执行 | `fdt_find_regions` | `fdt_get_name`返回NULL未检查；处理根节点时空指针解引用导致DoS；处理子节点时若零地址映射则`strcpy`可致栈缓冲区溢出 | DoS / 任意代码执行 |
| BRLY-2026-038 | 代码执行 | `fdt_find_regions` | `fdt_get_name`失败时`len`被写入负错误码（-11），指针后退操作可覆盖返回地址 | 任意代码执行 |
| BRLY-2026-039 | 拒绝服务 | `fit_config_check_sig` | `hashed-strings`属性第二字大小值未校验，攻击者可设为0xFFFFFFFF致哈希例程越界读取 | DoS（崩溃） |
| BRLY-2026-040 | 拒绝服务 | `fdt_find_regions` | 旧版FDT（版本<0x10）下`fdt_get_property_by_offset`返回NULL，调用方直接解引用`prop->nameoff` | DoS（崩溃） |
| BRLY-2026-041 | 拒绝服务 | `fit_image_get_data` | 外部数据的`data-position`/`data-offset`/`data-size`完全由攻击者控制且未经边界校验 | DoS（崩溃） |
| BRLY-2026-042 | 拒绝服务 | `fdt_check_no_at` | 递归遍历FIT节点树时仅靠无子节点终止，深度嵌套镜像可耗尽栈空间（每层仅需12字节镜像/消耗≥16字节栈） | DoS（栈耗尽） |

其中两个代码执行漏洞实为同一根源问题的不同利用路径。BRLY-2026-037与BRLY-2026-038均源于`fdt_find_regions`函数在调用`fdt_get_name`后未检查返回值。当处理FDT版本低于0x10且节点名不含“/”字符的畸形镜像时，`fdt_get_name`会返回空指针及负的错误码。BRLY-2026-037沿空指针执行`strcpy`内存复制——在零地址已映射的嵌入式设备环境中，可导致基于栈的缓冲区溢出；BRLY-2026-038则将负长度值传入指针运算，使`end`指针每次反向移动10字节（错误码-11加上`*end++ = '/'`的补偿），逐步逼近并最终覆盖`fdt_find_regions`的返回地址。Binarly使用`qemu_arm_defconfig`构建配置成功验证了代码执行的可达性，在U-Boot执行期间向控制台打印出[BRLY]消息。

**影响范围与攻击面：潜伏逾十年的代码，覆盖超50个版本**

Binarly在博客中明确指出，大多数受影响代码自U-Boot v2013.07版本起就已存在，这意味着漏洞可能影响超过50个稳定发行版及众多下游厂商分支，“对行业影响深远”。U-Boot的运行平台极为广泛，BleepingComputer将其归纳为“企业服务器的基板管理控制器、网络设备、工业系统、物联网设备及其他设备”。The Hacker News则进一步指出，U-Boot与Linux内核、barebox等项目共享libfdt扁平设备树库，产生两个最严重漏洞的辅助函数`fdt_get_name`即来源于此——同样的未检查返回错误可能出现在任何使用该代码的地方，暗示影响范围可能溢出U-Boot生态本身。

关于攻击路径，多家媒体均引述Binarly的说明：尽管利用这些漏洞通常被认为需要物理接触设备以重新刷写SPI闪存，但实际情况往往并非如此。Binarly此前对Supermicro BMC的研究已证明，拥有BMC管理界面远程访问权限的攻击者，可利用设备自身的合法固件更新机制刷入恶意镜像，无需物理接触硬件。The Hacker News与Cybersecurity News均强调，恶意镜像一旦在签名验证前即触发漏洞，便可完全绕过信任检查。

**各方警示**

BleepingComputer在报道中总结道，一旦代码执行漏洞被成功利用，攻击者可在操作系统加载前执行恶意代码，这可能用于“禁用固件安全功能、修改启动流程、安装持久化固件恶意软件”。由于恶意代码在操作系统启动前即已运行，将“极难被检测”。对于拒绝服务漏洞，最坏情况下需物理重新刷写SPI闪存方可恢复设备。

**披露与修复时间线**

漏洞的披露与修复过程可按时间序列梳理如下：

| 时间节点 | 事件 |
| --- | --- |
| 2013年7月 | 受影响代码随U-Boot v2013.07版本引入，此后长期存在 |
| 2026年4月6日 | U-Boot v2026.04发布，Binarly基于此版本展开审计 |
| 2026年4月-6月 | Binarly发现六个漏洞并制备补丁；初始报告因沟通误解未被顺利接收，团队随后与维护者协作推进 |
| 2026年6月 | 全部六个补丁经多轮审查后合入U-Boot的master分支 |
| 2026年7月4日（约） | U-Boot v2026.07发布，但因代码于4月冻结，未包含本次修复 |
| 2026年7月9日 | Binarly官方博客发布详细技术报告，公开漏洞详情及PoC |
| 2026年7月10日 | BleepingComputer、The Hacker News、Cybersecurity News等相继报道 |
| 2026年10月（预期） | U-Boot v2026.10预计发布，届时将正式包含修复 |

Binarly在博客中特别致谢了U-Boot维护团队成员Simon Glass和Tom Rini在披露过程中的协作。但BleepingComputer与The Hacker News均冷静指出，修复分发才是真正的挑战：U-Boot集成于各硬件制造商的固件中，修复程序必须经厂商纳入固件更新后方可送达终端用户；已停止更新支持的老旧设备可能永远无法获得补丁。The Hacker News以2020年的BootHole漏洞为鉴提醒业界：当引导加载程序漏洞击穿整个生态系统的安全启动防线时，“编写补丁只是第一步，真正耗时的是将补丁部署到运行着不同U-Boot版本的数百万台设备上”。

**结语**

Binarly在博客结尾宣告，其透明性平台已扩展对U-Boot引导加载程序的分析能力，可规模化检测此类固件层面的隐蔽问题。这一系列漏洞的发现，再度将固件安全推向聚光灯下：在攻击者日益将目光投向操作系统之下、启动阶段之前的趋势中，对引导加载程序等奠基性组件的持续安全审计和严格的输入校验，已不仅是技术必要，更是维护整个平台完整性的基础防线。

参考文献

[1] Ivanov, A. (2026, July 9). *Unfit to Boot: Breaking U-Boot’s FIT Signature Verification*. Binarly. https://www.binarly.io/blog/unfit-to-boot-breaking-u-boots-fit-signature-verification

[2] Abrams, L. (2026, July 10). *New U-Boot flaws could enable stealthy firmware attacks*. BleepingComputer. https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/

[3] Khandelwal, S. (2026, July 10). *Six New U-Boot Flaws Could Let Malicious Images Crash or Run Malicious Code at Boot*. The Hacker News. https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html

[4] Abinaya. (2026, July 10). *U-Boot FIT Signature Verification Flaws Could Lead to Code Execution and DoS Attacks*. Cybersecurity News. https://cybersecuritynews.com/u-boot-fit-signature-verification/

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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