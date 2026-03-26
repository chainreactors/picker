---
title: THE CAR HACKER’S HANDBOOK 解读第一章
url: https://mp.weixin.qq.com/s/nM3hM0hbw403ynrYm3IChg
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:28:17.659914
---

# THE CAR HACKER’S HANDBOOK 解读第一章

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/94kIPh1QgiaB2ZkvBfeeefS1Sibc6yx5kjEiaLpPIkwAEr5d53BgWplROh1icLStIH2xTuwCXTILydLvIaFkq7h1mIMpfshAvIVRgx3MF9jRqibQ/0?wx_fmt=jpeg)

# THE CAR HACKER’S HANDBOOK 解读第一章

原创

朝阳
朝阳

Sec朝阳

![]()

在小说阅读器中沉浸阅读

目录：

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaAVsPRbcibMB9mgsjRDOJqw7ovvCGVYCD2UbMTGGhv4GFWuNpKO0LCwojkOZZVatzkIHYics4eDibSXVDrLhbtOAVl0psDnXUpEOs/640?wx_fmt=png&from=appmsg)

# 第一章

理解威胁模型教你如何评估车辆，将学会如何识别风险最高的区域。

# 1、寻找攻击面

在评估车辆的供给面时，可以把自己想象一个邪恶的间谍，试图对车辆做坏事。为了发现车辆安全的弱点，评估车辆周边，并记录车辆环境。一定要考虑所有数据进入车辆的方式，这些包括车辆与外界通信的所有方式。

在检查车辆外观时，请问自己以下问题：接收到了哪些信号，无线电波、钥匙扣、距离传感器?有实体键盘访问吗？是否有触摸或动作传感器？如果车辆是电动的，如何充电？检查内部时有哪些音频输入选择：CD、USB、蓝牙？是否有诊断口，仪表板有哪些功能？GPS、蓝牙、互联网？

# 2、威胁建模

对汽车进行威胁建模时，你需要收集目标车辆架构的信息，并绘制图表来展示汽车各部件之间的通信方式。然后你用这些地图来识别高风险输入，并保持一份需要审计的清单，这会帮助到我们。

优先选择可能带来最大回报的切入点，威胁模型通常在产品开发和设计中建立，如果某公司有良好的开发生命周期，他会在产品开发开始时创建威胁模型，并在产品生命周期的推进过程中不断更新模型。

## 等级 0 ：鸟瞰图

在这个层级，我们用自己制定的检查表来考虑攻击面，想想数据是如何进入到车辆的，在中心画出车辆，然后标记外部和内部空间。

矩阵方框是输入，中心的圆圈代表整个车辆，在前往车辆的途中，输入会穿过两条虚线，代表外部和内部威胁。

车辆圆圈不代表输入，而是一个复杂的过程，细分为各个进程，并带有编号，这个编号是1.0。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaCib1LpKZRV21I4GbISTg7x4wCh887WqzzInfDFmOEUbIGtOCN4aQlNhz7uvZQFcu39icMa7kkfaJKN0r2oZBibks6jD85kRWRnmk/640?wx_fmt=png&from=appmsg)

## 等级 1 ：接收者

要进入第一层图，选择一个流程进行探索。因为图纸只有一个过程，我们就深入探讨载体过程，重点关注每个输入对应的内容。

图 1-2 中显示 1 级地图与 0 级地图几乎相同。唯一区别是我们指定接收 Level 0 输入的车辆连接。我们暂时不会深入分析，我们只关注输入与其通信的基本设备和区域。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaA2pmyIj0rpvia6sNVPjmOHFcf2KlnKYaHcXfVqel1fOCVJeLehiar120XXv6a5h2L9cpjaibwROoEBwxibo53AApB3ZcubE5S2HV8/640?wx_fmt=png&from=appmsg)

注意图 1-2 中我们为每个接收器编号。第一位数字代表 1-1 中 Level 0 图中的标签，第二位数字是接收端的编号。因为信息语了单元是一个复杂的过程，也是输入，我们给他设定一个流程圈。我们还有另外流程：防盗器、ECU 和 TPMS 接收器。

第一层地图上的虚线代表界限，图顶的输入最不值得信赖，底部的输入最受信任。通信渠道信任边界越多，风险越大。

## 等级 2 ：接收器故障

在第二层，我们考察车内的通信。示例图(图 1-3)聚焦于基于 Linux 的信息娱乐控制台，接收器 1.1。这是比较复杂的接收器之一，通常直接连接到车辆内部网络。

图 1-3 中，我们将通信信道分组为虚线框，再次表示信任边界。现在，信息语了控制台内部出现了一个新的信任边界，称为内核空间。

直接与内核通信和系统比系统应用通信的系统风险更高，因为它可以绕过信息娱乐单元上的任何访问控制机制。因此蜂窝信道风险高于 Wi-Fi 信道，因为他跨请求越过了信任边界进入到内核，而 Wi-Fi 信道则与用户空间中的 WPA 请求进程通信。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaAWfiac1nvwHB5BLENEr2yEBNiciaueHwYWm8TkZbKhsYRDtRpaWU3mvhXJc1sjc3jljU1lVVSrdk4uMUc7rhjGESLhoNntUFicGzc/640?wx_fmt=png&from=appmsg)

蜂窝(Cellulor)直接与内核通信。从此图中我们不难看出直接与内核通信的有蜂窝(Cellulor)、USB、ECU(电子元器单元)，威胁最高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCKWM4yNrkhe5dUTzfhWbRQkA1LsQ1noPmXoJmA9GU5ErKjzVMwZZRzNsF08iat69lFLouZgmPt3TA90ZpYK6LaQvPefv2wCjX8/640?wx_fmt=png&from=appmsg)

该系统基于 Linux 的车载信息娱乐系统(IVI),采用 Linux 环境中常见的部件。内核空间中，你会看到对内核模块 udev、HSI 和 Kvaser 的引用，这些模块接收来自我们的威胁模型的输入。udev 模块负责加载 USB 设备，HSI 是处理蜂窝通信的串口驱动，Kvaser 是车辆的网络驱动。

第二级编号模式为 X.X.X，识别系统与之前相同。在 0 级时，我们发现 1.0 的载具流程更深入地挖掘。然后我们将第一级内的所有进程标记为 1.1、1.2，以此类推。接下来，我们选择标有 1.1 的信息娱乐流程并进一步分解，形成了第二图层。因此，在第二层，我们将所有复杂进程标记为 1.1.1、1.1.2 等。

# 3、威胁识别

现在我们了解了两层威胁建模地图，可以开始识别潜在的威胁了。

## Level 0 :鸟瞰图

在 0 级时判断潜在威胁时，尽量保持高等级。有些模型可能看起来不现实，因为你知道还有额外的障碍和保护，但重要的是要将所有可能威胁纳入此表，即使其中一些已经被解决。这里重点就是想尽每个过程和投入的风险。

最危险的威胁包括攻击者可能：

远控车辆、关闭车辆、监视车辆乘员、解锁车辆、偷车、追踪车辆、障碍安全系统、在车辆上安装恶意软件。

## Level 1 :接收者

第一级威胁识别更侧重于每个部分的连接，而非直接连接到输入的连接。我们在这个层面假设的漏洞，与影响车辆设备连接方式的漏洞有关。

我们将这些分组分为威胁模型，分别涉及蜂窝网络、WiFi、钥匙扣(KES)、胎压监测传感器(TPMS)、信息娱乐控制台、USB、蓝牙和控制区域网络 (CAN) 总线连接。

## 蜂窝

攻击者可利用车辆的蜂窝网连接，从任何地方访问车内网络、利用信息娱乐单元中的应用处理来来电、通过信息娱乐单元访问用户身份模块(SIM)、使用蜂窝网远程连接诊断系统(OnStar)、窃听蜂窝通信、发出干扰求救信号、跟踪车辆行踪、建立一个虚假的全球移动通信系统(GSM)基站。

## WiFi

攻击者可能利用 Wi-Fi 连接进行以下攻击，从 300 码或更远距离访问车辆、寻找处理入侵连接软件的漏洞、在信息娱乐设备上注入恶意代码、破解 Wi-Fi 密码，设置假经销商接入点、欺骗车辆以为正在维修、拦截通过 Wi-Fi 网络的通信，追踪车辆。

## 钥匙扣

攻击者可利用钥匙扣发送错误的钥匙扣请求，使车辆的防盗器处于未知状态、主动探测防盗器以耗尽汽车电池、锁定车钥匙、在握手过程中捕获从防盗器泄露的密码信息、暴力破解钥匙扣算法、克隆钥匙扣、干扰要是遥控器的信号、耗尽钥匙扣的电源。

## 轮胎气压检测传感器

可利用 TPMS 连接进行向发动机控制单元(ECU)发送不可能的状态，引发故障并被利用、诱使 ECU 对伪装路况进行过度修正、将 TPMS 接收器或 ECU 置于无法恢复的状态，可能导致司机靠边停车检查爆胎，甚至车辆熄火，根据 TPMS 追踪车辆唯一 ID、伪造 TPMS 信号以触发内部报警。

## 信息娱乐控制台

将控制台调整模式、更改诊断设置、找到意外结果的输入错误、安装恶意软件、使用恶意应用访问内部 CAN 总线网络、使用恶意应用监听车辆乘员的操作、使用恶意应用伪造显示在用户面前的数据，如车辆位置。

## USB

可在信息娱乐单元安装恶意软件、利用信息娱乐单元 USB 协议栈的漏洞、连接专门设计我呢见的恶意 USB 设备，用于破坏信息娱乐单元的导入器，如通信录和 MP3 解码器、在车辆上安装修改过的更新软件、短路 USB 端口，从而破坏信息娱乐系统。

## 蓝牙

在信息娱乐单元上执行代码、利用信息娱乐单元蓝牙栈的缺陷、上传格式错误的信息、干扰蓝牙设备等。

## 控制器区域网络

向 CAN 总线连接并进行以下操作：安装恶意诊断设备向 CAN 总线发送数据包、直接插入 CAN 总线，尝试无密钥启动车辆、直接插入 CAN 总线上传恶意软件、安装恶意诊断设备以追踪车辆、安装恶意诊断设备，使得远程通信直接通过 CAN 总线，使原本内部攻击变外部威胁。

## Level 2 :接收器故障

在第二层，我们可以更多地讨论识别具体威胁，当我们精确处理哪个用于处理那条连接时，可以开始基于可能的威胁进行验证。

我们将威胁分为五类：Bluez(蓝牙守护进程)、wpa\_supplicant(Wi-Fi守护进程)、HSI(高速同步接口蜂窝内核模块)、udev(内核设备管理器)、Kvaser 驱动(CAN 收发驱动)。

## Bluez

较旧或未打补丁的 Bluez 守护进程、无法处理损坏的通讯录、未正确配置加密、无法配置并支持安全握手、默认密钥等。

## wpa\_supplicant

历史漏洞、无法强制执行 WPA2 式无线加密，可能连接到恶意接入点、通过 BSSID(网络接口) 泄露驱动信息。

## HSI

历史漏洞、可能收到串行通信(中间人)

## udev

旧版未打补丁、没有维护的设备白名单，允许攻击者加载未测试或未使用的额外驱动程序或 USB 设备、可能允许攻击者加载外部设备，如键盘以访问信息娱乐系统(IVI)。

## Kvaser Driver

旧版未打补丁、可能允许攻击者向 Kvaser 设备上传恶意固件。

# 4、威胁评级系统

在记录许多威胁后，我们现在可以用风险等级来评级，常见评级系统包括 DREAD、ASIL、MIL-STD-882E。

DREAD 常用于网络测试，汽车行业和政府分别用 ISO 26262 ASIL 和 MIL-STD-882E 作为威胁等级。

这是这一章总结内容，如下图所示，整体流程即为找接口、找设备、找驱动。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDr8YibXpTuqmnIdE8EXl3wAelTOdBISbkGPYCibPj22KWPNNIoyS92YgcR70RB1iagxdIlZe5xHIW6VBHVutjdUpicNE9v4hPBDRU/640?wx_fmt=png&from=appmsg)

# 术语解释

Infotainment/IVI 车载信息娱乐系统

Cellular 蜂窝网络

Key Fob 钥匙扣

TPMS 胎压检测系统

udev 设备管理器

Daemon 守护进程(如 Bluez 是蓝牙的后台)

HSI 高速同步接口

Kvaser Driver kvaser 驱动(CAN 适配器驱动)

此处省略DREAD 评级系统、包括第一章剩余内容。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT1rh31vZg2fMe2vyiarFdM38QmFs6j6WLf5Zfu9LJDicbib1e9j0N4OpgeCiaFPXzmXbElD1sdZM3AwHg/0?wx_fmt=png)

Sec朝阳

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HgEiaULLGWT1rh31vZg2fMe2vyiarFdM38QmFs6j6WLf5Zfu9LJDicbib1e9j0N4OpgeCiaFPXzmXbElD1sdZM3AwHg/0?wx_fmt=png)

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