---
title: New Win-DDoS Flaws Let Attackers Turn Public Domain Controllers into DDoS Botnet via RPC, LDAP
url: https://thehackernews.com/2025/08/new-win-ddos-flaws-let-attackers-turn.html
source: The Hacker News
date: 2025-08-11
fetch_date: 2025-10-07T00:49:52.609431
---

# New Win-DDoS Flaws Let Attackers Turn Public Domain Controllers into DDoS Botnet via RPC, LDAP

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [New Win-DDoS Flaws Let Attackers Turn Public Domain Controllers into DDoS Botnet via RPC, LDAP](https://thehackernews.com/2025/08/new-win-ddos-flaws-let-attackers-turn.html)

**Aug 10, 2025**Ravie LakshmananVulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3tlsxQOiYwyFsW_lhycutlJ1DR4E4kWwYK_t3KF0ywK3_b8k9cQGeLRBKyStWx2QWW9l34JTO7wKM0qYjz1fFOiXtBD8VZcJa5LmbYLruofCVzrTbXwXI1lemF6YhVC_SEzCEWLbLkhyphenhyphenXq4KUe5DlYKfjOxSia5lRtiB8zv0Q1qXBTXg91oxJukLKborD/s790-rw-e365/ddos.jpg)

A novel attack technique could be weaponized to rope thousands of public domain controllers (DCs) around the world to create a malicious botnet and use it to conduct powerful distributed denial-of-service (DDoS) attacks.

The approach has been codenamed Win-DDoS by SafeBreach researchers Or Yair and Shahak Morag, who [presented](https://defcon.org/html/defcon-33/dc-33-speakers.html#content_60389) their findings at the DEF CON 33 security conference today.

"As we explored the intricacies of the Windows LDAP client code, we discovered a significant flaw that allowed us to manipulate the URL referral process to point DCs at a victim server to overwhelm it," Yair and Morag said in a [report](https://www.safebreach.com/blog/win-dos-epidemic-abusing-rpc-for-dos-and-ddos/) shared with The Hacker News.

"As a result, we were able to create Win-DDoS, a technique that would enable an attacker to harness the power of tens of thousands of public DCs around the world to create a malicious botnet with vast resources and upload rates. All without purchasing anything and without leaving a traceable footprint."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In transforming DCs into a DDoS bot without the need for code execution or credentials, the attack essentially turns the Windows platform into becoming both the victim and the weapon. The attack flow is as follows -

* Attacker sends an RPC call to DCs that triggers them to become CLDAP clients
* DCs send the CLDAP request to the attacker's CLDAP server, which then returns a referral response that refers the DCs to the attacker's LDAP server in order to switch from UDP to TCP
* DCs then send the LDAP query to the attacker's LDAP server over TCP
* Attacker's LDAP server responds with an LDAP referral response containing a long list of LDAP referral URLs, all of which point to a single port on a single IP address
* DCs send an LDAP query on that port, causing the web server that may be served via the port to close the TCP connection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsFHy6nRHApDCqyOiEtYA3anfAXRfxqG_vogeEIx7hWInl5UYUPuQVYdUAQC_4sWPWXbyUSHiZpKed7zgLVKdgWYJzbOlpb9_3eiBUNgk_bCmsVNleXXbPGbma8BMAwi0IEcHsJ7hxMuhs8WbqzKVenAfj6XISz6yuD9wjZhyphenhyphen33rnrM2saMfFkxcVhutfH/s790-rw-e365/ddos-attack.jpg)

"Once the TCP connection is aborted, the DCs continue to the next referral on the list, which points to the same server again," the researchers said. "And this behavior repeats itself until all the URLs in the referral list are over, creating our innovative Win-DDoS attack technique."

What makes Win-DDoS significant is that it has high bandwidth and does not require an attacker to purchase dedicated infrastructure. Nor does it necessitate them to breach any devices, thereby allowing them to fly under the radar.

Further analysis of the LDAP client code referral process has revealed that it's possible to trigger an LSASS crash, reboot, or a blue screen of death ([BSoD](https://en.wikipedia.org/wiki/Blue_screen_of_death)) by sending lengthy referral lists to DCs by taking advantage of the fact that there are no limits on referral list sizes and referrals are not released from the DC's heap memory until the information is successfully retrieved.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigKl4VLSXdH04pw1X3aOTXd-bcd4ueA4sp9n-18f4zl7mgzXaa4KWC6kBr6MFaT6oGMwa7k4eQR0BCwNzqms8663fXbgqXLdHVlHmwXVg7JP65Joe6tWpt7j8Ho0HOEiyI-4af9JNn1oIsfQocJ_QwqzFgDP_apifrtYTcPwUupE_BSJDVET9sGa37OlS_/s790-rw-e365/ms-flow.jpg)

Win-DDoS turns this behavior on its head by providing a machine with a referral list that refers to a victim to be targeted, instead of crashing the system by providing it a huge amount of referral that can exhaust the domain controller's resources. This opens the door to a scenario where public Domain Controllers worldwide can be targeted to send LDAP packets to any IP and port of the attacker's choosing.

Given that [domain controllers](https://www.digitalguardian.com/blog/what-domain-controller-definitions-functions-benefits-limitations-and-mor) rely heavily on RPC to function, particularly for authentication, user management, and service management, SafeBreach found that it's possible to employ a denial-of-service (DoS) technique called TorpeDoS against RPC servers.

"TorpeDoS is a technique that we invented which creates the impact of a DDoS, but from a single computer," SafeBreach told The Hacker News. "It doesn't use many different computers worldwide to create a DDoS, it just improves the efficiency of RPC-call-rate by so much that the impact of a single computer implementing TorpeDoS is equivalent to the impact of a DDoS attack made by tens of thousands of computers."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

On top of that, the transport-agnostic code that's executed to server client requests has been found to harbor three new denial-of-service (DoS) vulnerabilities that can crash domain controllers without the need for authentication, and one additional DoS flaw that provides any authenticated user with the ability to crash a domain controller or Windows computer in a domain.

The identified shortcomings are listed below -

* **[CVE-2025-26673](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26673)** (CVSS score: 7.5) - Uncontro...