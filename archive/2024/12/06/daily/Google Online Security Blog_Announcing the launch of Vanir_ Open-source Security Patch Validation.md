---
title: Announcing the launch of Vanir: Open-source Security Patch Validation
url: http://security.googleblog.com/2024/12/announcing-launch-of-vanir-open-source.html
source: Google Online Security Blog
date: 2024-12-06
fetch_date: 2025-10-06T19:35:21.267715
---

# Announcing the launch of Vanir: Open-source Security Patch Validation

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Announcing the launch of Vanir: Open-source Security Patch Validation](https://security.googleblog.com/2024/12/announcing-launch-of-vanir-open-source.html "Announcing the launch of Vanir: Open-source Security Patch Validation")

December 5, 2024

Posted by Hyunwook Baek, Duy Truong, Justin Dunlap and Lauren Stan from Android Security and Privacy, and Oliver Chang with the Google Open Source Security Team

Today, we are announcing the availability of [Vanir](https://github.com/google/vanir), a new open-source security patch validation tool. Introduced at Android Bootcamp in April, Vanir gives Android platform developers the power to quickly and efficiently scan their custom platform code for missing security patches and identify applicable available patches. Vanir significantly accelerates patch validation by automating this process, allowing OEMs to ensure devices are protected with critical security updates much faster than traditional methods. This strengthens the security of the Android ecosystem, helping to keep Android users around the world safe.

By open-sourcing Vanir, we aim to empower the broader security community to contribute to and benefit from this tool, enabling wider adoption and ultimately improving security across various ecosystems. While initially designed for Android, Vanir can be easily adapted to other ecosystems with relatively small modifications, making it a versatile tool for enhancing software security across the board. In collaboration with the Google Open Source Security Team, we have incorporated feedback from our early adopters to improve Vanir and make it more useful for security professionals. [This tool is now available](https://github.com/google/vanir.) for you to start developing on top of, and integrating into, your systems.

The Android ecosystem relies on a multi-stage process for vulnerability mitigation. When a new vulnerability is discovered, upstream AOSP developers create and release upstream patches. The downstream device and chip manufacturers then assess the impact on their specific devices and backport the necessary fixes. This process, while effective, can present scalability challenges, especially for manufacturers managing a diverse range of devices and old models with complex update histories. Managing patch coverage across diverse and customized devices often requires considerable effort due to the manual nature of backporting.

To streamline the vital security workflow, we developed Vanir. Vanir provides a scalable and sustainable solution for security patch adoption and validation, helping to ensure Android devices receive timely protection against potential threats.

# The power of Vanir

## Source-code-based static analysis

Vanir’s first-of-its-kind approach to Android security patch validation uses source-code-based static analysis to directly compare the target source code against known vulnerable code patterns. Vanir does not rely on traditional metadata-based validation mechanisms, such as version numbers, repository history and build configs, which can be prone to errors. This unique approach enables Vanir to analyze entire codebases with full history, individual files, or even partial code snippets.

A main focus of Vanir is to automate the time consuming and costly process of identifying missing security patches in the open source software ecosystem. During the early development of Vanir, it became clear that manually identifying a high-volume of missing patches is not only labor intensive but also can leave user devices inadvertently exposed to known vulnerabilities for a period of time. To address this, Vanir utilizes novel automatic signature refinement techniques and multiple pattern analysis algorithms, inspired by the vulnerable code clone detection algorithms proposed by [Jang et al.](https://ieeexplore.ieee.org/document/6234404) [1] and [Kim et al.](https://ieeexplore.ieee.org/document/7958600) [2]. These algorithms have low false-alarm rates and can effectively handle broad classes of code changes that might appear in code patch processes. In fact, based on our 2-year operation of Vanir, only 2.72% of signatures triggered  false alarms. This allows Vanir to efficiently find missing patches, even with code changes, while minimizing unnecessary alerts and manual review efforts.

Vanir's source-code-based approach also enables rapid scaling across any ecosystem. It can generate signatures for any source files written in supported languages. Vanir's signature generator automatically generates, tests, and refines these signatures, allowing users to quickly create signatures for new vulnerabilities in any ecosystem simply by providing source files with security patches.

Android’s successful use of Vanir highlights its efficiency compared to traditional patch verification methods. A single engineer used Vanir to generate signatures for over 150 vulnerabilities and verify missing security patches across its downstream branches – all within just five days.

## Vanir for Android

Currently Vanir supports C/C++ and Java targets and covers 95% of Android kernel and userspace CVEs with public security patches. Google Android Security team consistently incorporates the latest CVEs into Vanir’s coverage to provide a complete picture of the Android ecosystem’s patch adoption risk profile.

The Vanir signatures for Android vulnerabilities are published through the [Open Source Vulnerabilities (OSV)](https://osv.dev/) database. This allows Vanir users to seamlessly protect their codebases against latest Android vulnerabilities without any additional updates. Currently, there are over [2,000 Android vulnerabilities in OSV](https://osv.dev/list?q=&ecosystem=Android), and finishing scanning an entire Android source tree can take 10-20 minutes with a modern PC.

![](data:image/png;base64...)

## Flexible integration, adoption and expansion.

Vanir is developed not only as a standalone application but also as a Python library. Users who want to integrate automated patch verification processes with their continuous build or test chain may easily achieve it by wiring their build integration tool with Vanir scanner libraries. For instance, Vanir is integrated with a continuous testing pipeline in Google, ensuring all security patches are adopted in ever-evolving Android codebase and their first-party downstream branches.

Vanir is also fully open-sourced, and under BSD-3 license. As Vanir is not fundamentally limited to the Android ecosystem, you may easily adopt Vanir for the ecosystem that you want to protect by making relatively small modifications in Vanir. In addition, since Vanir’s underlying algorithm is not limited to security patch validation, you may modify the source and use it for different purposes such as licensed code detection or code clone detection. The Android Security team welcomes your contributions to Vanir for any direction that may expand its capability and scope. You can also contribute to Vanir by providing vulnerability data with Vanir signatures to OSV.

# Vanir Results

Since early last year, we have partnered with several Android OEMs to test the tool’s effectiveness. Internally we have been able to integrate the tool into our build system continuously testing against over 1,300 vulnerabilities. Currently Vanir covers 95% of all Android, Wear, and Pixel vulnerabilities with public fixes across Android Kernel and Userspace. It has a 97% accuracy rate, which has saved our internal teams over 500 hours to date in patch fix time.

# Next steps

We are happy to announce that Vanir is now available for public use. Vanir is not technically limited to Android, a...