---
title: Abusing Active Directory Certificate Services (Part 4)
url: https://www.blackhillsinfosec.com/abusing-active-directory-certificate-services-part-4/
source: Black Hills Information Security
date: 2024-05-31
fetch_date: 2025-10-06T16:51:08.107455
---

# Abusing Active Directory Certificate Services (Part 4)

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

30
May
2024

[Alyssa Snow](https://www.blackhillsinfosec.com/category/author/alyssa-snow/), [Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/)

# [Abusing Active Directory Certificate Services (Part 4)](https://www.blackhillsinfosec.com/abusing-active-directory-certificate-services-part-4/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/10/Alyssa-943x1024-462x462-1-150x150.jpeg)

| [Alyssa Snow](https://www.linkedin.com/in/alyssa-snow-2b8437169)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/AD_pt4header-1024x576.png)

*Start this blog series from the beginning here:* [PART 1](https://www.blackhillsinfosec.com/abusing-active-directory-certificate-services-part-one/)

Misconfigurations in Active Directory Certificate Services (ADCS) can introduce critical vulnerabilities into an Enterprise environment. In this article, we will cover the basics of exploiting escalation techniques ESC2 and ESC3 using [Certipy](https://github.com/ly4k/Certipy). These escalation techniques abuse overly permissive enrollment rights and Extended Key Usage configurations. The Extended Key Usage (EKU) policies define how a certificate can be used. Some examples of the available descriptors for the EKU policy are shown in the following screenshot.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/ADpt4_01.jpg)

**EKU Descriptor Examples**

Users authorized to request a certificate can be defined on the Certificate Authority itself and in the certificate template object. The CA properties can be viewed via the `certsrv` utility, **Right Click CA > Properties > Security**.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture2-1-500x461.png)

**CA CSR Descriptor**

The template permissions for the “User” template are displayed in the Certificate Template Console, as shown below.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture3-2-500x313.png)

**Template Security Permissions**

### ****ESC2****

A certificate template vulnerable to ESC2 is configured with the **Any Purpose** EKU or without an EKU configuration.

A template that specifies the **Any Purpose** EKU can allow an attacker to create a certificate with any purpose such as Code Signing, Client authentication, etc. Such a certificate can be used to authenticate to Active Directory as the user who originally requested the certificate and can be used to sign other certificates.

Templates vulnerable to ESC2 have the following conditions:

* Low Privilege Users Granted Enrollment Rights
* Signatures Required: 0
* Enabled: True
* Requires Management Approval: False
* Any Purpose: True **OR** Extended Key Usage: False

**Example:**

In the following example, let’s imagine that we have gained a foothold in our target company, FOOBAR’s, internal network, and we’ve compromised the account of a user with the name *bspears*.

First, let’s try to request a certificate on behalf of the domain admin using an existing template. Using the Certipy command below, we will request a certificate using the default “User” template on behalf of the domain admin with the username *administrator*.

The Certipy arguments required to request the certificate are as follows:

* `u` – username
* `p` – user’s password
* `dc-ip` – domain controller IP address
* `target` – target CA (Certificate Authority) DNS (Domain Name System) Name
* `ca` – short CA Name
* `template` – template name
* `on-behalf-of` – specifies another entity to request a certificate for

```
certipy-ad req -u 'bspears' -p 'REDACTED' -dc-ip '10.10.0.10' \
-target 'dc01.foobar.com'
-ca 'foobar-CA' \
-template 'User' \
-on-behalf-of 'example\administrator'
```

As shown in the figure below, this request resulted in an error and indicated that a PFX is required. Currently, we do not have a PFX that can be used to request a certificate on behalf of another user.

However, if *bspears* can request a certificate using a template configured with an EKU of **Any Purpose**, we can use the resulting PFX to request another certificate on behalf of another domain account.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture4-2.png)

**Failed to Obtain New Certificate for Administrator**

To find a certificate vulnerable to ESC2, we can enumerate ADCS configurations...