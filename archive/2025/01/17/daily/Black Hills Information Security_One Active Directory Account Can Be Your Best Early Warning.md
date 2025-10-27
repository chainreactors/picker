---
title: One Active Directory Account Can Be Your Best Early Warning
url: https://www.blackhillsinfosec.com/one-active-directory-account-can-be-your-best-early-warning/
source: Black Hills Information Security
date: 2025-01-17
fetch_date: 2025-10-06T20:10:41.369221
---

# One Active Directory Account Can Be Your Best Early Warning

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

16
Jan
2025

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 201](https://www.blackhillsinfosec.com/category/infosec-201/), [Jordan Drysdale](https://www.blackhillsinfosec.com/category/author/jordan-drysdale/)

# [One Active Directory Account Can Be Your Best Early Warning](https://www.blackhillsinfosec.com/one-active-directory-account-can-be-your-best-early-warning/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/11/jordan-1024x1024-462x462-1-150x150.jpg)

| [Jordan Drysdale](https://www.blackhillsinfosec.com/team/jordan-drysdale/)

*Jordan has been hanging around the tech industry for 25 years now and was baited hook, line, and sinker by Napster. He’s been part of the Black Hills Information Security team for a decade in various capacities and has been a part of Antisyphon Training’s amazing growth trajectory as an instructor.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/AD_Warning_header.png)

Here we go again, discussing Active Directory, hacking, and detection engineering.

**tl;dr:** One AD account can provide you with three detections that if implemented properly will catch common adversarial activities early. Which detects?

* AD Enumeration via ADExplorer, BloodHound, and LDP.exe
* Kerberoasting and service principal attacks.
* Password sprays, credential stuffing, and brute-forcing.

You can follow along with this blog in an ephemeral lab on Microsoft Azure. Use an ARM template to build that AD lab: <https://www.doazlab.com.> The lab looks something like the screenshot below when your builder completes.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/001_labov-1024x578.jpg)

Lab Environment Overview

If you’ve never seen Azure, just search for your public IPs. Click on any of the objects to get an overview of the assigned IP and DNS record.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/002_public.jpg)

How To Find Your Public IP Resources

The IP and DNS details for the blog environment are shown below. Should you choose to deploy the lab environment, your IP address allocations will differ.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/003_ipdeets-1024x447.jpg)

Public IP Resource Details

The remainder of these configuration tasks were completed from the DC01 desktop, PowerShell, and command prompt.

```
<PowerShell command block>
whoami
hostname
setspn -T doazlab.com -Q */*
</PowerShell command block>
```

These commands tell us who we are, where we are, and all the discoverable service principal names (SPNs) on the domain.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/004_setspn.jpg)

SetSPN Command to List Service Principals

The next command creates an account in AD, Ricardo Beneficio, which will be useful for a few engineered detections later. Then, we gather our new object’s GUID, because we will need this value to engineer detections for LDAP enumeration.

```
<PowerShell command block>
# create honey account
New-ADUser -UserPrincipalName [email protected] -Path "OU=DomainUsers,dc=doazlab,DC=com" -GivenName "Ricardo" -Surname "Beneficio" -Enabled 1 -Name "Ricardo.Beneficio" -desc "Accounting Controller" -office "Accounting" -title "Controller" -company "DevLabs" -AccountPassword (ConvertTo-SecureString "Contrasena#2" -AsPlainText -Force)

# get honey user object GUID because not all event XML was created equal
Get-ADUser -Identity ricardo.beneficio -Properties "ObjectGuid"
</command block>
```

This should return a few details about the object, including the ObjectGUID, which can be useful for some detections.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/005_objectguid.jpg)

Ricardo’s ObjectGUID Retrieval with Get-ADUser

Let’s use event IDs (EIDs) 4624 and 4625 as our first example. After log shipping, these events provide us with a normalized representation of the AD object (username). So, as shown in the next screenshot, a valid login for our honey account contains the normalized account name, human readable, and easily searchable.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/006_ricardo_4624.jpg)

Normalized Object Name in Account Field (Valid Login)

With a bit more audit configuration, we can capture an additional event ID for comparison. The following PowerShell will grab a copy of Open Threat Research Forge’s (OTRF) Set-AuditRule.ps1 script. Using that tool, we will enable auditing on Ricardo’s UAC attribute, meanin...