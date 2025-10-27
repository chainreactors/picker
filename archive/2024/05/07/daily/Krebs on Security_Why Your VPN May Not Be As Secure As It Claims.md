---
title: Why Your VPN May Not Be As Secure As It Claims
url: https://krebsonsecurity.com/2024/05/why-your-vpn-may-not-be-as-secure-as-it-claims/
source: Krebs on Security
date: 2024-05-07
fetch_date: 2025-10-06T17:29:31.136136
---

# Why Your VPN May Not Be As Secure As It Claims

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Why Your VPN May Not Be As Secure As It Claims

May 6, 2024

[44 Comments](https://krebsonsecurity.com/2024/05/why-your-vpn-may-not-be-as-secure-as-it-claims/#comments)

Virtual private networking (VPN) companies market their services as a way to prevent anyone from snooping on your Internet usage. But new research suggests this is a dangerous assumption when connecting to a VPN via an untrusted network, because attackers on the same network could force a target’s traffic off of the protection provided by their VPN without triggering any alerts to the user.

![](https://krebsonsecurity.com/wp-content/uploads/2024/05/tunnelvision.png)

When a device initially tries to connect to a network, it broadcasts a message to the entire local network stating that it is requesting an Internet address. Normally, the only system on the network that notices this request and replies is the router responsible for managing the network to which the user is trying to connect.

The machine on a network responsible for fielding these requests is called a **Dynamic Host Configuration Protocol** (DHCP) server, which will issue time-based leases for IP addresses. The DHCP server also takes care of setting a specific local address — known as an **Internet gateway** — that all connecting systems will use as a primary route to the Web.

VPNs work by creating a virtual network interface that serves as an encrypted tunnel for communications. But researchers at **Leviathan Security** say they’ve discovered it’s possible to abuse an obscure feature built into the DHCP standard so that other users on the local network are forced to connect to a rogue DHCP server.

“Our technique is to run a DHCP server on the same network as a targeted VPN user and to also set our DHCP configuration to use itself as a gateway,” Leviathan researchers **Lizzie Moratti** and **Dani Cronce** wrote. “When the traffic hits our gateway, we use traffic forwarding rules on the DHCP server to pass traffic through to a legitimate gateway while we snoop on it.”

The feature being abused here is known as [DHCP option 121](https://datatracker.ietf.org/doc/html/rfc3442), and it allows a DHCP server to set a route on the VPN user’s system that is more specific than those used by most VPNs. Abusing this option, Leviathan found, effectively gives an attacker on the local network the ability to set up routing rules that have a higher priority than the routes for the virtual network interface that the target’s VPN creates.

“Pushing a route also means that the network traffic will be sent over the same interface as the DHCP server instead of the virtual network interface,” the Leviathan researchers said. “This is intended functionality that isn’t clearly stated in the RFC [standard]. Therefore, for the routes we push, it is never encrypted by the VPN’s virtual interface but instead transmitted by the network interface that is talking to the DHCP server. As an attacker, we can select which IP addresses go over the tunnel and which addresses go over the network interface talking to our DHCP server.”

Leviathan found they could force VPNs on the local network that already had a connection to arbitrarily request a new one. In this well-documented tactic, known as a [DHCP starvation attack](https://www.prosec-networks.com/en/blog/dhcp-starvation-attack/), an attacker floods the DHCP server with requests that consume all available IP addresses that can be allocated. Once the network’s legitimate DHCP server is completely tied up, the attacker can then have their rogue DHCP server respond to all pending requests.

“This technique can also be used against an already established VPN connection once the VPN user’s host needs to renew a lease from our DHCP server,” the researchers wrote. “We can artificially create that scenario by setting a short lease time in the DHCP lease, so the user updates their routing table more frequently. In addition, the VPN control channel is still intact because it already uses the physical interface for its communication. In our testing, the VPN always continued to report as connected, and the kill switch was never engaged to drop our VPN connection.”

The researchers say their methods could be used by an attacker who compromises a DHCP server or wireless access point, or by a rogue network administrator who owns the infrastructure themselves and maliciously configures it. Alternatively, an attacker could set up an “[evil twin](https://www.techtarget.com/searchsecurity/definition/evil-twin)” wireless hotspot that mimics the signal broadcast by a legitimate provider.

## ANALYSIS

**Bill Woodcock** is executive director at [Packet Clearing House](http://www.pch.net), a nonprofit based in San Francisco. Woodcock said Option 121 has been included in the DHCP standard since 2002, which means the attack described by Leviathan has technically been possible for the last 22 years.

“They’re realizing now that this can be used to circumvent a VPN in a way that’s really problematic, and they’re right,” Woodcock said.

Woodcock said anyone who might be a target of spear phishing attacks should be very concerned about using VPNs on an untrusted network.

“Anyone who is in a position of authority or maybe even someone who is just a high net worth individual, those are all very reasonable targets of this attack,” he said. “If I were trying to do an attack against someone at a relatively high security company and I knew where they typically get their coffee or sandwich at twice a week, this is a very effective tool in that toolbox. I’d be a little surprised if it wasn’t already being exploited in that way, because again this isn’t rocket science. It’s just thinking a little outside the box.”

Successfully executing this attack on a network likely would not allow an attacker to see all of a target’s traffic or browsing activity. That’s because for the vast majority of the websites visited by the target, the content is encrypted (the site’s address begins with https://). However, an attacker would still be able to see the metadata — such as the source and destination addresses — of any traffic flowing by.

KrebsOnSecurity shared Leviathan’s research with [John Kristoff](https://www.netscout.com/asert/john-kristoff), founder of [dataplane.org](https://dataplane.org/) and a PhD candidate in computer science at the **University of Illinois Chicago**. Kristoff said practically all user-edge network gear, including WiFi deployments, support some form of rogue DHCP server detection and mitigation, but that it’s unclear how widely deployed those protections are in real-world environments.

“However, and I think this is a key point to emphasize, an untrusted network is an untrusted network, which is why you’re usually employing the VPN in the first place,” Kristoff said. “If [the] local network is inherently hostile and has no qualms about operating a rogue DHCP server, then this is a sneaky technique that could be used to de-cloak some traffic – and if done carefully, I’m sure a user might never notice.”

## MITIGATIONS

According to Leviathan, there are several ways to minimize the threat from rogue DHCP servers on an unsecured network. One is using a device powered by the **...