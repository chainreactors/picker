---
title: ThreatsDay Bulletin: Spyware Alerts, Mirai Strikes, Docker Leaks, ValleyRAT Rootkit — and 20 More Stories
url: https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html
source: The Hacker News
date: 2025-12-11
fetch_date: 2025-12-12T03:23:19.714865
---

# ThreatsDay Bulletin: Spyware Alerts, Mirai Strikes, Docker Leaks, ValleyRAT Rootkit — and 20 More Stories

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

# [ThreatsDay Bulletin: Spyware Alerts, Mirai Strikes, Docker Leaks, ValleyRAT Rootkit — and 20 More Stories](https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html)

**Dec 11, 2025**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcBEIOMDHFHbMxpqG8wwxxLRZJ4TavL-Z4AoU09ldjKg_8LpfxabE_BKPBfWUHK8GClxPJ2r3BRs078HZ8KwPrMHVHS1m5ZcCdPNR9mtUD5SZfz6WE3FLp6KnoT6HY2UhC-uV7CxqoFYiPyJw_4V0r0A5-vgSI0Znq74OKWlQxr6morZEwQUBaZd89AVg9/s790-rw-e365/threatsday.jpg)

This week's cyber stories show how fast the online world can turn risky. Hackers are sneaking malware into movie downloads, browser add-ons, and even software updates people trust. Tech giants and governments are racing to plug new holes while arguing over privacy and control. And researchers keep uncovering just how much of our digital life is still wide open.

The new Threatsday Bulletin brings it all together—big hacks, quiet exploits, bold arrests, and smart discoveries that explain where cyber threats are headed next.

It's your quick, plain-spoken look at the week's biggest security moves before they become tomorrow's headlines.

1. Maritime IoT under siege

   [Mirai-Based Broadside Botnet Exploits TBK DVR Flaw](https://cydome.io/cydome-identifies-broadside-a-new-mirai-botnet-variant-targeting-maritime-iot/)

   A new Mirai botnet variant dubbed Broadside has been exploiting a critical-severity vulnerability in TBK DVR ([CVE-2024-3721](https://nvd.nist.gov/vuln/detail/CVE-2024-3721)) in attacks targeting the maritime logistics sector. "Unlike previous Mirai variants, Broadside employs a custom C2 protocol, a unique 'Magic Header; signature, and an advanced 'Judge, Jury, and Executioner' module for exclusivity," Cydome [said](https://cydome.io/cydome-identifies-broadside-a-new-mirai-botnet-variant-targeting-maritime-iot/). "Technically, it diverges from standard Mirai by utilizing Netlink kernel sockets for stealthy, event-driven process monitoring (replacing noisy filesystem polling), and employing payload polymorphism to evade static defenses." Specifically, it tries to maintain exclusive control over the host by terminating other processes that match specific path patterns, fail internal checks, or have already been classified as hostile. Broadside extends beyond denial-of-service attacks, as it attempts to harvest system credential files (/etc/passwd and /etc/shadow) with an aim to establish a strategic foothold into compromised devices. Mirai is a formidable botnet that has spawned several variants since its source code was leaked in 2016.
2. LLM flaws persist indefinitely

   [NCSC Says Prompt Injections Might Never Go Away](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection)

   The U.K. National Cyber Security Centre [said](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection) prompt injections – which refer to flaws in generative artificial intelligence (GenAI) applications that allow them to parse malicious instructions to generate content that's otherwise not possible – "will never be properly mitigated" and that it's important to raise awareness about the class of vulnerability, as well as designing systems that "constrain the actions of the system, rather than just attempting to prevent malicious content reaching the LLM."
3. VaaS crackdown nets 193 arrests

   [Europol Arrests 193 in Connection with VaaS Crackdown](https://www.europol.europa.eu/media-press/newsroom/news/operational-taskforce-grimm-193-arrests-in-6-months-tackling-violence-service-networks)

   Europol's Operational Taskforce (OTF) GRIMM has arrested 193 individuals and disrupted criminal networks that have fueled the growth of violence-as-a-service (VaaS). The task force was launched in April 2025 to combat the threat, which involves recruiting young, inexperienced perpetrators to commit violent acts. "These individuals are groomed or coerced into committing a range of violent crimes, from acts of intimidation and torture to murder," Europol [said](https://www.europol.europa.eu/media-press/newsroom/news/operational-taskforce-grimm-193-arrests-in-6-months-tackling-violence-service-networks). Many of the criminals involved in the schemes are alleged to be members of The Com, a loosely-knit collective comprising primarily English speakers who are involved in cyber attacks, SIM swaps, extortion, and physical violence.
4. Hack tools seized in Poland

   [Poland Arrests 3 Ukrainians for Alleged Attempt to Sabotage IT Systems](https://srodmiescie.policja.gov.pl/rs/aktualnosci/145521%2CPodrozowali-po-Europie-z-detektorem-urzadzen-szpiegowskich-i-sprzetem-hakerskim.html)

   Polish law enforcement arrested three Ukrainian nationals for allegedly attempting to damage IT systems in the country using specialized hacking equipment after their vehicle was stopped and inspected. They have been charged with fraud, computer fraud, and acquiring computer equipment and software adapted to commit crimes, including damage to computer data of particular importance to the country's defense. "Officers thoroughly searched the vehicle's interior. They found suspicious items that could even be used to interfere with the country's strategic IT systems, breaking into IT and telecommunications networks," authorities [said](https://srodmiescie.policja.gov.pl/rs/aktualnosci/145521%2CPodrozowali-po-Europie-z-detektorem-urzadzen-szpiegowskich-i-sprzetem-hakerskim.html). "During the investigation, officers seized a spy device detector, advanced Flipper hacking equipment, antennas, laptops, a large number of SIM cards, routers, portable hard drives, and cameras." The three men, of ages between 39 and 43, claimed to be computer scientists and "were visibly nervous," but did not give reasons as to why they were carrying such tools in the first place, and pretended not to understand what was being said to them, officials said.
5. Teen data thief caught

   [Spain Nabs Teen Hacker for Allegedly Stealing 64M Records](https://www.policia.es/_...