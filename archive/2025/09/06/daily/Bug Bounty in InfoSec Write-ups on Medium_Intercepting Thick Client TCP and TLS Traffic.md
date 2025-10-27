---
title: Intercepting Thick Client TCP and TLS Traffic
url: https://infosecwriteups.com/intercepting-thick-client-tcp-and-tls-traffic-72fab07fffe7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-06
fetch_date: 2025-10-02T19:44:34.473796
---

# Intercepting Thick Client TCP and TLS Traffic

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F72fab07fffe7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fintercepting-thick-client-tcp-and-tls-traffic-72fab07fffe7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fintercepting-thick-client-tcp-and-tls-traffic-72fab07fffe7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-72fab07fffe7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-72fab07fffe7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Intercepting Thick Client TCP and TLS Traffic

[![Sourav Kalal](https://miro.medium.com/v2/resize:fill:64:64/1*3dHIoCEZxeENLBxleec9sw.png)](https://blog.souravkalal.tech/?source=post_page---byline--72fab07fffe7---------------------------------------)

[Sourav Kalal](https://blog.souravkalal.tech/?source=post_page---byline--72fab07fffe7---------------------------------------)

4 min read

·

Sep 5, 2025

--

Listen

Share

Intercepting and analysing the traffic is one of the important parts of the pentest, whether it’s a mobile, web or desktop application. On the web, it’s easy to intercept. In the case of mobile applications, it’s easy to intercept unless there are security mitigation implementations, but those are often bypassed. In all those cases, the web or mobile app protocol used is HTTP/s, which means we have the option to intercept easily via BurpSuite.

When it comes to a Desktop Thick client application, it’s always easy to intercept when the HTTP/S protocol is used. In some rare cases, it requires different methods, and to intercept HTTP/s, but it’s always possible as we have different tools and proxy applications like BurpSuite, ZAP available to intercept the HTTP/s traffic. In many cases, applications don’t use the HTTP protocol, instead, they use different protocols. In most cases, it’s based on a protocol or custom protocol and with TLS, which makes it hard to intercept, as there are no direct, easy solutions to intercept on TCP+TLS traffic.

We can set up the MITMProxy application, but it requires multiple setups and does not always work with non-TCP + TLS traffic.

To make things easy, similar to BurpSuite, like single click install and setup proxy, I have created InterceptSuite, which uses Socks5 proxy, with 1 click installation and easy to intercept and modify the tick client TCP and TLS traffic with a modern GUI.

To get started, go to the InterceptSuite GitHub Repository, navigate to the release page and download the installer EXE for Windows, PKG for MacOS or RPM, Deb, and App Image file for Linux.

[## GitHub - InterceptSuite/InterceptSuite: A TLS MITM proxy for Non-HTTP traffic, with support for TLS…

### A TLS MITM proxy for Non-HTTP traffic, with support for TLS upgrades like STARTTLS, PostgreSQL, and more. …

github.com](https://github.com/InterceptSuite/InterceptSuite/?source=post_page-----72fab07fffe7---------------------------------------)

If not, you can directly download it from the [InterceptSuite website](http://interceptsuite.com/Download).

To test the TCP Intercept, I am using the BetaFast Vulnerable Thick Client application.

[## GitHub - NetSPI/BetaFast: Vulnerable thick client applications used as examples in the Introduction…

### Vulnerable thick client applications used as examples in the Introduction to Hacking Desktop Applications blog series …

github.com](https://github.com/NetSPI/BetaFast?source=post_page-----72fab07fffe7---------------------------------------)

InterceptSuite make use of Socks5 Proxy; for some reason, Windows does not support Socks proxy. In order to redirect the application traffic to any proxy server, including for an unaware application, the best option is Proxifier.

Press enter or click to view image in full size

![]()

Install and open the Proxifier application and navigate to the Profile → Proxy Server.

Press enter or click to view image in full size

![]()

Click on the Add button and enter the interceptSuite proxy server IP and port. Default is 127.0.0.1 port 4444, select protocol as SOCKS Version 5.

We can now configure Proxifier to redirect traffic from specific applications, IP addresses, or ports to the proxy. To do this, navigate to Profile → Proxyification Rules.

Press enter or click to view image in full size

![]()

We need to create two rules: the first rule will redirect the thick client traffic to our proxy application.

Press enter or click to view image in full size

![]()

The second rule will ensure that the traffic for the proxy application, which is InterceptSuite, goes directly to the server and does not go through the proxy again. This is important to prevent an endless redirect loop.

Press enter or click to view image in full size

![]()

To view the TCP data between the BetaBank application and the server, open the BetaBank application, submit your credentials, and then navigate to the proxy history in InterceptSuite.

Press enter or click to view image in full size

![]()

No more complex setup, just plug in InterceptSuite and start analysing TCP and TLS traffic instantly.

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----72fab07fffe7---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----72fab07fffe7---------------------------------------)

[Application Security](https://medium.com/tag/application-security?source=post_page-----72fab07fffe7---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----72fab07fffe7---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----72fab07fffe7---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--72fab07fffe7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--72fab07fffe7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--72fab07fffe7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--72fab07fffe7---------------------------------------)

·[Last published 4 days ago](/ho...