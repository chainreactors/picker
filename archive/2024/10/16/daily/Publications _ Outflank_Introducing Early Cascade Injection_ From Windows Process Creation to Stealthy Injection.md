---
title: Introducing Early Cascade Injection: From Windows Process Creation to Stealthy Injection
url: https://www.outflank.nl/blog/2024/10/15/introducing-early-cascade-injection-from-windows-process-creation-to-stealthy-injection/
source: Publications | Outflank
date: 2024-10-16
fetch_date: 2025-10-06T18:52:48.516605
---

# Introducing Early Cascade Injection: From Windows Process Creation to Stealthy Injection

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

# [Introducing Early Cascade Injection: From Windows Process Creation to Stealthy Injection](https://www.outflank.nl/blog/2024/10/15/introducing-early-cascade-injection-from-windows-process-creation-to-stealthy-injection/ "Introducing Early Cascade Injection: From Windows Process Creation to Stealthy Injection")

[Dima van de Wouw](https://www.outflank.nl/blog/author/dima/ "Posts by Dima van de Wouw")
 |
October 15, 2024

*By [Guido Miggelenbrink](https://www.linkedin.com/in/guido-miggelenbrink-63aa0a166/) at Outflank*

## Introduction

In this blog post we introduce a novel process injection technique named Early Cascade Injection, explore Windows process creation, and identify how several Endpoint Detection and Response systems (EDRs) initialize their in-process detection capabilities. This new Early Cascade Injection technique targets the user-mode part of process creation and combines elements of the well-known Early Bird APC Injection technique with the recently published EDR-Preloading technique [by Marcus Hutchins](https://www.malwaretech.com/2024/02/bypassing-edrs-with-edr-preload.html) [[1]](https://www.malwaretech.com/2024/02/bypassing-edrs-with-edr-preload.html). Unlike Early Bird APC Injection, this new technique avoids queuing cross-process Asynchronous Procedure Calls (APCs), while having minimal remote process interaction. This makes Early Cascade Injection a stealthy process injection technique that is effective against top tier EDRs while avoiding detection.

To provide insights into Early Cascade Injection’s internals, this blog also presents a timeline of the user-mode process creation flow. This overview illustrates how Early Cascade Injection operates and pinpoints the exact moment at which it intervenes in process creation. Furthermore, we compare that to the initialization timing of EDR user-mode detection measures.

Now, let’s dive into the details of Windows process creation, Early Bird APC Injection, and EDR-Preloading. Once we have a solid understanding of these topics, we can proceed to explore Early Cascade Injection.

## Understanding Windows Process Creation

### Process creation APIs

In Windows there are various APIs to create a process, such as `CreateProcess`, `CreateProcessAsUser`, and `CreateProcessWithLogon`, as shown in figure 1. Ultimately, all these functions invoke the NAPI `NtCreateUserProcess` in `ntdll.dll`. This function is responsible for initiating process creation by switching control to the kernel, where the equally named function `NtCreateUserProcess` is executed.

Each of these functions include the `dwCreationFlags` parameter, which controls how the process is created. In this post, we’ll encounter the `CREATE_SUSPENDED` flag, which instructs the kernel to create the new process’s initial thread in a suspended state [[2]](https://learn.microsoft.com/en-us/windows/win32/procthread/process-creation-flags). The thread remains suspended until the `ResumeThread` function is called.

Obviously, these functions also have a parameter specifying the path to the application’s image file for which a process is to be created. Refer to the MSDN for the other parameters and flags of these APIs [[2]](https://learn.microsoft.com/en-us/windows/win32/procthread/process-creation-flags).

[![](https://www.outflank.nl/wp-content/uploads/2024/10/CreateProcessAPIs-1024x430.png)](https://www.outflank.nl/wp-content/uploads/2024/10/CreateProcessAPIs.png)

*Figure 1: Process creation functions (Source: Windows Internals, Part 1)*

### Kernel-mode and user-mode process creation

Process creation has two parts: kernel-mode and user-mode. It begins with the kernel-mode part, initiated by `NtCreateUserProcess`. Once the process’s context and environment are created in kernel-mode, the initial thread of the process completes process creation in user-mode.

The kernel-mode part is responsible for opening the image file of the specified application and mapping it into memory. It then creates process-specific and thread-specific objects, maps the native library `ntdll.dll` into the process, followed by the creation of the process’s initial thread. If the `CREATE_SUSPENDED` flag is specified, this thread is created in suspended state, waiting to be resumed before control returns to user-mode for the remainder of the process creation.

The module `ntdll.dll` is the first DLL loaded into a process and it is the only DLL loaded in kernel-mode, all other modules are loaded in user-mode. Further, `ntdll.dll` includes the exported function `LdrInitializeThunk`, which handles the user-mode part of process creation before the application’s main entry point runs. This function is also known as the image loader and the functions related to it in `ntdll.dll` are prefixed with `Ldr`.

Returning to the newly created thread: upon resumption of this suspended thread, it starts executing `LdrInitializeThunk`, the user-mode part of process creation. After, the new process is fully initialized and ready to run the application. The initial thread then begins executing the application’s main entry point.

> Note that using the `CREATE_SUSPENDED` flag pauses process creation just before the initial thread switches to user-mode to run `LdrInitializeThunk`. This is particularly interesting because **user-mode malware can interfere with process creation at this point**. Therefore, let’s take a closer look at what happens inside `LdrInitializeThunk`.

### User-mode process creation: `LdrInitializeThunk`

`LdrInitializeThunk` is the first function executed in user-mode, marking the initial point where malware and EDRs can intervene in a process. We will later explore how techniques such as Early Bird APC Injection, EDR-Preloading and Early Cascade Injection interact with `LdrInitializeThunk`. For now, let’s delve into the details of this function.

`LdrInitializeThunk` is a complex function responsible for the user-mode part of process creation. It handles numerous process initialisation tasks, which are listed and briefly described in the *Windows Internals, Part 1* book. However, the book does not cover which subordinate functions within `LdrInitializeThunk` are responsible for these tasks. Hence, to gain a deeper understanding of `LdrInitializeThunk` and its subordinate functions, we analysed it using x64dbg and IDA Pro.

Based on this analysis, we created a call graph that outlines the sequence of events in the user-mode part of process creation. This timeline includes the functions relevant to this post and thus omits some tasks and associated functions of `LdrInitializeThunk`. Additionally, please note that this call graph reflects ...