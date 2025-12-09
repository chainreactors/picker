---
title: Experts Confirm JS#SMUGGLER Uses Compromised Sites to Deploy NetSupport RAT
url: https://thehackernews.com/2025/12/experts-confirm-jssmuggler-uses.html
source: The Hacker News
date: 2025-12-08
fetch_date: 2025-12-09T03:18:21.426228
---

# Experts Confirm JS#SMUGGLER Uses Compromised Sites to Deploy NetSupport RAT

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Experts Confirm JS#SMUGGLER Uses Compromised Sites to Deploy NetSupport RAT](https://thehackernews.com/2025/12/experts-confirm-jssmuggler-uses.html)

**Dec 08, 2025**Ravie LakshmananMalware / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCgAhdt5sz3PXhLRrV59c310Qk-9hJwShYKfrpg9cq5fdx7FH4hzseiqnNqE8X0_skZaT476KMf0GzbvSRJjQeO15Ra468a4l5C71u-nXGm3IrRQXlDzgf-_lYNldneG0WwsR81AK7jSvkeaO49RZlYoWTbATFVSAFDIl1NOogHhOUpzyc3IXTsQz6WyMv/s790-rw-e365/hacked-website.jpg)

Cybersecurity researchers are calling attention to a new campaign dubbed **JS#SMUGGLER** that has been observed leveraging compromised websites as a distribution vector for a remote access trojan named [NetSupport RAT](https://thehackernews.com/2025/02/threat-actors-exploit-clickfix-to.html).

The attack chain, analyzed by Securonix, involves three main moving parts: An obfuscated JavaScript loader injected into a website, an HTML Application (HTA) that runs encrypted PowerShell stagers using "mshta.exe," and a PowerShell payload that's designed to download and execute the main malware.

"NetSupport RAT enables full attacker control over the victim host, including remote desktop access, file operations, command execution, data theft, and proxy capabilities," researchers Akshay Gaikwad, Shikha Sangwan, and Aaron Beardslee [said](https://www.securonix.com/blog/jssmuggler-multi-stage-hidden-iframes-obfuscated-javascript-silent-redirectors-netsupport-rat-delivery/).

There is little evidence at this stage to tie the campaign to any known threat group or country. The activity has been found to target enterprise users through compromised websites, indicative of a broad-strokes effort.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

The cybersecurity company described it as a multi-stage web-based malware operation that employs hidden iframes, obfuscated loaders, and layered script execution for malware deployment and remote control.

In these attacks, silent redirects embedded into the infected websites act as a conduit for a heavily scrambled JavaScript loader ("phone.js") retrieved from an external domain, which then profiles the device to determine whether to serve a full-screen iframe (when visiting from a mobile phone) or load another remote second-stage script (when visiting from a desktop).

The invisible iframe is designed to direct the victim to a malicious URL. The JavaScript loader incorporates a tracking mechanism to ensure that the malicious logic is fired only once and during the first visit, thereby minimizing the chances of detection.

"This device-aware branching enables attackers to tailor the infection path, hide malicious activity from certain environments, and maximize their success rate by delivering platform-appropriate payloads while avoiding unnecessary exposure," the researchers said.

The remote script downloaded in the first stage of the attack lays the foundation by constructing at runtime a URL from which an HTA payload is downloaded and executed using "mshta.exe." The HTA payload is another loader for a temporary PowerShell stager, which is written to disk, decrypted, and executed directly in memory to evade detection.

Furthermore, the HTA file is run stealthily by disabling all visible window elements and minimizing the application at startup. Once the decrypted payload is executed, it also takes steps to remove the PowerShell stager from disk and terminates itself to avoid leaving as much forensic trail as possible.

The primary goal of the decrypted PowerShell payload is to retrieve and deploy NetSupport RAT, granting the attacker complete control over the compromised host.

"The sophistication and layered evasion techniques strongly indicate an actively maintained, professional-grade malware framework," Securonix said. "Defenders should deploy strong CSP enforcement, script monitoring, PowerShell logging, mshta.exe restrictions, and behavioral analytics to detect such attacks effectively."

### CHAMELEON#NET Delivers Formbook Malware

The disclosure comes weeks after the company also detailed another multi-stage malspam campaign dubbed CHAMELEON#NET that uses phishing emails to deliver [Formbook](https://thehackernews.com/2023/02/formbook-malware-spreads-via.html), a keylogger and information stealer. The email messages are aimed at luring victims in the National Social Security Sector into downloading a seemingly harmless archive after their credentials on a bogus webmail portal designed for this purpose.

"This campaign begins with a phishing email that tricks users into downloading a .BZ2 archive, initiating a multi-stage infection chain," Sangwan [said](https://www.securonix.com/blog/chameleonnet-a-deep-dive-into-multi-stage-net-malware-leveraging-reflective-loading-and-custom-decryption-for-stealthy-operations/). "The initial payload is a heavily obfuscated JavaScript file that acts as a dropper, leading to the execution of a complex VB.NET loader. This loader uses advanced reflection and a custom conditional XOR cipher to decrypt and execute its final payload, the Formbook RAT, entirely in memory."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

Specifically, the JavaScript dropper decodes and writes to disk in the %TEMP% directory two additional JavaScript files -

* svchost.js, which drops a .NET loader executable dubbed [DarkTortilla](https://thehackernews.com/2022/08/researchers-detail-evasive-darktortilla.html) ("QNaZg.exe"), a crypter that's often used to distribute next-stage payloads
* adobe.js, which drops a file named "PHat.jar," an MSI installer package that exhibits similar behavior as "svchost.js"

In this campaign, the loader is configured to decrypt and execute an embedded DLL, the Formbook malware. Persistence is achieved by adding it to the Windows startup folder to ensure that it's automatically launched upon a system reboot. Alternatively, it also manages persistence through the Windows Registry...