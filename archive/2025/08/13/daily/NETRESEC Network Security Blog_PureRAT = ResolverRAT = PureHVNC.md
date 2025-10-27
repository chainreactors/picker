---
title: PureRAT = ResolverRAT = PureHVNC
url: https://www.netresec.com/?page=Blog&month=2025-08&post=PureRAT-ResolverRAT-PureHVNC
source: NETRESEC Network Security Blog
date: 2025-08-13
fetch_date: 2025-10-07T00:58:00.709231
---

# PureRAT = ResolverRAT = PureHVNC

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

Tuesday, 12 August 2025 15:43:00 (UTC/GMT)

## [PureRAT = ResolverRAT = PureHVNC](/?page=Blog&month=2025-08&post=PureRAT-ResolverRAT-PureHVNC)

PureRAT is a Remote Access Trojan, which can be used by an attacker to remotely control someone else’s PC. PureRAT provides the following features to an attacker:

* See the victims user interface
* Interact with the victim PC using mouse and keyboard
* View the webcam
* Listen to the microphone
* Record keystrokes
* Upload and download files
* Proxy network traffic through victim

![PureRAT user interface](https://media.netresec.com/images/PureRAT_UI_1024x512.webp)

*What the PureRAT user interface looks like to the attacker*

PureRAT is the exact same malware as what Morphisec and others call ResolverRAT. PureHVNC, on the other hand, is the predecessor to PureRAT. These three malware names are all used by threat intel companies and researchers when referring to the same malware family. We will call this malware family “PureRAT” in this blog post.

**Indicators of PureRAT**

Malware analysts might recognize PureRAT through properties like these ones:

* Loader is a .NET executable obfuscated with Eazfuscator.NET
* Payload is AES-256 encrypted in CBC mode
* Payload is gzip compressed
* Extracted PureRAT payload is a DLL
* PureRAT DLL is packed with .NET Reactor
* A handler is registered for the [ResourceResolve](https://learn.microsoft.com/en-us/dotnet/api/system.appdomain.resourceresolve) event to inject a malicious .NET assembly

See analysis by [eSentire](https://www.esentire.com/blog/ghost-crypt-powers-purerat-with-hypnosis), [Morphisec](https://www.morphisec.com/blog/new-malware-variant-identified-resolverrat-enters-the-maze/), [Kaspersky](https://securelist.ru/purerat-attacks-russian-organizations/112619/), [Fortinet](https://www.fortinet.com/blog/threat-research/purehvnc-deployed-via-python-multi-stage-loader) and [0xlibris](https://0xlibris.net/posts/infection_chain_infostealer_2/) for more reverse engineering details on PureRAT and related software from the PureCoder developer(s).

Another way to identify the malware is to run it in a sandbox and inspect the network traffic. The following characteristics are typical indicators of PureRAT:

* C2 TCP port is often 56001, 56002 or 56003
* Client (bot) first sends 04 00 00 00 (in hex), followed by a TLS handshake
* Client and server run TLS 1.0
* X.509 cert is self signed
* X.509 cert expires 9999-12-31 23:59:59 UTC

![/ResolverRAT_CapLoader_Transcript](https://media.netresec.com/images/ResolverRAT_CapLoader_Transcript_986x623.webp)

As you can see in the flow transcript above, [CapLoader](https://www.netresec.com/?page=CapLoader) currently identifies this traffic as “ResolverRAT”. This detection will most likely be changed to “PureRAT” in future versions of CapLoader.

**IOC List**

Here are some IP:port tuples for C2 servers used by recent samples of PureRAT:

* 193.26.115.125:8883
* purebase.ddns[.]net:8883
* 45.74.10.38:56001
* 139.99.83.25:56001

Posted by Erik Hjelmvik on Tuesday, 12 August 2025 15:43:00 (UTC/GMT)

Tags:
#[PureCoder](/?page=Blog&tag=PureCoder)​

Short URL:
<https://netresec.com/?b=2589522>

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