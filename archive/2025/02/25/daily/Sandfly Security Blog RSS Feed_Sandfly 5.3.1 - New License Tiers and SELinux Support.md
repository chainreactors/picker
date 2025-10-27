---
title: Sandfly 5.3.1 - New License Tiers and SELinux Support
url: https://sandflysecurity.com/about-us/news/sandfly-5-3-1-new-license-tiers-and-selinux-support/
source: Sandfly Security Blog RSS Feed
date: 2025-02-25
fetch_date: 2025-10-06T20:34:58.181885
---

# Sandfly 5.3.1 - New License Tiers and SELinux Support

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.3.1 - New License Tiers and SELinux Support

24 February 2025

Product Update

Sandfly 5.3.1 features new licensing tier options, including an affordable Home User Edition. We've also added SELinux support and more stealth rootkit detection. New features include just some of the following:

* New Home, Professional, and Air-Gapped license tiers
* Monthly and annual subscriptions
* SELinux support
* Expanded stealth rootkit detection
* New detections for masquerading processes, network sniffers, and SSH forwarding

### New License Tiers

We have been asked many times if we would offer a full-featured license for home users. We have also been asked if we had easier ways to try the product without needing to buy an annual license for commercial users. We now have answers to both of these questions.

#### Home User Edition License

Introducing our new Home User Edition of Sandfly. This is a full-featured version of Sandfly that is extremely affordable. This version has the following features:

* Protects up to 10 hosts **all inclusive** in the price
* Unlimited alert views
* SSH Hunter
* Password auditor
* 30 days data retention
* Automated scheduled threat scans
* Custom sandfly threat hunting modules

This version is perfect for a home network. The annual subscription is about $8 a month, or $99 a year to watch 10 systems. You get full agentless Linux EDR for an incredibly low price.

#### Professional Edition License

The Professional Edition allows users to quickly buy a Sandfly license that is fully unlocked. This version is for commercial use, or for power users at home that need extra capabilities such as distributed scanning, result replication, and Single Sign On (SSO). This version is available in monthly subscription, or annually at a discount. The Professional Edition features everything in the Home User Edition, plus:

* Unlimited users, including SSO login
* Unlimited schedules
* Jump hosts
* Distributed scanning
* Result replication to external SIEM and SOAR applications
* Full REST API access

This version gives immediate protection to commercial deployments either on-prem or in the cloud.

#### Air Gapped License

Sandfly is unique as we are one of the only Linux EDRs that does not require any active Internet connection to run. The product was designed from the beginning to allow air-gap operation and this continues with our Air Gapped license tier. This license has all the features of the Professional Edition, but is available as annual only with a license that works completely offline.

This license is perfect for organizations that will be using Sandfly in networks where the infrastructure will not have any Internet access.

#### Annual or Monthly Subscriptions

We have added the ability to get monthly subscriptions for users looking to try Sandfly on an extended basis. Annual subscriptions all offer substantial discounts once customers decide to upgrade. The air gapped license is available as an annual subscription only due to how the licensing works (offline only). Read more about the different licenses here:

[Get Sandfly](https://sandflysecurity.com/get-sandfly/)

If you need a larger volume of hosts, please [reach out to our team](https://sandflysecurity.com/contact-us/) for more information.

### SELinux Support

We have added support to determine SELinux boot and configuration status. We also made SELinux security context labels available for all processes, files, and directories.

#### SELinux Status Detection

Sandfly can now scan for the status of SELinux on your systems. If you require systems to run with SELinux enabled, this can be easily seen and verified with Sandfly. Further, we can also detect if the status since boot has changed to be disabled or is not set correctly.

The new policy modules for SELinux are the following:

*policy\_kernel\_selinux\_disabled* - Looks for systems that have SELinux disabled.

*policy\_kernel\_selinux\_enforce\_mode\_boot\_disabled* - Looks for systems that have SELinux enforce mode disabled at boot time.

*policy\_kernel\_selinux\_enforce\_mode\_boot\_permissive* - Looks for systems that have SELinux enforce mode set permissive at boot time.

*policy\_kernel\_selinux\_enforce\_mode\_current\_disabled* - Looks for systems that have SELinux enforce mode disabled in current state.

*policy\_kernel\_selinux\_enforce\_mode\_current\_permissive* - Looks for systems that have SELinux enforce mode set permissive in current state.

***policy\_kernel\_selinux\_enforce\_mode\_disabled\_since\_boot*** - Looks for systems that have had SELinux enforce mode disabled since boot.

*policy\_kernel\_selinux\_mls\_disabled* - Looks for systems that have SELinux MLS disabled.

The bold **policy\_kernel\_selinux\_enforce\_mode\_disabled\_since\_boot** module is enabled by default. Others can be enabled if relevant for your environment.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SELinux Disabled with setenforce 0](https://www.datocms-assets.com/56687/1740348128-selinux-disabled-since-boot.png?auto=format&dpr=2&q=60&w=920 "SELinux Disabled with setenforce 0")

SELinux Disabled with setenforce 0

The **policy\_kernel\_selinux\_enforce\_mode\_disabled\_since\_boot** is enabled by default as it can find systems where attackers executed *setenforce 0* to disable SELinux. This is often done by attackers that have obtained root access and is a strong indication of compromise if you are not expecting to see it on your hosts.

#### SELinux Security Contexts: Processes, Files, and Directories

We have added SELinux security context label reporting on all processes, files, directories and file descriptors. This is a powerful way to make sure systems are not running unconfined processes, incorrect SELinux types, or leaking data in directories where it shouldn't be.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Unconfined SELinux Network Process Found](https://www.datocms-assets.com/56687/1740349400-selinux-unconfined-network-process.png?auto=format&dpr=2&q=60&w=920 "Unconfined SELinux Network Process Found")

For instance, admins can quickly find any systems running unconfined network processes. Or, security teams can search across directories for sensitive file contexts that may have leaked (e.g. password or SSH key data). We have a variety of modules teams can clone and modify to suit their needs as well. New modules include the following:

*policy\_process\_selinux\_unconfined\_type\_network\_port\_listening* - Looks for network processes with listening ports and unconfined SELinux context.

*policy\_process\_selinux\_unconfined\_type\_network\_port\_operating* - Looks for network processes operating (listening or established) with unconfined SELinux context.

*policy\_process\_selinux\_unconfined\_type\_running* - Looks for **any** process running with unconfined type SELinux context.

We also have modules to find SELinux file contexts that may be sensitive if left in vulnerable areas. These modules can be easily cloned and modified by teams for custom SELinux sweeps for a variety of uses.

*file\_selinux\_passwd\_shadow\_context\_in\_dev\_shm\_dir* - Searches for */etc/passwd* or */etc/shadow* SELinux context types in system /dev/shm ramdisk directories.

*file\_selinux\_passwd\_shadow\_context\_in\_tmp\_dir* - Searches for */etc/passwd* or */etc/shadow* SELinux context types in system temporary directories.

*file\_selinux\_shell\_exec\_context\_in\_dev\_shm\_dir* - Searches for shell\_exec\_t system shell context types in system /dev/shm ramdisk directories.

*file\_selinux\_shell\_exec\_context\_in\_tmp\_dir* - Searches for shell\_exec\_t system shell SELinux context types in sys...