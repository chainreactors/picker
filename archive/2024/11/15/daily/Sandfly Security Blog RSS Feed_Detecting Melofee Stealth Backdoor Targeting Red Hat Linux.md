---
title: Detecting Melofee Stealth Backdoor Targeting Red Hat Linux
url: https://sandflysecurity.com/blog/detecting-melofee-stealth-backdoor-targeting-redhat-linux/
source: Sandfly Security Blog RSS Feed
date: 2024-11-15
fetch_date: 2025-10-06T19:18:30.935525
---

# Detecting Melofee Stealth Backdoor Targeting Red Hat Linux

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Detecting Melofee Stealth Backdoor Targeting Red Hat Linux

14 November 2024

Linux Security

A new report from Qianxin's X Lab was released detailing new stealth malware targeting Red Hat 7.9 and similar systems:

[New Zero-Detection Variant of Melofee Backdoor from Winnti Strikes RHEL 7.9](https://blog.xlab.qianxin.com/analysis_of_new_melofee_variant_en/)

This malware currently shows zero detection coverage at Virus Total as of today, but Sandfly was able to easily see it operating. In this report we'll discuss Sandfly detection of this malware to help customers assess their hosts for compromise.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Virus Total Zero Detection](https://www.datocms-assets.com/56687/1731539030-virustotal-summary.png?auto=format&dpr=2&q=60&w=920 "Virus Total Zero Detection")

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Melofee Stealth Malware Sandfly Alerts](https://www.datocms-assets.com/56687/1731545579-melofee-malware-sandfly-alerts.png?auto=format&dpr=2&q=60&w=920 "Melofee Stealth Malware Sandfly Alerts")

## Melofee Malware Stealth Evasion

As the report above states, the *melofee* malware has full stealth capabilities. In particular, the malware includes an encrypted Loadable Kernel Module (LKM) rootkit based on the *Reptile* project which is a common base for many kinds of malware. The encryption helps avoid signature scanning and related detection techniques.

Once the rootkit goes active, it loads the LKM portion rendering the main process invisible along with other capabilities. Casual observation of a system infected with the malware will not show its presence.

The malware has capability to do some of the following:

* Hide processes.
* Hide files.
* Hide kernel module presence.
* Hide persistence mechanisms.

The malware has functionality to enable stealth and maintain access to systems where it is executed.

## Sandfly Detection

The malware is showing no detection with legacy anti-virus systems as of now, but tactically it is doing many things that are suspicious and identified by Sandfly immediately. Sandfly customers seeing these alerts should take immediate action.

## Hidden Kernel Module

First, we identify a kernel module that is trying to hide itself called *kworkerx*. The rootkit hides itself once active so it is not present in *lsmod* or similar commands that try to list active modules.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Melofee Kernel Module Hiding Detection](https://www.datocms-assets.com/56687/1731539830-melofee-kernel-module-hidden.png?auto=format&dpr=2&q=60&w=920 "Melofee Kernel Module Hiding Detection")

## Kernel Taint Inconsistency

Once active, the Linux kernel is "tainted" as the malicious module is not signed nor part of the distribution (called out-of-tree). Modules that are unsigned, or out-of-tree, are always suspicious unless you know why they are present (e.g. a proprietary video driver).

In this case, the module taints the kernel with an unsigned module, but then hides itself from view. This creates an inconsistency that Sandfly alerts on. Basically, the kernel says it is tainted with an unsigned module, but nobody is fessing up to have done it. This means the module that caused the taint may very likely be hiding.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux Rootkit Kernel Taint Inconsistency](https://www.datocms-assets.com/56687/1731540170-melofee-kernel-module-inconsistency.png?auto=format&dpr=2&q=60&w=920 "Linux Rootkit Kernel Taint Inconsistency")

## Kernel Module Missing

On Linux, legitimate kernel modules usually are located in specific directories for the kernel version on the host. When we look for this file we do not find it. This means the module is either loading from a non-standard location (which is suspicious), or is hiding itself from being viewed in the directory with other modules (even more suspicious). In either case, we see an alert for our *kworkerx* module again as it hides.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Melofee Malware Kernel Module Missing](https://www.datocms-assets.com/56687/1731540558-melofee-kernel-module-missing.png?auto=format&dpr=2&q=60&w=920 "Melofee Malware Kernel Module Missing")

## Drift Detection Kernel Module Alert

If you are using [Sandfly's drift detection](https://sandflysecurity.com/platform/drift-detection/), you can have it spot new kernel modules that have appeared. In the case of our affected host, we again see that a new module called *kworkerx* has made its presence known. Drift detection is a powerful way to spot novel malware on Linux across processes, users, SSH keys, kernel modules, network services, and more. We encourage customers to use it where appropriate.

Drift detection easily spots the new module even outside of the suspicious activity it did prior. The list below shows the new module in red among valid green modules the drift detection expects to see on the host.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Kernel Module Drift Detection Spots Intruder](https://www.datocms-assets.com/56687/1731540755-melofee-kernel-module-drift-detection.png?auto=format&dpr=2&q=60&w=920 "Kernel Module Drift Detection Spots Intruder")

## Hidden Stealth Process

After the rootkit activates, it spins up a new process called *[md]* and hides itself. The process is the main communications part of the malware to allow attacker control of the system. The process name is significant as it is trying to impersonate a kernel thread (discussed below). But more significantly, it activates the hidden process detection in Sandfly. Sandfly shows the process forensics data after de-cloaking the entire operation.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![De-Cloaking Hidden Melofee Malware Process](https://www.datocms-assets.com/56687/1731541027-melofee-process-hidden.png?auto=format&dpr=2&q=60&w=920 "De-Cloaking Hidden Melofee Malware Process")

## Process Kernel Thread Masquerading

The malicious *[md]* process uses brackets meaning it is trying to look like a kernel thread in process listings. This is a common tactic with Linux malware. In this case, it activates five separate alerts in Sandfly for kernel thread masquerading. The alerts are all variations of the same attack type seen from different perspectives. One of the results is shown below for illustration.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Kernel Thread Masquerading Alerts](https://www.datocms-assets.com/56687/1731541232-melofee-kernel-masquerade-alerts.png?auto=format&dpr=2&q=60&w=920 "Kernel Thread Masquerading Alerts")

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux Kernel Thread Masquerading Specifics](https://www.datocms-assets.com/56687/1731541303-melofee-kernel-masquerade-alert-variant.png?auto=format&dpr=2&q=60&w=920 "Linux Kernel Thread Masquerading Specifics")

Processes using [brackets] for their name that are not kernel threads are often malicious. For this malware, it leaves a very clear trail that something is wrong with this host.

## Manual Discovery

While we strongly recommend using Sandfly to help hunt for this malware due to the stealth nature, it is possible to find it manually if you choose to do so. While it is tempting to use the cryptographic hash of the malware to search systems, this is notoriously unreliable on Linux. We recommend reading the initial report and looking for the following.

First: A dropper file is present when the malware is active on a host:

*/tmp/lock\_tmp1*

Second: This malicious module directory is present when the malware is active:
...