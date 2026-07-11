---
title: 【万字总结】近八年的，Kali Linux系统相关排雷实录
url: https://mp.weixin.qq.com/s/Xa8KSReBJEkJWRo8OegCIQ
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:55.665184
---

# 【万字总结】近八年的，Kali Linux系统相关排雷实录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MIGLFDXRTiaQwy8w2nGk4dRhVus0u7xBNMbUM5a0QoMbeoNPnT02hicvRgRl6ZvMuyqDV8gfDynMiboLyibrsCMiaUI1jS9NLYn6ADvAfs7OEYUY/0?wx_fmt=jpeg)

# 【万字总结】近八年的，Kali Linux系统相关排雷实录

原创

赛赛
赛赛

W啥都学

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> # 简历
>
> Kali Linux 作为物理主力机 近八年，从 Ubuntu 到 Arch 再回到 Kali，踩过的坑连起来能绕电脑三圈
>
> 这篇是 2024 年那两篇文章的全面升级版——新增了大量硬件级修复方案，包括触控板 HID 协议修复、蓝牙底层排查、指纹驱动编译等。依然是老规矩：不讲玄学，从原理出发，每一步都讲清楚「为什么」
>
> 全文按问题分类，可直接当手册查阅。建议收藏，总用得上

文档目录：

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaTwwHtEMvI0mibC6rticHYN0ticBOU9VclcA9vIXibqBfiaXQ2K3NxL9opZXPro3Wjk44jLrB1J7lRoOmq3srsbtUz3OmPFjN59974c/640?wx_fmt=png&from=appmsg)

# 关于小米Book Pro 14专项问题

这个真的我要吐槽一下，怎么装上linux就等于完全不能用，就相当于你只能使用小米指定的他自己的系统…

这个问题我真是解决了好久，要是之前没有ai的时代真的不知道要弄到什么时候

## 1. 键盘不可用

**问题**: 安装 Kali Linux 后内置键盘完全无反应

**原因**: 小米 EC 固件不响应标准 i8042 命令字的 KBDDIS 控制，需要显式发送 0xAE 命令

**解决**: 在 `/etc/default/grub` 中添加内核参数：

```
GRUB_CMDLINE_LINUX="i8042.nopnp i8042.dumbkbd=1"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaQibs0DT7qziajtSJprlhz4USiavk7GNRxpyQzibvU03LdwsBlibUZgzWPYNu8dIibPgGL37KUsDodlfmkpWqgsSd3afNv4lhHv9uz90/640?wx_fmt=png&from=appmsg)

修改后执行 `update-grub` 并重启

## 2. 多系统引导（ESP 默认引导路径）

**问题**: 硬盘上有多个系统（Kali + Windows），但小米只识别到 Windows Boot Manager。

**原因**: 小米 UEFI 固件默认只启动 `/EFI/BOOT/BOOTX64.EFI`，该文件原为 Windows Boot Manager。

**解决**:

```
# 备份原 Windows Boot Manager
cp /boot/efi/EFI/BOOT/BOOTX64.EFI /boot/efi/EFI/BOOT/BOOTX64.EFI.windows.bak

# 用 GRUB 替换
cp /boot/efi/EFI/KALI/grubx64.efi /boot/efi/EFI/BOOT/BOOTX64.EFI
```

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaTtBy2Dl5bYicQ0eoFA8ibxsKiaX0eG8dBJgRrrBgxX6uRlD4AgVVSEn1HyNRRb57VlqqoLmOIoR9RV8Gc3MjPq19o4DXvE4MBH0s/640?wx_fmt=png&from=appmsg)

确保 `/boot/efi/EFI/BOOT/grub.cfg` 和 `/boot/efi/EFI/KALI/grub.cfg` 内容正确指向根分区：

```
search.fs_uuid <ROOT_PARTITION_UUID> root hd0,gptX
set prefix=($root)"/boot/grub"
configfile $prefix/grub.cfg
```

![image-20260706135409406](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaSDntVjIEfv7DNRfgHFYYE7eFJ21IYYQHgq4gY7tNLXY25OnC4ic6Q8gMZMicSOxKpDYn3cQhzec3b8HDtac6r8wmrkrp3AbkCpQ/640?wx_fmt=png&from=appmsg)

image-20260706135409406

## 3. 屏幕花屏/闪烁

**问题**: 屏幕间歇性花屏、闪烁。

**原因**: Intel Panther Lake GPU 的 Xe 驱动中 PSR（Panel Self Refresh）导致。需要强制使用 Xe 驱动而非 i915，并关闭 PSR。

**解决**: 在 `/etc/default/grub` 的 `GRUB_CMDLINE_LINUX` 中添加：

```
xe.force_probe=b080 i915.force_probe=!b080 xe.enable_psr=0
```

完整参数示例：

```
GRUB_CMDLINE_LINUX="i8042.nopnp i8042.dumbkbd=1 xe.force_probe=b080 i915.force_probe=!b080 xe.enable_psr=0"
```

修改后执行 `update-grub` 并重启

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaSoAvIfyicgLmq2nKyzBsdLAY4ib3Tj8qjzOicQDC3SdXRJnNgB2pZ3icFJjejTS0iciajM6O8JoSBJfUzgP0Uv1AW9aYLPDjWYtxtibM/640?wx_fmt=png&from=appmsg)

## 4. WiFi 不可用

**问题**: WiFi 无法使用，缺少固件。

**原因**: 默认固件包 `firmware-iwlwifi` 版本过旧（20251111-1），不包含 `iwlwifi-sc-a0-gf-a0-100.ucode`。

**解决**: 升级固件到 20260519-1 版本：

```
apt update
apt install firmware-iwlwifi
```

然后重新加载驱动或重启：

```
modprobe -r iwlwifi && modprobe iwlwifi
```

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaSQhmAiaARbWddibwdh3FRYMDwnFibA8YbqksX6zK1FLPA9uWG2SzGT7QrQTaIJ2XicakQSTibHkSiaJXGBzNwNTC23WTAd7l0eOJib7g/640?wx_fmt=png&from=appmsg)

## 5. 触控板不可用（关键问题，已解决）

**问题**: 触控板无反应，指针不移动。

**原因**: 这是一个多层级问题，需要从 HID 模式、电源管理、libinput 三个层面修复：

1. 1. **HID 模式**: BLTP7853 (347D:7853) 触控板默认处于 Mouse 模式（Input Mode=0），需要通过 HID Feature Report 切换到 Multitouch 模式（Input Mode=3），Report ID=3, Usage=0x52
2. 2. **电源管理**: 触控板会在空闲时自动挂起（power/control=auto），唤醒后可能状态异常
3. 3. **libinput 跳跃检测误判**: libinput 会误判触控板正常移动为 “Touch jump” 并丢弃所有触摸事件。Xorg 日志出现 `(EE) event5 - BLTP7853:00 347D:7853 Touchpad: kernel bug: Touch jump detected and discarded.`

内核 6.6.3+ 已包含 `MT_CLS_VTL` quirk（commit `9ffccb691adb`），但仅靠内核补丁不够，还需要以上用户态修复

### 5.1 修复程序

**`/usr/local/bin/fix-touchpad-mode.c`** — C 程序，发送 HID Feature Report 切换模式：

```
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
#include<sys/ioctl.h>
#include<linux/hidraw.h>
#include<errno.h>

intmain(int argc, char *argv[]) {
char *devpath = "/dev/hidraw1";
if (argc > 1)
        devpath = argv[1];

int fd = open(devpath, O_RDWR);
if (fd < 0) { perror("open"); return1; }

unsignedchar buf[2] = {0x03, 0x03};
int ret = ioctl(fd, HIDIOCSFEATURE(2), buf);
if (ret < 0) {
        perror("HIDIOCSFEATURE");
        close(fd);
return1;
    }
printf("Touchpad mode set to multitouch (%d) on %s\n", buf[1], devpath);
    close(fd);
return0;
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaRcxmhJmEvRQv2Zv4sRnpjvhEupd0ajKFdTacxCibmlpCFnfD8OMcxtDnZBGzQDyPGBoriaAmiaZj9WZ2o96sJNMQOFlIf8La2hn0/640?wx_fmt=png&from=appmsg)

编译：

```
gcc -o /usr/local/bin/fix-touchpad-mode /usr/local/bin/fix-touchpad-mode.c
```

或者使用 `hid-tools` 中的 `hid-feature` 工具替代（效果相同）：

```
sudo apt install hid-tools
sudo hid-feature set -f 30000 3 $(sudo hid-feature list-devices | grep BLTP7853 | awk -F: '{print $1}')
```

### 5.2 自动化脚本

**`/usr/local/bin/fix-touchpad.sh`** — 整合了电源管理禁用、驱动重新绑定、模式切换：

```
#!/bin/bash

# 禁用触控板电源管理，防止空闲挂起后失灵
for dev in /sys/bus/hid/devices/*:347D:7853.*; do
if [ -d "$dev" ]; then
echo"on" > "$dev/power/control" 2>/dev/null
fi
done
for dev in /sys/bus/i2c/devices/i2c-BLTP7853:*/power/control; do
if [ -f "$dev" ]; then
echo"on" > "$dev" 2>/dev/null
fi
done

# 重新绑定 hid-multitouch 驱动，触发重新初始化
for dev in /sys/bus/hid/devices/*:347D:7853.*; do
if [ -d "$dev" ]; then
        name=$(basename"$dev")
echo"$name" > /sys/bus/hid/drivers/hid-multitouch/unbind 2>/dev/null
sleep 0.5
echo"$name" > /sys/bus/hid/drivers/hid-multitouch/bind 2>/dev/null
fi
done

sleep 0.3

# 切换到多点触控模式
for h in /dev/hidraw*; do
if [ -e "$h" ]; then
ifcat /sys/class/hidraw/$(basename$h)/device/uevent 2>/dev/null | grep -q "BLTP7853"; then
            /usr/local/bin/fix-touchpad-mode "$h"
fi
fi
done
```

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaTw2a7rmOegmklhzVJBoZXpNicmj13hGPJ0Om0S3KBIk4YZZ72juU9x3sudllpZ8yzOhQlBIyPoZxHkeicpMlZov63v3OicypXUcs/640?wx_fmt=png&from=appmsg)

设置权限：

```
chmod +x /usr/local/bin/fix-touchpad.sh
```

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaTSwYHtsNozABHKrjtCmqYsxyVDN6mX0qNNAZp1GCdc07RickLEdmM2I80A94wT1B3FBgSJCI5k1tCgEZDM7OvxRicr71RTzFYP4/640?wx_fmt=png&from=appmsg)

### 5.3 Systemd 开机自启动

**`/etc/systemd/system/fix-touchpad.service`**：

```
[Unit]
Description=Fix Xiaomi Book Pro 14 touchpad initialization
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/fix-touchpad.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaTF1BmtONsGSicmTatbzZW630vc7hDRUNDvnl6sqoPCC5BN7FVbOicBdbGeDc6j0dl76hGaKtwfjA6icIQ623jZ6UjZVZP5jeuTJg/640?wx_fmt=png&from=appmsg)

启用：

```
systemctl daemon-reload
systemctl enable --now fix-touchpad.service
```

### 5.4 睡眠唤醒后自动修复

**`/lib/systemd/system-sleep/fix-touchpad.sh`**：

```
#!/bin/bash
case$1in
    post)
        /usr/local/bin/fix-touchpad.sh
        ;;
esac
```

```
chmod +x /lib/systemd/system-sleep/fix-touchpad.sh
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaTG1JGc6dkDtf1DxVbNQKmzOdldMic6OXuoP0ORUcJjFUV3l8RA6EpJjpes0UZGD7ZJ8w7ibpbwUeN54JibCR3IYQHicu3BdPmH4n4/640?wx_fmt=png&from=appmsg)

### 5.5 udev 规则 — 禁止触控板电源管理

**`/etc/udev/rules.d/99-xiaomi-touchpad-pm.rules`** — 防止触控板被系统自动挂起：

```
# 禁止 BLTP7853 触控板电源管理挂起
ACTION=="add", SUBSYSTEM=="hid", ATTRS{idVendor}=="347d", ATTRS{idProduct}=="7853", ATTR{power/control}="on"
# 同时禁止 I2C 父设备挂起
ACTION=="add", SUBSYSTEM=="i2c", KERNEL=="i2c-BLTP7853:*", ATTR{power/control}="on"
```

重载 udev：

```
udevadm control --reload-rules
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaTddUiatefsHTolsOq0evWk3497mC7ZXXZicTRnK3VRfiaknLFoBvG9CHPqKeZjiaI8icwDBFqNwbgicK4WRn40XEXYU1LicjDTuPhqus/640?wx_fmt=png&from=appmsg)

### 5.6 libinput quirk — 修复跳跃检测误判

**`/etc/libinput/local-overrides.quirks`** — 防止 libinput 将正常触摸误判为光标跳跃并丢弃：

```
# 小米 Book Pro 14 2026 - BLTP7853 触控板
# 禁用误触发的触摸跳跃检测
[Xiaomi Book Pro 14 Touchpad]
MatchUdevType=touchpad
MatchName=*BLTP7853*
AttrPalmPressur...