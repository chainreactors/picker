---
title: Memory Forensics R&D Illustrated: Detecting Hidden Windows Services
url: https://volatility-labs.blogspot.com/2023/03/memory-forensics-r-d-illustrated-detecting-hidden-windows-services.html
source: Volatility Labs
date: 2023-03-23
fetch_date: 2025-10-04T10:25:05.102725
---

# Memory Forensics R&D Illustrated: Detecting Hidden Windows Services

# [[Archive of Volatility Labs]](https://volatility-labs.blogspot.com/)

**This site is an archive of the Volatility Labs blog. The blog has moved to <https://volatilityfoundation.org/volatility-blog/>**

## Wednesday, March 22, 2023

### Memory Forensics R&D Illustrated: Detecting Hidden Windows Services

*As mentioned in a [recent blog post](https://volatility-labs.blogspot.com/2023/06/malware-and-memory-forensics-training-headed-to-amsterdam-in-october-2023.html), our team is once again offering in-person training, and we have substantially updated our course for this occasion. Over the next several weeks, we will be publishing a series of blog posts, offering a sneak peek at the types of analysis incorporated into the updated Malware & Memory Forensics training course.*

### Introduction

To begin the series, this post discusses a new detection technique for hidden services on Windows 7 through 11. Since not all readers will be familiar with hidden services and the danger they pose on live systems, we will start with some brief background. We will then walk through how *services.exe* stores service information, and how we can recover it in an orderly manner. This will lead to how we developed two new Volatility 3 plugins to help automate detection of hidden services.

The power of these plugins will be showcased against the powerful [GhostEmperor APT rootkit](https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/) that was discovered in the wild by researchers at Kaspersky. GhostEmperor employs a kernel mode rootkit and a userland DLL to maintain persistence and control the victim system. This DLL operates as a service that is hidden from live analysis and DFIR triage tools, and it interacts directly with the rootkit driver in kernel memory. As will be demonstrated, by automatically detecting the hidden service of GhostEmperor through memory analysis, we can quickly find the rest of its components, including those hidden on the live system.

### Services Background

Services are a powerful feature of Windows that allow malware to run in one of three possible forms. The first allows malware to register a DLL that will be loaded into a shared *svchost.exe* process, hiding it amongst other DLLs loaded inside the same process, as well as the many *svchost.exe* instances that run on a normal system. The second form allows malware to run as its own process. The third, and most dangerous, form is when malware creates a service to load a kernel driver (rootkit).

When services are created and started using standard methods, a few artifacts are left behind for investigators to find. The first is a set of registry keys and values under *CurrentControlSet\Services\<service name>*. The second is the service’s entry within a linked list maintained by *services.exe*. This list is enumerated when system APIs, such as *EnumServiceStatus{A,W,Ex}*, and tools, such as *sc.exe query*, are used to enumerate services on the running system.

Given the power of services, malware often abuses the ability to create or hijack services for its own purposes. This leads to the inspection of services on a running system by endpoint detection and response solutions (EDRs) and threat hunting teams to look for any suspicious signs. To avoid detection while keeping a service active, malware has historically targeted both sources of artifacts—the registry keys and the *services.exe* list—with registry keys being targeted in two ways: deleting or hiding them.

In the first approach, malware will delete its registry keys while running, and then rewrite them before system shutdown or reboot. This has a major disadvantage though, as sudden system crashes or service stops prevent the malware from re-registering its persistence.

This deficiency led to the current approach malware takes, including by GhostEmperor, which is to simply hide its keys from the running system. The following screenshot shows Kaspersky’s report on the malware's approach:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjfVSdit6mOWJfI22ZTewyRta0FJPd4Dp-u8xRN58q3vx4g6erKQEZzQQVgOKwM94vL1DmhHmF2vB2K5OvqrybDwF6s-hSzIU9CKZgaJMBVN-8FfhphHJCjZla1I_3Cx_k08i0saQIOA_i2SynsXaArwpAgec6XOuoS2zkON4VQ8Of6KLhAI1oWeD0fUg=w640-h203)](https://blogger.googleusercontent.com/img/a/AVvXsEjfVSdit6mOWJfI22ZTewyRta0FJPd4Dp-u8xRN58q3vx4g6erKQEZzQQVgOKwM94vL1DmhHmF2vB2K5OvqrybDwF6s-hSzIU9CKZgaJMBVN-8FfhphHJCjZla1I_3Cx_k08i0saQIOA_i2SynsXaArwpAgec6XOuoS2zkON4VQ8Of6KLhAI1oWeD0fUg)

As discussed in Kapersky's report, the *CmRegisterCallback* usage effectively allows the malware to hide its service’s keys from tools on the live system. Detecting this malicious callback is possible with Volatility’s *callbacks* plugin though, and there are also EDRs capable of enumerating callbacks from within kernel memory. To avoid these EDRs, some rootkits found during recent APT campaigns have implemented a completely new method of registry key hiding, known as *GetCellRoutine hijacking*, that we will cover in an upcoming post along with another new Volatility 3 plugin.

Beyond the registry, malware also wants to hide its malicious service from tools on the live system that query *services.exe* to enumerate running services. To accomplish this, malware will inject code into the *services.exe* process, and then unlink the malicious service of interest. This will effectively hide the service from live DFIR triage tools and built-in Windows commands. It's the detection of these unlinked services using new memory forensics capabilities that we cover further in this blog post.

|  |
| --- |
| *Note: Chapter 12 in [The Art of Memory Forensics](https://www.memoryanalysis.net/amf) is devoted to discussion of Windows services, ways malware abuses them, and several historical methods of detection. If you would like a complete treatment of the subject after reading this blog post, then we suggest reading this chapter.* |

### Detecting Unlinked Services

As mentioned, a wide variety of malware samples will unlink their malicious services for anti-forensics purposes. The following screenshot from the Kaspersky report on GhostEmperor describes this for the malware sample:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi-cGtfFtkSX5COu6s8qkt-Fzwa_glCPZ8QotewOsHKQ6wkQHy7XlUu6-C_QMuqTa9FLH6JctVOJxojA2p6jba3OB1Pwa-F0K4d1pLCU3ouH_6tE1k2NoGwASqyz0wCZ9SYvLZXqa19-1dIVS5y8KesYRGKGPZ-e5-bI8QF79XUUybWMlSxRdX3X-u9_Q=w640-h116)](https://blogger.googleusercontent.com/img/a/AVvXsEi-cGtfFtkSX5COu6s8qkt-Fzwa_glCPZ8QotewOsHKQ6wkQHy7XlUu6-C_QMuqTa9FLH6JctVOJxojA2p6jba3OB1Pwa-F0K4d1pLCU3ouH_6tE1k2NoGwASqyz0wCZ9SYvLZXqa19-1dIVS5y8KesYRGKGPZ-e5-bI8QF79XUUybWMlSxRdX3X-u9_Q)

In our analyzed memory sample, the name of the hidden service is “msdecode”, which is one of the possibilities listed in the report.

[The Art of Memory Forensics](https://www.memoryanalysis.net/amf) details one method for detecting unlinked services with Volatility. This method relies on scanning physical memory for services records, and then drawing a dot graph of how each service is linked to other services. This linkage is based on the previous and next pointers of the doubly linked list. During normal operations, each service record should have one service’s forward pointer referencing it, and one service’s backwards pointer referencing it. In the case of an unlinked service, the hidden service will have no services that reference it. The following image from *The Art of Memory Forensics* shows how this detection logic is applied to an unlinked *wscsvc* service:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiydLm4mcIRm0W3JBEaRKHNKIeCW0Y3UwKxqTmq9_xQEvPQA0K_9OgfE_c33a7c1IOWNcpd1Jps1oNqUom-2Lh-p4TstP9KOjZuFkAXtxqdmoLttjABc1z6dkVovzNKO8oNlzNHr4p2lyW9X3lkKqE36Ov_VQEqvSnNULqMhRmzRAxzAMGDUkztFbex2A=w640-h510)](https://blogger.googleusercontent.com/img/a/AVvXsEiydLm4mcIRm0W3JBEaRKHNKIeCW0Y3UwKxqTmq9_xQEvPQA0K_9OgfE_c33a7c1IOWNcpd1Jps1oNqUom-2Lh-p4TstP9KOjZuFkAXtxqdmoLttjABc1z6d...