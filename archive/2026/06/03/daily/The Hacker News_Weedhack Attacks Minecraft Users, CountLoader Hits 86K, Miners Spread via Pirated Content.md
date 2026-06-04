---
title: Weedhack Attacks Minecraft Users, CountLoader Hits 86K, Miners Spread via Pirated Content
url: https://thehackernews.com/2026/06/weedhack-attacks-minecraft-users.html
source: The Hacker News
date: 2026-06-03
fetch_date: 2026-06-04T06:32:18.799364
---

# Weedhack Attacks Minecraft Users, CountLoader Hits 86K, Miners Spread via Pirated Content

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Weedhack Attacks Minecraft Users, CountLoader Hits 86K, Miners Spread via Pirated Content](https://thehackernews.com/2026/06/weedhack-attacks-minecraft-users.html)

**Ravie Lakshmanan**Jun 03, 2026Cryptocurrency / SEO Poisoning

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBhPg_oWS3s5XgNMW4vuwq3Pwrnsw3l3FyzGwoYkQ7AwCuU6VXH6sOv03o04S4jw-7pkVzAsccuFCxzMX1tg8JbB8D9k5onrVg0-D7HBQduN4pAHq2FOH9a-tSeokVqGIyJS-hStrL7fs5I9u67yp2gRKjOYuTYF_xUrsJnIWL3GdTZ7bLiU6u1vObezoD/s1700-e365/hacker-pirate.jpg)

Cybersecurity researchers have flagged a new campaign targeting Minecraft players via YouTube to spread malware capable of gaining control of victims' systems.

The Minecraft-focused malware-as-a-service (MaaS) campaign has been codenamed **Weedhack** by McAfee Labs, stating the activity has been active since January 2026 and impersonates Minecraft clients and mods to infect users. In all, 3820 unique malicious JAR files and over 240 URLs responsible for distributing the malware have been identified.

"This campaign utilizes SEO poisoning and YouTube to generate traffic to these malicious URLs," security researcher Aayush Tyagi [said](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/weedhack-minecraft-malware-as-a-service-campaign-research/). "We also found two YouTube channels and multiple videos that demonstrate Minecraft Mods and Clients and redirect viewers to these URLs."

Central to the campaign is an enterprise-grade dashboard ("weedhack[.]to") that enables customers to view stolen credentials and system information, as well as remotely keep tabs on the compromised systems. Furthermore, it allows criminals to create custom payloads that can target Minecraft versions 1.21.0 to 1.21.11, not to mention inject the malware into legitimate Minecraft mods.

The starting point of the attack is a malicious JAR file ("DonutDupe.jar") downloaded from the malicious websites. The file then retrieves details of the command-and-control (C2) server domain using a known technique called [EtherHiding](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html), which employs the Ethereum blockchain as a dead drop resolver.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

In the next stage, the malware contacts the C2 server to fetch another Java-based JAR payload ("Elevator.jar") that collects system information, configures Microsoft Defender exclusions, and serves as a conduit for dropping two additional JAR payloads. The third JAR payload ("SecurityManager.jar") establishes persistence and acts as a stager for the final component ("Component.jar") that deploys the remote access features.

The threat actors behind the tooling leverage a Telegram channel to advertise their warez, broadcast updates, and provide customer support. The channel has more than 850 members. The tool, for its part, comes in two tiers -

* Free, which includes a comprehensive infostealer that can target Minecraft session IDs and four Minecraft launchers; capture screenshots; and harvest files, system information, cookies, and passwords from 36 different web browsers, data from 56 browser-based cryptocurrency wallets and 12 desktop wallet apps, and credentials for Discord, Steam, and Telegram.
* Premium, which starts at $4.99 per month (or $24.99 for a lifetime license) and offers additional remote access capabilities, such as webcam access, keylogging, reverse shell execution, screen sharing with keyboard and mouse access, and file uploads and downloads.

Attack chains revolve around SEO poisoning and YouTube videos containing descriptions that embed links to malicious Minecraft Clients to target unsuspecting users. The majority of Weedhack infections have been identified in the U.S., followed by Germany, India, the U.K., Italy, Vietnam, Canada, Norway, Sweden, Finland, and Spain.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOwo-ydexLj40xeol3IglcoxymCjOpQLqMfiN0HJIIJ1uDqfdrWAU8ovf5ymf-3G1dFIdETB7PPvDkhFeAesAX2Koa1KiNUsvWhun7-Zy5aQpqAvu9fPVGQpo4Zx-Bex_wy2Ag5g1e0-nEkH7jfn3gG-8TgXCoqAkt4Qn43nHrGLOKD6wKGUirFYma7_dw/s1700-e365/yb.png)

"One of the key features that makes Weedhack unique is that it is hosted on the clear net and provides access to sophisticated malware for free," Tyagi said. "This difference in cost and ease of access with detailed tutorials on how to use the malware significantly reduces the barrier to entry for prospective customers. Furthermore, its ability to steal Minecraft accounts attracts a younger audience. Both of these factors complement each other and make the campaign much more lethal."

McAfee Labs said it has also observed the malware acting as a trigger for cyberbullying, where the customers, who appear to be teenagers and young adults, are weaponizing its remote access capabilities to threaten, harass, and monitor their victims. They have found a way to record victims via their webcams and shared the videos on the Telegram channel as "trophies."

### CountLoader Delivers Crypto Clipper

The disclosure comes as the cybersecurity company shed light on a large-scale [CountLoader](https://thehackernews.com/2025/12/cracked-software-and-youtube-videos.html) campaign that's estimated to have compromised 86,000 unique machines. CountLoader is a JavaScript loader that's typically distributed via cracked software distribution sites. It's known to deploy various payloads like Cobalt Strike, AdaptixC2, PureHVNC RAT, Amatera Stealer, and PureMiner.

Of these compromises, approximately 9,000 infections are said to have resulted from the malware spreading via USB drives and removable media. McAfee Labs said the highest number of infections was observed in India, followed by Indonesia, the U.S., and several countries across Southeast Asia, adding it was able to successfully sinkhole the malware communication infrastructure by registering a fake C2 domain.

"The infection begins when an...