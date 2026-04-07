---
title: Qilin and Warlock Ransomware Use Vulnerable Drivers to Disable 300+ EDR Tools
url: https://thehackernews.com/2026/04/qilin-and-warlock-ransomware-use.html
source: The Hacker News
date: 2026-04-06
fetch_date: 2026-04-07T04:30:48.397603
---

# Qilin and Warlock Ransomware Use Vulnerable Drivers to Disable 300+ EDR Tools

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Qilin and Warlock Ransomware Use Vulnerable Drivers to Disable 300+ EDR Tools](https://thehackernews.com/2026/04/qilin-and-warlock-ransomware-use.html)

**Ravie Lakshmanan**Apr 06, 2026Ransomware / Endpoint Security

[![Qilin and Warlock Ransomware](data:image/png;base64... "Qilin and Warlock Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtrUKOrJ2Y_pSYHNcKDjbrBsZa2igYlNorTwmH31JNSjdA7VP84kXj23nmkk7DTqlrCUsfCjNo6xt-niyZeKeCR7VtBzMWW9eNUKzU0WGnpmw2yYjHBdboP2uF2UA8CCsdclyeDlRJcU7DEOD8OrFthlhQX-OkgePmyT__ZDQA4IXgRYbnNtp21MoleCTU/s1700-e365/lock-ransomware.jpg)

Threat actors associated with [Qilin](https://thehackernews.com/2025/10/qilin-ransomware-combines-linux-payload.html) and [Warlock](https://thehackernews.com/2026/02/warlock-ransomware-breaches.html) ransomware operations have been observed using the bring your own vulnerable driver ([BYOVD](https://thehackernews.com/2026/03/54-edr-killers-use-byovd-to-exploit-34.html)) technique to silence security tools running on compromised hosts, according to findings from Cisco Talos and Trend Micro.

Qilin attacks analyzed by Talos have been found to deploy a malicious DLL named "msimg32.dll," which initiates a multi-stage infection chain to disable endpoint detection and response (EDR) solutions. The DLL, launched via DLL side-loading, is capable of terminating more than 300 EDR drivers from almost every security vendor in the market.

"The first stage consists of a PE loader responsible for preparing the execution environment for the EDR killer component," Talos researchers Takahiro Takeda and Holger Unterbrink [said](https://blog.talosintelligence.com/qilin-edr-killer/). "This secondary payload is embedded within the loader in an encrypted form."

The DLL loader implements an array of techniques to evade detection. It neutralizes user-mode hooks, suppresses Event Tracing for Windows (ETW) event logs, and takes steps to conceal control flow and API invocation patterns. As a result, it allows the main EDR killer payload to be decrypted, loaded, and executed entirely in memory while entirely flying under the radar.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

Once launched, the malware makes use of two drivers -

* rwdrv.sys, a renamed version of "ThrottleStop.sys" that's used to gain access to the system's physical memory and act as a kernel-mode hardware access layer.
* hlpdrv.sys, to terminate processes associated with over 300 different EDR drivers belonging to various security solutions.

It's worth noting that both drivers have been used as part of BYOVD attacks carried out in conjunction with [Akira](https://thehackernews.com/2025/08/sonicwall-investigating-potential-ssl.html) and [Makop](https://thehackernews.com/2026/01/new-osiris-ransomware-emerges-as-new.html) ransomware intrusions.

"Prior to loading the second driver, the EDR killer component unregisters monitoring callbacks established by the EDR, ensuring that process termination can proceed without interference," Talos said. "It demonstrates the sophisticated tricks the malware is employing to circumvent or completely disable modern EDR protection features on compromised systems."

According to statistics compiled by [CYFIRMA](https://www.cyfirma.com/research/tracking-ransomware-jan-2026/) and [Cynet](https://www.cynet.com/blog/qilin-green-blood-0apt-ransomware-groups-to-watch-march-2026/), Qilin has [emerged](https://blog.talosintelligence.com/ransomware-in-2025-blending-in-is-the-strategy/) as the most active ransomware group in recent months, claiming hundreds of victims. The group has been linked to 22 out of 134 ransomware incidents that were reported in Japan in 2025, representing 16.4% of all attacks.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-G9T7oKmDVk_OCp7UjRDNUMcVCIIE-5hhpBsbE6ExXVl5WQNNT2c_TLAKaAK5cif1q8w58uBc-VuYmexWWYrcLnlM__0P5u8Wsopcg1tnIgfVOY7oOMzwUr8ttFXPArBUYxX22ugl5qAiOKsNzTqwPbVLkindO-2j-UP57d3ylUVh5MQO27NkXKCyAuHN/s1700-e365/talos.jpg)

"Qilin primarily relies on stolen credentials to gain initial access," Talos [said](https://blog.talosintelligence.com/an-overview-of-ransomware-threats-in-japan-in-2025-and-early-detection-insights-from-qilin-cases/). "After successfully breaching a target environment, the group places considerable emphasis on post-compromise activities, allowing it to methodically expand its control and maximize impact."

The cybersecurity vendor also noted that ransomware execution occurred on average roughly six days after the initial compromise, highlighting the need for organizations to detect malicious activity at the earliest possible stage and to prevent the deployment of ransomware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCYR3RFB_n5fGH99dW-begvmy-YET_Kxz3EdTkFIpO3ORgOxMi6g_7C2LKHwolltluGw7jZpmO6HPQ8VuD9U5z8-MITHHk_8G8v_uGakfjKPmuYN_B6tJqdmSp_bmYpaCpMt_WuXmQH6uMxnoUClPwykfoJDpiMNBdA2CewDoXvmlMQnF_qRxEwmSDcIrq/s1700-e365/ransomware.jpg)

The disclosure comes as the Warlock (aka Water Manaul) ransomware group continues to exploit unpatched Microsoft SharePoint servers, while updating its toolset for enhanced persistence, lateral movement, and defense evasion.This includes the use of [TightVNC](https://thehackernews.com/2025/09/from-mostererat-to-clickfix-new-malware.html) for persistent control and a legitimate-but-vulnerable [NSec driver](https://github.com/BlackSnufkin/BYOVD) ("NSecKrnl.sys") in a BYOVD attack to terminate security products at the kernel level, replacing the "googleApiUtil64.sys" driver used in prior campaigns.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

Also observed during the course of the Warlock attack in January 2026 were the following tools -

* [PsExec](https://www.silverfort.com/glossary/psexec/), for lateral movement.
* RDP Patcher, for facilitating concurren...