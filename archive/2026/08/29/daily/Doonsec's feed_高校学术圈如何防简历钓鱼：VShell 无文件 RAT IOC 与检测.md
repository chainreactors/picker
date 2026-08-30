---
title: 高校学术圈如何防简历钓鱼：VShell 无文件 RAT IOC 与检测
url: https://mp.weixin.qq.com/s/C9l-oEhkw9LFV-vXApdjiQ
source: Doonsec's feed
date: 2026-08-29
fetch_date: 2026-08-30T07:41:11.802242
---

# 高校学术圈如何防简历钓鱼：VShell 无文件 RAT IOC 与检测

# 高校学术圈如何防简历钓鱼：VShell 无文件 RAT IOC 与检测

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

前言

2026 年 8 月 27 日，安全研究员 Himanshu Anand 发了一篇威胁情报，讲的是一套以伪造学术简历为饵的链式攻击：一个伪装成简历的 ZIP/EXE，被双击后后台依次加载 Go loader、SNOWLIGHT、VShell RAT，全程无文件落地，取交互式远程控制。本文基于其 ANY.RUN 沙箱捕获与静态解码复盘技术事实与影响范围。先给结论：这是定向鱼叉，受害者语境中置信指向大陆学术圈，攻击者归属未知，无持久化与泄密实锤，不是大规模蠕虫，也远未到 APT 定案。

一、攻击事实

初始向量是一个 ZIP 压缩包，内部放了一个与压缩包同名的 .exe。Windows 默认隐藏扩展名，加上图标仿成文档，收件人双击"简历"实际跑的是 PE。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0HdnelxUcKRp3mibGiaDlu4elZ0VczTOvTfdqlW7MXME3B6SbkruKYibFU2Crfj6fNaDsmC68eibkoZ3ufsXU1dibCF8mIU9SvWnXxE/640?wx_fmt=jpeg&from=appmsg)

运行后它从远程拉一份真实 DOCX 诱饵，存到 C:\Windows\Temp\ 并调用 Word 打开，让受害者以为文件正常，后台同时跑 staged 加载。

完整载荷链是：Fake Resume EXE 触发 Stage1 Go loader，Stage1 拉起 Stage2 SNOWLIGHT shellcode，Stage2 再接收并跳进 Stage3 VShell RAT，全程 fileless。

VShell 是什么需要说清。它是公开可得的 Go 语言跨平台远程访问木马框架，SNOWLIGHT 是其默认 stager。本例解码出来是 32 位 Go PE，.data 段高熵加密、符号混淆。公开文档与控制台记录显示，它具备交互式终端与任意命令执行、文件浏览上传下载、屏幕截图与实时监控、主机与网络侦察、反向代理隧道，以及 TCP/WebSocket/KCP 等多传输协议。

把 VShell 当作"某个神秘 APT 专属武器"是误读，它是商品化/已泄露的货架 RAT，任何拿到面板的 operator 都能生成相同 stager。

二、攻击链拆解

2.1 Stage1：Go loader 的反沙箱与配置

样本是 32 位 Go 1.22.0 Windows 二进制，带一枚无效的金山签名（HashMismatch）。它先做反沙箱：检查路径含 C:\Users\Administrator\Desktop 且文件名含 2016 就退出，针对微步类沙箱；CPU 逻辑核数小于 4 也退出；还用 kernel32!Beep(30000Hz,10s) 测算真实时间，加速型沙箱会被识破退出。

配置是加密的，流程是 Base32hex → AES-CBC（密钥 YtWzxwZimsZoeMen） → 按位 NOT → Base64，解出两个 URL 和落盘路径。内存执行靠 Activeds.dll!AllocADsMem 分配可执行内存，起线程跑 shellcode。

反沙箱 + 多层编码是商品化 loader 的标配，静态直接看字符串基本无功，必须解码配置或沙箱真跑。

2.2 Stage2：SNOWLIGHT 跨界到 Windows

从 :50813/EasyConnectUpdata\_Log.txt 下载约 6KB 响应，解码成 1454 字节 x86 shellcode。它建 %TEMP%\log\_de.log 作为 kill-switch，文件存在就退出；连接 38.207.178[.]192:50812；先发 40 字节架构/检查包（开头 w32 加端口加 IP）；再以 0x99 循环异或接收约 4.65MB 后跳转执行。全程无服务器认证、无签名校验，是 VShell 面板生成的通用 stager。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0EyNON1B9tLC5WcunGXkSF1UgEVz4Q7CHgoI6Vxonl5bPBk0gxd3lLLAicZ6CfofZyhZF9gFwkkjaFe3DSC1GqsbGRsOLJ9B6SQ/640?wx_fmt=png&from=appmsg)

kill-switch 与无认证设计说明它是通用投递件，不绑定特定 operator，这也是为何多团伙能共用同一套。

2.3 Stage3：VShell 的 C2 与行为

C2 用 AES-256-GCM，密钥是 MD5(salt) 的十六进制串，帧结构是 4 字节小端长度 + 12 字节 nonce + 密文 + 16 字节 tag。沙箱里观察到注册、MD5 挑战、conf 通道与心跳等约 198 帧健康流量，但没有看到人工下发的指令。

只看到心跳没看到操作指令，说明捕获的是"已上线未行动"的窗口，不能据此推断攻击目的已达成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0GtzAHfe5p8DA061GrfXgcaqMjj1cpvdrrpVV0BqgPK92ChRQrl8kGicSO3nIAweibrc4xRWP8V7EyQxVyvPKgVEpb6pEN6rlibTk/640?wx_fmt=png&from=appmsg)

三、影响范围核实

本节是全文重心，逐项给证据，避免被标题带偏成 APT 定案或全网恐慌。

3.1 直接受影响

直接中招的是打开恶意 ZIP 内伪装 EXE 的 Windows 用户。风险最高的一类，是通过学术邮箱收到这份"简历附件"的高校教师或课题组负责人。诱饵文档用简体中文、WPS 区域码 2052，满是"应届毕业生""个人简历""课题组""贵课题组"等大陆学术用语，研究意向聚焦 AI 电网故障诊断、智能电气系统、新能源变流器控制，明显是套磁导师的模板。

3.2 潜在扩散

若单台工作站失陷，VShell 的反向代理隧道可以深入内网，做横向移动与凭据收集，波及整个研究室或院校网络。这是潜在面，取决于失陷主机的网络位置与权限。

3.3 非断言项

作者明确区分了三件事。第一，北京理工大学仅为诱饵声称的"申请人母校"，不代表该校是受害者机构。第二，没有数据证明国防研究项目遭定向攻击。第三，没有证据显示已发生数据泄密。把"用了 BIT 名义"直接读成"打了中国国防"是过度推断。

3.4 无文件与持久化

本例全程 fileless，仅诱饵 DOCX 与 kill-switch 标记文件落盘。沙箱里 Windows Defender 阻断了重建的 PE，没有注册表、服务层面的持久化实锤。

3.5 地域与行业语境

综合 lure 语言、WPS 简中环境、"国防七子"名义的权威感包装，以及研究意向集中在电力系统与可再生能源控制，中置信结论指向大陆学术科研网络。这是受害者画像，不是攻击者画像。

四、检测与狩猎（我带你看怎么查）

我们从网络层先拦。已知的 C2 基础设施是 38.207.178[.]192，涉及 50812（SNOWLIGHT/VShell）、50813（HTTP 暂存与诱饵）、40010（历史 VShell 中置信）三个端口，边界与出向规则直接阻断。SNOWLIGHT 那条 40 字节检查包带 w32 标签，VShell 帧带 12 字节 nonce，都是可写告警的特征。

终端上我们盯几个点。搜 %TEMP%\log\_de.log 这个 kill-switch 标记；看"简历名 EXE 启动 Word 又起 cmd"的父子进程关系；抓 AllocADsMem → VirtualProtect → CreateThread 这条内存执行链；注意先收大段 TCP 再分配数十 MB 可执行内存的行为；还有带无效金山证书的 Go 二进制、出向流量里的 w32/w64/... 标签。

邮件网关侧，对 ZIP 内 EXE、仿文档文件名、以及借"国防七子"等名义的套磁附件提高审查等级，必要时默认拦截可执行附件。

五、归因与防御视角

归因上作者没有给出定论，最贴切的标签是"使用面向大陆学术 lure、商品化 SNOWLIGHT+VShell 生态的未知 actor"。SNOWLIGHT 历史上由 Mandiant 命名并与 UNC5174 相关，但到 2026 年 VShell 面板已经商品化甚至泄露，Earth Lamia、UAT-8302、UNC6586 都用过同一套却无本例 IOC 重合。工具共性不能当成同一团伙证据。

防御要三道防线一起上。其一，学术邮箱严格过滤 ZIP/EXE，默认显示扩展名、禁用双击来源不明 EXE。其二，终端 EDR 覆盖内存执行与无文件行为，不止看落盘 PE。其三，网络阻断已知 C2、做零信任分段限制横向。人员培训也关键，让师生识别"仿文档 EXE"和套磁钓鱼。

商品化 RAT 加本土化社工是低成本高回报组合，治本在"人加网关加 EDR"，而不是等归因定案再动。

结束语

本文核实的结论很明确：这是以伪造简历为饵、无文件投递 VShell RAT 的定向鱼叉，受害者语境中置信指向大陆学术圈，攻击者归属未知，无持久化与泄密实锤。高校与科研单位不必全网恐慌，应按 3.1 到 3.3 把资产自查落在学术邮箱网关、终端 EDR 与网络 IOC 三处。VShell/SNOWLIGHT 生态商品化让"无文件 RAT 加本土化社工"成为常态，唯有把社工防线与无文件检测建起来，才能从根上收口。

```
Original archive SHA-256
c25d4412f7f93e7de5b2aaf41747175d94cffd983ca20efbd0efcdd718b58c4d

Go loader SHA-256
81c51138d5527ca7dcc258171eb36659c479f66c86a8947b6340d040b3860a30

Go loader MD5
a7cc7e3cdd2f0f9210044911a483fa5d

Encrypted HTTP response SHA-256
f6d4da5afc89bf9e536a9002c4d256c696df2389d77279f4c5daf6979557e74e

SNOWLIGHT shellcode SHA-256
0524619d2471d77aba4b7993f5ffbaa4b8be6d2c0d91e63a02943851dc4b6404

XOR-encoded VShell stream SHA-256
ed2eaa6ef3eda95383b6efc35b88acbca742ad7bd118931f74727a3139ff7e97

Decoded VShell SHA-256
c666ac4f1a1b8df7ccfe8b19705279acd8b7eb7a4d0b3802bb3465064883ab25

DOCX decoy SHA-256
de3f56d0d5b71f2a1a1905f0b01b84fbab237e9d4c5179a05b127d806823f83c

C2 / staging IP       38.207.178[.]192
HTTP staging          38.207.178[.]192:50813
SNOWLIGHT TCP         38.207.178[.]192:50812
Loader AES key        YtWzxwZimsZoeMen
SNOWLIGHT XOR key     0x99
Kill-switch marker    %TEMP%\log_de.log
```

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0G1HLwD6W2fWqtLAR9hgr1khFEDdC2Vfayz0kbWz5Af4tJciaFUAjy9mmPgWZ6kV88dzWfjrBD4RJdOLHeVvFKHRx1WJZxLGoo8/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址

文章广告会导致阅读影响 - 会开一段时间和关一段时间

公众号 | AnQuan7 (Ots安全)

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