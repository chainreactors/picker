---
title: Investigating Surfshark and NordVPN with JA4T
url: https://medium.com/foxio/investigating-surfshark-and-nordvpn-with-ja4t-7bbf5a33aad0
source: Over Security - Cybersecurity news aggregator
date: 2024-05-19
fetch_date: 2025-10-06T16:49:36.498738
---

# Investigating Surfshark and NordVPN with JA4T

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7bbf5a33aad0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Ffoxio%2Finvestigating-surfshark-and-nordvpn-with-ja4t-7bbf5a33aad0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Ffoxio%2Finvestigating-surfshark-and-nordvpn-with-ja4t-7bbf5a33aad0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## FoxIO](https://medium.com/foxio?source=post_page---publication_nav-7ddaac9afbf4-7bbf5a33aad0---------------------------------------)

·

[![FoxIO](https://miro.medium.com/v2/resize:fill:76:76/1*WAO6aZG-6shir09RY2K2ng.png)](https://medium.com/foxio?source=post_page---post_publication_sidebar-7ddaac9afbf4-7bbf5a33aad0---------------------------------------)

FoxIO is a technology innovations company focused on creating simple, highly effective solutions to major industry problems.

# Investigating Surfshark and NordVPN with JA4T

[![John Althouse](https://miro.medium.com/v2/resize:fill:64:64/2*u7kgtidAMzS9ZD41CQWC9w.jpeg)](/%40jalthouse?source=post_page---byline--7bbf5a33aad0---------------------------------------)

[John Althouse](/%40jalthouse?source=post_page---byline--7bbf5a33aad0---------------------------------------)

8 min read

·

May 14, 2024

--

4

Listen

Share

Surfshark & NordVPN Route Certain Ports Through Proxies?

## TL;DR

This is an investigation of Surfshark and NordVPN using JA4TCP Fingerprinting.

We found that both Surfshark and NordVPN route certain ports through TCP proxies such as port 5060, which is only used for unencrypted phone calls. No other VPN providers proxy traffic in this way. The reason for the proxying is u̶n̶k̶n̶o̶w̶n̶ now known, see below. Additionally, we found that NordVPN’s proxy appears to be misconfigured, causing increased latency and bandwidth usage.

Resources:
**JA4+ Network Fingerprinting:** <https://github.com/FoxIO-LLC/ja4>
**JA4+ Blog:** <https://blog.foxio.io/ja4%2B-network-fingerprinting>
**JA4TCP Blog:** <https://blog.foxio.io/ja4t-tcp-fingerprinting>
**JA4TScan:** <https://github.com/FoxIO-LLC/ja4tscan>
**NMap:** <https://nmap.org/>
**gait:** <https://github.com/sandialabs/gait>

## Quick Refresher on JA4+ Fingerprinting

[JA4+](https://github.com/FoxIO-LLC/ja4) is a suite of network fingerprinting methods that are being implemented across the industry and consist of the following methods, with more being added on a regular basis:

![]()

For this investigation, we are primarily utilizing JA4TCP (JA4T). You can read up on how JA4T works in [this blog post](https://blog.foxio.io/ja4t-tcp-fingerprinting). In short, it’s a collection of artifacts from the TCP SYN and SYN-ACK packets which make up the TCP three-way handshake. These fingerprints allow us to fingerprint client and server operating systems, devices, certain applications, hosting/provider characteristics, if a connection is going through a tunnel, VPN or proxy, and enable us to troubleshoot network issues.

Press enter or click to view image in full size

![]()

![]()

For this blog, we will also be focusing on the Maximum Segment Size (MSS) part of the JA4T/S fingerprint. The MSS is the largest data payload size that a source will accept per packet, and is dependent on the overhead in the network connection. For example, the most common Maximum Segment Size (MSS) initially set is 1460, based on an ethernet Maximum Transmission Unit (MTU) of 1500. Observing an MSS of 1380 indicates that there is overhead on the network path, such as a tunnel or VPN, requiring a reduced MSS to account for it. Unique network conditions produce different amounts of overhead:

Press enter or click to view image in full size

![]()

Setting the MSS option to be larger than the actual available size will result in poor network performance, latency, and fragmentation. [MSS Clamping](https://www.cloudflare.com/learning/network-layer/what-is-mss/) is a common method used to avoid this issue.

## Surfshark & NordVPN Route Certain Ports Through Proxies?

Nord Security and Surfshark merged in 2022, and, together, they are the world’s largest VPN provider. While testing [JA4T](https://blog.foxio.io/ja4t-tcp-fingerprinting) through NordVPN and listening on the server side, I noticed something odd in my network logs. Connections over port 443 from NordVPN had a JA4T of *65535\_2–4–8–1–3\_1460\_9* (Unix), no matter what the client was. On the client side, I would see a normal-looking JA4T fingerprint where the MSS was 1380 (to account for the VPN overhead). So why does the server see a MSS of 1460? I tried connecting to the server using a different port, 8443, and only then did the server see the correct JA4T fingerprint of my client.

What is going on here? I did some further research, and here is what I found:

Observed network traffic on the **server** side:

Press enter or click to view image in full size

![]()

Why does the client TCP fingerprint change from Windows to Unix when connecting through Nord and Surfshark, but only over ports 80 and 443?

Observed network traffic on the **client** side:

Press enter or click to view image in full size

![]()

Why is the server’s TCP response fingerprint different when connecting through Nord and Surfshark, but only over ports 80 and 443?

When looking at latency measurements and hop counts with [JA4L](https://blog.foxio.io/ja4%2B-network-fingerprinting), I noticed that NordVPN and Surfshark would initiate the TCP three-way handshake from their exit node and that the hop counts were different, but only over ports 80 and 443. All of these observations led me to believe that NordVPN and Surfshark are rerouting certain ports to proxies that intercept the TCP connection.

To confirm this theory, I ran a SYN scan of all ports against an IP address for which no server exists. The scan should return no results since the destination server does not exist. However, both NordVPN and Surfshark responded on the following ports, which confirms that they are routing these ports through TCP proxies:

![]()

If you have NordVPN or Surfshark, you can test this yourself by running:

### nmap -v -Pn -n 203.0.113.100 (or use any other IP that is not in use)

![]()

[Telegram](https://telegram.org/) is a service that runs over several ports, including ports 80 and 443. Telegram does not use TLS but instead uses [MTProto](https://core.telegram.org/mtproto), a proprietary protocol that encrypts messages over several protocols, including HTTP. I connected directly to Telegram and then connected through NordVPN to see if there was a difference.

Press enter or click to view image in full size

![]()

When connecting directly, the client sends an HTTP POST to the server. The server responds with an ACK, then a FIN ACK to close the connection. When connecting over NordVPN, the client sends an HTTP POST to the server, the server responds with an HTTP 200 OK, and then both the client and the server send FIN ACKs to close the connection.

This discrepancy is interesting. I don’t know what the reason is, but it is repeatable.

I tested this with other VPN providers, including Private Internet Access and Proton VPN, but did not observe the same be...