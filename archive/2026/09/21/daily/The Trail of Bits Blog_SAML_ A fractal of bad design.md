---
title: SAML: A fractal of bad design
url: https://blog.trailofbits.com/2026/09/21/saml-a-fractal-of-bad-design/
source: The Trail of Bits Blog
date: 2026-09-21
fetch_date: 2026-09-22T07:03:32.866435
---

# SAML: A fractal of bad design

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# SAML: A fractal of bad design

[Matt Schwager](/authors/matt-schwager/)

September 21, 2026

[authentication](/categories/authentication/), [vulnerabilities](/categories/vulnerabilities/)

Page content

* [SAML and the birth of the SSO industry](#saml-and-the-birth-of-the-sso-industry)
* [A crack in the armor](#a-crack-in-the-armor)
* [A fractal of bad design](#a-fractal-of-bad-design)
  + [Built on XML](#built-on-xml)
  + [Canonicalization](#canonicalization)
  + [Enveloped signatures](#enveloped-signatures)
  + [“Kitchen-sink” design](#kitchen-sink-design)
  + [Ossification](#ossification)
* [All roads lead to OIDC](#all-roads-lead-to-oidc)

Born out of academia and raised in corporate IT departments, the Security Assertion Markup Language (SAML) authentication protocol continues to be a staple in these organizations. However, it’s time for it to retire. With the rise of software-as-a-service (SaaS) companies in the late aughts, IT departments needed a way for users to authenticate to many new web services. SAML and the burgeoning single sign-on (SSO) industry fulfilled this need. However, SAML is being crushed under the weight of its own complexity. It’s time to deprecate it and move on to modern alternatives like OpenID Connect (OIDC). In this post, I will explore the design-by-committee origin of SAML, its progression through the ranks in academic and corporate environments, its slow disintegration at the hands of the security research community, and its (hopeful) deprecation in favor of newer protocols.

![“SAML 101”](/2026/09/21/saml-a-fractal-of-bad-design/saml-a-fractal-of-bad-design-image-1.svg)

SAML 101

> What’s insidious about SAML is that it really is mostly straightforward to understand, but it’s built on a foundation of sand, bone dust, and ash; it works … if you assume XML signature validation is reliable. But XML signature validation is deeply cursed, and is so complicated that most fielded SAML implementations are wrapping libxmlsec, a gnarly C codebase nobody reads.
> — [Thomas Ptacek, 2023](https://news.ycombinator.com/item?id=37564758)

## SAML and the birth of the SSO industry

[Wikipedia tells me](https://en.wikipedia.org/wiki/SAML) that “SAML is an XML-based markup language for security assertions.” It was created in 2002 by the Organization for the Advancement of Structured Information Standards (OASIS) Security Services Technical Committee (SSTC). Okay, we’re not off to a great start by modern standards. XML, despite having some redeeming qualities, is quite complex compared to newer alternatives like JSON, but we’ll get more into that later. Further, a committee of subcommittees having meetings is a recipe for “kitchen-sink” protocol design (e.g., [waterfall methodology](https://en.wikipedia.org/wiki/Waterfall_model), [big design up front](https://en.wikipedia.org/wiki/Big_design_up_front), etc.). And sure enough, we’ve now jammed four (!) XML-based security protocols into one:

> … the following intellectual property was contributed to the SSTC:
>
> * Security Services Markup Language (S2ML) from Netegrity
> * AuthXML from Securant
> * XML Trust Assertion Service Specification (X-TASS) from VeriSign
> * Information Technology Markup Language (ITML) from Jamcracker
>
> — [SAML: History](https://en.wikipedia.org/wiki/SAML#History)

However, the desire for such a protocol was undeniable. As the internet shifted from Web 1.0 in the 90s to Web 2.0 in the early aughts, users and organizations needed an easy way to authenticate to many new web services. Academia was the biggest driver of this movement, although not the only one: Central Authentication Service (CAS) in 2002 at Yale, Shibboleth IdP in 2003 by Internet2, a consortium of research universities ([including my alma mater](https://its.umich.edu/enterprise/wifi-networks/researchers/internet2)), ADFS in 2003 by Microsoft, and simpleSAMLphp [around 2007](https://web.archive.org/web/20071214140857/http%3A//rnd.feide.no/simplesamlphp) by Uninett, a state-owned Norwegian company with close ties to academia. All these authentication projects eventually supported SAML in one way or another. Like ARPANET before it, universities were at the forefront of internet development and were the earliest consumers of web services. Once this base layer of protocol availability and nascent academic proving ground was established, the commercial industry took it and ran toward a multibillion dollar industry.

The SSO, identity, and authentication provider industry was also starting up in the early aughts, but really came to fruition a few years later: Ping Identity (2002), OneLogin (2009), Okta (2009), and Duo Security (2010). These companies were essentially built on the SAML protocol with the exception of Duo, who would introduce their first SSO product in 2015, which is where I come into the story. I worked on Duo’s first [on-premises Access Gateway product](https://duo.com/docs/dag) (DAG), which was built on simpleSAMLphp and, obviously, the SAML protocol. It’s where I became intimately familiar with the SAML protocol and spent many years of my life digesting its lengthy specifications. I was there when [Kelby Ludwig](https://kel.bz/) found the [XML comment bypass](https://i.blackhat.com/us-18/Thu-August-9/us-18-Ludwig-Identity-Theft-Attacks-On-SSO-Systems.pdf), but we will get into various attacks and SAML deficiencies later. Suffice it to say, the SSO and authentication provider industry was booming, and much of it was built on the SAML protocol.

## A crack in the armor

XML signature wrapping (XSW) attacks are the proverbial arrow to SAML’s heel. While there was earlier security research into both signature wrapping ([2005](https://dl.acm.org/doi/10.1145/1103022.1103026), [2008](https://arxiv.org/pdf/0812.4181), and [2009](https://lists.w3.org/Archives/Public/public-xmlsec/2009Nov/att-0019/Camera-Ready.pdf)) and SAML ([2008](https://dl.acm.org/doi/10.1145/1456396.1456397)), I consider the godfather of it all to be “On Breaking SAML: Be Whoever You Want to Be” ([2012](https://www.usenix.org/system/files/conference/usenixsecurity12/sec12-final91.pdf)). It tested theory against practice and resulted in [an automated way](https://github.com/CompassSecurity/SAMLRaider/blob/v2.5.2/src/main/java/helpers/XSWHelpers.java#L34-L39) to check for XSW attacks. This was our north star when implementing the DAG. It was the reason we chose simpleSAMLphp as our building block. PHP, [especially at the time](https://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/), was not exactly known for its security track record, but simpleSAMLphp’s spoke for itself. simpleSAMLphp was resilient to XSW at a time when nobody really knew what that was:

![simpleSAMLphp’s security track record (credit: On Breaking SAML)](/2026/09/21/saml-a-fractal-of-bad-design/saml-a-fractal-of-bad-design-image-2_hu_e836bff9fc613f68.webp)

simpleSAMLphp’s security track record (credit: On Breaking SAML)

Despite being front and center in this 2012 paper, XSW is [still present today](https://portswigger.net/research/the-fragile-lock). If we know the bug class, then why can’t we fix it? But before we get into SAML’s flaws we first have to consider the shaky ground it was built upon: XML.

XML is no slouch when it comes to a (lack of) security track record. [These bug classes](https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html) would have been more familiar to a developer in the 90s, but nonetheless are still present in XML today: XXE, entity expansion (“billion laughs”), DTD retrieval (SSRF), XPath/XQuery/XInclude/XSLT/CDATA injection, and more. A SAML library needs to handle all these bug classes before even getting to the actual SAML functionality.

In addition to security bug classes, there’s also the sheer complexity of XML when compared against something like J...