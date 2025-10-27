---
title: PolarProxy 1.0 Released
url: https://www.netresec.com/?page=Blog&month=2024-05&post=PolarProxy-1-0-Released
source: NETRESEC Network Security Blog
date: 2024-05-03
fetch_date: 2025-10-06T17:16:12.009012
---

# PolarProxy 1.0 Released

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Thursday, 02 May 2024 07:00:00 (UTC/GMT)

## [PolarProxy 1.0 Released](/?page=Blog&month=2024-05&post=PolarProxy-1-0-Released)

I am thrilled to announce the release of [PolarProxy](https://www.netresec.com/?page=PolarProxy) version 1.0 today!
Several bugs that affected performance, stability and memory usage have now been resolved in our TLS inspection proxy. PolarProxy has also been updated with better logic for importing external root CA certificates and the HAProxy implementation has been improved. But the most significant addition in the 1.0 release is what we call the “TLS Firewall” mode.

**TLS Firewall**

PolarProxy now supports [rule based logic](https://www.netresec.com/?page=TlsFirewall) for determining if a session should be allowed to pass through, get blocked or if the TLS encrypted data should be inspected (i.e. decrypted and re-encrypted) by the proxy.
This rule based logic can be used to turn PolarProxy into a TLS firewall. As an example, the [ruleset-block-malicious.json](https://github.com/Netresec/PolarProxy/blob/main/rulesets/ruleset-block-malicious.json) ruleset included in the new PolarProxy release blocks traffic to malicious domains in abuse.ch’s [ThreatFox IOC database](https://threatfox.abuse.ch/browse/) as well as traffic to web tracker domains listed in the EasyPrivacy filter from [EasyList](https://easylist.to/). This ruleset also includes an allow list in order to avoid accidentally blocking access to legitimate websites.

![PolarProxy TLS Firewall - block malicious, inspect suspicious, bypass legitimate](https://media.netresec.com/images/PolarProxy_block-inspect-bypass-ascii_520x380.png)

PolarProxy’s ruleset logic isn’t limited to just domain names. It is also possible to match traffic based on [JA3](https://github.com/salesforce/ja3) or [JA4](https://blog.foxio.io/ja4%2B-network-fingerprinting) hashes as well as application layer protocol information provided in the [ALPN](https://datatracker.ietf.org/doc/html/rfc7301) extension of a client’s TLS handshake.

For more information on the ruleset format and how to use PolarProxy as a TLS firewall, see here:
<https://www.netresec.com/?page=TlsFirewall>

Linux, macOS and Windows builds of the new PolarProxy release can be downloaded from here:
<https://www.netresec.com/?page=PolarProxy>

Posted by Erik Hjelmvik on Thursday, 02 May 2024 07:00:00 (UTC/GMT)

Tags:
#[PolarProxy](/?page=Blog&tag=PolarProxy)​
#[TLS](/?page=Blog&tag=TLS)​
#[inspect](/?page=Blog&tag=inspect)​
#[bypass](/?page=Blog&tag=bypass)​
#[ThreatFox](/?page=Blog&tag=ThreatFox)​
#[ASCII-art](/?page=Blog&tag=ASCII-art)​

Short URL:
<https://netresec.com/?b=2451e98>

### Recent Posts

» [Gh0stKCP Protocol](/?page=Blog&month=2025-09&post=Gh0stKCP-Protocol)

» [Define Protocol from Traffic (XenoRAT)](/?page=Blog&month=2025-08&post=Define-Protocol-from-Traffic-XenoRAT)

» [PureRAT = ResolverRAT = PureHVNC](/?page=Blog&month=2025-08&post=PureRAT-ResolverRAT-PureHVNC)

» [PureLogs Forensics](/?page=Blog&month=2025-07&post=PureLogs-Forensics)

» [CapLoader 2.0.1 Released](/?page=Blog&month=2025-07&post=CapLoader-2-0-1-Released)

» [Detecting PureLogs traffic with CapLoader](/?page=Blog&month=2025-06&post=Detecting-PureLogs-traffic-with-CapLoader)

» [CapLoader 2.0 Released](/?page=Blog&month=2025-06&post=CapLoader-2-0-Released)

» [Comparison of tools that extract files from PCAP](/?page=Blog&month=2025-05&post=Comparison-of-tools-that-extract-files-from-PCAP)

### Blog Archive

» [2025 Blog Posts](?page=Blog&year=2025)

» [2024 Blog Posts](?page=Blog&year=2024)

» [2023 Blog Posts](?page=Blog&year=2023)

» [2022 Blog Posts](?page=Blog&year=2022)

» [2021 Blog Posts](?page=Blog&year=2021)

» [2020 Blog Posts](?page=Blog&year=2020)

» [2019 Blog Posts](?page=Blog&year=2019)

» [2018 Blog Posts](?page=Blog&year=2018)

» [2017 Blog Posts](?page=Blog&year=2017)

» [2016 Blog Posts](?page=Blog&year=2016)

» [2015 Blog Posts](?page=Blog&year=2015)

» [2014 Blog Posts](?page=Blog&year=2014)

» [2013 Blog Posts](?page=Blog&year=2013)

» [2012 Blog Posts](?page=Blog&year=2012)

» [2011 Blog Posts](?page=Blog&year=2011)

[List all blog posts](/?page=Blog&blogPostList=true)

[Video blog posts](/?page=Video)

### News Feeds

» [FeedBurner](https://feeds.feedburner.com/Netresec-Network-Security-Blog)

» [RSS Feed](https://www.netresec.com/rss.ashx)

![X / twitter](/images/X_100x90.png)

𝕏:
[@netresec](https://x.com/netresec)

---

![Bluesky](/images/bluesky_100x88.png)

Bluesky:
[@netresec.com](https://bsky.app/profile/netresec.com)

---

![Mastodon](/images/mastodon_100x107.png)

Mastodon:
[@netresec@infosec.exchange](https://infosec.exchange/%40netresec)

𝙽𝙴𝚃𝚁𝙴𝚂𝙴𝙲 |
[Contact](/?page=AboutNetresec)
|
[Privacy](/?page=Privacy)
|
[Mastodon](https://infosec.exchange/%40netresec)
|
[Bluesky](https://bsky.app/profile/netresec.com)
|
[𝕏](https://x.com/netresec)
|
[RSS](https://www.netresec.com/rss.ashx)