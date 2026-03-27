---
title: Sandfly 5.7 - Performance Upgrade
url: https://sandflysecurity.com/blog/sandfly-57-performance-upgrade
source: Sandfly Security Blog RSS Feed
date: 2026-03-26
fetch_date: 2026-03-27T04:31:33.540722
---

# Sandfly 5.7 - Performance Upgrade

[Press Release - Ericsson Partners with Sandfly. See Details](/blog/ericsson-partners-with-sandfly-to-strengthen-telecom-security)

[Partners](/partners)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.7 - Performance Upgrade

26 March 2026

Product Update

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![](https://www.datocms-assets.com/56687/1774486183-5-7-thumbnail-no-logo.png?auto=format&dpr=2&q=60&w=920)

Speed and visibility are everything during a security investigation. With the release of Sandfly 5.7, we’ve drastically reduced scan times, expanded our threat detection to catch stealthy backdoors, and made it easier than ever to scale your Linux forensics.

### Faster Scans with Lower System Impact

While Sandfly has always been known as being high performance with low system impacts, we are always looking to improve our agentless technology. With Sandfly 5.7 we have carefully reviewed our scanning engines for performance bottlenecks and have increased scan speeds by 50% or more. This has resulted in less time running on a host, less memory used when running, and lower impacts during scans.

The performance boost affects most of our scanning process. While you may not see it yourself, know that under the covers significant speedups were made where it counts to ensure Linux forensics data is collected more quickly and accurately than ever.

### Cross File System Mount Scan Blocking

We now have checks to prevent crossing file system mounts such as NFS. This prevents Sandfly from scanning potentially slow network links on remotely mounted file systems which can cause the scan to time out waiting for data. This feature can be disabled on custom sandflies for customers that want to maintain scanning across mount points.

### Scale Securely with SSH Jump Host Enhancements

For customers running Sandfly across jump hosts, we have made big improvements to how they are handled, resulting in large performance gains here as well. A single jump host can now carry many more connections without overloading and scan times have been dropped dramatically when doing large host count scanning behind jump hosts.

### Drift Detection for Firewall Configurations

We have added a new reconnaissance module **recon\_file\_attributes\_in\_etc\_firewall** which is disabled by default, but provides a mechanism for customers to enable and start capturing file attributes for critical firewall configuration areas. This module would be useful for those using our [agentless drift detection feature](https://sandflysecurity.com/platform/drift-detection) to find firewall rules that may have been modified on disk. This means if an attacker silently alters a firewall rule to open a backdoor port, you'll know immediately.

### Login UID Attack Detection

Linux provides a process value called **loginuid** which is the User ID (UID) of the original owner that started a process. This value will remain set to the original owner even if the process forks or is taken over by the *systemd* process (PID 1) if a user logs out and keeps the binary running.

Why should you care? Well, it means that if someone starts a malicious process on a host and it changes owner to *root* (or any other user), the *loginuid* will show the UID of the user that originally started it. This means security teams can find out what user initially started a binary even if it is masked by how it was spawned on the host.

For example, the webserver spawns an attack that pivots to *root*. The *loginuid* value will show the process was started by the webserver, and not *root.* This helps investigators rapidly get to the bottom of where and how an intrusion may have happened.

We have leveraged this to add several new detections as well:

**process\_backdoor\_shell\_no\_loginuid\_network** - Looks for shell processes with no audit login trail (login UID unset) that have active network connections. These are typically bind shell backdoors trying to hide who or what started them.

**process\_deleted\_loginuid\_set** - Looks for processes with deleted binaries that were started by a logged-in user (login UID set). These are processes likely started by an interactive session that then deleted the process binary from disk to hide evidence.

**process\_deleted\_root\_loginuid\_nonroot** - Looks for deleted binaries running as root where the audit login UID shows a non-root user originally authenticated. Typically it's a non-root user starting a process and then removing it from the disk after privilege escalation to hide.

**process\_running\_hidden\_loginuid\_set** - Looks for hidden processes that have a valid audit login UID set. Generally spawned processes from stealth rootkits.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux backdoor process with loginuid missing.](https://www.datocms-assets.com/56687/1774484704-process_backdoor_shell_no_loginuid_network.png?auto=format&dpr=2&q=60&w=920 "Linux backdoor process with loginuid missing.")

### ICMP Backdoor Detection Expanded

We expanded our ability to spot ICMP backdoors, including more magic packet type variants. New detections were added to spot the raw ICMP port activity that is suspicious. This builds upon our other detections that find sniffing and raw socket malware backdoor activity across multiple protocols.

### 100,000 Host and Result Views

To support larger Sandfly deployments, we have enhanced the UI to allow listing 100,000 hosts and results at a time. Customers can select view sizes at the bottom of the Hosts and Result screens.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly can show 100,000 results or hosts at a time.](https://www.datocms-assets.com/56687/1774481600-host-view-limit.png?auto=format&dpr=2&q=60&w=920 "Sandfly can show 100,000 results or hosts at a time.")

### Richer Syslog Integration for Better Alerting

We have added the ability to send not just alerts like we have in the past, but also error and audit log events to *syslog*. We also enabled the ability to set facility values for customers that manage log data using them.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly syslog improvements.](https://www.datocms-assets.com/56687/1774481871-syslog-config.png?auto=format&dpr=2&q=60&w=920 "Sandfly syslog improvements.")

### Server Config Updates

We have consolidated and improved our server configurations page. All server settings are better organized and visible to admins.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly server config updates.](https://www.datocms-assets.com/56687/1774481917-server-settings.png?auto=format&dpr=2&q=60&w=920 "Sandfly server config updates.")

### AI Analyst LLM Support For Claude

We have added Anthropic's Claude AI LLM support along with existing OpenAI, Google Gemini, xAI, Digital Ocean, and OpenAI API compatible settings.

We are vendor-agnostic when it comes to AI LLMs and find that all the frontier LLM systems work pretty well. Use what your organization provides and our accurate forensics data will give you good results. You can even use on-prem models with the OpenAI API-compatible setting which works well with *Ollama* and other local model hosting platforms.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![](https://www.datocms-assets.com/56687/1774482030-claud-api-support.png?auto=format&dpr=2&q=60&w=920)

### Sandfly 5.7 Performance

Whether you are hunting for stealthy rootkits or managing security across 100,000 nodes, Sandfly 5.7 gives you the speed and visibility you need without the burden of endpoint agents.

Please see our documentation on the new features and capabilities:

[Sandfly Documentation →](https://docs.sandflysecurity.com/)

Customers wishing to upgrade can follow the instructions here:

[Upgrading Sandfly →](https://docs.sandflysecurity.com/docs/upg...