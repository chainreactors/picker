---
title: Memory Safe Languages in Android 13
url: http://security.googleblog.com/2022/12/memory-safe-languages-in-android-13.html
source: Google Online Security Blog
date: 2022-12-02
fetch_date: 2025-10-04T00:16:26.806257
---

# Memory Safe Languages in Android 13

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Memory Safe Languages in Android 13](https://security.googleblog.com/2022/12/memory-safe-languages-in-android-13.html "Memory Safe Languages in Android 13")

December 1, 2022

Posted by Jeffrey Vander Stoep

For more than a decade, memory safety vulnerabilities have consistently represented more than 65% of vulnerabilities [across products, and across the industry](https://alexgaynor.net/2020/may/27/science-on-memory-unsafety-and-security/). On Android, we’re now seeing something different - a significant drop in memory safety vulnerabilities and an associated drop in the severity of our vulnerabilities.

Looking at vulnerabilities reported in the [Android security bulletin](https://source.android.com/docs/security/bulletin), which includes [critical/high](https://source.android.com/docs/security/overview/updates-resources#severity) severity vulnerabilities reported through our [vulnerability rewards program](https://bughunters.google.com/about/rules/6171833274204160/android-and-google-devices-security-reward-program-rules) (VRP) and vulnerabilities reported internally, we see that the number of memory safety vulnerabilities have dropped considerably over the past few years/releases. From 2019 to 2022 the annual number of memory safety vulnerabilities dropped from 223 down to 85.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0Jc4WA4Zbch9KSu4ApG67kOIwSoxnTih3B43kfyr_nS8Q96-5eaS4l2Czb-ZDexcU6c5JMtnXboax5ZO1J0VbkqRKqfiIl5TtOfoTHmLiAivLPxRqpvTV1wJWNi0azR38SpKMFDLIcKjGRMwyOcKzdCEM4RBptIhVnR63DkWsg3brjQrG9D9rlAAvUA/s1600/Screenshot%202022-11-30%2011.08.27%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0Jc4WA4Zbch9KSu4ApG67kOIwSoxnTih3B43kfyr_nS8Q96-5eaS4l2Czb-ZDexcU6c5JMtnXboax5ZO1J0VbkqRKqfiIl5TtOfoTHmLiAivLPxRqpvTV1wJWNi0azR38SpKMFDLIcKjGRMwyOcKzdCEM4RBptIhVnR63DkWsg3brjQrG9D9rlAAvUA/s1600/Screenshot%202022-11-30%2011.08.27%20PM.png)

This drop coincides with a shift in programming language usage away from memory unsafe languages. **Android 13 is the first Android release where a majority of new code added to the release is in a memory safe language**.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigIE5IcW8C7JTLXvkcJzrChCsF8-y37632RSEbvTbhjplY5A4Tafvk2IuRKYShxjeznoC-EK3v9IrnpehiT_wUdnGGkvUKf5YSv8Dh9pLaD5GtPBu5O4JHP97ah5XFticV-aCt7G7YX-NIfRFXPhDbQ_pVNROX2ifIDCgBck6KyzZG-CqcvRJiaxFIjw/s400/Screenshot%202022-11-30%2011.20.22%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigIE5IcW8C7JTLXvkcJzrChCsF8-y37632RSEbvTbhjplY5A4Tafvk2IuRKYShxjeznoC-EK3v9IrnpehiT_wUdnGGkvUKf5YSv8Dh9pLaD5GtPBu5O4JHP97ah5XFticV-aCt7G7YX-NIfRFXPhDbQ_pVNROX2ifIDCgBck6KyzZG-CqcvRJiaxFIjw/s626/Screenshot%202022-11-30%2011.20.22%20PM.png)

As the amount of new memory-unsafe code entering Android has decreased, so too has the number of memory safety vulnerabilities. From 2019 to 2022 it has dropped from 76% down to 35% of Android’s total vulnerabilities. **2022 is the first year where memory safety vulnerabilities do not represent a majority of Android’s vulnerabilities**.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQtnkSTDtPq_NDcTMM-zh_Ck9IFGj9Y9sC2yvZ7MRSYCSKZ9mqkYt5hfbxXZhrmAUdxxinY8GnNtT8_H0T6it9k0_mmjaWrxpbKhFMuR8N9eOopGBfKn5zxRH92hxO36ZTWdT0fl7ss2B8udmDgryj5BYhKkuYcqKQYemUMqGGwONg00C_DibLdyBiZQ/s1600/Screenshot%202022-11-30%2011.12.01%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQtnkSTDtPq_NDcTMM-zh_Ck9IFGj9Y9sC2yvZ7MRSYCSKZ9mqkYt5hfbxXZhrmAUdxxinY8GnNtT8_H0T6it9k0_mmjaWrxpbKhFMuR8N9eOopGBfKn5zxRH92hxO36ZTWdT0fl7ss2B8udmDgryj5BYhKkuYcqKQYemUMqGGwONg00C_DibLdyBiZQ/s1600/Screenshot%202022-11-30%2011.12.01%20PM.png)

While correlation doesn’t necessarily mean causation, it’s interesting to note that the percent of vulnerabilities caused by memory safety issues seems to correlate rather closely with the development language that’s used for new code. This matches the [expectations published in our blog post 2 years ago](https://security.googleblog.com/2021/04/rust-in-android-platform.html) about the age of memory safety vulnerabilities and why our focus should be on new code, not rewriting existing components. Of course there may be other contributing factors or alternative explanations. However, the shift is a major departure from industry-wide trends that have persisted for more than a decade (and likely longer) despite substantial investments in improvements to memory unsafe languages.

We continue to invest in tools to improve the safety of our C/C++. Over the past few releases we’ve introduced the Scudo hardened allocator, HWASAN, GWP-ASAN, and KFENCE on production Android devices. We’ve also increased our fuzzing coverage on our existing code base. Vulnerabilities found using these tools contributed both to prevention of vulnerabilities in new code as well as vulnerabilities found in old code that are included in the above evaluation. These are important tools, and critically important for our C/C++ code. However, these alone do not account for the large shift in vulnerabilities that we’re seeing, and other projects that have deployed these technologies have not seen a major shift in their vulnerability composition. We believe Android’s ongoing shift from memory-unsafe to memory-safe languages is a major factor.

# Rust for Native Code

In Android 12 we announced support for the Rust programming language in the Android platform as a memory-safe alternative to C/C++. Since then we’ve been scaling up our Rust experience and usage within the Android Open Source Project (AOSP).

As we noted in the original announcement, our goal is not to convert existing C/C++ to Rust, but rather to shift development of new code to memory safe languages over time.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK7bZcWqsUDmKTeZEvMXZDXDoGViXjhUmjmkIpG7OwCKVVRK2Ps7UqWzENqylekR3jREu5j6uCcMp6KXC52LY_0vsPO33_6fzZB1lgCEP5bhcU-D4B1EUxWrrhfAR4j3Pu_jiIGSlNrRSov58resIoQcAPuoxbeccvY6PbCPl3E9oFLuCivwFoT-lG5g/s1600/Screenshot%202022-11-30%2011.13.29%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK7bZcWqsUDmKTeZEvMXZDXDoGViXjhUmjmkIpG7OwCKVVRK2Ps7UqWzENqylekR3jREu5j6uCcMp6KXC52LY_0vsPO33_6fzZB1lgCEP5bhcU-D4B1EUxWrrhfAR4j3Pu_jiIGSlNrRSov58resIoQcAPuoxbeccvY6PbCPl3E9oFLuCivwFoT-lG5g/s1600/Screenshot%202022-11-30%2011.13.29%20PM.png)

In Android 13, about 21% of all new native code (C/C++/Rust) is in Rust. There are approximately 1.5 million total lines of Rust code in AOSP across new functionality and components such as Keystore2, the new Ultra-wideband (UWB) stack, DNS-over-HTTP3, Android’s Virtualization framework (AVF), and various other components and their open source dependencies. These are low-level components that require a systems language which otherwise would have been implemented in C++.

## Security impact

**To date, there have been zero memory safety vulnerabilities discovered in Android’s Rust code.**

We don’t expect that number to stay zero forever, but given the volume of new Rust code across two Android releases, and the security-sensitive components where it’s being used, it’s a significant result. It demonstrates that Rust is fulfilling its intended purpose of preventing Android’s most common source of vulnerabilities. Historical vulnerability density is greater than 1/kLOC (1 vulnerability per thousand lines of code) in many of Android’s C/C++ components (e.g. media, Bluetooth, NFC, etc). Based on this historical vulnerability density, it’s likely that using Rust has already prevented hundreds of vulnerabilities from reaching production.

## What about unsafe Rust?

Operating system development requires acces...