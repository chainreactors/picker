---
title: John Strand's 11 Core Skills: For SOC Analysts
url: https://www.blackhillsinfosec.com/soc-core-skills/
source: Black Hills Information Security
date: 2026-10-28
fetch_date: 2026-10-29T07:51:08.722338
---

# John Strand's 11 Core Skills: For SOC Analysts

[Skip to main content](#main-content)

[![BHIS](/uploads/media/bhis-text-bhis-f909d4808e69428ba2547d42a650842f.png)![BHIS](/uploads/media/bhis-text-bhis-light-f0fc7d40d92b4eccb72ef18ffe68bef6.png)](/)

Services

[All Services](/services/ "All Services")

[Penetration Testing](/services/traditional-penetrating-testing/ "Penetration Testing")

[Continuous Penetration Testing](/services/antisoc/ "Continuous Penetration Testing")

[Web Application Testing](/services/web-appllication-testing/ "Web Application Testing")

[ActiveSOC](https://activesoc.blackhillsinfosec.com/ "ActiveSOC")

[Fusion PenTest](/fusion-penetration-testing/ "Fusion PenTest")

[AI Security Assessments](/services/ai-security-assessments/ "AI Security Assessments")

[Incident Response](/services/incident-response/ "Incident Response")

[Blue Team Services](/services/blue-team-services/ "Blue Team Services")

[Blockchain Security](/services/blockchain-security/ "Blockchain Security")

[High-Profile Risk Assessments](/services/high-profile-risk-assessments/ "High-Profile Risk Assessments")

[Complete Service Guide](/services/complete-service-guide/ "Complete Service Guide")

[Governance, Risk and Compliance](/grc/ "Governance, Risk and Compliance")

[Contact Us](/contact-us/ "Contact Us")

About Us

[BHIS Tribe of Companies](/bhis-tribe-of-companies/ "BHIS Tribe of Companies")

[Admin Staff](/about/admin-staff/ "Admin Staff")

[Security Consultants](/about/security-consultants/ "Security Consultants")

[BHIS Privacy Policy](/bhis-online-privacy-policy/ "BHIS Privacy Policy")

Free Resources

[Blogs](/blog/ "Blogs")

[Webcasts](/webcasts/ "Webcasts")

[Free Cyber Security Tools](/free-cybersecurity-tools/ "Free Cyber Security Tools")

[Free Cybersecurity Webcasts](/free-cybersecurity-webcasts/ "Free Cybersecurity Webcasts")

[BHIS Podcasts](/bhis-podcasts/ "BHIS Podcasts")

[RITA](/rita/ "RITA")

Training

[BHIS & Antisyphon Training](/bhis-and-antisyphon-training/ "BHIS & Antisyphon Training")

[Wild West Hackin' Fest](/wild-west-hackin-fest/ "Wild West Hackin' Fest")

Community

[Connect](/community/ "Connect")

[Discord](https://discord.gg/BHIS "Discord")

[LinkedIn](https://www.linkedin.com/company/black-hills-information-security/ "LinkedIn")

[YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos "YouTube")

[Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social "Bluesky")

[Twitter/X](https://twitter.com/BHinfoSecurity "Twitter/X")

[Upcoming Events](/community/events/ "Upcoming Events")

Fun Stuff

[Backdoors and Breaches](/tools/backdoorsandbreaches/ "Backdoors and Breaches")

[Free Lab Fridays](/free-lab-fridays/ "Free Lab Fridays")

[Merch, Zines & More](/spearphish-general-store/ "Merch, Zines & More")

[PROMPT# Zine](/prompt-zine/ "PROMPT# Zine")

[REKCAH](/rekcah/ "REKCAH")

[Books](/tools/books/ "Books")

[Game of Life](/game-of-life/ "Game of Life")

1. [Home](/)
2. [Blog](/blog)
3. John Strand's 11 Core Skills: For SOC Analysts

[SOC](/blog?topic=SOC)[Active SOC](/blog?topic=Active%20SOC)[Network](/blog?topic=Network)[EDR](/blog?topic=EDR)[IR](/blog?topic=IR)[Threat Hunting](/blog?topic=Threat%20Hunting)

![John Strand](/uploads/media/team/john-strand.jpg)

[John Strand](/blog?author=john-strand "See all posts by John Strand")Owner & Security Consultant

![](/uploads/media/for-soc-analysts-f63324b86eb541c48e8381775a4966c0.png)

|  |
| --- |
| *This article was originally published in the InfoSec Survival Guide: Blue Book — SOC Analysts. Read it free online [HERE](https://www.blackhillsinfosec.com/prompt-zine/), or grab it on the [Spearphish General Store](https://spearphish-general-store.myshopify.com/collections/infosec-survival-guides) (free digital download or a $1.25 physical copy, your call).* |

The cybersecurity battlefield evolves daily, with SOC analysts serving as front-line defenders. After years of training SOC teams, I’ve identified 11 core skills that separate effective defenders from the rest.

Here’s the problem: we’re training analysts to look for needles in haystacks when they don’t even know what hay looks like. Too many enter SOC positions without understanding the systems they’re trying to protect.

### 1. Understanding Operating Systems

You can’t defend what you don’t understand. Period. Master both Windows and Linux. Not just surface stuff, but really get how they work under the hood. Learn through the incident response lens:”If this system were hacked, how would I find the bad guys?”

### 2. Network Traffic Analysis

Understand TCP/IP and how traffic actually flows (the OSI model matters less than knowing what a SYN flood, DNS tunnel, or C2 beacon looks like on the wire). Know the difference between TCP and UDP, and establish baselines for what normal traffic looks like in your environment.

### 3. Memory Analysis

Memory forensics shows you malware that might be invisible on disk. Tools like Volatility let you examine processes, connections, and DLLs from a memory dump. This works even when attackers delete their tools or use fileless malware. It’s like catching someone with their hand in the cookie jar.

### 4. Log Analysis

Logs are your investigative breadcrumbs. Know which ones to collect and how to make sense of them. Remember, no single log tells the whole story. You need to connect multiple data points, like a detective piecing together clues at a crime scene.

### 5. Endpoint Detection and Response

Master your EDR solutions. Understand how they work, what they can do, and where they fall short. No EDR catches everything. You need to tune these tools, like adjusting the sights on a rifle for better accuracy.

### 6. Threat Hunting

Don’t just sit back waiting for alerts. Get out there and hunt! Look for threats that slipped past your automated systems. Combine smart hypotheses with data analysis to find attackers living off the land, using legitimate tools for evil purposes.

### 7. Malware Analysis

Every SOC analyst should know basic static and dynamic analysis. Look at the file without running it, then observe its behavior in a safe sandbox. Learn to spot common techniques like obfuscation and persistence. Know thy enemy, right?

### 8. Vulnerability Management

Understand different vulnerability types and how they’re exploited. Don’t just focus on CVSS scores. Consider actual exploitability in your environment and the potential impact. A “critical” vulnerability that can’t actually be exploited in your environment isn’t critical for you.

### 9. Incident Response

When stuff hits the fan, know what to do. Identify what happened, contain it, kick out the attackers, and recover your systems. Document everything. Not just for compliance, but so your team can learn and improve.

### 10. Automation and Scripting

Automate the boring stuff with PowerShell, Python, or Bash. Create tools that do the repetitive work for you. This frees you up to focus on the complex problems that need human brainpower.

### 11. Communication and Documentation

Technical skills alone won’t cut it. You need to explain complex technical stuff to different audiences. The most brilliant analysis in the world is useless if you can’t make the bosses understand why they should care.

### Conclusion

Mastering these skills won’t happen overnight, but they’re the foundation of being an effective SOC analyst. What makes great analysts stand out isn’t just knowing individual skills but connecting dots across domains: seeing how network traffic ties to endpoint behavior, when log weirdness might point to memory-resident malware, and how vulnerabilities create openings for attackers

By building these core skills, you’ll be ready to protect your organization against even the nastiest threats out there..

![](/uploads/media/infosec-survival-guide/infosec-survival-guide-teal-book-threat-hunting-final-c1-13eaa664397244fd88a1dd657307b8dc.png)

---

***Explore the Infosec Survival Guide and more… for FREE!***

*Get instant access to every issue of the...