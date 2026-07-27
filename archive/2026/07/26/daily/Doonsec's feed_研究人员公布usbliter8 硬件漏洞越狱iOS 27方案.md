---
title: 研究人员公布usbliter8 硬件漏洞越狱iOS 27方案
url: https://mp.weixin.qq.com/s/Oqw4Yq6aSgH0kuQ3kTsXmw
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:40:11.917513
---

# 研究人员公布usbliter8 硬件漏洞越狱iOS 27方案

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrKqqvdM7HRnndjQsicarNlQ9j0at2dxg7PW0icicQ2WCDBDUFKqsH8M7GoeiacdIkxZo8NH7rKo0VLfbX2USNhQbPIsAhIbiaO0Kn0/0?wx_fmt=jpeg)

# 研究人员公布usbliter8 硬件漏洞越狱iOS 27方案

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](https://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

近日 GitHub 上的 usbliter8-fun 开源项目引发了技术圈关注，这套方案成功在 iPhone11Pro 上实现了 iOS27.0 测试版的系统越狱。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpbjNBR2fRib1vZ0mH9p4g0DicrtefPMGV0aSsF2bgpImDE2UnQGbptoq3mKnrkKp5jhyT54wM3hdOBhu6OuKs7KJL5OztWelEVA/640?wx_fmt=jpeg&from=appmsg)

和大众认知里的一键越狱工具不同，这是一套纯面向开发者的深度技术实验，依托芯片级的 SecureROM (安全只读存储器) 漏洞，通过外接硬件触发破解模式，刷入修改后的自定义固件突破系统全部安全限制。整个操作会彻底抹除设备数据，还会导致多项核心硬件功能失效，只适合用闲置设备做研究使用。

github[.]com/34306/usbliter8-fun

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqevLyNZ9n6bQrMHOV2CDcnDSF9xH8icR1sAmmmVq6mWn2WYeRsNKZFOOMq4hOXjQWxFcw08QthI6uxTfIvBcclzzzrbzljjvAw/640?wx_fmt=png&from=appmsg)

整个方案的核心是由 Paradigm Shift 团队披露的 [usbliter8](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451187115&idx=1&sn=7f5c9068ae5957b1cd79e9ece8c47195&scene=21#wechat_redirect) 漏洞，攻击目标是芯片内置的 SecureROM。

相关情况可见：

[usbliter8：苹果 A12/A13 BootROM 硬件漏洞的完整利用路径](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451187115&idx=1&sn=7f5c9068ae5957b1cd79e9ece8c47195&scene=21#wechat_redirect)

这部分代码属于硬件级初始引导程序，固化在芯片内部，优先级高于系统固件，正常情况下无法通过软件手段修改。

该漏洞影响范围覆盖 A12 和 A13 芯片，Apple Watch 系列的 S4 和 S5 芯片同样存在对应缺陷。

漏洞无法单纯通过电脑 USB 触发，必须借助搭载 RP2350 芯片的开发板发送特定信号，才能让设备进入 PWN DFU (可篡改设备固件升级) 模式。

正常 DFU 模式下设备会严格校验固件的官方签名，而 PWN DFU 模式会突破这层校验，允许刷入任意修改过的自定义固件。

项目作者使用的硬件载体是 Raspberry Pi Pico 2 开发板，搭配一根改造后的 Lightning 数据线。具体接线规则为红线接 VBUS 供电引脚，黑线接 GND 接地引脚，数据线内部的白芯 D - 引脚接开发板 G13，绿芯 D + 引脚接开发板 G12。

将原版 usbliter8 的漏洞程序烧录进开发板后，这套装置就可以用来触发设备的漏洞模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpjdNVgiaic1SGBWNZ7GUwnMKWKH4naDSgMt8Z2mHqObXI4mL8Bib8tBmicSdke00hkHxTH58XLdDbCSQlKVXNwGZPtlNp9SVecLao/640?wx_fmt=jpeg&from=appmsg)

目前这套方案仅适配 iPhone11Pro，其他搭载同系列芯片的设备需要找到对应内存偏移量才能适配，无法直接复用。 操作本身风险极高，刷入自定义固件会清空设备全部数据，还会造成 SEP (安全隔区) 异常、密码功能失效、WiFi 无法使用、基带功能损坏、蓝牙部分功能异常，以及所有苹果官方服务无法运行。绝对不能在日常使用的主力机上操作，仅适合拥有闲置设备的开发者进行技术实验。

项目的核心工作是对官方 IPSW (苹果设备固件包) 进行多处二进制修改，突破系统各层级的安全限制。这些补丁覆盖内核、设备树、系统服务三个层面，每一处都对应苹果的一项安全机制，修改位置和指令都有明确的偏移量对应。

内核层面共有三处核心修改。第一处针对内核中 isDeviceInRestoreMode 函数，对应文件偏移 0x2894b68，写入二进制指令 20 00 80 d2 c0 03 5f d6，让内核始终判定设备处于恢复模式，以此绕过 USB 限制模式的约束。第二处针对沙盒机制，在 file\_check\_mmap 函数偏移 0x2f774e0 处写入指令 00 00 80 d2 c0 03 5f d6，同时修改 mount\_check\_mount 偏移 0x2f75640、remount 偏移 0x2f75474、umount 偏移 0x2f75110、vnode\_check\_rename 偏移 0x2f7019c 等多处位置，放开 /var/jb 目录的代码执行权限，同时解除挂载、重挂载、卸载和文件重命名的沙盒限制，为越狱环境的运行提供基础权限。第三处修改 AMFIIsCDHashInTrustCache 函数偏移 0x1f1ebe0 处的指令，让函数直接返回真值，跳过代码签名的信任缓存校验，实现任意代码运行。

设备树层面修改 ephemeral-storage 参数，将其值设为 u32 类型的 1，解决刷机过程中进度条卡在 99% 的问题。

系统服务层面的补丁主要解决两个核心问题。一是在 coreauthd 进程偏移 0x95c0 位置填入 NOP (空操作) 指令，在 ctkd 进程偏移 0x1b38 和 0x1b3c 位置修改为返回 0 的指令，避免 SEP 安全隔区崩溃，保证设备能够正常启动。二是修改 mobileactivationd 激活服务，在 should\_hactivate 函数偏移 0x2ebb14 处写入指令 20 00 80 52，也就是让寄存器返回 1，实现伪激活，让设备无需连接苹果官方服务器就能进入系统。同时对 getActivationState 相关的 0x327cb0 等四处位置的判断逻辑进行修改，确保系统始终识别为已激活状态，形成多重保障。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDo4j83FXorj28REKn0MMJXeqib1xrxeKYRiaMmiaw6ibA113yhG6gMds1osgavdEb6N9yjMWuuC6utAWbTjibRtoKKwwMIibkyVtbrWA/640?wx_fmt=jpeg&from=appmsg)

##

整个操作分为四个阶段，全程需要通过命令行执行，依赖 Python 环境和相关工具库。开始前需要先从苹果官网下载对应机型的 iOS27.0 beta2 固件，再安装 requests、pyimg4、pymobiledevice3 三个 Python 依赖库，所有操作都在 work-27.0b2 目录下进行。

### 1. 刷入自定义固件

先手动将设备进入 DFU 模式，连接到准备好的 PWN DFU 硬件装置。开发板指示灯闪烁两次代表正在执行漏洞触发，指示灯常亮代表成功进入 PWN DFU 模式，如果指示灯熄灭则触发失败，需要重新进入 DFU 模式再次尝试。也可以在电脑的 USB 设备列表中验证，当设备描述中出现 PWND:[usbliter8] 字样，就说明漏洞触发成功。 确认成功后将设备接回电脑，进入对应工作目录，执行 make\_cfw.py 脚本生成自定义固件，该脚本需要管理员权限运行。随后启动 tss 代理服务并执行 restore\_cfw.sh 脚本，开始向设备刷入自定义固件。设备屏幕会出现恢复进度条，等待脚本执行完毕，设备会回到恢复模式，刷机阶段完成。

### 2. SSH Ramdisk 引导

再次将设备进入 DFU 模式并触发 PWN 模式，接回电脑后依次执行 get\_rd.py 和 boot\_rd.sh 脚本，启动带 SSH 功能的临时 Ramdisk 内存盘系统。通过 iproxy 工具将电脑的 2222 端口映射到设备的 22 端口，就可以用 SSH 工具连接设备，默认 root 用户密码为 alpine。 连接设备后挂载对应系统分区，找到设备自带的 sep-firmware.img4 文件，将其传回电脑并命名为 dev\_sep.img4。使用 img4tool 工具搭配签名文件对该固件进行处理，解决 SEP 固件的签名兼容问题。

### 3. 正常系统启动

处理完 SEP 固件后，执行 get\_boot.py 和 boot.py 脚本，引导设备启动刷好的自定义固件系统。系统启动后可以继续通过 USB 搭配 iproxy 和 SSH 连接设备，默认密码不变，手动安装越狱基础环境和 Sileo 包管理器。

### 4. 网络补全与环境完善

由于 WiFi 和基带功能都无法使用，设备本身不能直接联网。执行 net\_up.sh 脚本可以通过 USB 共享电脑的网络给设备，满足安装软件的需求。网络连通后安装越狱基础引导包，完成后 Sileo 就会出现在设备桌面。 如果 Sileo 没有正常显示，可以重新进入 SSHRamdisk 模式，将 /var/jb 目录下的 Sileo 应用移动到系统应用目录，重启设备后执行 uicache 命令刷新桌面即可。如果桌面仅显示设置、电话和反馈助理三个应用，同样在 Ramdisk 模式下将预装的系统应用全部复制到系统应用目录，就能恢复完整的系统应用列表。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrmCMuJjC32nQf23wl1VVwaOcE4WRGORUuGvlL0ncw8toWmqR2d6deUhF5UH3V5movJ3ibPunOskM7EictqxVxmImrGfTVe8ico44/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpJDNUjJ6GpwjW8R9LEjzXu4nFiaEL4JC8FBE3Zqjc2nJkra8Zc4YJo7mscJBPia0NTGYZE1NNocn1cLmIGXicIESxdxaKQsTec84/640?wx_fmt=jpeg&from=appmsg)

##

这套方案是目前较早针对 iOS27 系统的完整越狱探索，它验证了 usbliter8 底层漏洞在新一代系统上的可用性，完整呈现了从硬件触发漏洞、自定义固件修改到越狱环境部署的全链路技术逻辑，对 iOS 安全研究有明确参考意义。 同时它的局限性也非常明显。仅支持单一机型，适配其他设备需要逆向分析寻找对应偏移量，工作量极大。

大量核心硬件功能无法正常使用，完全不具备日常使用价值。操作流程复杂繁琐，全程依赖命令行和手动调试，没有面向普通用户的可视化界面，非技术人员几乎无法完成全流程操作。

对于普通用户来说，这类底层越狱项目更多是了解 iOS 安全机制的窗口。苹果的安全防护层层递进，从芯片级 SecureROM 到系统内核再到应用沙盒，每一层都有对应的校验机制。

而越狱研究的过程，本质上就是寻找并串联每一层防护缺口的过程。如果没有对应的技术基础和闲置设备，不建议动手尝试，避免造成设备永久损坏。

相关项目

* **wh1te4ever**制作的**usbliter8-fun** ，适用于 CFW 和 Ramdisk，已针对 iOS 27.0 beta 2 (24A5370h) 进行修补。
  https://github.com/wh1te4ever/usbliter8-fun
* **khanhduytran0**为内核中的设备树和 USB 限制提供了思路

  https://github.com/khanhduytran0
* **img4/img4tool**由**tihmstar**开发，用于使用 APTicket 签名 IMG4
* **m1stadev** / **doronz88**的**pyimg4/pymobiledevice3**用于导出内核缓存，转发 usbmux 端口
* **Lakr233**的**trollvnc**用于通过 USB 控制设备

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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