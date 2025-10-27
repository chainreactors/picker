---
title: Hardening Firmware Across the Android Ecosystem
url: http://security.googleblog.com/2023/02/hardening-firmware-across-android.html
source: Google Online Security Blog
date: 2023-02-22
fetch_date: 2025-10-04T07:41:26.964667
---

# Hardening Firmware Across the Android Ecosystem

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Hardening Firmware Across the Android Ecosystem](https://security.googleblog.com/2023/02/hardening-firmware-across-android.html "Hardening Firmware Across the Android Ecosystem")

February 21, 2023

Posted by Roger Piqueras Jover, Ivan Lozano, Sudhi Herle, and Stephan Somogyi, Android Team

A modern Android powered smartphone is a complex hardware device: Android OS runs on a multi-core CPU - also called an Application Processor (AP). And the AP is one of many such processors of a System On Chip (SoC). Other processors on the SoC perform various specialized tasks — such as security functions, image & video processing, and most importantly cellular communications. The processor performing cellular communications is often referred to as the baseband. For the purposes of this blog, we refer to the software that runs on all these other processors as “Firmware”.

Securing the Android Platform requires going beyond the confines of the Application Processor (AP). Android’s defense-in-depth strategy also applies to the firmware running on bare-metal environments in these microcontrollers, as they are a critical part of the attack surface of a device.

### **A popular attack vector within the security research community**

As the security of the Android Platform has been steadily improved, some security researchers have shifted their focus towards other parts of the software stack, including firmware. Over the last decade there have been numerous [publications](https://www.usenix.org/system/files/conference/woot12/woot12-final24.pdf), [talks](https://player.vimeo.com/video/214013463), [Pwn2Own contest winners](https://downloads.immunityinc.com/infiltrate2018-slidepacks/amat-cama-a-walk-with-shannon/presentation.pdf), and [CVEs](https://source.android.com/docs/security/bulletin/2022-06-01#unisoc-components) targeting exploitation of vulnerabilities in firmware running in these secondary processors. Bugs remotely exploitable over the air (eg. WiFi and cellular baseband bugs) are of particular concern and, therefore, are popular within the security research community. These types of bugs even have [their own categorization in well known 3rd party exploit marketplaces](https://www.zerodium.com/images/zerodium_prices_mobiles.png).

Regardless of whether it is remote code execution within the [WiFi SoC](https://googleprojectzero.blogspot.com/2017/04/over-air-exploiting-broadcoms-wi-fi_4.html) or within the cellular baseband, a [common](https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Over-The-Air-Baseband-Exploit-Gaining-Remote-Code-Execution-On-5G-Smartphones.pdf) and [resonating](https://speakerdeck.com/marcograss/exploitation-of-a-modern-smartphone-baseband) [theme](https://player.vimeo.com/video/214013463) has been the *consistent* lack of exploit mitigations in firmware. Conveniently, Android has significant [experience](https://security.googleblog.com/2021/01/data-driven-security-hardening-in.html) in enabling exploit mitigations across critical attack surfaces.

### **Applying years worth of lessons learned in systems hardening**

Over the last few years, we have [successfully enabled compiler-based mitigations](https://android-developers.googleblog.com/2018/06/compiler-based-security-mitigations-in.html) in Android — on the AP — which add additional layers of defense across the platform, making it harder to build reproducible exploits and to [prevent certain types of bugs from becoming vulnerabilities](https://android-developers.googleblog.com/2020/06/system-hardening-in-android-11.html). Building on top of these successes and lessons learned, we’re applying the same principles to hardening the security of firmware that runs outside of Android per se, directly on the bare-metal hardware.

In particular, we are working with our ecosystem partners in several areas aimed at hardening the security of firmware that interacts with Android:

* Exploring and enabling compiler-based sanitizers ([BoundSan](https://source.android.com/docs/security/test/bounds-sanitizer), [IntSan](https://source.android.com/docs/security/test/intsan)) and other exploit mitigations ([CFI](https://source.android.com/docs/security/test/cfi), [kCFI](https://source.android.com/docs/security/test/kcfi), [Shadow Call Stack](https://source.android.com/docs/security/test/shadow-call-stack), Stack Canaries) in firmware.* Enabling further memory safety features ([Auto-initialize Memory](https://source.android.com/docs/security/test/memory-safety/zero-initialized-memory)) in firmware.

### **Bare-metal support**

Compiler-based sanitizers [have no runtime requirements in trapping mode](https://releases.llvm.org/11.0.1/tools/clang/docs/UndefinedBehaviorSanitizer.html#usage), which provides a meaningful layer of protection we want: it causes the program to abort execution when detecting undefined behavior. As a result, memory corruption vulnerabilities that would otherwise be exploitable are now stopped entirely. To aid developers in testing, [troubleshooting](https://source.android.com/devices/tech/debug/bounds-sanitizer#troubleshooting), and generating bug reports on debug builds, both minimal and full diagnostics modes can be enabled, which require defining and linking the requisite runtime handlers.

Most Control Flow Integrity (CFI) schemes also work for bare-metal targets in trapping mode. LLVM’s[1](#fn1) CFI across shared libraries scheme (cross-DSO) is the exception as it requires a runtime to be defined for the target. Shadow Call Stack, an AArch64-only feature, has a runtime component which initializes the shadow stack. [LLVM does not provide this runtime for any target](https://clang.llvm.org/docs/ShadowCallStack.html#compatibility), so bare-metal users would need to define that runtime to use it.

### **The challenge**

Enabling exploit mitigations in firmware running on bare metal targets is no easy feat. While the AP (Application Processor) hosts a powerful operating system (Linux) with comparatively abundant CPU and memory resources, bare metal targets are often severely resource-constrained, and are tuned to run a very specific set of functions. Any perturbation in compute and/or memory consumption introduced by enabling, for example, compiler-based sanitizers, could have a significant impact in functionality, performance, and stability.

Therefore, it is critical to optimize how and where exploit mitigations are turned on. The goal is to maximize impact — harden the most exposed attack surface — while minimizing any performance/stability impact. For example, in the case of the cellular baseband, we recommend focusing on code and libraries responsible for parsing messages delivered over the air (particularly for pre-authentication protocols such as [RRC](https://onlinelibrary.wiley.com/doi/10.1002/9781118188545.ch3) and [NAS](https://www.dialogic.com/glossary/nas), which are the most exposed attack surface), libraries encoding/decoding complex formats (for example [ASN.1](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=asn.1)), and libraries implementing IMS (IP Multimedia System) functionality, or parsing SMS and/or MMS.

### **Fuzzing and Vulnerability Rewards Program**

Enabling exploit mitigations and compiler-based sanitizers are excellent techniques to minimize the chances of unknown bugs becoming exploitable. However, it is also important to continuously look for, find, and patch bugs.

Fuzzing continues to be a highly efficient method to find impactful bugs. It’s also been proven to be effective for signaling larger design issues in code. Our team partners closely with Android teams working on fuzzing and security assessments to leverage [their expertis...