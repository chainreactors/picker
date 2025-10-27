---
title: Revisiting the User-Defined Reflective Loader Part 1: Simplifying Development
url: https://www.cobaltstrike.com/blog/revisiting-the-udrl-part-1-simplifying-development/
source: Cobalt Strike Research and Development
date: 2023-03-16
fetch_date: 2025-10-04T09:45:53.060380
---

# Revisiting the User-Defined Reflective Loader Part 1: Simplifying Development

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

[Home](https://www.cobaltstrike.com/) » [Blog](/blog/) » Revisiting the User-Defined Reflective Loader Part 1: Simplifying Development

# Revisiting the User-Defined Reflective Loader Part 1: Simplifying Development

This blog post accompanies a new addition to the Arsenal Kit – The User-Defined Reflective Loader Visual Studio (UDRL-VS). Over the past few months, we have received a lot of feedback from our users that whilst the flexibility of the UDRL is great, there is not enough information/example code to get the most out of this feature. The intention of this kit is to lower the barrier to entry for developing and debugging custom reflective loaders. This post includes a walkthrough of creating a UDRL in Visual Studio that facilitates debugging, an introduction to UDRL-VS, and an overview of how to apply a UDRL to Beacon.

**Note:** *There are many people out there that prefer to use tools such as MingGW/GCC/LD/GDB etc. and we salute you. However, this post is intended for those of us that like the simplicity of Visual Studio and enjoy a GUI. To develop this template we used Visual Studio Community 2022.*

### Reflective Loading

Beacon is just a Dynamic Link Library (DLL). As a result, it needs to be “loaded” for us to work with it. There are many different ways to load a DLL in Windows, but [Reflective DLL Injection](https://github.com/stephenfewer/ReflectiveDLLInjection), first published by Stephen Fewer in 2008, provides the means to load a DLL completely in memory. There is a lot of information available regarding [PE files](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format), [reflective loading](https://securityintelligence.com/posts/defining-cobalt-strike-reflective-loader/), and even [improving upon Reflective DLL Injection](https://disman.tl/2015/01/30/an-improved-reflective-dll-injection-technique.html). Therefore, this post will not delve into this in much detail. Fundamentally though, a reflective loader must:

* Allocate some memory.
* Copy the target DLL into that memory allocation.
* Parse the target DLL’s imports/load the required modules/resolve function addresses.
* Rebase the DLL (fix the relocations).
* Locate the DLL’s Entry Point.
* Execute the Entry Point.

In Stephen Fewer’s original implementation, the code used to load the DLL into memory is compiled into the DLL and “[exported](https://learn.microsoft.com/en-us/cpp/build/exporting-from-a-dll?view=msvc-170)” as a function. This is how Beacon’s default reflective loader works; if you inspect Beacon’s exported functions you’ll find one called `ReflectiveLoader()` which is where the magic happens. The following screenshot shows Beacon’s Export Address Table (EAT) and its `ReflectiveLoader()` function in [CFF Explorer](https://ntcore.com/?page_id=388).

![](https://www.cobaltstrike.com/app/uploads/2023/07/cffexplorer_beacon-reflective-loader-function.png)

Figure 1. Beacon’s Export Address Table in CFF Explorer.

**Note:** *Typically, when a reflective loader is implemented in this fashion, a small shellcode stub is also written to the start of the PE file (over the DOS header) to ensure that execution is correctly directed to the right place (the `ReflectiveLoader()` function). This is what makes it position independent as it’s possible to simply write the reflective DLL to memory, start a thread and let it run.*

In 2017, an [analysis of the Double Pulsar User Mode Injector](https://blog.f-secure.com/doublepulsar-usermode-analysis-generic-reflective-dll-loader/) (*Double Pulsar*) leaked by Shadow Brokers showed an alternate approach to reflective loading ([archive link](https://web.archive.org/web/20171118102938/https%3A/www.countercept.com/our-thinking/doublepulsar-usermode-analysis-generic-reflective-dll-loader/)). *Double Pulsar* differed because it was not compiled into the DLL but prepended in front of it. This approach allowed it to reflectively load any DLL. Later in 2017, the [Shellcode Reflective DLL Injection](https://www.netspi.com/blog/technical/adversary-simulation/srdi-shellcode-reflective-dll-injection/) (sRDI) project was released which used a similar approach. [sRDI](https://github.com/monoxgas/sRDI) is able to take an arbitrary PE file and make it *position independent* which means it can also be used to load Beacon.

The following high-level diagram shows the different locations of the reflective loader between Stephen Fewer’s approach and *Double Pulsar*.

![](https://www.cobaltstrike.com/app/uploads/2023/07/diagram_different-locations-of-reflective-loader-1024x483.png)

Figure 2. The different locations of `ReflectiveLoader()`.

### The User-Defined Reflective Loader (UDRL)

The UDRL is an important aspect of Cobalt Strike’s evasion strategy. Cobalt Strike achieves “*evasion through flexibility*”, meaning we give you the tools you need to modify default behaviors and customize Beacon to your liking. This was something ...