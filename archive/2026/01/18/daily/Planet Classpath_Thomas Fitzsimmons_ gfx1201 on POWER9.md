---
title: Thomas Fitzsimmons: gfx1201 on POWER9
url: https://www.fitzsim.org/blog/?p=797
source: Planet Classpath
date: 2026-01-18
fetch_date: 2026-01-19T03:44:20.262246
---

# Thomas Fitzsimmons: gfx1201 on POWER9

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# gfx1201 on POWER9

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [January 18, 2026January 18, 2026](https://www.fitzsim.org/blog/?p=797)
[Leave a comment on gfx1201 on POWER9](https://www.fitzsim.org/blog/?p=797#respond)

*AI GoF disclaimer: I don’t expect this blog post to contribute to frontier AI gain-of-function research or I would refrain from publishing it. Please consider supporting [Doom Debates](https://doomdebates.com/) to improve the quality of discourse around the risks of frontier AI research, and [MIRI](https://intelligence.org/) to try to [mitigate the risks](https://ifanyonebuildsit.com/treaty).*

I have been wanting to experiment with open weights language models on the [*Talos II*](https://www.fitzsim.org/blog/?p=350).

I have a `gfx803` card that I always wanted to use for compute, but it is now out-of-support for *ROCm*. I have made progress getting a `gfx1201` card working on this machine and I wanted to write up all the interesting error messages for reference.

I took a risk and bought a new GPU, the *AMD Radeon AI Pro R9700* ([ASRock Creator 32GB](https://oc.asrock.com/Graphics-Card/AMD/Radeon%20AI%20PRO%20R9700%20Creator%2032GB/index.us.asp)), without knowing if I could get it working with the *Talos II* mainboard, which is now seven years old.

First I realized my existing power supply did not have enough free connectors; I needed a new “modular” power supply for the GPU’s new-style `12v-2x6` power connector (which is actually a 16 pin connector, with an array of 2 x 6 main big pins and 4 little pins at the top). That prerequisite project was nerve-racking but successful. Physically, the card fit fine in the mainboard and *EATX* chassis.

With the latest *Debian Trixie* kernel driver, the card showed up as a *PCIe* device in `lspci` (validating the physical installation) but without displaying the card’s name. I figured the driver was not new enough to recognize the card’s product identifier. I read online that a *Debian*-derivative’s `6.17` kernel recognized the card on a different CPU architecture, so I temporarily enabled the *Debian* `testing` repository, installed `linux-image`, and rebooted. Now `lspci` displayed the card’s name, so that was progress. But as a side effect of the kernel upgrade, my virtual machines failed to start up. The `libvirtd` message was:

```
qemu-system-ppc64: Can't support 64 kiB guest pages with 4 kiB host pages with this KVM implementation
```

It turned out *Debian* `ppc64le` had changed the default page size from `64KiB` to `4KiB`. *Debian* though, with its characteristic flexibility, still provided a `64KiB` page-size `linux-image` variant. With that the virtual machines worked again and the GPU continued to be recognized.

Next I shifted to userspace; the *Debian*-packaged `rocminfo` segfaulted early during its initialization, so I looked upstream and found [*TheRoc*k](https://github.com/ROCm/TheRock).

I had lots of initial trouble with *TheRock*‘s `CMake` monorepo/subprojects; I am not yet sure what’s up with that, but I suspect it may be `ppc64le`-specific. That said, I was able to make progress by building individual subprojects one-by-one (this is probably a better approach anyway, at this stage of porting).

Eventually I got `amd-llvm` bootstrapped, built with a minimal configuration with *Trixie*‘s `gcc` `14.2.0`. Then I built `amd-llvm` with itself, in the *TheRock*-recommended configuration, except for the `PowerPC` and `AMDGPU` targets. Next I built `rocminfo`. It segfaulted in the same place as *Debian*‘s package! Some debugging resulted in [a patch](https://www.fitzsim.org/patches/0001-rocr-Fix-vDSO-detection-on-ppc64-architectures-in-os.patch) to accommodate `ppc64`‘s `vDSO` naming; that eliminated the segault.

Then `rocminfo` ran and showed both the CPUs as “Agents” 0 and 1. But no sign of the GPU.

I further debugged `rocminfo` and found it was traversing `sysfs`, and specifically the *AMD* *Kernel Fusion Driver* (`kfd`) topology. The card did not have an entry there.

I looked at `dmesg` and noticed:

```
[...] amdgpu 0033:03:00.0: amdgpu: Error parsing VCRAT
[...] kfd kfd: amdgpu: Error adding device to topology
[...] kfd kfd: amdgpu: Error initializing KFD node
[...] kfd kfd: amdgpu: device 1002:7551 NOT added due to errors
```

First I tried building and updating a `.deb` of the [`linux-firmware` from its `Git` repository](https://gitlab.com/kernel-firmware/linux-firmware), to rule out the parsing error being caused by an outdated binary-only firmware blob. (This is my one disappointment with the *ROCm* stack; it would be great if the firmware and firmware toolchains were free software.) Rebooting with the new firmware produced the same result.

I looked at the kernel source for that driver, and noticed extra debug `printk`s. *Debian* helpfully enables the `CONFIG_DYNAMIC_DEBUG` kernel option. I tried dynamically reloading the `amdgpu` driver and various *PCIe* and GPU reset approaches, but I could not get the card back to its after-boot state. I would have to reboot to test each change.

I added `amdgpu.dyndbg="+p"` to the kernel command line, and that gave me some extra `kfd` messages; with those I narrowed down the failure to the `IO link` entry of the *Virtual Component Resource Association Table* (`VCRAT`).

I re-reviewed `dmesg` and, earlier than the parsing error, there was another clue:

```
[...] amdgpu: IO link not available for non x86 platforms
```

That message was printed during the creation of the CPU `VCRAT` (in `kfd_create_vcrat_image_cpu`). That was the `#else` branch of a platform-specific `#ifdef`. `kfd_create_vcrat_image_gpu` which did not have a corresponding `#ifdef`; “this could explain the subsequent parsing failure on the `VCRAT` IO link entry, on `ppc64le`, a non-`x86` platform”, I thought.

It was time to recompile the *Linux* kernel. *Debian* makes this surprisingly easy; I followed the [official instructions](https://kernel-team.pages.debian.net/kernel-handbook/ch-common-tasks.html) to build a custom kernel `.deb` with [my attempted fix](https://www.fitzsim.org/patches/0001-drm-amdgpu-fix-non-x86-GPU-VCRAT-parsing.patch) applied to the `amdgpu.ko` module. Another reboot and no more `VCRAT` parsing failure message in `dmesg`. That seemed like more progress. (Perhaps a more proper solution would be to add `IO link` support to `ppc64le` upstream; I don’t know if there is an equivalent *POWER9* capability, hardware-wise. For my purposes, I have not yet needed an `IO link`.)

`rocminfo` still failed though, albeit in a new way:

```
hsa api call failure at: /TheRock/rocm-systems/projects/rocminfo/rocminfo.cc:1329
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

The co-timed `dmesg` messages were:

```
[...] amdgpu 0033:03:00.0: amdgpu: bo 00000000bdd46d97 va 0x0ffffffbfe-0x0ffffffc1d conflict with 0x0ffffffc00-0x0ffffffe00
[...] amdgpu: Failed to map VA 0xffffffbfe000 in vm. ret -22
[...] amdgpu: Failed to map bo to gpuvm
```

I analyzed the section of kernel driver code that generated those messages and noticed the use of `AMDGPU_GPU_PAGE_SIZE` in range calculations. It is hard-coded to `4096`.

I had a hunch that the driver needed the kernel’s page size to match. I did a quick side quest to [change all my virtual machines to use `4KiB` pages](https://wiki.raptorcs.com/wiki/Virtualization), reconfigured my custom *Debian* kernel for `4KiB` pages, and rebooted again.

Now the virtual machines loaded, and finally `rocminfo` [showed the card’s information](https://www.fitzsim.org/screenshots/ppc64le-amd-radeon-ai-pro-r9700-rocminfo.txt)!

```
[...]
*******
Agent 3
*******
  Name:                    gfx1201
  Uuid:                    GPU-6413e1798933ffe0
 ...