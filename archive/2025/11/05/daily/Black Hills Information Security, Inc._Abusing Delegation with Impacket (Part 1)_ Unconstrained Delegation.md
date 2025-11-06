---
title: Abusing Delegation with Impacket (Part 1): Unconstrained Delegation
url: https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-1/
source: Black Hills Information Security, Inc.
date: 2025-11-05
fetch_date: 2025-11-06T03:14:43.856726
---

# Abusing Delegation with Impacket (Part 1): Unconstrained Delegation

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

5
Nov
2025

[How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Active Directory](https://www.blackhillsinfosec.com/tag/active-directory/), [Hunter Wade](https://www.blackhillsinfosec.com/tag/hunter-wade/), [Impacket](https://www.blackhillsinfosec.com/tag/impacket/), [Kerberos](https://www.blackhillsinfosec.com/tag/kerberos/)

# [Abusing Delegation with Impacket (Part 1): Unconstrained Delegation](https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-1/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/HWade-150x150.png)

| [Hunter Wade](https://hunio.org/)

*Hunter recently graduated with his Master’s degree in Cyber Defense and has over two years of experience in penetration testing. His favorite area of testing is Active Directory, and in his free time, he enjoys working in his home lab and analyzing malware.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/del_header-1.png)

This blog has been cross-posted. We’re grateful to Hunter for allowing us to share this insightful work—you can check out the original post in full [HERE](https://hunio.org/posts/security/abusing-delegation-with-impacket/).

## The inspiration behind this

In Active Directory exploitation, Kerberos delegation is easily among my top favorite vectors of abuse, and in the years I’ve been learning Kerberos exploitation, I’ve noticed that Impacket doesn’t get nearly as much coverage as tools like Rubeus or Mimikatz.

From a penetration testing perspective, especially when operating from a remote dropbox, being able to interface Kali to the domain controller provides tremendous value, as we don’t need to drop binaries on disk, nor do we need to worry about host-based detections.

This is **not** an exhaustive list of every explicit delegation abuse path possible, otherwise I’d be working on this forever! Instead, I wanted to focus on each type of delegation configured for **both users and machines,** and the most common attack paths for each.

## Kerberos

Kerberos is a **ticket-based** authentication protocol that enables secure communication in untrusted environments by first establishing two-party trust through a mutual third party. Kerberos requires three parties:

* **Client:** The user or system requesting access to a resource.
* **Server:** The destination resource the client wants to access.
* **Key Distribution Center (KDC):** A trusted third party responsible for authenticating users and issuing tickets.

### The ticketing process

The Kerberos authentication flow works like this:

1. **Authentication Service Request:** The client sends an authentication request encrypted with their password to the KDC.
2. **Authentication Service Response:** If the KDC can decrypt the request with the user’s password, the client has proven their identity. The KDC then responds with a Ticket-Granting-Ticket (TGT), encrypted with the KDC’s secret key.
3. **Ticket-Granting-Ticket Request:** The client presents the TGT back to the KDC requesting access to a destination service.
4. **Ticket-Granting-Ticket Response:** If the KDC can decrypt the TGT, it proves the client presented a valid TGT, as no other entity knows the KDC’s secret key. The KDC responds with a Service Ticket (ST), encrypted with the destination service’s password.
5. **Service Ticket Request:** The client passes the ST to the destination service, requesting access. If the destination service can decrypt the service ticket, it proves the ticket is valid, as only the KDC and the service itself should possess the service’s password.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/09/Kerberos_01.png)

Through the trusted intermediary – the KDC – the client and destination service can establish trust, relying on the assumption that only the KDC knows everything.

Kerberos references services by their Service Principal Name, or SPN, and one ticket can be generated per one SPN at a time. For added efficiency, if a user wants to obtain tickets for multiple services, instead of performing the entire authentication process each time, they can simply reuse their TGT to obtain access to various other services. By default, [Microsoft states a TGT is valid for 10 hours](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-gpsb/0fce5b92-bcc1-4b96-9c2b-56397c3f144f) before the entire authentication process must fully begin again.

### The double-hop problem and delegation

Because of how tickets are constructed, services cannot forward client credentials to other resources: they only possess a service ticket encrypted with their own key. This inability to forward credenti...