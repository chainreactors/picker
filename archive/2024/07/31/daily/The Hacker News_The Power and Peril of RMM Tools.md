---
title: The Power and Peril of RMM Tools
url: https://thehackernews.com/2024/07/the-power-and-peril-of-rmm-tools.html
source: The Hacker News
date: 2024-07-31
fetch_date: 2025-10-06T17:47:00.603501
---

# The Power and Peril of RMM Tools

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [The Power and Peril of RMM Tools](https://thehackernews.com/2024/07/the-power-and-peril-of-rmm-tools.html)

**Jul 30, 2024**The Hacker NewsNetwork Management / IT Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVsEmMhcvcq75qU6Eqio1WRmZuA1IMIaR3979YNtorLL3vJnm2lQ0rp6bXCsTEVmD1UIZZLLcUGyqo4qpG7ETt94QwUcoWftl832uvPDOx-zqSxrKg4SbWIW9B1niui1fziI9ZIU_ysSssnZKkJHxA_fyVlg05a872NzATTIDCxhDqc6teTBZXicN3MoQ/s790-rw-e365/main.png)

As more people work remotely, IT departments must manage devices distributed over different cities and countries relying on VPNs and remote monitoring and management (RMM) tools for system administration.

However, like any new technology, RMM tools can also be used maliciously. Threat actors can establish connections to a victim's device and run commands, exfiltrate data, and stay undetected.

This article will cover real-world examples of RMM exploits and show you how to protect your organization from these attacks.

## **What are RMM tools?**

RMM software simplifies network management, allowing IT professionals to remotely solve problems, install software, and upload or download files to or from devices.

Unfortunately, this connection is not always secure, and attackers can use malicious software to connect their servers to a victim's device. As these connections become easier to detect, however, [ransomware-as-a-service (RaaS)](https://www.varonis.com/blog/ransomware-as-a-service?hsLang=en) groups have had to adjust their methods.

In most of the cyber incidents Varonis investigated last year, RaaS gangs employed a technique known as [Living off the Land](https://www.cisa.gov/sites/default/files/2024-02/Joint-Guidance-Identifying-and-Mitigating-LOTL_V3508c.pdf), using legitimate IT tools to gain remote control, navigate networks undetected, and steal data.

RMM tools enable attackers to blend in and evade detection. They and their traffic are typically "ignored" by security controls and organizational security policies, such as application whitelisting.

This tactic also helps script kiddies — once connected, they will find everything they need already installed and ready for them.

Our research identified two main methods attackers use to manipulate RMM tools:

1. **Abusing existing RMM tools:** Attackers gain initial access to an organization's network using preexisting RMM tools. They exploit weak or default credentials or tool vulnerabilities to gain access without triggering detection.
2. **Installing new RMM tools:** Attackers install their preferred RMM tools by first gaining access to the network. They use phishing emails or social engineering techniques to trick victims into unwittingly installing the RMM tool on their network.

Below are common RMM tools and RaaS gangs:

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_JZF2UHwT3HT7_sO2g9-_FoGklX3UcHwrZCwVtTkdEtPnCrG9f70T9rY2cUCxp-KS_ZuIBY8GuPWiU2j31KlUo_B84zsRQbeRXq39ARiDZSlBSTDUqbr6GRdWgO5DNrhwtd_w6IA8u2Y-BLR3056IJcO_FYsWM39UEosrfzC52JVIAP1f5YmEXtGyDpk/s790-rw-e365/2.png) |
| Common RMM tools and RaaS gangs |

## **Real-world examples of RMM exploits**

During a recent investigation, our [Managed Data Detection and Response (MDDR)](https://www.varonis.com/products/mddr?hsLang=en) team analyzed an organization's data and found, in the PowerShell history of a compromised device, evidence of an RMM tool named "KiTTY."

This software was a modified version of PuTTY, a well-known tool for creating telnet and SSH sessions with remote machines. Because PuTTY is a legitimate RMM tool, none of the organization's security software raised any red flags, so KiTTY was able to create reverse tunnels over port 443 to expose internal servers to an AWS EC2 box.

The Varonis team conducted a comprehensive analysis. They found that the sessions to the AWS EC2 box using KiTTY were key to revealing what happened, how it was done, and — most importantly — what files were stolen.

This crucial evidence was a turning point in the investigation and helped trace the entire attack chain. It also revealed the organization's security gaps, how to address them, and the potential consequences of this attack.

## **Strategies to defend RMM tools**

Consider implementing the following strategies to reduce the chance of attackers abusing RMM tools.

### **An application control policy**

Restrict your organization from using multiple RMM tools by enforcing an application control policy:

* Ensure RMM tools are updated, patched, and accessible only to authorized users with MFA enabled
* Proactively block both inbound and outbound connections on forbidden RMM ports and protocols at the network perimeter

One option is to create a [Windows Defender Application Control (WDAC)](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac-and-applocker-overview) policy using PowerShell that whitelists applications based on their publisher. It's important to note that creating WDAC policies requires administrative privileges, and deploying them via Group Policy requires domain administrative privileges.

As a precaution, you should test the policy in audit mode before deploying it in enforce mode to avoid inadvertently blocking necessary applications.

1. **Open PowerShell with administrative privileges**
2. **Create a new policy:** You can create a new policy using the **New-CIPolicy** cmdlet. This cmdlet takes a path to a directory or a file, scans it, and makes a policy that allows all files in that path, such as executables and DLL files, to run on your network.

   For example, if you want to allow everything signed by the publisher of a specific application, you can follow the example below:
   New-CIPolicy -FilePath "C:\Path\To\Application.exe" -Level Publisher -UserPEs -Fallback Hash -Enable -OutputFilePath "C:\Path\To\Policy.xml"

   In this command, **-FilePath** specifies the path to the ...