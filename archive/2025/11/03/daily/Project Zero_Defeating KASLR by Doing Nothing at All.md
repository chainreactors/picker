---
title: Defeating KASLR by Doing Nothing at All
url: https://googleprojectzero.blogspot.com/2025/11/defeating-kaslr-by-doing-nothing-at-all.html
source: Project Zero
date: 2025-11-03
fetch_date: 2025-11-04T03:09:46.389833
---

# Defeating KASLR by Doing Nothing at All

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Monday, November 3, 2025

### Defeating KASLR by Doing Nothing at All

*Posted by Seth Jenkins, Project Zero*

# Introduction

I've recently been researching Pixel kernel exploitation and as part of this research I found myself with an excellent arbitrary write primitive…but without a KASLR leak. As necessity is the mother of all invention, on a hunch, I started researching the Linux kernel linear mapping.

# The Linux Linear Mapping

The linear mapping is a region in the kernel virtual address space that is a direct 1:1 unstructured representation of physical memory. Working with Jann, I learned how the kernel decided where to place this region in the virtual address space. To make it possible to analyze kernel internals on a rooted phone, Jann wrote a tool to call tracing BPF's privileged BPF\_FUNC\_probe\_read\_kernel helper, which by design permits arbitrary kernel reads. The code for this is available [here](https://project-zero.issues.chromium.org/issues/434208461). The linear mapping virtual address for a given physical address is calculated by the following macro:

#define phys\_to\_virt(x)    ((unsigned long)((x) - PHYS\_OFFSET) | PAGE\_OFFSET)

On Arm64 PAGE\_OFFSET is simply:

#define VA\_BITS   (CONFIG\_ARM64\_VA\_BITS)

#define \_PAGE\_OFFSET(va) (-(UL(1) << (va)))

#define PAGE\_OFFSET  (\_PAGE\_OFFSET(VA\_BITS))

As CONFIG\_ARM64\_VA\_BITS is 39 on Android, it’s easy to calculate PAGE\_OFFSET = 0xffffff8000000000.

PHYS\_OFFSET is calculated by:

extern s64   memstart\_addr;

/\* PHYS\_OFFSET - the physical address of the start of memory. \*/

#define PHYS\_OFFSET  ({ VM\_BUG\_ON(memstart\_addr & 1); memstart\_addr; })

memstart\_addr is an exported variable that can be looked up in /proc/kallsyms. Using Jann’s bpf\_arb\_read program, it’s easy to see what this value is:

tokay:/ # grep memstart /proc/kallsyms

ffffffee6d3b2b20 D memstart\_addr

ffffffee6d3f2f80 r \_\_ksymtab\_memstart\_addr

ffffffee6dd86cc8 D memstart\_offset\_seed

tokay:/ # cd /data/local/tmp

tokay:/data/local/tmp # ./bpf\_arb\_read ffffffee6d3b2b20 8                                              <

ffffffee6d3b2b20  00 00 00 80 00 00 00 00                          |........|

tokay:/data/local/tmp #

This value (0x80000000) doesn’t look particularly random. In fact, memstart\_addr was theoretically randomized on every boot, but in practice this hasn’t happened for a while on arm64. In fact as of commit [1db780bafa4c](https://git.kernel.org/pub/scm/linux/kernel/git/arm64/linux.git/commit/?id=1db780bafa4c) it’s no longer even theoretical - virtual address randomization of the linear map is no longer a supported feature in arm64 Linux kernel.

The systemic issue is that memory can (theoretically) be hot plugged in Linux and on Android because of CONFIG\_MEMORY\_HOTPLUG=y. This feature is enabled on Android due to its usage in VM memory sharing. When new memory is plugged into an already running system, it must be possible for the Linux kernel to address this new memory, including adding it onto the linear map. Android on arm64 uses a page size of 4 KiB and 3-level paging, which means virtual addresses in the kernel are limited to 39 bits, unlike typical X86-64 desktops which use 4-level paging and have 48 bits of virtual address space (for kernel and userspace combined); the linear map has to fit within this space further shrinking the area available for it. Given that the maximum amount of theoretical physical memory is far larger than the entire possible linear map region range, the kernel places the linear map at the lowest possible virtual address so it can theoretically be prepared to handle exorbitant (up to 256GB) quantities of hypothetical future hot-plugged physical memory. While it is not technically necessary to choose between memory hot-plugging support and linear map randomization, the Linux kernel developers [decided](https://lore.kernel.org/all/CAMj1kXHXAYt0xLnx4%3D%2BqiCbnuF5U%2B9dzwnds1yd%2BvhTtpP5v3Q%40mail.gmail.com/) not to invest the engineering effort to implement memory hot-plugging in a way that preserves linear map randomization.

So we now know that PHYS\_OFFSET will always be 0x80000000, and thusly, the phys\_to\_virt calculation becomes purely static - given any physical address, you can calculate the corresponding linear map virtual address by the following formula:

#define phys\_to\_virt(x)    ((unsigned long)((x) - 0x80000000) | 0xffffff8000000000)

# Kernel physical address non-randomization

Compounding this issue, it also happens that on Pixel phones, the bootloader decompresses the kernel itself at the same physical address every boot: 0x80010000.

tokay:/ # grep Kernel /proc/iomem

  80010000-81baffff : Kernel code

  81fc0000-8225ffff : Kernel data

[Theoretically, the bootloader can place the kernel at a random physical address every boot,](https://docs.kernel.org/arch/arm64/booting.html) and many (but not all) other phones, such as the Samsung S25, do this. Unfortunately, Pixel phones are an example of a device that simply decompresses the kernel at a static physical address.

# Calculating static kernel virtual addresses

This means that we can statically calculate a kernel virtual address for any kernel .data entry. Here’s an example of me computing that linear map address for the modprobe\_path string in kernel .data on a Pixel 9:

tokay:/ # grep modprobe\_path /proc/kallsyms

ffffffee6ddf2398 D modprobe\_path

tokay:/ # grep stext /proc/kallsyms

ffffffee6be10000 T \_stext

//Offset from kernel base will be 0xffffffee6ddf2398 - 0xffffffee6be10000 = 0x1fe2398

//Physical address will be 0x80010000 + 0x1fe2398 = 0x81ff2398

//phys\_to\_virt(0x81ff2398) = 0xffffff8001ff2398

tokay:/ # /data/local/tmp/bpf\_arb\_read ffffff8001ff2398 64

ffffff8001ff2398  00 73 79 73 74 65 6d 2f 62 69 6e 2f 6d 6f 64 70  |.system/bin/modp|

ffffff8001ff23a8  72 6f 62 65 00 00 00 00 00 00 00 00 00 00 00 00  |robe............|

[ zeroes ]

tokay:/ # reboot                                                                                                         sethjenkins@sethjenkins91:~$ adb shell

tokay:/ $ su

tokay:/ # /data/local/tmp/bpf\_arb\_read ffffff8001ff2398 64

ffffff8001ff2398  00 73 79 73 74 65 6d 2f 62 69 6e 2f 6d 6f 64 70  |.system/bin/modp|

ffffff8001ff23a8  72 6f 62 65 00 00 00 00 00 00 00 00 00 00 00 00  |robe............|

[ zeroes ]

tokay:/ #

So modprobe\_path will always be accessible at the kernel virtual address 0xffffff8001ff2398, in addition to its normal mapping, even with KASLR enabled. In practice, on Pixel devices you can derive a valid virtual address for a kernel symbol by calculating its offset and simply adding a hardcoded static kernel base address of 0xffffff8000010000. In short, instead of breaking the KASLR slide, it is possible to just use 0xffffff8000010000 as a kernel base instead.

The linear mapping memory is even mapped rw for any kernel .data regions. The only consolation that makes using this address slightly less effective than the traditional method of leaking the KASLR slide is that .text regions are not mapped executable - so an attacker cannot use this base for e.g. ROP gadgets or more generally PC control. But oftentimes, a Linux kernel attacker’s goal isn’t arbitrary code execution in kernel context anyway - arbitrary read-write is the more frequently desired primitive.

# Impact on devices with kernel physical address randomization

Even on devices where the kernel location is randomized in the physical address space, linear mapping non-randomization still softens the kernel considerably to attempts at exploitation. This is particularly because techniques that involve spraying memory (either kernel structures or even userland mmap’s!) can land at predictable physical addresses - and those physical addresses are easily referenceable in kernel virtual address space through the l...