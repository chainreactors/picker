---
title: Debugging a boot loop on Acer Veriton GN100 (NVIDIA DGX OS)
url: https://hshrzd.wordpress.com/2026/11/09/debugging-a-boot-loop-on-nvidia-dgx-os/
source: hasherezade's 1001 nights
date: 2026-11-09
fetch_date: 2026-11-10T09:02:05.164541
---

# Debugging a boot loop on Acer Veriton GN100 (NVIDIA DGX OS)

[hasherezade's 1001 nights](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

projects and tasks that I do in my free time

[![Split illustration comparing tangled legacy technology with organized modern digital systems](https://hshrzd.wordpress.com/wp-content/uploads/2026/11/split-scene-laptop-boot-repair-transition-6af15d2f60f38.png?w=940&h=198&crop=1)](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

[Skip to content](#content "Skip to content")

* [Home](https://hshrzd.wordpress.com)
* [Projects](https://hshrzd.wordpress.com/mycode/)
  + [PE-sieve](https://hshrzd.wordpress.com/pe-sieve/)
  + [PE\_unmapper](https://hshrzd.wordpress.com/pe_unmapper/)
  + [IAT Patcher](https://hshrzd.wordpress.com/iat-patcher/)
  + [PE-bear](https://hshrzd.wordpress.com/pe-bear/)
  + [ViDi](https://hshrzd.wordpress.com/vidi-visual-disassembler/)
  + [DMA Unlocker](https://hshrzd.wordpress.com/mycode/dma-unlocker/)
* [How to start RE/malware analysis?](https://hshrzd.wordpress.com/how-to-start/)

[← Flare-On 12 – Task 8](https://hshrzd.wordpress.com/2025/11/25/flare-on-12-task-8/)

## [Debugging a boot loop on Acer Veriton GN100 (NVIDIA DGX OS)](https://hshrzd.wordpress.com/2026/11/09/debugging-a-boot-loop-on-nvidia-dgx-os/)

Posted on [November 9, 2026](https://hshrzd.wordpress.com/2026/11/09/debugging-a-boot-loop-on-nvidia-dgx-os/ "5:27 am") by [hasherezade](https://hshrzd.wordpress.com/author/hshrzd/ "View all posts by hasherezade")

***TL;DR:** After a routine system upgrade, my Acer Veriton GN100 (an NVIDIA GB10-based machine) got stuck in a reboot loop caused by kernel `7.0.0-1024-nvidia`. I recovered it without reinstalling the OS, using an Ubuntu ARM64 USB stick’s GRUB console to manually boot the installed kernel with the `initcall_blacklist=power_wrap_init` workaround added. I then installed NVIDIA’s official fix, `nvidia-spark-initcall-bl` 1.0-2 (via `sudo apt dist-upgrade`), to make it permanent, and made the GRUB menu visible so I won’t need a rescue stick next time.*

---

Recently I bought a Spark-class machine to start experimenting with local models. But my first adventure with it turned out to be quite different.

It took me back to my early experiences with Linux in 2002, when, as a teenager, I was trying to compile a custom kernel to get NVIDIA drivers working on a Linux installation my father had allowed me to set up on his computer. The new kernel ended up panicking, and when I tried to configure LILO to let me choose between the old and the new kernel, I somehow messed up the bootloader too. As a result, neither my Linux nor my father’s Windows would boot anymore. I don’t remember exactly what went wrong, just that after all I managed to fix it and it ended well. But I still remember the horror of realizing that I had just made my father’s computer unbootable… As Linux matured over the years, and I continued using it daily, I almost forgot such problems exist.

This time, I wasn’t recompiling a kernel or doing anything fancy. But as we will see, even standard updates on this relatively new stack can sometimes cause unexpected problems, so it’s better to be prepared.

My Acer is doing fine now, and in this blog post I just wanted to share the steps I took to fix it and the lessons I learned. And unlike in my teenage years, this time I had a helper along the way: a GPT-6 bot.

# How it started

I was happy to finally have this machine, and I couldn’t wait to start setting things up. So as soon as I booted it for the first time, I decided to run a standard system update. This Acer model comes with NVIDIA DGX OS preinstalled, which is Ubuntu-based.

```
sudo apt update

sudo apt full-upgrade
```

During the update, the kernel got updated from `6.11.0-1016-nvidia` to the latest at the time: `7.0.0-1024-nvidia`. But everything looked fine, so I thought it was time to reboot.

And this is where my rude awakening happened. Instead of my system booting cleanly, I saw the Acer logo, then something resembling a memory check, with rows of zeros. But it went nowhere. After a moment, the system rebooted and repeated the same loop over and over.

![](https://hshrzd.wordpress.com/wp-content/uploads/2026/11/boot_fail.png?w=1024)

# Let’s boot anything

What was going on? I didn’t know much at this point, but I suspected that the update was responsible, probably the kernel update. So, as usual in such cases, my first thought was to try booting the last kernel that worked. We just needed to reach it…

The GRUB menu was hidden and set to automatically boot the default entry. I tried to trigger it using a variety of recommended key combinations after the Acer logo (such as Left Shift + Insert), but I couldn’t get it to appear.

Finally, I gave up trying to trigger GRUB and decided to enter UEFI setup to see what options I had. The reboot loop was so quick that it took me several attempts at pressing Esc to finally reach the UEFI menu.

Looking at the “Boot” tab, I understood why it had been so difficult to enter UEFI. “Setup Prompt Timeout” was set to just 1 second.

![](https://hshrzd.wordpress.com/wp-content/uploads/2026/11/aptio_setup.png?w=640)

So I changed it first, setting the timeout to 5 seconds.

If we can’t choose what kernel to boot from the disk, we may try a different way, and boot the system from a different medium. It is an ARM64 machine, so I downloaded an Ubuntu ARM64 image (precisely: Ubuntu 24.04.5 LTS arm64) and flashed a pendrive with the ISO. The Boot Override accessible from UEFI allowed me to select the exact medium I wanted to be used.

And it booted – well, sort of.

The live desktop didn’t start: all I got was a black screen with an X-shaped cursor, which looked familiar from my earlier Linux adventures when the X Window System failed to initialize properly. Trying to switch to a text console using Ctrl+Alt+F2/F3/F4 didn’t really do a thing. So it looks like this way is blocked too…

But there was one more thing worth trying. The Ubuntu pendrive had its own GRUB menu, which appeared before the live system started. Maybe we could use it to access the internal disk?

# Booting the kernel via the GRUB command line

I rebooted the machine from the Ubuntu pendrive again, but this time, instead of starting Ubuntu, I pressed `C` in the GRUB menu to enter its command line.

At the GRUB prompt, I used the `ls` command to list the available disks and partitions. My internal SSD was among them, so I started exploring its contents.

* `(hd0,gpt1)` contained the EFI files.
* `(hd0,gpt2)` contained the Linux root filesystem, including `/boot`.

![](https://hshrzd.wordpress.com/wp-content/uploads/2026/11/grub_ls.png?w=1024)
> Note that GRUB device identifiers may differ between machines. Make sure to identify your Linux root partition before using the commands below.

Both kernels – the old one and the newly installed one – should be in `/boot`, so let’s check:

```
ls (hd0,gpt2)/boot/
```

![](https://hshrzd.wordpress.com/wp-content/uploads/2026/11/ls_boot.png?w=1024)

And here they are.

## Trying to boot the old kernel

The files with `6.11.0` belong to the previously working kernel:

```
vmlinuz-6.11.0-1016-nvidia # Linux kernel

initrd.img-6.11.0-1016-nvidia # Initial RAM filesystem
```

Now we will try to manually issue the commands to boot the old kernel.

It also needs the root filesystem UUID, which is pretty long. Since we cannot use copy-paste here, and retyping is error-prone, we can store it in the environment variable first:

```
set root=(hd0,gpt2)

probe --fs-uuid --set=rootuuid (hd0,gpt2)

echo $rootuuid
```

On my first attempt I tried the following minimal configuration. The `boot` command will initiate the booting process.

```
linux /boot/vmlinuz-6.11.0-1016-nvidia root=UUID=$rootuuid ro

initrd /boot/initrd.img-6.11.0-1016-nvidia

boot
```

The boot started, but then appeared to freeze after displaying:

```
EFI stub: Booting Linux Kernel...

EFI stub: Loaded initrd from LINUX_EFI_INITRD_MEDIA_GUID device pa...