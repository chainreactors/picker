---
title: 不拆闪存也能抽固件：BD Alaris 8015 输液泵的活体 JTAG
url: https://mp.weixin.qq.com/s/JtuHqVjED7ScaCPIDC6k7g
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:43:03.093104
---

# 不拆闪存也能抽固件：BD Alaris 8015 输液泵的活体 JTAG

# 不拆闪存也能抽固件：BD Alaris 8015 输液泵的活体 JTAG

原创

黑卷
黑卷

黑卷的IoT攻防日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以前要读 Alaris 8015 输液泵的固件，公开做法是把 NOR 闪存拆焊下来，外挂编程器硬读——板子废掉，也拿不到片上调试。NARF Industries 这次换了路子：顺着 12 层板的内层走线，把埋在内部连接器里的 JTAG 揪出来，用 Segger J-Link 把 PXA270 停在复位向量，整机 16MB 镜像直接 dump。

目标是 CareFusion / BD 的 Alaris 8015 PCU（Point of Care Unit）——医院里常见的大容量静脉输液泵控制单元，FDA 510(k) 过审的医疗设备。研究在 ARPA-H UPGRADE 项目下完成，目的很明确：拿到完整固件镜像，并摸清板上能做动态分析的调试口。

![四步：认芯片 → X 光找线 → 焊出线束 → 活体停机读固件](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84UOyVo6hticlsj81MVUF5cI7ezG6eWtUwJErAtwPVGgdFicTicKB0vGTAndIqXCxMIhia3Ubws9eyVY1LKj5f0f75YecsWXJy0Bp7E/640?from=appmsg)

研究用了多台物理样机，而且刻意把"破坏性操作"和"活体目标"拆开：闪存抽取在一台板上做，芯片盘点和 JTAG 连续性测试在第二台同款逻辑板上做，真正的活体 JTAG 起机则留给第三台还能正常开机的整机。这样即便拆球、焊飞线翻了车，也不会把唯一一台能跑的设备弄废——医疗设备研究里，这种分工几乎是标配。

## 一、先认芯片：三颗带 JTAG 的家伙

拆机后，在立体显微镜下把主要 IC 的丝印逐个读出来。跟这次研究直接相关的有五颗：

* **处理器**

  ：Intel PXA270C5C312（23×23 mm、360 球 PBGA）——XScale ARMv5TE 应用处理器
* **NOR 闪存**

  ：Intel 28F128J3（128 Mbit，BGA64）
* **SDRAM**

  ：Micron MT48LC16M16A2（256 Mbit）
* **带 PSD 的 MCU**

  ：ST uPSD3354DV-40U6（另一台样机上是 TI MSP430F5418A）
* **CPLD**

  ：Xilinx XCR3064XL-10VQ100

PXA 系列原本是 Intel 的，2006 年卖给了 Marvell，所以不同版本数据手册上的厂商名会跳来跳去——但球位没变。

![主处理器：Intel PXA270C5C312，360 球 BGA](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84UIxkicibibQUb5dUgcS5TxLJDI0Kg31IyFLqypEO5ucC4pwsfllMuG4Iq7fy4OjoCPnickvH9Bmic6gjKVjTEpEu3dB00A5VR08Pa0/640?from=appmsg)

![NOR 闪存 U23：Intel 28F128J3，128 Mbit](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84VYo2zBwmKOia4iaXRGvc3dFWgQTcpteLJv8sNmibwBnkx9WgGKgE3K4vxF0kfe8R5Sh2FlT1p7wLMyaEhqpKYlohCD1KhT6xMxwM/640?from=appmsg)

![Micron SDRAM：MT48LC16M16A2](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84UDXszpJ48ZibGZmTaib74XBqpJ488ALxueg10I8ibIqiadHeNDR5q9obIZd6kAsostIJWmNMwVAQLiajGuUJ2JFFTL8GM2ohez2nL4/640?from=appmsg)

![ST uPSD3354DV：自己也带一套 JTAG TAP](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VnibRQ3ziboZqPickqzmt1BZDKZDYpBe8aEnurx9HpNTItcybyCEibr1WngFEQqAR2ygAk9ntbvlCqX1biaoMnOkC4rUibeZvosAUicw/640?from=appmsg)

![Xilinx XCR3064XL CPLD：第三条 JTAG](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84V5Cswkax72E68E1cFWqxT3SQXpGO7LoFPjJkd9iab2y0s6fBYUK55BpJAQcvI7g9M9m5jdSv1sAJAs2ib6ouiaxiaPDNah24KibO60/640?from=appmsg)

这三颗——PXA270、uPSD、CPLD——各自都有独立的 JTAG TAP。接下来的问题只有一个：它们的调试线，最后接到了哪里？

值得一提的是，PXA270 这颗处理器本身已经算"古董"了——XScale 架构、360 球 BGA、年代感拉满。但在医疗设备里，一颗芯片一旦通过认证，往往会跟着产品线用上十几年。调试口的设计决策，也会跟着一起被"冻"在板子里。

## 二、12 层板埋线：X 光把 J1 揪出来

GTRI（佐治亚理工研究院）对这块 12 层逻辑板做了 X 光成像，结论很干净：三颗芯片的 JTAG 信号，全部汇到同一个内部 50 针板对板连接器——丝印 **J1**。这跟 Alaris 技术服务手册里 Figure 7-24 的描述对得上。内层走线用万用表根本跟不住，X 光是唯一现实的办法。

![GTRI 提供的 X 光图：JTAG 走线全部汇向内部连接器 J1](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84X8wMyW4YJDGMvTr5NHcv5srF7Yos3icB5NVwbAmbib7Q6B7VP1cBw5z3WcG5WhiakAZF0144t54ueW5gbAHL0mr7xJgWiaqwcJroo/640?from=appmsg)

为了把 X 光结论钉死，团队在一块备用板上做了连续性测试：把 PXA270 拆焊下来，让每个 JTAG 球位变成可直接戳的焊盘，再用万用表量到 J1。

![拆掉 PXA270 之后的 BGA 焊盘：右侧可见 75Ω 串阻 R81](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XgNQjcFLgKyXJ8QKneIRibOqD5hsz4pXDnk8eibM9Xsq2uCntoC7X9vS3VKCgUnuPb87y2rOyGe9kpRtF1Es7x3bGXqeqgdibABw/640?from=appmsg)

按数据手册，PXA270 的 JTAG 球在封装右下角：TCK=R19、TMS=R20、TDO=R21、TDI=R22、nTRST=T20。量出来的映射是：

* TDO → J1 右 7（经 75Ω 串阻 R81）
* nRESET → J1 右 8
* TCK → J1 右 9
* TMS → J1 右 10
* TDI → J1 右 11
* nTRST → J1 右 12

TDO 那条要特别当心：中间串了 R81，球到 J1 直量会显示"不通"，必须跨电阻两端量。uPSD 和 CPLD 的脚位同样被一一对上——三颗芯片各自独立一套 TCK/TMS/TDI/TDO，**没有 daisy-chain**。CPLD 还有个坑：PORT\_EN 脚量到对地 100Ω，手册要求它拉高才开 JTAG，而这根脚没露到 J1。

电源和地也在 J1 上对上了：右 1 是 VCC\_IN（3.3 V，实测 3.25 V），左 1 是机壳地。三颗芯片各自一套完整的 TCK/TMS/TDI/TDO，互不 daisy-chain——这意味着调试器要分别寻址，但也意味着你不会因为其中一颗 TAP 挂掉就把整条链拖死。

![关键数字：50 针 · 12 层 · 3 个 TAP · 16MB 明文](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84VHK8YyhO918icSKUX2F7d3FcL7fVFjq0icYXsXa1KZLBhQU6JjH0UK6TeqyZRwUZPNGQHzJvMibjCzqesalTt4OAib3I5mBtzibsbA/640?from=appmsg)

## 三、从 WiFi 子卡抠出同款连接器

J1 是内部连接器，市面上不好买配对件。团队直接从机器里紧挨着 J1 的 WiFi 子卡上，热风拆下一颗完全一样的 50 针座，把彩色飞线焊上去，做成飞线 breakout。

![拆掉后面板，露出内部逻辑板](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84U9Yd9SnJKic059vibpk7D0FhECRYhN4CApmYEQnNib2yibc2tdk0SC2KDuZibtjePddbPUcgtRSgQqgL9m7aozgMvMtWMSibictib36L8/640?from=appmsg)

![从 WiFi 子卡拆下来的同款 50 针座，焊上彩色飞线](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84UwUlXRuRpia4adTdz4VZibcme2YO9ge6EcUY5OcHiaZMIPJqqicib5uDYMAQohPibxB4KbMFbEKNoDXDcNU0Ddoy6TAHuTFoxwTU8VM/640?from=appmsg)

![逐根量通：细间距下最怕相邻脚短路](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84XADjd6992U8PGmOGl2bzQ7ianHezicfc3gNzLxBIn7fPUSl71UWJE7FZeLaKRTialgzMwAaewzB25ArsHxK7Q8b9g5miclRgvbIrw/640?from=appmsg)

![飞线座插回 J1，线束从机箱后部引出](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84W9ricCPCf1RT6BJIXIzsAwFRhlErVLYpiayKwwx0DInvIM1oFz3EAOaGaZXLCel0z2WWg6Ck7Lk0qCV9J1bs5Fd4iaXhKgA6vicA0/640?from=appmsg)

![线束从机箱后部引出，方便接外部调试器](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84X1SLufTEh1luvsv4L1sf8rAdB4UbklVsVWpT29jshC7gv3gZYGDaAqAIWsxxvMAKs5icO5EJiaLD6gHswMNDo6vwgW2H2JhSUnE/640?from=appmsg)

上正式调试器之前，先用 JTAGulator（3.3V）扫一遍 0–4 通道。扫出来的结果干净利落：

```
TDI: 2  TDO: 1  TCK: 4  TMS: 3 Device ID #1: 0x79265013
```

IDCODE `0x79265013` 解出来是 JEDEC 厂商 0x009（Intel）、部件 0x9265、版本 0x7——正是 OpenOCD 自带 `pxa270.cfg` 认的三个合法 IDCODE 之一（另外两个 `0x49265013` / `0x89265013` 对应不同硅步进）。四根信号一次扫齐、IDCODE 对得上——线束和脚位，确认无误。

细间距 50 针座最容易翻的车是相邻脚短路。团队在插回整机之前，用万用表把每根彩线到目标 J1 脚又量了一遍，确认没有桥接，才敢上电。

## 四、J-Link + OpenOCD：停在复位向量

飞线接到 Segger J-Link Pro V5（经通用 20 针 ARM 转接板）。有一个兼容性坑值得记：现在的 J-Link Commander 已经把 PXA 家族从设备库里删了，所以改用还留着 XScale 驱动的 **OpenOCD 0.12.0**：

```
adapter driver jlink transport select jtag adapter speed 1000 reset_config trst_and_srst srst_open_drain source [find target/pxa270.cfg]
```

跑起来后，在 4444 端口的 telnet 里丢一句 `reset init`，CPU 就停住了：

```
JTAG tap: pxa270.cpu tap/device found: 0x79265013 target halted in ARM state due to debug-request,     current mode: Supervisor cpsr: 0xd80000d3  pc: 0x00000000 MMU: disabled, D-Cache: disabled, I-Cache: disabled
```

PC = 0x00000000，MMU 和两级 Cache 全关——这是干净的复位向量停机，固件一行都还没跑。`pxa270.cfg` 里还把片内 SRAM（`0x5C000000`）配成了 work area，并设了 `adapter srst delay 260` / `jtag_ntrst_delay 250` 这套复位时序——这些细节看起来不起眼，但对老 XScale 目标往往是能不能稳定 halt 的关键。

从这个状态出发，一条 `dump_image flash_jtag.bin 0x00000000 0x1000000`，16MB 整机镜像就顺着 JTAG 吐出来了。不拆闪存、不破坏板子、设备还能再开机——这才是"活体调试"四个字的含金量。

![最终台架：J-Link Pro 经自制飞线连着一台能开机的 Alaris 8015](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84WxPZPlPqz1HFsXVBdLDBn2av12e3LViavGSJ7mZNEJICsrEZiaMIFkr4V3iaYyLzmn9cxwdjgXjUObMuycqibCpXb9QicbMprT2eoo/640?from=appmsg)

## 五、16MB 镜像长什么样

对 JTAG 抽出来的镜像做字符串、熵值、binwalk 签名和 ARM 异常向量表分析，布局大致如下。没有任何区域熵值超过 7.5——**固件没有加密**。

![16MB NOR 的分区布局：Bootloader / 日志 / FlashFX / 主应用](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84VQ2caWzFvZZpVoeUFIk7a0HG835TXvaiac0ZRPNTQaqCQV9v3uLm8Ribk6QTOBOictXjpVEJNdYJb9n6ow2Aibp7PjFT1jORDmO0E/640?from=appmsg)

* **Bootloader**

  （约 1.06 MB）：内部代号「Polo」（BSP）/「Tequila」（板级），提示符 `polo@tequila>`，版本 12.1.0.76（2019-12-08）。底座是 Enea OSE 5.1.0 + Interpeak 网络栈 + OpenSSL 0.9.7c。
* **日志区**

  约 3.75 MB；**FlashFX** 文件系统 1 MB。
* **主应用**

  （约 7.80 MB）：`Pcu1.5App` 12.1.3.6（2022-04-06），静态链接 ARM ELF，加载地址 `0xA0100000`，同样跑在 Enea OSE 上，OpenSSL 升到了 1.0.1g。

字符串里能摸到一整套协议痕迹：带 AES 的 DCMP、NCM / PTP 的 protobuf 引用、FTP / TFTP / Telnet，以及从 WEP 一路到 WPA2-EAP-TLS 的 WiFi 安全字串。第二台样机上是同一套 Polo bootloader，但 OSE 版本更老（4.5.2）——说明同一硬件平台上，软件栈也会随批次漂移，做动态分析时不能默认"所有机器都是同一个构建"。

到这一步，团队完成的是整条链路的奠基：从密封整机出发，认出主要硅片，用 X 光定位埋藏的 50 针调试口，拆球验证每一根 JTAG 线，自做飞线 harness，最后用 J-Link + OpenOCD 把 PXA270 停在复位向量，并直接读出完整固件。后续的漏洞挖掘和动态分析，都可以站在这个地基上继续往下挖。

![以前要拆焊 NOR；这次不破坏板子也能活体 halt](https://mmbiz.qpic.cn/mmbiz_png/JdicK53hX84VaCiaZ6iaib70eibhpfmUuib6wBROf0iapgaTAbiaZ3OGMpLpDhRLKUT3fjM4b6eI112Jh484JDrVCaUJlhXrEqfU87aux4DvdNbqNrU/640?from=appmsg)

## 黑卷点评

Alaris 8015 这一仗，打的不是"又挖出一个 0day"，而是把**医疗设备调试面**这件事钉得更清楚。

* **藏得深 ≠ 藏得住**

  。12 层板、内层走线、内部 50 针座——看起来已经够狠。但只要有人愿意做 X 光 + 拆球连续性测试，那条总线就会重新露出来。物理接触一旦成立，设计阶段埋线的成本就被一次性摊平。
* **破坏性抽闪存和活体 JTAG，能力差一个量级**

  。前者只能做静态分析；后者能把 CPU 停在复位向量，MMU 和 Cache 全关，等于把整机冻在"开机第一指令"——动态调试、内存改写、实时观察，全部打开。
* **固件不加密，是第二道本不该松的门**

  。16MB 镜像熵值不过 7.5，字符串、协议、版本号直接可读。调试口一旦被跟出来，后面几乎没有额外摩擦。

医疗设备的安全，常常卡在"调试口有没有真正关掉"，而不是"包装盒上印了多少合规徽章"。能救命的从来不是把连接器藏得更深，而是量产时熔断调试、加密闪存、把签名校验做到 boot 链上——让就算有人跟出每一根飞线，也读不出、改不进、跑不起来。
...