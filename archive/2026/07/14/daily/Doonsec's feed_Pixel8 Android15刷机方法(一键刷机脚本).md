---
title: Pixel8 Android15刷机方法(一键刷机脚本)
url: https://mp.weixin.qq.com/s/x84GlP1LCOWrWXxSQ4TQPg
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:46:54.621946
---

# Pixel8 Android15刷机方法(一键刷机脚本)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Wxusn17ibicDY4asIaJQH4UEcl97uBBR5m3O0aCmU9CmWQH2YL1FGdqjNnxsgCIiboGN5KA7ia5wZABdmIRtyjo0HalLtcVkvRT26oJEcic73GP8/0?wx_fmt=jpeg)

# Pixel8 Android15刷机方法(一键刷机脚本)

原创

云天实验室
云天实验室

哆啦安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 1. 编译生成的镜像分析

![](https://mmbiz.qpic.cn/mmbiz_png/Wxusn17ibicDbqsDDdrqp8nibY1vSibcICIuiaunxQ5Mw099kAmwlfyt07lCFPXHkJJKH280VVrjAYI4Xpx5fBYEpqU31myETwbNPuhdIFiaTdhcY/640?wx_fmt=png&from=appmsg)

[Google Pixel8 Android15](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500846&idx=1&sn=e36fe912d632b8ecc52bc7490a924de0&scene=21#wechat_redirect)

[Android系统镜像刷机方法(一)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247488387&idx=1&sn=81b2b25e651f0b90fd91aa793445364d&scene=21#wechat_redirect)

[Android系统镜像刷机方法(二)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247488387&idx=2&sn=ba78a14a9414cc091fae1ca0712e1f7a&scene=21#wechat_redirect)

[Android系统镜像刷机方法(三)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247488417&idx=1&sn=8029e7e1334905598047afc99bd12ac4&scene=21#wechat_redirect)

[Pixel8 Android15安全手机定制(编译源码)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247501022&idx=1&sn=654651c6db5ec23f216d8012a7db4981&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/Wxusn17ibicDamXCuIIvDPyiaRcYOZKyEibxgZves3Jibanr526H5R9NuAuiaNY0HvfwXuqgkASia49pMrxTuZe1FHYgokKxNBXguZibt5W80AtrvdY/640?wx_fmt=png&from=appmsg)

##

## ![图片](https://mmbiz.qpic.cn/mmbiz_png/Wxusn17ibicDYBMXVAO30H1ia86f2uPP9T1vtnugibjibiaIOqMTK900j0asM9O20j5xkeXonictFeLaHLFXEXwtpc0CmibLKZbCHmhO2rYafqJopg8/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

##

## [Android10至16系统ROM定制(绕过检测方法)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500957&idx=1&sn=3a64aba80472e5095ed15c34da581830&scene=21#wechat_redirect)

##

## 2. 刷机环境准备（前置条件）

* **解锁 Bootloader**：在手机“开发者选项”中开启“OEM 解锁”，并通过 `fastboot flashing unlock` 解锁。
* **安装 fastboot 与 adb**：

```
sudo apt install android-tools-adb android-tools-fastboot   # Debian/Ubuntu# 或从 Android SDK Platform-Tools 下载
```

* **USB 驱动**：确保 Linux 下识别手机（`lsusb` 可见 Google 设备），并配置 udev 规则（如 `/etc/udev/rules.d/51-android.rules`）。
* **数据备份**：刷机过程会清空用户数据（除非指定保留）。

## 3. 一键刷机脚本及文档

在仓库的 `script/` 目录下创建以下两个文件：

* `flash_all.sh` —— 一键刷机脚本
* `刷机指南.md` —— 详细操作说明

### 3.1 刷机脚本 `script/flash_all.sh`

```
#!/bin/bash################################################################################ AOSP 一键刷机脚本 (Pixel 8 / Android 15)# 用法：#   ./flash_all.sh              # 完整刷写并清除用户数据#   ./flash_all.sh --keep-data  # 保留用户数据刷写（仅更新系统）###############################################################################
set -e
# --------------- 配置变量 ---------------# 可通过环境变量 AOSP_OUT 指定产品镜像目录，否则使用默认路径DEFAULT_OUT="/home/gyp/gyp/GMSecPlatform/MTAppSecRSROM/aosp-pixel8-android15/out/target/product/shiba"AOSP_OUT="${AOSP_OUT:-${DEFAULT_OUT}}"
FASTBOOT_CMD="fastboot"KEEP_DATA=false
# 解析参数for arg in "$@"; do    case "$arg" in        --keep-data)            KEEP_DATA=true            ;;        *)            echo "未知参数: $arg"            echo "用法: $0 [--keep-data]"            exit 1            ;;    esacdone
# --------------- 前置检查 ---------------echo "========================================"echo " AOSP 一键刷机脚本"echo " 镜像路径: ${AOSP_OUT}"echo "========================================"
if ! command -v $FASTBOOT_CMD &> /dev/null; then    echo "错误：未找到 fastboot 命令，请安装 Android SDK Platform-Tools。"    exit 1fi
if [ ! -d "$AOSP_OUT" ]; then    echo "错误：产品镜像目录不存在: ${AOSP_OUT}"    echo "请通过环境变量 AOSP_OUT 指定正确的路径，例如："    echo "  export AOSP_OUT=/path/to/out/target/product/shiba"    exit 1fi
# 检查必要镜像是否存在REQUIRED_IMGS=("boot.img" "dtbo.img" "vendor_boot.img" "vbmeta.img" "super.img")for img in "${REQUIRED_IMGS[@]}"; do    if [ ! -f "${AOSP_OUT}/${img}" ]; then        echo "错误：缺少镜像文件 ${AOSP_OUT}/${img}"        exit 1    fidone
# --------------- 连接设备 ---------------echo "等待设备进入 fastboot 模式..."$FASTBOOT_CMD devices | grep -q "fastboot" || {    echo "未检测到 fastboot 设备。请手动将手机进入 bootloader（关机后按住 音量- + 电源），然后重试。"    exit 1}
DEVICE_FASTBOOT=$($FASTBOOT_CMD devices | awk '{print $1}')echo "已连接设备: ${DEVICE_FASTBOOT}"
# --------------- 开始刷写 ---------------echo ">>> 刷写 bootloader 分区 ..."# bootloader 和 radio 需要从官方镜像获取，这里仅提示跳过echo "    [跳过] 未提供 bootloader/radio 镜像，请确保当前固件与系统兼容。"
echo ">>> 刷写 dtbo, vendor_boot, boot ..."$FASTBOOT_CMD flash dtbo "${AOSP_OUT}/dtbo.img"$FASTBOOT_CMD flash vendor_boot "${AOSP_OUT}/vendor_boot.img"$FASTBOOT_CMD flash boot "${AOSP_OUT}/boot.img"
echo ">>> 处理 vbmeta (禁用 AVB 验证)..."if [ -f "${AOSP_OUT}/vbmeta.img" ]; then    $FASTBOOT_CMD flash vbmeta --disable-verity --disable-verification "${AOSP_OUT}/vbmeta.img"else    echo "    警告：vbmeta.img 不存在，跳过。"fiif [ -f "${AOSP_OUT}/vbmeta_system.img" ]; then    $FASTBOOT_CMD flash vbmeta_system --disable-verity --disable-verification "${AOSP_OUT}/vbmeta_system.img"fiif [ -f "${AOSP_OUT}/vbmeta_vendor.img" ]; then    $FASTBOOT_CMD flash vbmeta_vendor --disable-verity --disable-verification "${AOSP_OUT}/vbmeta_vendor.img"fi
echo ">>> 刷写动态分区（super 镜像）..."if [ -f "${AOSP_OUT}/super.img" ]; then    $FASTBOOT_CMD flash super "${AOSP_OUT}/super.img"else    echo "    未找到 super.img，尝试逐个刷写逻辑分区..."    # 进入 fastbootd 模式    $FASTBOOT_CMD reboot fastboot    sleep 5    echo "    等待设备重新连接 fastbootd ..."    $FASTBOOT_CMD devices    # 刷写逻辑分区（根据实际产物调整）    for part in system product system_ext vendor; do        if [ -f "${AOSP_OUT}/${part}.img" ]; then            $FASTBOOT_CMD flash ${part} "${AOSP_OUT}/${part}.img"        fi    donefi
# --------------- 清除 / 保留数据 ---------------if [ "$KEEP_DATA" = false ]; then    echo ">>> 清除用户数据（首次刷机推荐）..."    $FASTBOOT_CMD erase userdata    # 也可以格式化 metadata    $FASTBOOT_CMD erase metadataelse    echo ">>> 保留用户数据，跳过清除步骤。"fi
# --------------- 完成 ---------------echo ">>> 重启设备..."$FASTBOOT_CMD reboot
echo ""echo "========================================"echo " 刷机完成！手机正在重启。"echo "========================================"
```

#### 使用方式

```
cd scriptchmod +x flash_all.sh
# 完整刷写并擦除数据./flash_all.sh
# 保留用户数据（升级系统）./flash_all.sh --keep-data
```

### 3.2 刷机指南

```
# Pixel 8 Android 15 AOSP 刷机指南
#aosp-pixel8-android15源码编译产物，提供完整的一键刷机方法。
## 1. 准备工作
### 1.1 解锁 Bootloader1. 开启手机【开发者选项】→【OEM 解锁】。2. 在电脑执行：     adb reboot bootloader   fastboot flashing unlock（按手机提示确认，此操作会清除所有数据）。
### 1.2 安装工具- Linux: sudo apt install android-tools-adb android-tools-fastboot- Windows / macOS: 下载 [Platform-Tools](https://developer.android.com/tools/releases/platform-tools)，将目录加入 PATH。
### 1.3 准备镜像编译成功后，所有刷机镜像位于源码根目录下的out/target/product/shiba/（产品名可能为shiba或husky）。  脚本默认使用该路径，你也可通过环境变量AOSP_OUT自定义：export AOSP_OUT="/your/path/to/out/target/product/shiba"
```

**注意**：本脚本不会刷写 bootloader 和 radio，建议当前手机已运行与 AOSP 版本兼容的官方底层固件。若有需要，可自行从Google 出厂镜像中提取并手动刷入。

## 2. 一键刷机

```
# 添加执行权限chmod +x flash_all.sh
# 刷机（会清空用户数据，首次编译后推荐）./flash_all.sh
# 刷机（保留用户数据，适合后续迭代升级）./flash_all.sh --keep-data
```

脚本会自动完成以下操作：

1. 检查 fastboot 连接。
2. 刷入 `dtbo`、`vendor_boot`、`boot`。
3. 禁用 `vbmeta` 验证，确保自定义系统可启动。
4. 刷入动态分区 `super` 镜像（或逐个逻辑分区刷写）。
5. 根据参数决定是否清除 `userdata` 和 `metadata`。
6. 重启手机。

## 3. 常见问题

### 3.1 设备未识别

* 确认手机已进入 Bootloader（关机后按住 **音量- + 电源**）。
* 执行 `fastboot devices` 应显示设备序列号。
* Linux 用户请配置 udev 规则：

```
echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="18d1", MODE="0666", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/51-android.rulessudo udevadm control --reload-rules
```

### 3.2 卡在 Google 启动界面

* 第一次开机因生成 ART 缓存可能需 5–10 分钟，请耐心等待。
* 若超过 15 分钟仍未完成，尝试擦除用户数据重刷：

```
fastboot -wfastboot reboot
```

### 3.3 "super partition not found" 错误

* 确保设备支持动态分区（Pixel 8 支持），且当前 Bootloader 版本与系统兼容。
* 检查是否成功刷写了 `super.img`，或尝试手动进入 `fastbootd` 后刷写逻辑分区。

[Google Pixel8 Android15](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500846&idx=1&sn=e36fe912d632b8ecc52bc7490a924de0&scene=21#wechat_redirect)

[Redroid Android13云手机定制(一键优化清理磁盘)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247500815&idx=1&sn=e2473e146e4c5d1f28d31dd13247ec08&scene=21#wechat_redirect)
...