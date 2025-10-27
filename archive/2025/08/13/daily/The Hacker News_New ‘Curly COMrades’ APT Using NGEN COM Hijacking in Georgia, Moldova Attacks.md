---
title: New ‘Curly COMrades’ APT Using NGEN COM Hijacking in Georgia, Moldova Attacks
url: https://thehackernews.com/2025/08/new-curly-comrades-apt-using-ngen-com.html
source: The Hacker News
date: 2025-08-13
fetch_date: 2025-10-07T00:53:16.380358
---

# New ‘Curly COMrades’ APT Using NGEN COM Hijacking in Georgia, Moldova Attacks

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

# [New 'Curly COMrades' APT Using NGEN COM Hijacking in Georgia, Moldova Attacks](https://thehackernews.com/2025/08/new-curly-comrades-apt-using-ngen-com.html)

**Aug 12, 2025**Ravie LakshmananCyber Espionage / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5tCNabpGIibUaFVEXFDFsxFfz-2BpIqJPPeWdQvsUCd-Znm3DoxTzC0__25iFdRKqHmjfv2gbpetKWi93HTG-R1WP7tBolG_fZY-Er6tTAY3dPpV-Olvin8Ljb-6mtASMI020z0Qyl6VMAG9Xdzz6tiooVwBscutT-PBmV4Va44zc6qDyqQ-DiolX7UX5/s790-rw-e365/russian-hackers.png)

A previously undocumented threat actor dubbed **Curly COMrades** has been observed targeting entities in Georgia and Moldova as part of a cyber espionage campaign designed to facilitate long-term access to target networks.

"They repeatedly tried to extract the NTDS database from domain controllers -- the primary repository for user password hashes and authentication data in a Windows network," Bitdefender [said](https://businessinsights.bitdefender.com/curly-comrades-new-threat-actor-targeting-geopolitical-hotbeds) in a report shared with The Hacker News. "Additionally, they attempted to dump LSASS memory from specific systems to recover active user credentials, potentially plain-text passwords, from machines where users were logged on."

The activity, tracked by the Romanian cybersecurity company since mid-2024, has singled out judicial and government bodies in Georgia, as well as an energy distribution company in Moldova.

"Regarding the timeline, while we have been tracking the campaign since mid-2024, our analysis of the artifacts indicates that activity began earlier," Martin Zugec, technical solutions director at Bitdefender, told the publication. "The earliest confirmed date we have for the use of the MucorAgent malware is November 2023, though it is highly probable that the group was active before that time."

Curly COMrades are assessed to be operating with goals that are aligned with Russia's geopolitical strategy. It gets its name from the heavy reliance on the curl utility for command-and-control (C2) and data transfer, and the hijacking of the component object model (COM) objects.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The end goal of the attacks is to enable long-term access to carry out reconnaissance and credential theft, and leverage that information to burrow deeper into the network, collect data using custom tools, and exfiltrate to attacker-controlled infrastructure.

"The overall behavior indicates a methodical approach in which the attackers combined standard attack techniques with tailored implementations to blend into legitimate system activity," the company pointed out. "Their operations were characterized by repeated trial-and-error, use of redundant methods, and incremental setup steps - all aimed at maintaining a resilient and low-noise foothold across multiple systems."

A notable aspect of the attacks is the use of legitimate tools like [Resocks](https://blog.redteam-pentesting.de/2023/introducing-resocks/), SSH, and [Stunnel](https://www.stunnel.org) to create multiple conduits into internal networks and remotely execute commands using the stolen credentials. Another proxy tool deployed besides Resocks is [SOCKS5](https://github.com/earthquake/Socks5Server). The exact initial access vector employed by the threat actor is currently not known.

Persistent access to the infected endpoints is accomplished by means of a bespoke backdoor called MucorAgent, which hijacks class identifiers ([CLSIDs](https://learn.microsoft.com/en-us/windows/win32/com/clsid-key-hklm)) – globally unique identifiers that identify a COM class object – to target Native Image Generator ([Ngen](https://learn.microsoft.com/en-us/dotnet/framework/tools/ngen-exe-native-image-generator)), an ahead-of-time compilation service that's part of the .NET Framework.

"Ngen, a default Windows .NET Framework component that pre-compiles assemblies, provides a mechanism for persistence via a disabled scheduled task," Bitdefender noted. "This task appears inactive, yet the operating system occasionally enables and executes it at unpredictable intervals (such as during system idle times or new application deployments), making it a great mechanism for restoring access covertly."

Abusing the CLSID linked to Ngen underscores the adversary's technical prowess, while granting them the ability to execute malicious commands under the highly privileged SYSTEM account. It's suspected that there likely exists a more reliable mechanism for executing the specific task given the overall unpredictability associated with Ngen.

A modular .NET implant, MucorAgent is launched via a three-stage process and is capable of executing an encrypted PowerShell script and uploading the output to a designated server. Bitdefender said it did not recover any other PowerShell payloads.

"The design of the MucorAgent suggests that it was likely intended to function as a backdoor capable of executing payloads on a periodic basis," the company explained. "Each encrypted payload is deleted after being loaded into memory, and no additional mechanism for regularly delivering new payloads was identified."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also weaponized by Curly COMrades are legitimate-but-compromised websites for use as relays during C2 communications and data exfiltration in a bid to fly under the radar by blending malicious traffic with normal network activity. Some of the other tools observed in the attacks are listed below -

* CurlCat, which is used to facilitate bidirectional data transfer between standard input and output streams (STDIN and STDOUT) and C2 server over HTTPS by routing the traffic through a compromised site
* RuRat, a legitimate Remote Monitoring and Management (RMM) program for persistent access
* Mimikatz, which is used to extract credentials from memory
* Various built-in commands like netstat, tasklis...