---
title: PlayReady Activation protocol issues (weak auth / fake client	identities)
url: https://seclists.org/fulldisclosure/2025/Aug/3
source: Full Disclosure
date: 2025-08-13
fetch_date: 2025-10-07T00:58:02.826786
---

# PlayReady Activation protocol issues (weak auth / fake client	identities)

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# PlayReady Activation protocol issues (weak auth / fake client identities)

---

*From*: Security Explorations <contact () security-explorations com>
*Date*: Tue, 12 Aug 2025 09:59:25 +0200

---

```
Dear All,

PlayReady Communication Protocols [1] include services for PlayReady
clients (such as Secure Clock), device owner's services (Activation /
Provisioning) and content service (License Server).

Back in 2022, we reported to Microsoft an issue pertaining to no auth at
PlayReady license server end, which was evaluated by Microsoft as no bug.

There is yet another auth issue, which builds on the above and affects
PlayReady Activation service used for initializing client identity [2]
certificates for Windows 10 / 11 clients.

PlayReady Activation service does not implement real authentication, but
some form of obfuscated identification scheme where static (shared) data
specific to PlayReady library is encrypted with the use of AES CTR algorithm
and sent along the key material (randomly chosen) to the server for
"authentication" purposes.

Arbitrary PlayReady identity can be requested by the client through public
API [3] and potentially abused for a successful license server access (such
as depicted in attack #5 [4]).

We verified that Microsoft PlayReady Activation service doesn't fully check
the validity of the HW / MF system identity sent as part of the request. As
a result, arbitrary fake identity (such as random one) can be used for leaf
certificate generation (and client identification). This can impact
attribution (identification of rogue clients).

Finally, there seems to be no limits on the number of PlayReady identities
requested for a given system identifier (such as fake one) or in a given
time frame. This can impact security of the whole ecosystem (vide massive
valid leaf certificates generation that can be abused and that are hard to
follow for revocation).

A ZIP archive containing sample fake PlayReady client identity (corresponding
to FAKE.PR.ID string) generated through the abuse of the Activation protocol
can be downloaded from this location:

https://security-explorations.com/samples/fake_pr_id.zip

Theoretically, publication of a partially compromised (and fake) PlayReady
certificate constitutes a security incident (violation of PlayReady Compliance
and/or Robustness Rules [5]). It's not clear if Microsoft is to revoke the
cert though (the last time it took company nearly 2 years to revoke a fully
compromised identity).

With respect to the fixing / security improvements, while we have not received
any information from Microsoft on the topic, our tests conducted for PlayReady
binaries available on Windows 10 22H2 build 19045.6093 from Jul 2025 indicate
no change to shared XOR keys. This could mean that Microsoft might have given
up to fix PlayReady on Windows 10, which is to be EOL'ed in Oct 2025.

Thank you.

Best Regards,
Adam Gowdiak

----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------

REFERENCES
[1] PlayReady Communication Protocols
    https://learn.microsoft.com/en-us/playready/overview/communication-protocols
[2] PlayReady Client Initialization
    https://learn.microsoft.com/en-us/playready/overview/initialization
[3] PlayReadyIndividualizationServiceRequest Class

https://learn.microsoft.com/en-us/uwp/api/windows.media.protection.playready.playreadyindividualizationservicerequest?view=winrt-26100
[4] Microsoft PlayReady WMRMECC256 Key / root key issue (attack #5)
    https://seclists.org/fulldisclosure/2024/Aug/15
[5] Compliance & Robustness Rules
    https://www.microsoft.com/playready/licensing/compliance/
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **PlayReady Activation protocol issues (weak auth / fake client identities)** *Security Explorations (Aug 12)*

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