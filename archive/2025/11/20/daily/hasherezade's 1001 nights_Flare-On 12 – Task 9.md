---
title: Flare-On 12 – Task 9
url: https://hshrzd.wordpress.com/2025/11/20/flare-on-12-task-9/
source: hasherezade's 1001 nights
date: 2025-11-20
fetch_date: 2025-11-21T03:12:23.161404
---

# Flare-On 12 – Task 9

[hasherezade's 1001 nights](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

projects and tasks that I do in my free time

[![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/a-picture-with-1000-locked-and-chained-boxes-in-the.png?w=940&h=198&crop=1)](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

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

[← Tutorial: unpacking executables with TinyTracer + PE-sieve](https://hshrzd.wordpress.com/2025/03/22/unpacking-executables-with-tinytracer-pe-sieve/)

## [Flare-On 12 – Task 9](https://hshrzd.wordpress.com/2025/11/20/flare-on-12-task-9/)

Posted on [November 20, 2025](https://hshrzd.wordpress.com/2025/11/20/flare-on-12-task-9/ "6:07 am") by [hasherezade](https://hshrzd.wordpress.com/author/hshrzd/ "View all posts by hasherezade")

*In this mini-series I describe the solutions of my favorite tasks from this year’s [Flare-On competition](https://flare-on12.ctfd.io/scoreboard). To those of you who are not familiar, [Flare-On](https://flare-on.com/) is a marathon of reverse engineering. This year it ran for 4 weeks, and consisted of 9 tasks of increasing difficulty. Collection of my sourcecodes created in the process of solving can be found in my Github repository [flareon\_2025](https://github.com/hasherezade/flareon2025).*

Task 9 was the last one, and it came with a significant increase in the difficulty level compared to the earlier tasks.

SHA256 of the executable: `785a6e2bb7ce9685afe80589bbc7e28b1676e003b0041e1f74e4984044a4e551`.

# Overview

## PE-bear

The file is a 64-bit Windows PE. Since the very first look we can see that it is quite big: `1.07 GB`. When we run it from command-line, we get:

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t9_running.png?w=296)

I started by opening it in PE-bear. We can spot that the `.rsrc` section takes the majority of space.

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t9_res.png?w=731)

The natural next step in this situation would be to see the list of the resources. At first, PE-bear showed me only 50 entries in the resources directory (due to a hard-limit set in code, that is now removed; in reality there are 10000 of them). It is clear from the first look that the resources are compressed PE files. The pattern starting the header looked familiar to me from malware analysis: it is `M8Z` – which suggests compression with [aPlib](https://ibsensoftware.com/products_aPLib.html).

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t9_resources_1.png?w=725)

It can be decompressed with a Python script using [`malduck` library](https://github.com/CERT-Polska/malduck) (example [here](https://github.com/hasherezade/flareon2025/blob/main/task9/dump_dlls/aplib_decompress.py)).

## IDA

Before proceeding further I decided to take a look in IDA.

The PE files from the resources are indeed loaded, and manually mapped:

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t9_libs_load.png?w=659)

The function that loads the PEs (renamed to `pass_Buffer1_and_load_libs`) occurs in the function responsible for checking the license, and is called in the loop 10000 times.

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t9_call_the_loop.png?w=825)

This shed light on why the executable is named `10000.exe` : it carries inside 10000 of different DLLs.

## Extracting DLLs

After removing the hardcoded limit PE-bear was able to see all the DLLs, and dump them into a selected directory. Decompressed the full directory content with the help of the following script:

+ [`aplib_decompress.py`](https://github.com/hasherezade/flareon2025/blob/main/task9/dump_dlls/aplib_decompress.py)

As a result I obtained 10000 DLLs, with the export tables similar to the following:

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t9_dll_exports.png?w=695)

Each DLL has a long list of entries with mangled names. Two distinct types appear. There are multiple functions with a name like \_Z21f00155255799705906783Ph ( format: `_Z21f{number}Ph`) – for simplicity, they will be referenced as “f” functions. In addition to it, each DLL has exactly only one “check” function (`_Z5checkPh`) .

The real names of the DLLs are stored in the Export Table, so, with the help of another script, using `pefile` I renamed them to the stored names.

+ [rename\_dlls.py](https://github.com/hasherezade/flareon2025/blob/main/task9/dump_dlls/rename_dlls.py)

The DLLs are not just independent units. They may import each other:

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t9_imports.png?w=808)

As we can see, they use for it simplified version of their names – without the “.real.” part. So, in order to keep it consistent, I made a little cleanup script, that walks though all the DLLs and rename them accordingly:

+ [remove\_name\_part.py](https://github.com/hasherezade/flareon2025/blob/main/task9/dump_dlls/remove_name_part.py)

As a result we have all DLLs: from 0000.dll to 9999.dll stored in a directory. That is in total around 4 GB of data.

# Understanding the flow

As the initial overview already revealed, the task is about checking some license file. At this point we have several questions to answer:

1. What is the expected format of the license file?
2. What is the condition that makes the license correct?
3. How does it connect to the DLLs that we just obtained?

The code of this challenge is not obfuscated, so it is relatively easy to follow. Most important actions happen in the function at VA = `0x140001e87` denoted as `verify_license`.

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t9_verif.png?w=836)

Analyzing the code of the following function, few things come to light.

* The license is supposed to be stored in the file license.bin, in the same directory as the task
* Its size is exactly 0x53020 bytes
* the content is read into a buffer, and SHA256 hash is calculated first. This hash will be used at the end.
* The license consists of 10000 chunks. Each of them is 34 bytes long. The first WORD of the chunk must be not greater than 9999. It is an index, used to decide what DLL should be used for the verification of that chunk. The appropriate DLL is fetched from the resources, and manually loaded. Then, the function “check” (mangled \_Z5checkPh) is called, with the current chunk passed as an argument. If the chunk verification failed, the loop exits with an error.
* Each iteration causes an update of another, global buffer. This buffer is then compared with the hardcoded one using simple `memcmp`. If the comparison fails, the application exits with an error.
* If all the steps passed, the license is accepted. The previously calculated SHA256 of the license is used to decrypt the flag.

There are still some more details to figure out, but at this point we can answer the 3 basic questions:

1. What is the expected format of the license file?

* The license is expected to be exactly 0x53020 bytes long. It consists of 10000 chunks. Each chunk contains (1+16) WORDs, meaning it is 34 bytes long.

* The first WORD of the chunk denotes the ID (0–9999) of the DLL that will be used for its verification. The remaining 32 bytes are the content passed to the “`check`” function. The chunk is correct if the “check” function returned TRUE.

2. What is the condition that makes the license correct?

* The license must be filled with chunks that pass verification with each of th...