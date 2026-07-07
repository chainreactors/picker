---
title: Suspected China-Nexus Hackers Use Fake Indian Tax Filing Utility to Deploy DcRAT
url: https://thehackernews.com/2026/07/suspected-china-nexus-hackers-use-fake.html
source: The Hacker News
date: 2026-07-06
fetch_date: 2026-07-07T06:05:05.689862
---

# Suspected China-Nexus Hackers Use Fake Indian Tax Filing Utility to Deploy DcRAT

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Suspected China-Nexus Hackers Use Fake Indian Tax Filing Utility to Deploy DcRAT](https://thehackernews.com/2026/07/suspected-china-nexus-hackers-use-fake.html)

**Ravie Lakshmanan**Jul 06, 2026Cyber Espionage / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0L8iGbVZ6lxBg26K2nsc6uYpFED8ZcgCtrh4C34U4oixLPC0OKHOWWpiPBfaSwe-tpOTbCqZfRZQTMoropayZXEm0GXTtKpyBuBPRk9zF-0WPRprknYiaI2DXLDZnQb8t70R7-0Fjl5G-NNCQFF-Ex40vQZMbUJmJ2JLyXJUjYdAVvgjl3_oBF5wbHrHl/s1700-e365/income-tax.jpg)

A suspected China-nexus threat activity cluster has been observed targeting Indian taxpayers, tax professionals, and corporate finance teams to deliver a remote access trojan designed to steal sensitive data from compromised hosts.

The multi-stage campaign, codenamed Operation DragonReturn by Seqrite Labs, involves sending spear-phishing emails impersonating the Income Tax Department of India. It was first observed on May 18, 2026. The activity, per the cybersecurity company, coincides with the annual income tax filing season in the country.

"It is not opportunistic – the precision of the lure document, the use of real legal citations, bilingual content, and active payload rotation indicate a deliberate, resourced, and sustained threat operation focused exclusively on the Indian taxpayer ecosystem," security researchers Dixit Panchal and Soumen Burma [said](https://www.seqrite.com/blog/operation-dragonreturn-china-nexus-cyber-espionage-campaign-targeting-govt-of-india-mof-tax-infrastructure-via-multi-stage-dcrat-deployment/).

The end goal of the campaign is assessed to be the deployment of malware for financial gain or sensitive data theft.

The attack chains begin with phishing messages masquerading as India's income tax department, using tax violations and penalty lures to induce a false sense of urgency and trick users into clicking on a malicious link ("govtop[.]one/incometax") embedded within PDF attachments.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The bogus landing page, for its part, instructs users to download a ZIP archive containing what appears to be a [common offline utility](https://www.incometax.gov.in/iec/foportal/downloads) provided by the department to file tax returns, but, in reality, is engineered to sideload a malicious DLL ("nvdaHelperRemote.dll"), which, in turn, injects another payload into memory.

This payload ensures it's running with administrative privileges, and if not, triggers a User Account Control (UAC) prompt to get the user to run it with elevated permissions. Once launched, it performs checks to avoid executing within analysis and sandboxed environments, and then retrieves a JPG image ("lllyd.jpg") from a hard-coded server ("204.194.48[.]250") and stores it as "C:\Windows\background.jpg."

"This image file is used as a container for a secondary payload, from which a 504 KB DLL is extracted and written to 'C:\Program Files\Windows Media Player\nvdaHelperRemote.dll,'" Seqrite Labs explained. "After extracting the payload, the malware copies itself as 'Mixed Reality.exe' and establishes persistence by creating a Windows service named MixedSvc, configured to start automatically on system boot."

"This behaviour confirms that the sample functions as a downloader and installer, using image-based payload concealment and Windows service persistence to maintain long-term access to the infected system."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhruPjuEUNx3oeLkjZnayl5tAwDMOkr6p3k66Y98oyxhc664vGJunx2qJ9DkE0SHsUD4g3zKeID3UBEb8YQQrw8irnMVqwCvUG1redfiwaVTs-Jm5Ndu7gzx-H5A7UIFxiOKWPm4Jd6S1s2UYnXWEG8O3PoCVJ_NSuPFG7RslQDXymmCtYE_twfRBrJOWpJ/s1700-e365/seq.png)

The "Mixed Reality.exe" binary is responsible for deploying two different payloads, one of which is a .NET malware loader that carries out anti-analysis checks, establishes persistence, disables Windows AMSI scanning, and decrypts and loads [DCRat](https://thehackernews.com/2022/05/experts-sound-alarm-on-dcrat-backdoor.html) on the infected machine. The second payload features capabilities to take screenshots and exfiltrate data to a remote server ("kkxqbh[.]top").

Exactly who is behind the activity is unclear, but infrastructure analysis indicates the use of IP addresses belonging to ChinaNet, as well as a Chinese-language web management panel exposed by the DCRat command-and-control (C2) server ("223.26.63[.]40"). In addition, Seqrite said it identified infrastructure and tactical overlaps with Silver Fox, a Chinese cybercrime group [previously attributed](https://thehackernews.com/2025/12/silver-fox-targets-indian-users-with.html) to tax-themed phishing campaigns that deliver ValleyRAT.

Based on these similarities, it's suspected that the campaign is the work of a China-aligned threat actor conducted with an aim to establish covert access for intelligence collection, credential theft, and systematic data exfiltration, Seqrite concluded.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The disclosure comes as LevelBlue [said](https://www.levelblue.com/blogs/spiderlabs-blog/an-analysis-of-valleyrat-infection-campaigns-from-fake-installers-japanese-malicious-emails) it detected two distinct campaigns that employ [fake installers](https://thehackernews.com/2025/12/silver-fox-uses-fake-microsoft-teams.html) for LINE and phishing emails with salary adjustment lures to distribute [ValleyRAT](https://thehackernews.com/2026/05/silver-fox-deploys-abcdoor-malware-via.html) targeting Chinese- and Japanese-speaking users.

The email-driven campaign begins with a malicious email containing a URL link that...