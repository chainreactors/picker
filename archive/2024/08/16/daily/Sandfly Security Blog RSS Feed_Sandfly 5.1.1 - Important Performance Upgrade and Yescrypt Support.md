---
title: Sandfly 5.1.1 - Important Performance Upgrade and Yescrypt Support
url: https://sandflysecurity.com/about-us/news/sandfly-5-1-1-important-performance-upgrade-and-yescrypt-support
source: Sandfly Security Blog RSS Feed
date: 2024-08-16
fetch_date: 2025-10-06T18:03:29.999355
---

# Sandfly 5.1.1 - Important Performance Upgrade and Yescrypt Support

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.1.1 - Important Performance Upgrade and Yescrypt Support

15 August 2024

Product Update

Sandfly 5.1.1 is released and includes an important bug fix which will improve database efficiency. It also includes new *yescrypt* support for our agentless password auditing, plus new detection modules for debugger attacks, thread masquerading, host system information, and more.

The database bug fix offers **significant performance improvement** and we recommend you read that section carefully before upgrading.

### Database Bug Fix

We fixed a bug where raw result JSON was not being deleted when events automatically expired. The only way this data would delete is if the customer selected "Delete All" results. Because the raw result JSON was not being deleted automatically, this bug could lead to continuous database growth even though old results appeared to be deleted after the data retention period expired.

Sandfly 5.1.1 has scripts to go in and delete this old data during the upgrade. However, if you have many old results **this can take a long time** and cannot be backgrounded. You will need to wait until the clean-up operation completes before the system comes up after upgrade.

**We recommend you do "Delete All" results in the UI before you do the upgrade.** If you do not need the results this will ensure an instant upgrade happens. Deleting all results is shown in our documentation:

[Deleting Results](https://docs.sandflysecurity.com/docs/deleting-results)

If you require the old results, you will need to wait until the upgrade process completes. Depending on the result totals and server hardware, this can take some time to finish as the database is scrubbed of old data.

With this bug fixed, it will result in significantly smaller database storage needs and system performance will be faster as well.

### Yescrypt Password Algorithm Support

We sponsored the open source porting of the [Yescrypt password algorithm](https://www.openwall.com/yescrypt/) to Go and made this available in our agentless password auditor.

Sandfly is unique as we work as a Linux EDR, but also can do things on remote systems to be proactive about security. One of our proactive features is our ability to audit users directly on endpoints and find default, weak, and custom passwords agentlessly that will lead to immediate compromise.

Newer Linux distributions have moved to using the *Yescrypt* algorithm by default. *Yescrypt* is a modern hashing algorithm with protections in place to make dedicated hardware brute forcing much harder. We worked with the designers of *Yescrypt* over at [Openwall](https://www.openwall.com/) to implement the algorithm for use in Sandfly. We also sponsored this work as an open source project so others can make use of the algorithm in their own Go code.

Sandfly can now audit passwords on modern systems running *Yescrypt* to legacy distributions using older SHA512, MD5 and other algorithms. This includes extremely difficult to monitor embedded systems which very often have default passwords creating a significant security risk to organizations.

### New Detection Modules

We have added in many new detection capabilities detailed below.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Alert on Linux kernels version 3](https://www.datocms-assets.com/56687/1723695686-screenshot-2024-08-15-at-4-21-00-pm.png?auto=format&dpr=2&q=60&w=920 "Alert on Linux kernels version 3")

Alert on Linux kernels version 3

#### OS Identify Signatures and Custom Detection

Sandfly always runs our *os\_identify* module when we connect to a host. This module pulls over all basic operating system information such as hardware, distribution versions, CPU details, memory, disk mounts, network interfaces, performance data, plus much more. It functions as an asset inventory. Now, customers can build sandfly modules against any of these parameters such as kernel versions, CPU bugs, hardware types, and more to generate alerts.

We have included the following modules to provide an example of the capability to customers:

**policy\_cpu\_bugs\_meltdown** - A sample template to show you how to search for specific CPU bugs you want to know about. This demonstrates searching for the Meltdown CPU bug, but can be altered to search for any or all bugs. This is not enabled by default, but can be used to build custom sandfly modules for your needs.

**policy\_kernel\_version\_notable** - Another template to allow you to search for specific kernel versions of interest operating in your environment.

**policy\_kernel\_version\_release\_2\_or\_older** - A policy module that will show you any system running old 2.x Linux kernels. Disabled by default.

**policy\_kernel\_version\_release\_3** - Another policy module that will show you any Linux kernels that are version 3. Disabled by default.

These modules demonstrate this new capability which can be cloned and used by teams to search for any attribute we collect in the *os\_identify* data. We collect extensive data and are here to assist customers if they need any help in customizing them for their needs.

#### Threat Detection

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![](https://www.datocms-assets.com/56687/1723672768-tracer-pid-running.png?auto=format&dpr=2&q=60&w=920)

We have improved and added in new detections for the following:

**process\_masquerade\_kernel\_thread\_flag\_mismatch** -A process is running that is trying to impersonate a kernel thread. This builds on our existing threat detection modules for this attack by leveraging new Linux kernel flags present in 6.x kernels.

**process\_running\_debugger\_anti\_debugging** -Spots a process that has attached a debugger function to itself to prevent other debuggers from being used against it. This is often done for anti-debugging in malware to prevent runtime analysis.

**process\_running\_debugger\_attached** -A process is running with an active debugger attached. This could indicate someone is trying to steal confidential data such as passwords, cryptographic keys, or confidential data from a process.

**process\_running\_debugger\_attached\_state** -Like previous, another way to detect a process is running with a debugger attached.

**process\_shell\_running\_ssh\_command\_invocation** -A shell was invoked directly from ssh instead of using the normal user login shell. This is a suspicious way to invoke a shell and often is done to prevent command history and other auditing. This check is **disabled** by default due to false alarm risk on older CentOS systems. For modern systems it can be enabled and provides reliable detection of this problem.

**recon\_process\_list\_root\_gid** - Get a recon listing of all processes running with the *root* group ID (GID). Useful for drift detection profiling if you want to spot new root owned processes running.

**recon\_process\_list\_root\_uid** -Like above, but recon list for the *root* user ID (UID) running a process. Again, useful for drift detection of new *root* owned processes running on a host.

**process\_match\_groupname\_status** -A *template* to allow you to find any process running with a specific group name. For instance, finding all processes running under a web server group. This template provides examples of how to do this search for custom sandfly use.

### SSH Banned Key Zone Violation

When a banned key is seen inside a SSH Security Zone, the zone will show a new Banned Key Violation tag even if the key is tagged as authorized in that zone.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH Zone Alert](https://www.datocms-assets.com/56687/1723695502-screenshot-2024-08-15-at-4-13-5...