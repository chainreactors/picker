---
title: Pixel 4A 集成KernelSU小记
url: https://mp.weixin.qq.com/s/UG_6Ta8HjY7sLWiMyegr0g
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:24:13.793279
---

# Pixel 4A 集成KernelSU小记

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1uhnrtZXL04ogswfUSbibmibp8DWQKSjY8TsLKHIO56OQFJW3snv6xCtBAg67uXsic3dG7ZVVGzicKiamuzOYKKYzialXhquib9ibw9bxM/0?wx_fmt=jpeg)

# Pixel 4A 集成KernelSU小记

原创

十月的进阶之路
十月的进阶之路

十月的进阶之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 写在前面

江湖传闻`KernelSU`乃`root`神器，无需修改系统分区，隐藏性极佳，但5.10以下内核只能结合源码自己编译，虽然社区提供了多个版本的镜像，但是不巧的是就是没有pixel4a的。于是在下决定为手头的`Pixel 4a`（代号`sunfish`）量身定制一个带`KernelSU`的内核。回头看看，用`GKI`内核启动`sunfish`专属设备（扑街）、关了不该关的驱动导致`ADSP`罢工（再扑街）、修改了`vermagic`不合导致模块一个都加载不起来（继续扑街）。**想让自编译内核乖乖加载vendor分区的闭源模块，vermagic得一致、CRC校验要跳过、驱动配置不能冲突。**

## 第一话：兵马未动，粮草先行

首先，把编译环境理顺。在下用的是`Ubuntu 20.04`虚拟机，工具链是从`LineageOS`提取的`Android`专用`Clang。`

```
# 工作目录
/mnt/sda1/shiyue/
├── sunfish-kernel/          # Pixel 4a 专属内核源码
├── KernelSU-0.9.5/          # 注意版本！非GKI设备只能到0.9.5
├── clang/clang-r416183b/    # Android专用工具链
├── magiskboot/              # boot.img解包打包工具
└── factory/                 # 原厂镜像备份
```

**关键工具链配置:**原厂内核版本是`4.14.302-g92e0d94b6cba，由``clang 12.0.5 (r416183b)` 编译。这意味着我们的工具链版本必须对上号，否则`vermagic`不匹配，`vendor`模块全部罢工。

先从原厂`vendor.img`里看看模块的庐山真面目：

```
sudo mount -o loop,ro vendor.img vendor_mount
modinfo vendor_mount/lib/modules/adsp_loader_dlkm.ko | grep vermagic
# 输出: vermagic: 4.14.302-g92e0d94b6cba SMP preempt mod_unload modversions aarch64
```

注意那个`modversions`标志——这意味着每个内核符号都有`CRC`校验值。

## 第二话：集成KernelSU与手动Hook

`KernelSU 0.9.5`是官方对`4.14`内核的最后支持版本。集成三步走：

```
# 1. 复制KernelSU驱动代码
cp -r KernelSU-0.9.5/kernel sunfish-kernel/drivers/kernelsu

# 2. 修改 drivers/Kconfig（在endmenu前添加）
echo 'source "drivers/kernelsu/Kconfig"' >> drivers/Kconfig

# 3. 修改 drivers/Makefile
echo 'obj-$(CONFIG_KSU) += kernelsu/' >> drivers/Makefile
```

然后是最关键的**手动Hook注入。**因为关闭了`CONFIG_KPROBES，``KernelSU`需要手动在五个关键路径插入钩子：

```
// fs/exec.c - do_execveat_common() 函数前
extern bool ksu_execveat_hook __read_mostly;
extern int ksu_handle_execveat(...);
// 函数体内：
if (unlikely(ksu_execveat_hook))
    ksu_handle_execveat(&fd, &filename, &argv, &envp, &flags);
else
    ksu_handle_execveat_sucompat(&fd, &filename, &argv, &envp, &flags);
```

同样在`fs/open.c、``fs/read_write.c、``fs/stat.c、``fs/devpts/inode.c` 中注入对应`Hook。`具体代码参考`KernelSU`官方非`GKI`集成文档，这里不逐一赘述。

但有一个坑：`KernelSU`版本号。因为我们的`drivers/kernelsu`不是`git`子模块，版本号回落到默认值`16，``Manager`会报"版本过低"。在 `drivers/kernelsu/Makefile` 中硬编码：

```
ccflags-y += -DKSU_VERSION=11872
```

## 第三话：defconfig——成败在此一举

这是最烧脑的一关，因为`Pixel 4a`的触摸屏、振动器、`ADSP`等驱动都是以 `.ko` 模块形式躺在`vendor`分区的闭源二进制文件。

**我们要做到：**让内核的符号表与这些闭源模块兼容。经过实验，关键配置如下：

```
# arch/arm64/configs/sunfish_defconfig 关键修改：
CONFIG_MODVERSIONS=y          # 必须！匹配模块的modversions标志
CONFIG_MODULE_FORCE_LOAD=y    # 辅助：允许强制加载
CONFIG_LOCALVERSION="-g92e0d94b6cba"  # vermagic字符串一模不两样
CONFIG_LOCALVERSION_AUTO=n    # 别自动追加dirty后缀

# KernelSU配置
CONFIG_KSU=y
CONFIG_KSU_MANUAL_HOOK=y

# 这三个驱动绝对不能built-in，必须用vendor的.ko！
CONFIG_TOUCHSCREEN_HEATMAP=m
CONFIG_INPUT_DRV2624_HAPTICS=m
# CONFIG_TOUCHSCREEN_ST is not set   # 内核自带的不含TBN支持，删掉！
```

**一个教训:**如果你把 `TOUCHSCREEN_HEATMAP` 或 `DRV2624` 设成 `=y，`它们会与`vendor`的 `.ko` 产生符号冲突，导致 `ftm5.ko`（触摸屏）加载失败。

## 第四话：CRC校验——一场不对等的战争

配置搞定，编译刷机。结果？`/proc/modules` 一行都没有！

原来开启了 `CONFIG_MODVERSIONS` 之后，内核加载模块时会逐个校验符号`CRC。`我们用 `objdump -s -j __versions` 查看闭源模块期望的`CRC，`再用自编译内核的 `Module.symvers` 对比，发现：

|  |  |  |  |
| --- | --- | --- | --- |
| 符号 | 模块期望CRC | 自编译内核CRC | 结论 |
| module\_layout | 0x92a602f9 | 0x6147625b | ❌ 不匹配 |
| printk | 0x985558a1 | 0x985558a1 | ✅ 匹配 |

根源在于我们去除`LTO/CFI`改变了 `module_layout` 的结构体布局。`CRC`值不对，模块一个都加载不了。

**暴力解法**——修改 `kernel/module.c，`跳过所有`CRC`校验：

```
// 约1282行，check_version() 函数体直接改成：
static int check_version(...) { return 1; }

// 约1331行，check_modstruct_version() 同理：
static inline int check_modstruct_version(...) { return 1; }
```

重新编译，`/proc/modules` 终于出现了36个模块。

## 第五话：最后的钉子——触摸屏不灵

模块加载了，系统能进桌面，能adb连接，但屏幕戳烂都没反应。

检查 `/proc/modules，`发现少了 `ftm5.ko、``heatmap.ko、``drv2624.ko` 这三位。回头看defconfig——我之前脑子一热把他们设成`=y`了！Vendor分区里又有同样的模块，符号冲突导致加载失败。

修正：

```
# 删除CONFIG_TOUCHSCREEN_ST（不支持=m），其他改成模块
# CONFIG_TOUCHSCREEN_ST is not set
CONFIG_TOUCHSCREEN_HEATMAP=m
CONFIG_INPUT_DRV2624_HAPTICS=m
```

重新编译刷机，`getevent -l` 终于出现了 `fts` 设备节点。

## 大结局：完整编译打包流程

```
cd /mnt/sda1/shiyue/sunfish-kernel

# 1. 生成.config（必须mrproper确保配置干净）
make mrproper
make ARCH=arm64 \
  CC=/mnt/sda1/shiyue/clang/clang-r416183b/clang/bin/clang-wrap \
  LD=/mnt/sda1/shiyue/clang/clang-r416183b/clang/bin/ld.lld \
  CLANG_TRIPLE=aarch64-linux-gnu- \
  CROSS_COMPILE=aarch64-linux-gnu- \
  CROSS_COMPILE_ARM32=arm-linux-gnueabihf- \
  LLVM=1 LLVM_IAS=1 \
  sunfish_defconfig

# 2. 编译（增量编译可省略mrproper和defconfig步骤）
make -j$(nproc) ARCH=arm64 \
  CC=/mnt/sda1/shiyue/clang/clang-r416183b/clang/bin/clang-wrap \
  LD=/mnt/sda1/shiyue/clang/clang-r416183b/clang/bin/ld.lld \
  CLANG_TRIPLE=aarch64-linux-gnu- \
  CROSS_COMPILE=aarch64-linux-gnu- \
  CROSS_COMPILE_ARM32=arm-linux-gnueabihf- \
  LLVM=1 LLVM_IAS=1 \
  LOCALVERSION="" \
  Image.lz4 2>&1 | tee /mnt/sda1/shiyue/output/build-final.log

# 3. 打包boot.img
cp arch/arm64/boot/Image.lz4 /mnt/sda1/shiyue/magiskboot/fresh_unpack/kernel
cd /mnt/sda1/shiyue/magiskboot/fresh_unpack
../magiskboot repack stock-boot.img ../output/new-boot.img

# 4. 刷入测试（先临时启动，确认无误再正式写入）
fastboot boot new-boot.img
# 验证模块加载：/proc/modules 应显示39个，包含ftm5、heatmap、drv2624
# 验证触摸：getevent -l 应出现 fts 设备，触摸正常
# 确认无误后：
fastboot flash boot new-boot.img

# 5. 安装KernelSU Manager (v0.9.5对应版本)
adb install KernelSU_v0.9.5_11872-release.apk
```

## 镜像获取

在公众号后台回复`KernelSU，`你将获取完整的项目源码，以及编译好的`sunfish-KernelSU.img`可直接刷入测试，不过对于设备刷入后可能出现的各类问题，本文不作任何保障与承诺，最后丢张图镇楼。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uWkPXMB5ibELkKPdhkWZhvkvdic3MjMpEa32jYJplDdn6AAA3KBK9gB5qBzZNZl13KhPcF6ptHMibVcCXyicEHDe3eXpfIEgn1lwM/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

十月的进阶之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

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