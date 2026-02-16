---
title: BPFDoor Detection, Analysis, and Hunting Tactics on Linux
url: https://sandflysecurity.com/blog/bpfdoor-detection-analysis-and-hunting-tactics-on-linux
source: Sandfly Security Blog RSS Feed
date: 2026-02-15
fetch_date: 2026-02-16T04:18:22.155185
---

# BPFDoor Detection, Analysis, and Hunting Tactics on Linux

[5.6 Released - Game Changing Automatic Drift Detection. See Details](/blog/sandfly-5-6-automatic-drift-detection)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# BPFDoor Detection, Analysis, and Hunting Tactics on Linux

15 February 2026

Malware

### BPFDoor Introduction

BPFDoor is a simple but stealthy Linux backdoor linked to Chinese nation state threat actors. While often found targeting telecommunications infrastructure, it is likely used in other critical infrastructure breaches around the world. This document details detection of BPFDoor versions 1 and 2 by Sandfly Security’s agentless intrusion detection and incident response platform.

We **strongly urge** customers to let Sandfly do agentless hunts for this threat to avoid missing any compromised systems. Sandfly works across nearly all Linux distributions including modern systems, 10+ year old legacy systems, and even embedded devices without deploying endpoint agents. Sandfly can find BPFDoor in seconds saving countless hours of time using risky scripts and manual work.

### BPFDoor Technical Overview

The original BPFDoor has existed for some time and was able to remain unnoticed due to the low-key nature of how it worked and the lack of monitoring on most Linux systems. Sandfly wrote an in-depth technical overview of BPFDoor back in 2022. The complete technical breakdown of what it did is outlined in our original research below:

[BPFDoor - An Evasive Linux Backdoor Technical Analysis](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis)

We also made a video presentation about the operation of this backdoor along with slides:

[BPFDoor Presentation](https://sandflysecurity.com/blog/evasive-linux-malware-detection-video-presentation-bpfdoor)

[BPFDoor Slides](https://sandflysecurity.com/sharing/evasive-linux-backdoors-cold-incident-response-conference-2023.pdf)

The above analysis covered Version 1 of this backdoor. Version 2 of BPFDoor was recently discussed by Haxrob in his two part blog:

[BPFDoor - Part 1 The Past](https://haxrob.net/bpfdoor-past-and-present-part-1/)

[BPFDoor - Part 2 The Present](https://haxrob.net/bpfdoor-past-and-present-part-2/)

The two backdoors have largely similar functions with changes to evade some detection in the Version 2 variants. The main change for Version 2 is that the new versions incorporate much stronger public/private key encryption. The new version’s stronger encryption prevents network monitoring and also unauthorized use by anyone except the operators that installed it.

### BPFDoor Basic Operation

BPFDoor waits for a “magic packet” to arrive on any port of the victim system once installed. The magic packet is a specially crafted network packet on the TCP, UDP or ICMP protocols that contains a string sequence and password to activate the backdoor. Without any magic packet received, the backdoor sits quietly using negligible system resources to not draw any attention to itself.

Once a magic packet is seen by the backdoor, it will reconfigure the local firewall to either start a bind shell backdoor that the attacker then connects to, or start a reverse shell back to the attacker. More critically, the attacker can communicate on the port it sent the original packet on. Meaning that if the victim is running a webserver on port 443 with encrypted traffic, the attacker can send a packet to port 443 and start an encrypted backdoor session to blend in with other traffic. Any port can be used in this way.

The important thing to understand is that it **does not matter** if the system has a local firewall configured to drop unauthorized packets. The backdoor will intercept the packets before the firewall has dropped them and activate. The firewall will not prevent the backdoor from activating once it sees a packet.

The above point is significant because a system that operators think is protected against unauthorized traffic by a firewall can in fact be accessed. The diagram below shows the basic operation of this mechanism for the bind shell backdoor from Version 1. If a reverse shell is requested instead of a bind shell, the backdoor will initiate a connection potentially bypassing packet filters that do not restrict traffic outbound.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![BPFDoor Firewall Redirect/Bypass](https://www.datocms-assets.com/56687/1652238177-firewall-redirect-diagram.png?auto=format&dpr=2&q=60&w=920 "BPFDoor Firewall Redirect/Bypass")

In both cases, the attacker can hit any open or closed port and cause the backdoor to activate. The attacker can hit an open port, such as a webserver, to blend into normal traffic. Or, they can hit a closed port that may not be monitored and get access that way.

### Detecting BPFDoor

BPFDoor is a simple but effective backdoor because it limits its features to the bare minimum for the job, and incorporates simple hiding methods that are reliable across Linux distributions. However, it has several attributes that lend itself to reliable detection:

1. It is sniffing network traffic.
2. It masquerades the process name to hide.
3. It utilizes anti-forensics to conceal activity.
4. It launches command shells in suspicious or unusual ways.

We’re going to now show you how Sandfly finds the above in all known variants of this backdoor.

### Sandfly BPFDoor Alerts

Sandfly focuses on the tactics of compromise which makes our detection on Linux more versatile than standard malware signatures. In the case of BPFDoor, we do not try to identify it directly. Instead, we find the tactics of how it works which makes it obvious something serious is happening on the targeted system.

For example, we have Version 1 and 2 of BPFDoor operating on victim hosts. This is what Sandfly alerts on when the backdoor is running but idle (e.g. not running an active shell yet).

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![BPFDoor Version 1 Alerts](https://www.datocms-assets.com/56687/1771182666-bpfdoorv1-alerts.png?auto=format&dpr=2&q=60&w=920 "BPFDoor Version 1 Alerts")

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![BPFDoor Version 2 Alerts](https://www.datocms-assets.com/56687/1771182702-bpfdoorv2-alerts.png?auto=format&dpr=2&q=60&w=920 "BPFDoor Version 2 Alerts")

BPFDoor has many significant and serious alerts when idle:

**process\_running\_from\_dev\_dir** - A process running from */dev* directory.

**process\_deleted** - A process with a deleted binary has been detected on the host.

**process\_running\_sniffer\_environ\_empty** - A network sniffing process is missing its environment.

**process\_running\_sniffer\_environ\_corrupt** - A network sniffing process has a corrupt environment.

**process\_running\_sniffer\_operating\_deleted** - A process binary that is sniffing traffic has been deleted from the disk.

**process\_running\_sniffer\_operating\_ipv4\_traffic** - A process is grabbing all IPv4 traffic.

**process\_stack\_packet\_sniffer** - A process with evidence it is operating as a sniffer in the stack has been detected.

**process\_running\_sniffer\_cmdline\_overwrite** - A process with a suspicious command line has been detected.

**recon\_process\_list\_all** - Drift detection has found a new process that is not authorized to be running on this host.

**recon\_process\_list\_sniffer\_operating** - Drift detection has found a new process that is sniffing network traffic running on this host.

**process\_threat\_feed\_match** - A known malware binary hash from a threat feed has been found operating on this host.

### Suspicious Process Paths

The detection *process\_running\_from\_dev\_dir* is related to a series of checks Sandfly does to find processes that are running from suspicious locations on Linux. In general, Linux processes tend to run from system areas such as */bin*, */usr/bin*, or u...