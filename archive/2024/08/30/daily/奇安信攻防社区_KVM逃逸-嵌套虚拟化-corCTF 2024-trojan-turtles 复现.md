---
title: KVM逃逸-嵌套虚拟化-corCTF 2024-trojan-turtles 复现
url: https://forum.butian.net/share/3689
source: 奇安信攻防社区
date: 2024-08-30
fetch_date: 2025-10-06T18:02:20.317721
---

# KVM逃逸-嵌套虚拟化-corCTF 2024-trojan-turtles 复现

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### KVM逃逸-嵌套虚拟化-corCTF 2024-trojan-turtles 复现

* [CTF](https://forum.butian.net/topic/52)

一直对虚拟化技术比较感兴趣，前段时间尝试了qemu逃逸和vmware逃逸的例题，这次2024corctf发现一道KVM嵌套虚拟化逃逸的题目，来了兴趣，但个人接触CTF时间还不到1年，思路方面还是受阻了很多，当时就把相关KVM和VMX源码大致逻辑看了看，赛后找shellphish团队要了一份wp来学习，在此写下复现记录

参考
==
<https://zolutal.github.io/corctf-trojan-turtles/>
<https://eqqie.cn/index.php/archives/1972>
前言
==
一直对虚拟化技术比较感兴趣，前段时间尝试了qemu逃逸和vmware逃逸的例题，这次2024corctf发现一道KVM嵌套虚拟化逃逸的题目，来了兴趣，但个人接触CTF时间还不到1年，思路方面还是受阻了很多，当时就把相关KVM和VMX源码大致逻辑看了看，赛后找shellphish团队要了一份wp来学习，在此写下复现记录
KVM（Kernel-based Virtual Machine）
=================================
### KVM 的概念
KVM 是一种基于 Linux 内核的虚拟化技术，它允许 Linux 内核充当虚拟机监控器 (VMM) 或 hypervisor。KVM 的主要目的是提供一个统一的接口，使用户空间程序能够利用硬件虚拟化特性（如 Intel 的 VMX 和 AMD 的 SVM）来创建和管理虚拟机。
### KVM 的实现
KVM 通过一个名为 `/dev/kvm` 的字符设备驱动程序实现。该驱动程序提供了一系列 ioctl (输入输出控制) 命令，用于管理和控制虚拟机 (VM) 的状态和行为。
#### ioctl 命令
ioctl 命令是一种通用的机制，用于在用户空间程序和内核空间之间传递控制信息。KVM 设备驱动程序提供了许多 ioctl 命令，这些命令用于配置虚拟机的状态、设置寄存器值、加载虚拟机的内存映射、控制虚拟机的执行等。
- \*\*KVM\\_SET\\_REGS\*\*:
- 该命令用于设置虚拟机的寄存器状态。
- 用户空间程序可以使用此命令来将通用寄存器写入 vcpu的通用寄存器中。
#### KVM API 文档
- \*\*API 文档\*\*:
- 更多关于 KVM API 的详细信息可以在 Linux 内核文档中找到，具体链接为：<https://docs.kernel.org/virt/kvm/api.html>
- 这些文档详细介绍了可用的 ioctl 命令、参数结构和如何使用它们来控制虚拟机。
### KVM 的编译选项
KVM 可以以不同的形式集成到 Linux 内核中，具体取决于编译时的选择：
- \*\*编译到内核中\*\*:
- 如果在内核配置中将 `CONFIG\_KVM\_INTEL` 设置为 `y`，则 KVM 将被编译到内核映像中。
- 这意味着 KVM 成为内核的一部分，无需加载额外的模块即可使用。
- \*\*编译为内核模块\*\*:
- 如果 `CONFIG\_KVM\_INTEL` 设置为 `m`，那么 KVM 将被编译为一个可加载的内核模块。
- 这意味着 KVM 功能可以通过动态加载模块的方式启用或禁用，提供了更大的灵活性。
### QEMU 与 KVM 的结合
QEMU 是一个通用的全系统仿真器，它可以模拟多种硬件架构。当与 KVM 结合使用时，QEMU 可以利用 KVM 提供的硬件加速功能来提高虚拟机的性能。
- \*\*使用 KVM\*\*:
- 当您使用 `--enable-kvm` 参数启动 QEMU 时，QEMU 将使用 KVM API 来运行虚拟机。
- 这意味着 QEMU 将利用硬件虚拟化特性，而不是完全通过软件进行模拟。
- 结果是提高了虚拟机的性能，减少了 CPU 开销。
- \*\*不使用 KVM\*\*:
- 如果没有使用 `--enable-kvm` 参数，QEMU 将通过纯软件模拟的方式来运行虚拟机。
- 这种模式下的性能通常较低，因为它需要 QEMU 在用户空间中模拟所有的硬件细节。
### 工作原理
1. \*\*初始化\*\*：当 KVM 被启动时，它会检查硬件是否支持虚拟化，并初始化必要的数据结构。
2. \*\*创建虚拟机\*\*：用户空间的应用程序通过系统调用告知内核创建一个新的虚拟机实例。
3. \*\*配置虚拟机\*\*：应用程序通过一系列系统调用来配置虚拟机的硬件（如内存大小、CPU 数量等）和加载操作系统镜像。
4. \*\*运行虚拟机\*\*：一旦配置完成，应用程序可以启动虚拟机。此时，KVM 会接管虚拟机的操作并确保它们正确地执行。
5. \*\*特权指令处理\*\*：当虚拟机尝试执行特权指令时，这些指令会被捕获并传递给 KVM，由 KVM 在宿主机上模拟执行或直接在硬件上执行（如果支持的话）。
嵌套虚拟化（虚拟机里再建一个虚拟机）
==================
当我们说"处理器现在可以执行VMX(虚拟化)相关的指令了"，这意味着CPU获得了执行一系列特殊指令的能力，这些指令专门用于虚拟化操作。
1. VMX指令集：
- Intel处理器有一组特殊的指令，专门用于虚拟化，称为VMX（Virtual Machine Extensions）指令。
- 这些指令包括VMXON, VMXOFF, VMLAUNCH, VMRESUME, VMREAD, VMWRITE等。
2. 指令的作用：
- 这些指令允许操作系统或虚拟机管理器（如VMware, VirtualBox）创建和管理虚拟机。
- 它们提供了硬件级别的支持，使虚拟化更高效、更安全。
3. 启用前后的区别：
- 启用VMXE位之前：如果尝试执行这些VMX指令，处理器会产生一个异常（通常是非法指令异常）。
- 启用VMXE位之后：处理器能够正确识别和执行这些指令。
4. 实际应用例子：
假设你要在电脑上运行一个虚拟机：
- 启用VMXE之前：虚拟机软件只能通过纯软件模拟来运行虚拟机，效率较低。
- 启用VMXE之后：虚拟机软件可以利用这些硬件指令，大大提高虚拟机的运行效率。
嵌套虚拟化的系统中虚拟机执行vmx指令（对虚拟机中的虚拟机的相关操作）
===================================
[vmx指令相关使用](https://wiki.osdev.org/VMX#VMCS)
1. 初始状态：
- L0: 主机VMM (Hypervisor)
- L1: 第一层虚拟机，运行自己的VMM
- L2: 第二层虚拟机（可选）
2. L1执行VMX指令：
a. 指令拦截：
- L1尝试执行VMX指令
- 硬件检测到这是一个需要特殊处理的指令
b. VM Exit到L0：
- 控制权从L1转移到L0 VMM
- L0 VMM获得关于VM Exit原因的信息
c. L0 VMM分析：
- 确定是VMX指令导致的退出
- 检查L1的权限和当前状态
d. 模拟执行：
- L0 VMM不会直接执行该指令
- 相反，它模拟指令的效果
e. 虚拟VMCS操作：
- 如果指令涉及VMCS操作，L0会操作分配给L1的虚拟VMCS
- 虚拟VMCS是实际VMCS的一个"影子"或模拟
f. 状态更新：
- L0更新L1的虚拟状态，使其看起来好像指令已经执行
g. VM Entry回到L1：
- L0完成模拟后，将控制权返回给L1
- L1继续执行，就像它直接执行了VMX指令一样
3. 特殊情况 - L1创建L2：
a. L1执行VMLAUNCH/VMRESUME：
- 用于启动或恢复L2虚拟机
b. L0拦截并模拟：
- L0创建或配置用于L2的新虚拟VMCS
- 设置必要的嵌套虚拟化结构
c. 实际VM Entry：
- L0执行真正的VM Entry进入L2
- L2开始执行，认为它是由L1直接管理的
4. L2执行需要VM Exit的操作：
a. 硬件VM Exit到L0：
- 控制权直接转到L0，不经过L1
b. L0决策：
- 决定是否需要通知L1
- 如果需要，模拟一个从L2到L1的VM Exit
- 否则，L0自己处理并返回到L2
5. 优化和硬件支持：
- 现代处理器提供如VMCS Shadowing等功能
- 这些功能可以减少VM Exit的次数，提高性能
6. 循环继续：
- 这个过程不断重复，处理L1和L2的各种操作
镜像文件qcow2/上传exp/调试
==================
- 安装了 QEMU 的工具 ```bash
# 对于 Debian/Ubuntu:
sudo apt-get install qemu-utils
```
```php
接下来，检查 `.qcow2` 文件的信息：
```bash
qemu-img info chall.qcow2
```
- 挂载查看文件并修改
```bash
sudo guestmount -a chall.qcow2 -m /dev/sda /mnt/qcow2
cd /mnt/qcow2
```
```php
root@ubuntu:/mnt/qcow2# ls
bin dev etc home lib lost+found media mnt opt proc root run sbin srv sys tmp usr var vm
```
```bash
tree -L 2
```
发现有这个玩意，应该就是虚拟机对应的镜像了和文件系统和启动脚本了，将其虚拟机的文件系统解压查看然后添加exp模块进去再打包再起虚拟机就行了
```php
└── vm
├── bzImage
├── initramfs.cpio
└── run-vm.sh
```
分别安装相关内核库,这里是要生成对应的虚拟机中的内核模块，然后加载模块进而逃逸到主机
```bash
sudo dpkg -i linux-hwe-5.15-headers-5.15.0-107\_5.15.0-107.117~20.04.1\_all.deb
sudo dpkg -i linux-headers-5.15.0-107-generic\_5.15.0-107.117~20.04.1\_amd64.deb
ls /usr/lib/modules/5.15.0-107-generic/build
```
exp.c下的Makefile，/usr/lib/modules/5.15.0-107-generic/build目录下一般也有，没就建一个就好了
```bash
obj-m += exp.o
KDIR := /usr/lib/modules/5.15.0-107-generic/build
PWD := $(shell pwd)
all:
make -C $(KDIR) M=$(PWD) modules
clean:
make -C $(KDIR) M=$(PWD) clean
```
然后make就可以生成了
漏洞
==
虚拟机进行相关vmx指令或者说嵌套虚拟化时由于相关vmx指令会被检测到是特殊指令会触发VMexit，然后宿主机VMM来处理该特殊指令
diff
----
diff点在于handle\\_vmread和handle\\_vmwrite函数
```c
\_\_int64 \_\_fastcall handle\_vmwrite(\_\_int64 a1, int a2, int a3, int a4, int a5, int a6){
{
………
………
if ( kvm\_get\_dr(a1, 0LL) == 0x1337BABE )
{
dr = kvm\_get\_dr(a1, 1LL);
\*(\_QWORD \*)(v7 + 8 \* dr) = kvm\_get\_dr(a1, 2LL);
}
………
}
\_\_int64 \_\_fastcall handle\_vmread(\_\_int64 a1, int a2, int a3, int a4, int a5, int a6)
{
…………
if ( kvm\_get\_dr(a1, 0LL) == 0x1337BABE )
{
dr = kvm\_get\_dr(a1, 1LL);
kvm\_set\_dr(a1, 2LL, \*(\_QWORD \*)(v6 + 8 \* dr));
}
…………………
}
```
```c
static inline struct vmcs12 \*get\_shadow\_vmcs12(struct kvm\_vcpu \*vcpu)
{
return to\_vmx(vcpu)->nested.cached\_shadow\_vmcs12;
}
static \_\_always\_inline struct vcpu\_vmx \*to\_vmx(struct kvm\_vcpu \*vcpu)
{
return container\_of(vcpu, struct vcpu\_vmx, vcpu);
}
#define container\_of(ptr, type, member) ({ \
void \*\_\_mptr = (void \*)(ptr); \
static\_assert(\_\_same\_type(\*(ptr), ((type \*)0)->member) || \
\_\_same\_type(\*(ptr), void), \
"pointer type mismatch in container\_of()"); \
((type \*)(\_\_mptr - offsetof(type, member))); })
```
漏洞点
---
- handle\\_vmwrite会从第struct kvm\\_vcpu的arch.db\[0\]对应的内容，如果是0x1337BABE，然后会取第struct kvm\\_vcpu的arch.db\[1\]对应的内容为dr，然后会取第struct kvm\\_vcpu的arch.db\[2\]对应的内容赋值给 struct vmcs12 \*+8\*dr对应的地址所在内容
`\*（struct vmcs12 \*+8\*struct kvm\_vcpu的arch.db[0]）=struct kvm\_vcpu的arch.db[2]`
- handle\\_vmread会从第struct kvm\\_vcpu的arch.db\[0\]对应的内容，如果是0x1337BABE，然后会取第struct kvm\\_vcpu的arch.db\[1\]对应的内容为dr，然后会将 struct vmcs12 \*+8\*dr对应的地址的内容赋值给struct kvm\\_vcpu的arch.db\[2\]
`struct kvm\_vcpu的arch.db[2]= \*（struct vmcs12 \*+8\*struct kvm\_vcpu的arch.db[0]）`
可以相对struct vmcs12 \\*的任意地址读写，而且这个 vmcs12指向的是我们在虚拟机分配的vmcs在主机上的地址，为什么呢？因为这个地方是处理虚拟机执行vmx指令的，而vmread指令是从控制的虚拟机的vmcs里读取相关字段，而虚拟机执行vmread会陷入到主机的vmm中去，然后再去处理虚拟机的vmread，所以这里的vmcs自然也是虚拟机控制的虚拟机的VMCS了
这就相当于主机的任意地址读写了（但这里的struct kvm\\_vcpu \\*vcpu还是虚拟机的，不是虚拟机里的虚拟机的）
思路
==
vmx相关初始化
--------
[vmx指令相关使用](https://wiki.osdev.org/VMX#VMCS)
为了能够执行 vmread/vmwrite 指令，需要进行一些设置。vmread 和 vmwrite 指令用于与“虚拟机控制结构”(VMCS) 交互，在虚拟机机中执行就是和嵌套虚拟机的VMCS交互，所以首先虚拟机要开启VMX模式（嵌套虚拟机化），这样才能嵌套虚拟化，所以没有嵌套虚拟机的VMCS，自然vmread指令和vmwrite无法使用
首先是分配并初始化VMXON Region和嵌套虚拟机实例对应的VMCS Region
```c
vmxon\_page = kmalloc(4096, GFP\_KERNEL);
memset(vmxon\_page, 0, 4096);
vmcs\_page = kmalloc(4096, GFP\_KERNEL);
memset(vmcs\_page, 0, 4096);
vmxon\_page\_pa = virt\_to\_phys(vmxon\_page);
vmcs\_page\_pa = virt\_to\_phys(vmcs\_page);
printk("vmxon\_page %p --- vmxon\_page\_pa %p",vmxon\_page,vmxon\_page\_pa);
printk...