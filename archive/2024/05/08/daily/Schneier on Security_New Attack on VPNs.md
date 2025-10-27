---
title: New Attack on VPNs
url: https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html
source: Schneier on Security
date: 2024-05-08
fetch_date: 2025-10-06T17:22:40.296761
---

# New Attack on VPNs

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## New Attack on VPNs

This [attack](https://arstechnica.com/security/2024/05/novel-attack-against-virtually-all-vpn-apps-neuters-their-entire-purpose/) has been feasible for over two decades:

> Researchers have devised an attack against nearly all virtual private network applications that forces them to send and receive some or all traffic outside of the encrypted tunnel designed to protect it from snooping or tampering.
>
> TunnelVision, as the researchers have named their attack, largely negates the entire purpose and selling point of VPNs, which is to encapsulate incoming and outgoing Internet traffic in an encrypted tunnel and to cloak the user’s IP address. The researchers believe it affects all VPN applications when they’re connected to a hostile network and that there are no ways to prevent such attacks except when the user’s VPN runs on Linux or Android. They also said their attack technique may have been possible since 2002 and may already have been discovered and used in the wild since then.
>
> […]
>
> The attack works by manipulating the [DHCP server](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) that allocates IP addresses to devices trying to connect to the local network. A setting known as [option 121](https://datatracker.ietf.org/doc/html/rfc3442) allows the DHCP server to override default routing rules that send VPN traffic through a local IP address that initiates the encrypted tunnel. By using option 121 to route VPN traffic through the DHCP server, the attack diverts the data to the DHCP server itself.

Tags: [cyberattack](https://www.schneier.com/tag/cyberattack/), [VPN](https://www.schneier.com/tag/vpn/)

[Posted on May 7, 2024 at 11:32 AM](https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html) •
[53 Comments](https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html#comments)

### Comments

Aaron •
[May 7, 2024 11:48 AM](https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html/#comment-436422)

As much attention as this is getting; it’s a rather pathetic attack vector which is easily controlled… so why is this getting so much attention?

John Wythe •
[May 7, 2024 12:03 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html/#comment-436424)

It is getting a lot of attention because new security “experts” don’t read 3-digit RFCs anymore

On a more serious note however, maybe this explains the big focus recently on getting access to the ISP home routers (or “boxes” as we call them in France)

Getting access to an ISP consumer box permits a whole lot of shenanigans, of witch this abuse of option 121 is only one example.

echo •
[May 7, 2024 12:20 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html/#comment-436426)

Most VPN to the best of my knowledge at the consumer level is bought on the basis of changing geolocation or lightly concealing traffic type and content from an ISP. It doesn’t need to be bullet proof just good enough to thwart consumer grade providers. Ditto most hum drum business stuff. The problems start creeping in when it involves valuable IP which can shift the future of industries or people dying. It’s not always going to be the usual big ticket military. It can be vulnerable persecuted minorities too.

> The attack works by manipulating the DHCP server that allocates IP addresses to devices trying to connect to the local network. A setting known as option 121 allows the DHCP server to override default routing rules that send VPN traffic through a local IP address that initiates the encrypted tunnel. By using option 121 to route VPN traffic through the DHCP server, the attack diverts the data to the DHCP server itself. Researchers from Leviathan Security explained:

Okay, change defaults or block option 121.

> Interestingly, Android is the only operating system that fully immunizes VPN apps from the attack because it doesn’t implement option 121. For all other OSes, there are no complete fixes. When apps run on Linux there’s a setting that minimizes the effects, but even then TunnelVision can be used to exploit a side channel that can be used to de-anonymize destination traffic and perform targeted denial-of-service attacks. Network firewalls can also be configured to deny inbound and outbound traffic to and from the physical interface. This remedy is problematic for two reasons: (1) a VPN user connecting to an untrusted network has no ability to control the firewall and (2) it opens the same side channel present with the Linux mitigation.

Okay, block option 121.

Doesn’t effect (verified) trusted networks.

As for Microsoft? Sheesh.

I know people don’t like my position but if you don’t like dead people then fix it. If it’s not fixed I’m going to assume people don’t care. If you don’t care then find a job in another profession.

Anonymous •
[May 7, 2024 12:50 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html/#comment-436429)

Not sure that these are fundamentally new research findings, though the authors may not be making that strong a claim.

E.g. from 2015:

“However, a DHCP server can also push its own routes (called “classless static routes”) to the DHCP client. So a rogue DHCP server can push routes even more specific than the OpenVPN routes, such as for 0.0.0.0/2, 64.0.0.0/2, 128.0.0.0/2, and 192.0.0.0/2. These routes cover the entire IPv4 address space, and take precedence over the less-specific OpenVPN routes.”

<https://www.agwa.name/blog/post/hardening_openvpn_for_def_con>

jm •
[May 7, 2024 2:10 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html/#comment-436433)

Some enterprise VPN clients (ZScaler) also modify routing policy using “ip rule” and their rules take precedence before the regular routing table, so this attack may be limited use.

Anonymous •
[May 7, 2024 2:23 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html/#comment-436435)

Does anyone know whether ProtonVPN and AirVPN are affected by this?
These are my primary, and secondary, VPNs of choice.

lurker •
[May 7, 2024 2:46 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-on-vpns.html/#comment-436436)

@Bruce

This might look like a new attack on VPN, but in fact it’s an old attack on DHCP. It also assumes access to the LAN that the VPN client is on (as mentioned in the arstehnica comments: coffee shops, free wifi, &c.) The attack is against VPNs used for evading geolocation where all traffic is routed through the VPN.

It seems that this attack should not work against a WorkFromHome VPN that is configured acording to this **option** described by Leviathan:

> 3. The VPN client optionally runs a startup script to configure the host. It may configure routing rules, the DNS server to use, host-based firewall rules, or other settings

<https://www.leviathansecurity.com/blog/tunnelvision>

A...