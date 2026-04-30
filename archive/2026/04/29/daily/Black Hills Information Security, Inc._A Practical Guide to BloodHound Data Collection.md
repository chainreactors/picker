---
title: A Practical Guide to BloodHound Data Collection
url: https://www.blackhillsinfosec.com/bloodhound-data-collection/
source: Black Hills Information Security, Inc.
date: 2026-04-29
fetch_date: 2026-04-30T05:29:38.272755
---

# A Practical Guide to BloodHound Data Collection

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
  + [Admin Team](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [Active SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
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

29
Apr
2026

[Alyssa Snow](https://www.blackhillsinfosec.com/category/author/alyssa-snow/), [Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Active Directory](https://www.blackhillsinfosec.com/tag/active-directory/), [bloodhound](https://www.blackhillsinfosec.com/tag/bloodhound/)

# [A Practical Guide to BloodHound Data Collection](https://www.blackhillsinfosec.com/bloodhound-data-collection/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/10/Alyssa-943x1024-462x462-1-150x150.jpeg)

| [Alyssa Snow](https://www.linkedin.com/in/alyssa-snow-2b8437169)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/bloodhound_header.png)

BloodHound is a tool used to enumerate Active Directory (AD) information. It is commonly employed to identify vulnerable configurations and attack paths in Active Directory. BloodHound provides a visual view of relationships between AD objects, which can be used to identify paths of domain privilege escalation.

This blog will not dive too deeply into BloodHound itself; instead, we will focus on various methods to collect AD data to provide BloodHound as input.

## Data Structure

BloodHound is a graphical database that ingests data in the form of JSON blobs. Once the JSON data has been uploaded to the BloodHound database, the web interface can be used to query the database via cypher queries and map attack paths.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/BloodHound_AD_01.png)

There are several built-in cypher queries that can be used by going to Saved Queries under the CYPHER tab. Simply click the built-in query to execute it. The cypher syntax for each built-in query will display when it runs. For example, you can list all domain admins.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/BloodHound_AD_02-1024x655.png)

There are also built-in escalation path queries, such as built-in queries for Active Directory Certificate Services (ADCS) privilege escalation techniques. The screenshot below shows a [privilege escalation path using ESC1](https://www.blackhillsinfosec.com/abusing-active-directory-certificate-services-part-one/) for the domain users and domain computers groups.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/BH_AD_03-1024x326.png)

### BloodHound.py

BloodHound.py is a python data collector used to enumerate Active Directory information and store the data in JSON files that can be ingested by the BloodHound UI. There are several data collection methods. In this example, we are specifying all collection methods. BloodHound.py requires valid domain credentials to execute.

```
python3 bloodhound.py -u USER -p 'PASSWORD' -d DOMAIN -c all
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/BH_AD_04-1024x424.png)

This method of collecting data is not particularly stealthy; however, it is thorough and effective. Especially when executing from a system that is running Linux and/or not domain joined.

### SharpHound

SharpHound is a C# data collector written by the maintainers of BloodHound. SharpHound is intended to be executed on a domain-joined Windows system and executes in the context of the user that executes the program. No credentials have to be provided to execute the tool.

```
./SharpHound.exe -c All
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/BH_AD_05-1024x411.png)

This method of collecting data is also not particularly stealthy. However, it is a useful method when you have access to a domain-joined Windows system, especially if you do not have plaintext credentials.

### ADExplorer

ADExplorer is a tool used by admins to view and modify Active Directory objects. Any user with valid domain credentials can use this tool to connect to the AD database. ADExplorer is a Sysinternals tool, so it’s trusted by Microsoft, and unlike the first two methods of data collection, it would not be flagged as malicious.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/BH_AD_06-1024x861.png)

ADExplorer can accept credentials and a specific domain/domain controller, or you can simply select “OK” and ADExplorer will execute in the conte...