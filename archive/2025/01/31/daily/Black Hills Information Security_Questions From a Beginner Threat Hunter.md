---
title: Questions From a Beginner Threat Hunter
url: https://www.blackhillsinfosec.com/questions-from-a-beginner-threat-hunter/
source: Black Hills Information Security
date: 2025-01-31
fetch_date: 2025-10-06T20:10:38.982867
---

# Questions From a Beginner Threat Hunter

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

30
Jan
2025

[Hunt Teaming](https://www.blackhillsinfosec.com/category/blue-team/hunt-teaming/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/)
[Beginner](https://www.blackhillsinfosec.com/tag/beginner/), [On the Hunt](https://www.blackhillsinfosec.com/tag/on-the-hunt/), [PROMPT#](https://www.blackhillsinfosec.com/tag/prompt/), [Q&A](https://www.blackhillsinfosec.com/tag/qa/), [threat hunting](https://www.blackhillsinfosec.com/tag/threat-hunting/)

# [Questions From a Beginner Threat Hunter](https://www.blackhillsinfosec.com/questions-from-a-beginner-threat-hunter/)

*Answered by [Chris Brenton of Active Countermeasures](https://www.activecountermeasures.com/about-us/)* | *Questions compiled from the infosec community by Shelby Perry*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/promptthreat_header.png)

*This article was originally published in the Threat Hunting issue of our infosec zine, PROMPT#. Find it free online [HERE](https://www.blackhillsinfosec.com/prompt-zine/prompt-issue-threat-hunting/).*

### **Q:** What is the primary difference between threat hunting and threat detection?

**A:** *Threat detection* is the act of detecting malicious activity on the network. This may occur through a number of different means, like an alert being triggered or during a forensic analysis. Threat detection is a very generic term and the process can be passive or active.

*Threat hunting* is specific to actively searching through network and host data, looking for indicators of compromise. This activity is performed regardless of whether any alerts have been triggered.

### **Q:** What’s required to start threat hunting?

**A:** Process-wise*:* The first step is to identify what checks you wish to perform and what data is needed to perform that check. For example, if you want to hunt for C2 communications, you need a way to analyze all traffic passing between the internal network and the internet. This is usually accomplished by capturing traffic at the internal interface of the firewall. This may be done with a network tap or by leveraging a switch SPAN port. Once the data is collected, you need tools and processes to distinguish between C2 communications and normal traffic patterns. C2 can be pretty stealthy, so you may need the ability to analyze the traffic in 12 hour(+) “chunks” of time in order to be able to distinguish it from normal patterns.

Knowledge-wise: For network threat hunting, it’s extremely helpful to have a good knowledge of networking and protocol communications. For example, HTTPS communications typically use the SSL/TLS protocols over TCP port 443. Many C2 tools pass their traffic over TCP/443, but simply obfuscate it (they don’t use SSL/TLS). So if you are network savvy and see traffic using TCP/443 that does not include the SSL/TLS handshake, you know that’s something that needs to be investigated further.

If you plan to do your hunts on the endpoints, you need to have a strong knowledge of every operating system and the applications they are using. For example, PowerShell is a powerful scripting language built into the Windows operating system. It is rare that anyone outside of the IT or security teams would have a legitimate reason for using it. So as a threat hunter, you would need to know that Nancy-in-accounting running PowerShell is extremely suspicious behavior.

### **Q:** What does C2 over DNS mean?

**A:** C2 over DNS is the practice of an attacker embedding the C2 traffic inside legitimate DNS queries. This causes your DNS forwarders to happily send the C2 traffic out to the internet. The attackers will then register a remote domain and set up their C2 servers as the authoritative DNS servers for the domain. This means that your DNS servers will send the C2 traffic to the remote C2 server. What makes this C2 activity so stealthy is that the compromised system does not generate any new traffic headed to the internet. Instead, you simply see an increase in the number of DNS queries.

### **Q:** There are so many tools out there… How do I know which to use for what?

**A:** Try them out! See which works best in your environment and matches your workflow. Also, don’t expect one tool to always be a perfect fit for every need. For example, if I’m analyzing overall traffic flow, I’ll use a tool like Zeek. If I’m looking for specific patterns, I’ll use Suricata. For specific traffic flows, I’ll use Tshark. For a deep analysis on a single session, I’ll turn to Wireshark. **My best advice: pick one tool and stick with it.** **When it doesn’t help with a specific challenge, check out other tools.**

### **Q:** ...