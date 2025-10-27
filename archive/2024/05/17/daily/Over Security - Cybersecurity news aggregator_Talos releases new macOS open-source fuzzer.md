---
title: Talos releases new macOS open-source fuzzer
url: https://blog.talosintelligence.com/talos-releases-new-macos-fuzzer/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-17
fetch_date: 2025-10-06T17:20:07.740451
---

# Talos releases new macOS open-source fuzzer

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2024/05/VulnDeepDive.png)

# Talos releases new macOS open-source fuzzer

By
[Aleksandar Nikolic](https://blog.talosintelligence.com/author/aleksandar/)

Thursday, May 16, 2024 08:00

[Vulnerability Deep Dive](/category/vulnerability-deep-dive/)

* Cisco Talos has developed a fuzzer that enables us to test macOS software on commodity hardware.
* Fuzzer utilizes a snapshot-based fuzzing approach and is based on WhatTheFuzz framework.
* Support for VM state extraction was implemented and WhatTheFuzz was extended to support the loading of VMWare virtual machine snapshots.
* Additional tools support symbolizing and code coverage analysis of fuzzing traces.

#### Table of Contents

[Previously in snapshot fuzzing](#previously-in-snapshot-fuzzing)

[Snapshot fuzzing building blocks](#snapshot-fuzzing-building-blocks)

[Debugging](#debugging)

[Snapshot acquisition](#snapshoty-acquisition)

[Snapshot loading into WTF](#snapshot-loading-into-wtf)

[Catching crashes](#catching-crashes)

[Fuzzing harness and fixups](#fuzzing-harness-and-fixups)

[Coverage](#snapshoty-acquisition)

Finding novel and unique vulnerabilities often requires the development of unique tools that are best suited for the task. Platforms and hardware that target software run on usually dictate tools and techniques that can be used.  This is especially true for parts of the macOS operating system and kernel due to its close-sourced nature and lack of tools that support advanced debugging, introspection or instrumentation.

Compared to fuzzing for software vulnerabilities on Linux, where most of the code is open-source, targeting anything on macOS presents a few difficulties. Things are closed-source, so we can’t use compile-time instrumentation. While Dynamic Binary instrumentation tools like Dynamorio and TinyInst work on macOS, they cannot be used to instrument kernel components.

There are also hardware considerations – with few exceptions, macOS only runs on Apple hardware. Yes, it can be virtualized, but that has its drawbacks. What this means in practice is that we cannot use our commodity off-the-shelf servers to test macOS code. And fuzzing on laptops isn’t exactly effective.

A while ago, we embarked upon a project that would alleviate most of these issues, and we are making the [code available](https://github.com/Cisco-Talos/snap_wtf_macos) today.

Using a snapshot-based approach enables us to target closed-source code without custom harnesses precisely. Researchers can obtain full instrumentation and code coverage by executing tests in an emulator, which enables us to perform tests on our existing hardware. While this approach is limited to testing macOS running on Intel hardware, most of the code is still shared between Intel and ARM versions.

# Previously in snapshot fuzzing

The simplest way to fuzz a target application is to run it in a loop while changing the inputs. The obvious downside is that you lose time on application initialization, boilerplate code and less CPU time spent on executing the relevant part of the code.

The approach in snapshot-based fuzzing is to define a point in process execution to inject the fuzzing test case (at an entry point of an important function). Then, you interrupt the program at a given point (via breakpoint or other means) and take a snapshot. The snapshot includes all of the virtual memory being used, and the CPU or other process state required to restore and resume process execution. Then, you insert the fuzzing test case by modifying the memory and resume execution.

When the execution reaches a predefined sink (end of function, error state, etc.) you stop the program, discard and replace the state with the previously saved one.

The benefit of this is that you only pay the penalty of restoring the process to its previous state, you don’t create it from scratch. Additionally, suppose you can rely on OS or CPU mechanisms such as CopyOnWrite, page-dirty tracking and on-demand paging. In that case, the operation of restoring the process can be very fast and have little impact on overall fuzzing speed.

Cory Duplantis championed our previous attempts at utilizing snapshot-based fuzzing in his work on [Barbervisor](https://blog.talosintelligence.com/barbervisor/), abare metal hypervisor developed to support high-performance snapshot fuzzing.

It involved acquiring a snapshot of a full (Virtual Box-based) VM and then transplanting it into Barbervisor where it could be executed. It relied on Intel CPU features to enable high performance by only restoring modified memory pages.

While this showed great potential and gave us a glimpse into the potential utility of snapshot-based fuzzing, it had a few downsides. A similar approach, built on top of KVM and with numerous improvements, was implemented in [Snapchange](https://aws.amazon.com/blogs/opensource/announcing-snapchange-an-open-source-kvm-backed-snapshot-fuzzing-framework/) and released by AWS Labs.

# Snapshot fuzzing building blocks

Around the time Talos published Barbervisor, Axel Souchet published his [WTF](https://github.com/0vercl0k/wtf) project, which takes a different approach. It trades performance to have a clean development environment by relying on existing tooling. It uses Hyper-V to run virtual machines that are to be snapshotted, then uses kd (Windows kernel debugger) to perform the snapshot, which saves the state in a Windows memory dump file format, which is optimized for loading. WTF is written in C++, which means it can benefit from the plethora of existing support libraries such as custom mutators or fuzz generators.

It has multiple possible execution backends, but the most fully featured one is based on Bochs, an x86 emulator, which provides a complete instrumentation framework. The user will likely see a dip in performance – it’...