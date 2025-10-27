---
title: Behind the Mask: Spoofing Call Stacks Dynamically with Timers
url: https://www.cobaltstrike.com/blog/behind-the-mask-spoofing-call-stacks-dynamically-with-timers/
source: Cobalt Strike Research and Development
date: 2023-02-14
fetch_date: 2025-10-04T06:32:04.332828
---

# Behind the Mask: Spoofing Call Stacks Dynamically with Timers

[Skip to content](#content)

[![Fortra](https://static.fortra.com/fortra-global-assets/fortra-logo-full.svg)
![fortra mobile logo](https://www.cobaltstrike.com/app/themes/helpsystems/img/fortra-delta-white.svg)

![Cobalt Strike](https://www.cobaltstrike.com/app/uploads/2023/06/fta-cobalt-strike-light-1.svg)](https://www.cobaltstrike.com/)

* [Fortra.com](https://www.fortra.com/?utm_source=coresecurity.com&utm_medium=referral&utm_campaign=fortra_secondarynav_link "Fortra.com")
* [Blog](/blog "Blog")
* [Download](https://download.cobaltstrike.com/download "Download")
* [Contact Us](/contact-us "Contact Us")

## Main Navigation

* [REQUEST PRICING](/product/quote-request "REQUEST PRICING")
* [Product](/product "Product")
  + Features
    - [Beacon](https://www.cobaltstrike.com/product/features/beacon "Beacon")
    - [Malleable C2](https://www.cobaltstrike.com/product/features/malleable-c2 "Malleable C2")
    - [Interoperability](https://www.cobaltstrike.com/product/features/interoperability "Interoperability")
    - [Community](https://www.cobaltstrike.com/product/features/community "Community")
    - [Flexibility](https://www.cobaltstrike.com/product/features/flexibility "Flexibility")
    - [UDRL](https://www.cobaltstrike.com/product/features/user-defined-reflective-loader "UDRL")
    - [View More Features >](/product/features/ "View More Features >")
  + Interoperability
    - [Core Impact](https://www.cobaltstrike.com/product/core-impact "Core Impact")
    - [Outflank Security Tooling](https://www.cobaltstrike.com/product/outflank-security-tooling "Outflank Security Tooling")
  + Bundles
    - [Cobalt Strike + Core Impact](/resources/datasheets/advanced-bundle/ "Cobalt Strike + Core Impact")
    - [Cobalt Strike + Outflank Security Tooling](/resources/datasheets/red-team-bundle/ "Cobalt Strike + Outflank Security Tooling")
    - [Cobalt Strike, Core Impact, Outflank Security Tooling](/resources/datasheets/advanced-red-team-bundle/ "Cobalt Strike, Core Impact, Outflank Security Tooling")
    - [View All Product Bundles >](/product/bundles/ "View All Product Bundles >")
* [Industry](https://www.cobaltstrike.com/industry "Industry")
  + [Finance](https://www.cobaltstrike.com/industry/finance "Finance")
  + [Healthcare](https://www.cobaltstrike.com/industry/healthcare "Healthcare")
  + [Government & Public Sector](https://www.cobaltstrike.com/industry/government "Government & Public Sector ")
* [Support](/support "Support")
  + [Training](https://www.cobaltstrike.com/support/training "Training")
  + [User Manuals](https://www.cobaltstrike.com/support/user-manuals "User Manuals")
  + [Community Kit](https://cobalt-strike.github.io/community_kit/ "Community Kit")
* [Resources](/resources "Resources")
  + [Blog](/blog "Blog")
  + [Screenshots](https://www.cobaltstrike.com/resources/screenshots "Screenshots")
  + [Datasheets](/resources/type-datasheet "Datasheets")
  + [Videos](/resources/type-video "Videos")
  + [Events and Webinars](/resources/type-upcoming-event "Events and Webinars")
* [Search](#collapseSearch)

Search for:

[Home](https://www.cobaltstrike.com/) » [Blog](/blog/) » Behind the Mask: Spoofing Call Stacks Dynamically with Timers

# Behind the Mask: Spoofing Call Stacks Dynamically with Timers

This blog introduces a PoC technique for spoofing call stacks using timers. Prior to our implant sleeping, we can queue up timers to overwrite its call stack with a fake one and then restore the original before resuming execution. Hence, in the same way we can mask memory belonging to our implant during sleep, we can also mask the call stack of our main thread. Furthermore, this approach avoids having to deal with the complexities of X64 stack unwinding, which is typical of other call stack spoofing approaches.

### The Call Stack Problem

The core memory evasion problem from an attacker’s perspective is that implants typically operate from injected code (ignoring any module hollowing approaches). Therefore, one of the pillars of modern detection is to monitor for the creation of threads which belong to unbacked (or ‘floating’) memory. This [blog](https://www.elastic.co/security-labs/get-injectedthreadex-detection-thread-creation-trampolines) by Elastic is a good approximation to the state of the art in terms of anomalous thread detection from an EDR perspective.

However, another implication of this problem for attackers is that all the implants’ API calls will also originate from unbacked memory. By examining call stacks either at the time of a specific API invocation, or by proactively inspecting running threads (i.e. ones which are sleeping), suspicious call stacks can be identified via return addresses to unbacked memory.

This is one detection area which historically has not received a huge amount of focus/research in modern EDR stacks (in my experience). However, this is starting to change with the release of open-source tools such as [Hunt-Sleeping-Beacons](https://github.com/thefLink/Hunt-Sleeping-Beacons), which will proactively inspect “sleeping” threads to find call stacks with unbacked regions. This demonstrably provides a high confidence signal of suspicious activity; hence it is valuable to EDRs and something attackers need to seriously consider in their evasion TTPs.

### Call Stack Inspection at Rest

The first problem to solve from an attacker’s perspective is how to manipulate the call stack of a sleeping thread so that it can bypass this type of inspection. This could be performed by the actual thread itself or via some external mechanism (APCs etc.).

Typically, this is referred to as “spoofing at rest” (h/t to Kyle Avery here for this terminology in his [excellent blog](https://www.blackhillsinfosec.com/avoiding-memory-scanners/) on avoiding memory scanners). The first public attempt to solve this problem is mgeeky’s [ThreadStackSpoofer](https://github.com/mgeeky/ThreadStackSpoofer), which overwrites the last return address on the stack.

As a note, the opposite way to approach this problem is by having no thread or call stack present at all, à la [DeathSleep.](https://github.com/janoglezcampos/DeathSleep) The downside of this technique is the potential for the repeated creation of unbacked threads, (depends on the exact implementation), which is a much greater evil in modern environments. However, future use of [Hardware Stack Protection](https://www.elastic.co/security-labs/finding-truth-in-the-shadows) by EDR vendors may make this type of approach inevitable.

### Call Stack Inspection During Execution – User Mode

The second problem is call stack inspection during execution*,* which could either be implemented in user mode or kernel mode. In terms of user mode implementation, this would typically involve hooking a commonly abused function and walking the stack to see where the call originated. If we find unbacked memory, it is highly likely to be suspicious. An obvious example of this is injected shellcode stagers calling WinInet functions. [MalMemDetect](https://github.com/waldo-irc/MalMemDetect) is a good example of an open-source project that demonstrates this detection technique.

For these scenarios, techniques such as [RET address spoofing](https://www.unknowncheats.me/forum/anti-cheat-bypass/268039-x64-return-address-spoofing-source-explanation.html) are normally sufficient to remove any evidence of unbacked addresses from the call stack. At a high level, this involves inserting a small assembly harness around the target function which will manually replace the last return address on the stack and redirect the target function to return to a trampoline gadget (e.g. jmp rbx).

Additionally, there is [SilentMoonWalk](https://klezvirus.github.io/RedTeaming/AV_Evasion/StackSpoofing/) which uses a clever de-syncing approach (essentially a ROP gadget built on X64 stack unwinding codes). This can dynamically hide the origin of a function call and will similarly bypass these basic detection heuristics. Most importantly to an ...