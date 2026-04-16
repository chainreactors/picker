---
title: Predator间谍软件iOS内核利用引擎深度解析
url: https://mp.weixin.qq.com/s/AKJbKulNMQPcSDX_EU7Lvw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:45:21.659026
---

# Predator间谍软件iOS内核利用引擎深度解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpmHNQUgaZTe9SaWGWyFMWLGYHqIAfKv1xBJ73FxPEnPv8iaQwd3SoibiavTEwhFwWmvOIpPqeiaI8cncAFyZUaeoCILbV5FXKmqPk/0?wx_fmt=jpeg)

# Predator间谍软件iOS内核利用引擎深度解析

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

商用间谍软件突破苹果指针身份验证，实现内核内存访问

在前期研究中，Jamf记录了Predator间谍软件如何规避iOS反分析检测、绕过iOS录音指示器的技术。这些报告揭示了Predator的攻击行为，却未说明其获取系统深层权限的实现方式。

相关阅读：
[苹果手机间谍软件Predator中未公开的反检测反蜜罐反取证技术](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184834&idx=1&sn=9370a0d59636bba8440ef349cbfa1afc&scene=21#wechat_redirect)

[苹果手机间谍软件劫持iOS私有API：摄像头麦克风偷偷录制毫无提示](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451185122&idx=1&sn=c023e4c313f1af1895f4d3b385325abc&scene=21#wechat_redirect)

本文将揭晓这一核心答案。

通过对Predator iOS样本的持续逆向分析，在首份报告的基础上，首次披露Predator内核利用引擎支撑其监控能力的完整技术原理。

本次分析的攻击链针对iOS 17以下版本，覆盖A16及前代芯片设备。苹果在A15设备中引入的安全页表监视器（SPTM） 将页表管理迁移至EL2异常级别，从架构层面有效缓解了本文所述的内核代码篡改技术。

核心发现

1. FDGuardNeonRW：一款内核读写原语，利用ARM NEON向量寄存器作为隐蔽数据通道，实现任意内核内存的读写操作；

2. 基于JavaScriptCore工具链挖掘的PAC绕过：Predator在苹果原生JavaScriptCore框架中检索特定20字节ARM64指令序列，伪造PAC签名指针；

3. 256项PAC签名缓存：按地址字节索引预计算签名指针，实现无加密延迟的实时钩子回调；

4. RWTransfer：通过受保护文件描述符与Mach端口操控，实现进程间内核读写权限的传递；

5. callFunc：一套远程函数执行框架，借助Mach异常消息劫持线程状态；

6. 覆盖21款设备型号（iPhone XS至iPhone 14 Pro Max），划分为5个设备适配类别。

背景：Predator必须突破的iOS安全特性

指针身份验证码（PAC）

自A12芯片（2018年iPhone XS）起，苹果引入PAC硬件安全特性，为代码指针添加加密签名。处理器执行函数指针或返回地址前会校验签名，攻击者篡改指针将触发校验失败与系统异常。

内核地址空间布局随机化（KASLR）

iOS每次开机都会随机化内核基地址，所有内核代码与静态数据结构均偏移不可预测的数值。即便攻击者掌握内核漏洞，也需先获取可靠的内核内存读取原语以计算偏移量——而这正是FDGuardNeonRW的核心能力。

发现一：FDGuardNeonRW——通过向量寄存器实现内核内存访问

命名解析

FDGuardNeonRW的类名完整编码了其技术原理：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpPZroicsJ9LsQA1RQdFAUJkfib3pqbrnMJnzSYjCSjp7Yr6sqh3utQWSHWGcrDHJsA4aBApYoqCznK54QRbxQJAx5toOpOEEMibA/640?wx_fmt=jpeg)

组成部分 含义
FD 文件描述符，漏洞利用涉及change\_fdguard\_np系统调用
Guard 操控文件描述符防护机制，搭建内核原语
Neon ARM NEON向量寄存器作为数据传输通道
RW 实现内核内存的读写双向访问

这是Predator所有功能的核心原语：所有钩子、进程注入、PAC绕过，均依赖FDGuardNeonRW对任意内核内存的读写能力。

NEON数据通道

ARM NEON是一组128位向量寄存器（V0-V31），原生用于SIMD并行运算，也是内核上下文切换时保存/恢复的线程状态数据。

Predator复用经典攻击技术：通过thread\_get\_state/thread\_set\_state Mach API，跨线程读写完整寄存器状态（含NEON寄存器）。其创新点在于专用NEON寄存器组传输内核数据：32个128位向量寄存器单次调用可传输528字节数据（含FPSR、FPCR与对齐填充），远超通用寄存器的272字节传输能力。

该通道依赖初始漏洞搭建的内核组件：NEON仅为传输载体，内核内存读写由内核权限代码执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpMEKL0oicXHGj6hoGIWW7oFBLPW74tcaz6GGsgLL5N1Aymf0VHBPf1tvp4UMZzO4Cuscz3f6w64JyXHjIQp3MsvOu9IbcWSmRs/640?wx_fmt=jpeg)

（图1：FDGuardNeonRW以NEON寄存器为高带宽内核数据通道的读写原语）

读取原语（单次528字节）

读取操作依赖初始漏洞植入的内核代码路径：将受控内核地址的数据加载至NEON寄存器后触发陷阱指令。目标线程恢复执行并触发陷阱，Predator异常处理程序接收ID为2406（0x966）的Mach异常消息，获取携带内核数据的NEON状态。程序最多重试10次解决时序竞争问题，单次读取528字节。

写入原语（轮询确认）

写入操作反向复用传输通道：Predator挂起目标线程，读取VFP/NEON基准状态，按设备专属偏移修改目标地址与数据，发送携带修改后状态的异常响应。内核将状态还原至线程上下文，线程恢复后，漏洞内核代码从NEON寄存器读取数据并写入目标内核地址。程序最长轮询3秒，比对回传数据确认写入成功。

选用NEON寄存器的核心优势

• 大容量：单次操作传输512字节以上数据；

• 内核托管：属于标准线程状态管理范畴；

• 异常可见：完整包含于Mach异常消息；

• 双向复用：读写共用同一套机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDribUSaNzTlVz76EAMjiaiat73ZSibnesh09DTKNz5ZXgL0XwwtY6NBC2V5T2ptNK08wPTzt1ibOBFGUm3SiaPQ1rEtPEQ0iaUiaYtYHw8/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDr0kfRJAFIDpFpFaFL29DaGK3adrvIwzSVOrQvhXvXpOoCPJKRDNWEhk5wMu4icH76pltVxFmKsWlQwh16p5yj8Vh58Kd2dCHTQ/640?wx_fmt=jpeg)

（图2-3：NEON读写原语的IDA反汇编与反编译代码）

发现二：在JavaScriptCore中挖掘PAC绕过工具链

技术痛点

Predator在系统进程中安装钩子需重定向函数执行，即修改代码指针。PAC设备（iPhone XS及后续机型）的所有代码指针均携带加密签名，Predator必须为重定向指针伪造有效签名。

解决方案：复用苹果原生代码

Predator未自研签名算法，而是在苹果JavaScriptCore框架（Safari JS引擎原生组件）中，检索可控输入的PAC签名原生代码序列，目标函数为JSC::JSArrayBuffer::isShared()。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqKQwmTTodIialLLoq4OKWRMI3byySt4IzYFom5RmteMnGAPsNmcLRjE0yN8TU9uUGAkkEIzDLHIhAGauugKibzyTjoP5mbf3XKI/640?wx_fmt=jpeg)

（图4：基于JSC工具链挖掘+256项预计算签名缓存的PAC绕过方案）

20字节核心工具链

Predator通过memmem()在isShared符号前后1000字节范围内，精准匹配以下20字节ARM64指令：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDr4icS8On2HpSCJuFQuQRuoBhribWPSHEqHibBKafAGcOc1eDLmLZFDz0teg51JoWeznGy169gGDv6Jiaj1fvzrdibNawjAbQLFxicaQ/640?wx_fmt=jpeg)

机器码 ARM64指令 功能
30 02 C1 DA PACIA X16, X17 以X17为上下文，硬件签名X16指针
E8 03 90 9A CSEL X8,XZR,X16,EQ 校验有效则复制结果
1F 01 00 F1 CMP X8, #0 校验签名是否成功
E0 07 9F 1A CSET W0, NE 设置返回值
C0 03 5F D6 RET 返回签名指针

核心指令PACIA X16, X17可通过硬件PAC密钥签名指针，Predator操控X16/X17寄存器，即可伪造任意指针的有效签名。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDr51NUTaGQczia5uCd6wXcKupSiazeyLyPIvXicb4ZO9uzDzrv5uheticaVsCcXfIiazpV8QyqHCa2KdLjRBEhkFsicuPr6efRReqVHc/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqz1YZaqX5EnibauaK1kmH2WgJEQBgWCHxABbRuFPu8mXDXz1xFD4Rn3RwkxlOEjaAwPbo0PQw4pOqBrDOqSSxe9QfKcQbsLcQ8/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqSCtkuPViaCJ8hCMYrstn3iaxHcCP6nicQ5iaFFWLLTJQZ8xIViah08iaSuVkdCc2lX9nDglXasm9iaE0zm5MzYwdydibjOwia3acPhjcs/640?wx_fmt=jpeg)

（图5-7：远程PACIA工具链挖掘流程的反汇编、反编译与十六进制数据）

发现三：256项PAC签名缓存

单次remotePACIA调用需创建线程、配置异常端口、修改内核线程状态，耗时毫秒级，无法满足微秒级的钩子回调需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqVk6uTLZOC9lhDTibZvHZrTw4fcJ8JvGFTE6yrWgAOqy7l5qTiaqslPHu6uc6CErOibibv5oHA1GPLEdDfW4XZzrUzzu1pYZVqA04/640?wx_fmt=jpeg)

预计算签名表

Predator初始化时构建256项预签名指针缓存，覆盖地址所有高字节取值，钩子触发时可即时查询有效签名指针。
参数 数值 说明
缓存大小 4096字节 256项×16字节/项
条目格式 [签名PC, 签名LR] 各8字节
PC鉴别器 0x7481000000000000 程序计数器签名
LR鉴别器 0x77D3000000000000 链接寄存器签名
索引规则 cache[16×(flags>>24)] CPSR标志位高字节
哈希算法 CityHash64（谷歌） 哈希桶查询

PC/LR独立鉴别器是苹果的纵深防御机制，Predator针对性适配；每个函数目标仅需执行512次高耗时remotePACIA调用，后续钩子回调均为零延迟缓存查询。

发现四：callFunc——远程函数执行框架

callFunc是Predator在远程进程中执行任意函数的核心机制，整合PAC缓存、Mach异常与线程状态操控，支持传入函数指针与最多6个参数（x0-x5）。

实现原理

远程进程中驻留木马线程（Predator内部命名），持续触发断点生成Mach异常。callFunc接收异常后填充参数寄存器，从PAC缓存查询签名PC/LR，异常响应携带修改后的线程状态；内核交付响应后，木马线程以指定参数执行目标函数。

毒化LR返回地址指向另一断点，函数返回时触发新异常，Predator重新接管控制权，形成可无限复用的远程过程调用机制。

源码溯源：0x10000B028函数日志标注文件为TaskROPDevOff.h，证实这是面向未开启开发者模式设备的ROP技术。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDoxRiaDbMicq2jhAUNngIITjtefCBxeFk3n8Nzc6FK1CHYOYvTETYkrRibNWcwMHupaWDYT1SZ1icmaJPIZ0G8g2GI19YVuticLwz6M/640?wx_fmt=jpeg)

（图8：callFunc反编译代码——缓存未命中时构建256项缓存，命中时即时查询签名指针）

发现五：RWTransfer——进程间内核原语共享

Predator采用多进程架构：监控进程管理生命周期，辅助进程执行实际监控。初始漏洞仅赋予监控进程内核读写权限，RWTransfer实现权限跨进程传递。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpyXypKJxXdBFt0qY9DZVK8cvhgibx0O8rsvmqvkXgA3fOictnEelC6jvicMz2wia4iacliaicQJUZsKElyafjjDrukAR5SUaUDnjSoEE/640?wx_fmt=jpeg)

（图9：RWTransfer进程间内核读写权限传递协议）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpbsXiahY64VCvFgvPuhLOgQudDHfr28J8ibiaVU4RBVdRHfGD1RgOZW0OiaSlib9xwtRvo4kj1K6mGtnt7VPWzFYjrOIozJ7U14Cic4/640?wx_fmt=jpeg)

组件 数值 功能
传输魔数 0x998B3D24 标识内核内存中的权限传输结构
端口防护 0x9991AF84 应用于Mach接收端口
文件描述符 200个指向"/"的FD 调用change\_fdguard\_np(guard=100)创建
线程创建 pthread\_create\_suspended\_np 专属传输线程
传输方式 mach\_msg 向辅助进程发送FD数组+线程端口

监控进程遍历内核链表（按设备类别适配偏移），定位辅助进程的任务结构、IPC空间与端口条目，是Predator最复杂的组件，同步操控Mach端口、文件描述符、内核链表与线程状态。

发现六：远程Objective-C方法解析

Predator挂钩远程进程Objective-C方法时，无法依赖本地运行时查询：dyld共享缓存方法地址全进程一致，而应用二进制方法受进程级ASLR偏移影响。

因此Predator通过callFunc远程执行完整Objective-C运行时解析链路，保证结果精准：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrt80fVicIuT7TiclTQC0DFg1SlL1doGibWB2ehsUPjicTGtDAlhlKyzyVHPyYV0AvvjWOUBR3gAmsyxXrNVPeYjYpHLxNuhrt40JI/640?wx_fmt=jpeg)

阶段 运行时函数 功能
1 sel\_registerName 方法名转选择器
2 objc\_getClass 获取类对象
3 class\_getInstanceMethod 获取方法结构体
4 method\_getImplementation 获取实现指针

每次调用均完整执行Mach异常→PAC缓存→线程状态操控流程，彻底解决ASLR带来的地址偏移问题。

发现七：设备支持矩阵——5类适配，覆盖21款机型

不同iPhone的SoC、安全特性、内核版本导致内核结构布局差异，Predator按设备类别配置精准内核偏移。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrPI0NLvHxIKx0ULGRv8INpmDicv2OPD47tRGD2a74X9CSPld0wayrkhRPUxbCOL95zrXrqa68yxxMwzJtrdxNjstrtQibBt9Lxo/640?wx_fmt=jpeg)

类别 芯片 iPhone机型 数量
0 A12仿生 XS、XS Max、XS Max（国行）、XR 4
1 A13仿生 11、11 Pro、11 Pro Max、SE（第二代） 4
3 A14仿生 12 mini、12、12 Pro、12 Pro Max 4
4 A15/A16 13全系列、SE（第三代）、14全系列 9

注：样本未使用类别2，大概率为硬件版本预留或合并适配；不支持设备返回错误码5，安全终止执行避免内核崩溃。总计覆盖2018-2022年21款iPhone。

XOR比对解码

反编译代码中的十六进制常量为XOR编码ASCII字符串：程序调用uname()获取设备标识（如iPhone15,3），XOR比对结果为0即匹配设备。编码规则为小端序，如0x3531对应ASCII"15"、0x332C对应",3"，直接映射iPhone型号。

示例：iPhone15,3（iPhone 14 Pro Max）匹配双重XOR校验为0的条件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDphFld0ZaVFw6Hibumn9siazwTaqslLLKW5RT2SKvjK6gz9...