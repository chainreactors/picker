---
title: Microsoft Office Online Server Remote Code Execution
url: https://www.mdsec.co.uk/2022/10/microsoft-office-online-server-remote-code-execution/
source: Penetration testing Archives - MDSec
date: 2022-10-20
fetch_date: 2025-10-03T20:26:51.426546
---

# Microsoft Office Online Server Remote Code Execution

* Our Services
* Knowledge Centre
* [About](https://www.mdsec.co.uk/about/)
* [Contact](https://www.mdsec.co.uk/contact/)

* Our Services
  + [Adversary Simulation](https://www.mdsec.co.uk/our-services/adversary-simulation/)
  + [Application Security](https://www.mdsec.co.uk/our-services/application-security/)
  + [Penetration Testing](https://www.mdsec.co.uk/our-services/penetration-testing/)
  + [Response](https://www.mdsec.co.uk/our-services/response/)
* Knowledge Centre
  + [Insights](https://www.mdsec.co.uk/knowledge-centre/insights/)
  + [Research](https://www.mdsec.co.uk/knowledge-centre/research/)
  + [Training](https://www.mdsec.co.uk/knowledge-centre/training/)
* [About](https://www.mdsec.co.uk/about/)
* [Contact](https://www.mdsec.co.uk/contact/)

* [![Adversary](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-adversary.svg)

  ## Adversary Simulation

  Our best in class red team can deliver a holistic cyber attack simulation to provide a true evaluation of your organisation’s cyber resilience.](https://www.mdsec.co.uk/our-services/adversary-simulation/)
* [![Application Security](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-application-security.svg)

  ## Application Security

  Leverage the team behind the industry-leading Web Application and Mobile Hacker’s Handbook series.](https://www.mdsec.co.uk/our-services/applicaton-security/)
* [![Penetration Testing](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-penetration-testing.svg)

  ## Penetration Testing

  MDSec’s penetration testing team is trusted by companies from the world’s leading technology firms to global financial institutions.](https://www.mdsec.co.uk/our-services/penetration-testing/)
* [![Response](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-response.svg)

  ## Response

  Our certified team work with customers at all stages of the Incident Response lifecycle through our range of proactive and reactive services.](https://www.mdsec.co.uk/our-services/response/)

* [## Research

  MDSec’s dedicated research team periodically releases white papers, blog posts, and tooling.](https://www.mdsec.co.uk/knowledge-centre/research/)
* [## Training

  MDSec’s training courses are informed by our security consultancy and research functions, ensuring you benefit from the latest and most applicable trends in the field.](https://www.mdsec.co.uk/knowledge-centre/training/)
* [## Insights

  View insights from MDSec’s consultancy and research teams.](https://www.mdsec.co.uk/knowledge-centre/insights/)

ActiveBreach

# Microsoft Office Online Server Remote Code Execution

[Home](https://www.mdsec.co.uk/) >
[Knowledge Centre](https://www.mdsec.co.uk/knowledge-centre/) >
[Insights](https://www.mdsec.co.uk/knowledge-centre/insights) >
Microsoft Office Online Server Remote Code Execution

Microsoft’s [Office Online Server](https://learn.microsoft.com/en-us/officeonlineserver/office-online-server-overview) is the next generation of Office Web Apps Server; it provides a browser based viewer/editor for Word, PowerPoint, Excel and OneNote documents. The product can be integrated with SharePoint to provide web based access to these documents within Sharepoint.

During a routine penetration test, MDSec discovered a Server-Side Request Forgery vulnerability that, under the right conditions, can be exploited to achieve remote code execution on the Office Online Server itself.

## The Vulnerability

The */op/view.aspx* endpoint within Office Online Server is intended to be used for retrieving Office documents from remote resources and displaying them within the browser. The endpoint is affected by a classic Server-Side Request Forgery, whereby providing it with a HTTP(s) or UNC location will initiate a connection from the application.

MDSec witnessed this vulnerability within Office Online Server versions 16.0.10338.20039 and below.

## Exploitation

The aforementioned vulnerable endpoint can be exploited using a simple, unauthenticated GET request. The example below illustrates how internal resources can be fingerprinted using timing based attacks to identify valid IP addresses:

![](https://www.mdsec.co.uk/wp-content/uploads/2022/10/image-17-960x791.png)

While enumeration is interesting, code execution is better. During analysis, it was further noted that the connections from Office Online Server were performed using the machine account of the host, facilitating coerced authentication. This of course raises some interesting options for exploitation, as the machine account can be relayed to other resources such as LDAP (to add shadow credentials) or Active Directory Certificate Services (to recover a client certificate for PKINIT authentication).

Assuming the Office Online Server is able to access an attacker controlled SMB server, the SSRF can be submitted to [ntlmrelayx](https://github.com/SecureAuthCorp/impacket/blob/master/examples/ntlmrelayx.py) and subsequently relayed to ADCS, as shown below:

![](https://www.mdsec.co.uk/wp-content/uploads/2022/10/image-18-960x549.png)

Using the certificate, it is possible to obtain a TGT for the server:

![](https://www.mdsec.co.uk/wp-content/uploads/2022/10/image-20-960x659.png)

Using the TGT, a s4u2Self request can be made to receive a forged service ticket for the server, leading to local administrator privileges on the Office Online Server host:

![](https://www.mdsec.co.uk/wp-content/uploads/2022/10/image-21-960x571.png)

A similar end result could almost certainly be achieved by leveraging ntlmrelayx to relay to LDAP and to perform a shadow credential attack, but this is left as an exercise for the reader.

MDSec informed Microsoft MSRC of this vulnerability, but it was considered intended use for the endpoint and determined to be a “won’t fix”.

## Timeline

**23/08/2022** – MDSec provide a description of the SSRF to MSRC.

**12/09/2022** – MSRC indicate that this feature is by design and that as a mitigation, Internet connected servers should “lock down ports and any accounts on that farm to have least privilege”. Additionally, setting the *OpenFromUNCEnabled* flag to false can disable this feature.

This blog post was written by [Manish Tanwar](https://twitter.com/IndiShell1046).

![](https://secure.gravatar.com/avatar/9cb7b62409a4b5ef00769dca4ba852fc49229c9729d600fc2637daf77068c31c?s=96&d=wp_user_avatar&r=g)

written by

#### MDSec Research

## Ready to engage with MDSec?

[Get in touch](https://www.mdsec.co.uk/contact)

Stay updated with the latest
news from MDSec.

Newsletter Signup Form

Email

If you are human, leave this field blank.

Submit

[![MDsec](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/mdsec-logo.svg)](https://www.mdsec.co.uk "MDSec")

### Services

* [Adversary Simulation](https://www.mdsec.co.uk/our-services/adversary-simulation/)
* [Application Security](https://www.mdsec.co.uk/our-services/applicaton-security/)
* [Penetration Testing](https://www.mdsec.co.uk/our-services/penetration-testing/)
* [Response](https://www.mdsec.co.uk/our-services/response/)

### Resource Centre

* [Research](https://www.mdsec.co.uk/knowledge-centre/research/)
* [Training](https://www.mdsec.co.uk/knowledge-centre/training/)
* [Insights](https://www.mdsec.co.uk/knowledge-centre/insights/)

### Company

* [About](https://www.mdsec.co.uk/about/)
* [Contact](https://www.mdsec.co.uk/contact/)
* [Careers](https://www.mdsec.co.uk/careers/)
* [Privacy](https://www.mdsec.co.uk/privacy-policy/)

t: +44 (0) 1625 263 503
e: contact@mdsec.co.uk

32A Park Green
Macclesfield
Cheshire
SK11 7NA

### Accreditations

![Best](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/logos/best.png)

![IT Health Check Service](https://www.mdsec.co.uk/wp-content/uploads/2019/11/check-whitetrans.png)

![Crest Star](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/logos/crest-star.png)

![Crest](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/logos/crest.png)

![Cyber Essentials](https://www.mdsec...