---
title: iOS虚拟手机实现原理解析
url: https://mp.weixin.qq.com/s/uGw95eaMC4E-JujsPUJ4pA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:50:52.052956
---

# iOS虚拟手机实现原理解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Sq4BUsrXeTicDbOXGx2D8geVHJLX1EG6NLCNu2J23nyfDG1tx5a4ibyMKRp99MuqJ1icUGn8w4uLRRHTAQU1mzEtHSqGiczNJ7s0ChVKUJWbtA4/0?wx_fmt=jpeg)

# iOS虚拟手机实现原理解析

原创

非虫
非虫

软件安全与逆向分析

![]()

在小说阅读器中沉浸阅读

# iOS虚拟手机实现原理解析

最近推上iOS虚拟手机话题很火，很从我晒了自己动手修改实现的可运行的iOS虚拟手机。

基于`tart`的`super-tart-vphone`项目用起来要20G的空间，这着实有些难受。本文主要从iOS系统框架介绍说起，讲解`vphone-cli`工具一步步实现iOS虚拟手机制作的全过程。

目前`vphone-cli`工具还没有将文件补丁与VM的制作实现全自动化，旦笔者相信，在强大的社区力量的贡献下，要不了多久，iOS虚拟手机/iOS云手机这类自动化的工具会快速的完善起来。届时，想要玩macOS/iOS平台的逆向工程，只需要一台2999元的Mac Mini M4基础款就可以啦！

## 1 项目背景

2024年底，Apple正式推出Private Cloud Compute(以下简称PCC)，声称为云端AI隐私开辟新的方向。PCC的核心是一套运行在Apple Silicon服务器上的虚拟化系统，对外提供安全研究用的虚拟机实例。到2025年底，安全研究者在PCC固件的cloudOS 26版本中发现了一个令人震惊的组件: vphone600ap，即"iPhone Research Environment Virtual Machine"。

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTibibsiarXVYNRABLCEL6BAbhMUIAxsWrg1XNWsmDWmgbMmuXY6xNUJW4KqtpDwYp0E6bOAP9TdibqiaUWvckhfnwxuL90hQ6Ht6pqY/640?wx_fmt=png&from=appmsg)

这意味着Apple在PCC固件内嵌入了完整的虚拟iPhone运行环境。无论这是Apple有意为安全研究者准备的工具，还是一次意外泄露(类似2021年iOS 15 beta中DEVELOPMENT/KASAN内核被包含长达4个月的事件)，社区已经迅速行动，将这一发现转化为可实际运行的虚拟iPhone方案。

经过wh1te4ever、Lakr233等研究者的持续工作，目前已实现在macOS上完整启动iOS 26虚拟机，支持SSH远程访问、VNC图形界面，可以运行SpringBoard和系统应用。对于iOS逆向工程和安全研究来说，这是一个真正可以投入生产环境使用的虚拟化分析平台。

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9y8ReyInzhTQx8A3oKLM8icjicn4ehfosgS1ib48jJDTs3D7AvrZTvYVffrhe33xTV2ibNNfDsDDcGuZXZOzJsVtWDxzKESkxkrw4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT9uIcTpkDkHzxRGpicN4nHsaEibOEXPIYJ40KfBzKFUzAgUMMuBpaCDcM7qKEaodaRNq5Ce9HEFJnoZAvv1pyRSjQy6AChJk8SDA/640?wx_fmt=png&from=appmsg)

上图展示了虚拟iPhone的实际运行效果。通过VNC客户端连接后，可以看到完整的iOS 26用户界面，包括SpringBoard主屏幕、系统设置等原生应用。虚拟机内核版本为Darwin 25.1.0(xnu-12377.42.6)，设备标识为iPhone99,11，硬件型号vresearch101ap。

本文将从Apple提供的Virtualization.framework出发，逐步拆解虚拟iPhone从创建到运行的完整技术实现。涉及的核心仓库包括:

* wh1te4ever/super-tart-vphone: 固件补丁工具集，包含41+处二进制修改
* wh1te4ever/super-tart-vphone-writeup: 完整的技术文档和操作记录
* Lakr233/vphone-cli: 基于Swift的虚拟机启动工具

## 2 Virtualization.framework与私有API

### 2.1 公开框架的能力边界

Apple从macOS 11开始提供Virtualization.framework，用于在Apple Silicon上创建和管理轻量级虚拟机。公开API支持创建macOS和Linux虚拟机，提供CPU、内存、磁盘、网络、图形等外设的配置能力。框架内部使用Hypervisor.framework提供的硬件虚拟化支持，直接利用ARM架构的EL2特权级。

但公开API有一个明确的限制: 只支持macOS和Linux客户机操作系统。iOS从未出现在官方文档的支持列表中。

### 2.2 Platform Version 3与vphone硬件模型

突破口在于Virtualization.framework内部的私有API。通过逆向分析框架二进制，研究者发现了`_VZMacHardwareModelDescriptor`这个未公开的类。该类的`setPlatformVersion:`方法接受一个无符号整数参数，不同的值对应不同的硬件平台:

* PV=1: 标准macOS虚拟机
* PV=2: 未知(可能是服务器配置)
* PV=3: vphone，即虚拟iPhone

创建PV=3硬件模型的核心代码如下:

```
VZMacHardwareModel *VPhoneCreateHardwareModel(void) {
  _VZMacHardwareModelDescriptor *desc = [[_VZMacHardwareModelDescriptor alloc] init];
  [desc setPlatformVersion:3];
  [desc setBoardID:0x90];
  [desc setISA:2];

  VZMacHardwareModel *model = [VZMacHardwareModel _hardwareModelWithDescriptor:desc];
return model;
}
```

其中`boardID:0x90`对应vresearch101板卡标识，`ISA:2`指定ARM64指令集架构。这些参数与PCC固件中的vphone600ap配置完全匹配。

### 2.3 私有API调用清单

整个虚拟iPhone的创建过程依赖11个私有API，通过ObjC桥接层调用，汇总如下:

| 私有类/方法 | C包装函数 | 用途 |
| --- | --- | --- |
| `_VZMacHardwareModelDescriptor` | `VPhoneCreateHardwareModel()` | 创建PV=3硬件模型 |
| `-_setROMURL:` | `VPhoneSetBootLoaderROMURL()` | 指定自定义ROM二进制 |
| `-_setForceDFU:` | `VPhoneConfigureStartOptions()` | 强制DFU模式启动 |
| `_VZGDBDebugStubConfiguration` | `VPhoneSetGDBDebugStubDefault()` | GDB调试支持 |
| `_VZPvPanicDeviceConfiguration` | `VPhoneSetPanicDevice()` | 捕获VM panic |
| `-_setCoprocessors:` | `VPhoneSetCoprocessors()` | 配置SEP等协处理器 |
| `-_setProductionModeEnabled:` | `VPhoneDisableProductionMode()` | 禁用生产模式 |
| `-_setDataValue:forNVRAMVariableNamed:` | `VPhoneSetNVRAMVariable()` | 设置NVRAM启动参数 |
| `_VZPL011SerialPortConfiguration` | `VPhoneCreatePL011SerialPort()` | ARM PL011串口 |
| `_VZUSBTouchScreenConfiguration` | `VPhoneConfigureMultiTouch()` | USB多点触控 |
| `_VZSEPCoprocessorConfiguration` | `VPhoneConfigureSEP()` | Secure Enclave配置 |

表2-1 虚拟iPhone私有API清单

这些API都位于Virtualization.framework内部，以下划线开头，不在公开头文件中暴露。由于ObjC的动态特性，可以通过`NSClassFromString`和`performSelector`在运行时访问。

### 2.4 Entitlements权限体系

使用私有API还不够，macOS在执行虚拟化操作前会检查进程的代码签名权限(Entitlements)。虚拟iPhone要求以下5项权限:

```
<dict>
<key>com.apple.security.virtualization</key>
<true/>
<key>com.apple.private.virtualization</key>
<true/>
<key>com.apple.private.virtualization.security-research</key>
<true/>
<key>com.apple.vm.networking</key>
<true/>
<key>com.apple.security.get-task-allow</key>
<true/>
</dict>
```

其中`com.apple.private.virtualization`授权访问私有虚拟化API，`com.apple.private.virtualization.security-research`是PV=3专属权限，缺少任何一项都会导致VM创建失败。

在正常情况下，私有Entitlements只有Apple签名的系统二进制才能使用。要让自编译的vphone-cli获得这些权限，必须禁用系统完整性保护(SIP)和Apple Mobile File Integrity(AMFI):

```
# 恢复模式下执行
csrutil disable
csrutil allow-research-guests enable

# 重启后在macOS中执行
sudo nvram boot-args="amfi_get_out_of_my_way=1 -v"
```

然后使用Ad-hoc签名将Entitlements附加到二进制:

```
codesign --force --sign - --entitlements vphone.entitlements .build/release/vphone-cli
```

## 3 环境准备与工具链

### 3.1 macOS系统配置

虚拟iPhone要求macOS 15.0(Sequoia)或更新版本，运行在Apple Silicon设备上。系统配置分三步:

第一步，进入恢复模式。长按电源键直到屏幕显示"Loading boot options"，在恢复模式的Terminal中执行:

```
csrutil disable
csrutil allow-research-guests enable
```

第二步，重启进入macOS后设置启动参数:

```
sudo nvram boot-args="amfi_get_out_of_my_way=1 -v"
```

第三步，再次重启使参数生效。

### 3.2 libimobiledevice套件编译

整个固件操作流程依赖libimobiledevice生态系统，需要从源码编译以下组件:

```
libplist         -> plist解析
libimobiledevice -> iOS设备通信协议
libusbmuxd       -> USB复用守护进程
libirecovery     -> 恢复模式通信(需添加vresearch101设备定义)
idevicerestore   -> 固件恢复工具
```

其中libirecovery需要添加虚拟设备的硬件标识才能正确识别vphone:

```
{ "iPhone99,11", "vresearch101ap", 0x90, 0xFE01, "iPhone 99,11" },
```

vphone-cli项目提供了一键编译脚本:

```
zsh Scripts/compile_all_libimobiledevice_deps.sh
```

### 3.3 Python依赖

固件补丁脚本使用Python3编写，依赖三个关键库:

```
pip3 install capstone keystone-engine pyimg4
```

* capstone: 多架构反汇编引擎，用于分析ARM64指令
* keystone-engine: 多架构汇编引擎，用于生成补丁指令
* pyimg4: Apple Image4格式处理，用于IM4P文件的解包和重打包

### 3.4 vphone-cli编译与签名

vphone-cli是一个Swift Package Manager项目，使用ObjC桥接层调用私有API。编译和签名一步完成:

```
./build_and_sign.sh
```

该脚本执行三个操作:

```
# 1. Release模式编译
swift build -c release

# 2. 使用Entitlements签名
codesign --force --sign - --entitlements vphone.entitlements .build/release/vphone-cli

# 3. 验证签名
codesign -d --entitlements - .build/release/vphone-cli
```

验证输出应包含全部5项权限:

```
[Dict]
    [Key] com.apple.private.virtualization
    [Value]
        [Bool] true
    [Key] com.apple.private.virtualization.security-research
    [Value]
        [Bool] true
    ...
```

## 4 固件准备与混合策略

### 4.1 两份固件的来源

虚拟iPhone的固件并非来自单一来源，而是将iPhone OS和cloudOS PCC两份固件进行"杂交"。这是因为PCC固件包含vresearch101平台的引导链(iBSS/iBEC/LLB/内核等)，而iPhone IPSW包含完整的iOS用户空间(Cryptex/SystemOS/AppOS)。

需要下载的固件:

```
iPhone OS:  iPhone17,3_26.1_23B85_Restore.ipsw
cloudOS:    PCC-CloudOS-26.1-23B85固件
```

iPhone固件可通过Apple CDN直接获取，cloudOS固件通过PCC安全研究工具下载。

### 4.2 PCC虚拟机模板创建

在合并固件之前,需要先通过Apple提供的pccvre工具创建一个PCC研究虚拟机作为模板:

```
sudo /System/Library/SecurityResearch/usr/bin/pccvre
cd /System/Library/SecurityResearch/usr/bin/
./pccvre release list
./pccvre release download --release 35622
./pccvre instance create -N pcc-research -R 35622 --variant research
```

创建完成后，模板虚拟机位于:

```
~/Library/Application Support/com.apple.security-research.vrevm/VM-Library/pcc-research.vm
```

从中需要提取以下文件:

```
AuxiliaryStorage    -> NVRAM辅助存储
Disk.img            -> 磁盘镜像
SEPStorage          -> Secure Enclave存储
config.plist        -> 虚拟机配置
```

另外还需要从系统Virtualization.framework中复制ROM文件:

```
/System/Library/Frameworks/Virtualization.framework/Versions/A/Resources/AVPBooter.vresearch1.bin
/System/Library/Frameworks/Virtualization.framework/Versions/A/Resources/AVPSEPBooter.vresearch1.bin
```

### 4.3 固件合并流程

prepare\_firmware.sh脚本负责将两份固件合并为虚拟iPhone可用的混合固件。核心操作是将cloudOS的引导链组件覆盖到iPhone IPSW目录:

```
# 内核缓存(来自cloudOS)
cp${CLOUDOS_DIR}/kernelcache.* "$IPHONE_DIR"/

# 引导链、设备树等固件组件(来自cloudOS)
for sub in agx all_flash ane dfu pmp; do
cp${CLOUDOS_DIR}/Firmware/${sub}/* "$IPHONE_DIR/Firmware/${sub}"/
done
cp${CLOU...