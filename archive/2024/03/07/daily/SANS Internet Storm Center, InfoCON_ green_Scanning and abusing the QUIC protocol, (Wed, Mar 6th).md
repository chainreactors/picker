---
title: Scanning and abusing the QUIC protocol, (Wed, Mar 6th)
url: https://isc.sans.edu/diary/rss/30720
source: SANS Internet Storm Center, InfoCON: green
date: 2024-03-07
fetch_date: 2025-10-06T17:11:20.353106
---

# Scanning and abusing the QUIC protocol, (Wed, Mar 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30716)
* [next](/diary/30722)

My next class:

|  |  |  |
| --- | --- | --- |
| [Web App Penetration Testing and Ethical Hacking](https://www.sans.org/event/london-march-2026/course/web-app-penetration-testing-ethical-hacking) | London | Mar 2nd - Mar 7th 2026 |

# [Scanning and abusing the QUIC protocol](/forums/diary/Scanning%2Band%2Babusing%2Bthe%2BQUIC%2Bprotocol/30720/)

**Published**: 2024-03-06. **Last Updated**: 2024-03-06 09:43:39 UTC
**by** [Bojan Zdrnja](/handler_list.html#bojan-zdrnja) (Version: 1)

[1 comment(s)](/diary/Scanning%2Band%2Babusing%2Bthe%2BQUIC%2Bprotocol/30720/#comments)

The QUIC protocol has slowly (pun intended) crawled into our browsers and many other protocols. Last week, at [BSides Zagreb](https://bsideszagreb.srce.hr/) I presented some research I did about applications using (and abusing) this protocol, so it made sense to put this into one diary.

While QUIC has been around for some time, the official RFC 9000 that defines QUIC v1 was released in 2021. Of course, our browsers (namely Chrome, as Google was the main power behind QUIC) started supporting and using QUIC long time ago. Chrome, for example, added support for QUIC back in 2012, while Mozilla Firefox waited until 2021. Today, all browsers not only support QUIC but also use it – A LOT!

For example, if you take a look at your network traffic today to Google, YouTube, Facebook and similar web sites you will see that this network traffic consists of HTTP/3, which uses QUIC, almost exclusively – just open Developer Tools, go to the Network tab and right click on columns, add Protocol and you will see something like this:

![](https://isc.sans.edu/diaryimages/images/QUIC1.png)

This was me streaming something from YouTube – it’s almost exclusively HTTP/3. So, I wanted to understand the protocol and see if there are some potentials for abuse.

**Some protocol specifics**

While I will not dive into encryption (that was part of the presentation – it should be available soon on YouTube), QUIC makes security and privacy a first-class citizen. In other words, QUIC authors tried to encrypt absolutely everything and as much data as possible. QUIC also relies on TLSv1.3 which helps with a shorter handshake – generally we will have 1 RTT requests, and if we visited a certain web site before we can even have 0 RTT requests – quite impressive!

RFC 9000 describes all the details (and I’ll make a follow up diary about encryption), but here are couple of things that are important for the rest of this diary:

* While the QUIC protocol encrypts everything even in the first packet, it is still possible to decrypt some frame information and get certain metadata about the connection, including TLSv1.3 exchange parameters. This cannot be solved really – in the first packet there is no relationship between a server and a client so the public part of a randomly generated key (by a client) is sent in plain text, and the salt that is used for HKDF algorithms used by QUIC is a static value (it’s always 38762cf7f55934b34d179ae6a4c80cadccbb7f0a – the first SHA-1 collision found by Google researchers).
* This means that any observer always can decrypt certain metadata from the very first packet. I’m personally not sure of the benefit of this encryption due to this, but passive analysis devices (Hi Darktrace, Vectra …) will have a bit more difficult job in tracking first connections (and they will not see anything after that due to TLSv1.3).
* These packets define all parameters of a connection, together with supported stream (in QUIC a single connection has multiple streams). The important parameter we will want to pay more attention to is the ALPN (Application Layer Protocol Negotiation) extension that defines what application protocol we want to use. Most often this is h3 for HTTP/3, but it can be absolutely anything!

**Applications on top of QUIC**

Thanks to ALPN we can basically use practically any application protocol on top of QUIC. Of course, HTTP/3 is the most commonly used protocol, but there is a bunch of other supported protocols already registered with IANA, as we can see at <https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids>

The one that caught my attention (hence this diary) is SMB2: yes, SMB can work over QUIC. And what’s perhaps even more terrifying is that Microsoft started adding support for this! Some time ago, SMB over QUIC (SMB VPN as Microsoft likes to call it) was available only on Windows Server 2022 Datacenter Azure Edition, however Microsoft actually added support now even in Windows Server 2025 Insider Preview! With client side supported already by Windows 11 – you can even have SMB over QUIC running on premise.

The screenshot below shows my Windows Server 2025 server configured to host SMB over QUIC – which now becomes accessible over UDP port 443 – as any other QUIC application running on this port, including HTTP/3.

![](https://isc.sans.edu/diaryimages/images/QUIC2.png)

Microsoft’s idea here is to allow VPN-less SMB connections – your client might be at home, and “all you need” is to expose SMB over QUIC on UDP port 443 and they can connect to it now from anywhere in the world! What could go wrong here …

Imagine an attacker silently enabling this feature without anyone even knowing, and then using it to exfiltrate data – what a perfect covert channel, blended with HTTP/3.

**QUIC scanning**

So naturally I became interested in scanning servers for QUIC enabled services – after all, when we perform penetration tests, this should be part of our methodology.

I was sad to see that my favorite tool, nmap, cannot reliably scan QUIC enabled services. As UDP scanning is not easy anyway, due to specific packet contents that need to be generated, the very latest nmap is quite bad (and slow) in fingerprinting QUIC services, even when you enable all probes.

Couple of researchers extended zmap and added modules for QUIC scanning. This extended version is available at <https://github.com/tumi8/zmap> and it allows one to scan QUIC services – but zmap will only log initial data, if you want more information (i.e. to check for TLS certificates), you will need to use another tool released by same researchers – QScanner, which is available at <https://github.com/tumi8/qscanner>. It takes zmap’s CSV output and connects to QUIC services to fingerprint supported protocols (oh yeah, I forgot to mention that you can tweak QUIC protocols too, something similar to TCP flavors – but that’s for another diary). However, it supports only HTTP/3.

**Releasing quicmap**

As I felt that a simple tool that would allow for scanning of QUIC services as well as for fingerprinting supported Application Layer Protocol Negotiation (ALPN) protocols is missing, my colleague Fran ?utura and I made a simple QUIC scanner in Python that we call quicmap.

The scanner is available at <https://github.com/bojanisc/quicmap> and this first version allows you to scan arbitrary networks, hostnames and IP addresses as well as ports. The tool will run with 50 threads by default so it is quite fast, and the bonus feature is in brute forcing supported ALPN’s so we can identify if another protocol is supported. Fran even sped this up so we used binary searching to be as efficient as possible.

Here is what it looks like:

![](https://isc.sans.edu/diaryimages/images/QUIC3.png)

We already have plans for adding some additional features to make it more reliable in fingerprinting SMB specifically – this will be added in the upcoming days.

**Future abuse**

As QUIC is here and it will not go away, I think that we will probably see more abuse of this protocol in the future. Due to UDP being used, we already saw some Denial of Se...