---
title: The browser blind spot: Why your security tool may not be blocking what you think it is &#x5b;Guest Diary&#x5d;, (Wed, Jun 17th)
url: https://isc.sans.edu/diary/rss/33084
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-17
fetch_date: 2026-06-18T06:51:48.326285
---

# The browser blind spot: Why your security tool may not be blocking what you think it is &#x5b;Guest Diary&#x5d;, (Wed, Jun 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33080)
* [next](/diary/33086)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [The browser blind spot: Why your security tool may not be blocking what you think it is [Guest Diary]](/forums/diary/The%2Bbrowser%2Bblind%2Bspot%2BWhy%2Byour%2Bsecurity%2Btool%2Bmay%2Bnot%2Bbe%2Bblocking%2Bwhat%2Byou%2Bthink%2Bit%2Bis%2BGuest%2BDiary/33084/)

**Published**: 2026-06-17. **Last Updated**: 2026-06-17 16:01:33 UTC
**by** [Varun Murdula](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/The%2Bbrowser%2Bblind%2Bspot%2BWhy%2Byour%2Bsecurity%2Btool%2Bmay%2Bnot%2Bbe%2Bblocking%2Bwhat%2Byou%2Bthink%2Bit%2Bis%2BGuest%2BDiary/33084/#comments)

[This is a guest diary submitted by Varun Murdula]

### SUMMARY

CASB block policies rely on inspecting TCP traffic. QUIC, the protocol powering HTTP/3, runs over UDP, a protocol most CASBs cannot inspect. The result: Chrome can reach a destination your CASB is supposed to block, and nothing in the logs shows it happened. This article explains the gap, how to test for it, and what to do about it.
When a security team blocks access to a website or cloud service, the assumption is simple: the block is in place, so users cannot reach that destination. The rule is configured. The tool is running.

> "Job done. Time for coffee."

That assumption is often wrong. When it is, there is nothing in the logs to tell you.

I ran a test across five browsers on a managed endpoint with an active CASB policy. What I found is what this article describes. There is a real enforcement gap in how CASBs handle browser traffic. It is documented by the security vendors themselves, including published guidance from Palo Alto Networks, Forcepoint, and Cloudflare. But many security teams have never tested for it and do not know it applies to them. The tools are doing what they were designed to do. The way CASBs were built predates how browsers behave today. A block policy can look completely fine in every log and dashboard while traffic to the blocked destination flows freely through a different browser on the same machine.

### First, what is a CASB?

A Cloud Access Security Broker (CASB, pronounced “cazz-bee”) is a security tool that sits between an organization’s users and the internet. Gartner, which coined the term in 2012, defines it as “on-premises, or cloud-based security policy enforcement points, placed between cloud service consumers and cloud service providers to combine and interject enterprise security policies as the cloud-based resources are accessed.”10 In plain terms: it sits in the path of every internet connection and decides what gets through.

Proxy mode is the most common deployment for web traffic inspection. In this mode, every time a browser connects to a website or service, the CASB intercepts the request, checks it against policy rules, and either allows it or blocks it. It acts like a security checkpoint on every outbound internet connection.

CASBs are used to stop employees from sending sensitive data to places their organization does not permit: personal cloud storage, unauthorized file sharing tools, and generative AI chatbots where organizational policies may prohibit data sharing.

To inspect web traffic, a CASB needs to read the content of the connection, including encrypted ones. The vast majority of web traffic today is encrypted using Transport Layer Security (TLS). A protocol is a set of rules for how data travels across a network. TLS encrypts data in transit so only the sender and recipient can read it. It is the technology behind the padlock icon in your browser’s address bar.

To inspect TLS-encrypted traffic, a CASB performs SSL/TLS inspection (SSL stands for Secure Sockets Layer, TLS’s older predecessor). The CASB intercepts the connection and decrypts it. It then inspects the content, applies its policy, re-encrypts the traffic, and forwards it on. From the user’s side, nothing looks different. The padlock is still in the address bar.
For this to work, the CASB needs the browser to trust its re-signed certificates. It does that by installing a root Certificate Authority (CA) certificate into the device’s trusted certificate store, a list of credentials the device recognizes as legitimate. Once that certificate is there, the browser trusts the CASB’s re-signed traffic and continues normally.

This works fine, but not every browser on the device handles that certificate the same way.

### How QUIC creates a gap in your CASB coverage

Two things explain this gap.

The first is QUIC, a modern transport protocol developed by Google and standardized by the IETF.1 It was designed to make web connections faster and more reliable. It was not designed to circumvent enterprise security controls. This gap exists because proxy-based inspection tools were built around TCP, not because QUIC has a flaw. The name is not an acronym. Google just called it QUIC.

The second is the difference between TCP and UDP, the two transport mechanisms that determine whether your CASB ever sees the traffic.

TCP (Transmission Control Protocol) is the traditional protocol behind most internet traffic. Ordered, reliable, and what CASB SSL/TLS inspection is built around.

UDP (User Datagram Protocol) is a faster, lower-overhead alternative. It trades some of TCP’s reliability for speed and does not require the same connection handshake.

QUIC runs over UDP, not TCP. CASB inspection only works on TCP, so it never sees QUIC traffic.

> "Chrome took the side door. The CASB was watching the front."

QUIC is the transport behind HTTP/3 (the third version of the Hypertext Transfer Protocol, the language of the web). Chrome learns which servers support QUIC through previous connections, Alt-Svc headers, or DNS HTTPS records (RFC 9460), which let servers signal QUIC support before a connection even starts.9 Once Chrome knows a server supports QUIC, it tries it automatically. When that happens, the traffic goes over UDP. The CASB only monitors TCP, so it never sees the connection. No block fires and nothing is logged.

> KEY FINDING:  A user on a managed laptop can reach a destination the CASB is supposed to block, simply because Chrome used QUIC over UDP instead of TCP. The tool is running. The policy is active. The block does not fire.

These are not hypothetical concerns. Palo Alto Networks explicitly recommends blocking QUIC in their internet gateway security best practices.2 Forcepoint published a dedicated advisory documenting that QUIC traffic from Chrome, Edge, Brave, Firefox, and Safari may not be intercepted by their proxy.3 Cloudflare’s gateway documentation states directly: if the UDP proxy or TLS decryption is off, HTTP/3 traffic from Chrome bypasses inspection entirely. [4]

### The broader problem: Browsers do not all behave the same way

QUIC is the clearest example, but it is not the only way enforcement can fail across browsers.

When a CASB policy is set up and tested, it is usually tested once, from a single browser, and signed off as working. Most teams never verify whether the policy is enforced consistently across every browser on managed devices.

> "One browser tested. Zero browsers questioned. Ticket closed."

Keep Aware’s 2026 Browser Security Report makes the point clearly: DLP and CASB tools were built for a different era of computing, one defined by email attachments, file transfers, and endpoint storage.5 They were never designed for what people actually do in a browser today: typing sensitive data into a web form, pasting content into an AI chatbot, uploading files through a browser interface.

Some DLP tools enforce policy through a browser extension rather than a network proxy. That ex...