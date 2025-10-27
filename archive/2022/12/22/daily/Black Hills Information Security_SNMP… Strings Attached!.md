---
title: SNMP… Strings Attached!
url: https://www.blackhillsinfosec.com/snmp-strings-attached/
source: Black Hills Information Security
date: 2022-12-22
fetch_date: 2025-10-04T02:13:47.848325
---

# SNMP… Strings Attached!

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

21
Dec
2022

[Author](https://www.blackhillsinfosec.com/category/author/), [Dale Hobbs](https://www.blackhillsinfosec.com/category/author/dale-hobbs/), [External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 201](https://www.blackhillsinfosec.com/category/infosec-201/), [Recon](https://www.blackhillsinfosec.com/category/red-team/recon/)
[Community Strings](https://www.blackhillsinfosec.com/tag/community-strings/), [Default](https://www.blackhillsinfosec.com/tag/default/), [SNMP](https://www.blackhillsinfosec.com/tag/snmp/)

# [SNMP… Strings Attached!](https://www.blackhillsinfosec.com/snmp-strings-attached/)

[Dale Hobbs](https://www.blackhillsinfosec.com/team/dale-hobbs/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2022/12/BLOG_chalkboard_00607-1024x576.png)

One thing that I almost always find when performing an internal network penetration test is Simple Network Management Protocol (SNMP) configured with default community strings.

Simple Network Management Protocol (SNMP) is a widely-used protocol for managing and monitoring network devices such as routers, switches, and servers. It allows network administrators to manage and monitor the performance of network devices and to troubleshoot issues when they arise.

SNMP is based on a “manager-agent” model, where a central network management system (NMS) acts as the manager and communicates with SNMP agents on each network device. The NMS sends requests to the agents for information about the device, and the agents respond with the requested data. This allows the NMS to collect and analyze data from all the devices on the network.

SNMP depends on secure strings (or “community strings”) that grant access to portions of a device’s management planes. There are two common community strings that we often see — ‘public’ which mainly provides read-only access and ‘private’ which generally provides read-write access.

A device that uses default SNMP community strings can have its entire configuration read using SNMP queries. In addition, when a device is configured with SNMP write access using a default string such as ‘public’, it is trivial for an attacker to modify the device’s configuration.

There are 3 versions of SNMP:

SNMPv1: This is the oldest version whereby the authentication is based on a community string that is transmitted without the benefit of encryption and as such, all the information is transmitted in plain text as well. It’s easy to set up but is only protected by the plain text community string.

SNMPv2c: Version 2c is nearly identical to Version 1 except it adds support for 64-bit counters. This is by far the most frequently used version today but like Version 1, also sends the traffic in plain text as well uses a plain text community string as authentication. Even if you have a non-default community string, gaining a Machine in the Middle position will result in disclosure of the community string through simple packet analysis.

SNMPv3: Version 3 is the latest version of SNMP and adds both encryption and authentication which can either be used together or separately. It’s more complex to set up than Version 1 or Version 2c but is a much more secure choice.

Let’s look at what types of information we can gather from a device. Nmap has a handful of useful NSE scripts specifically for SNMP. For example, using the ‘snmp-sysdescr’ NSE script, we can retrieve the server type and operating system.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2022/12/Picture3-1.png)

Using the ‘snmp-interfaces’ NSE script, we can gather some network information about the device, such as IP addresses, any additional network interfaces, and even traffic statistics.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2022/12/Picture4-1.png)

While these are all useful for a network administrator, they’re also useful for an attacker, as they can start to build a profile about the system and attempt to formulate an attack.

While this is by no means an exhaustive list of what you can do with SNMP, it should at least give you an idea of what we can gather using SNMP. If you’d like to see more SNMP scripts, you can consult <https://nmap.org>.

So now that we’ve seen a couple things you can do with SNMP from a blue team perspective, let’s see what we can do as an attacker using SNMP when configured with default community strings. For the purposes of this article, we’re going to be attacking a Linux-based system configured with SNMP in hopes of gaining a remote shell.

First off, by doing a simple Nmap UDP sc...