---
title: The Windows Registry Adventure #7: Attack surface analysis
url: https://googleprojectzero.blogspot.com/2025/05/the-windows-registry-adventure-7-attack-surface.html
source: Project Zero
date: 2025-05-24
fetch_date: 2025-10-06T22:35:31.361525
---

# The Windows Registry Adventure #7: Attack surface analysis

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Friday, May 23, 2025

### The Windows Registry Adventure #7: Attack surface analysis

Posted by Mateusz Jurczyk, Google Project Zero

In the first three blog posts of this series, I sought to outline what the Windows Registry actually is, its role, history, and where to find further information about it. In the subsequent three posts, my goal was to describe in detail how this mechanism works internally – from the perspective of its clients (e.g., user-mode applications running on Windows), the regf format used to encode hives, and finally the kernel itself, which contains its canonical implementation. I believe all these elements are essential for painting a complete picture of this subsystem, and in a way, it shows my own approach to security research. One could say that going through this tedious process of getting to know the target unnecessarily lengthens the total research time, and to some extent, they would be right. On the other hand, I believe that to conduct complete research, it is equally important to answer the question of how certain things are implemented, as well as why they are implemented that way – and the latter part often requires a deeper dive into the subject. And since I have already spent the time reverse engineering and understanding various internal aspects of the registry, there are great reasons to share the information with the wider community. There is a lack of publicly available materials on how various mechanisms in the registry work, especially the most recent and most complicated ones, so I hope that the knowledge I have documented here will prove useful to others in the future.

In this blog post, we get to the heart of the matter, the actual security of the Windows Registry. I'd like to talk about what made a feature that was initially meant to be just a quick test of my fuzzing infrastructure draw me into manual research for the next 1.5 ~ 2 years, and result in Microsoft fixing (so far) 53 CVEs. I will describe the various areas that are important in the context of low-level security research, from very general ones, such as the characteristics of the codebase that allow security bugs to exist in the first place, to more specific ones, like all possible entry points to attack the registry, the impact of vulnerabilities and the primitives they generate, and some considerations on effective fuzzing and where more bugs might still be lurking.

Let's start with a quick recap of the registry's most fundamental properties as an attack surface:

* Local attack surface for privilege escalation: As we already know, the Windows Registry is a strictly local attack surface that can potentially be leveraged by a less privileged process to gain the privileges of a higher privileged process or the kernel. It doesn't have any remote components except for the Remote Registry service, which is relatively small and not accessible from the Internet on most Windows installations.
* Complex, old codebase in a memory-unsafe language: The Windows Registry is a vast and complex mechanism, entirely written in C, most of it many years ago. This means that both logic and memory safety bugs are likely to occur, and many such issues, once found, would likely remain unfixed for years or even decades.
* Present in the core NT kernel: The registry implementation resides in the core Windows kernel executable (ntoskrnl.exe), which means it is not subject to mitigations like the win32k lockdown. Of course, the reachability of each registry bug needs to be considered separately in the context of specific restrictions (e.g., sandbox), as some of them require file system access or the ability to open a handle to a specific key. Nevertheless, being an integral part of the kernel significantly increases the chances that a given bug can be exploited.
* Most code reachable by unprivileged users: The registry is a feature that was created for use by ordinary user-mode applications. It is therefore not surprising that the vast majority of registry-related code is reachable without any special privileges, and only a small part of the interface requires administrator rights. Privilege escalation from medium IL (Integrity Level) to the kernel is probably the most likely scenario of how a registry vulnerability could be exploited.
* Manages sensitive information: In addition to the registry implementation itself being complex and potentially prone to bugs, it's important to remember that the registry inherently stores security-critical system information, including various global configurations, passwords, user permissions, and other sensitive data. This means that not only low-level bugs that directly allow code execution are a concern, but also data-only attacks and logic bugs that permit unauthorized modification or even disclosure of registry keys without proper permissions.
* Not trivial to fuzz, and not very well documented: Overall, it seems that the registry is not a very friendly target for bug hunting without any knowledge of its internals. At the same time, obtaining the information is not easy either, especially for the latest registry mechanisms, which are not publicly documented and learning about them basically boils down to reverse engineering. In other words, the entry bar into this area is quite high, which can be an advantage or a disadvantage depending on the time and commitment of a potential researcher.

## Security properties

The above cursory analysis seems to indicate that the registry may be a good audit target for someone interested in EoP bugs on Windows.  Let's now take a closer look at some of the specific low-level reasons why the registry has proven to be a fruitful research objective.

### Broad range of bug classes

Due to the registry being both complex and a central mechanism in the system operating with kernel-mode privileges, numerous classes of bugs can occur within it. An example vulnerability classification is presented below:

* Hive memory corruption: Every invasive operation performed on the registry (i.e., a "write" operation) is reflected in changes made to the memory-mapped view of the hive's structure. Considering that objects within the hive include variable-length arrays, structures with counted references, and references to other cells via cell indexes (hives' equivalent of memory pointers), it's natural to expect common issues like buffer overflows or use-after-frees.
* Pool memory corruption: In addition to hive memory mappings, the Configuration Manager also stores a significant amount of information on kernel pools. Firstly, there are cached copies of certain hive data, as described in my previous blog post. Secondly, there are various auxiliary objects, such as those allocated and subsequently released within a single system call. Many of these objects can fall victim to memory management bugs typical of the C language.
* Information disclosure: Because the registry implementation is part of the kernel, and it exchanges large amounts of information with unprivileged user-mode applications, it must be careful not to accidentally disclose uninitialized data from the stack or kernel pools to the caller. This can happen both through output data copied to user-mode memory and through other channels, such as data leakage to a file (hive file or related log file). Therefore, it is worthwhile to keep an eye on whether all arrays and dynamically allocated buffers are fully populated or carefully filled with zeros before passing them to a lower-privileged context.
* Race conditions: As a multithreaded environment, Windows allows for concurrent registry access by multiple threads. Consequently, the registry implementation must correctly synchronize access to all shared kernel-side objects and be mindful of "double fetch" bugs, which are characteristic of user-mode client interactions.
* Logic bug...