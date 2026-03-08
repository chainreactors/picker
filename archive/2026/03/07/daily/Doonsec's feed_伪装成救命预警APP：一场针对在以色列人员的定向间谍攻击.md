---
title: 伪装成救命预警APP：一场针对在以色列人员的定向间谍攻击
url: https://mp.weixin.qq.com/s/Q2OgpGDrq6hlyIRIWeiTXA
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:03:49.871032
---

# 伪装成救命预警APP：一场针对在以色列人员的定向间谍攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpcWicGz3r2FhtPZcknric3Y6X9viaogKcNxUyYu2QGuCGUicdYZkwvgoh3XDScvG1AAk1ibkewr3SNCUJDUSH4ZGeplOuJBGjNmLCI/0?wx_fmt=jpeg)

# 伪装成救命预警APP：一场针对在以色列人员的定向间谍攻击

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

随着中东冲突升级，境外安全机构披露了一起定向针对以色列用户的移动间谍软件攻击活动。

攻击者伪装以色列官方本土前线司令部，通过仿冒官方预警服务的短信，向目标分发植入木马的 “红色预警” 火箭预警安卓应用（Red Alert rocket warning system），正版包名是com.red.alert。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpAtDFQekibmDMCz5wahAgiaTnVYLaTMYicYpQLc7wHvH2BK7SUS4LKGemHHiaxMhvs2Fw4Vf1c0eCM1HW9Oib6bWcssuJKksg85KbE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpTWHA1XDMYBdwZbcwarpKH5r4LmdgKicJHuoZ867mUYXciamrpeJk2l7ibCaKAXzqHh62akoQkkgEz9dDbBpNJK3ibRPJibMWHje0c/640?wx_fmt=png&from=appmsg)

Red Alert（希伯来名צבע אדום，音译 Tzeva Adom）是以色列境内普及率最高、民众最依赖的民用火箭弹与紧急安全事件预警移动应用，也是地缘冲突背景下，以色列民众日常避险的核心工具之一。

## 核心功能如下：

### 1. 核心实时预警能力

* 覆盖多类安全威胁预警，核心为火箭弹袭击（Tzeva Adom 红色代码预警），同时支持敌对飞行器入侵、恐怖分子渗透等紧急事件的实时推送；
* 依托专用通知服务器，预警推送速度可与以色列官方公共防空警报同步，甚至提前触发，为用户争取避险时间；
* 警报触发时，会同步显示弹着预估倒计时（精确到秒），明确告知用户剩余的避险窗口，这也是其相比公共广播警报的核心优势之一。

### 2. 精准化个性化预警设置

* 双模式预警推送：支持基于 GPS 的实时位置预警，用户移动过程中也能自动接收所在区域的警报；也可手动搜索、选定关注的城市 / 区域，仅接收指定范围的预警通知；
* 可设置多个关注区域，并为不同区域配置差异化的提示音，区分核心居住地与其他关注区域的警报；
* 支持静默模式强制唤醒，即使手机处于静音、震动状态，也会强行播放警报音，最大程度避免用户错过紧急预警。

### 3. 配套应急与实用功能

* 警报历史记录：可查看过往所有警报的触发位置、时间，支持按本地时间适配查看；
* 连通性自检：内置 “self-test” 功能，可随时验证设备能否正常接收预警推送，避免因网络、权限问题错过警报；
* 音频自定义：提供 15 种预设警报音，同时支持用户自定义铃声，适配不同使用场景；
* 一键报平安：内置 “I'm safe” 功能，警报触发后可快速向亲友发送安全状态，降低战时失联焦虑；

该恶意程序在完整保留官方火箭预警功能的同时，会在后台秘密窃取用户敏感数据，是一起典型的、利用地缘冲突与公众对紧急服务信任实施的定向间谍攻击。

1. 攻击以仿冒以色列本土前线司令部的短信为载体，向以色列用户推送木马化的 “红警” 火箭预警安卓应用，利用冲突时期公众对预警服务的迫切需求实施钓鱼欺诈。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqibEmy9HhJsrVlnaGglJEA9A1RU4gqQoIPaLK29xt4PT4IPSYasahZP1vWeFaPjcdic0Lnw4jegjxdCN9RtQS9m9tGTNDJaxFF4/640?wx_fmt=jpeg)
2. 恶意应用完整保留了正版火箭预警的全部功能，表面运行完全合规，同时在后台静默执行恶意代码，极具迷惑性。
3. 攻击者通过证书伪造、运行时操控技术绕过安卓安全校验，让恶意应用伪装成拥有合法签名、来自谷歌官方应用商店的正规程序。
4. 恶意软件可窃取用户短信、联系人、实时位置、设备账户信息、已安装应用列表等核心敏感数据，并持续回传至攻击者控制的远程命令与控制（C2）服务器。
5. 该攻击凸显了地缘紧张时期，公众信任的紧急服务极易被武器化，攻击者结合社会工程学与移动间谍技术，可大幅提升攻击成功率。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqIqJUiaDbic5PJoInHagcSCIyicibFSKwcfmFPIRdrFEkXTR8OPooexcA7aVVf8xT8S8wjV8ypLwjj2kV9fZ8HRXClj4ZFpdzITV8/640?wx_fmt=png&from=appmsg)

2026 年 3 月 1 日这起攻击活动被发现，同期以色列民众也在社交媒体上集中反馈收到了相关诈骗短信。

本次攻击仿冒的 “红警”（צבע אדום）应用，是以色列数百万民众日常使用的官方火箭、导弹实时预警程序。在冲突持续的背景下，用户对这类预警应用的安装、更新需求极为迫切，极易放松安全警惕，尤其是当推送信息看起来来自以色列官方本土前线司令部（פיקוד העורף）时，用户的信任度会大幅提升。

接收通知时的错误已解决。请尽快更新到新版本

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqDTOwRibWDNpibhutwb5RQCmICX2dOBCKgNnGR8lWt9qCGib822VK6ez0HXhT5zOGDQ0N0RKJ5LjjghkchmaXtUgpQycYkyV5GaE/640?wx_fmt=png&from=appmsg)

从攻击溯源来看，同类攻击早有先例。2023 年 10 月，黑客组织 AnonGhost 就发起过仿冒该应用的木马攻击，本次攻击与其存在部分技术特征重叠，但使用了全新的攻击基础设施与部分代码。

本次攻击的入口是仿冒官方 “Oref Alert” 火箭预警服务的短信。攻击者通过伪造发件人 ID，向以色列用户发送短信，谎称预警系统出现故障，要求收件人立即安装应用的 “更新版本”。短信内包含 bit.ly 短链接，会将受害者重定向至恶意 APK 的下载地址，诱导用户绕过官方应用商店，手动侧载（Sideload，即非官方渠道手动安装）木马化的安装包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrrLk8Ch7RwoIAXgkpWnWc9pJn8vZf9doU2c4TJY5GRHlFB2ADwia723M6206UJpSHlOEAcaHhrN8gXpmAYnszkicEWGlGbpUNfA/640?wx_fmt=png&from=appmsg)

### 2. 恶意样本基础信息

本次攻击的核心恶意样本信息如下，可作为失陷排查的核心指标：

* 应用名称：RedAlert.apk
* 安装包名：com.red.alertx
* SHA256 哈希值：

  83651b0589665b112687f0858bfe2832ca317ba75e700c91ac34025ee6578b72

###

该恶意应用采用了双阶段运行架构，同时兼具加载器与间谍软件双重功能，也是其能完美隐匿恶意行为的核心原因。

#### 第一阶段：签名伪造与系统信任绕过

####

恶意软件通过动态代理技术，hook 了安卓系统的 IPackageManager 服务，通过反射访问 ActivityThread，将系统原生的 sPackageManager 字段替换为攻击者构造的代理对象。这一操作可以拦截系统对应用信息的查询请求，修改返回数据 —— 当系统校验应用签名时，加载器会将伪造的签名返回给系统，让恶意安装包 com.red.alertx 伪装成正版应用。

同时，伪造用的证书以 Base64 格式硬编码在代码中，通过 FakeSignatureProvider 类适配了新旧不同版本的安卓签名校验机制，确保在各类安卓版本上都能绕过签名验证。除此之外，加载器还会伪造应用的安装来源，强制让系统查询安装来源时返回 com.android.vending，让应用看起来是从谷歌官方应用商店安装的，进一步降低用户与系统的警惕性。

#### 第二阶段：正版应用加载与恶意代码隐匿

####

在完成信任绕过之后，加载器会从 APK 的 assets 文件夹中提取名为 umgdn 的正版应用文件，写入到应用的私有目录 /data/user/0/com.red.alertx/files/ 下。随后，加载器会修改 ActivityThread 中的 mAppDir、sourceDir、publicSourceDir 等安卓运行时核心字段，强制安卓系统执行提取出来的正版应用，而非用户看到的木马安装包。

这一设计的狡猾之处在于：用户打开应用时，看到的、使用的是完全正常、功能完整的正版火箭预警应用，能正常接收实时预警通知；而恶意的间谍软件组件，则完全隐匿在后台静默运行，用户几乎无法察觉异常。

该间谍软件的核心逻辑是：一旦用户授予对应权限，立即触发对应的数据窃取操作，无任何延迟，具体核心能力如下：

**信内容全量窃取**

当用户授予短信读取权限后，恶意软件会立即通过 Telephony.Sms.CONTENT\_URI 接口，读取设备内的全部短信数据库，完整窃取所有短信内容，包括银行交易通知、一次性验证码、私人通讯信息等核心高价值数据。

通讯录信息深度采集

当用户授予通讯录读取权限后，恶意软件会立即访问 ContactsContract.Contacts.CONTENT\_URI 接口，读取设备内的所有联系人条目，不仅包含联系人姓名，还会通过配套接口提取对应的手机号、邮箱地址等关联信息，构建完整的联系人数据集。

实时位置追踪与地理围栏

触发恶意软件可获取设备的精准 GPS 定位信息，不仅会采集并回传用户的实时位置，还会计算用户当前位置与预设目标区域的距离，仅当用户处于指定范围之内时，才会触发后续的恶意操作，实现基于地理位置的定向攻击。

**设备账户信息批量窃取**

恶意软件通过 Java 反射技术，动态调用安卓 AccountManager 类的内部方法，在绕过静态分析的同时，批量获取设备上注册的所有账户信息，包括谷歌账户、邮箱账户、各类社交与服务应用的绑定账户，为后续的账户入侵提供支撑。

**已安装应用全量枚举与用户画像**

恶意软件会通过系统 PackageManager 服务，获取设备上安装的所有应用列表，为每一个应用构建结构化的 JSON 数据，以 200 个为一批次回传至攻击者服务器。这一行为可让攻击者完整掌握受害者的设备使用环境，识别安全工具、金融应用、社交软件等高价值目标，制定后续的精准攻击方案。

为了对抗安全分析与逆向工程，该恶意应用采用了多层混淆与编码技术：

* 代码中绝大多数字符串常量都经过 Base64 编码，同时使用唯一的 32 字节 XOR 密钥进行加密，仅在运行时解密，安全分析人员无法直接从代码中提取 C2 地址、恶意行为标识等关键信息；
* 代码中的类名、方法名被全部替换为随机无意义的字符，同时插入大量无用的包装函数，混淆真实的代码执行流程，大幅提升逆向分析的难度。

##

恶意软件的 C2 服务器地址硬编码在代码中，经过了 Base64+XOR 多层加密保护，运行时解密后得到的核心数据回传地址为：`hxxps://api[.]ra-backup[.]com/analytics/submit[.]php`，所有窃取的用户数据都会被持续传输至该地址。

经溯源，核心域名 ra-backup [.] com 于 2025 年 6 月通过 Namecheap 注册，是专门为本次攻击搭建的全新一次性基础设施，这也是定向攻击中常用的 disposable C2 域名模式。

目前该 C2 地址的访问返回 404 状态码，推测该服务要么设置了严格的请求头校验，仅接收来自恶意样本的合法请求，要么已经被关停。

基于目前已有的攻击特征、目标定向、技术手法等证据，评估，本次攻击大概率与双尾蝎(Arid Viper,也被称为 APT-C-23）组织相关。

本次攻击事件，是一起典型的利用地缘冲突与公众对紧急服务信任的定向网络间谍活动。攻击者将间谍软件嵌入功能完整的官方预警应用中，在最大程度保留用户信任、规避用户察觉的同时，实现了对受害者敏感数据的秘密窃取。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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