---
title: Default Web Content
url: https://www.blackhillsinfosec.com/default-web-content/
source: Black Hills Information Security, Inc.
date: 2025-09-04
fetch_date: 2025-10-02T19:37:19.339637
---

# Default Web Content

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

3
Sep
2025

[Chris Sullo'](https://www.blackhillsinfosec.com/category/author/chris-sullo/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)

# [Default Web Content](https://www.blackhillsinfosec.com/default-web-content/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/Sullo-150x150.png)

| [Sullo](https://www.blackhillsinfosec.com/team/chris-sullo/)

*Chris has been working in security for 30 years, mainly doing penetration testing in both consulting and corporate environments. Chris is the author of the Nikto web scanner, founder of the RVAsec conference, and has been involved in many OSS projects and community efforts.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/default_web_header.png)

Whether it’s forgotten temporary files, installation artifacts, READMEs, or even simple image files—default content on web servers can turn into a boon for attackers. In the most innocent of cases, these types of content can let attackers know more about the tech stack of the environment, and in the worst case scenario can lead to exploitation.

## Technical Details

When developers build sites they are focused on functionality and meeting requirements. Cleaning up after themselves—or the application environment—often takes a backseat to fixing bugs and adding features. And if it’s the web server itself (and not the application), is that the responsibility of the developer or the system administrator?

Most COTS (commercial off-the-shelf software) products litter the filesystem with debris—installation scripts and programs, README files, examples, and more. Just because these are not critical for app operations doesn’t mean they shouldn’t be taken seriously and removed or restricted.

### **Example Programs**

Example or sample programs can sometimes be a source of compromise. These applications are designed to show off technology, not to be secure. A quick search shows nearly a dozen CVEs related to Apache Tomcat’s default examples.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/default_web_01.png)

**Tomcat Admin Interface** ([CC Image](https://commons.wikimedia.org/w/index.php?curid=2386939) Credit)

Even in this example, the administrator interface itself is “default content” (more on this below). Production web servers do not need these admin interfaces, let alone the example programs, accessible to anyone but administrators.

### **README/CHANGELOG**

We all need a little help sometimes—especially when installing complex pieces of software in a tech stack. But once it’s working, those helpful files can lead to information disclosure scenarios that leak details of the installed software and/or versions.

**Question:** What’s the difference between Apache 2.4.59 and Apache 2.4.60?

**Answer:** CVE-2024-36387

As an attacker, maybe I’m going to check for this whether I know the version or not. But if I can use a README file to confirm my target is Apache 2.4.59, I’m much more likely to look closely at this CVE to see if it applies to the environment and if I can use it.

Sure, it is vulnerable without version confirmation, but the chances an attacker hones in on a particular flaw skyrocket when a software version can be confidently determined.

WordPress, the most widely used CMS, defines a standard for plugin README files.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/default_web_02.png)

**WordPress README Example**

It starts with enough information to get a rough idea of the plugin and WordPress versions (sometimes it’s directly listed), but even if it doesn’t, elsewhere the file usually contains a changelog that pinpoints the version.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/default_web_03-1.png)

**WordPress Changelog Example**

Why guess the version when the README will tell you?

### **Installation Artifacts**

It’s harder to count CVEs related to installation or update files, but plenty exist. One example is Atlassian Confluence, which was impacted by CVE-2023-22518, where a leftover installation file allowed attackers to reset the admin password.

Other artifacts may include example config files or scripts that, again, reveal installation information. Drupal, another popular CMS, includes half-a-dozen “dotfiles” (files that begin with a period) that *should* be restricted by default–but are often not due to a web server misconfiguration. It also includes files lik...