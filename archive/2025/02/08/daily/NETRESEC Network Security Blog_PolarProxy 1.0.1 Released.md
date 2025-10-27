---
title: PolarProxy 1.0.1 Released
url: https://www.netresec.com/?page=Blog&month=2025-02&post=PolarProxy-1-0-1-Released
source: NETRESEC Network Security Blog
date: 2025-02-08
fetch_date: 2025-10-06T20:47:14.750484
---

# PolarProxy 1.0.1 Released

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

Friday, 07 February 2025 10:10:00 (UTC/GMT)

## [PolarProxy 1.0.1 Released](/?page=Blog&month=2025-02&post=PolarProxy-1-0-1-Released)

![PolarProxy 1.0.1](https://media.netresec.com/images/PolarProxy 1-0-1_400x392.png)

The new release of [PolarProxy](https://www.netresec.com/?page=PolarProxy) generates JA4 fingerprints and enables ruleset to match on specific decryption errors, for example to enable fail-open in case the TLS traffic cannot be decrypted and inspected.

**JA4 Fingerprints**

[JA4 fingerprints](https://github.com/FoxIO-LLC/ja4) provide several improvements over its JA3 predecessor. One advantage is that JA4 fingerprints have a human readable segment that allow humans (as well as computers) to instantly see important features in a client handshake, such as the TLS version and whether or not the [SNI](https://en.wikipedia.org/wiki/Server_Name_Indication) and [ALPN](https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation) extensions are used. JA4 is also resilient against [TLS extension order randomization](https://chromestatus.com/feature/5124606246518784).

![JA4 hash explained. Breakdown of Remcos JA4 hash t13i010400_0f2cb44170f4_5c4c70b73fa0](https://media.netresec.com/images/JA4-explained.svg)

We added support for [rule based](https://www.netresec.com/?page=TlsFirewall) matching of JA4 fingerprints in the [previous release](https://netresec.com/?b=2451e98) of PolarProxy. Such a JA4 rule can be used to have PolarProxy take different actions (block, intercept, bypass etc.) based on the JA4 fingerprint of the client’s TLS handshake.

This release additionally includes JA4 fingerprints in the flow metadata that PolarProxy writes to disk when the -f <file> argument is provided.

**Flexible Handling of TLS Auth Failures**

PolarProxy’s [firewall rules](https://www.netresec.com/?page=TlsFirewall) now support using TLS authentication error codes as triggers. As an example, the ruleset [fail-open.json](https://github.com/Netresec/PolarProxy/blob/main/rulesets/fail-open.json) attempts to inspect (decrypt and re-encrypt) all TLS traffic, except when the client has rejected the server’s certificate at least once during the past 60 seconds. More specifically, it only bypasses decryption if the reason for the rejection was either “bad certificate” or “unknown CA”.

{
  "name": "Inspect TLS with fail open for OpenSSL alerts", "version": "1.0.1", "rules": [
    {
      "active": true,
      "match": { "type": "nontls" },
      "action": { "type": "block" },
      "description": "Block non-TLS traffic"
    },
    {
      "active": true,
      "match": { "type": "decrypt\_fail\_errorcode", "expression": "0x0A000412", "period": 60, "count": 1 },
      "action": { "type": "bypass" },
      "description": "bad certificate"
    },
    {
      "active": true,
      "match": { "type": "decrypt\_fail\_errorcode", "expression": "0x0A000418", "period": 60, "count": 1 },
      "action": { "type": "bypass" },
      "description": "unknown CA"
    }
    ],
  "default": {
    "action": { "type": "inspect" },
    "description": "Attempt to inspect TLS traffic"
  }
}

*Figure:
PolarProxy [fail-open.json](https://github.com/Netresec/PolarProxy/blob/main/rulesets/fail-open.json)
ruleset*

The specific error codes (here 0x0A000412 for “bad certificate” and 0x0A000418 for “unknown CA”) might differ between deployments, since they depend on the underlying TLS library of the PolarProxy machine. The specific values in this example are from a Linux deployment with OpenSSL 3.0.13 installed. Look for the “decrypt\_fail\_errorcode” messages that PolarProxy prints to stderr to find out what error codes your system is using. You can also run PolarProxy with -v (verbose) or -d (debug) to get even more information about the error codes.

**Ruleset Reload on SIGHUP**

A PolarProxy [ruleset](https://www.netresec.com/?page=TlsFirewall) can now be updated on the fly without having to restart PolarProxy. Simply send a SIGHUP signal to PolarProxy, for example pkill -HUP PolarProxy, to have it reload the updated ruleset without affecting sessions that PolarProxy is currently proxying.

If PolarProxy is running as a systemd service, then adding
> ExecReload=/bin/kill -HUP $MAINPID

to the unit file allows PolarProxy’s ruleset to be reloaded with:

sudo systemctl reload PolarProxy.service

**.NET 8**

The .NET version has been bumped from 6 to 8 in the 1.0.1 release, which provides better performance as well as [long-term support](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core).
We've also bumped the System.Security.Cryptography.Xml library from version 4.5 to 9.0.

Posted by Erik Hjelmvik on Friday, 07 February 2025 10:10:00 (UTC/GMT)

Tags:
#[PolarProxy](/?page=Blog&tag=PolarProxy)​
#[JA4](/?page=Blog&tag=JA4)​
#[fail-open](/?page=Blog&tag=fail-open)​

Short URL:
<https://netresec.com/?b=2523c96>

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