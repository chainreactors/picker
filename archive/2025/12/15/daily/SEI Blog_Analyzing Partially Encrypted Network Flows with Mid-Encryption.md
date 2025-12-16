---
title: Analyzing Partially Encrypted Network Flows with Mid-Encryption
url: https://www.sei.cmu.edu/blog/analyzing-partially-encrypted-network-flows-with-mid-encryption/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2025-12-15
fetch_date: 2025-12-16T03:24:35.766605
---

# Analyzing Partially Encrypted Network Flows with Mid-Encryption

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Our Work

Publications

News and Events

Education and Outreach

Careers

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. Analyzing Partially Encrypted Network Flows with Mid-Encryption

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Ibarra, S., and Thomas, M., 2025: Analyzing Partially Encrypted Network Flows with Mid-Encryption. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed December 15, 2025, https://doi.org/10.58012/8s4r-zp63.

Copy

APA Citation

Ibarra, S., & Thomas, M. (2025, December 15). Analyzing Partially Encrypted Network Flows with Mid-Encryption. Retrieved December 15, 2025, from https://doi.org/10.58012/8s4r-zp63.

Copy

Chicago Citation

Ibarra, Steven, and Mark Thomas. "Analyzing Partially Encrypted Network Flows with Mid-Encryption." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, December 15, 2025. https://doi.org/10.58012/8s4r-zp63.

Copy

IEEE Citation

S. Ibarra, and M. Thomas, "Analyzing Partially Encrypted Network Flows with Mid-Encryption," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 15-Dec-2025 [Online]. Available: https://doi.org/10.58012/8s4r-zp63. [Accessed: 15-Dec-2025].

Copy

BibTeX Code

@misc{ibarra\_2025,
author={Ibarra, Steven and Thomas, Mark},
title={Analyzing Partially Encrypted Network Flows with Mid-Encryption},
month={{Dec},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/8s4r-zp63},
note={Accessed: 2025-Dec-15}
}

Copy

# Analyzing Partially Encrypted Network Flows with Mid-Encryption

![Headshot of Steven Ibarra](/media/images/sibarra.max-180x180.format-webp.webp)
![Headshot of Mark Thomas.](/media/images/mthomas.max-180x180.format-webp.webp)

###### [Steven Ibarra](/authors/steven-ibarra) and [Mark Thomas](/authors/mark-thomas)

###### December 15, 2025

##### PUBLISHED IN

[Situational Awareness](/blog/topics/situational-awareness/)

##### CITE

<https://doi.org/10.58012/8s4r-zp63>

Get Citation

##### SHARE

Encrypted traffic has come to dominate network flows, which makes it difficult for traditional flow monitoring tools to maintain visibility. This is particularly true when the process to enable encryption occurs after an initial data exchange, causing the encryption attributes to be missed.

In this blog post we take a closer look at a new feature added to CERT’s [Yet Another Flowmeter tool (YAF)](https://tools.netsa.cert.org/yaf2/) to capture the attributes of encryption when it occurs after the start of the session. We call this *mid-encryption*. We explore what mid-encryption means, why it matters, how it works within YAF, and what benefits this brings to traffic analysis and network security teams.

From 2014 to 2024, we saw a steady increase in the percentage of traffic that is encrypted with [more than 80 percent of pages loaded by Firefox](https://letsencrypt.org/stats/#percent-pageloads) and [96 percent of traffic across Google](https://transparencyreport.google.com/archive/https/overview) being encrypted.

CERT researchers developed [Yet Another Flowmeter (YAF)](https://tools.netsa.cert.org/yaf2/) 20 years ago to read network packets and create [Internet Protocol Flow Information Export (IPFIX)](https://en.wikipedia.org/wiki/IPFIX) network flow records—where each record summarizes a connection between two hosts (a network session. The infrequent use of encryption at that time meant YAF had full visibility into many of these records: YAF was able to capture the metadata of various connections, including: HTTP for web sites, [Simple Mail Transport Protocol (SMTP)](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol), [Internet Message Access Protocol (IMAP)](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol), and [Post Office Protocol v3 (POP3)](https://en.wikipedia.org/wiki/Post_Office_Protocol).

For connections that started with an encryption request, YAF could capture attributes of the encrypted session (the [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) ClientHello and ServerHello) and the certificates used for encryption. Although the encrypted session itself was opaque, the captured attributes allowed network analysts to verify that certificates were legitimate, and the connection was properly encrypted.

## What is Mid-Encryption?

Mid-encryption refers to a network session beginning in an unencrypted (usually text-based) state and transitioning to an encrypted state during the same session. This action is triggered using mechanisms such as `STARTTLS`, a command used in application-layered protocols (e.g., [Simple Mail Transfer Protocol](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol), [Internet Message Access Protocol](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol), [Extensible Messaging and Presence Protocol](https://en.wikipedia.org/wiki/XMPP%22)) that begins encryption using TLS.
Typically flow sensors label the session as *encrypted* or *unencrypted* by examining the beginning of the session. While this process usually helps with labeling the correct protocol and capturing the metadata, commands such as `STARTTLS` may lead to potential loss of visibility and metadata because they launch the encryption process during the session.

## Why Mid-Encryption Support Matters

Today’s HTTP traffic is largely encrypted, but older protocols often use an opportunistic encryption model that is easier to implement and allows servers and clients to communicate when both parties do not support encryption. With opportunistic encryption, a session starts in plain text before negotiations for encryption occur via a `STARTTLS` or `HTTPS` upgrade. Early session metadata is available to the sensor, while the rest may be nontransparent.

Without mid-encryption support, YAF may miss the indicators of when encryption occurs and fail to label the session correctly. This scenario could lead to partial loss of visibility—we don’t know if encryption was successful—and incorrectly labeled flow records, which may lead to analysts needlessly investigating benign traffic.With mid-encryption support, YAF can capture early metadata during the clear-text phase, detect and capture the encryption indicators (e.g., `STARTTLS` string), annotate the flow accurately, provide TLS handshake metadata, and compute JA3 fingerprints from the metadata. The fingerprints provide a quick why to distinguish legitimate traffic from malicious traffic and to detect the use of weak or revoked certificates.

## Mid Encryption Capabilities

With the new feature, YAF can now track protocol negotiations in real time and identify encryption flags (like the `STARTTLS` command or TLS ClientHello). The [Internet Protocol Flow Information Export (IPFIX)](https://en.wikipedia.org/wiki/IP_Flow_Information_Export) records it generates are enriched with encryption information: when the encryption began, what protocol was negotiated, and which portions of the flow are encrypted or clear text. The record also includes TLS ClientHello metadata: TLS version, cipher suites offered and selected, and server certificate details.

Mid encryption is useful with protocols that still allow clear text preludes before upgrading, such as SMTP, POP3, IMAP, [Network News Transport Protocol (NNTP)](https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol), [Lightweight Directory Access Protocol (LDAP)](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol), XMPP, and [IRC](https://en.wikipedia.org/wiki/IRC).

## E...