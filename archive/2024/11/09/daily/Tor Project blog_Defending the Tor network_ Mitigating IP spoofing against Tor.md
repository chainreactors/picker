---
title: Defending the Tor network: Mitigating IP spoofing against Tor
url: https://blog.torproject.org/defending-tor-mitigating-IP-spoofing/
source: Tor Project blog
date: 2024-11-09
fetch_date: 2025-10-06T19:24:31.584460
---

# Defending the Tor network: Mitigating IP spoofing against Tor

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Defending the Tor network: Mitigating IP spoofing against Tor

by [gus](/author/gus)
| November 8, 2024

![](/defending-tor-mitigating-IP-spoofing/lead.png)

At the end of October, [Tor directory authorities](https://community.torproject.org/relay/governance/policies-and-proposals/directory-authority/), [relay operators](https://community.torproject.org/relay/), and even the [Tor Project sysadmin team](https://gitlab.torproject.org/tpo/tpa/team/-/issues/41840) received multiple abuse complaints from their providers about port scanning. These complaints were traced back to a coordinated IP spoofing attack, where an attacker spoofed non-exit relays and other Tor-related IPs to trigger abuse reports aimed at disrupting the Tor Project and the Tor network.

Thanks to a joint effort from the Tor community, [InterSecLab](https://www.opentech.fund/projects-we-support/supported-projects/interseclab/), and the support of Andrew Morris and the team at [GreyNoise](https://www.greynoise.io/), the origin of these spoofed packets was identified and shut down on November 7th, 2024.

We want to reassure everyone that this incident had no effect on Tor users. While the attack had a limited impact on the Tor network - taking a few relays offline temporarily - it caused unnecessary stress and inconvenience for many relay operators who had to address these complaints. Although this attack targeted our community, IP spoofing attacks can happen with any [online service](https://cyberscoop.com/spoofed-bank-ip-address-greynoise-andrew-morris-bank-of-america).

There's still work ahead: we need to support relay operators in getting their accounts reinstated and assist providers in unblocking IPs for Tor directory authorities.

### Hosting providers and abuse complaints

If you are a relay operator whose hosting provider is still blocking or has suspended your relay due to these complaints, here are steps you can take to resolve the issue:

1. Check Tor directory authorities reachability from your relay: If you suspect your provider has blocked Tor access -- i.e., because your relay dropped from the Tor consensus --, use [OONI Probe](https://ooni.org/install/) and ["Circumvention" test](https://ooni.org/nettest/tor/) to check the reachability of Tor directory authorities. If the test shows that most directory authorities are reachable, your relay will successfully (re-)connect to the Tor network. If Tor directory authorities are still blocked, please contact your hosting provider support and share this blog post.
2. Reply to your hosting company: If you got contacted by your provider due to the abuse complaints, share this blog post to help them understand the incident and clarify that your Tor relay was targeted by a spoofing attack, and is NOT originating any suspicious traffic. You can adapt and use this [template about abuse complaints](https://gitlab.torproject.org/tpo/network-health/analysis/-/issues/85#note_3126618).

### Community strength and collaboration

This incident has demonstrated the resilience and collaborative spirit of the Tor relay operator community. Over the past days, we've seen many instances of good collaboration to defend the Tor network: analysis, investigation, and knowledge sharing. Relay operators worked together to troubleshoot issues, support each other over email and chat, and keep relays online.

We encourage relay operators to stay connected and informed through our [official community channels](https://lists.torproject.org/mailman3/postorius/lists/tor-relays.lists.torproject.org/) and participate in our monthly relay operator meetups.

Thank you to every relay operator for your ongoing efforts to run relays, protect online privacy, and support the Tor Project! <3

### Background: What happened?

On October 20, Tor directory authorities began receiving abuse complaints claiming that their servers were engaged in unauthorized port scans. In the Tor network, directory authorities play a critical role in maintaining the list of available relays.

This attack focused on non-exit relays, using spoofed SYN packets to make it appear that Tor relay IP addresses were the sources of these scans. This led to automated abuse complaints directed at data centers such as OVH, Hetzner, and other providers. The attacker's intent seems to have been to disrupt the Tor network and the Tor Project by getting these IPs on blocklists with these unfounded complaints.

Pierre Bourdon, a relay operator, shared insights into the attack in his post, *["One weird trick to get the whole planet to send abuse complaints to your best friend(s)"](https://delroth.net/posts/spoofed-mass-scan-abuse/)*, which sheds light on how the attacker used spoofed IP packets to trigger automated abuse complaints across the network. A huge thank you to Pierre for his detailed analysis and for sharing his findings with the community!

While we received support from many individuals and organizations during this incident, we also experienced instances of unprofessional conduct, where a the refusal to investigate and lack of diligence inadvertently amplified the impact of this attack. Much of the reporting on this fake abuse attack comes from watchdogcyberdefense[.]com and we endorse the calls within the cybersecurity community to [treat these reports with caution](https://seclists.org/nanog/2024/Nov/24).

For a more detailed discussion, please refer to our [public ticket on the issue](https://gitlab.torproject.org/tpo/network-health/analysis/-/issues/85) and [our mailing list](https://archive.torproject.org/websites/lists.torproject.org/pipermail/tor-relays/2024-October/021953.html).

While spoofing activity is not specific to Tor, itâs concerning that someone would choose to deliberately disrupt a service that is essential for people experiencing digital surveillance and internet censorship. Tor plays a critical role in supporting freedom of access and expression globally, and targeting it undermines these fundamental rights. We are grateful for the resilience and dedication of our relay operator community, whose collective efforts ensure the strength of Torâs decentralized network.

* [community](/category/community)
* [network](/category/network)
* [relays](/category/relays)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/defending-tor-mitigating-IP-spoofing/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/defending-tor-mitigating-IP-spoofing/&text=Over%20the%20last%20few%20weeks%2C%20the%20Tor%20Project%20and%20relay%20operators%20received%20abuse%20complaints%20regarding%20alleged%20port%20scanning%20activity%20from%20their%20servers.%20Thanks%20to%20a%20collaborative%20effort%2C%20the%20source%20of%20the%20spoofed%20packets%20has%20been%20identified%20and%20shut%20down.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/defending-tor-mitigating-IP-spoofing/&text=Over%20the%20last%20few%20weeks%2C%20the%20Tor%20Project%20and%20relay%20operators%20received%20abuse%20complaints%20regarding%20alleged%20port%20scanning%20activity%20from%20their%20servers.%20Thanks%20to%20a%20collaborative%20effort%2C%20the%20source%20of%20the%20spoofed%20packets%20has%20been%20identified%20and%20shut%20down.)
[Bluesky](https://bsky.app/intent/compose?text=Over%20the%20last%20few%20weeks%2C%20the%20Tor%20Project%20and%20relay%20operators%20received%20abuse%20complaints%20regarding%20alleged%20port%20scanning%20activity%20from%20their%20servers.%20Thanks%20to%20a%20collaborative%20effort%2C%20the%20source%20of%20the%20spoofed%20packets%20has%20been%20identified%20and%20shut%20down.%0Ahttps%3A//blog.torproject.org...