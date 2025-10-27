---
title: Attacking the Samsung Galaxy A Boot Chain
url: https://blog.quarkslab.com/attacking-the-samsung-galaxy-a-boot-chain.html
source: Instapaper: Unread
date: 2024-10-19
fetch_date: 2025-10-06T18:56:32.641711
---

# Attacking the Samsung Galaxy A Boot Chain

[Quarkslab's blog](./index.html)

##### [Quarkslab's blog](./index.html)

---

* [Categories](./categories.html)
* [Tags](./tags.html)
* [Authors](./authors.html)

---

* [Quarkslab](https://www.quarkslab.com/)
* [linkedin](https://linkedin.com/company/quarkslab)
* [X](https://x.com/quarkslab)
* [mastodon](https://infosec.exchange/%40quarkslab)
* [bluesky](https://bsky.app/profile/quarkslab.bsky.social)
* [github](https://github.com/quarkslab)

---

* Toggle theme

  + Light
  + Dark

* #### Table of contents
* + [Introduction](#introduction "Introduction")
  + [Little Kernel](#little kernel "Little Kernel")
  + [Secure Monitor](#secure monitor "Secure Monitor")
  + [Conclusion](#conclusion "Conclusion")
  + [Acknowledgment](#acknowledgment "Acknowledgment")

# [Attacking the Samsung Galaxy A\* Boot Chain](./attacking-the-samsung-galaxy-a-boot-chain.html "Permalink to Attacking the Samsung Galaxy A* Boot Chain")

Posted
Tue 15 October 2024

Authors
[Maxime Rossi Bellom](./author/maxime-rossi-bellom.html),
[RaphaÃ«l Neveu](./author/raphael-neveu.html)

Category
[Android](./category/android.html)

Tags
[reverse-engineering](./tag/reverse-engineering.html),
[exploitation](./tag/exploitation.html),
[vulnerability](./tag/vulnerability.html),
[Android](./tag/android.html),
[2024](./tag/2024.html)

---

We discovered several vulnerabilities impacting the boot chain of several Samsung devices. Chained together, they allow us to execute code in the bootloader, get root access on Android with persistency, and finally leak anything from the Secure World's memory including the Android Keystore keys.

---

## Introduction

We targeted the middle-end device Samsung Galaxy A225F on which we had gathered a good knowledge over its boot process during our previous research analyzing the [Android File-Based encryption scheme](https://blog.quarkslab.com/android-data-encryption-in-depth.html). The vulnerabilities impact two critical components of the system: Little Kernel which is the third bootloader responsible for booting the Android OS, and the Secure Monitor which is the piece of software running with the highest privileges on the device. Other devices from the Galaxy A family are also impacted by some of these vulnerabilities.

We presented how we discovered and exploited these vulnerabilities at [BlackHat USA 2024](https://www.blackhat.com/us-24/briefings/schedule/#attacking-samsung-galaxy-a-boot-chain-and-beyond-38526). A whitepaper describing the work done is [also available](https://www.sstic.org/media/SSTIC2024/SSTIC-actes/when_vendor1_meets_vendor2_the_story_of_a_small_bu/SSTIC2024-Article-when_vendor1_meets_vendor2_the_story_of_a_small_bug_chain-rossi-bellom_neveu.pdf).

Along with this blog post, we release the proof-of-concepts for the 4 vulnerabilities we discovered on [github](https://github.com/quarkslab/samsung-bootchain-poc).

## Little Kernel

The two vulnerabilities in Little Kernel are the following:

* **CVE-2024-20832** (SVE-2023-2079): Heap overflow in Little Kernel

> Samsung added a custom JPEG parser in Little Kernel that is used to show logos and error messages while booting. The code responsible for loading the JPEG file will place it in a fixed-size structure on the heap. But it never checks the size of the file, causing a heap overflow.
>
> And thanks to the simplicity of the heap algorithm and the lack of mitigation, it is possible to exploit this vulnerability and achieve code execution in Little Kernel, with persistency (it should survive reboots and factory resets).
>
> It is interesting to note that the partition containing the JPEGs (called `up_param`) is not verified at boot, allowing an attacker with the capability to modify the internal memory of the device to change them and to trigger the vulnerability.

* **CVE-2024-20865** (SVE-2024-0234): Odin authentication bypass in Little Kernel

> Odin is the recovery system implemented by Samsung in Little Kernel, and it allows us to flash partitions through USB. Odin will authenticate the images being flashed, so images must be signed (and it should not be possible to flash custom images).
>
> However, we discovered a vulnerability allowing us to bypass the authentication. Two partition tables are used by Little Kernel: the GPT (GUID Partition Table) and the PIT (Partition Information Table) which is used by Odin. The GPT happens to be flashable through Odin without authentication! We leveraged this issue in order to modify the PIT and allow us to flash other partition without authentication. Thanks to this issue, we can flash arbitrary data on the internal memory of the device through USB, which includes the partition `up_param` containing the JPEGs needed to exploit the previous vulnerability.

By chaining these two vulnerabilities we can, through USB, execute code in Little Kernel with persistency. And since Little Kernel is responsible for verifying and booting Android, we used our exploit to patch the code and disable the verification of the `boot` image. That way we can boot a modified (in this case a rooted) Android system.

At this point we can already do many things with our root privileges in Android (like accessing most of the user's data). But, by design, some components like the keys of the Android Keystore are not reachable, even by root, since there are protected with the Secure World. To get them, we need to elevate privileges...

## Secure Monitor

The Secure Monitor (also called ARM Trusted Firmware) is the highest privileged component running on the device. It is reachable from Normal and Secure World kernels through SMC instructions and allows the two worlds to communicate with each other. It makes this component particularly interesting for vulnerability research. We targeted the SMC handlers accessible from the Linux Kernel and discovered two vulnerabilities:

* **CVE-2024-20820** (SVE-2023-2215): Read out-of-bound in Secure Monitor

> There is a read out-of-bound in a specific handler (corresponding to the id `0xc2000526`), which permits us to leak the full memory virtually mapped in the Secure Monitor.

* **CVE-2024-20021**: Mapping arbitrary physical memory to virtual memory

> Another handler (corresponding to the id `0x8200022a`) allows us to *mmap* arbitrary physical addresses (up to 1 MB at a time) at the same virtual ones in the Secure Monitor. Since there is no way to ummap the addresses, we are limited to 8 consecutive mmaps which represent 8 MB of data.

It is possible to chain these two vulnerabilities in order to leak anything from the system memory, including the Secure World. The only constraint is the number of consecutive mmaps limited to 8.

We implemented a little demo showing how we used these vulnerabilities to leak a key from the Android Keystore.

## Conclusion

The chain of 4 bugs we presented allowed us to execute code in Little Kernel from USB, get a root access on Android with persistency, and finally leak anything from the Secure World's memory which includes the Android Keystore keys. The device on which we did this research and implemented the exploits is a Samsung Galaxy A225F, but most of the Samsung devices based on a Mediatek SoC are vulnerable to, at least, the vulnerabilities in Little Kernel.

More details on these vulnerabilities and exploits can be found in the [whitepaper](https://www.sstic.org/media/SSTIC2024/SSTIC-actes/when_vendor1_meets_vendor2_the_story_of_a_small_bu/SSTIC2024-Article-when_vendor1_meets_vendor2_the_story_of_a_small_bug_chain-rossi-bellom_neveu.pdf) or by viewing the talk we gave at [BlackHat USA 2024](https://www.blackhat.com/us-24/briefings/schedule/#attacking-samsung-galaxy-a-boot-chain-and-beyond-38526) (soon to be released).

The exploits for the 4 vulnerabilities can be found on our [github repository](https://github.com/quarkslab/samsung-bootchain-poc).

## Acknowledgment

A huge thanks to the two other contributors on this research: Damiano Melotti and Gabrielle Viala, and to our colleagues who...