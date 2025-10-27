---
title: Misconfiguration Manager: Detection Updates
url: https://posts.specterops.io/misconfiguration-manager-detection-updates-8a9828b72dbf?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-12-17
fetch_date: 2025-10-06T19:59:43.006557
---

# Misconfiguration Manager: Detection Updates

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8a9828b72dbf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmisconfiguration-manager-detection-updates-8a9828b72dbf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmisconfiguration-manager-detection-updates-8a9828b72dbf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-8a9828b72dbf---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-8a9828b72dbf---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Misconfiguration Manager: Detection Updates

[![Joshua Prager](https://miro.medium.com/v2/resize:fill:64:64/2*fGwz9f3HjOXo_FknMmAyZg.png)](https://medium.com/%40bouj33boy?source=post_page---byline--8a9828b72dbf---------------------------------------)

[Joshua Prager](https://medium.com/%40bouj33boy?source=post_page---byline--8a9828b72dbf---------------------------------------)

6 min read

·

Dec 16, 2024

--

Listen

Share

**TL;DR:** *The* [*Misconfiguration Manager DETECT*](https://github.com/subat0mik/Misconfiguration-Manager/tree/main/defense-techniques/DETECT) *section has been updated with relevant guidance to help defensive operators identify the most prolific attack techniques from the Misconfiguration Manager project.*

## Background

If you have been following SpecterOps’s offensive security research over the last few years, you may have noticed our interest in targeting attack paths leveraging Microsoft’s Configuration Manager (CM), formerly known as System Center Configuration Manager or SCCM.

At SO-CON 2024, [Duane Michael](https://subat0mik.medium.com/), [Chris Thompson](https://medium.com/%40Mayyhem), and [Garrett Foster](https://medium.com/%40garrfoster) released the [Misconfiguration Manager](https://github.com/subat0mik/Misconfiguration-Manager/tree/main) project, which represented a knowledge base of offensive techniques. Additionally, the project contained a large list of [preventive controls](https://github.com/subat0mik/Misconfiguration-Manager/tree/main/defense-techniques/PREVENT) complemented by a small list of [detective controls](https://github.com/subat0mik/Misconfiguration-Manager/tree/main/defense-techniques/DETECT) that I had put together for the launch of the project. You can read more about the original attack and defensive techniques from the project launch on Duane’s blog, [Misconfiguration Manager: Overlooked and Overprivileged](/misconfiguration-manager-overlooked-and-overprivileged-70983b8f350d).

This project grabbed my attention before launch due to its relatability to my network operations background. As many security researchers began this career path, I started my career in customer support and eventually found myself in system administration. Many years ago, I can remember learning how to deploy security patches, software, and operating systems via SCCM. One lesson that stood out to me was this understanding that access to SCCM was to be guarded due to the power this management tool had within the entire Active Directory domain. Once implemented, SCCM managed the whole domain with high levels of privilege and the SCCM console acted as a central point of administration.

Fast-forward many years, I was happy to help document detections for this project and give defenders a chance to detect the prolific attack techniques targeting Microsoft’s Configuration Manager. My goal was to give the current industry the tools that I needed when I was responsible for guarding the use of SCCM.

## DETECT-4

[DETECT-4: Monitor App Deployments via Status Message Queue](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/defense-techniques/DETECT/DETECT-4/detect-4_description.md)

Configuration Manager can deploy applications to domain-joined and non-domain-joined clients within the scoped environment. These application deployments need only to reference a UNC path, which opens quite a wide gate to *where* the application can be sourced. Applications can be locally hosted on the targeted client machine, stored within a remote hosted share, or uploaded and hosted within Configuration Manager, itself. Luckily, Configuration Manager maintains the [Status Message Queue](https://learn.microsoft.com/en-us/mem/configmgr/develop/core/servers/manage/about-configuration-manager-status-messages) log that queries the backend Configuration Manager MSSQL database and returns the plain text verbiage of each application deployment. Defenders can ingest these status messages into a centralized logging solution (Elastic, Splunk, etc). The logs without the corresponding MSSQL database returns are located on the Site Server’s `smsprov.log` file. There are several open-source [projects](https://github.com/slaven-s/splunk-sccm) that aid in collecting the status messages and most of them will require configuring DB Connect at some point to match the collected SMSProv log to the MSSQL returns to get the full event ingested.

Once ingested, defenders can use this data source to build a composite event identifying the collection creation (Message: 30015) or the modification of a collection (Message: 30016), the creation of a deployment (Message: 30226), and the initiation of the deployment (Message: 40800).

Press enter or click to view image in full size

![]()

Composite Event For Application Deployment

## DETECT-5 and DETECT-6

[DETECT-5: Monitor Group Membership Changes to SMS Admins Group](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/defense-techniques/DETECT/DETECT-5/detect-5_description.md)

[DETECT-6: Monitor Group Membership Changes for RBAC\_Admins Table](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/defense-techniques/DETECT/DETECT-6/detect-6_description.md)

The `[SMS Admins](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/plan-for-the-sms-provider)` [security group](https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/hierarchy/plan-for-the-sms-provider) and the `RBAC_Admins` table represent the local security group with access to the SMS Provider, a WMI provider with write access to Configuration Manager (CM) databases. When a Full Administrator is added via the console or directly through modifications to the `RBAC_Admins` and `RBAC_ExtendedPermissions` tables in the site database, the account gets added to the local SMS Admins group on computers hosting the SMS Provider role. Defenders can leverage object access auditing to identify modifications to the local security group `SMS Admins`indicating a new member has been maliciously added/removed ([Event ID: 4732](https://learn.microsoft.com/en-us/previous-versions/windows/it-...