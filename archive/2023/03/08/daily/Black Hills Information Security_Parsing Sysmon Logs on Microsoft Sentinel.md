---
title: Parsing Sysmon Logs on Microsoft Sentinel
url: https://www.blackhillsinfosec.com/parsing-sysmon-logs-on-microsoft-sentinel/
source: Black Hills Information Security
date: 2023-03-08
fetch_date: 2025-10-04T08:55:07.332950
---

# Parsing Sysmon Logs on Microsoft Sentinel

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

7
Mar
2023

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Jordan Drysdale](https://www.blackhillsinfosec.com/category/author/jordan-drysdale/)

# [Parsing Sysmon Logs on Microsoft Sentinel](https://www.blackhillsinfosec.com/parsing-sysmon-logs-on-microsoft-sentinel/)

[Jordan Drysdale](https://www.linkedin.com/in/jordandrysdale/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/BLOG_chalkboard_00619-1024x576.png)

**Tl;dr:** Many parsers have been written and several are referenced here. This blog describes a simple parser for Sysmon logs through Event ID (EID) 28 for Microsoft Sentinel.

Let’s start with a description of the Sysmon schema version. As shown below, the latest schema version as of 23-DEC-22 was 4.83. This will need to be updated in your Sysmon config files if you wish to stay bleeding edge.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture21.jpg)

The following blocks include some additions to the version of Sysmon modular generating as of 23-DEC-22. Modular was referenced in a link above, the few lines below allow the writing of Sysmon EIDs 27 and 28 to the operational logs.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture22.jpg)

But wait… why am I talking about these things in the Sentinel Sysmon parser’s GitHub repo? Hang tight, trust the process, we will get through this.

As you can see, default download (c:\users\*\downloads) locations in userland get blocked with the Sysmon EID 27 configuration shown above. This configuration is insufficient for proper usage for modern protective considerations but demonstrates the possibilities.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture23.jpg)

This event then gets written to Windows logs. Assuming you are integrated with Microsoft Analytics or Log Analytics agents and are capturing Sysmon logs in your workspace, these logs will be queryable in just a few minutes.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture24.jpg)

We can now also restrict file shredding in locations we configure with the config file directives. Scroll back up and check out the <– EID 28 –> config block. All we restrict is c:\users\*\Downloads; obviously, this is insufficient.

Shown next is an attempt to SDelete (shred) the Firefox installer (pretend this is an adversary trying to cover their tracks). BLOCKED!!!!!!!

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture25.jpg)

This was also written to the event log.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture26.jpg)

Now for the actual goods — what we all came here for. If you want to make your Sysmon logs meaningful in most SIEMs, you need to parse them. There are a few parsers available, and some appear to be well-maintained. The link below was last updated on March 1, 2023, and appears to cover all versions of Sysmon.

[Microsoft Azure Parsers GitHub Repo](https://github.com/Azure/Azure-Sentinel/blob/master/Parsers/) — and has a Sysmon parser available.

Buttttttttt, [here’s another one](https://github.com/DefensiveOrigins/MSSentinelSysmonParser/blob/main/SysmonParser) we wrote for our APT class crafted from other bits and pieces available.

As shown, you want to copy the contents of the parser.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture27.jpg)

Paste the entire blob into a Sentinel > Logs query window and run it. The query may take a moment. Once complete, click to Save As > Function.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture28.jpg)

Name the function accordingly — it matters — because you will be using this to query Sysmon logs in all future queries. As shown, it was named SysmonParser.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture29.jpg)

Finally, run the function in a new query window by calling SysmonParser() and looking for those couple of event IDs – 27 and 28.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture30.jpg)

## Reference Materials:

[Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) – the best system monitor for Windows! Even better than Windows auditing!

[Olaf Hartong’s Sysmon Modular](https://github.com/olafhartong/sysmon-modular) – The best configuration generator for Sysmon ever shared with the world!

[Olaf Hartong’s recent article on Sysmon EID 27 – file block executables](https://medium.c...