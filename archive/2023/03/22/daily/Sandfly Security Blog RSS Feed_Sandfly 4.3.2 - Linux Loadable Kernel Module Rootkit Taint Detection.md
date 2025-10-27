---
title: Sandfly 4.3.2 - Linux Loadable Kernel Module Rootkit Taint Detection
url: https://sandflysecurity.com/blog/sandfly-4-3-2-linux-loadable-kernel-module-rootkit-taint-detection
source: Sandfly Security Blog RSS Feed
date: 2023-03-22
fetch_date: 2025-10-04T10:15:13.875429
---

# Sandfly 4.3.2 - Linux Loadable Kernel Module Rootkit Taint Detection

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 4.3.2 - Linux Loadable Kernel Module Rootkit Taint Detection

21 March 2023

Product Update

Version 4.3.2 of Sandfly incorporates various innovative techniques for identifying Linux kernel taint inconsistencies, which aid in uncovering stealth rootkit activity. Additionally, we have integrated extra modules for auditing unverified and out-of-tree kernel modules and *memfd\_create* file descriptor activities typical of malware. We also have modules to expand our general Linux rootkit detection that are using common kernel hooking libraries.

In addition to this, we have also incorporated SSH host key validation features.

Finally, we have substantially enhanced the database performance of SSH Hunter and overall result processing to handle considerably larger workloads.

## Kernel Taint Detection

The Linux kernel uses the term "taint" to indicate if the active kernel contains unsigned, non-standard (out-of-tree), or other types of modules. Modules causing a tainted kernel can range from harmless, such as proprietary video drivers, to malicious, like Loadable Kernel Module (LKM) rootkits.

Sandfly has introduced multiple techniques for detecting kernel taint, enabling operators to establish policies for reporting on different tainted modes. We now provide modules to identify the following:

* Unsigned modules.
* Out-of-tree modules.
* Custom tainted modules (user-defined).
* Kernel taint inconsistencies.
* Policy detection for tainted kernel modules in use, regardless of type.

## Unsigned and Out-Of-Tree Modules

The most frequent module activities that may be deemed suspicious are those marked as unsigned or out-of-tree. These flags indicate that a module has been detected without a valid signature and/or not belonging to the standard kernel build tree. While this can occur occasionally with specific proprietary drivers (e.g., video), it might be considered unusual on a base system and potentially indicative of an active LKM rootkit.

We now offer optional detection for such activities, along with additional customizable detections for identifying any type of tainted flag that has been set.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Unsigned Linux Kernel Module Detected](https://www.datocms-assets.com/56687/1679361529-kernel_module_tainted_unsigned.png?auto=format&dpr=2&q=60&w=920 "Unsigned Linux Kernel Module Detected")

## Kernel Taint Inconsistency

LKM rootkits typically go to extraordinary lengths to conceal their presence on a host. For example, they might alter commands like *lsmod* to avoid displaying the rootkit when listing loaded modules.

However, these rootkits frequently overlook hiding all evidence of kernel taint on a system. Sandfly now ensures that kernel taint flags correspond with the kernel's stated status. Any inconsistency detected will be flagged for investigation.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux LKM rootkit causing inconsistency.](https://www.datocms-assets.com/56687/1679361728-kernel-taint-inconsistency.png?auto=format&dpr=2&q=60&w=920 "Linux LKM rootkit causing inconsistency.")

## Tainted Module Mismatch with Kernel

Related to the above, if a kernel module displays taint while the kernel fails to report it accurately, this will also be flagged. Such a situation may arise if a rootkit conceals itself but neglects to hide other tainted modules simultaneously. The discrepancy between the kernel's report and Sandfly's observations suggests that rootkit activity is occurring.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Mismatched kernel taint state on Linux means a rootkit is active.](https://www.datocms-assets.com/56687/1679361873-kernel_module_tainted_not_in_kernel.png?auto=format&dpr=2&q=60&w=920 "Mismatched kernel taint state on Linux means a rootkit is active.")

## Kernel Module Unexpected Policy

We have added a new policy check where customers can define a list of expected modules across their systems and Sandfly will flag any modules that show up that are not on the list.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Unexpected Linux kernel module detected.](https://www.datocms-assets.com/56687/1679361993-kernel_module_unexpected.png?auto=format&dpr=2&q=60&w=920 "Unexpected Linux kernel module detected.")

## Hiding Linux ELF Executable in memfd\_create()

The *memfd\_create()* call can be used for a variety of hiding activities for fileless malware on Linux. We have been able to detect suspicious activity using this tactic for some time, but have enhanced it with specific detection for the file type we see being concealed.

Below we have a detection that has flagged a Linux ELF executable file being hidden in a *memfd* file descriptor. This kind of activity is extremely suspicious and requires immediate investigation.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![memfd_create fileless attack on Linux.](https://www.datocms-assets.com/56687/1679431079-memfd_create-elf-hidden.png?auto=format&dpr=2&q=60&w=920 "memfd_create fileless attack on Linux.")

## Khook Rootkit Library Detection

We have improved detection for various Linux stealth rootkits based on the *khook* library. Systems showing signs of this style of rootkit now have more detection options.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Reptile rootkit on Linux detected.](https://www.datocms-assets.com/56687/1679430629-process_kernel_rootkit_lkm_vmallocinfo.png?auto=format&dpr=2&q=60&w=920 "Reptile rootkit on Linux detected.")

## Massive Speed Boost for SSH Hunter and Results

Customers have experienced tremendous success using our SSH Hunter to track and audit SSH keys. We have now implemented significant performance improvements, enabling queries to finish in less than a second, even when tracking tens of thousands of SSH keys.

Besides the speed enhancements for SSH Hunter, we have made substantial advancements in managing result ingestion. The user interface is now more responsive, and the system can accommodate much larger workloads on existing hardware.

## SSH Host Key Verification

You can how tell Sandfly to enforce host key verification when you add a group of hosts or enable/disable on a per host level.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH host key verification.](https://www.datocms-assets.com/56687/1679362954-host-key-verification-individual.png?auto=format&dpr=2&q=60&w=920 "SSH host key verification.")

## Host Load and RAM View and UI Improvements

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Host view from Sandfly.](https://www.datocms-assets.com/56687/1679362382-host-load.png?auto=format&dpr=2&q=60&w=920 "Host view from Sandfly.")

The UI has had many significant enhancements such as the following:

* Load and RAM status on hosts.
* Search bar on tables.
* Whitelisting/Un-Whitelisting Button
* Improved and wider view areas.
* SSH Key Hunter timeline cleanups and optimizations.

## Upgrading Sandfly

Customers wishing to upgrade can follow the instructions here:

[Upgrading Sandfly](https://support.sandflysecurity.com/support/solutions/articles/72000078711-upgrading-sandfly)

If you have any questions, please [reach out to us](https://www.sandflysecurity.com/contact-us/).

Thank you for using Sandfly.

---

Post Tags:

[Product Update](/blog/tag/product-update)[News](/blog/tag/news)

Share this post:

[← Return to Blog](/blog)

---

#### Contact Us

---

+64 3 3792313[4 Ash Street Christchurch, New Zealand 8011](https://goo.gl/maps/9cFto1o6GNa9RK6S9)

#### Connect With Us

---

#### Product Navigation

---

* [Threat Detection](/platform/threat-detection)
* ...