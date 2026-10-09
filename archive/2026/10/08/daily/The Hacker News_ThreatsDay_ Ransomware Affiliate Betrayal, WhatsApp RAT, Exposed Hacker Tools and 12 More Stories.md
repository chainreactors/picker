---
title: ThreatsDay: Ransomware Affiliate Betrayal, WhatsApp RAT, Exposed Hacker Tools and 12 More Stories
url: https://thehackernews.com/2026/10/threatsday-ransomware-affiliate.html
source: The Hacker News
date: 2026-10-08
fetch_date: 2026-10-09T08:12:11.821816
---

# ThreatsDay: Ransomware Affiliate Betrayal, WhatsApp RAT, Exposed Hacker Tools and 12 More Stories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [ThreatsDay: Ransomware Affiliate Betrayal, WhatsApp RAT, Exposed Hacker Tools and 12 More Stories](https://thehackernews.com/2026/10/threatsday-ransomware-affiliate.html)

**Ravie Lakshmanan**Oct 08, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgR_DE5ORKWCpLgZgXBuH-MFmuqfxFNnkGQxremc0ffY4dopMHnx-2HvgZTMh48BvVr8k22lGaM__jTS83DuXnLpF4NC9u4bsQF-8_K34gZU0kJS_-10pUSL7WNxecJG0pCiHyNFiqxXEqWP7NqUK2-uvwzo8-ETqwZkPWdNOjhNn5S1Y0uFQX2HGBE5_5J/s1700-nu-rw-lo-l85-e365/t-day.jpg)

The crooks have trust problems of their own. One ransomware affiliate decided to keep the profits for himself. Elsewhere, an attacker left a server exposed, complete with tools and traces of an intrusion. Apparently, keeping things secure is a problem on both sides of the fence.

The rest of the week isn't much more reassuring. Malicious code turned up in developer packages and extensions that looked harmless. Familiar online services helped phishing emails appear legitimate. A basic file upload flaw gave attackers a way in, while weak session cookies made impersonation far too easy. Even AI assistants are getting their own instructions hidden inside phishing messages now.

What's interesting is the gap between effort and results. Some attacks involve several stages, careful timing, and plenty of tricks. Others get surprisingly far because of a bad design choice or something nobody bothered to check. Both seem to be working well enough. Anyway, here's what else turned up.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. Malicious VS Code themes exposed

   [GlassWorm-Linked VS Code Extensions Discovered](https://socket.dev/blog/glassworm-vscode-themes)

   Socket [said](https://socket.dev/blog/glassworm-vscode-themes) it discovered two suspicious VS Code themes still available on the Visual Studio Marketplace (Coca-Cola Christmas and Aurora Borealis Studio Theme) that claim to be color themes but share ties to Aurora Nocturne Night Theme, a previously removed malicious extension that concealed an obfuscated Windows downloader. Further analysis has uncovered six cluster-linked extension identities in Open VSX, including Open VSX versions of Coca-Cola Christmas, Aurora Borealis Studio Theme, and Cosmic Nebula Themes. An analysis of the Visual Studio Marketplace build of Cosmic Nebula Themes has revealed that it contains a loader that decrypts and executes embedded JavaScript, avoids Russian-language and Russian-timezone systems, and uses Solana transaction memos as a dead drop resolver to identify follow-on payload infrastructure. "That build contains the same Solana address, AES key, and execution model [previously documented](https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html) in [GlassWorm](https://thehackernews.com/2026/05/glassworm-malware-takedown-disrupts.html) activity," Socket researcher Kirill Boychenko said.
2. BraZetsu C2 infrastructure traced

   [Mapping BraZetsu Infrastructure via TLS Certificates](https://hunt.io/blog/brazetsu-access-broker-infrastructure)

   Last month, Group-IB published a detailed analysis of [BraZetsu](https://hunt.io/blog/brazetsu-access-broker-infrastructure), a Python-based Windows malware framework that's designed to gain access to Windows hosts via phishing attacks. It's also linked to Infected Marketplace, an underground market that inventories compromised Windows hosts and sells the access after a deposit of about $5.80, settled through NowPayments. Hunt.io, in a new analysis of the network indicators, [said](https://thehackernews.com/2026/09/brazetsu-malware-turns-compromised.html) "the command hostname reported on 31 August, c2.installscenter[.]com, was already serving TLS on a second VPS (80.78.27[.]252) on port 2083 from 4 April 2026, almost five months before the disclosure. The same IP also presents painel.installscenter[.]com on ports 8083 and 8443, so a control panel hostname and the C2 hostname sit on the same apex and the same host."
3. WhatsApp lure deploys Windows RAT

   [New VulcanRAT207.A Detailed](https://www.morphisec.com/blog/copy-of-how-to-stop-ransomware-before-execution/)

   A financial-document lure ("Statement.exe"), reportedly delivered via WhatsApp, has been found to deliver a previously tracked WebSocket remote access trojan (RAT) tracked as VulcanRAT207. As part of a multi-stage Windows intrusion. "After unpacking, the loader screened the host, attempted elevation, and injected a downloader into the LocalSystem Task Scheduler process," Morphisec [said](https://www.morphisec.com/blog/copy-of-how-to-stop-ransomware-before-execution/). "The chain retrieved a deployment bundle, used a signed GoFly driver ["GoFly64.sys"] to terminate selected Baidu security processes [using the [BYOVD](https://thehackernews.com/2026/02/reynolds-ransomware-embeds-byovd-driver.html) technique], established a Vulkan DLL side-loading task, and launched a WebSocket remote access trojan (RAT). The loader screens the host, attempts elevation, and uses [PoolParty Variant 7](https://thehackernews.com/2023/12/new-poolparty-process-injection.html) to place a downloader in the Windows Task Scheduler process without relying on CreateRemoteThread." The malware can collect system metadata, enable interactive shell access, terminate security processes, implement process injection techniques, replace clipboard text, enumerate local accounts, and terminate itself.
4. Qilin suspect extradited

   [Alleged Qilin Ransomware Group Member Extradited to Germany](https://cypro.co.uk/insights/cyber-bulletins/qilin-ransomware-extradition-to-germany/)

   An alleged member of the Qilin ransomware group has been [arrested](https://cypro.co.uk/insights/cyber-bulletins/qilin-ransomware-extradition-to-germany/) in Japan and extradited to Germany. The suspect, a 28-year-old Russian national, was detained in Osak...