---
title: Azure AD Kerberos Tickets: Pivoting to the Cloud
url: https://www.trustedsec.com/blog/azure-ad-kerberos-tickets-pivoting-to-the-cloud/
source: TrustedSec
date: 2023-02-10
fetch_date: 2025-10-04T06:15:54.390463
---

# Azure AD Kerberos Tickets: Pivoting to the Cloud

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Azure AD Kerberos Tickets: Pivoting to the Cloud](https://trustedsec.com/blog/azure-ad-kerberos-tickets-pivoting-to-the-cloud)

February 09, 2023

# Azure AD Kerberos Tickets: Pivoting to the Cloud

Written by
Edwin David

Active Directory Security Review
Cloud Assessment
Cloud Baseline Configuration Review
Cloud Penetration Testing
Penetration Testing
Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AzureADKerberos_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695564570&s=dd72909416f724d250b4e9fd2a0679f5)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#9fa0eceafdf5fafceba2dcf7fafcf4baadaff0eaebbaadafebf7f6ecbaadaffeedebf6fcf3fabaadaff9edf0f2baadafcbedeaecebfafbccfafcbaadaeb9fef2efa4fdf0fbe6a2dee5eaedfabaadafdedbbaadafd4faedfdfaedf0ecbaadafcbf6fcf4faebecbaacdebaadafcff6e9f0ebf6f1f8baadafebf0baadafebf7fabaadafdcf3f0eafbbaacdebaadaff7ebebefecbaacdebaadd9baadd9ebedeaecebfafbecfafcb1fcf0f2baadd9fdf3f0f8baadd9fee5eaedfab2fefbb2f4faedfdfaedf0ecb2ebf6fcf4faebecb2eff6e9f0ebf6f1f8b2ebf0b2ebf7fab2fcf3f0eafb "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazure-ad-kerberos-tickets-pivoting-to-the-cloud "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Azure%20AD%20Kerberos%20Tickets%3A%20Pivoting%20to%20the%20Cloud%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazure-ad-kerberos-tickets-pivoting-to-the-cloud "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazure-ad-kerberos-tickets-pivoting-to-the-cloud&mini=true "Share on LinkedIn")

If you've ever been doing an Internal Penetration test where you've reached Domain Admin status and you have a cloud presence, your entire Azure cloud can still be compromised. In this blog, I'll take you through this scenario and show you the dangers of machine account SSO compromise. We will do so without extracting any user account hashes and will have the ability to impersonate any account without MFA to achieve full cloud dominance.

## **Scenario:**

While an Internal Penetration test was being conducted, a service account with backup privileges to a Domain Controller (DC) was compromised. The team conducting the test was able to achieve full internal domain compromise. Using [***SecretsDump***](https://github.com/fortra/impacket/blob/master/examples/secretsdump.py), the team extracted the machine account, **AZUREADSSOACC$**. This indicates that Azure SSO may be enabled in the target tenant.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-1.png)

To confirm Azure SSO was in use in this hybrid environment, ***AADInternals*** was used to perform reconnaissance on the Azure environment as an outsider. ***AADInternals*** can be obtained from the PowerShell Gallery or from GitHub. We can perform reconnaissance with the following command:

`Invoke-AADIntReconAsOutsider -Domain domain.local | Format-Table`

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-2.png)

Figure 2 - Initial Azure Tenant Enumeration With AADInternals

Now that we have confirmed that SSO is in use, we will need to do some initial reconnaissance of the Azure environment. First, we will need to pick out a user. Service accounts are preferred since they are normally not backed with any form of MFA. One common issue that occurs when an enterprise syncs Azure AD for the first time, is that they will sync all on-premises AD environment IDs to the cloud. Service accounts can easily be pulled from an internal foothold in an AD environment.

An easy way to manually confirm if an ID is synced to an Azure environment is to simply type the full [***UPN***](https://social.technet.microsoft.com/wiki/contents/articles/52250.active-directory-user-principal-name.aspx) in the Azure portal, and see if it asks for a password. In the case below, we are prompted to enter a password. This is a good sign that we have an ID that can be used for initial reconnaissance.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-3.png)

Figure 3 - Manual User Enumeration

Going back to our foothold in the internal AD environment, usernames beginning with 'SVC' SIDs were exfiltrated using ***rpcclient***. Using ***rpcclient*** to query accounts directly from a DC does not produce any alerts from Defender for Identity.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-4.png)

Figure 4 - Account Enumeration With rpcclient

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Figure-5.png)
...