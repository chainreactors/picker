---
title: iOS虚拟手机实现能力现状
url: https://mp.weixin.qq.com/s/Mn4qQt3wRm4Rm2oWP5uYtA
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:03:12.022370
---

# iOS虚拟手机实现能力现状

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Sq4BUsrXeT8ibZZB2ialGYrS8ibrwU30RxXJLrF4CVzbevzMcAy6s5YUxY3ia2knbiajxmIK6t4k8oFXXwhbFBDmMiamTG0ArspWRsdPR8e4mHzsM/0?wx_fmt=jpeg)

# iOS虚拟手机实现能力现状

原创

非虫
非虫

软件安全与逆向分析

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# iOS虚拟手机实现能力现状

上一篇《iOS虚拟手机实现原理解析》写作时，`vphone-cli`还处在很早期的形态，仓库大约只有5个commit。那时它更像一个把Apple私有`Virtualization.framework`能力拉起来的启动工具：用少量Swift/ObjC代码创建PV=3虚拟机，再配合Python脚本和Shell脚本完成固件合并、引导链补丁、DFU恢复、Ramdisk启动和CFW安装。

截至2026-04-26分析时，`vphone-cli`已经不只是“能启动虚拟iPhone”的PoC，而是逐渐演化成了一套围绕iOS虚拟手机构建、修补、安装、运行、自动化、越狱和环境切换的研究平台。

本文不再重复上一篇中已经讲过的PV=3硬件模型、私有Entitlements、DFU恢复、SHSH签名、Ramdisk引导和基础CFW安装细节，而是从当前仓库的提交演进和文件结构出发，梳理`vphone-cli`现在具备了哪些能力，以及这些能力相比早期版本解决了什么问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT8qkHwUQRUNx9ibEeGzPA6CRViajNKPicFvibia42DHmpXkxicdiaLWZOkic3pMsIIL1nU5YibD7flebiaOQJVoEkibHicAgSA4ZBQTL1z0ato/640?wx_fmt=png&from=appmsg)

## 1 分析基线

分析的仓库为：

```
https://github.com/Lakr233/vphone-cli
```

项目当前最关键的变化可以概括为五点。

第一，固件补丁逻辑从早期Python脚本为主，迁移到Swift`FirmwarePatcher`模块为主。Python现在主要保留在CFW二进制修补、`pymobiledevice3`桥接、Ramdisk构建等脚本侧。

第二，工具入口从分散脚本变成`Makefile`统一入口。构建、签名、VM创建、固件准备、固件补丁、DFU恢复、Ramdisk、CFW、越狱安装、Host预检、AMFI绕过辅助和备份切换都集中在`make`目标中。

第三，固件变体从单一路线扩展为`Patchless`、`Regular`、`Development`和`Jailbreak`四种路径。不同路径对应不同的安全绕过强度、调试能力和越狱能力。

第四，虚拟机运行时不再只是显示图形界面和串口，而是通过`vphoned`和主机侧控制Socket提供文件、应用、钥匙串、剪贴板、IPA/TIPA安装、位置、电池、低电量、触控、按键、截图和自动化测试能力。

第五，研究环境从一次性制作转向可复用生命周期管理。VM配置进入`config.plist`清单，ECID和UDID可以稳定预测，VM状态可以备份、恢复和切换。

## 2 项目变化

项目初始提交发生在2026-02-27，主题是“Add vphone CLI, ObjC wrappers, and scripts”。这个提交一次性加入23个文件，大约4933行内容。这个阶段的核心目标很明确：把PCC固件里的vphone能力搬到本地macOS上，让虚拟iPhone可以进入DFU、恢复固件、启动系统，并通过SSH/VNC访问。它更像上一篇文章分析的形态，技术重点集中在“如何跑起来”。

从2026-03-01到2026-03-08，提交密度明显上升。2026-03-04单日就有43次commit，是整个仓库演进中最密集的一天。这一阶段集中出现了JB安装流程、TXM补丁重构、Kernel JB补丁验证、GDB调试Stub、Ramdisk测试流程、vphoned雏形、录屏截图、文件传输、位置模拟、窗口状态、JB首启收尾等能力。也就是说，项目已经从“启动链补丁工具”转向“可交互研究环境”。

从2026-03-10到2026-03-12，仓库进入结构化重构阶段。`d042596`提交完成Swift固件补丁器与CLI接线，`6d11093`加入VM manifest系统，`e189b80`加入vphoned模块化、菜单整合和SwiftUI应用浏览器。这个阶段的意义在于，早期散落在Python脚本和临时验证脚本中的固件补丁逻辑，开始沉淀为可测试、可复用、可由CLI直接调用的Swift模块。

从2026-03-14到2026-03-20，仓库开始补齐工程化能力。新增VM备份、恢复和切换，新增`aria2c`下载支持，`pymobiledevice3`替代大部分外部libimobiledevice工具，`--install-ipa`支持自动安装，`boot_host_preflight.sh`开始承担Host环境诊断职责。这些提交解决的是“每次都手工搭环境、手工排错、手工切换”的痛点。

从2026-03-28到2026-04-22，项目的重点又转向自动化和`Patchless`变体。主机侧`vm/vphone.sock`自动化控制Socket被加入，随后每次动作返回压缩灰度截图，适合AI或E2E测试工具闭环控制。`Patchless`路线则尝试减少传统引导链和内核安全绕过，转向文件系统重建、BuildManifest哈希更新、AEA密钥处理、GPU驱动和Mobile Activation修补等路线。2026-04中旬以后，AMFI预检、非完全关闭SIP/AMFI环境支持、`amfidont`辅助脚本、`Patchless` binpack和`--no-vphoned`选项也陆续出现。

这些提交线索说明，`vphone-cli`的目标已经从“证明iOS虚拟手机可启动”升级为“让安全研究者能够重复创建、修补、运行、控制和维护多个虚拟iOS环境”。

## 3 项目仓库结构

当前仓库结构已经明显分层。

`sources/vphone-cli`负责Host侧主程序。它包含CLI参数解析、VM生命周期、PV=3硬件模型、Virtualization配置、窗口和菜单、虚拟机视图、触控注入、位置转发、电池同步、Touch ID转发、录屏截图、文件浏览、应用浏览、钥匙串浏览、IPA/TIPA安装和主机侧自动化Socket。

`sources/FirmwarePatcher`负责Swift固件补丁。它按AVPBooter、iBoot、TXM、Kernel、DeviceTree、Filesystem和Manifest拆分模块，并通过`FirmwarePipeline`按固件变体组织执行顺序。这里还引入了ARM64编码/反汇编、IM4P处理、Mach-O辅助、PatchRecord输出和测试目标。

`scripts/vphoned`是Guest侧守护进程。它运行在iOS虚拟机内部，通过vsock端口1337和Host侧通信。它承担HID、文件、钥匙串、应用、剪贴板、URL、设置、位置、低电量、IPA安装等能力，并在非Patchless路径下支持自更新。

`scripts/patchers`现在主要保留CFW阶段的动态二进制修补逻辑，例如`seputil`、`launchd_cache_loader`、`mobileactivationd`和`launchd`的jetsam补丁。

`research`目录则记录补丁矩阵、TXM分析、Kernel JB补丁验证、DeviceTree、manifest来源、键盘事件链路、机器标识存储和迁移总结。它已经不只是说明文档，而是补丁可靠性和跨版本迁移的依据。

## 4 四种固件变体

当前项目把固件路线分为`Patchless`、`Regular`、`Development`和`Jailbreak`四种变体。它们不是简单的开关组合，而是四个不同目标的制作路径。

`Patchless`变体的目标是尽量减少传统意义上的引导链和内核安全绕过。它保留更多iOS安全机制，转而通过文件系统合并、trustcache生成、mtree生成、digest.db生成、SystemVolume root\_hash生成、BuildManifest哈希更新和AEA重新加密来让系统接受修改后的文件系统。后续提交还加入了GPU驱动、Mobile Activation补丁、vphoned安装、binpack可选安装、`--no-binpack`和`--no-vphoned`开关。它适合研究“更接近原厂安全状态”的虚拟iOS环境，但并不等于完全无修改。

`Regular`变体是上一篇文章主线的延续。它会绕过AVPBooter、iBSS、iBEC、LLB、TXM和Kernel中的关键签名、SSV、APFS、AMFI、launch constraints、dyld策略和Sandbox路径，再通过CFW安装Cryptex、GPU驱动、iosbinpack64、launchd缓存加载器补丁、mobileactivationd补丁和LaunchDaemons。它的价值是稳定得到一个可SSH、可VNC、可运行基础工具的虚拟iPhone。

`Development`变体在`Regular`基础上增强调试能力。它使用TXMDevPatcher，加入get-task-allow、debugger entitlement、Developer Mode bypass等补丁，并在CFW阶段加入dev overlay、`rpcserver_ios`替换和debugserver权限修补。2026-04-20还加入了`thread_guard_violation`相关内核补丁，用于禁用EXC\_GUARD交付，使行为更接近生产环境中不崩溃的路径。这个变体更适合动态调试、RPC控制和调试器接入。

`Jailbreak`变体是安全绕过最强的路径。根据`research/0_binary_patch_comparison.md`，它在基础补丁之外包含TXM Dev/JB补丁、iBSS nonce跳过、Kernel JB扩展、Procursus bootstrap、BaseBin hooks、TweakLoader、Sileo、TrollStore Lite和首启LaunchDaemon收尾。研究文档中的细粒度统计显示，`Regular`总计51项，`Development`总计65项，`Jailbreak`总计127项。这里的总数包含启动链补丁、CFW二进制补丁和安装组件，粒度比README首页的用户摘要更细。

从能力定位看，四种变体可以这样理解：

* `Patchless`

  用于尽量保留安全机制的文件系统重建路线。
* `Regular`

  用于稳定启动和基础远程访问。
* `Development`

  用于调试器、RPC和开发态实验。
* `Jailbreak`

  用于完整越狱环境、包管理器、插件加载和更深系统访问。

## 5 Swift固件补丁

早期仓库使用`Scripts/patch_firmware.py`处理固件补丁。当前仓库已经把这条主线迁移到Swift`FirmwarePatcher`模块。`Package.swift`中可以看到独立的`FirmwarePatcher`target，它依赖`Capstone`、`Img4tool`和`MachOKit`，并被`vphone-cli`可执行程序引用。

当前CLI支持两个直接面向固件补丁的子命令：

```
vphone-cli patch-firmware --vm-directory <dir> --variant regular
vphone-cli patch-component --component kernel-base --input <file> --output <raw>
```

`FirmwarePipeline`按以下顺序组织组件：

```
AVPBooter
iBSS
iBEC
LLB
TXM
kernelcache
DeviceTree
Filesystem
Manifest
```

不同变体会在这些组件上选择不同的patcher。Regular使用基础iBoot、TXM和Kernel补丁。Development把TXM切换为`TXMDevPatcher`，Kernel使用dev模式。Jailbreak会在基础Kernel补丁后追加`KernelJBPatcher`，并在iBSS阶段追加JB扩展。Patchless则跳过大部分传统引导链和内核补丁，把重点放到Filesystem和Manifest。

这次迁移的价值不只是“用Swift重写”。它改变了补丁工程的组织方式：

* IM4P容器加载和保存由`IM4PHandler`统一处理。
* PatchRecord可以输出为JSON，便于比较和回归。
* DeviceTree、Filesystem和Manifest作为管线阶段参与，而不是散落在临时脚本中。
* `make fw_patch`

  、`make fw_patch_dev`和`make fw_patch_jb`都通过Swift管线执行，减少Python脚本与Swift启动器之间的语义漂移。
* 测试目标`tests/FirmwarePatcherTests`用于维持补丁行为的一致性。

上一篇文章中大量描述了AVPBooter、iBoot、TXM和Kernel的补丁原理。当前仓库真正新增的能力，是把这些补丁从“可执行脚本”提升为“项目内部可维护的固件补丁系统”。

## 6 自动化安装与运行

早期制作拉起虚拟iPhone需要人工串起多个步骤：安装依赖、构建工具、创建VM、下载两份固件、合并固件、补丁、启动DFU、获取SHSH、恢复、构建Ramdisk、发送Ramdisk、进入SSH、安装CFW、首次启动。当前`Makefile`已经把这些步骤统一成可组合目标。

一键流程入口是：

```
make setup_machine
```

它背后的`scripts/setup_machine.sh`会按顺序完成以下工作：

1. 执行Host依赖安装、项目构建和签名。
2. 创建VM目录并生成`config.plist`。
3. 执行`fw_prepare`下载或复制iPhone IPSW和cloudOS IPSW。
4. 根据参数选择`fw_patch`、`fw_patch_dev`、`fw_patch_jb`或`fw_patch_less`。
5. 启动DFU并执行`restore_get_shsh`和`restore`。
6. 再次进入DFU，构建并发送SSH Ramdisk。
7. 启动usbmux端口转发并执行CFW安装。
8. 启动首次正常系统并分析串口输出。

它还支持多个实用参数：

```
make setup_machine JB=1
make setup_machine DEV=1
make setup_machine LESS=1
make setup_machine NONE_INTERACTIVE=1
make setup_machine SUDO_PASSWORD=...
make setup_machine SKIP_PROJECT_SETUP=1
make setup_machine LESS=1 NO_BINPACK=1
make setup_machine LESS=1 NO_VPHONED=1
```

这些参数解决了不同研究场景下的重复制作问题。比如调试Kernel补丁时可以跳过项目安装，只重复固件和启动流程；做Patchless实验时可以排除binpack或vphoned，观察更小修改面的系统行为。

`setup_tools.sh`负责依赖安装。它会检查Homebrew依赖，构建`trustcache`和`insert_dylib`，创建Python虚拟环境，并在Patchless模式下额外准备`apfs_sealvolume`。这相比早期手工编译libimobiledevice生态的流程简单很多。

`fw_prepare.sh`也比早期更灵活。它不再只接受固定URL，而是支持本地IPSW、直接URL、版本号、Build号和固件列表查询。它优先使用`aria2c`下载，并能基于`ipsw`工具列出目标设备可下载固件。对于反复尝试不同iOS 26构建的研究者，这比手工找URL可靠得多。

恢复和Ramdisk发送也转向`pymobiledevice3`桥接。`scripts/pymobiledevice3_bridge.py`提供`usbmux-list`、`recovery-probe`、`ramdisk-send`、`restore-get-shsh`和`restore-update`等命令，减少对外部二进制工具和本地编译状态的依赖。

## 7 Host环境和AMFI管理

虚拟iPhone依赖Apple私有虚拟化API和私有Entitlements，Host环境一直是最容易失败的地方。当前仓库已经把这部分纳入工程化检查。

`boot_host_preflight.sh`会检查以下状态：

* macOS版本和硬件型号。
* 是否运行在嵌套Apple VM中。
* `kern.hv_vmm_present`

  状态。
* SIP状态。
* `allow-research-guests`

  状态。
* 当前`kern.bootargs`和下次启动的`nvram boot-args`。
* Gatekeeper评估状态。
* release二进制、debug二进制和签名debug二进制是否能正常执行。

如果release签名二进制启动即退出137，脚本会提示这是AMFI或执行策略不允许私有虚拟化Entitlements的典型表现。如果Host本身是嵌套Apple VM，它会在`--assert-bootable`模式下提前失败，避免浪费时间进入VM启动阶段。

当前README给出两类Host安全配置路径。第一类是完全关闭SIP并通过`amfi_get_out_of_my_way=1`禁用AMFI限制。第二类是保留大部分SIP，只关闭debug限制，再使用`amfidont`或`amfree`对项目路径做允许。仓库里的辅助目标是：

```
make amfidont_allow_vphone
```

它会构建bundle，然后运行`scripts/start_amfidont_f...