---
title: MITM on wired 802.1x with a Raspberry PI
url: https://www.adainese.it/blog/2024/03/10/mitm-on-wired-802.1x-with-a-raspberry-pi/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-11
fetch_date: 2025-10-04T12:08:40.792571
---

# MITM on wired 802.1x with a Raspberry PI

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# MITM on wired 802.1x with a Raspberry PI

#### Table of contents

* [Introduction: NAC solutions](#introduction-nac-solutions)
* [Switch configuration](#switch-configuration)
* [MITM on 802.1x](#mitm-on-8021x)
* [Defense strategies](#defense-strategies)

#### Latest posts

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/01/circular-dependencies-with-ndo/)

[Circular Dependencies with NDO](/blog/2025/10/01/circular-dependencies-with-ndo/)
October 01, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)

[Modifying an object in Strata Cloud Manager](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)
September 28, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)

[From Single-Site to Multi-Site with NDO](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)
September 24, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)

[Retrieving firewall interfaces with Strata Cloud Manager](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)
September 21, 2025

[![Post cover](/images/vendors/eve-ng.webp)](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)

[EVE-NG Linux VM SSH troubleshooting](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)
September 20, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 159 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 123 posts

[![Category cover](/images/categories/ciso.webp)](/categories/ciso)

[CISO](/categories/ciso)
 23 posts

[![Category cover](/images/categories/personal-security.webp)](/categories/personal-security)

[Personal Security](/categories/personal-security)
 22 posts

[![Category cover](/images/categories/security.webp)](/categories/security)

[Security](/categories/security)
 20 posts

[![Category cover](/images/categories/notes.webp)](/categories/notes)

[Notes](/categories/notes)
 19 posts

[![Category cover](/images/categories/infrastructure.webp)](/categories/infrastructure)

[Infrastructure](/categories/infrastructure)
 12 posts

[![Category cover](/images/categories/ot-ics.webp)](/categories/ot-ics)

[OT/ICS](/categories/ot-ics)
 5 posts

[![Category cover](/images/categories/books.webp)](/categories/books)

[Books](/categories/books)
 3 posts

[![Category cover](/images/categories/unetlab.webp)](/categories/unetlab)

[UNetLab](/categories/unetlab)
 3 posts

[![Category cover](/images/categories/writeup.webp)](/categories/writeup)

[Write-up](/categories/writeup)
 3 posts

[![Category cover](/images/categories/osint.webp)](/categories/osint)

[OSInt](/categories/osint)
 2 posts

[![Category cover](/images/categories/life.webp)](/categories/life)

[My life](/categories/life)
 1 posts

## MITM on wired 802.1x with a Raspberry PI

Andrea Dainese

March 10, 2024

[Security](/categories/security/ "All posts under Security"),
[Infrastructure](/categories/infrastructure/ "All posts under Infrastructure")

[![Post cover](/images/categories/security.webp)](/images/categories/security.webp)

In recent years, Network Access Control (NAC) solutions based on the 802.1x protocol have gained significant traction. Like all security solutions, it is crucial to carefully evaluate their functionality to integrate them into a proper Cybersecurity strategy.

I understand that this evaluation requires highly specific technical knowledge, and often those assessing rely on what is described in datasheets. This post serves three purposes:

* to raise awareness that incorrectly assessing a security solution exposes organizations to threats;
* to describe the steps by which a threat actor can exploit weaknesses in NAC solutions,
* to be informative and therefore understandable even to non-technical individuals.

## Introduction: NAC solutions

First and foremost, an overview of NAC or Network Access Control solutions is necessary. These solutions are based on the 802.1x protocol to authenticate and authorize connected devices. Some solutions, through additional components, also assess device behavior to identify any anomalies.

The problem these solutions aim to solve is related to unauthorized access to Ethernet ports by unauthorized devices. Specifically, these solutions protect ports naturally accessible to individuals, particularly in offices and public areas.

Over time, these solutions have evolved to not only authenticate but also authorize and profile connected devices. In other words, it is possible to dynamically configure Ethernet ports based on connected devices. This functionality greatly aids in improving and automating the management of large and dynamic campus areas.

Device authentication is based on the 802.1x protocol: the switch requests authentication from the device, and authentications are validated through external servers. Authentication can occur via username and password or through certificates. Once the device is authenticated, the channel is active until the session expires, which must then be renewed.

Over time, solutions have evolved to support multiple connected devices, such as:

* Phone with cascaded computers;
* Computers with virtual machines;
* …

However, in the real world, there are numerous devices that do not implement the 802.1x protocol. NAC solutions have further “evolved” (perhaps it would be more correct to say “devolved”), authenticating devices based on their MAC address: this functionality is called MAB or MAC Address Bypass. It is evident that the term “bypass” cannot be associated with a security feature, and indeed, we recall that NAC solutions are also used for automation.

The most important consideration, however, concerns how an authenticated session is established. 802.1x allows authentication of the channel, not individual packets. Specifically, the switch associates the authenticated session with the MAC address of the device. An attacker can thus insert a malicious device between the authenticated device and the switch, exploiting the authenticated channel.

The final consideration concerns what I call “silent” devices. For NAC solutions to work, connected devices must support 802.1x or transmit at least one packet to make their MAC address known to the switch. Some devices are designed to receive data but not transmit it, making it impossible to use any NAC solution.

## Switch configuration

Switch configuration should be carefully evaluated to minimize risks, which, as we will see later, are still present.

Each Ethernet port can be configured in various modes depending on the vendor. Examining Cisco switches, the modes are:

* Multi-Host: once the port is authenticated by the connected device, any other device can use the channel (for example, in the case of virtual machines).
* Multi-Domain: each connected device, belonging to a specific VLAN, must be authenticated (for example, in the case of cascaded phones and computers).
* Multi-Auth: each MAC address that appears on the Ethernet port must be authenticated.
* MAB: no real authentication is performed, but only a check that the MAC address is enabled.

Where possible, the preference should be, in order, Multi-Auth, Multi-Domain, Multi-Host, MAB (note: definitions depend on the vendor, the important thing is to understand the concept).

## MITM on 802.1x

From the attacker’s perspective, in the worst-case scenario, inserting oneself between an authenticated device and a switch means being transparent. Specifically, it means, in order:

1. forwarding any data to and from the switch without applying any filters to local frames;
2. waiting for the chan...