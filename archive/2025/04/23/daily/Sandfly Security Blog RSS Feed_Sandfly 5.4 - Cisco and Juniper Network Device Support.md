---
title: Sandfly 5.4 - Cisco and Juniper Network Device Support
url: https://sandflysecurity.com/about-us/news/sandfly-5-4-cisco-and-juniper-network-device-support/
source: Sandfly Security Blog RSS Feed
date: 2025-04-23
fetch_date: 2025-10-06T22:05:35.767789
---

# Sandfly 5.4 - Cisco and Juniper Network Device Support

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.4 - Cisco and Juniper Network Device Support

22 April 2025

Product Update

Sandfly 5.4 is introducing an industry-first new feature: Agentless EDR support for Cisco and Juniper networking gear. This new feature gives customers full Linux EDR coverage of these critical devices combined with Sandfly's proven speed, stability, and safety. Sandfly continues to have the widest Linux-based server, embedded, network appliance and device support in the industry.

In addition to protecting edge devices like Juniper and Cisco, Sandfly 5.4 has these new features as well:

* Webhook integrations for notifications to Slack and others.
* Threat feed integration for public and private hash databases.
* Expanded detection for Salt Typhoon Chinese nation-state tactics and related activity.

### Cisco and Juniper Network Device Support

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Juniper Evolved OS Detail View](https://www.datocms-assets.com/56687/1745358617-juniper-os-view.png?auto=format&dpr=2&q=60&w=920 "Juniper Evolved OS Detail View")

Juniper router detected and monitored by Sandfly

Sandfly's full functionality has been extended to routers and switches from Juniper and Cisco running Linux-based operating systems. This includes:

* Cisco [IOS XR](https://www.cisco.com/site/us/en/products/networking/software/ios-xr/index.html) network operating system for routers.
* Cisco Nexus [NX-OS](https://www.cisco.com/site/us/en/products/networking/cloud-networking/nx-os/index.html) data center operating system for switches and related hardware.
* Juniper [Evolved OS](https://www.juniper.net/us/en/products/network-operating-system/junos-evolved.html) for routers and switches.

Sandfly's full feature set is available to any of these devices we can access. This means customers running Cisco and Juniper network gear get the following:

* Full Linux EDR detection coverage from Sandfly.
* Drift detection for any unauthorized changes, new processes, new users, new SSH keys, or related alterations to the device.
* Full SSH key tracking and SSH Security Zone protections.
* Password auditing of existing user accounts to find weak and default passwords.
* Total device visibility into what processes it is running, network ports operating, users present, *systemd* services, kernel modules, and more.
* Custom threat hunting for incident response.
* Instant agentless coverage that is fast, safe, and stable that will not impact operations.

#### Salt Typhoon Threats

The recently disclosed attacks by Chinese nation state threat actors against telcos, dubbed Salt Typhoon, targeted critical networking gear from Cisco and Juniper. Once on these devices, the attackers can maintain persistence for extended periods and access extremely sensitive information about customers and network operations. The main reason they were able to persist for so long was because there was no effective way to monitor these devices before now.

Details of their attack patterns are available in several sources, but the main thrust of their attacks consisted of:

* Gain access to critical router and network switching gear through various exploits or stolen credentials.
* Maintain persistence using built-in mechanisms.
* Activating remote access through enabling SSH on alternate ports.
* Deploying backdoors for further stealthy access and persistence.
* Grabbing sensitive network traffic, such as unencrypted credentials, to move further into critical infrastructure.

#### Detecting Cisco and Juniper Threats

Sandfly's agentless security platform has EDR combined with drift detection. Both of these functions would make the actions of Salt Typhoon and others considerably more difficult.

For instance, our drift detection feature can be easily configured to lock down known-good profiles of devices and alert on any new process started, files changed, new users added and more. Our EDR can find threats running on systems, or as part of an incident response to check existing systems for signs of compromise. Finally, our ability to track SSH keys means new access added to devices can be seen immediately limiting lateral movement risks.

#### Configuring Cisco & Juniper Network Gear

Juniper and Cisco both have special requirements to enable Sandfly SSH access. Juniper Evolved OS requires a signed binary to run which is accomplished with the instructions below. Cisco equipment also requires configuration to allow SSH access along with other special considerations. Please see the documentation for more details:

[Cisco NX-OS Application Notes](https://docs.sandflysecurity.com/docs/notes-cisco-nx-os)

[Cisco IOS-XR Application Notes](https://docs.sandflysecurity.com/docs/notes-cisco-ios-xr)

[Juniper Evolved OS Application Notes](https://docs.sandflysecurity.com/docs/notes-junos-evolved)

### Slack and Other Webhook Notifications

We have added in webhook support to send alerts to applications like Slack and others. The new notifications allow you to customize alert templates for other platforms as well. Webhook activation can be done by following the below instructions:

[Activating Webhooks](https://docs.sandflysecurity.com/docs/adding-webhook-notifications)

### Threat Feeds

Sandfly can now access a list of hashes for known Linux malware from places such as Malware Bazaar, and other threat feeds. The hash lists will alert on any of the following:

* Process hash matches
* File hash matches
* SSH key hash matches

The threat feed feature can also pull from a custom list of hashes maintained by security teams at a URL provided by the customer.

Threat feeds can be added by following our documentation below:

[Threat Feed Configuration](https://docs.sandflysecurity.com/docs/threat-feeds-ui)

### Expanded Tactics Detection

We expanded coverage to make a broader net for tactics used by Salt Typhoon plus other new threats. The new detections find more backdoor activity, suspicious processes, unusual network processes and related exploits. This expands our already extensive industry-leading Linux coverage. The new detections feature some of the following:

* *process\_injector\_memfd\_\*\_network\_operating* - New detections to find network processes running from *memfd* sockets as used by fileless malware backdoors.
* *process\_masquerade\_cmdline\_overwrite*  - Detects binary masquerading techniques that overwrite the command line used to start the process with an imposter name.
* *policy\_process\_ssh\_port\_non\_standard\_tcp\_port* - Finds SSH daemons running on non-standard ports (e.g. not TCP port 22).

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Tinyshell Backdoor Detected](https://www.datocms-assets.com/56687/1745346762-tinyshell-backdoor.png?auto=format&dpr=2&q=60&w=920 "Tinyshell Backdoor Detected")

* *process\_backdoor\_bindshell\_login\_mode* - Finds system shells being used in login mode commonly associated with backdoor activity.
* *process\_backdoor\_bindshell\_interactive\_mode* - Finds system shells being used in interactive mode commonly associated with backdoor activity.
* *process\_backdoor\_bindshell\_pseudo\_master* - Finds suspicious use of the Linux pseudo terminal master/slave commonly seen with backdoor activity.
* *process\_backdoor\_bindshell\_parent\_static\_binary* - Looks for shells spawned by statically built network process binaries commonly seen with backdoor activity.
* *process\_masquerade\_sshd* - Finds SSH daemon processes running under another name to hide their presence.
* *process\_running\_ping\_sweep\_operating*  - Finds signs that a ping sweep process is being run on the system.
* *process\_running\_port\_scanner\_operating\_nmap* - Finds instances of...