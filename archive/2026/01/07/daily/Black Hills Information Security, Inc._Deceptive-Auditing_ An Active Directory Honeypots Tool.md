---
title: Deceptive-Auditing: An Active Directory Honeypots Tool
url: https://www.blackhillsinfosec.com/deceptive-auditing/
source: Black Hills Information Security, Inc.
date: 2026-01-07
fetch_date: 2026-01-08T03:29:42.427154
---

# Deceptive-Auditing: An Active Directory Honeypots Tool

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
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
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

7
Jan
2026

[Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Intern](https://www.blackhillsinfosec.com/category/author/intern/)
[Active Directory](https://www.blackhillsinfosec.com/tag/active-directory/), [automation](https://www.blackhillsinfosec.com/tag/automation/), [Honey Pots](https://www.blackhillsinfosec.com/tag/honey-pots/)

# [Deceptive-Auditing: An Active Directory Honeypots Tool](https://www.blackhillsinfosec.com/deceptive-auditing/)

by [Sean Minnick](https://www.blackhillsinfosec.com/team/sean-minnick/) || QC Automation Support Intern

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/deceptiveaud_header-2.png)

**Tool GitHub:** <https://github.com/SeanMinnick/Deceptive-Auditing>

Deceptive-Auditing is a tool that deploys Active Directory honeypots and automatically enables auditing for those honeypots. This complete tool is based on two previous projects, Set-AuditRule and Deploy-Deception, created by Roberto “Cyb3rWard0g” Rodriguez, and Nikhil “SamratAshok” Mittal. Nikhil Mittal has his own personal blog where he writes about the original tool (<https://www.labofapenetrationtester.com/2018/10/deploy-deception.html>). I merged these tools into one complete function set and added some more functionality.

In this blog, I’ll go over how to use this tool to set up a deceptive Active Directory environment.

Each object in Active Directory has a SACL (System Access Control List) and DACL (Discretionary Access Control List). Both ACLs hold ACEs (Access Control Entry) which determine permissions for object and auditing for the object. The DACL will determine who can access the object: User1 can read the object, User2 can modify the object, etc. The SACL controls auditing, alerts if anyone reads the object, alerts if anyone modifies the object, etc. Adding ACEs to the SACL can be done manually; this tool allows you to automate that process and create PowerShell scripts that automatically create or remove ACEs from an objects SACL.

The tool itself is a set of PowerShell cmdlets that can be imported into your PowerShell session. The backbone of the function set is Set-AuditRule. This is a merged function that allows you to audit AD objects, registry keys, or any type of file. This is used internally by all deployment functions to set up auditing. It’s also pretty simple to use on its own. Below, I have an example of using it on a text file to set up auditing.

```
Set-AuditRule -FilePath "C:\Windows\depdec\Test.txt" -WellKnownSidType WorldSid -Rights Read -InheritanceFlags None -PropagationFlags None -AuditFlags Success
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/Decept-Aud_01-1024x42.png)

* When setting an audit rule for files, it’s important that the first parameter used is –FilePath; this sets up the dynamic parameters for files specifically.
* -WellKnownSidType specifies who the audit rule applies to. SIDs (Security Identifiers) in Active Directory are standardized identifiers used by the Windows operating system to represent specific users, groups, and service accounts. These SIDs are consistent across all installations of Windows. In this example, WorldSid applies this audit rule to everyone—nobody is exempt from auditing—however, any well-known SID can be used in place.
* The -Rights parameter specifies which action to audit. In this example, it’s auditing when anyone (WorldSid) reads the file.
* The -InheritancFlags parameter specifies whether the audit rule should be inherited by the object’s children. Although this doesn’t apply to this file, it’s important for other filesystem auditing. More specifics on how to use this parameter can be found in the README.
* -PropogationFlags specifies how the audit rule is inherited only if -InheritanceFlags is used.
* Finally, AuditFlags is set to success, meaning the audit rule will trigger when someone successfully reads the file.

The code for these file system events is 4663. After using Get-Content to “read” the contents of the file you can see the event in event viewer.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/Decept-Aud_02.png)

This same principle works for registry keys.

```
Set-AuditRule -RegistryPath "HKLM:\SOFTWARE\TestAuditKey" -WellKnownSidType WorldSid -Rights ReadKey -InheritanceFlags None -PropagationFlags None -AuditFlags Success
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/Decept-Aud_03.png)![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/Decept-Aud_04.png)

For each of...