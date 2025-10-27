---
title: Golden Chickens Deploy TerraStealerV2 to Steal Browser Credentials and Crypto Wallet Data
url: https://thehackernews.com/2025/05/golden-chickens-deploy-terrastealerv2.html
source: The Hacker News
date: 2025-05-06
fetch_date: 2025-10-06T22:34:47.819551
---

# Golden Chickens Deploy TerraStealerV2 to Steal Browser Credentials and Crypto Wallet Data

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

# [Golden Chickens Deploy TerraStealerV2 to Steal Browser Credentials and Crypto Wallet Data](https://thehackernews.com/2025/05/golden-chickens-deploy-terrastealerv2.html)

**May 05, 2025**Ravie LakshmananMalware / Browser Security

[![Malware Steal Browser Credentials and Crypto Wallet Data](data:image/png;base64... "Malware Steal Browser Credentials and Crypto Wallet Data")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1a9_-RHYv5m5VEtMKpT8Mgak_STgbyVtoWcEHRwpXNnePtrvWRpuMcgskRY6Zy2uOifE-hl_qKe5N6-wSt2JhgHrKCs8MDDxm6tBF5Nt785WCGUh_ijy5e-8q8DRPib56D_hfvqhBoV32X9ie1Dmco7iXaDI6H2tfZl0SaQN4qyjYcUaOba_n7A70BWjU/s790-rw-e365/hackers.jpg)

The threat actors known as Golden Chickens have been attributed to two new malware families dubbed TerraStealerV2 and TerraLogger, suggesting continued development efforts to fine-tune and diversify their arsenal.

"TerraStealerV2 is designed to collect browser credentials, cryptocurrency wallet data, and browser extension information," Recorded Future Insikt Group [said](https://www.recordedfuture.com/research/terrastealerv2-and-terralogger). "TerraLogger, by contrast, is a standalone keylogger. It uses a common low-level keyboard hook to record keystrokes and writes the logs to local files."

Golden Chickens, also known as Venom Spider, is the name given to a financially motivated threat actor linked to a [notorious](https://thehackernews.com/2024/06/moreeggs-malware-disguised-as-resumes.html) malware family called [More\_eggs](https://thehackernews.com/2024/10/fake-job-applications-deliver-dangerous.html). It's known to be active since at least 2018, offering its warez under a malware-as-a-service (MaaS) model.

Campaigns distributing More\_eggs entail the use of spear-phishing emails to [target](https://thehackernews.com/2023/12/bazacall-phishing-scammers-now.html) hiring managers using fake resumes, allowing attackers to steal confidential data. Other campaign waves have [singled out](https://thehackernews.com/2021/04/hackers-targeting-professionals-with.html) professionals on LinkedIn with weaponized job offers to deliver the malware.

Recent attack chains documented by Arctic Wolf have used phishing emails as a ploy to lead recipients to an actor-controlled website from where they can download a decoy resume, which is nothing but a Windows Shortcut (.LNK) file that, in turn, uses a batch script to launch the lure document while running a JavaScript malware in the background.

The JavaScript payload acts as a conduit to deploy a More\_eggs\_Dropper, a DLL file that's designed to launch another JavaScript malware called TerraLoader. This malware is then used to decrypt and load More\_eggs.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The threat actor has demonstrated a continued investment in the development and maintenance of its backdoor infrastructure over time," Arctic Wolf Labs [said](https://arcticwolf.com/resources/blog/venom-spider-uses-server-side-polymorphism-to-weave-a-web-around-victims/). "This is evidenced by the use of sophisticated code obfuscation and code encryption, which improve its stealth and evasiveness against defenders."

As of 2023, Golden Chickens has been attributed to an online persona known as badbullzvenom, an account that's believed to be operated jointly by individuals from [Canada](https://thehackernews.com/2023/01/experts-uncover-identity-of-mastermind.html) and [Romania](https://thehackernews.com/2023/05/meet-jack-from-romania-mastermind.html). Some of the other malicious tools developed by the e-crime group include More\_eggs lite (oka lite\_more\_eggs), VenomLNK, TerraLoader, and TerraCrypt.

Late last year, Zscaler ThreatLabz [detailed](https://thehackernews.com/2024/12/moreeggs-maas-expands-operations-with.html) new Golden Chickens-related activity involving a backdoor called RevC2 and a loader referred to as Venom Loader, both of which are delivered via a VenomLNK.

The latest findings from Recorded Future show that the threat actors are continuing to work on their offerings, releasing an updated version of their stealer malware that's capable of harvesting data from browsers, cryptocurrency wallets, and browser extensions.

TerraStealerV2 has been distributed via various formats, such as executable files (EXEs), dynamic-link libraries (DLLs), Windows Installer packages (MSI), and shortcut (LNK) files.

In all these cases, the stealer payload is delivered in the form of an OCX (short for Microsoft's OLE Control Extension) payload that's retrieved from an external domain ("wetransfers[.]io").

"While it targets the Chrome 'Login Data' database to steal credentials, it does not bypass Application Bound Encryption ([ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)) protections introduced in Chrome updates after July 2024, indicating the malware code is outdated or still under development," the cybersecurity company said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6-Ww4gwf6GnDyvmticDVV4yVaXvv84HJVox7ODvI9QpLwwyo3dAsfzadQccdQ-iwLz5Ew4OXNIQy52a8tPTJFJDNC3nYe1dv8GGFMDgAPyjxjy2BiG7Lcly8gEbNujHKaDL4NJkzcq1S-nB0WmfVGuVMaTinr67aLSXL2yWm-HIWhPTL2FQ40V4CUdCst/s790-rw-e365/exit.jpg)

The data captured by TerraStealerV2 is exfiltrated to both Telegram and the domain "wetransfers[.]io." It also leverages trusted Windows utilities, such as regsvr32.exe and mshta.exe, to evade detection.

TerraLogger, also propagated as an OCX file, is engineered to record keystrokes. However, it does not include functionality for data exfiltration or command-and-control (C2) communication, suggesting it is either in early development or intended to be used in conjunction with another malware part of the Golden Chickens MaaS ecosystem.

"The current state of TerraStealerV2 and TerraLogger suggests that both tools remain under active development and do not yet exhibit the level of stealth typically associated with mature Golden Chicken...