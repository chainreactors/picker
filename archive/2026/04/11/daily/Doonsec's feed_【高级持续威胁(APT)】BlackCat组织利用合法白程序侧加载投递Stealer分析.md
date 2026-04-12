---
title: 【高级持续威胁(APT)】BlackCat组织利用合法白程序侧加载投递Stealer分析
url: https://mp.weixin.qq.com/s/2fFVA0KOZDe3Zbwb_qdOwQ
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:45:24.753430
---

# 【高级持续威胁(APT)】BlackCat组织利用合法白程序侧加载投递Stealer分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/APc6NwjLsxT03IjDQomhVIQicI1IGeBiboIF1VqjBFia9dMRtCicOd81eB4HribKjPcXBQPZ2VsSCTicHqibicyWoTrXnjZ4Co41HbpEpwC95h2zRN0/0?wx_fmt=jpeg)

# 【高级持续威胁(APT)】BlackCat组织利用合法白程序侧加载投递Stealer分析

深瞻情报实验室
深瞻情报实验室

深信服千里目安全技术中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxSEwPRojnAFN7VPYv5yibAb9ItouhRdnsC8DibsjN3vFkKRbibwFGAFMclumKxdujibicX92yCEQ7dyJx3OeZibgibZdpvMhmX1JWXJPk/640?wx_fmt=gif&from=appmsg)

近期，深信服深瞻情报实验室捕获到一起利用合法白程序（M9OLUM4P.exe，原文件名为wisdom\_class.exe）实施的恶意活动。攻击者“Black Cat”团伙利用DLL侧加载技术，将恶意侧加载模块伪装成合法的 libcef.dll 并放置在同级目录下，从而绕过安全产品的检测。这一手法常被运用于供应链攻击和针对特定目标的隐蔽驻留。

经过关联分析发现，该团伙常通过伪造如Notepad++等日常办公和开发使用软件的安装包，利用粗放的搜索引擎关键词广告散播上述带有 libcef.dll 劫持模块的污染压缩文件。这种手段既涵盖了传统水坑攻击特征，也包含了针对个人与企业开发者群体供应链进行潜藏与后门植入的安全危害。

本次捕获的样本采用多层RC4加密混淆保护核心攻击载荷，并在内存中进行反射加载执行。攻击模块成功运行后，会执行记录键盘输入、窃取剪切板数据以及浏览器用户数据等窃密操作，随后连接 xumeno.com 和 sbido.com 等恶意域名，实施数据外发。

**攻击时间线**

|  |  |  |
| --- | --- | --- |
| 时间 | 阶段 | 事件描述 |
| 攻击初期 | 初始访问 | 攻击者通过恶意搜索优化（SEO）等方式，在搜索引擎前列投递多款常用软件（如Notepad++、Clash、WinSCP、Obsidian）的仿冒钓鱼网站（如 cn-notepadplusplus.com）。用户访问并在伪造的下载页面下载了被植入恶意组件的安装包。 |
| 攻击中期 | 载荷投递 | 攻击者在用户环境中释放了包含合法白程序（M9OLUM4P.exe）、恶意动态链接库（libcef.dll）、密钥分片（.AD1AE）以及加密负载（.1CCE）的完整文件夹。 |
| 攻击中后期 | 恶意执行 | 进程启动时自动加载了同目录下的恶意 libcef.dll。该模块通过多重解密在内存中反射加载真正的载荷。 |
| 攻击后期 | 持久化 | 恶意模块在注册表的 Run 键下写入自启动项，指向白程序，从而实现隐蔽的自启动驻留。 |
| 攻击完成 | 数据窃取 | 核心窃密功能启动，并隐蔽连接 C2 服务器实施数据窃取，硬编码端口为2869。 |

**样本列表**

|  |  |  |  |
| --- | --- | --- | --- |
| SHA256 | 文件名 | 类型 | C2/域 |
| 82b157e33335e0cb07f6fe24d36e9020f9c26f37e60170234efc007eb30181b8 | M9OLUM4P.exe | 合法白程序 | \ |
| 3efc5829a243a5ee78ba56b94530c32eec152c40b22491fa77257b0c23a38c9f | libcef.dll | 恶意侧加载模块 | xumeno.com, sbido.com |

**样本分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxR0wFkbWhjTzXklu9Ad7e90nEan5B3zZNmycLBibclX3wQeendnhk606t1B66os1ibROLeWhJSqXyWQqGmXGoQibcEKpy7jv6uwp8/640?wx_fmt=gif&from=appmsg)

**文件基本信息**

|  |  |
| --- | --- |
| 描述 | 详细信息 |
| M9OLUM4P.exe | 为wisdom\_class.exe白文件 (x86架构)，主要被用作侧加载的合法宿主。 |
| libcef.dll | Delphi编写，采用了RC4算法强加密保护，包含劫持导出函数。大小约 3.5 MB。编译时间为2025-09-08 14:53:41。 |
| M9OLUM4P.AD1AE | 密钥分片 |
| M9OLUM4P.1CCE | 包含被强加密的内容，解密后为核心负载PE镜像。 |

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxR9ibNceXH78BGvsfROnPdBNWWKwWD9Ln5VqGp7ZUHe22G1b7MEsAicsHtLTtkOTYeWicXJkF56pQjTLAxa1ibjj6FD0iaxDTN73ZbY/640?wx_fmt=gif&from=appmsg)

**攻击流程分析**

攻击者利用DLL加载机制的漏洞，将恶意的 libcef.dll 放置于存在漏洞的合法程序所在的同一目录下。当受到触发执行合法的 M9OLUM4P.exe 时，系统优先加载了同目录的恶意DLL。

恶意DLL运行后，读取本地目录中的 `.AD1AE` 密钥文件与 `.1CCE` 加密载荷。在经历了两阶段RC4解密后，恢复出在内存中的载荷，并直接通过反射式注入加载至当前合法进程内存空间之中，最后跳转执行。

攻击链特征呈现为：

1. 受害者下载仿冒安装包后点击运行，此时会执行带有数字签名的白程序M9OLUM4P.exe。
2. M9OLUM4P.exe 错误加载同级目录下的恶意修改版 libcef.dll 模块。
3. libcef.dll 内部劫持了关键导出函数 cef\_string\_wide\_set，激活解密。
4. 解密还原在内存中的载荷，并启动反射加载跳转至标记为 6AD1 的入口位置。
5. 与外部恶意控制端开展通信并在本机注册表中建立持久化自启动项。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxSd5dicAMoDazsAUwR9MhdLFhHhRjl8mEyIuUmRZqwvBEB0V0h0nlfpiaBhcNfExUg8sTyEU3kXcoyZoDjf0jRaY0ZdW0vSRwicvs/640?wx_fmt=gif&from=appmsg)

**技术细节**

由于 M9OLUM4P.exe 预期会调用 libcef.dll 的标准导出函数，攻击者在劫持 DLL 中针对特定的接口进行了重新实现，如 cef\_string\_wide\_set。

关键触发代码逻辑如下：

![](https://mmbiz.qpic.cn/mmbiz_png/APc6NwjLsxSp8tXJ12SfGHehaXSQzRdS1sicpojmQOj7kmOoy1icz0IKaYxrawUFHdWiaVmdsiaWfM5aWKHp0GzD6sSJtgrGgMcJqYnuGVCtM9Y/640?wx_fmt=png&from=appmsg)

在这个入口点中，侧加载模块动态获取了后缀为 .AD1AE 密钥分片的路径。接着它调用了加密密钥衍生函数，进行第一阶段衍生解密密匙。如果验证其衍生结果匹配目标条件（如 AC826AD1AE1CCEC22），这部分程序代码才会继续解密出最终的 .1CCE 负载。

同时，针对代码防护，其中包含了经过变形的RC4加解密循环结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/APc6NwjLsxRicOQ4Z6aZGeVpdk5QcSnsmxcmoCANwp8Q3AO2jias64g2Kn67MBu57icnibzyap4OfqJdzDnUEWXSXFv6v2PZuibC10R4JhmZ0w64/640?wx_fmt=png&from=appmsg)

分析解密后的文件，程序首先会进入加密负载的AED55A700AC826AD1AE1CCEC2260AEF0427A8273E864FB7BD96020C51F6AD1函数，首先创建互斥体GREAD1AE1CCEC2260AEF02cNC5lZG5来保证单例运行。从注册表HKEY\_CURRENT\_USER\Software\\FEm9tGRY5读取查看是否存在相关配置：

InjectProcess：进程注入
OffKeyLog：关闭键盘记录
CopyUSBDeviceFiles：复制USB文件
ShareExclusive：独占共享
ReplaceClipboard：替换剪贴板
MonitorAPI：监控API

![](https://mmbiz.qpic.cn/sz_mmbiz_png/APc6NwjLsxTBBeJ2OVLWGRLXEXfNOCESwct6Ysw7zjOSkLRE4gnaDWKSaTY52hE5ueBWO33ueuXv7KGDK5KibjNLV5kMkB44XdjicRGFcodLc/640?wx_fmt=png&from=appmsg)

键盘记录器位于sub\_2FE2478，使用 SetWindowsHookExW 设置 WH\_KEYBOARD\_LL (id 13) 钩子。钩子回调函数 sub\_2FE1FF4 负责：调用 GetKeyNameTextW 获取特殊按键名称（如 "Space", "Enter"），使用 ToUnicodeEx 将按键转换为对应的 Unicode 字符。触发额外的日志记录或屏幕截图，将捕获的内容保存到 \\klogs 目录下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/APc6NwjLsxTELpJk5ZNraFpuN8NuolH4kloJG8qRBHdeyEUYcGOMkbicPBrHeznYoY0PgZhibo2eFTDBON8TqW1qia8ANOJPWEQQv3QkVpkicSM/640?wx_fmt=png&from=appmsg)

进程注入位于sub\_3110ac8，其首先通过互斥体检查进程是否存在，然后动态解析 kernel32 和 user32 的函数地址。核心逻辑位于其调用的sub\_3110284函数，使用 CreateRemoteThread 在目标进程中执行代码，通过 sub\_3110248 分配内存并写入 shellcode，支持通过 ReadProcessMemory 从目标进程读取返回的数据（用于信息抓取）。

![](https://mmbiz.qpic.cn/mmbiz_png/APc6NwjLsxQDaHC7wboAbbsZwGKO9DIZYrws2ic6hUzSibIUjHJG2D9zYd2dBMJqMQVxLRIqfQWI7KaoTk6Hh1icjswPK1SNumuqIDxib5KSjFg/640?wx_fmt=png&from=appmsg)

图中配置用于存储窃密数据内容，其中USB文件窃取 位于sub\_31146E4，它会递归遍历 USB 驱动器中的所有目录和文件，忽略大于 100MB (104857600 字节) 的文件。使用 CopyFileW 将文件静默复制到本地的 \\usbfiles 目录：

\\klogs：保存按键记录日志。
\\slogs：保存屏幕截图。
\\plugs：存储插件组件。
\\usbfiles：存储从 USB 设备窃取的、小于 100MB 的文件。
\\MnemonicWord：存储窃取的加密货币助记词。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/APc6NwjLsxSCBNnZPRLcvOR4djusLf9CiaUf2yIYXYFQSezaBZYnnCFHBOaFP75bFS2aI1ic5frHIo4TC1iaAmt0hZXiaC3jbfDzLqibcwickQWO8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxQXj8SB793fT9EuAeebIdQZhFnw162icTTG6AIp6VGDhv7XEvxzeSp8kJ3grV1eZuFXKrtOg86iaI8qdRrbalnDdlfiaTaMuHT4tM/640?wx_fmt=gif&from=appmsg)

**持久化机制**

经分析，该样本采用多层级的持久化策略以确保在系统重启后启动运行。首先，恶意组件向 HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run 中注册了名为 M9OLUM4PM9OLUM4P 的键值，并将其直接指向在本地存放的合法程序 M9OLUM4P.exe 的完整执行路径。从而利用受信任的高级宿主程序的执行身份达成长期的持久化存续目标。

![](https://mmbiz.qpic.cn/mmbiz_png/APc6NwjLsxS1IEurnmpfohwf5DtDsskS2AN6DwBs2qPs2IYmz8DFecib6StiaT5zmXQXPvxCicDobGuWF1Wibh168icImfykN5ZEaRz3rw5wvwZo/640?wx_fmt=png&from=appmsg)

通过设置 Environment 注册表中的 UserInitMprLogonScript 变量，在用户登录时自动执行脚本或程序。

![](https://mmbiz.qpic.cn/mmbiz_png/APc6NwjLsxRwk8YU8j6cqFpsZRghH2iaxicM6FgnZhkQNsxOJczCZZgyuu7aLLrhuo1sc5p77HYogD8TRqxeMkoFhWEFTSvePRPMZn2exozias/640?wx_fmt=png&from=appmsg)

通过 sub\_2FBB4FC 调用 CreateServiceW，将自身安装为 Windows 服务。

![](https://mmbiz.qpic.cn/mmbiz_png/APc6NwjLsxSiatRoablzJYpdCrNyCLbQreafGmM1nkJvqjlVqhu46EZiaoUW962Uku1slQzicUJX44ySiaRRmyp7uQv4fTo5bQHic9CntBGU9K6s/640?wx_fmt=png&from=appmsg)

除此之外，样本还表现出了对Telegram客户端的特别关注，通过搜索 Telegram.lnk 和 Telegram.exe，利用 sub\_2FCDAF4 函数修改快捷方式或劫持执行路径。这利用了用户频繁打开常用软件的习惯来触发木马运行。sub\_2FD5C64 线程作为“看门狗”，通过 FindFirstFileW/FindNextFileW 持续扫描文件系统和注册表。如果发现持久化项丢失，会立即尝试重新植入，实现自我修复。

其持久化设计非常成熟，结合了系统级服务、用户级环境劫持以及常用软件劫持。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxR6bwicTWSmR76KOLGuU4EicURCT6UBBLtKnNMVyibQp0b9EfKE0k52b4iaJ1hyeibQRv3NIm2tPoYN5pF4pI7mDibicliczH1cwdPm3us/640?wx_fmt=gif&from=appmsg)

**C2通信**

恶意模块成功注入合法进程后，它会优先从注册表 HKCU\Software\FEm9tGRY5\ConnectIp 读取经过 XOR 加密的 C2 地址，如果注册表为空，则会向 xumeno.com 以及 sbido.com 的2869端口进行连接尝试，对外发送其窃取的敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/APc6NwjLsxT3xjvibMTjKfR78SAXYHj7MtSMSARw3CzmXxBHjBJicwjKKCPWVicN0hJZwFr6zAtWibbUXAmV6jQ3tBEU2kNXfF2g2CTE6zGTmR0/640?wx_fmt=png&from=appmsg)

连接逻辑位于sub\_3167FA0，成功建立连接后，会进入sub\_31595AC 这个庞大的状态机函数，该函数包含超过 270 个分支，是本样本的核心部分，定义了其所有的攻击能力。

**关联分析**

本部分内容来源于CNCERT所发布的《关于“黑猫”团伙利用搜索引擎传播仿冒Notepad++下载远控后门的风险提示》，同时结合域名和攻击手法可将本次恶意攻击活动归因于“黑猫”黑产团伙。该团伙的最早攻击活动能追溯至2022年，是一个以窃密远控为主要目标的黑产团伙。

2023年：该团伙通过仿冒AICoin（虚拟货币行情交易平台）虚假下载网站，窃取了价值不低于16万美金的虚拟货币。
2024年：通过SEO技术在Bing搜索引擎投递了仿冒Chrome浏览器钓鱼页面，释放窃密及挖矿程序。
2025年：利用国内某知名搜索引擎投递了QQ国际版、爱思助手等软件的仿冒程序。近期进一步利用搜索引擎SEO技术推广 Notepad++、Clash、WinSCP、Obsidian 等常用工具的仿冒网站，向普通网民人群大规模扩散。

在2025年12月，“黑猫”黑产团伙通过此类木马投放导致境内约27.78万台主机被控，境内日上线肉鸡数量最高达6.2万余台。该类型木马属于“黑猫”独有自研的窃密木马，尚未在其他黑产团伙活动中出现。

**总结**

该次攻击综合了SEO投毒诱导用户下载仿冒程序、“白加黑”攻击、多重加密规避及无文件内存执行（反射加载）。

防御处置上，可以通过以下手段进行针对性监测与拦截（仅供参考，不构成任何专业建议或服务）：

1. 加强系统白名单签名审查：关注易引起DLL加载欺骗的常见名字如 libcef.dll 等文件，如果这些文件不具备可信发布者数字签名，应产生拦截告警。

2. 隔离与清除已知恶意网络C2：针对已明确的控制节点采取企业网络的 DNS 策略。并更新相应入侵防御体系中的特征码匹配规则库。

**IOCs**

xumeno.com
sbido.com
3efc5829a243a5ee78ba...