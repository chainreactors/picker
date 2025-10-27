---
title: Cobalt Strike 4.8: (System) Call Me Maybe
url: https://www.cobaltstrike.com/blog/cobalt-strike-4-8-system-call-me-maybe/
source: Cobalt Strike Research and Development
date: 2023-03-08
fetch_date: 2025-10-04T08:57:09.185654
---

# Cobalt Strike 4.8: (System) Call Me Maybe

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

[Home](https://www.cobaltstrike.com/) » [Blog](/blog/) » Cobalt Strike 4.8: (System) Call Me Maybe

# Cobalt Strike 4.8: (System) Call Me Maybe

Cobalt Strike 4.8 is now available. This release sees support for system calls, options to specify payload guardrails, a new token store, and more.

We had originally planned to get this release out late in 2022 but progress was stymied due to the [4.7.1](https://www.cobaltstrike.com/blog/out-of-band-update-cobalt-strike-4-7-1/) and [4.7.2](https://www.cobaltstrike.com/blog/out-of-band-update-cobalt-strike-4-7-2/) patch releases that we had to put out to fix vulnerabilities that were reported in the 4.7 release. We spent a few development cycles performing a security review of the code and working on some technical debt, and then it was the holiday season. It’s here now though, and better late than never!

Before getting into the details of this release, I just wanted to mention that you should now start to see much more content from us to supplement main product releases. [William Burgess recently released his first blog post since joining the Cobalt Strike team](https://www.cobaltstrike.com/blog/behind-the-mask-spoofing-call-stacks-dynamically-with-timers/) and he will be playing a key role in providing technical guidance on the future direction of the product. We have more blog posts and tooling coming over the next few weeks and months, starting with a series on UDRL development (the first of which should drop next week). Coming later in the year are some **huge** changes to Cobalt Strike itself. More details on that will come in a follow-up blog post soon. We know that our users are struggling with evasion and have reported other pain points. As I mentioned in my [roadmap update](https://www.cobaltstrike.com/blog/cobalt-strike-roadmap-update/) last year, we have been aggressively building out our R&D team and while it’s taken a while to do that and get all of our ducks in a row, you’ll now really start to see the benefits of those behind-the-scenes changes. Now, back to the 4.8 release.

### System Calls Support

This release sees the addition of support for direct and indirect system calls. We have added support for a number of system calls, specifically:

* *CloseHandle*
* *CreateFileMapping*
* *CreateRemoteThread*
* *CreateThread*
* *GetThreadContext*
* *MapViewOfFile*
* *OpenProcess*
* *OpenThread*
* *ResumeThread*
* *SetThreadContext*
* *UnmapViewOfFile*
* *VirtualAlloc*
* *VirtualAllocEx*
* *VirtualFree*
* *VirtualProtect*
* *VirtualProtectEx*
* *VirtualQuery*

The stageless Beacon payload generation dialog has been updated to allow you to specify the system call method to be used at execution time. The available options are:

**None**: Use the standard Windows API function
**Direct**: Use the Nt\* version of the function
**Indirect**: Jump to the appropriate instruction within the Nt\* version of the function

![](https://www.cobaltstrike.com/app/uploads/2023/07/image-2.png)

It is important to note that there are some commands and workflows that inject or spawn a new Beacon that do not allow you to set the initial system call method. Those commands/workflows are:

* *elevate*
* *inject*
* *jump*
* *spawn*
* *spawnas*
* *spawnu*
* *teamserver responding to a stageless payload request*
* *teamserver responding to an External C2 payload request*

The **stage.syscall\_method** in the MalleableC2 profile controls the method used at execution time, and you can use the **syscall-method [method]** command to modify the method that will be used for subsequent commands. Additionally, **syscall-method** without any arguments will query and return the current method.

System call support is something that we intend to continue to update and enhance in future releases. Your feedback on this is welcomed.

### Generate Payloads With Built-In Guardrails

Support has been added for payload guardrails, which can be set at the listener level and then, if required, overridden when generating a payload.

Guardrails can be set based on the following criteria:

* **IP address**: This can be a single IP address or a range using a wildcard to replace the rightmost octet(s). For example, 123.123.123.123, 123.123.123.\*, 123.123.\*.\* and 123.\*.\*.\* are all valid inputs. 123.\*.123.\* is not.
* **Username**: This can be a specific username, or you can prefix/suffix a wildcard (i.e. \*user or user\*). The username field is case insensitive.
* **Server name**: Again, this can be a specific server name, or you can prefix/suffix a wildcard (i.e. \*server or server\*). The server name field is case insensitive.
* **Domain**: As with username and server name, the domain field can either be a specific domain or you can prefix/suffix a wildcard (i.e. \*domain or domain\*). The domain name field is also case insensitive.

The listener dialog has a new “Guardrails” option at the bottom of the screen that allow...