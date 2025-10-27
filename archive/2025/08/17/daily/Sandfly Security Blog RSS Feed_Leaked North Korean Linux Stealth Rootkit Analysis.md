---
title: Leaked North Korean Linux Stealth Rootkit Analysis
url: https://sandflysecurity.com/blog/leaked-north-korean-linux-stealth-rootkit-analysis
source: Sandfly Security Blog RSS Feed
date: 2025-08-17
fetch_date: 2025-10-07T00:17:36.441750
---

# Leaked North Korean Linux Stealth Rootkit Analysis

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Leaked Chinese (Korea Targeting) Linux Stealth Rootkit Analysis

14 August 2025

Malware

[Phrack Magazine](https://www.phrack.org) issue #72 recently released a data dump from a suspected Chinese or possibly North Korean hacking group that contained a large trove of exploit tactics, compromised system information, and a stealth rootkit targeting Linux. We have reviewed the rootkit and are providing additional detection and operation details for incident responders.

We highly encourage teams to read the initial Phrack article which lays out the data obtained. Specifically they note:

1. Chinese threat actor targets government and private sector in South Korea and Taiwan. Some of its targets and tactics align with North Korean Kimsuky APT group.
2. Dump suggests that the attackers accessed internal South Korean government networks and had access to sensitive certificates.
3. Screenshot of the attacker’s desktop shows active backdoor development.

Phrack has made the entire data dump available below along with the PDF article of the leaked information. Please be aware that this archive contains live malware binaries for multiple platforms and should be handled carefully:

[Phrack North Korean Data Dump](https://drive.proton.me/urls/ZQ1235FY7C#P0khjXI2uEtS)

### Rootkit Details

As the Phrack article states, the malware is a Loadable Kernel Module (LKM) style rootkit with ability to hide from detection and operate on any network port. The data dump contained two bundles of the rootkit. This analysis is for the most recently dated 2025 version.

The rootkit has the following features:

* Based on the [khook library](https://github.com/milabs/khook) which is commonly used by malware to hook and intercept Linux kernel system calls to evade detection.
* Hides its kernel module from listing with tools like *lsmod*.
* Hides processes and backdoor network activity.
* Hides persistence files dropped under */etc/init.d* and */etc/rc\*.d* directories.
* Receives magic packet on any port to activate backdoor.
* The backdoor can execute shells, upload and download files, activate proxies, or chain hosts together for lateral movement.
* Commands have anti-forensic features for the backdoor binary and shells spawned.
* All traffic is encrypted.

### Rootkit Detection

The rootkit can be found by Sandfly out of the box without any updates for customers. We have had detections for this style of rootkit for some time. We **strongly urge**customers use automated tools to find this rootkit so detection can be done accurately and at scale. However, we will provide manual commands you may choose to use on individual hosts you are investigating for compromise in this article. Below are the default alerts Sandfly will generate on a host with this kernel rootkit and backdoor activated.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Rootkit Sandfly Alerts](https://www.datocms-assets.com/56687/1755172808-korea-rootkit-initial-alerts.png?auto=format&dpr=2&q=60&w=920 "Rootkit Sandfly Alerts")

### Rootkit Basic Operation

As with almost all LKM style rootkits, they tend to be fragile and kernel version specific. This rootkit is no different. To be deployed successfully, the attacker would need to have a version built for the specific victim kernel version. This is tedious and prone to risk, but once working the module goes live and sits quietly. However, it also means that system updates that involve a new kernel may very well cause the rootkit to fail entirely and not load or work correctly.

### Kernel Module Location

The malicious module is stored under */usr/lib64/tracker-fs* in the disclosed version. This is easily changed by attackers however and should not be relied upon for certain detection. However, for initial incident response it is not a bad idea to look for it using the following commands:

`stat /usr/lib64/tracker-fs
file /usr/lib64/tracker-fs`

These command should not show any files. If you get data back then the module is present and this means it is active, or was once active, on the host. Here are a couple examples of what you is seen if the module is active.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Using stat command to reveal hidden rootkit module.](https://www.datocms-assets.com/56687/1755149700-korea-stat-usr-include-tracker-fs.png?auto=format&dpr=2&q=60&w=920 "Using stat command to reveal hidden rootkit module.")

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Using file command to reveal rootkit module.](https://www.datocms-assets.com/56687/1755149706-korea-file-usr-include-tracker-fs.png?auto=format&dpr=2&q=60&w=920 "Using file command to reveal rootkit module.")

### Unsigned Module Kernel Taint Indicator

The next sign of trouble is that the kernel module is not signed. Unsigned kernel modules on Linux can be used by legitimate vendors (e.g. video cards), but if your systems do not use any unsigned modules it can mean trouble. We cover the detection of [tainted kernel modules in this post](https://sandflysecurity.com/blog/sandfly-4-3-2-linux-loadable-kernel-module-rootkit-taint-detection), but we can also find it with some basic commands.

For this rootkit, the default malicious kernel module name is *vmwfxs*. This can obviously be changed by attackers easily so we don't recommend searching for this string directly, but you can use the following commands to see what tainted modules may be in use on a system and this can expose new variants.

These three commands will show taint status, or the deliberate loading of the module *vmwfxs* which is the name used by this rootkit.

`dmesg | grep taint
dmesg | grep vmwfxs
grep taint /var/log/kern.log`

The output from an affected system will look like the below when searching for taint status in the *dmesg* command. Evaluate any output to see if a module name looks suspicious or unexpected.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![dmesg check for tainted modules on Linux.](https://www.datocms-assets.com/56687/1755147389-korea-dmesg-vmwfxs-module-signature-taint.png?auto=format&dpr=2&q=60&w=920 "dmesg check for tainted modules on Linux.")

Since *dmesg* is a ring buffer, it's possible that messages could have rolled out over time. Another area to check that may have more persistence is */var/log/kern.log* found on some systems. Below we see multiple tainted messages when the system rebooted and loaded the kernel module on each startup. The *dmesg* command won't show this continuity like the on-disk */var/log/kern.log* will if available.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Malicious Linux kernel module found in /var/log/kern.log](https://www.datocms-assets.com/56687/1755147534-korea-var-log-kern-log-vmwfxs-module-signature-taint.png?auto=format&dpr=2&q=60&w=920 "Malicious Linux kernel module found in /var/log/kern.log")

In Sandfly we also will identify tainted kernels, but go a step further to see if there is kernel taint but no module listed as having caused it. This often means a module loaded and then removed itself from listing to hide. Unfortunately while this is a great check, there is no direct command line tool to run it broadly so we recommend using our detection if available.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Kernel taint inconsistency detected by Sandfly.](https://www.datocms-assets.com/56687/1755147873-korea-kernel-tainted-inconsistency.png?auto=format&dpr=2&q=60&w=920 "Kernel taint inconsistency detected by Sandfly.")

Additionally, for customers using drift detection we will alert if taint status has shifted from the expected profile. This is another great option if ava...