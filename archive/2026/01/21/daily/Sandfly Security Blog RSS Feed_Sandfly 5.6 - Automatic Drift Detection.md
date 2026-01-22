---
title: Sandfly 5.6 - Automatic Drift Detection
url: https://sandflysecurity.com/blog/sandfly-5-6-automatic-drift-detection
source: Sandfly Security Blog RSS Feed
date: 2026-01-21
fetch_date: 2026-01-22T03:34:52.601263
---

# Sandfly 5.6 - Automatic Drift Detection

[New White Paper on the Advantages of Agentless EDR for Linux. Learn More](/blog/the-advantages-of-agentless-edr-for-linux-white-paper)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.6 - Automatic Drift Detection

21 January 2026

Product Update

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![](https://www.datocms-assets.com/56687/1768949771-5-6-thumbnail-alt-web.png?auto=format&dpr=2&q=60&w=920)

Sandfly 5.6 has been released with major updates to our powerful agentless drift detection for Linux. This is a significant upgrade in ease of use and detection for novel threats and attacks against Linux. The update also includes major UI improvements making it faster and more user friendly.

### Automatic Agentless Drift Detection (Auto-Drift)

Sandfly introduced our [novel and powerful agentless drift detection](https://sandflysecurity.com/platform/drift-detection) feature last year. This allows security teams to find any kind of process or system drift against any host we monitor. New processes, users, systemd services, kernel modules, and more can be instantly spotted, protecting hosts from advanced attacks, or even accidental changes.

We have dramatically improved the usability and power of this feature with our new automatic drift detection capability. This is highlighted in our new video demonstrating the feature.

With automatic drift detection, security teams can establish drift profiles in three easy steps:

**1) Select the model host that you wish to use to build a drift profile.**

The model hosts can be a gold image isolated system, a fresh system build, deployed systems, or embedded devices you wish to monitor for any changes.

**2) Setup auto-drift to monitor the system for a period of time to gather data.**

During this time Sandfly will collect usage information from the system and automatically build a profile of processes, users, files and other activity to be monitored for change on the host. We will also automatically whitelist alerts during this process so tuning is completed for you.

**3) When the initial profile gathering is completed, the drift profile is automatically applied to tagged hosts and scheduled threat detection begins.**

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Auto Drift Detection Wizard](https://www.datocms-assets.com/56687/1768877647-sandfly5-6-drift-wizard.png?auto=format&dpr=2&q=60&w=920 "Auto Drift Detection Wizard")

#### Auto-Drift Default Profiles

Drift detection includes a built-in list of pre-defined profiles we recommend to use based on the types of systems customers are looking to protect. For instance, customers can select embedded devices for our recommendations for those platforms. Customers can also select detection modules to customize exactly what they want to monitor on their hosts.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Drift Detection Profiles](https://www.datocms-assets.com/56687/1768877341-sandfly-5-6-drift-profile-types.png?auto=format&dpr=2&q=60&w=920 "Drift Detection Profiles")

#### Auto-Drift Whitelisting

In addition to change detection with auto-drift, Sandfly will also automatically whitelist any alerts on model hosts to alleviate manual tuning of alerts. Once the gather period completes, alerts are automatically dealt with without any user intervention when new hosts are added to the drift profile.

#### Auto-Drift Container Escape Detection

Auto-drift also has the ability to ignore containerized processes on a host. This is a perfect solution for monitoring systems that are managing a wide range of constantly changing container workloads. Teams that want to make sure the host OS is not altered due to a container escape attack now have a powerful feature to do that.

#### Auto-Drift Profile Editing

A frequently requested feature is the ability to edit drift profiles. We now allow users to edit the profiles and remove unwanted sandfly modules and tune what was whitelisted.

### New Linux Threat Detections

We have added to our already large Linux attack detection with more threat coverage and improvements such as the ones below.

#### Enhanced Stealth Process and Kernel Module Hiding

We have expanded the ability to detect new ways of Loadable Kernel Module (LKM) hiding for Linux stealth rootkits. We also enhanced our ability to decloak processes being hidden by LKM rootkits.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux Stealth Rootkit Detection](https://www.datocms-assets.com/56687/1768879660-sandfly5-6-vmalloc-artifact.png?auto=format&dpr=2&q=60&w=920 "Linux Stealth Rootkit Detection")

#### Process and File Capabilities

Sandfly now decodes process and file capabilities. These attributes can be built into rules to help teams find suspicious file or process activity involving rogue capabilities such as CAP\_SETUID to bypass traditional *setuid* (SUID) file system flags. We have upgraded our SUID file checks to look for file capabilities which can hide privileged binaries from discovery.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux CAP_SETUID Capabilities Detection](https://www.datocms-assets.com/56687/1768879208-sandfly-5-6-setcap.png?auto=format&dpr=2&q=60&w=920 "Linux CAP_SETUID Capabilities Detection")

#### SNMP Common Community String

Abuse of common SNMP community strings is still common, especially on network devices. Sandfly will now look for common SNMP community names and warn you about them. We will also warn you about insecure SNMP versions in use.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Vulnerable SNMP Community String Detection](https://www.datocms-assets.com/56687/1768879856-sandfly5-6-snmpd-community-string.png?auto=format&dpr=2&q=60&w=920 "Vulnerable SNMP Community String Detection")

#### Other New Detections

We have continued to add many more Linux threats Sandfly can detect to provide customers with the most thorough coverage for Linux. Other threat modules that are new or updated include:

* **SSH Invalid Key Data Detected** - Finds SSH keys that have invalid data indicating corruption or possibly hidden data inside *authorized\_keys* files.
* **Kernel Address Space Layout Randomization (ASLR) Disabled** - Looks for kernels where ASLR has been deliberately disabled enabling wider attack surface.
* **Policy User Credential Leak** - Finds users with files that could expose unencrypted credentials.
* **Recon File Attributes SSH Config** - Specifically monitors SSH server config files for changes for drift detection.
* **Password Auditor List Upgrades** - Expanded default password coverage for multiple network devices and passwords.
* **Process Anomalies** - Zero epoch processes, corrupted environments, and more.
* **Enhanced Port Scanner Detection** - Expanded port scanner and raw packet operation detection on host.

### Embedded Device Dropbear SSH and Enhanced ARM Support

We have extended coverage to devices using the Dropbear SSH service and more ARM processors. This mainly applies to embedded devices and allows us to cover a wider range of IoT systems than before. These updates extend Sandfly's agentless monitoring which continues to offer the absolute widest and safest coverage of Linux in the industry.

### Major UI Upgrades

We have made significant overhauls to the UI to make it more usable and faster. Many new updates have been made for usability, clearer display of forensic data, improved workflow, and much more. The UI enhancements include a variety of tweaks to make information more visible and a faster response.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Enhanced UI](https://www.datocms-assets.com/56687/1768881289-sandfly-5-6-alert-screen.png?auto=format&dpr=2&q=60&w=920 "Sandfly Enhanced UI")

### Sandfly 5.6 Offers Powerful New Features

S...