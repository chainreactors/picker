---
title: Abusing Delegation with Impacket (Part 3): Resource-Based Constrained Delegation
url: https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-3/
source: Black Hills Information Security, Inc.
date: 2025-11-26
fetch_date: 2025-11-27T03:11:45.616578
---

# Abusing Delegation with Impacket (Part 3): Resource-Based Constrained Delegation

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

26
Nov
2025

[How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Active Directory](https://www.blackhillsinfosec.com/tag/active-directory/), [Hunter Wade](https://www.blackhillsinfosec.com/tag/hunter-wade/), [Impacket](https://www.blackhillsinfosec.com/tag/impacket/), [Kerberos](https://www.blackhillsinfosec.com/tag/kerberos/)

# [Abusing Delegation with Impacket (Part 3): Resource-Based Constrained Delegation](https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-3/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/HWade-150x150.png)

| [Hunter Wade](https://hunio.org/)

*Hunter recently graduated with his Master’s degree in Cyber Defense and has over two years of experience in penetration testing. His favorite area of testing is Active Directory, and in his free time, he enjoys working in his home lab and analyzing malware.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/del3_header.png)

This blog has been cross-posted. We’re grateful to Hunter for allowing us to share this insightful work—you can check out the original post in full [HERE](https://hunio.org/posts/security/abusing-delegation-with-impacket/).

This is the third in a three-part series of blog posts discussing how to abuse Kerberos delegation! If you haven’t already, feel free to read the [first blog post](https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-1-unconstrained-delegation/), as they discuss the Kerberos authentication process and how delegation plays an important role in solving the double-hop problem, and how to abuse unconstrained delegation. The [second blog post](https://www.blackhillsinfosec.com/abusing-delegation-with-impacket-part-2/) discusses how to abuse constrained delegation!

## What is resource-based constrained delegation?

Resource-based constrained delegation (RBCD) is similar to constrained delegation, but the resource itself controls which accounts can delegate to it. By default, a domain account can configure RBCD on themselves or any resource they control. This approach **lets the service decide who may delegate to it** instead of the domain.

## Resource-based constrained delegation abuse techniques

Resource-based constrained delegation is a bit of an outlier, primarily with how it’s configured. It alone provides little for pivoting or privilege escalation. Additionally, configuring RBCD oftentimes requires a host be compromised in some way, which quickly makes it a “chicken and the egg” situation.

That said, when you start to bring in CVEs and misconfigured permissions, RBCD becomes far more interesting. This writeup covers two primary methods that let an attacker arbitrarily manipulate RBCD permissions for services that haven’t yet been compromised:

1. Drop the MIC – CVE-2019-1040
2. GenericWrite DACL abuse (machine accounts)
3. GenericWrite DACL abuse (user SPNs)

### 1. Drop the MIC and configure RBCD

CVE-2019-1040 (Drop the MIC) bypasses SMB signing. By effectively “dropping the MIC” during SMB authentication, vulnerable hosts still accept connections even if they’re being relayed by an attacker. This can be leveraged to pivot protocols, like coercing SMB and to authenticating to LDAP, which allows configuring RBCD as a relayed host. This approach generally requires at least two domain controllers.

Assume we’ve compromised the user `user.one` with the password `Password1!`, which does not have any special permissions or configuration. Just a default user.

If we are in a domain with at least two domain controllers (`DC01` and `DC02`), with at least one of them being vulnerable to CVE-2019-1040 (`DC01`), we can leverage the basic permissions of this user to coerce authentication, relay the connection while dropping the MIC, and configuring resource based constrained delegation to trust an attacker-controlled resource for delegation.

The high-level steps are:

1. Compromise a user or machine in the domain.
2. Identify a domain controller vulnerable to CVE-2019-1040.
3. Coerce a second domain controller to authenticate to the attacker.
4. Drop the MIC and relay authentication to LDAP on the vulnerable domain controller.
5. Use this session to add a machine account via Machine Account Quota.
6. Use this session to trust the MAQ machine for delegation via RBCD.

**1. Find a machine vulnerable to CVE-2019-1040 (`10.0.1.202`)**

*NetExec [v1.4.0 SmoothOperator](https://www.netexec.wiki/news/v1.4.0-smoothoperator) has a remove-mic scanner now!*

```
nxc smb 10.0.1.202 -u 'user.one' -p 'Password1!' -M remove-mic
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/11/Del_67...