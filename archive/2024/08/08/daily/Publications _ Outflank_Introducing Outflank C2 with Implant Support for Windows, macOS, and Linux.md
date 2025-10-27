---
title: Introducing Outflank C2 with Implant Support for Windows, macOS, and Linux
url: https://www.outflank.nl/blog/2024/08/07/introducing-outflank-c2-with-implant-support-for-windows-macos-and-linux/
source: Publications | Outflank
date: 2024-08-08
fetch_date: 2025-10-06T18:04:14.061948
---

# Introducing Outflank C2 with Implant Support for Windows, macOS, and Linux

[Skip to the content](#content)

[logo](https://www.outflank.nl)
Experts in red teaming

* [Red Team Tools](/products/)
  + [Outflank Security Tooling](/products/outflank-security-tooling/)
    - [Outflank C2](https://www.outflank.nl/products/outflank-security-tooling/outflank-c2/)
    - [Payload Generator](/products/outflank-security-tooling/pe-payload-generator/)
    - [Tooling](/products/outflank-security-tooling/ost-tool-list/)
    - [Tradecraft](/products/outflank-security-tooling/tradecraft/)
    - [Demo Videos](/videos/ost-demo-videos/)
  + [Cobalt Strike](/products/cobalt-strike/)
  + [Red Team Bundle](/datasheets/red-team-bundle/)
  + [Advanced Red Team Bundle](/datasheets/advanced-red-team-bundle/)
* [Red Team Services](/services/red-teaming/)
* Blog & Resources
  + [Outflank Blog](/blog/)
  + [Community](/products/outflank-security-tooling/ost-community/)
  + [Datasheets](/datasheets/)
  + [OST Demo Videos](/videos/ost-demo-videos/)
  + [OST Releases](/services/outflank-security-tooling/releases/)
  + [Upcoming Events](https://www.outflank.nl/upcoming-events/)
* [About Us](/company/)
  + [Our Company](/company/)
  + [OST Testimonials](/company/outflank-security-tooling-testimonials/)
  + [Contact Us](/contact/)
* [Schedule a Demo](/demo-request/)
* [REQUEST QUOTEREQUEST QUOTE](/request-a-quote/)

# Publications

# [Introducing Outflank C2 with Implant Support for Windows, macOS, and Linux](https://www.outflank.nl/blog/2024/08/07/introducing-outflank-c2-with-implant-support-for-windows-macos-and-linux/ "Introducing Outflank C2 with Implant Support for Windows, macOS, and Linux")

[Marc Smeets](https://www.outflank.nl/blog/author/marc/ "Posts by Marc Smeets")
 |
August 7, 2024

We have rebranded our commercial C2 framework from Stage1 to Outflank C2 to reflect its continued growth and functionality, including native implant support for Windows, macOS, and Linux.

## The Evolution of Stage1

Since the origin of our red team tooling offering, [Outflank Security Tooling (OST)](https://www.outflank.nl/products/outflank-security-tooling/), Stage1 C2 has been a core component. [Stage1](https://www.outflank.nl/videos/stage-1/) began as a minimal framework, with its sole focus being an initial access implant with some nifty OPSEC and C2 characteristics. It was ideal for initial reconnaissance, modifying C2 channels if needed, and OPSEC safe techniques for loading another C2 framework once you required stage-2 capabilities.

As more red teams adopted OST, Stage1 quickly proved to be an unexpectedly popular framework, with users providing consistently positive feedback and requests for more features. Subsequently, we began to slowly add cool new functionality, including proxying, support for BOFs, and automation using Python, just to name a few.

While Stage1 was now serving its primary purpose and more, we found that we didn’t want to stop there. One of the top requests from our OST customers — which included our team in our own red team operations — was to add support for macOS and Linux platforms. As we began work on this upgrade and contemplated other developments down the road, we decided that Stage1 had outgrown its name.

So, we’re excited to announce **two new implants for macOS and Linux** and a rebranded C2 framework, **Outflank C2**!

![](https://www.outflank.nl/wp-content/uploads/2024/08/15.gif)

*Figure 1. Creating an Outflank C2 macOS implant and dylib loader to sideload [Gimp](https://www.gimp.org/)*.

## New Features in Outflank C2

This release has a slew of new features for the new macOS and Linux implants, as well as enhancements for the existing Windows implant. Here are the highlights:

* **Native Implants:** Tailored for each OS, both new implants are written in C/C++/ASM.
* **Dynamic Execution:** Linux implants support ELF Beacon Object Files (BOF) and macOS implants can execute inline JXA.
* **Network Tunneling:** All three implants include a SOCKS proxy and portforward / rportforward commands.
* **C2 Traffic:** Both new implants support HTTP(S) and TCP comms.
* **Implant Linking**: P2P implant linking works between all three implants. P2P is supported between any OC2 implants – Linux/macOS, Linux/Windows, or macOS/Windows!
* **Guardrails:** All three implants support debugger detection, hostname keying, and SSL pinning.
* **Payload Formats:** Payload execution is available in multiple formats, including a shared library, standalone executables, and other payload formats for all three platforms.
* **Evasion:**Months of R&D have enabled many OPSEC features from Windows to be carried to these new platforms. Continuous [EDR research](https://www.outflank.nl/blog/2024/06/03/edr-internals-macos-linux/) ensures users have state-of-the-art macOS and Linux tools.

![](https://www.outflank.nl/wp-content/uploads/2024/08/11.gif)

*Figure 2. Creating an Outflank C2 P2P Linux implant and linking it with an existing Windows implant.*

## Emphasizing a Multi-Tool Mindset

OST was created because we strongly believe modern red teams need a broad toolset to be effective in modern operations, not just a single C2. Outflank C2 strongly supports this ideal in several ways. Since Outflank C2 is part of the bigger OST toolset, it can both leverage the awesome functionality of other tools like Builder and Payload Generator, as well as rely on the years of research on EDR evasion techniques.

Increasingly, more red teams are opting to use multiple command and control tools in their operations to attain their objectives. We have been pleased that Stage1 served a unique purpose that complemented other C2 frameworks. We’re confident this trend will continue with Outflank C2 and we are particularly proud to offer the versatility that comes with providing native support for these three platforms.

The official release of Outflank C2 will take place August 15th and will be reflected in the [release timeline](https://www.outflank.nl/services/outflank-security-tooling/releases/). We will have more information to share over the coming period and you’ll see updates to the site to reflect Stage1’s transition to Outflank C2. In the mean time, you can consider scheduling an expert-led demo to learn more about the diverse offerings in OST.

[Schedule a Demo](https://outflank.nl/demo-request/)

Categories: [Uncategorized](https://www.outflank.nl/blog/category/uncategorized/)

## Post navigation

[← EDR Internals for macOS and Linux](https://www.outflank.nl/blog/2024/06/03/edr-internals-macos-linux/)

[Will the real #GrimResource please stand up? – Abusing the MSC file format →](https://www.outflank.nl/blog/2024/08/13/will-the-real-grimresource-please-stand-up-abusing-the-msc-file-format/)

## Need help right away?Call our emergency number

+31 20 2618996

Or send us an [email](/cdn-cgi/l/email-protection#b8d1d6ded7f8d7cdccded4d9d6d396d6d487cbcddad2dddbcc85e3f1d6dbd1dcddd6cc989598cfcfcf96d7cdccded4d9d6d396d6d4e5) and we’ll get back to you as soon as possible

[logo](/)

Experts in red teaming

#### Services

* [Red teaming](/services/red-teaming/)

#### Company

[Meet the Team](/company)
[OST Testimonials](/company/outflank-security-tooling-testimonials)

#### Publications

* [Training Specialist Models: Automating Malware Development](https://www.outflank.nl/blog/2025/08/07/training-specialist-models/)
* [Accelerating Offensive R&D with Large Language Models](https://www.outflank.nl/blog/2025/07/29/accelerating-offensive-research-with-llm/)
* [Async BOFs – “Wake Me Up, Before You Go Go”](https://www.outflank.nl/blog/2025/07/16/async-bofs-wake-me-up-before-you-go-go/)

#### Connect with us

[[email protected]](/cdn-cgi/l/email-protection#90f9fef6ffd0ffe5e4f6fcf1fefbbefefc)

[Privacy Policy](https://www.fortra.com/privacy-policy)
[Cookie Policy](https://www.fortra.com/cookie-policy)
[Terms of Service](https://www.fortra.com/terms-of-service)
Copyright © Fortra, LLC and its group of companies. Fortra®, the Fortra® logos, and other identified marks are proprietary tra...