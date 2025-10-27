---
title: Magniber ransomware analysis: Tiny Tracer in action
url: https://hshrzd.wordpress.com/2023/03/30/magniber-ransomware-analysis/
source: hasherezade's 1001 nights
date: 2023-03-31
fetch_date: 2025-10-04T11:13:45.539245
---

# Magniber ransomware analysis: Tiny Tracer in action

[hasherezade's 1001 nights](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

projects and tasks that I do in my free time

[![](https://hshrzd.wordpress.com/wp-content/uploads/2013/12/cropped-sky31.jpg)](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

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

[← Flare-On 9 – Task 8](https://hshrzd.wordpress.com/2022/11/12/flare-on-9-task-8/)

[Flare-On 11 – Task 10 →](https://hshrzd.wordpress.com/2024/10/27/flare-on-11-task-10/)

## [Magniber ransomware analysis: Tiny Tracer in action](https://hshrzd.wordpress.com/2023/03/30/magniber-ransomware-analysis/)

Posted on [March 30, 2023](https://hshrzd.wordpress.com/2023/03/30/magniber-ransomware-analysis/ "9:39 pm") by [hasherezade](https://hshrzd.wordpress.com/author/hshrzd/ "View all posts by hasherezade")

## Intro

Magniber is a ransomware that was initially targeting South Korea. My first report on this malware was written for Malwarebytes in 2017 ([here](https://www.malwarebytes.com/blog/news/2017/10/magniber-ransomware-exclusively-for-south-koreans)).

Since then, the ransomware was completely rewritten, and turned into a much more complex beast. The articles showing the timeline of the evolution of Magniber ransomware are available here: [Magniber at Malpedia](https://malpedia.caad.fkie.fraunhofer.de/details/win.magniber). In this writeup we will have a deep dive in a one of the samples from the updated edition.

**Note that the sample described here is not new**: it has been discovered in 2022 and analyzed by various researchers. Due to the fact that this malware uses raw syscalls, I decided that it is a good example to showcase [the new version of Tiny Tracer (v2.3)](https://github.com/hasherezade/tiny_tracer/releases), allowing to trace syscalls. However, this writeup is not limited to a short demo, but shows the analysis process step by step, from the beginning. Tiny Tracer will help us easily reach the hidden core of this obfuscated ransomware: the code directly responsible for the files encryption process.

---

## Analyzed sample

1. [7bb15a442a5aed5b2fa47eef3bc292e9](https://www.virustotal.com/gui/file/74e922ff426dc1146188fe48db8410ff720d2a2e8641af902a6891539ced6077/detection) – Original sample: the MSI installer
2. [796eb864005f3393c3adce70dc31d6ba](https://www.virustotal.com/gui/file/ba28c3d409daa2e3685673fe2dde9d8c93aec2b35c478fd66d4c407deceec63c) – the Magniber DLL
3. [882a21d7c07b3997d87e970f30110243](https://www.virustotal.com/gui/file/3a2b8ef624b4318fc142a6266c70f88799e80d10566f6dd2d8d74e91d651491a/detection) – the Magniber’s injector (shellcode#1)
4. [a841c3bf69df48f7b796752d7c86bc38](https://www.virustotal.com/gui/file/3a2b8ef624b4318fc142a6266c70f88799e80d10566f6dd2d8d74e91d651491a/detection) – the Magniber’s core (shellcode#2)

## Behavioral analysis

When executed, this rasomware runs silently, encrypting files with selected extensions, and appending its own extension at the end. In case of the currently analyzed sample, the added extention is ‘`vieijibfm`‘. In each directory with encrypted files, we can also find a ransom note: `README.html`.

![](https://hshrzd.wordpress.com/wp-content/uploads/2023/03/locked_example-1.png?w=308)

Visualization of an encrypted BMP file – before and after (created with the help of [file2png.py](https://github.com/hasherezade/crypto_utils/blob/master/file2png.py)):

![](https://hshrzd.wordpress.com/wp-content/uploads/2023/03/enc_square1.bmp.png?w=219)

Before the encryption

![](https://hshrzd.wordpress.com/wp-content/uploads/2023/03/enc_square1-another-copy.bmp.vieijibfm.png?w=219)

After the encryption by Magniber

The entropy of the encrypted file is high, and there are no patterns visible. This may suggest that some strong encryption was used, possibly AES with block chaining (CBC mode).

It drops, runs and then deletes a VBS script in `C:\Users\Public` , under a random name:

![](https://hshrzd.wordpress.com/wp-content/uploads/2023/03/dropped.png)

We can also find there two files with pseudorandom names, that are used as mutexes, to indidate that the encryption is running, or completed. At the end, the PNG file is dropped in the same directory:

![](https://hshrzd.wordpress.com/wp-content/uploads/2023/03/dropped_png.png)

After a while, the wallpaper gets changed to the dropped PNG, announcing the attack:

![](https://hshrzd.wordpress.com/wp-content/uploads/2022/12/encrypted.png?w=1024)

The information printed at the wallpaper mentions the ransom note `README.html` where the victim can find more information.

The content of the `README.html` has the following form:

![](https://hshrzd.wordpress.com/wp-content/uploads/2023/03/ransom_note-1-1.png)

It mentions further a Tor website, that can be used to make the contact with the attacker, and possibly buy the key for files decryption. At the time of this analysis, the website was not available.

While the extension added to the encrypted files didn’t change, and also occurs in the note, the used number at the beginning of the address is generated per attack.

Note that the ransom note is almost identical as the note used by the old Magniber’s version from 2017:

![](https://hshrzd.wordpress.com/wp-content/uploads/2023/03/ransom_note-1.png)

*Above: ransom note from the old Magniber’s edition (from 2017), full analysis at: <https://www.malwarebytes.com/blog/news/2017/10/magniber-ransomware-exclusively-for-south-koreans>*

## Inside

### Upacking the MSI

Magniber sample comes packed in the MSI (Microsoft Installer). We can view the scripts inside with Microsoft’s tool, Orca MSI (mirror: [here](https://www.technipages.com/download-orca-msi-editor)).

![](https://hshrzd.wordpress.com/wp-content/uploads/2022/12/msi_pic.png?w=612)

By looking at the “Custom Action” we find out that the binary to be run is named “utskzc”, and the function that will be executed from there is “mvrtubhpxy”. In order to access that binary we need to unpack the content of the MSI package. We can do it with the help of 7zip.

Then we find out that the aforementioned binary is a PE file, and it exports the function “mvrtubhpxy”.

![](https://hshrzd.wordpress.com/wp-content/uploads/2022/12/export_table.png)

This is where the execution of the binary starts.

### Overview of Magniber’s DLL

If we try to open this binary in IDA, we can clearly see that this binary is obfuscated. The execution starts from a single call…

![](https://hshrzd.wordpress.com/wp-content/uploads/2023/03/inside_export.png?w=414)

…that leads into a “rabbithole” of jumps…

![](https://hshrzd.wordpress.com/wp-content/uploads/2023/03/jumps_list.png?w=735)

How can we analyze the ransomware inner workings, when it is so hard to even find the relevant code? It isn’t as hard as it seems if we involve DBI (Dynamic Binary Instrumentation) tools, such as Pin-based [Tiny Tracer](https://github.com/hasherezade/tiny_tracer).

### Tracing the first stage executable

Let’s dive into the sample by tracing it with [Tiny Tracer](https://github.com/hasherezade/tiny_tracer) (you can find the installation instructions [here](https://github.com/hasherezade/tiny_tracer/wiki/Installation)). To makes things easier, I converted the DLL into EXE (as described [here](https://hshrzd.wordpress.com/2016/07/21/how-to-turn-a-dll-into-a-standalone-exe/)), changing its entry point to the exported function (since the `DllMain` does not do much in this case, and the exported function takes ...