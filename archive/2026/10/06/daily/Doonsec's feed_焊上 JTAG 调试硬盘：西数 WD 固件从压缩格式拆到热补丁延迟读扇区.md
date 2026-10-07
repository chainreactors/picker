---
title: 焊上 JTAG 调试硬盘：西数 WD 固件从压缩格式拆到热补丁延迟读扇区
url: https://mp.weixin.qq.com/s/zdlco2p-pfbVZKyNI8Vemg
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:18.402407
---

# 焊上 JTAG 调试硬盘：西数 WD 固件从压缩格式拆到热补丁延迟读扇区

# 焊上 JTAG 调试硬盘：西数 WD 固件从压缩格式拆到热补丁延迟读扇区

原创

黑卷
黑卷

黑卷的IoT攻防日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 焊上 JTAG 调试硬盘：西数 WD 固件从压缩格式拆到热补丁延迟读扇区

去年我在做 Xbox 360 的一个漏洞利用（后来变成大家期待的 softmod）时，需要改一块硬盘的固件，去卡一个竞态条件。这事把我拖进了坑：手头几块 HDD / SSD，怎么 dump、分析、现场 JTAG 调试、改固件，一路摸过来。这篇是系列第一篇，只讲在**没有 AI 帮忙**的前提下，怎么把西数硬盘固件拆开、看懂、改掉。下一篇再说怎么用 AI 做同类活，以及黑盒推未知指令集。

## 背景

要打的洞是主机从硬盘读数据时的竞态：读请求发出去，到盘回包之间，需要卡出一段足够长的窗口，利用才能稳定触发。当时我对变量理解不够，盘回得太快，窗口不够用。第一反应就是改固件：读到某个特定扇区时，故意拖几百毫秒。

网上改硬盘固件的文章不少，但很少能拿来直接跑。概念不新，我只需要先搞通一块盘，把 Xbox 利用做完，再考虑扩到别的型号。后来竞态用别的办法调准了，其实**根本没必要改硬盘固件**——但这条旁支还是值得写下来。

从攻击和渗透测试角度看，改 HDD / SSD 固件很有意思。以前不愿碰，是因为嵌入式底下太复杂，逆向极吃时间。硬盘在微控制器层面到底怎么工作？盘片高速转、磁头读写，这种宏观说法人人都会；落到 MCU 上，多数人其实说不清。

我也不清楚。但我认定这个洞不能不打。挡在前面的如果是一块硬盘，那这块盘就得倒下。

## 试验对象

只要是容易买到、能改、能回刷的 HDD / SSD 都行。优先挑 Xbox 360 上常见的品牌（用利用的人多半手里就有一块），外加西数——以前碰过它们的后门厂商命令，能拿底层访问——再加两块手头的三星 SSD。受试对象如下：

![试验用硬盘与固态阵列](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84VzHp7ibic2TkaRnyQqoBoQ2WYibElhthKNxkicQiafA98vbnwn7HrLX3asxhxAhjkz4BC3yEZVoKko1EaZQOTUbiaRl5HHUQjJpJ6ic8/640?wx_fmt=jpeg&from=appmsg)

型号清单：

* Samsung HM020GI
* Hitachi HTS545032B9A300
* Western Digital WD3200BEVT
* Samsung PM871a

其中一块盘被「羞辱」得很彻底，是因为以前挂过坏的 USB 转接、又挂过坏的 SATA 口……盘本身其实是好的。

### 开干前先摸清路

先上网查这些型号：有没有固件 dump、有没有前人踩过的坑。HDD Guru 论坛上看了不少西数和日立的帖；还翻到 MalwareTech 改硬盘固件的系列，其中一句特别扎心：

> 动手前我决定先读别人的研究，找个切入点。资源很多对吧？结果发现，我拿来当基础的那些研究，要么是错的，要么根本对不上这块盘。

我的体验一模一样：大多是十五年前的论坛帖，错的或不适用。但碎片拼起来还是能成图。对每块盘的打法是：

* 搞到固件：网上找现成镜像，或自己从盘里 dump。
* 塞进 IDA 能分析：压缩、加密都得先拆掉。固件都看不了，后面谈不上改。
* 找到回刷改过的固件的路：板载 Flash 手工烧录，或标准 / 后门命令。写不回去，这块盘直接出局。
* 分析固件，找到处理读请求的代码。关心的是主机用的 `DMA READ EXT`。固件里多半有一张 ATA 命令处理表；找到表，就能摸到读命令处理函数，或至少有个起点。这步通常最难。
* 写补丁：读到指定扇区时插入几百毫秒延迟。
* 把改过的固件刷回盘。

## 拿到固件镜像

HDD Guru 上有人用 PC-3000（专业数据恢复设备，靠厂商私有命令诊断、修盘、dump 固件）上传过各种 dump。西数那块在论坛上找到了；发推后有人用手头的 PC-3000 帮我 dump 了 Samsung HM020GI。三星 PM871a 的固件在联想站上的升级工具里，一石二鸟：既有镜像，又能从工具里反出刷写命令。日立那块一直没找到固件，先搁着。

### 西数 WD

论坛上拼出镜像格式，再对着十六进制看了一会儿，结构大致是：

![固件镜像结构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XXs6nR1qyic4qicnCCbm1btAfNwYYUbteFy9TILMjDRnLkZvtMu66wrAhcKK5Ef7259M6GI2uWic68g8gYSlHQXb512nDfs0ybUg/640?wx_fmt=jpeg&from=appmsg)

很直白：扁平文件里一串静态基址的可执行 / 数据段，前面是段头；段头和数据块各自带 8 位累加校验。写了个 IDA loader 插件往里装，结果发现**除第一段外全部压缩**。论坛碎片里说过：第一段是 loader stub，给 MCU bootloader 解压并加载剩余段用的——但没人说压缩算法是什么。

先拿压缩块跑识别工具，没结果。于是把第一段当 ARM 逆向。很多 HDD / SSD 的 MCU 是 ARM，还经常多核；这块西数只有一个 ARM 核，省事不少。几分钟后标出了段加载循环和负责解压的函数：

![段加载函数反汇编](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84Vy2UBTM4rlIrqHQEJ0JqJSLYWTsNIKiaxUeicy0QjibyT61EwS2arMz4cQibOQVIej12dhl9JIkyGLJ3POtg09GvvK6NWOmHAwVjY/640?wx_fmt=jpeg&from=appmsg)

解压例程反完，写出可工作的重实现。算法是 **LZHUF**，但改过两处，所以识别工具认不出来：`N` 从 2048 改成 4096；run length 计算是减 `THRESHOLD` 而不是加：

![LZHUF 算法的改动示例](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VXlM8AL2Q8teGKjxmUTRiby45nrXlX88PVHF7RYadGRumNjuysTaVvAFS0XLYX7xGTMPQpa0SPoz9HYIGPsmeCuPMjOyXXAjgQ/640?wx_fmt=jpeg&from=appmsg)

更新 IDA loader 后，整包固件按正确基址加载完毕，可以开分析了。

### 三星 PM871a

联想站上的固件 + 升级工具是好策略：OEM 升级工具往往自带解密 / 去混淆，并负责刷写。三星 SSD 固件常被混淆，这块用的是从工具里抠出来的 bit fiddling：

这类工具能覆盖二十多种三星 SSD（外加一堆光驱），拿来扩面很值。去混淆后的镜像前几 KB 像元数据，再往后能看到疑似段描述符：

![两个固件文件对比](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84XdktsqnfmdXge0ibf7y8qjdmJ2TjHLjrmu7kaSCRXfiaOJer9icnIt0dYrSec3l96lib6vMrD9J4nibosySWWMm5esyJlD3vVmicsAo/640?wx_fmt=jpeg&from=appmsg)

![疑似段描述符的十六进制](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VqeMnSkvibIpewcso4Fibb4jqgW0ygCTNH556ucAecO19B6kfPVNI0Q9WMiaIdlUNyb8ejKOOtVj5ydvnDv4NU9m2DPgibkO011WM/640?wx_fmt=jpeg&from=appmsg)

红标字节很像代码 / 数据段的内存地址——和 ARM Cortex-M3 内存图也对得上：

![ARM Cortex-M3 内存图](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84W9AUvk4bek0wCdpTMEj0t4dfA8n9xrzQOicpn55DQ8p7KxmZM5h64T1DNHkpsJic9aiarwTOibqSqvfcABcO0knmofSVQQbLDib35w/640?wx_fmt=jpeg&from=appmsg)

再抠一会儿：各段偏移和大小按 16KB 块步进。又写了一个 IDA loader，整包加载完成。

前 28 字节那段长度很怪，可能是 SHA-224 或截断 SHA-256；对比两个同版本、不同形态（2.5" SATA vs M.2）的固件后，更像**没有强公钥签名**（RSA / ECDSA），但也不能完全排除局部签名——先放下。

### 三星 HM020GI

dump 里能看到明文串和像机器码的东西，但怎么都反汇编不出对应架构。整文件还像是按字翻转过：

![字节翻转后的固件数据](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84VicFicPyxlmNeUU6nA9p4RKP3XHSSia9jckrcJJT5d1vNPTeZibTE4szpiaNyunfnrTc8SgKsoQIXInyibLEeOje7wK3nBUX8MUDgxA/640?wx_fmt=jpeg&from=appmsg)

可能是极冷门 ISA，甚至是 MCU 里跑的自定义字节码。这篇先搁着，第二部分再回来。

## 怎么刷回改过的固件

后面只展开西数这块——花时间最多，也没必要把同样步骤在每块盘上重复三遍。其它盘在第二部分再各自讲独特点。

刷固件三条路：

* `DOWNLOAD MICROCODE`

  ATA 命令：最常见，现代盘升级多半走这条。
* 后门厂商命令：修盘 / 诊断，或主要靠盘片服务区 overlay 打补丁的型号。
* 板载串口：同样偏修盘 / 诊断。

### DOWNLOAD MICROCODE

主机和盘按 ATA 规范通信。`download microcode` 用来上传新代码：带上尺寸等寄存器，把固件流进去（分块或 DMA），盘可能校验后再写入非易失存储。成功就通断电；失败可能变砖——通常还能救，但要各种硬核手段，普通用户做不了。OEM 升级工具本质就是在走这条命令。

### 后门厂商命令

很多西数盘从不发完整固件升级，而是把新代码写到盘片**服务区**里的 overlay / module。服务区平时不可见，里面有型号 / 序列号、几何、SMART，以及启动时加载进内存的补丁代码。PC-3000 里能看到一长串 module：

![PC-3000 显示西数服务区模块](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Vw59iadgjGB1UM5NOYX0Ev1spoG0N5OkMCiaa8yicRckoySXYMhlDUXxHz8qms2DXicbDYUHRiaYfSArhJaaYTkPpKOnKeCQ7rOhM4/640?wx_fmt=jpeg&from=appmsg)

访问靠后门命令。西数走 `SMART READ/WRITE LOG`：本来用来读写 SMART 页，参数里有个 8 位 log address。ATA 规范给了一段「厂商自定义」区间，修盘和诊断命令就藏在这里：

![ATA 规范中的 log address](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84V5SNXupp7ePru16g6ybwEu1ia8LPscUxtEfv0QQaRFNMZq0Wexz3I4jhBs6AbOjlkXVGnLPvBCyQxhc8TVIdNtn4ZzXZF6iaiaFg/640?wx_fmt=jpeg&from=appmsg)

### 物理串口

很多盘在 SATA 口旁边有 4 针 RS232，可以下修盘 / 诊断命令。厂商和型号命令集不同，有的网上有文档，有的只能挖固件。这篇先不展开串口，第二部分再说。

![硬盘串口接线](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XA6iaOCibWmLhV6nS1D2Q950gPI1CXB0RCuudRJvGESFfa3ic42LCahAwS798hTibBKtRYTO7pW40ODk7T1m9aGWhS8Zh2mCMhZmc/640?wx_fmt=jpeg&from=appmsg)

### 西数板上的 SPI Flash

计划是用后门命令把改过的镜像写回去。解包 / 打补丁 / 重打包的 Python 脚本已经有了，缺的是写盘工具。怕的是：前几次补丁写砸，后门命令也跟着废，盘就回不来了——没有稳妥恢复手段，可能连续砖十几块才有进展。

好在西数主固件有两个落点：一是 MCU 内部 Flash（我这块在用）；二是部分型号板上的 **SPI Flash**，会覆盖内部 Flash。我这块没贴 SPI 芯片，但焊盘在，焊上芯片和几颗电阻，就能让 MCU 从 SPI 启动：

![SPI Flash 芯片位置](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VlC8xNcjrNYXgEAqM52x7QsNJJmmdD331paBGrgzkBCYUHsmnTbbMItSQGHyH7BqF2pN9r5Mkknf9kp3MK0R6TwcXORnxsB8E/640?wx_fmt=jpeg&from=appmsg)

计划：改固件先测 SPI；一旦刷成起不来或刷不进去，用外部编程器在线重刷。订了几颗合适的 SPI 芯片，等货期间先干分析。

## 分析固件

最难的一步：找到处理读请求的代码。这层固件几乎没有字符串可蹭，还散在多个内存段，有的段甚至不在镜像里。得换思路。

### 你调试过硬盘吗？

西数多数盘板子上有未贴的 38 针 MICTOR，就是 JTAG。焊几根线，就能对跑着硬盘的 MCU 做硬件级调试——对，**调试一块活硬盘**。

![JTAG 线焊在硬盘电路板上](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VbAGaIHMSwMfibuKSj4mXCAiakppmXNVWNt6ga5jZwFkLj5uoI9qL90PYKYto2fXTJFUicT7THPaQAtkTTLR8A27vAcbrxcDtrq8/640?wx_fmt=jpeg&from=appmsg)

能下断点、看内存和寄存器、单步，同时从 PC 发命令，价值极大。麻烦也不少：

* 盘要直接挂 PC 的 SATA，才能发 ATA 命令看断点是否命中（手头 USB 转接不支持 ATA passthrough）。
* 超时不回包，Windows 会当盘失踪，后续通信全挂，有的版本甚至 volmgr 直接蓝屏。
* 调试时盘偶尔会进怪状态，得断电重启才正常。

这是我第一次玩 JTAG，边学边试。OpenOCD + FT232 配了一通，总算连上并断进去：

![OpenOCD 连上硬盘 MCU](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VWDuBe7s9s0dmoUd66RsdtdYzFXlbR2WZ0YVXhR8miagaiauCsnOdu3wVqwAq7cgXdUh1XcgOxibiasDkeHx8hvMOeNjiadDWFfGAA/640?wx_fmt=jpeg&from=appmsg)

tap 配置大致参照 MalwareTech 的实验，但这块 MCU 略有不同；我只稳定认出了第一个核，有没有多核不清楚。下一步：写个小工具发命令。

### 厂商专用命令（VSC）

西数后门挂在 `SMART READ/WRITE LOG` 上，叫 vendor specific commands：读写固件、RAM、overlay、其它修盘诊断。眼下最有用的是**读 RAM**。打法：在地址 `0x41414141` 下内存断点，再发读 RAM、地址同为 `0x41414141`，断点应命中；看是谁在处理这条 VSC（也就是谁在处理 SMART READ LOG），顺着调用栈往上爬，找公共分发器，再摸到真正的读扇区处理。

发 VSC：构造 ATA passthrough，寄存器设成 SMART WRITE LOG，log page = `0xBE`（厂商自定义页，西数拿来当后门），再附带 1 个扇区的额外数据，里面是 VSC ID 和参数；读 RAM 还要带地址和长度。

![ATA passthrough 示意](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84U7nmzIe9A97auavlpt6U26ARbzgJibzlqZyMzu8A4gOzklvHm42LzjNwW0l23j4rvSuIfw6EUmsnhlPpvicHaA34qwDLzZXnWyc/640?wx_fmt=jpeg&from=appmsg)

断点设好，跑测试程序发读 RAM VSC，命中：

![断点处的 GDB 输出](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84UanGdU38xqgWWTa7snmf9HLP41pG4lWUWIbsicibJrPGgg7Vgw7frVtFLvyM5D2FcJr9Ql7NuxexIR4ZsuY1Vib5s1tsBhlOUYkM/640?wx_fmt=jpeg&from=appmsg)

读 `0x41414141` 的指令在 `0xFFE1D780`，落在固件代码段里。

### 钻进肚子里

围着触发断点的函数转几分钟，就能看清它怎么从 VSC 缓冲取参数、做内存读：

![读 RAM 命令处理的反汇编](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84X1ic9ibYw6BF5yUmS57RIsSjPwj7JRTuIibXGTEh9ibxk2hlPO88xfweg7ONJibBfX1H6UVDeOVjyibZqsRib70n9mRHoumM79xpWicsU/640?wx_fmt=jpeg&from=appmsg)

往上爬，找到一张 **67 项**的 VSC 处理表——比预想的多：

![VSC 函数处理表](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Ucn4LibibknbBQWybQJibH0uPdIOuYlbXrenL33GF9AJ79h5PJCqrABjM71fFic...