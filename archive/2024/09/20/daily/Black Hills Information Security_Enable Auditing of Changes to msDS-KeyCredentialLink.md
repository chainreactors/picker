---
title: Enable Auditing of Changes to msDS-KeyCredentialLink
url: https://www.blackhillsinfosec.com/enable-auditing-of-changes-to-msds-keycredentiallink/
source: Black Hills Information Security
date: 2024-09-20
fetch_date: 2025-10-06T18:27:45.097770
---

# Enable Auditing of Changes to msDS-KeyCredentialLink

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

19
Sep
2024

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Incident Response](https://www.blackhillsinfosec.com/category/blue-team/incident-response/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Jordan Drysdale](https://www.blackhillsinfosec.com/category/author/jordan-drysdale/)
[Blue Team Detections](https://www.blackhillsinfosec.com/tag/blue-team-detections/), [detection engineering](https://www.blackhillsinfosec.com/tag/detection-engineering/), [event auditing](https://www.blackhillsinfosec.com/tag/event-auditing/), [msDS-KeyCredentialLink](https://www.blackhillsinfosec.com/tag/msds-keycredentiallink/), [Shadow creds](https://www.blackhillsinfosec.com/tag/shadow-creds/)

# [Enable Auditing of Changes to msDS-KeyCredentialLink](https://www.blackhillsinfosec.com/enable-auditing-of-changes-to-msds-keycredentiallink/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/11/jordan-1024x1024-462x462-1-150x150.jpg)

| [Jordan Drysdale](https://www.blackhillsinfosec.com/team/jordan-drysdale/)

*Jordan has been hanging around the tech industry for 25 years now and was baited hook, line, and sinker by Napster. He’s been part of the Black Hills Information Security team for a decade in various capacities and has been a part of Antisyphon Training’s amazing growth trajectory as an instructor.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/09/msDS-KeyCredentialLink_header.png)

Changes to the msds-KeyCredentialLink attribute are not audited/logged with standard audit configurations. This required serious investigations and a partner firm in infosec provided us the answer: TrustedSec.

So, credit where it is due – this was amazing research: <https://trustedsec.com/blog/a-hitch-hackers-guide-to-dacl-based-detections-part-1b>. And this should resolve the lack of auditing on the attribute used so commonly of late to escalate privileges.

Another shout out is due here to the Open Threat Research Forge, Roberto Rodriguez and Jose Luis Rodriguez. Their efforts for open source are significant and they wrote the Set-AuditRule.ps1 tool used in the next commands. <https://github.com/OTRF/Set-AuditRule>

To configure Directory Service auditing of the msDS-CredentialLink attribute on all target objects in the domain, we must create a new AuditRule and specify the GUID of the attribute. The msDS-CredentialLink Schema GUID that will be added to the Audit Rule can be found here: <https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ada2/45916e5b-d66f-444e-b1e5-5b0666ed4d66>.

```
cn: ms-DS-Key-Credential-Link
ldapDisplayName: msDS-KeyCredentialLink
attributeID: 1.2.840.113556.1.4.2328
attributeSyntax: 2.5.5.7
omObjectClass: 1.2.840.113556.1.1.1.11
oMSyntax: 127
isSingleValued: FALSE
schemaIdGuid: 5b47d60f-6090-40b2-9f37-2a4de88f3063
systemOnly: FALSE
searchFlags: 0
linkId: 2220
systemFlags: FLAG_SCHEMA_BASE_OBJECT
attributeSecurityGUID: 9b026da6-0d3c-465c-8bee-5199d7165cba
showInAdvancedViewOnly: TRUE
```

Now that we have the Schema GUID of the attribute, 5b47d60f-6090-40b2-9f37-2a4de88f3063 we can use Set-AuditRule.ps1 to add an Audit Rule at the top of our domain to all descendant objects in the domain.

```
Import-Module ActiveDirectory
iwr -Uri https://raw.githubusercontent.com/OTRF/Set-AuditRule/master/Set-AuditRule.ps1 -OutFile Set-AuditRule.ps1
Import-Module .\Set-AuditRule.ps1
Set-AuditRule -AdObjectPath 'AD:\DC=doazlab,DC=com' -WellKnownSidType WorldSid -Rights WriteProperty,GenericWrite -InheritanceFlags All -AttributeGUID 5b47d60f-6090-40b2-9f37-2a4de88f3063 -AuditFlags Success
```

After configuring the Audit rule, future changes to objects’ msDS-KeyCredentialLink will create audit event logs if Directory Service auditing is enabled on the Domain Controllers.

#### **Detection Logic for Microsoft Sentinel**

Importing our logs into Sentinel, we can hunt for changes to msDS-KeyCredentialLink attributes using KQL.

```
union Event, SecurityEvent
| where EventID == 5136
| parse EventData with * 'ObjectDN">' ObjectDN "<" *
| parse EventData with * 'AttributeLDAPDisplayName">' ModifiedAttribute "<" *
| where ModifiedAttribute == "msDS-KeyCredentialLink"
| project Computer , TimeGenerated , Activity, ObjectDN, ModifiedAttribute
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/09/msDS-KeyCredentialLink_01.png)

This content is also available on GitHub at <https://github.com/DefensiveOrigins/Detect-msDS-KeyCredentialLink>

---

---

Want to learn more mad skills from the person who wrote this blog?

Check out these classes from Jordan and Kent:

**[Defending the Enterprise](https://www.antisyphontraining.com/on-demand-courses/defending-the-enterprise-w-kent...