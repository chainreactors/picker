---
title: Sandfly 5.1 - Introducing SSH Security Zones
url: https://sandflysecurity.com/about-us/news/sandfly-5-1-introducing-ssh-security-zones
source: Sandfly Security Blog RSS Feed
date: 2024-07-17
fetch_date: 2025-10-06T17:41:15.700472
---

# Sandfly 5.1 - Introducing SSH Security Zones

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.1 - Introducing SSH Security Zones

16 July 2024

Product Update

Sandfly 5.1 introduces SSH Security Zones to our powerful agentless security platform for Linux.

SSH Security Zones allow administrators to setup secure areas where authorized SSH keys are allowed to operate. Unauthorized keys appearing in these zones are instantly identified to quickly spot lateral movement and access risks. We've also expanded our ability to detect SSH key problems such as unencrypted private keys and weak keys.

In addition to this, we have added a large number of new Linux threat detection modules covering stealth rootkit activity and *systemd* attack vectors, plus more.

### SSH Security Zones

SSH Security Zones allow customers to track and alert on SSH key use and abuse.

SSH *authorized\_keys* files are notoriously difficult to manage. They frequently contain too many keys, old keys, orphaned keys, and can hide malicious keys used by intruders to maintain persistent access.

Unauthorized SSH keys show up in a variety of ways:

* Users add keys to their accounts that are not permitted
* Old keys remain for years and can be activated again if discovered by attackers during reconnaissance of a network
* Malware or intruders can drop a backdoor key on a system
* A system is restored and the backup had an old key that gets put back into service by accident
* Automated management puts keys where they shouldn't belong or does not remove keys properly

SSH key management is a significant threat and companies need a way to get a handle on how they are being used. Sandfly's SSH Security Zone feature does exactly this.

You can read more about SSH Security Zone operation in our documentation:

[SSH Security Documentation](https://docs.sandflysecurity.com/docs/ssh-hunter-ui)

### Monitor Keys with SSH Security Zones

SSH Security Zones allow customers to define areas where only certain keys are allowed to exist. For instance, customers may have an SSH Security Zone for production systems.

The production zone can be locked down to a very specific number of SSH keys that can operate on those systems. If a new key were to show up on any of those hosts, an alert is generated to allow security teams to investigate and respond.

Below we see an alert when a new key shows up for a user in a monitored zone.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH Security Zone Violation](https://www.datocms-assets.com/56687/1721096022-ssh-host-violation-view.png?auto=format&dpr=2&q=60&w=920 "SSH Security Zone Violation")

Customers can setup any number of zones to track what keys are being used for authentication, who is using them, and know if new keys have migrated into protected areas. Sandfly can track keys across cloud, on-premises, embedded, and even systems up to 10+ years old.

### Watch a Demo

Watch as Sandfly founder Craig Rowland goes over how fast and easy it is to setup a security zone for your SSH keys.

### Instantly Ban SSH Keys

Another problem security teams run into are finding and tracking keys that should no longer be used, or are part of an incident and need to be identified. With Sandfly, customers can mark keys as *banned* and we will alert if we see them on any system. This even works if the key is completely removed from your hosts, but shows up again in the future (such as being restored off a backup image).

Banned keys show up regardless of whether they are in a security zone or not. If we see them anywhereyou will get an alert.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly alert detail page showing a list of SSH keys found across a system where one is banned.](https://www.datocms-assets.com/56687/1721111454-screenshot-2024-07-16-at-6-29-40-pm.png?auto=format&dpr=2&q=60&w=920 "Sandfly alert detail page showing a list of SSH keys found across a system where one is banned.")

### Unencrypted Private SSH Keys

Unencrypted SSH private keys are a major risk. Responding to customer requests, we have added the ability to spot SSH private keys that are unencrypted.

Attackers that compromise a system frequently search for private keys to press lateral movement attacks. Unencrypted private keys make an attacker's job a lot easier. Sandfly helps you find these risky keys before attackers do.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Unencrypted SSH Private Key Detected](https://www.datocms-assets.com/56687/1721111715-alert-unencrypted-key.png?auto=format&dpr=2&q=60&w=920 "Unencrypted SSH Private Key Detected")

In addition to searching user home directories for unencrypted keys, Sandfly will search system */tmp* and */dev/shm* ramdisk directories for keys that may have been left there. Keys in these areas can be left by accident, by automated administration tools (our customers have seen this), or maliciously by an attacker that forgot to clean up their activity after compromise.

Finally, we have incident response sandfly modules that can search the entire file system of a suspect system for unencrypted private keys. This is valuable during an incident investigation to find suspicious keys, or to find keys that could have been found by an attacker and are now compromised and need to be removed.

### Weak SSH Keys

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Weak SSH RSA Key Detected](https://www.datocms-assets.com/56687/1721114201-alert-weak-rsa.png?auto=format&dpr=2&q=60&w=920 "Weak SSH RSA Key Detected")

Last on our SSH key threats, we have weak keys. Weak keys are considered to be RSA of 1024 bits or less and are deprecated in SSH now. Older SSH installations can contain weak keys and these can open the door to advanced adversaries that have the technical capabilities to break them. Sandfly will identify and alert on weak keys we find, this includes embedded and legacy systems that are often exposed to this risk due to their age and lack of updates.

### New Detection Modules

In addition to our new SSH capabilities, we have added a number of new detection modules to expand our threat coverage on Linux. The new modules cover stealth rootkit techniques plus more. Some of the new modules include:

* **process\_shell\_running\_empty\_file\_descriptors\_command\_mode** - Processes running with empty file descriptors (stealth rootkit spawned)
* **process\_environ\_proc\_home\_dir** - Suspicious home directory location in process environment
* **systemd\_exec\_args\_base64** - Looks for systemd units that contain base64 encoded data to obfuscate entries
* **user\_history\_as\_directory** - User's history file is really a directory (detection evasion)
* **systemd\_exec\_args\_obfuscation -** Looks for *systemd* units that are using commands that obfuscate data
* **systemd\_exec\_args\_malicious** - Looks for systemd units that have indications of suspicious or malicious use
* **systemd\_exec\_args\_shell\_execution** -Looks for systemd units that executes another shell via the command (-c) mode (likely backdoor)
* **process\_shell\_running\_kthread\_spawned\_command\_mode** - Looks for shell processes in command (-c) mode started by the kthread process (stealth rootkit backdoor)
* **policy\_cpu\_load15\_high** - High system load 15 minute values (finds overloaded systems or systems with suspiciously high CPU activity)
* **SSH Key checks -** Unencrypted keys in user home directories, unencrypted keys anywhere (for incident response), weak keys, keys in suspicious locations like */tmp* or */dev/shm*
* **Containerized Flag** - Sandfly syntax recognizes the *containerized* flag to create modules that only apply to containers, or ignores containers as required

In addition to the above, we h...