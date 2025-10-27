---
title: Microsoft Store and WinGet: Security Risks for Corporate Environments
url: https://www.blackhillsinfosec.com/microsoft-store-and-winget-security-risks/
source: Black Hills Information Security, Inc.
date: 2025-09-11
fetch_date: 2025-10-02T19:58:23.371104
---

# Microsoft Store and WinGet: Security Risks for Corporate Environments

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

10
Sep
2025

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [David Fletcher](https://www.blackhillsinfosec.com/category/author/david-fletcher/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Microsoft store](https://www.blackhillsinfosec.com/tag/microsoft-store/), [winget](https://www.blackhillsinfosec.com/tag/winget/)

# [Microsoft Store and WinGet: Security Risks for Corporate Environments](https://www.blackhillsinfosec.com/microsoft-store-and-winget-security-risks/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/DFletcher-150x150.png)

| [David Fletcher](https://www.blackhillsinfosec.com/team/tim-fowler/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/09/msstore_header.png)

The Microsoft Store provides a convenient mechanism to install software without needing administrator permissions. The feature is convenient for non-corporate and home users but is unlikely to be acceptable in corporate environments. This is because attackers and malicious employees can use the Microsoft Store to install software that might violate organizational policy.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/msstore_01.png)

**Microsoft Store User Interface**

Furthermore, the Microsoft Store is likely to allow users to install dual use applications that can be used to bypass security controls or access sensitive information in the environment. Several applications that are commonly used to facilitate bypass or data access are described below. This is not an exhaustive list, as the resources published to the Microsoft Store are extensive.

In addition to the Microsoft Store user interface, the WinGet utility can also be used to search for and install software. Packages can be discovered using the WinGet search command. In the image below, the source of msstore identifies packages available from the Microsoft Store that can be installed without elevated privileges. Other sources may or may not require elevated privileges, depending on the package details.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/msstore_02.png)

**Microsoft Store Packages Exposed via WinGet**

Once the desired package is identified, it can be installed using either the name or ID in the search results with the `winget install` command. In the image below, the Microsoft Dev tunnels client is installed.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/msstore_03.png)

**WinGet Package Installation (Dev Tunnels)**

Hopefully, by now you realize that the Microsoft Store and WinGet can both be used to install potentially dangerous and unauthorized software.

## Microsoft Store and WinGet Abuse Examples

To drive the point home, the following sections illustrate some of the packages that are frequently abused using Microsoft Store access.

### **Microsoft Quick Assist**

The Quick Assist application is bundled with Microsoft Windows operating systems and is used to obtain remote support when troubleshooting. Attackers often use the application to execute social engineering campaigns against organizations. Even if you have taken the time to harden your Windows hosts and removed this tool, access to the Microsoft Store provides an opportunity for users to reinstall the utility.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/msstore_04.png)

**Quick Assist Microsoft Store Entry**

The attacker typically attempts to impersonate IT staff wanting to check on the configuration of a host or to install a utility. The attacker then prompts the user to launch Quick Assist and enter a code provided the malicious caller.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/msstore_05.png)

**Quick Assist Authorization Code Prompt**

When the code is entered, the attacker requests remote control of the computer to perform their malicious activities. With the right pretext, this ruse is often very effective.

### **DBeaver Community Edition (CE)**

Attackers and malicious users who have gained remote control of a system are likely to search for opportunities to move laterally or access sensitive information. The DBeaver application is a universal database tool that can be used to facilitate both activities.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/msstore_06.png)

**DBeaver Microsoft Store Entry**

This application provides an easy-to-use interface to connect to, query, and make changes to a wide array of database server platforms. Access is often facilitated through Active Directory analysis, discovery of configuration files, or prior knowledge of the environ...