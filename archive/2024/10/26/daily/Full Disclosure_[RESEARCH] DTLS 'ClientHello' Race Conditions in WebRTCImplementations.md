---
title: [RESEARCH] DTLS 'ClientHello' Race Conditions in WebRTC	Implementations
url: https://seclists.org/fulldisclosure/2024/Oct/6
source: Full Disclosure
date: 2024-10-26
fetch_date: 2025-10-06T18:59:46.245720
---

# [RESEARCH] DTLS 'ClientHello' Race Conditions in WebRTC	Implementations

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# [RESEARCH] DTLS 'ClientHello' Race Conditions in WebRTC Implementations

---

*From*: Sandro Gauci via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 22 Oct 2024 09:17:53 +0200

---

```
Dear Full Disclosure community,

We've released a white paper detailing a critical vulnerability affecting multiple WebRTC implementations: "DTLS
'ClientHello' Race Conditions in WebRTC Implementations".

White paper: https://www.enablesecurity.com/research/webrtc-hello-race-conditions-paper.pdf

Key points:

1. Vulnerability: Failure to properly verify the origin of DTLS "ClientHello" messages in WebRTC sessions.
2. Impact: Potential for denial of service attacks.
3. Affected implementations (all Open-Source projects have been patched in latest versions):
   - RTPEngine
   - Asterisk
   - FreeSWITCH
   - Skype (PSTN)

4. Tested but not vulnerable:
   - Janus, Discord, Dolby.io, Facebook Messenger, Google Meet, LiveKit Meet, Webex, Zoho Meeting, Zoom, Mediasoup

5. Root cause: Not a specification bug, but a common implementation oversight.

Methodology:
- Extensive testing on open-source and proprietary WebRTC implementations
- Focus on media servers and popular communication platforms

This research expands on our previous blog post, providing more comprehensive details and analysis.

We invite the community to review our findings, methodology, and recommendations. Your feedback and further research
into WebRTC security is welcome.

--

    Sandro Gauci, CEO at Enable Security GmbH

    Register of Companies:       AG Charlottenburg HRB 173016 B
    Company HQ:                       Neuburger StraÃŸe 101 b, 94036 Passau, Germany
    RTCSec Newsletter:               https://www.rtcsec.com/subscribe
    Our blog:                                https://www.rtcsec.com
    Other points of contact:       https://www.enablesecurity.com/contact/
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

### Current thread:

* **[RESEARCH] DTLS 'ClientHello' Race Conditions in WebRTC Implementations** *Sandro Gauci via Fulldisclosure (Oct 24)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")