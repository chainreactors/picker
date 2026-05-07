---
title: Chrome 静默下载 4GB 模型的技术取证
url: https://mp.weixin.qq.com/s/Zqa1tQL76lH9Z67Gwbby_Q
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:27:33.445886
---

# Chrome 静默下载 4GB 模型的技术取证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PkfClzhSYicyS7vYI3kbYSygTbCMVodjgmtWpwOhaMqPJteKRIgymdkEyDbcRegvunO6p1nrTp7EGkXt57mt3M67IB0ALYqibKe8tXgdpeTAU/0?wx_fmt=jpeg)

# Chrome 静默下载 4GB 模型的技术取证

林00
林00

SecureNexusLab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 发现与取证

核心事实：Google Chrome 未经用户同意，在磁盘写入 4GB Gemini Nano 模型文件（`weights.bin`）。无弹窗、无退出选项、删了自动重下。

### 一、硬盘上发现了什么

在任意安装 Chrome 的设备上，用户配置目录下存在一个名为 OptGuideOnDeviceModel 的文件夹。

文件清单：

* `weights.bin`，约 4 GB
* `manifest.json`
* `_metadata/verified_contents.json`
* `on_device_model_execution_config.pb`

文件本质：`weights.bin` 是 Gemini Nano 的权重文件，Google 的本地 LLM。

用途：Chrome 用它驱动“帮我写”（Help me write）、本地诈骗检测，以及其他 AI 辅助浏览功能。

关键特征：

* 文件出现时没有任何同意提示
* Chrome 设置里没有一个复选框写着“下载 4GB AI 模型”
* 下载的触发条件是 Chrome 的 AI 功能处于激活状态，而在近几个 Chrome 版本中，这些功能默认就是激活的
* 只要机器满足硬件要求，Chrome 就会把用户的硬件当作分发目标，直接写入模型

### 二、删除后自动重下机制

Windows 平台上多个独立报告证实了删除后自动重下的循环 [5][6][7][8]。

添加这个文件需要零次点击。删除它则需要：发现文件存在、搞清楚它是什么、导航到隐藏的用户配置路径、删除它（Windows 上还要先清除只读属性），以及接受这样一个现实——除非用户进一步通过 chrome://flags 或企业策略工具禁用底层的 Chrome AI 功能，否则 Chrome 下次满足条件时就会再次默默重下 [5]。上述步骤中，没有任何一步是写在普通用户会看的地方，默认的 Chrome 里甚至连暗示都没有。

唯一能让删除“一劳永逸”的办法，要么通过 chrome://flags 或企业策略工具禁用 Chrome 的 AI 功能（普通家庭用户基本不会这么操作），要么彻底卸载 Chrome [5]。

macOS 平台情况：

* 文件权限为 mode 600，属主为用户（原则上可以删）
* Chrome 在写入字节后会把安装状态记录在 Local State 中
* 一旦 variations 服务器再次告知该配置文件“符合条件”，下载就会再次触发
* 架构是一样的，只是文件权限不同

### 三、技术取证：macOS 内核日志

关于这个行为的已有报告大多来自 Windows 用户——他们发现磁盘空间被吃掉了。这确实有用，但 Google 很可能（也确实会）把这些报告说成是“个例”或“非标准配置”。因此需要在一个不同的平台上找一个干净的证据。

为什么选 macOS：

* macOS 内核有一个名为 .fseventsd 的文件系统事件日志
* 它在操作系统层面记录每一次文件的创建、修改和删除，完全独立于任何应用的日志
* Chrome 改不了它，Google 没法远程动它
* 那些记录事件的 page file 即使引用的文件被删了也依然存在

实验环境：

* 2026 年 4 月 23 日，创建一个全新的 Chrome 用户数据目录，用于运行自动化审计（WebSentinel 的 100 站点隐私定期扫描）
* 审计驱动完全基于 Chrome DevTools Protocol：加载页面后停留五分钟，无任何输入，记录事件，站点间关闭 Chrome
* 从头到尾，这个配置文件从未接受过任何人类的键盘或鼠标输入
* Chrome 里所有“AI 模式”界面都没被碰过——实际上 Chrome 的任何界面都没被碰过，审计驱动只通过 CDP 与文档交互，连地址栏都没碰过
* 到 4 月 29 日，该配置文件里出现了 4GB 的 OptGuideOnDeviceModel 权重（发现方式：例行清理时对审计配置目录执行了 du -sh）

.fseventsd 取证结果（字节级精确，分散在三个顺序的 page file 中）：

**「第一时间点」**：2026 年 4 月 24 日 14:38:54 UTC，Chrome 在审计配置目录下创建了 OptGuideOnDeviceModel 文件夹（page file 0000000003f7f339）。

**「第二时间点」**：2026 年 4 月 24 日 14:47:22 UTC，三个并发的解压子进程在 /private/var/folders/.../com.google.Chrome.chrome\_chrome\_Unpacker\_BeginUnzipping.\*/ 下创建临时目录。

第一个子进程（5xzqPo）写入了：

* `weights.bin`
* `manifest.json`
* `_metadata/verified_contents.json`
* `on_device_model_execution_config.pb`

第二个子进程写入了证书吊销列表更新。

第三个子进程写入了浏览器预加载数据更新。

关键观察：Chrome 把一个安全更新、一个预加载刷新和一个 4GB 的 AI 模型，全都塞进了同一个空闲窗口里，当成三者等量齐观（page file 00000000040c8855）。

**「第三时间点」**：2026 年 4 月 24 日 14:53:22 UTC，解压后的 `weights.bin` 被移动到最终位置：OptGuideOnDeviceModel/2025.8.8.1141/`weights.bin`。

同时移动的还有：

* `adapter_cache.bin`
* `encoder_cache.bin`
* `_metadata/verified_contents.json`
* 执行配置

与此同时，另外四个模型目标在 Chrome 的 optimization-guide 枚举中编号为 40、49、51 和 59，它们在 optimization\_guide\_model\_store 里注册了新条目。这些是与 LLM 配合使用的较小的文本安全和提示路由模型。这之前，这个配置文件中完全没有这些目标（page file 00000000040d0f9c）。

**「总安装时长」**：从目录创建到最终移动完成，14 分 28 秒。

**「期间人类操作量」**：零。审计驱动要么在某个第三方首页停留，要么在站点之间切换。解压程序在后台触发，而前台标签页只是在等一个五分钟的计时器到期。

### 四、写入者身份确认

fseventsd 记录里的命名细节是最致命的点。

临时目录的完整路径模式是： /private/var/folders/.../com.google.Chrome.chrome\_chrome\_Unpacker\_BeginUnzipping.5xzqPo

前缀 com.google.Chrome.chrome\_chrome\_\* 是 Google Chrome 自己用的 bundle ID 和子进程命名规范。它不是 com.google.GoogleUpdater.*，也不是 com.google.GoogleSoftwareUpdate.*。

**「结论」**：写入者就是 Chrome 本身——那个用户安装并信任、用来加载网页的浏览器进程。它自发地伸手进用户的文件系统，在前台标签页做着完全不相关的事情的同时，放下一个 4GB 的机器学习二进制文件。

### 五、三重佐证证据

同一台机器上，还有另外三条佐证证据。

**「证据 A：Chrome 自己的 Local State JSON」**

审计配置文件中的 optimization\_guide.on\_device 块包含以下内容：

model\_validation\_result: { attempt\_count: 1, result: 2, component\_version: “2025.8.8.1141” }

result 为 2 表示 Chrome 已经实际运行过该模型。component\_version 与 .fseventsd 事件记录中作为路径组件的版本字符串完全一致。两个独立的见证者，指向同一个工件。

同一块还报告了 performance\_class: 6，vram\_mb: “36864”。这意味着 Chrome 评估了用户的硬件：读取了 GPU，读取了统一内存总量（36864 MB 即约 36GB），来决定是否有资格被推送模型。而此时，任何面向用户的 AI 功能都还没有出现。

**「证据 B：Chrome 的 ChromeFeatureState」**

审计配置文件的 enable-features 块中列出了两个项目：

OnDeviceModelBackgroundDownload<OnDeviceModelBackgroundDownload

ShowOnDeviceAiSettings<OnDeviceModelBackgroundDownload

第一个 flag 是触发静默下载的那个。第二个 flag 是在 chrome://settings 中显示本地 AI 设置项的那个。

两者被同一个 rollout flag 控制。这意味着，按照 Chrome 自己的架构设计，安装动作早于用户能够拒绝它的任何设置界面。那个能让用户发现该功能存在的设置页面，是和安装动作同步启用的。这不是疏忽，这是设计。

**「证据 C：GoogleUpdater 日志」**

日志中记录了本地模型控制组件的下载信息：

组件 ID 为 {44fc7fe2-65ce-487c-93f4-edee46eeaaab}。

下载地址为 http://edgedl.me.gvt1.com/edgedl/diffgen-puffin/%7B44fc7fe2-65ce-487c-93f4-edee46eeaaab%7D/...，使用明文 HTTP 协议。校验依赖包内 CRX-3 签名，而非传输层安全。

文件大小约 7 MB，是一个压缩控制文件。

到达时间为 2026 年 4 月 20 日，比上述审计配置文件的创建时间早了三天。

触发方式：由一个每小时触发一次的 LaunchAgent 自动启动，不依赖具体配置文件。

流程说明：控制组件给 Chrome 提供了指向实际权重文件的清单。然后 Chrome 自身的进程内 OnDeviceModelComponentInstaller——一条独立于 GoogleUpdater 的代码路径——从 Google 的 CDN 直接拉取数 GB 的权重文件。

### 六、四层证据链汇总

**「第一层」**：macOS .fseventsd 内核文件系统事件，记录了文件创建的精确时间戳和路径。Chrome 无法修改，Google 无法远程删除。page file 即使引用的文件被删也依然存在。

**「第二层」**：Chrome Local State JSON，记录了模型验证结果（证明模型已被运行）和硬件评估数据（GPU/内存）。Chrome 自己写入，可验证。

**「第三层」**：Chrome ChromeFeatureState 运行时功能标志，记录了功能开关状态（下载与设置界面同步启用）。Chrome 运行时标志，可读取。

**「第四层」**：GoogleUpdater 日志，记录了控制组件下载记录（提前三天到达，明文 HTTP）。系统日志，独立于 Chrome。

四层证据完全一致：一个 4GB 的 AI 模型，未经用户同意、没有任何通知，被放到了一个从未接收任何人类输入的配置文件上，仅用 14 分 28 秒，在一个周二下午，完成了这一切。

### 七、规模与影响范围

OptGuideOnDeviceModel 目录和 `weights.bin` 文件的报告，在社区论坛里已经流传了超过一年。

2026 年的新变化在于：规模和可验证性。

Chrome 的全球市场份额仍然稳定在 64% 以上 [9][10]。Chrome 的用户量在全球约 34.5 亿到 38.3 亿人之间（取决于使用哪个 2026 年的估算数字 [9][11]）。Google 正以越来越激进的态度将 Gemini 功能整合进 Chrome。

这个行为不再是影响少数平台上的少数高级用户。它正在影响数亿台设备，覆盖 Chrome 所支持的所有桌面操作系统（Windows、macOS、Linux）。

---

**「原文出处」**：That Privacy Guy

**「参考文献」**：[5][6][7][8][9][10][11] 见原文末尾

---

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