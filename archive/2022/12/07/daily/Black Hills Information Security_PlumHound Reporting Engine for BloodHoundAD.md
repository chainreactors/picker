---
title: PlumHound Reporting Engine for BloodHoundAD
url: https://www.blackhillsinfosec.com/plumhound-reporting-engine-for-bloodhoundad/
source: Black Hills Information Security
date: 2022-12-07
fetch_date: 2025-10-04T00:41:14.005686
---

# PlumHound Reporting Engine for BloodHoundAD

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

6
Dec
2022

[Author](https://www.blackhillsinfosec.com/category/author/), [Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Kent Ickler](https://www.blackhillsinfosec.com/category/author/kent-ickler/)
[Active Directory](https://www.blackhillsinfosec.com/tag/active-directory/), [bloodhound](https://www.blackhillsinfosec.com/tag/bloodhound/), [BloodHoundAD](https://www.blackhillsinfosec.com/tag/bloodhoundad/), [Control Paths](https://www.blackhillsinfosec.com/tag/control-paths/), [Domains](https://www.blackhillsinfosec.com/tag/domains/), [PlumHound](https://www.blackhillsinfosec.com/tag/plumhound/), [Purple Team](https://www.blackhillsinfosec.com/tag/purple-team/), [reports](https://www.blackhillsinfosec.com/tag/reports/), [System Administration](https://www.blackhillsinfosec.com/tag/system-administration/)

# [PlumHound Reporting Engine for BloodHoundAD](https://www.blackhillsinfosec.com/plumhound-reporting-engine-for-bloodhoundad/)

[Kent Ickler](https://twitter.com/KRelkci) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2022/12/BLOG_chalkboard_00606-1024x576.jpg)

It’s been over two years since Jordan and I talked about a Blue Team’s perspective on Red Team tools.

[A Blue Team’s Perspective on Red Team Hack Tools – YouTube](https://www.youtube.com/watch?v=0mIN2OU5hQE)

The webcast itself had interesting topics; at the end of the discussion, we talked about a tool we wrote. PlumHound is a report engine for BloodHoundAD to make actionable reports for Blue Teams, Systems Administrators, and Analysts. We figured it’s about time we got around to writing this blog.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2022/12/Picture3.png)

The framework for PlumHound is relatively simple: utilize the control path-finding capabilities of BloodHoundAD in Neo4j to build actionable intelligence for blue teams to identify Active Directory problems.

A while into development, we ran into Mathieu Saulnier ([Scoubi](https://github.com/Scoubi)) who had a similar project. Finding similar objectives, we merged our efforts. Mathieu brought in additional modules that would identify the weakest link (AnalyzePath) to a control path vulnerability and the most important paths to remediate first (BusiestPath) to be most effective— both modules of his BlueHound project.

On pentests where we found interesting control path vulnerabilities, we took a few moments to analyze the condition and, if it was something new, write a new PlumHound report using Neo4j cyphers. Meanwhile, other information security teams began to use the report engine to build their own reports as well.

Today, we have 69 PlumHound reports in the packaged “Default” reports, plus the Busiest Path and Analyze Path functions of Mathieu Saulnier’s BlueHound.

### ****So, how does it all work?****

First off, we have to acknowledge that we stand on the shoulders of the giants that built Neo4j, BloodHoundAD, and its data collectors. With that said, PlumHound uses Python to connect to the Neo4j database after BloodHoundAD has ingested and parsed data. PlumHound then uses Neo4j’s cypher language to query its database for information and output that information into CSV or HTML reports (or, alternatively, to standard output). That is, the BloodHoundAD analysis can be normalized into a reporting format that can be consumed for data-driven decision making about correcting common Active Directory control path vulnerabilities.

#### Running PlumHound Report Engine

Running PlumHound is easy: specify the Neo4j database connection and specify the “task-list” you want to do. Task-lists are sets of cypher queries and metadata that tell PlumHound what query to run and how to generate a report from the output. The “Default” task-list included with PlumHound includes 69 reports plus an index.

To shorthand things even further, if your Neo4j server is on localhost, you won’t need to specify a Neo4j connection.

For versions of Neo4j that still use “default” credentials, you must first update the default credentials to use the service. If you’re like me, you source-filter the Neo4j service and update credentials to be something… easy… lazy… terrible?  Anyway, I change the password from “neo4j” to “neo4jj” because source-filter the service. Remember, if you source-filtered the service, you will need to run PlumHound from that trusted source.

 If your username is “neo4j” and your updated password is “neo4jj”, you won’t need to specify your username and password to connect to the Neo4j database, because the default is “neo4jj”.

#### It’s as simple as:

That will execute the default included task-list.

`PlumHound...