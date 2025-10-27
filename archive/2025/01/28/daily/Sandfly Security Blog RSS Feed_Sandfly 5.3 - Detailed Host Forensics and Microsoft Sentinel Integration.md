---
title: Sandfly 5.3 - Detailed Host Forensics and Microsoft Sentinel Integration
url: https://sandflysecurity.com/about-us/news/sandfly-5-3-detailed-host-forensics-and-microsoft-sentinel-integration/
source: Sandfly Security Blog RSS Feed
date: 2025-01-28
fetch_date: 2025-10-06T20:09:20.112760
---

# Sandfly 5.3 - Detailed Host Forensics and Microsoft Sentinel Integration

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.3 - Detailed Host Forensics and Microsoft Sentinel Integration

27 January 2025

Product Update

Sandfly 5.3.0 features a major UI overhaul with our new Linux host forensics and data views. We’ve not only brought critical host data front and center for rapid incident investigation, but expanded threat coverage, added in Microsoft Sentinel support, and increased performance across the board.

### Host-Centric Forensic and Data Views

A powerful feature of Sandfly is our ability to agentlessly collect a vast amount of Linux forensics and telemetry data on any system we monitor. Whether the system is a decade old, modern cloud, on-prem, or embedded, chances are very high that Sandfly can monitor it. With Sandfly 5.3 we are making this quality information visible with a new intuitive and fast host-centric view.

With host-centric views users can not only see alerts quickly, but other host operations such as processes running, users present, scheduled tasks, SSH keys, and more are also instantly available. Security teams investigating an incident now have immediate access to critical host details at their fingertips to make faster decisions about threats.

The new host view gives users a unified dashboard as seen below.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Host Details View](https://www.datocms-assets.com/56687/1737936577-host-details.png?auto=format&dpr=2&q=60&w=920 "Sandfly Host Details View")

Here are some examples of the data available to users under the unified host view.

#### Alerts with Layered Forensics

We have improved alert views by optimizing screen real estate and access to alert forensics.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Linux Alert View](https://www.datocms-assets.com/56687/1737936783-results-details.png?auto=format&dpr=2&q=60&w=920 "Sandfly Linux Alert View")

#### Processes

Teams can immediately see every process running on a system, who owns it, and related details.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Host Process View](https://www.datocms-assets.com/56687/1737936674-host-details-processes.png?auto=format&dpr=2&q=60&w=920 "Host Process View")

#### Network Listening Services

All listening network services are shown separately from the general process list to quickly spot potential threats running on a host.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux Process View](https://www.datocms-assets.com/56687/1737936688-host-details-listeners.png?auto=format&dpr=2&q=60&w=920 "Linux Process View")

#### Users and Attributes

All users, their login shells, password status, and more are instantly visible.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Active Linux Users View](https://www.datocms-assets.com/56687/1737936822-host-details-users.png?auto=format&dpr=2&q=60&w=920 "Active Linux Users View")

#### Kernel Modules

Active and inactive kernel modules can be reviewed instantly.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Active Linux Kernel Modules View](https://www.datocms-assets.com/56687/1737936853-host-details-kernel-modules.png?auto=format&dpr=2&q=60&w=920 "Active Linux Kernel Modules View")

#### SSH Keys, SSH Security Zones, and SSH User Data

SSH keys, users with keys, and SSH Security Zone status is immediately visible. Views into key access allows fast and easy identification of who is accessing a host.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux User SSH Key View](https://www.datocms-assets.com/56687/1737936870-host-details-ssh.png?auto=format&dpr=2&q=60&w=920 "Linux User SSH Key View")

#### Cron and Systemd Scheduled Tasks

Identify persistence risks in *crontab* and *systemd* with simple and easy scrolling of what they are running.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Scheduled Task View](https://www.datocms-assets.com/56687/1737937021-host-details-services.png?auto=format&dpr=2&q=60&w=920 "Scheduled Task View")

#### System Hardware and Drive Status

See CPU and drive status of all systems, even those without traditional system performance monitoring solutions.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Hardware and Drive Status](https://www.datocms-assets.com/56687/1737936896-host-details-hardware.png?auto=format&dpr=2&q=60&w=920 "Hardware and Drive Status")

### Support for LDAP and Active Directory Users

We now scan users authenticating to Linux systems using LDAP, Active Directory, and similar services. Users logging in without an account under traditional */etc/passwd* will have their directories and data scanned as if they were a local user. This means that threats present in remotely mounted home directories will be found, and SSH key data to track access to systems will also be indexed.

### Faster

Many speed increases have been made to our forensic engines and result ingestion pipelines. Speed increases of several hundreds of percent were achieved making result processing faster and on-host performance even lower impact than before.

### New Detections

We have added many detections to cover more Linux backdoors, rootkits, and suspicious process activity:

* Malicious */etc/motd* scripts.
* Wider backdoor persistence detection in system scripts and user profiles.
* New recon checks in critical directories such as *at jobs*, *crontabs*, boot areas, and kernel module configurations for drift detection.
* Checks for malicious, hidden, or suspicious XDG autostart files and directories.
* SUID or SGID shells operating on a host.
* Processes running with command line self exe references (e.g. /proc/self/exe).
* Malicious or suspicious backdoor references inside *systemd* units.
* SUID files under a user’s home directory.
* Shell masquerading with SUID or SGID root permissions.
* Processes running as SUID from a user's home directory.
* Cloaked directories under kernel module configuration areas (e.g. */etc/modules-load.d*).
* Expanded and optimized SSH private key search to find unencrypted or exposed keys.
* Detecting processes running as a file descriptor.
* Search inside compressed log files if desired by the user.
* Detect processes running with deleted process maps.
* Detect processes accessing memory space of themselves or another process.

### Microsoft Sentinel Integration

We have added *Microsoft Sentinel* integration so Sandfly alerts can be directly sent to the *Sentinel* platform. This capability goes alongside our existing support for *Splunk*, *Elastic*, and *syslog* for result replication in addition to our existing REST API methods.

Sandfly is able to access many more systems than traditional agents. The data we collect and export is extremely valuable and augments networks running agent-based solutions that often have large visibility gaps on Linux.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Microsoft Sentinel Sandfly Result Replication](https://www.datocms-assets.com/56687/1737937068-integration-ms-sentinel.png?auto=format&dpr=2&q=60&w=920 "Microsoft Sentinel Sandfly Result Replication")

#### Get a Free License Today

If you have not tried Sandfly, get your free license below:

[Get Sandfly](https://sandflysecurity.com/get-sandfly/)

#### Upgrading Sandfly

All customers are encouraged to upgrade to see our expanded host view and get a better handle on what their systems are running.

We are here to help with any questions. Please see our documentation on the new features and capabilities:

[Sandfly Documentation](https://docs.sandflysecurity.com)

Customers wishing to upgrade can follow the instructions here:

[Upgrading Sandfly](htt...