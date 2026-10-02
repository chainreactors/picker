---
title: 黑客向管理员隐藏微软 Defender 排除项，以此规避杀毒扫描
url: https://mp.weixin.qq.com/s/YODcK9GM-MbsNBTjCQ9jZg
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:44:32.286553
---

# 黑客向管理员隐藏微软 Defender 排除项，以此规避杀毒扫描

# 黑客向管理员隐藏微软 Defender 排除项，以此规避杀毒扫描

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

威胁攻击者正越来越多地滥用微软 Defender 防病毒软件的排除项，让恶意文件绕过终端扫描。而一项鲜为人知的策略设置，可以让普通管理工具看不到这些排除项。

Huntress 研究人员发现，攻击者可以将大范围 Defender 排除项与  HideExclusionsFromLocalAdmins  设置相结合，构建一条隐蔽的防御规避途径。恶意活动不会被扫描到，同时篡改的证据也会被掩盖。

微软 Defender 防病毒（MDAV）排除项属于合法管理控制项，原本用来避免可信软件出现性能或兼容性问题。

排除项可以针对进程、文件路径、文件扩展名或者IP地址，使其避开杀毒软件特定的检测功能。

但攻击者一旦拿到本地管理员或更高权限，就可以滥用该功能，对存放、运行恶意软件的位置关闭实时扫描、计划扫描和按需扫描。

在入侵事件当中，路径排除和扩展名排除风险最高。

如果对临时目录、用户配置文件夹或者整个磁盘驱动器设置路径排除，攻击者就可以下载、解压并执行恶意载荷，全程不受 Defender 检测。

扩展名排除同样会制造检测盲区，恶意二进制程序、脚本、压缩包、重命名后的恶意载荷都可以借此躲过扫描。

微软说明，排除项可以通过 Intune、MDM、组策略、PowerShell 或者 WMI 进行配置。攻击者提权之后，可滥用的管理接口非常多。

只要配置了 Defender 的排除规则，相关设置最终都会写入 Windows 注册表。

因此无论使用哪种配置方式，注册表遥测数据对安全检测都极具价值。

实现隐藏效果的关键策略参数是  HideExclusionsFromLocalAdmins ，注册表路径如下：

HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\HideExclusionsFromLocalAdmins

开启该参数并不会删除已有的排除规则，而是阻止普通本地管理员查询到这些排除项，包括  Get‑MpPreference  命令；按照微软现有文档，在注册表编辑器里也看不到相关内容。

Huntress 还发现，该限制甚至会影响 SYSTEM 权限下的 PowerShell 查询。如果安全产品、检测脚本仅依靠 Defender 命令行工具核查排除规则，防护能力就会被削弱。

这种攻击手段比直接关闭微软 Defender 要隐蔽得多。杀毒服务一旦被禁用，很容易触发安全告警、合规报错，会立刻引起安全分析人员的注意。

而设置排除项，在服务器、开发人员终端、运行业务软件的设备上，看起来很像正常业务需要的杀毒例外规则，不容易引起怀疑。

Huntress 表示，微软 Defender 排除项的创建方式很多：PowerShell 命令  Set‑MpPreference 、 Add‑MpPreference ；WMI 类  MSFT\_MpPreference ；组策略；或者直接修改受策略管控的注册表项。

微软 Defender 排除项攻击

该技术已经出现在真实网络攻击活动中。GootKit 恶意软件曾通过 WMI 添加 Defender 路径排除；具有破坏性的 WhisperGate 恶意软件，利用 PowerShell 将C盘整盘加入排除列表。

这类行为对应 MITRE ATT&CK 攻击技术 T1562.001：破坏防御：禁用或修改安全工具，描述攻击者篡改安全控制，规避对恶意软件及其行为的检测。

防御人员不能只依靠  Get‑MpPreference  命令或者 Windows 安全中心界面去核查 Defender 配置。

事件响应人员应当采集并监控两处注册表键值的变更，一旦发生改动就触发告警：

HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions

HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Exclusions

只要  HideExclusionsFromLocalAdmins  参数发生改动，安全团队就需要开展调查；尤其是修改行为发生在可疑 PowerShell、WMI、组策略操作、远程管理、凭证窃取或者恶意载荷落地行为的前后。

Huntress 建议采用注册表层面遥测监控：因为无论用哪种方式添加排除项，最终都会产生注册表修改事件，可以对其进行监控。

企业应当尽量减少长期分配的本地管理员权限；通过 Intune 或者组策略集中管控 Defender 策略；明确核查是否允许本地管理员把本地自建排除项和集中下发的策略合并。

微软文档说明，系统默认会合并本地配置的排除项与集中部署的策略；发生冲突时，集中托管的排除规则优先级更高。

管理员还要建立一份经过审批的排除项基准。一旦出现大范围排除规则，例如磁盘根目录路径、临时目录、用户可写入文件夹、通配符扩展名、异常IP排除，就标记为风险。

只要发现存在隐藏排除项，就应当启动调查，不要默认是管理员的正常配置。

核心启示：杀毒软件显示处于开启状态，并不能代表终端防护有效。

Defender 表面上正常运行，但攻击者可以悄悄划出不受扫描的区域用来执行恶意软件，还能把这些例外规则对管理员隐藏起来。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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