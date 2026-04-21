---
title: 【天穹】暗度陈仓：银狐白利用技术升级
url: https://mp.weixin.qq.com/s/ulLnCu6xRVd9wbW9_Q2hxA
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:48:06.868667
---

# 【天穹】暗度陈仓：银狐白利用技术升级

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QSjGzxHEMduRvrkn7VUqpAInLjwYt5lPrg1CocNwfVw8d4n8nVNHaYZ9YtkQakWYetO38A39TVIQ5tqMLTIiaEnXiblf0coxJWODQTf3h8ojo/0?wx_fmt=jpeg)

# 【天穹】暗度陈仓：银狐白利用技术升级

星图实验室
星图实验室

奇安信技术研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**0****1**

**概述**

天穹沙箱近期捕获并深度分析了一类具备环境自适应能力的高级恶意样本。这些样本在初始执行阶段会主动探测系统是否安装 360sd.exe 或 ZhuDongFangYu.exe，并根据探测结果动态切换攻击路径：

**策略一（检测到安全软件）**：采用 .URL 热键快捷方式 + 文件关联劫持 + 模拟按键触发的组合链，通过终止并重启 explorer.exe 完成隐蔽投递，最终将载荷精准释放至开机启动项。

**策略二（载荷执行与C2通信）**：无论通过何种路径投递，最终均会利用“白加黑”技术加载 sgfeedbackhelper.exe 与 HWSignature.dll，在内存中反射执行 Shellcode，并直连 C2 服务器 206.238.180[.]192。

**策略一**攻击链全程使用系统白名单组件（explorer.exe、7z.exe），通过多层间接执行规避行为监控，最终将恶意载荷静默植入用户启动项。本文详细拆解该攻击链的技术细节。

**0****2**

**样本信息**

* 样本名： DingDing64x\_SETUP\_DD\_192.exe
* SHA1： dd5d5f25c4ec060065ebc8a5795cff92ac32ddf3
* 文件类型： EXE
* 文件大小： 31.31 MB (32828416 bytes)
* 家族归属：银狐
* 策略二分析报告链接：

  https://sandbox.qianxin.com/tq/report/toViewReport.dorid=21cf3efa2e40f35eede8cd611147a041&sk=52479977)

**0****3**

**攻击全景：恶意软件是如何“悄悄住进”系统的？**

为了躲避安全软件的查杀，攻击者放弃了传统的“直接运行病毒”模式，转而采用 **“借力打力”** 的策略。整个攻击过程就像一次精心策划的 **“接力赛”**，如图 1 所示。

1. 部署隐形传送门：攻击者在用户环境释放一个特殊的 .URL 文件。当系统或用户无意中触发它时，它会利用 Windows 内置的跳转协议，将执行权悄悄传递给另一个 .lnk 快捷方式文件。
2. 篡改“默认打开方式”：攻击者提前在系统后台动手脚，将某种自定义文件类型的“打开命令”替换为解压指令。当快捷方式被触发时，系统会“乖乖地”调用压缩工具执行操作，而不是报错。
3. 精准“空投”至开机目录：攻击者利用压缩工具的默认解压特性，配合精心设置的工作目录，让恶意快捷方式被完整解压到电脑的 Startup（开机启动项）文件夹中。
4. 静默潜伏：用户下次开机或重启资源管理器时，该快捷方式会自动运行，完成最终的恶意载荷加载。

![攻击全景](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdupdSVC8U74hCc2ARvaeFhD1WCphnbzvmFl5Mjbojh1DTeVBTY072wPw9M6NSiaBiavuvX9s3ficjDlD4BV6Exvo536Kg89LILfG4/640?wx_fmt=png&from=appmsg)

图1 攻击全景

## 核心手法拆解

本次攻击最危险的地方在于，全程使用的都是系统自带或常见的合法程序，没有调用任何可疑的恶意代码。

### 手法一：特制 .URL 文件充当“协议路由器”

普通用户常把 .URL 当作网页书签。但攻击者编写的 .URL 文件中隐藏了 `file:///` 本地路径跳转指令。配合特定的系统标识符，它能欺骗 Windows 资源管理器，使其像打开网页一样，平滑跳转到本地另一个恶意快捷方式。由于它只是纯文本，且格式完全符合微软规范，传统杀毒软件很难将其识别为威胁。

样本在 `C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Start Menu\` 目录下创建 SVPC.URL 文件，内容如下：

```
[{000214A0-0000-0000-C000-000000000046}]Prop3=19,9[InternetShortcut]URL=file:///C:\Program Files\SogouInput\15.11.0.2620\2p2WTGnE\2p2WTGnE.lnkIDList=HotKey=1147
```

技术要点：

1. CLSID声明：{000214A0-0000-0000-C000-000000000046} 为 Shell Link Object 标识，使系统按快捷方式逻辑解析。
2. 协议跳转：`file:///` 协议指向本地 .lnk 文件，实现二次跳转。
3. HotKey=1147（0x47B）对应 Alt+F12，即为该快捷方式设置了一个全局热键，当检测到 Alt+F12 组合键被按下时，会立即执行预设的 URL 链接，实现快速访问功能。

### 手法二：巧用压缩工具特性，实现“指哪打哪”

攻击者没有使用复杂的脚本，而是利用了 7z.exe 的一个基础特性：如果不指定解压路径，它会默认在“当前工作目录”下解压。攻击者在后台偷偷将工作目录切换到用户目录，而压缩包内部只记录了相对路径 `Microsoft\Windows\Start Menu\Programs\Startup\`。两者结合，恶意文件就像装了导航一样，精准降落在开机自启文件夹，且对普通用户完全透明。

快捷方式（2p2WTGnE.lnk）的结构如下：
• 目标程序：`"C:\Program Files\SogouInput\15.11.0.2620\RaYimlPT\7z.exe"`
• 执行参数：`x "C:\Program Files\SogouInput\15.11.0.2620\RaYimlPT\RaYimlPT.zip"`
• 起始位置（工作目录）：`C:\Users\<User>\AppData\Roaming`

RaYimlPT.zip 压缩包内存储的是相对路径而非绝对路径：

```
RaYimlPT.zip 内容结构：└── Microsoft/    └── Windows/        └── Start Menu/            └── Programs/                └── Startup/                    └── FaCveHBxNRaYimlPT.lnkXnOsgIDx
```

由于本次解压未显式指定输出目录，7-Zip 默认以当前工作目录作为解压基路径。在展开压缩包时，系统会自动将基路径与包内相对路径进行拼接，最终落盘至 `%AppData%\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`。该路径恰好对应当前用户的系统“启动”文件夹，属于 Windows 原生的开机自启持久化目录。

```
实际解压路径= 工作目录(CWD) + 压缩包内相对路径= %AppData%\Roaming\ + Microsoft\Windows\Start Menu\Programs\Startup\= %AppData%\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
```

样本通过代码模拟按下 `Alt + F12` 快捷键。系统识别到该组合键后，会自动执行预先绑定的网址（URL）打开或调用流程，全程无需用户交互。

```
keybd_event(VK_MENU, 0, 0, 0); // 按下ALTkeybd_event(VK_F12, 0, 0, 0); // 按下F12keybd_event(VK_F12, 0, KEYEVENTF_KEYUP, 0); // 释放F12keybd_event(VK_MENU, 0, KEYEVENTF_KEYUP, 0); // 释放ALT
```

### 手法三：劫持系统“文件关联”，借壳执行

该手法利用 Windows 系统 **“文件类型-默认程序”** 关联机制实现隐蔽加载。攻击者在注册表中伪造了特定后缀（`.lnkXnOsgIDx` / `.FaCveHBxN`）的打开规则，将其 `shell\open\command` 指向合法组件。系统重启时，`explorer.exe` 自动遍历启动目录，尝试执行 `FaCveHBxNRaYimlPT.lnkXnOsgIDx`。系统依据注册表关联将其识别为常规文件打开操作，从而放行并触发预设命令，最终静默拉起 `C:\Program Files\SogouInput\15.11.0.2620\RaYimlPT\sgfeedbackhelper.exe`。该过程依托系统原生行为掩护执行链，有效规避基于进程名或哈希的传统拦截策略。

**0****4**

**载荷执行—基于目录伪装的DLL（白加黑）**

无论通过策略一投递至 Startup，还是直接释放，后续执行逻辑完全一致：

* 目录伪装与白加黑

  样本在目标主机释放后续载荷至 `C:\Program Files\SogouInput\15.11.0.2620\<8位随机字符串>\`，例如：`C:\Program Files\SogouInput\15.11.0.2620\r9TV40qr\`。

  该目录下包含：

```
sgfeedbackhelper.exe：输入法官方反馈组件（合法签名白程序）HWSignature.dll：攻击者构造的恶意 DLL
```

当 sgfeedbackhelper.exe 启动时，Windows DLL 搜索顺序优先加载当前目录下的同名或依赖 DLL。恶意 HWSignature.dll 被成功劫持加载，这是典型的白加黑利用，如图 2 所示。

![白加黑利用](https://mmbiz.qpic.cn/mmbiz_png/QSjGzxHEMdtz1mxGrpjiaj9D8yOqbzxFM0AWr22N0cAvyqLU2Yzby9icYGx4ENRcyCOicdQ8iaTM7KmrfcwnnAzmIiadH0TwFEPPMy5PTRTKCUA8/640?wx_fmt=png&from=appmsg)

图2 白加黑利用检测

* 内存 Shellcode 执行与 C2 通信

  **内存执行链**：动态加载当前目录下的加密 `PeLoader` 载荷，采用无文件落地技术（Fileless Execution）在内存中解密并注入执行。

  **家族溯源**：载荷行为特征命中天穹沙箱内置检测规则，确认为 **“银狐”** 恶意软件家族，如图 3 所示。

  **C2 通信**：Shellcode 直接通过硬编码 IP 或域名与攻击者 C2 服务器建立通信隧道，实现持久化远程控制。

  ![威胁配置信息](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdv86BgFeyzstLBSjDCBA43HaaKicdibibgpnTsW23c2xHNhV4b1zXMO9QTTKb5J7oPY1YkmibaicOrQu911KdiaFhp06CSzM7qhN6tow/640?wx_fmt=png&from=appmsg)

  图3 威胁配置信息

**0****5**

**IOC**

**恶意文件（MD5）**

```
c5e622b8c1213357610e40688625430b DingDing64x_SETUP_DD_192.exeb1f13ebdec32a30c560f5ab2798040e5 2026.04.15----最新名单公示.exe.x64.exe
```

**恶意文件 IOC**

```
206.238.180[.]192:6666adbufrd[.]cn
```

**报告链接**
策略二分析报告链接：

https://sandbox.qianxin.com/tq/report/toViewReport.dorid=21cf3efa2e40f35eede8cd611147a041&sk=52479977)

天穹智能分析平台**（联系我们申请账号）：https://sandbox.qianxin.com**

天穹智能分析平台持续迭代升级，致力于为每一位样本分析人员打造更高效、更智能、更易用的分析平台——这始终是我们不变的初心与追求。

如果您希望深入了解平台功能，或在使用过程中遇到任何问题，欢迎随时联系我们。您的反馈，是我们进步的重要动力！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/lG0evzxL96k3J9EIwMqhiacpDHibsxFTCugUuHF9VUnGG5ceic7dILO41pMNfer7OzCyIviaBYAWAZicicVfocuO8HKw/0?wx_fmt=png)

奇安信技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lG0evzxL96k3J9EIwMqhiacpDHibsxFTCugUuHF9VUnGG5ceic7dILO41pMNfer7OzCyIviaBYAWAZicicVfocuO8HKw/0?wx_fmt=png)

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