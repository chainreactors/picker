---
title: Abusing S4U2Self for Active Directory Pivoting
url: https://www.blackhillsinfosec.com/abusing-s4u2self-for-active-directory-pivoting/
source: Black Hills Information Security, Inc.
date: 2025-06-12
fetch_date: 2025-10-06T22:54:05.062187
---

# Abusing S4U2Self for Active Directory Pivoting

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
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
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

11
Jun
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Active Directory](https://www.blackhillsinfosec.com/tag/active-directory/), [Constrained Delegation](https://www.blackhillsinfosec.com/tag/constrained-delegation/), [Hunter Wade](https://www.blackhillsinfosec.com/tag/hunter-wade/), [Kerberos](https://www.blackhillsinfosec.com/tag/kerberos/), [S4U2Self](https://www.blackhillsinfosec.com/tag/s4u2self/)

# [Abusing S4U2Self for Active Directory Pivoting](https://www.blackhillsinfosec.com/abusing-s4u2self-for-active-directory-pivoting/)

by [Hunter Wade](https://hunio.org) | BHIS Intern

*Hunter recently graduated with his Master’s degree in Cyber Defense and has over two years of experience in penetration testing. His favorite area of testing is Active Directory, and in his free time, he enjoys working in his home lab and analyzing malware.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/06/s4u2self_header.png)

This blog has been cross-posted. We’re grateful to Hunter for allowing us to share this insightful work—you can check out the original post [HERE](https://hunio.org/posts/security/abusing-s4u2self-for-active-directory-pivoting/).

### **TL;DR**

If you only have access to a valid machine hash, you can leverage the Kerberos S4U2Self proxy for local privilege escalation, which allows reopening and expanding potential local-to-domain pivoting paths, such as SEImpersonate!

### **What is Kerberos?**

Kerberos is a **ticket-based** authentication protocol that enables secure communication in untrusted environments by first establishing mutual trust through a mutual third party. As a result, Kerberos requires three parties:

* **Client:** The user or system requesting access to a resource.
* **Server:** The destination resource the client wants to access.
* **Key Distribution Center (KDC):** A trusted third party responsible for authenticating users and issuing tickets.

The key reason for this approach to authentication is to minimize the need to send passwords over the network, reducing the risk of credential theft.

#### The Ticketing Process

Throughout the Kerberos authentication process, services are referred to by their SPN, or Service Principal Name. Thus, the ticket generation process is as follows:

1. **Authentication Service Request:** The client sends an authentication request encrypted with its password to the KDC.
2. **Authentication Service Response:** If the KDC can decrypt the request with the user’s password, the client has proven their identity. The KDC then responds with a Ticket-Granting-Ticket (TGT), encrypted with the KDC’s secret key.
3. **Ticket-Granting-Ticket Request:** The client will pass the TGT back to the KDC requesting access to a destination service.
4. **Ticket-Granting-Ticket Response:** If the KDC can decrypt the TGT, it proves the client presented a valid TGT, as no other entity has access to the KDC’s secret key. The KDC then responds with a Service Ticket (ST), encrypted with the destination service’s password.
5. **Service Ticket Request:** The client passes the ST to the destination service, requesting access. If the destination service can decrypt the service ticket, it proves the ticket is valid, as only the KDC and the service itself should possess the service’s password.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/S4U2Self-_01-500x362.png)

Through the trusted intermediary – the KDC – the client and destination service can establish trust, relying on the assumption that only the KDC possesses the secret credentials.

#### Kerberos Delegation – The Double-Hop Problem

Because of how Kerberos tickets work, servers have no means of forwarding client credentials to other resources, as they only have the service ticket encrypted with their own password. This is known as the **Kerberos Double-Hop Problem.**

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/S4U2Self-_02.png)

To solve this, Microsoft introduced Delegation, a feature that allows servers to forward client credentials to another service, enabling the second service to authenticate the client on behalf of the first server. Today, there are three forms of Kerberos delegation:

* **Unconstrained Delegation:** Unconstrained was the first form of delegation. When a client authenticates to a server configured with unconstrained delegation, the client will also pass their TGT alongside their ST allowing the destination to reuse the TGT to authenticate as that user to the next resource.
* **Constrained Delegation:*...