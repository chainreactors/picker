---
title: ATF-FUZZ
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458554341&idx=1&sn=6755dbe6ed0d8ccd6ca2b7cf31be33fd&chksm=b18dbf6f86fa3679e5764443a6bd014d7fb305f0e7245fef913e51048b3fef7517d73d11c885&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-05-12
fetch_date: 2025-10-06T17:16:56.893499
---

# ATF-FUZZ

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F58BEbw642jdrS1Geofo5QeribC6Iku4NMom77YhUrFmVjZwEac94BX7m9sXFpV5upyyqT4O8jJeg/0?wx_fmt=jpeg)

# ATF-FUZZ

iosmosis

看雪学苑

```
一

FVP环境搭建
```

###

### FVP下载

https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QAp3dVvaLicBg02M8LLibEibDibkCnCLaWx1sxHbbmA2P5LoiczQwRllENKA/640?wx_fmt=png&from=appmsg)

下载完成后解压的到`Base_RevC_AEMvA_pkg。`

```
sudo apt install xterm
tar -xzvf FVP_Base_RevC-2xAEMvA_11.25_15_Linux64.tgz
# Base_RevC_AEMvA_pkg
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QDpfgVHOIvPRtuFWVNVMkibhPSwWzdY7HthNc6OqDsUSts6bFVE3WBIg/640?wx_fmt=png&from=appmsg)

注意对应的binary文件在`AEMv8R_base_pkg/models/Linux64_GCC-9.3`目录下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QMlTribXaOBEYvD2V7qVTXUCpsN4OrrFwpia2gCPSf8dicTOTqbfPRrO6g/640?wx_fmt=png&from=appmsg)

FVP的快捷的两种启动方法：1. ARM Develop Studio可视化启动 2.command line启动。本教程主要使用command line方式启动。

```
二

BL33构建
```

BL33作为None-security world镜像，一般情况下为uboot，当然也可以直接跳转到kernel。

```
export CROSS_COMPILE=/data/toolchains/SYS_PUBLIC_TOOLS/.toolchain/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu-linux-5.10/bin/aarch64-none-linux-gnu-
git clone https://github.com/u-boot/u-boot.git
cd u-boot
make vexpress_aemv8a_semi_defconfig
make -j 9
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QBp9g8u2E0QZX0F0ZTXRUg2L7rjS1jzicPYP9NZqZiaE1DWoYbC9q9u3w/640?wx_fmt=png&from=appmsg)

##

```
三

ATF构建
```

```
cd /data/Project/arm-trusted-firmware-lts-v2.8.4/
export CROSS_COMPILE=/data/toolchains/SYS_PUBLIC_TOOLS/.toolchain/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu-linux-5.10/bin/aarch64-none-linux-gnu-

// 调试编译
make PLAT=fvp BL33=/data/Project/u-boot/u-boot.bin DEBUG=1 all fip
// 正常编译
make PLAT=fvp BL33=/data/Project/u-boot/u-boot.bin all fip
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QOA2ttaXXHD57CPvicUj5ZL1kdXJ9nnl627fYbjrP0Rjj0pJ5e3zNxGw/640?wx_fmt=png&from=appmsg)

##

```
四

ATF运行
```

###

### AEMv8 Base FVP

使用`FVP_Base_RevC-2xAEMv8A`运行。

```
cd /data/Project/arm-trusted-firmware-lts-v2.8.4/build/fvp/debug/
export DISPLAY=:0
```

运行命令：

```
/data/Project/Base_RevC_AEMvA_pkg/models/Linux64_GCC-9.3/FVP_Base_RevC-2xAEMvA \
-C pctl.startup=0.0.0.0                                     \
-C bp.secure_memory=1                                       \
-C bp.tzc_400.diagnostics=1                                 \
-C cluster0.NUM_CORES=4                                     \
-C cluster1.NUM_CORES=4                                     \
-C cache_state_modelled=1                                   \
-C bp.secureflashloader.fname="./bl1.bin"      \
-C bp.flashloader0.fname="./fip.bin"

# 如果需要运行到rootfs请添加下方参数，
--data cluster0.cpu0="<path-to>/<kernel-binary>"@0x80080000 \
--data cluster0.cpu0="<path-to>/<ramdisk>"@0x84000000
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QOUG39b0lAseRVic2LYEicNawAT2XsSibCrdAQYZaFQAQj1f10qjzCOzOQ/640?wx_fmt=png&from=appmsg)

```
五

TF-A Tests构建并运行
```

```
export CROSS_COMPILE=/data/toolchains/SYS_PUBLIC_TOOLS/.toolchain/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu-linux-5.10/bin/aarch64-none-linux-gnu-
git clone https://review.trustedfirmware.orgTF-A/tf-a-tests.git
cd tf-a-tests
make PLAT=fvp tftf
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QnqYxiaqP6ibrm8wW2r2KQDA5xm7ejUiaQuhibiakVHWut8Tr2eqDo5Rcumw/640?wx_fmt=png&from=appmsg)

重编译ATF，指定bl33.bin为tftf.bin

```
cd /data/Project/arm-trusted-firmware-lts-v2.8.4/
export CROSS_COMPILE=/data/toolchains/SYS_PUBLIC_TOOLS/.toolchain/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu-linux-5.10/bin/aarch64-none-linux-gnu-
make PLAT=fvp BL33=/data/Project/tf-a-tests/build/fvp/release/tftf.bin all fip
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QqCqhcGQQYRVv8tvQx8jeERQ4OGgohvGIevxYm6aF0HicWSUv0XQ0qgg/640?wx_fmt=png&from=appmsg)

重新使用FVP运行，成功引导进入tftf中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QG8UGQpUGPMibB3LqUIOicibMYvEYDbHicFbxRm6dDCPklglJiawjK8c2Alg/640?wx_fmt=png&from=appmsg)

运行完成后会输出测试结果并提示退出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QZnjH3iaMJdgwInZiatNicY02VROkpACKsXGQTYSD55l9wJAjlT7tsuBOQ/640?wx_fmt=png&from=appmsg)

##

```
六

SMC Fuzz
```

推荐阅读：https://www.trustedfirmware.org/docs/Directed\_Radomized\_SMC\_Presentation.pdf

###

### 默认配置运行

```
export CROSS_COMPILE=/data/toolchains/SYS_PUBLIC_TOOLS/.toolchain/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu-linux-5.10/bin/aarch64-none-linux-gnu-
make PLAT=fvp SMC_FUZZING=1 SMC_FUZZ_DTS=/data/Project/tf-a-tests/smc_fuzz/dts/top.dts TESTS=smcfuzzing tftf
```

**注意这里的SMC\_FUZZ\_DTS是可以自定义的，这里使用了官方提供的top.dts**

```
/*
 * Copyright (c) 2023, Arm Limited. All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

/*
 * Top level device tree file to bias the SMC calls.  T
 * he biases are arbitrary and can be any value.
 * They are only significant when weighted against the
 * other biases.  30 was chosen arbitrarily.
 */

/dts-v1/;

/ {

    sdei {
        bias = <30>;
        sdei_version {
            bias = <30>;
            functionname = "sdei_version_funcid";
        };
        sdei_pe_unmask {
            bias = <30>;
            functionname = "sdei_pe_unmask_funcid";
        };
        sdei_pe_mask {
            bias = <30>;
            functionname = "sdei_pe_mask_funcid";
        };
        sdei_event_status {
            bias = <30>;
            functionname = "sdei_event_status_funcid";
        };
        sdei_event_signal {
            bias = <30>;
            functionname = "sdei_event_signal_funcid";
        };
        sdei_private_reset {
            bias = <30>;
            functionname = "sdei_private_reset_funcid";
        };
        sdei_shared_reset {
            bias = <30>;
            functionname = "sdei_shared_reset_funcid";
        };
    };
    tsp {
        bias = <30>;
        tsp_add_op {
            bias = <30>;
            functionname = "tsp_add_op_funcid";
        };
        tsp_sub_op {
            bias = <30>;
            functionname = "tsp_sub_op_funcid";
        };
        tsp_mul_op {
            bias = <30>;
            functionname = "tsp_mul_op_funcid";
        };
        tsp_div_op {
            bias = <30>;
            functionname = "tsp_div_op_funcid";
        };
    };
};
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QHRPurKj4tbQy4iaiaJGDwlqHCOKzS335GR1lwQByLp1loicib8gQjhQDQQ/640?wx_fmt=png&from=appmsg)

重编译ATF，并替换tftf.bin。

```
cd /data/Project/arm-trusted-firmware-lts-v2.8.4/
export CROSS_COMPILE=/data/toolchains/SYS_PUBLIC_TOOLS/.toolchain/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu-linux-5.10/bin/aarch64-none-linux-gnu-
make PLAT=fvp BL33=/data/Project/tf-a-tests/build/fvp/release/tftf.bin all fip
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QtavEICEJWVCZ2UZAXdRuET7ZRMLx59icEVK8lKc7oNg6F5zMlvE038g/640?wx_fmt=png&from=appmsg)

再次运行

```
cd /data/Project/arm-trusted-firmware-lts-v2.8.4/build/fvp/release/
/data/Project/Base_RevC_AEMvA_pkg/models/Linux64_GCC-9.3/FVP_Base_RevC-2xAEMvA \
-C pctl.startup=0.0.0.0                                     \
-C bp.secure_memory=1                                       \
-C bp.tzc_400.diagnostics=1                                 \
-C cluster0.NUM_CORES=4                                     \
-C cluster1.NUM_CORES=4                                     \
-C cache_state_modelled=1                                   \
-C bp.secureflashloader.fname="./bl1.bin"      \
-C bp.flashloader0.fname="./fip.bin"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QDZWjeLaicdSb0Vnicy0PlcqoE5kgduh770iaLhz5z8AGicicfYnyTw3UZNQ/640?wx_fmt=png&from=appmsg)

### 扩展SMC fuzz

先来通过目录结构确定需要扩展的文件1.`Dts`2.`fuzz helper。`

![](https://mm...