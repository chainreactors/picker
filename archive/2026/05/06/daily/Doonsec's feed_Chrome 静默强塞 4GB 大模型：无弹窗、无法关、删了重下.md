---
title: Chrome 静默强塞 4GB 大模型：无弹窗、无法关、删了重下
url: https://mp.weixin.qq.com/s/5mQ17M7biV_Rp06lQq5pgA
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:27:30.591045
---

# Chrome 静默强塞 4GB 大模型：无弹窗、无法关、删了重下

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PkfClzhSYicxCqs46l9sIfMg2usIHW4Y6JcAHibqldwAaUfAO1h5e3RZ58I8rET6ibsxgIJR7pM6wV0ScOHnO8TbuFX1icicuF5UPudgLO0UbH0U/0?wx_fmt=jpeg)

# Chrome 静默强塞 4GB 大模型：无弹窗、无法关、删了重下

林00
林00

SecureNexusLab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> ❝
>
> Google Chrome 未经任何同意，在用户磁盘写入一个 4GB 的 Gemini Nano 模型文件。无同意对话框、无退出选项、删了自动重下。
> **「这不是“AI 功能”，这是对用户设备的预部署。」**
>
> ❞

X 平台用户指出：“Chrome 会悄无声息地在你的设备上安装一个 4GB 的 AI 模型。无同意对话。没有选择退出界面。如果用户手动移除，会自动重新安装。这才是恶意软件的真正定义。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PkfClzhSYicyYz3f6zEf3Iia61tFjTT4o9wqL56bv996dPSyz3o6fyvVPCqgAvKhK1ATLBP91D8E3qagiaic3S4zwkEgXou1iaJEQ3nGtpnHkMtM/640?wx_fmt=png)

以下为完整的技术验证过程。

## 1. 证据：硬盘上多了什么？

在任意安装 Chrome 的设备上，用户配置目录下会出现一个名为 `OptGuideOnDeviceModel` 的文件夹，内含：

* `weights.bin`（约 4 GB）
* 配套的 `manifest.json`、`_metadata/verified_contents.json`
* 模型执行配置 `on_device_model_execution_config.pb`

这就是 **「Gemini Nano」** 的本地 LLM 权重文件。Chrome 用它驱动“帮我写”（Help me write）、本地诈骗检测以及其他 AI 辅助浏览功能，但这些功能在近几个 Chrome 版本中**「默认开启」**。

文件出现的时候，没有任何同意提示。Chrome 设置里没有一个复选框写着“下载 4GB AI 模型”。

## 2. 取证：全程无人输入，模型自动落地

大部分已有报告来自 Windows 用户（发现磁盘空间被吃掉），但技术分析人员选择在 **「macOS 上利用内核级日志 `.fseventsd`」** 进行验证。该日志在操作系统层面记录每一次文件的创建、修改和删除，Chrome 无法修改、Google 无法远程删除。

2026 年 4 月 23 日，分析人员创建了一个全新的 Chrome 用户数据目录用于自动化审计。该审计驱动完全基于 Chrome DevTools Protocol，加载页面后停留五分钟，无任何输入，站点间关闭 Chrome。从头到尾，这个配置文件从未接受过任何人类的键盘或鼠标输入。Chrome 里所有“AI 模式”界面、实际上 Chrome 的任何界面都没被碰过。

到 4 月 29 日，该配置文件目录下出现了 4GB 的 `OptGuideOnDeviceModel` 权重。`.fseventsd` 日志给出了精确到字节的记录：

* **「2026 年 4 月 24 日，14:38:54 UTC」**：Chrome 创建 `OptGuideOnDeviceModel` 目录。
* **「14:47:22 UTC」**：三个并发的解压子进程在 `/private/var/folders/.../com.google.Chrome.chrome_chrome_Unpacker_BeginUnzipping.*/` 下创建临时目录。其中一个写入 `weights.bin`、`manifest.json`、`_metadata/verified_contents.json` 和 `on_device_model_execution_config.pb`。第二个写入证书吊销列表更新。第三个写入浏览器预加载数据更新。**「Chrome 把一个安全更新、一个预加载刷新和一个 4GB 的 AI 模型，全部塞进了同一个空闲窗口」**。
* **「14:53:22 UTC」**：解压后的 `weights.bin` 被移动到最终位置 `OptGuideOnDeviceModel/2025.8.8.1141/weights.bin`，同时还有 `adapter_cache.bin`、`encoder_cache.bin`、`_metadata/verified_contents.json` 和执行配置。另外四个较小的模型（文本安全、提示路由）同时注册。

**「总安装时间：14 分 28 秒。期间人操作：零。」** 前台标签页只是在等一个五分钟计时器，完全无任何“AI 功能”被触发。

## 3. 三重独立证据链交叉验证

除了内核日志，分析还从 Chrome 自身状态中提取了三条不可抵赖的证据：

**「证据一：Chrome 的 `Local State` JSON」**
审计配置文件中包含 `optimization_guide.on_device` 块，内有 `model_validation_result: { attempt_count: 1, result: 2, component_version: "2025.8.8.1141" }` —— Chrome **「已经实际运行过该模型」**。版本字符串与 `.fseventsd` 记录完全一致。同一块还报告了 `performance_class: 6, vram_mb: "36864"`，说明 Chrome 先读取了 GPU 和统一内存总量来评估硬件，然后决定是否推送模型——而此时任何面向用户的 AI 功能都尚未出现。

**「证据二：Chrome 运行时功能标志 `ChromeFeatureState`」**
`enable-features` 中同时开启了：

* `OnDeviceModelBackgroundDownload`（触发静默下载）
* `ShowOnDeviceAiSettings`（在 `chrome://settings` 中显示本地 AI 设置项）

两个 flag 由同一个 rollout 控制。这意味着：**「下载早于用户能够拒绝它的任何设置界面」**。那个能让用户发现该功能存在的设置页面，是和安装动作同步启用的——这不是疏忽，这是架构设计。

**「证据三：GoogleUpdater 日志」**
本地模型控制组件（appid `{44fc7fe2-65ce-487c-93f4-edee46eeaaab}`）从 `http://edgedl.me.gvt1.com/...` 下载——一个 7MB 的压缩控制文件，URL 是**「明文 HTTP」**（包内通过 CRX-3 签名校验完整性，而非依赖传输层安全）。这控制组件在 2026 年 4 月 20 日到达，比上述审计配置文件的创建时间早了三天。它由一个每小时触发一次的 LaunchAgent 自动启动，不依赖具体配置文件。控制组件给 Chrome 提供指向实际权重文件的清单，然后 Chrome 自身的 `OnDeviceModelComponentInstaller`（独立于 GoogleUpdater 的代码路径）再从 Google CDN 直接拉取数 GB 权重。

结论：**「四层独立证据完全一致」**——macOS 内核文件系统事件、Chrome 每个配置文件的状态、Chrome 运行时功能标志、Google 组件更新日志，全部指向同一个行为：一个 4GB 的 AI 模型，未经任何人类交互，在 14 分 28 秒内被推送到用户磁盘。

## 4. 删不掉的重试机制

Windows 平台上已有多个独立报告证实了删除后自动重下的循环：用户删了，Chrome 重下；用户再删，Chrome 再重下。

在 macOS 上，文件权限为 mode 600、属主为用户（原则上可以删），但 Chrome 在写入字节后把安装状态记录在 `Local State` 中。一旦 variations 服务器再次告知该配置文件“符合条件”，下载就会再次触发——架构相同，只有文件权限不同。

唯一能让删除“一劳永逸”的方法：通过 `chrome://flags` 或企业策略工具禁用 Chrome 的 AI 功能（普通家庭用户基本不会这么操作），或者彻底卸载 Chrome。普通用户根本不会知道这些隐藏开关的存在。删除操作被 Chrome 视为“临时状态需纠正”，而非用户意图。

## 5. “AI 模式”的欺骗性设计

Chrome 147 启动后，地址栏右侧会渲染出一个 **「“AI 模式”」** 小药丸。一个理性用户看到这个出现在浏览器最显眼的 UI 元素中，又知道 Chrome 有本地 LLM 并已经被静默安装了一个 4GB 的 Gemini Nano 在自己硬盘上，自然会推断：这个可见的“AI 模式”用的应该是本地模型，查询会停留在设备上。

**「事实完全相反：」**

这“AI 模式”**「是一个」**云端支持的 Search Generative Experience 界面，每个查询都会被发送到 Google 服务器，由 Google 托管的模型处理。本地的 Nano 模型根本不会被这个 UI 流程调用。

真正使用本地 Nano 模型的功能（“帮我写”在 `<textarea>` 中、标签组 AI 建议、智能粘贴、页面摘要）全部藏在右键菜单和标签组的次级菜单中，普通用户平均来说可能永远都不会发现。

因此，用户付出了 4GB 磁盘空间和下载带宽的代价，却得不到任何本地化的隐私优势。最显眼的 AI 入口反而继续将用户输入外发到 Google 服务器。本地模型被预埋在用户设备上，只是为 Google 提供了一个“未来可选项”——供 Chrome 的其他子系统调用，无需额外的服务器往返。它不是用户的资产，而是放在用户设备上的、属于 Google 的资产。

## 6. 这不是个别案例

`OptGuideOnDeviceModel` 目录和 `weights.bin` 文件的报告在社区论坛里已经流传了一年多。2026 年的新变化在于规模和可验证性。

Chrome 的全球市场份额稳定在 64% 以上，用户量约 34.5 亿到 38.3 亿人。Google 正以越来越激进的态度将 Gemini 功能整合进 Chrome。这个行为不再是影响少数平台上的少数高级用户——它正在影响数亿台设备，覆盖 Chrome 所支持的所有桌面操作系统（Windows、macOS、Linux）。

## 7. 与同类行为的对比

分析者此前曾报道 Anthropic 在 Claude Desktop 安装时，向七个 Chromium 浏览器写入 Native Messaging 桥接配置。两者的暗黑模式完全相同：

1. **「跨越信任边界的强制绑定」**：Anthropic 写入其他浏览器；Google 写入用户文件系统一个 4GB 非浏览器本身的二进制。
2. **「不可见的默认行为」**：首次启动无提示，设置里无复选框。
3. **「删比装难得多」**：添加零点击；删除需发现文件、理解它是什么、导航到隐藏路径、删除（Windows 上还需清除只读属性），并接受 Chrome 会再次重下。
4. **「为用户尚未请求的功能预部署」**：模型在用户从未调用任何 AI 功能的情况下已存在于硬盘。
5. **「通用名称模糊范围」**：`OptGuideOnDeviceModel/weights.bin` 让用户无法联想到“Gemini Nano LLM”。
6. **「注册到用户未曾配置的资源」**：从未打开或只打开过一次就关闭的用户，照样收到模型。
7. **「文档缺失」**：面向用户的文档没有以与 4GB 下载相称的显著程度告知这一行为。
8. **「每次运行自动重装」**：删除后重建，用户删除被视为需“纠正”的临时状态。
9. **「通过正式发布通道分发」**：代码签名，Chrome 稳定版，非测试行为。
10. **「云端入口掩盖本地模型」**：最显眼的“AI 模式”不使用本地模型，形成误导。

## 8. 法律与环境层面的结论

**「法律层面」**：

* 这行为被指违反欧盟 **「ePrivacy 指令（2002/58/EC）第 5 条第 3 款」**：禁止在用户终端设备存储或访问信息，除非用户事先给出明确同意且该操作对于用户明确请求的服务绝对必要。4GB 模型文件未经同意写入，Chrome 无需该文件即可正常工作。
* 同时被指违反 **「GDPR（欧盟《通用数据保护条例》）第 5 条第 1 款」**（合法性、公平性、透明度）和**「第 25 条」**（默认数据保护设计）。
* 在英国，**「英国 GDPR」** 和 **「PECR 2003（隐私与电子通信条例）」** 分析相同。
* 在美国，**「CCPA（加州消费者隐私法案）」** 下未提供“收集时通知”，合规存疑。

**「环境层面」**：

* 分析师估算了本次推送的碳排放：每设备 0.06 kg CO2e（仅交付一次）。以 1 亿、5 亿、10 亿设备三个区间计算，总碳排放分别为 6,000、30,000、60,000 吨 CO2e。
* 这还不包括：持续占用的 SSD 存储的隐含碳（约 0.16 kg CO2e/GB NAND 制造）、用户删除后重下导致的额外传输、未来模型更新、以及模型实际使用时的本地推断能耗。
* 对于使用按量计费移动数据的用户（尤其是在手机作为唯一上网手段的地区），4GB 的非请求下载相当于一个月流量额度被 Chrome 单方面消耗。

## 9. 如何完全阻止

若想彻底终止该行为，需执行以下两步（缺一不可）：

**「第一步：删除已下载的模型文件」**

* Windows: `%LocalAppData%\Google\Chrome\User Data\Default\OptGuideOnDeviceModel`
* macOS: `~/Library/Application Support/Google/Chrome/Default/OptGuideOnDeviceModel`
* Linux: `~/.config/google-chrome/Default/OptGuideOnDeviceModel`

**「第二步：禁用 Chrome 的 AI 功能（阻止重下）」**

* 访问 `chrome://flags/#optimization-guide-on-device-model` → 设置为 `Disabled`
* 或通过企业策略：`OptimizationGuideOnDeviceModel` 设为 `false`

否则，删除文件后 Chrome 会在下次满足条件时重新下载。

## 10. 原文出处与技术验证

**「原文来源」**：That Privacy Guy – *“Google Chrome is downloading a 4 GB Gemini Nano model onto users' machines without consent”*

**「技术验证方法」**：

* macOS `.fseventsd` 内核级文件系统事件日志
* Chrome 每个配置文件的 `Local State` JSON
* Chrome 运行时功能标志 `ChromeFeatureState`
* GoogleUpdater 组件更新日志

**「影响范围」**：所有桌面平台（Windows、macOS、Linux）Chrome 稳定版，数亿级别设备

---

> ❝
>
> **「最后」**：浏览器不应在用户未明确要求时向磁盘写入 4GB 二进制。无论这二进制是 AI 模型、防病毒库还是浏览器组件，都应遵循 **「先问、再下、可关、删了不复活」** 的基本规则。
>
> ❞

**「讨论环节」**

看完这篇分析，你认为 Chrome 的行为算“恶意软件”吗？

1. **「你是否在自己的电脑上发现了 `OptGuideOnDeviceModel` 文件夹？」** 用了多久才发现磁盘空间被占用？
2. **「浏览器预部署 AI 模型的边界在哪里？」** 如果 Google 在首次启动时弹窗询问“是否下载 4GB 模型以启用本地 AI 功能”，你还会觉得有问题吗？问题到底出在“下载”本身，还是“未经同意”？

评论区见～

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkLGDzh5WQ5kuYab29V2PteuUrCj2HeRIHibmjQEK7plD7iccC97duj94oGugfkHdQdxcaXtB7w5icmg/0?wx_fmt=png)

SecureNexusLab

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkLGDzh5WQ5kuYab29V2PteuUrCj2HeRIHibmjQEK7plD7iccC97duj94oGugfkHdQdxcaXtB7w5icmg/0?wx_fmt=png)

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