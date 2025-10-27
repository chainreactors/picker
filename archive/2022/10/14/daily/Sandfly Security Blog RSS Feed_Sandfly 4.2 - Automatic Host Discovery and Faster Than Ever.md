---
title: Sandfly 4.2 - Automatic Host Discovery and Faster Than Ever
url: https://www.sandflysecurity.com/blog/sandfly-4-2-automatic-host-discovery-and-faster-than-ever
source: Sandfly Security Blog RSS Feed
date: 2022-10-14
fetch_date: 2025-10-03T19:49:13.288583
---

# Sandfly 4.2 - Automatic Host Discovery and Faster Than Ever

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 4.2 - Automatic Host Discovery and Faster Than Ever

13 October 2022

Product Update

Sandfly 4.2 has been released and features a new automatic host discovery for cloud and DHCP environments. Plus, it has been significantly optimized to be more than twice as fast with lower CPU usage.

In addition to this, we have many other upgrades:

* [SSH Hunter](https://www.sandflysecurity.com/platform/ssh-credential-security/) has more details on keys no longer present on any host (dead keys).
* Improved container process data collection and detection.
* New SSH *known\_hosts* detection and collection.
* New sudoers persistence and upgraded security checks.
* Improved scheduler tagging and bulk operations.
* Generation of SSH keys inside UI to secure private key from operators.
* TLS configuration and custom signed certificate options.

## Automatic Host Discovery

Being agentless means Sandfly can rapidly deploy against a wide range of Linux systems without leaving anything running on the endpoints. We now make this easier than ever with our new ability to automatically find and add hosts to Sandfly using [Discovery Scans](https://support.sandflysecurity.com/support/solutions/articles/72000574831).

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Automatically find and secure Linux hosts with Sandfly.](https://www.datocms-assets.com/56687/1665618251-discover-scan.png?auto=format&dpr=2&q=60&w=920 "Sandfly Discovery Scan")

A Discovery Scan can take either a pre-defined list of addresses, or multiple netblocks of your choice. They can be located at a cloud provider, or internally. Once added, Sandfly will automatically scan those ranges for any new hosts. If a new host is found, we will attempt to add it to the protected host list automatically.

Discovery Scans enable the following use cases:

* Automatically monitor a DHCP address pool for new Linux hosts.
* Secure address ranges and dynamic workloads at your cloud provider.
* Find new hosts that may have appeared on your network which are unauthorized.

This new feature significantly expands the ability of Sandfly to discover, track, scan and secure Linux assets. In-depth documentation on how to use the Discovery Scan feature is available here:

[Discovery Scans](https://support.sandflysecurity.com/support/solutions/articles/72000574831)

## Automatic Offline Host Removal

To compliment the automatic host discovery, we have added a feature to remove hosts that have been offline for a user-defined time period. This feature means you can have a dynamic pool range that is automatically maintained without any intervention. New hosts are added with Discovery Scans, and if they go away they are removed from the active pool making that slot available to any new hosts that show up again.

This feature is configurable in the scheduled scans area and can be applied to a range of hosts by tag so you can have different expiration times for different tag groups.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Automatically delete offline hosts.](https://www.datocms-assets.com/56687/1665618735-automatic-host-maintenance-removal.png?auto=format&dpr=2&q=60&w=920 "Automatically delete offline hosts.")

More information on configuring security scans is available here:

[Security Scans](https://support.sandflysecurity.com/support/solutions/articles/72000079050-adding-schedule)

## Optimized Forensic Engines Twice as Fast

We have further optimized our forensic engines so that they are at least twice as fast for many scanning operations. Customers will see scans complete much faster with even lower CPU and RAM impacts.

## SSH Dead Key Monitoring

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH Dead Key Explorer View](https://www.datocms-assets.com/56687/1665623866-ssh-dead-key-full-view.png?auto=format&dpr=2&q=60&w=920 "SSH Dead Key Explorer View")

SSH Hunter has new columns to show additional key information, including tracking of dead keys (keys that were seen at one time, but are now not visible on any hosts). If these keys come active again they will return to the active state. The SSH Hunter timeline will show all periods we first saw the key until it returned.

## Improved Container Threat Detection

We have improved detection of threats inside containers to provide expanded coverage of Docker and Podman platforms. Sandfly will search for more container types and search for process, file, directory and other threats both on the host OS and inside containers that it is running.

## SSH *known\_hosts* Tracking

We are now tracking user's SSH *known\_hosts* files to give administrators more insight into how they are being used and potentially abused.

SSH *known\_hosts* data is attached to all user forensic data we see on the host. This includes parsing out the fields into relevant blocks for quick analysis and review. The excerpt below shows unmasked SSH *known\_hosts* entries available in the raw forensic data view.

`{
 "known_hosts": {
 "data": [{
 "path": "/home/system/.ssh/known_hosts",
 "type": "ssh-ed25519",
 "entry": "10.1.1.10 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIXASDFASDFASDFASDFASDF/PZsEDAJOK5CkKUZBm2ija",
 "marker": "",
 "masked": false,
 "revoked": false,
 "entry_num": 1,
 "hostnames": [{
 "port": 22,
 "hostname": "10.1.1.10"
 }],
 "public_key": "AAAAC3NzaC1lZDI1NTE5AAAAIIXASDFASDFASDFASDFASDF/PZsEDAJOK5CkKUZBm2ija",
 "masked_salt": "",
 "masked_value": "",
 "cert_authority": false
 },
 {
 "path": "/home/system/.ssh/known_hosts",
 "type": "ssh-ed25519",
 "entry": "10.1.1.16 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIADFASDFASDFASDFASDFASDFASDF/QK52K",
 "marker": "",
 "masked": false,
 "revoked": false,
 "entry_num": 2,
 "hostnames": [{
 "port": 22,
 "hostname": "10.1.1.16"
 }],
 "public_key": "AAAAC3NzaC1lZDI1NTE5AAAAIADFASDFASDFASDFASDFASDFASDF/QK52K",
 "masked_salt": "",
 "masked_value": "",
 "cert_authority": false
 }
 ]
 }
}`

This data can be ingested into your SIEM for further tracking, but Sandfly also has detections for problems of its own as discussed below.

## Unmasked SSH *known\_hosts* Entries

We can alert you to users with unmasked SSH *known\_hosts* entries with a new policy check. Unmasked SSH entries leak connection information and allow intruders an immediate list of systems to attack if it is available. Linux malware often will search for *known\_hosts* files to harvest IP addresses as part of their automated attack sequence.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Unmasked SSH known_hosts detected on Linux.](https://www.datocms-assets.com/56687/1665623170-policy_user_ssh_known_hosts_unmasked.png?auto=format&dpr=2&q=60&w=920 "Unmasked SSH known_hosts detected on Linux.")

## Detecting if SSH *known\_hosts* is Present

One less obvious use for searching for *known\_hosts* files is to let you know if one is present. If you are running a group of servers that should never have users that are doing SSH outbound, it is useful to know if a user has tried it and left a *known\_hosts* file behind. This alerts you to suspicious SSH activity inside perimeters that may have evaded network monitoring.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH known_hosts file found on suspicious user.](https://www.datocms-assets.com/56687/1665623377-policy_user_ssh_known_hosts_filename_present.png?auto=format&dpr=2&q=60&w=920 "SSH known_hosts file found on suspicious user.")

## Sudoer Persistence and Other Threat Detection Improvements

We have added in modules to find new methods for persistence in */etc/sudoers* files and more. Other updates to existing threat hunting modules to expand coverage and reliability have been mad...