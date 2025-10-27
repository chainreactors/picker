---
title: Simple macOS kernel extension fuzzing in userspace with IDA and TinyInst
url: https://googleprojectzero.blogspot.com/2024/11/simple-macos-kernel-extension-fuzzing.html
source: Project Zero
date: 2024-11-22
fetch_date: 2025-10-06T19:29:42.333179
---

# Simple macOS kernel extension fuzzing in userspace with IDA and TinyInst

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Thursday, November 21, 2024

### Simple macOS kernel extension fuzzing in userspace with IDA and TinyInst

Posted by Ivan Fratric, Google Project Zero

Recently, one of the projects I was involved in had to do with video decoding on Apple platforms, specifically AV1 decoding. On Apple devices that support AV1 video format (starting from Apple A17 iOS / M3 macOS), decoding is done in hardware. However, despite this, during decoding, a large part of the AV1 format parsing happens in software, inside the kernel, more specifically inside the AppleAVD kernel extension (or at least, that used to be the case in macOS 14/ iOS 17). As fuzzing is one of the techniques we employ regularly, the question of how to effectively fuzz this code inevitably came up.

It should be noted that I wasn’t the first person to look into the problem of Apple kernel extension fuzzing, so before going into the details of my approach, other projects in this space should be mentioned.

In the [Fairplay research](https://www.google.com/url?q=https://github.com/pwn0rz/fairplay_research&sa=D&source=editors&ust=1732109826665586&usg=AOvVaw2FnTI8T0cVTT1L2JVZrloR) project, @pwn0rz utilized a custom loader to load the kernel extension into userspace. A coworker tried to run this code on the current AppleAVD extension, however it didn’t work for them (at least not out of the box) so we didn’t end up using it. It should be noted here that my approach also loads the kernel code into userspace, albeit in a more lightweight way.

In the [Cinema time!](https://www.google.com/url?q=https://2022.hexacon.fr/slides/hexacon2022_AppleAVD.pdf&sa=D&source=editors&ust=1732109826665829&usg=AOvVaw37MzWB_X_wWGPblQWVVSgA) presentation at Hexacon 2022, Andrey Labunets and Nikita Tarakanov presented their approach for fuzzing AppleAVD where the decompiled code was first extracted using IDA and then rebuilt. I used this approach in the past in some more constrained scenarios, however the decompiled code from IDA is not perfect and manual fixing was often required (such as, for example, when IDA would get the stack layout of a function incorrectly).

In the [KextFuzz](https://www.google.com/url?q=https://www.usenix.org/conference/usenixsecurity23/presentation/yin&sa=D&source=editors&ust=1732109826666172&usg=AOvVaw01DJ5e3AtzVICfDMFA--b9) project, Tingting Yin with the co-authors statically instrumented kernel extensions by replacing pointer authentication instructions with a jump to a coverage-collecting trampoline, which results in a partial coverage.

Most recently, the [Pishi](https://www.google.com/url?q=https://r00tkitsmm.github.io/fuzzing/2024/11/08/Pishi.html&sa=D&source=editors&ust=1732109826666444&usg=AOvVaw3AlBWiaSYgHpY_zWen8REB) project by Meysam Firouzi was released just before this research. The project statically instruments kernel extension code by using Ghidra to identify all basic blocks, and then replacing one instruction from each basic block with a branch to a dedicated trampoline. The trampoline records the coverage, executes the replaced instruction and jumps back to the address of the next instruction. This was reported to run on a real device.

Given the existence of these other projects, it is worth saying that my goal was not to create necessarily the “best” method for kernel extension fuzzing, but what for me was the simplest (if we don’t count the underlying complexity of the off-the shelf tools being used). In short, my approach, that will be discussed in detail in other sections, was

1. Load AppleAVD extension or full kernelcache into IDA
2. Rebase the module to an address that can be reliably allocated in userspace
3. Export raw memory using an IDA Python script
4. Load exported bytes using custom loader
5. Use custom [TinyInst](https://www.google.com/url?q=https://github.com/googleprojectzero/TinyInst&sa=D&source=editors&ust=1732109826667480&usg=AOvVaw2o31c8GLJoKLv7nsymgTWI) module to hook and instrument the extension
6. Use [Jackalope](https://www.google.com/url?q=https://github.com/googleprojectzero/Jackalope&sa=D&source=editors&ust=1732109826667687&usg=AOvVaw0RtwSfpDaMMyf56zmPPGGc) for fuzzing

All the project code can be found [here](https://www.google.com/url?q=https://github.com/googleprojectzero/p0tools/tree/master/SimpleKextFuzzing&sa=D&source=editors&ust=1732109826667926&usg=AOvVaw0hlvs1WHxSpAssYFPacajC). Various components will be explained in more detail throughout the rest of the blog post.

# Extracting kernel extension code

Normally, on macOS, kernel extensions are packaged inside “kernel collections” files that serve as containers for multiple extensions. At first OS boot (and whenever something is changed with regards to kernel extensions), the kernel extensions needed by the machine are repackaged into what is called the “kernel cache” (kernelcache file on the filesystem). Kernel extensions can be extracted from these caches and collections, but existing tooling can’t really produce individual .dylib files that can be loaded into userspace and run without issues.

However, reverse engineering tooling, specifically IDA Pro which I used in this research, comes with a surprisingly good loader for Apple kernel cache. I haven’t tried how other reverse engineering tools compare, but if they are comparable and someone would like to contribute to the project, I would gladly accept export scripts for these other tools.

So, instead of writing our own loader, we can simply piggyback on IDA’s. The idea is simple:

* we let IDA load the kernel extension we want (or even the entire kernelcache)
* we use IDA to rebase the code so it’s in memory range that is mappable in userspace (see image)
* using a simple IDA Python script, we export for each memory segment its start address, end address, protection flags and raw bytes
* optionally, we can also, using the same script, export all the symbol names and the corresponding addresses so we can later refer to symbols by name

The following image shows rebasing of the kernel extension. This functionality is accessible in IDA via Edit->Segments->Rebase program… menu. When choosing the new base address, it is convenient to only change the high bits which makes it easy to manually convert rebased to original addresses and vice versa when needed. In the example below the image base was changed from 0xFFFFFE000714C470 to  0xAB0714C470.

[![screenshot with image base selected, with the value set at  0xAB0714C470, with both the fix up the program and rebase the whole image options selected](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDdHVy0QXxYeSOzvh7t0mKsZgntTGvhyeLPNjtk-wjAqE80-xx8M6r9I3soy_EdWgj9XmrRcyMPcw0JqLSroCcTbw0sc8HR1tHFxSjhURZdCV4ikn6z_ZGMwQLXkOoe1wsCw-3jK9qow5mxzXOUtSczh4uN2gd07_1BqjiKJ0vgLFXnYzXpPU1xeEkx5k/s435/image1.png "screenshot with image base selected, with the value set at  0xAB0714C470, with both the fix up the program and rebase the whole image options selected")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDdHVy0QXxYeSOzvh7t0mKsZgntTGvhyeLPNjtk-wjAqE80-xx8M6r9I3soy_EdWgj9XmrRcyMPcw0JqLSroCcTbw0sc8HR1tHFxSjhURZdCV4ikn6z_ZGMwQLXkOoe1wsCw-3jK9qow5mxzXOUtSczh4uN2gd07_1BqjiKJ0vgLFXnYzXpPU1xeEkx5k/s435/image1.png)

Figure 1: Rebasing the extension

The IDA script for exporting the data can be found [here](https://www.google.com/url?q=https://github.com/googleprojectzero/p0tools/blob/master/SimpleKextFuzzing/segexport.py&sa=D&source=editors&ust=1732109826669199&usg=AOvVaw0cWfCbkZ7rLjG453N5Q3gz). You can run it using the following commands in IDA:

sys.path.append('/directory/containing/export/script')

import segexport

segexport.export('/path/to/output/file)

# Loading and running

Loading the exported data should now be only the matter of memory mapping the correct addresses and copying the corresponding data from the exported file. You can see it in the load() function [h...