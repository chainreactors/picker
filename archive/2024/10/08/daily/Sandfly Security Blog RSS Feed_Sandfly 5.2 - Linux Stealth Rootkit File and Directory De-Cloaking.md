---
title: Sandfly 5.2 - Linux Stealth Rootkit File and Directory De-Cloaking
url: https://sandflysecurity.com/about-us/news/sandfly-5-2-linux-stealth-rootkit-file-and-directory-de-cloaking/
source: Sandfly Security Blog RSS Feed
date: 2024-10-08
fetch_date: 2025-10-06T18:50:15.125902
---

# Sandfly 5.2 - Linux Stealth Rootkit File and Directory De-Cloaking

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.2 - Linux Stealth Rootkit File and Directory De-Cloaking

07 October 2024

Product Update

Sandfly 5.2 has a powerful new way to detect Linux stealth rootkits: Hidden file and directory de-cloaking.

This feature will make files and directories hidden by many types of stealth rootkits immediately visible. More importantly, many of the ways rootkits hide their files and directories from detection on Linux will no longer work. We turn hiding from an asset into a liability.

We encourage customers to upgrade and report back any findings. Please read more about this important new feature below.

### Linux Stealth Rootkit Background and Tactics

There are many types of rootkits available on Linux from very simple to advanced. At the top end of the threat spectrum are what is called Loadable Kernel Module (LKM) or simply stealth rootkits. These rootkits are characterized by some common traits:

* They intercept kernel system calls to hide their presence.
* They hide processes.
* They hide network activity.
* They hide directories.
* They hide files and the data they contain.

Sandfly has had mechanisms to find variants of these tactics for some time, but we wanted to go a step further. In particular, we wanted to detect and de-cloak files or directories hidden by these rootkits and make the entire hiding tactic no longer work for any of them. And, we wanted to do it with our proven fast and safe agentless mechanism.

We're happy to announce that we've succeeded. Sandfly 5.2 makes the entire class of hiding files and directories with traditional stealth rootkit methods easily spotted.

### Stealth Rootkit Hiding Methods

Linux stealth rootkits hook various system calls to hide processes, files, directories and even data inside files they do not want seen. Once these mechanisms are active, administrators and security teams logging into a host will see no signs of intruder activity.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux Stealth Rootkit Kernel Hooking](https://www.datocms-assets.com/56687/1728249167-stealth-rootkit-kernel-hooking.png?auto=format&dpr=2&q=60&w=920 "Linux Stealth Rootkit Kernel Hooking")

The illustration above shows the basic flow of a stealth rootkit on Linux. Attackers will hook relevant system calls that display running processes, directories, files, network activity and even data they don't want revealed in files (e.g. startup commands for persistence). Once hooked, the system calls are run through the rootkit and data is modified to appear innocent before being returned.

### Turning an Advantage into a Liability

What if we could see what files and directories a rootkit is hiding? If we could do this, then what is normally an advantage for the rootkit (being able to hide) actually turns into a significant disadvantage because it instantly reveals the system is compromised. This is what Sandfly 5.2 and our file and directory de-cloaking does: **We make hiding on Linux a liability.**

Let's see this liability in action. We'll use two common stealth rootkits: *Diamorphine* and *Reptile*. These rootkits are used as a base for many variants. They both use kernel hooking methods to hide files and directories that match secret words (e.g. the file or directory has the word "*reptile*" or "*diamorphine*" in it).

Below we flag a hidden directory from *Diamorphine* under the system */bin* directory. It is immediately obvious something is hiding from view.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Diamorphine Hidden Directory Detected](https://www.datocms-assets.com/56687/1728276607-diamorphine-hidden-directory.png?auto=format&dpr=2&q=60&w=920 "Diamorphine Hidden Directory Detected")

Next we look at a system running *Reptile* and identify the startup file being used to maintain persistence using *udev* rules. Notice that the file is not only de-cloaked, but all file forensic attributes are available including creation dates, owner, cryptographic hashes, and more. This happens even if you can't see the file on the host with other tools.

Most importantly, this is a high-fidelity alert. The rootkit actually calls out like a blaring siren that something is wrong by hiding.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Reptile rootkit with hidden file on Linux de-cloaked.](https://www.datocms-assets.com/56687/1728252051-reptile-hidden-file.png?auto=format&dpr=2&q=60&w=920 "Reptile rootkit with hidden file on Linux de-cloaked.")

### De-Cloaking Modules in Sandfly 5.2

Sandfly checks high-risk areas for signs of cloaked files or directories. The modules below are enabled by default with the exception of the *anywhere* check, which is designed for use during incident response to scan the entire file system if needed.

**dirs\_cloaked\_entry\_bin** - Cloaked files and directories under common system binary locations.

**dirs\_cloaked\_entry\_etc** - Cloaked files and directories under */etc.*

**dirs\_cloaked\_entry\_lib** - Cloaked files and directories under library and kernel module locations.

**dirs\_cloaked\_entry\_root** - Cloaked files and directories under the system */ (root)* locations.

**dirs\_cloaked\_entry\_system** - Cloaked files and directories under system areas such as */boot.*

**dirs\_cloaked\_entry\_usr\_*****\**** - Cloaked files and directories under various */usr* locations.

**dirs\_cloaked\_entry\_var** - Cloaked files or directories under */var* locations*.*

**dirs\_cloaked\_entry\_anywhere** - Cloaked files and directories anywhere on the disk (incident response check).

Customers can clone any of these and make custom directories they wish to check on demand.

### Stealth Rootkit Detection Arsenal To Date

In addition to these new features, all of the following stealth rootkit detection methods are in our core product for immediate deployment agentlessly.

* **De-cloaking hidden processes** - Finds binaries running with a hidden process ID (PID).
* **Reveal hidden kernel modules** - Detects kernel modules hiding their presence.
* **Detecting kernel taint inconsistencies** - Finds tainted kernels that have had unsigned or unknown modules loaded but are hiding from view.
* **Directory link count inconsistencies** - Finds directories that have one or more entries hidden due to inconsistent link counts (e.g. kernel says 3 directories but file system reports 4 present).
* **File size mismatches** - Finds files hiding data due to inconsistent byte counts vs. reported file size (e.g. kernel says file is 100 bytes, but file system says it is 120 bytes).
* **Suspicious activity with LD\_PRELOAD**- Finds user space rootkits using LD\_PRELOAD as attack vector. This is not kernel space rootkit, but we include it here for completeness.
* **File and directory de-cloaking**- Our new ability here to instantly reveal files or directories being actively hidden by a stealth rootkit on Linux.

### Technical Considerations

De-cloaking works on *EXT4* and *XFS* file systems. We may add support for other file systems in the future. However, these two file systems are the majority of Linux installs globally and we expect extremely wide coverage for this threat. The capability will work across any architecture Sandfly supports such as Intel, AMD, ARM, MIPS and IBM POWER CPUs. It also will work on servers, appliances and even embedded devices. As with all Sandfly installs, it also works on systems up to a decade+ old to modern distributions, even those in the cloud or on-premise.

Keeping with our core philosophy, these methods do not tie into kernel space and they work agentlessly. This significantly decreases system performance and stability risks commonly associated with agent-b...