---
title: Detecting ADCS Privilege Escalation
url: https://www.blackhillsinfosec.com/detecting-adcs-privilege-escalation/
source: Black Hills Information Security, Inc.
date: 2025-07-24
fetch_date: 2025-10-06T23:49:50.374126
---

# Detecting ADCS Privilege Escalation

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

23
Jul
2025

[Alyssa Snow](https://www.blackhillsinfosec.com/category/author/alyssa-snow/), [Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Active Directory](https://www.blackhillsinfosec.com/tag/active-directory/), [ADCS](https://www.blackhillsinfosec.com/tag/adcs/)

# [Detecting ADCS Privilege Escalation](https://www.blackhillsinfosec.com/detecting-adcs-privilege-escalation/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/10/Alyssa-943x1024-462x462-1-150x150.jpeg)

| [Alyssa Snow](https://www.linkedin.com/in/alyssa-snow-2b8437169)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/ADCS_header.png)

Active Directory Certificate Services (ADCS) is used to manage certificates for systems, users, applications, and more in an enterprise environment. Misconfigurations in ADCS can introduce critical vulnerabilities into an enterprise Active Directory environment. A few escalation techniques are covered in [ESC1](https://www.blackhillsinfosec.com/abusing-active-directory-certificate-services-part-4/), [ESC2&3](https://www.blackhillsinfosec.com/abusing-active-directory-certificate-services-part-4/), [ESC4](https://www.blackhillsinfosec.com/abusing-active-directory-certificate-services-part-2/), [ESC8](https://www.blackhillsinfosec.com/abusing-active-directory-certificate-services-part-3/). Each of those blogs include some of the security event IDs that could be used to detect these attacks. In this blog post, we are going to walk through how to detect some of these attacks in detail.

## Let’s Check the Logs …Wait

Well, first things first, to create an alert for malicious activity, we need to ensure that we are logging ADCS events. By default, ADCS auditing is not enabled. The CA’s auditing properties can be viewed via the `certsrv` utility, **Right Click CA > Properties > Auditing**. As shown in the screenshot below, the default settings are set to not log any events.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/AuditingADCS_01.png)

**Default CA Auditing Settings**

Let’s fix that. We can enable auditing by selecting each event as shown in the figure below.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/AuditingADCS_02.png)

**Enabled Auditing for ADCS**

## Detections

In [this blog](http://•%09https:/www.blackhillsinfosec.com/abusing-active-directory-certificate-services-part-one/), I demonstrated a privilege escalation technique known as ESC1 that allows a low privileged account to escalate to a privileged account (domain admin). I also mentioned the following security event IDs.

* 4886 – Request for certificate
* 4887 – Certificate Issued

In the previous section, we enabled auditing for the ADCS service, and now we will see what this looks like in [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/overview?tabs=azure-portal). Sentinel uses the Kusto Query Language ([KQL](https://learn.microsoft.com/en-us/kusto/query/?view=azure-data-explorer&preserve-view=true)). We are going to run the following basic query to identify the privilege escalation activity.

```
SecurityEvent
| where EventID == 4886 or EventID == 4887
```

Upon further investigation of the results, we can see that the “Requester” and the “UPN” (subject of the certificate) do not match.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/AuditingADCS_03.png)

**Sentinel Detection**

## Alerts

Now that we’ve confirmed that we have appropriate logging in place and we defined a query to identify this attack, let’s save this query to Sentinel.

1. Select Save > Save as query
2. Name the query
3. Add a description
4. Select Save

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/AuditingADCS_05.png)

**Save Query**

Next, let’s create an alert based on the query we defined. Click “New Alert Rule” then “Create Microsoft Sentinel Alert” to create a new rule based on this query.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/AuditingADCS_06.png)

Create New Alert Rule

Define the name, description, and severity. You can also set the MITRE technique. For this example, I am just modifying the name and description. I left the other values set to their defaults.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/AuditingADCS_07.png)

Create Alert

Configure the rule logic, such as how often the rule will be executed and...