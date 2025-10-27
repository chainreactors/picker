---
title: Re: Microsoft PlayReady security research
url: https://seclists.org/fulldisclosure/2023/Mar/12
source: Full Disclosure
date: 2023-03-23
fetch_date: 2025-10-04T10:25:43.650949
---

# Re: Microsoft PlayReady security research

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# Re: Microsoft PlayReady security research

---

*From*: Adam Gowdiak <contact () agsecurityresearch com>
*Date*: Tue, 21 Mar 2023 11:05:31 +0100

---

```
Hello,
```

> ```
> I tried to reach out to CANAL+ instead, but without much success. CANAL+ company
> was clearly not interested to talk to me over this (no responses to e-mails and/or
> requests to establish an official communication channel for the reporting,
> discussion and vulnerabilities disclosure purposes).
> ```

```
I feel obliged to provide additional comments to this paragraph as I
start to believe that CANAL+ might not deserve sole blame here...

While Microsoft claims there is absolutely no bug at its end, I
personally start to perceive the company as the one that should be
also blamed to some extent.

Below, I am providing you with the reasons that has lead me to such a
conclusion.

For many months, no response from CANAL+ was taken at my end as a sign
of a complete ignorance and/or disrespect regarding the issues
discovered and affecting security of content served by CANAL+.

This conclusion was rather straightforward:
- I have reached out to multiple personnel at Canal+ France and
Poland, these were people at various levels (PR, CTO, CSO, security
persons). I got no response with one exception. Yet, I failed to
establish a communication channel (the one where I could provide
Canal+ with the research, codes, etc.).

A copy of my last message sent to CANAL+ is provided at this link:
https://security-explorations.com/materials/cplus_message.pdf

But, I have recently come across sample Microsoft PlayReady Server
agreement and they indicate that CANAL+ or any other PlayReady
licensee might not be able to:
- discuss any PlayReady related matters with a 3rd party (no response
from CANAL+ might have its origin in legal agreements / NDAs signed,
not necessarily company's ignorance to security matters)
- develop a fix / mitigation for PlayReady vulnerabilities (Microsoft
responsibility) conduct an in-depth investigation of PlayReady
security (no reverse engineering, etc.)
- improve PlayReady security (no custom changes to PlayReady protocol,
licensing mechanism, etc.)

The licensing implicates Microsoft's ownership and responsibility for
any changes to PlayReady. That alone may prohibit any innovation /
development by licensees aimed at improving security of content such
as the use of HW security features present in a target environment or
support for authentication through additional delegation tokens.
Sample ideas that could be considered in that content are presented in
a doc available for download from this location:
https://security-explorations.com/materials/mspr_ideas.pdf
(comments and critics are welcome, especially from crypto people)

The licensing also implicates that any updates to PlayReady are at the
sole discretion of Microsoft (it is up to Microsoft to fix issues,
improve security or implement support for various HW security
features).

This could possibly explain the reasons for no response from CANAL+
(along many other vendors from a PayTV industry).

This also puts Microsoft in a little bit different light at my end
too. As the owner of the tech that:
- is the Widest Deployed Content Protection Technology in the World,
- has been the most trusted DRM technology by studios and content
owners, and as a vendor claiming significant experience in a security
space, one would expect the company to simply do better.

By doing better, I have the following in mind (among others):
- provide obfuscation capabilities or obfuscated binaries as part of
PlayReady SDK (for various architectures such as Hitachi SH4 of
STi7111 SoC),
- provide means for dynamic and secure PlayReady secrets /
certificates upgrade (change), I haven't spotted anything in code that
would serve that goal,
- make use of and provide support for HW security features whenever
available (such as STi7111 - the chip was announced to be EOLed ~10
years ago, but it is still in use by many SAT TV providers in the
field),
- provide some basic functionality for authentication or templates
(servers side sample code) illustrating authentication use,
- provide answers to questions received from a researcher, I'd like to
learn from Microsoft whether the company considers PlayReady to be
providing any security of content in the context of a demonstrated STB
compromise (my findings indicate this is not the case, but I'd love to
learn of vendor's response). I'd also like to see whether Microsoft
can still support the claim that PlayReady can be used to "help
prevent the unauthorized use of content".

The list of questions sent to Microsoft is at this link:
https://security-explorations.com/materials/mspr_questions.pdf

Maybe instead of avoiding answers to questions related to PlayReady
security strengths, Microsoft should face the reality and admit that
PlayReady SDK (having several hundred licensees) doesn't provide
proper security of content and offer their licensees a free migration
/ upgrade to Azure Media Services whenever possible (Microsoft claims
that AMS is E2E content security solution, free of the limitations
exposed by my research) ?

Finally, let me say that Oracle, which had many more reasons to ignore
my person (Java security mess) has always delivered a response to my
inquiry...

Thank you.

Best Regards,
Adam Gowdiak

----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

### Current thread:

* [Re: Microsoft PlayReady security research](10) *Security Explorations (Mar 21)*
  + <Possible follow-ups>
  + **Re: Microsoft PlayReady security research** *Adam Gowdiak (Mar 21)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](h...