---
title: Winning Against AI-Based Attacks Requires a Combined Defensive Approach
url: https://thehackernews.com/2026/01/winning-against-ai-based-attacks.html
source: The Hacker News
date: 2026-01-26
fetch_date: 2026-01-27T03:39:24.520435
---

# Winning Against AI-Based Attacks Requires a Combined Defensive Approach

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

# [Winning Against AI-Based Attacks Requires a Combined Defensive Approach](https://thehackernews.com/2026/01/winning-against-ai-based-attacks.html)

**The Hacker News**Jan 26, 2026Endpoint Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSTncIdUsnHK3Kps8gH8NtlxG7T5vp-JlCp6eWy56PFPvRgzGtsuG6PHp41yrm8pYLApQwGsTiFLBztGal_MQyIt_jKb0_GZFx3RlY6cg1AGzVMWlChqjOUVpL_woevpV3EHFOLHxuwsfbDfkpp__4SEO4Sj17-r6XOjiInQTrs3Y08LO3kVoC3zt2Zig/s1700-e365/edr-ndr.jpg)

If there's a constant in cybersecurity, it's that adversaries are always innovating. The rise of offensive AI is transforming attack strategies and making them harder to detect. [Google's Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools), recently reported on adversaries using Large Language Models (LLMs) to both conceal code and generate malicious scripts on the fly, letting malware shape-shift in real-time to evade conventional defenses. A deeper look at these novel attacks reveals both unprecedented sophistication and deception.

In November 2025, [Anthropic reported on](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf) what it described as the first known "AI-orchestrated cyber espionage campaign." This operation featured AI integrated throughout the stages of attack, from initial access to exfiltration, which was executed largely autonomously by the AI itself.

Another recent trend concerns [ClickFix-related attacks](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html) using steganography techniques (hiding malware within image files) that slipped past signature-based scans. Skillfully disguised as legitimate software update screens or CAPTCHAs, these attacks deceived users into deploying remote access trojans (RATs), info-stealers, and other malware payloads on their own devices.

Adversaries are also exploiting ways to trigger and then compromise anti-virus (AV) exclusion rules by using a combination of social engineering, attack-in-the-middle, and SIM swapping techniques. Based on research from [Microsoft's threat team from October 2025](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction), the threat actor they call Octo Tempest convinced its victims to disable various security products and automatically delete email notifications. These steps allowed their malware to spread across an enterprise network without tripping endpoint alerts. Actors are also easily deploying dynamic and adaptive [tools that specialize in detecting and disabling AV software on endpoints](https://thehackernews.com/2024/10/hackers-abuse-edrsilencer-tool-to.html).

All these techniques share a common thread: the ability to evade legacy defenses such as endpoint detection and response (EDR), exposing [the limitations of relying solely on EDR](https://corelight.com/blog/edr-evasion?utm_source=thehackernews&utm_medium=article-1&utm_campaign=awareness-wave-2). Their success illustrates where EDR, acting alone and without additional defensive measures, can be vulnerable. These are new attacks in every sense of the word, using AI automation and intelligence to subvert digital defenses. This moment signals a fundamental shift in the cyber threat landscape, and it's rapidly driving a change in defensive strategy.

## **NDR and EDR, working together**

[Network detection and response (NDR) and EDR both bring different protective benefits](https://corelight.com/blog/10-reasons-why-ndr-is-essential-alongside-edr?utm_source=thehackernews&utm_medium=article-1&utm_campaign=awareness-wave-2). EDR, by its nature, is focused on what is happening inside each specific endpoint, whereas NDR continuously monitors the network environment, detecting threats as they traverse the organization. It excels at picking up what EDR does not, identifying behavioral anomalies and deviations from typical network patterns.

In the age of AI-based threats, there is a need for both kinds of systems to work together, especially as these attacks can operate at higher speeds and greater scale. Some EDR systems weren't designed for the speed and scale of AI-fueled attacks. NDR can pick up these network anomalies and strengthen defenses and gain deeper insights from this network data, leveraging the additional protection this complementary technology can provide.

Compounding the challenge is that today's attack surface is expanding and growing more complex. Sophisticated threat actors now **combine threats that move across a variety of domains**, compromising identity, endpoint, cloud and on-premises infrastructure in a lethal mix. This means the corresponding security systems in each of these focus areas need to work together, sharing metadata and other signals, to find and stop these threats. The bad actors hide behind this complexity so as to maximize their reach, increase their blast radius, and provide cover while they use different hacking tools to assume various roles and focus on different intermediate targets.

[Blockade Spider](https://www.crowdstrike.com/en-us/blog/defeating-blockade-spider-how-crowdstrike-stops-cross-domain-attacks/), a group active since April 2024, uses these mixed domains for ransomware attacks. After gaining access through finding unmanaged systems, they move laterally across a network, searching for a file collection to encrypt to try to extract a ransom. The full breadth of their approach was discovered by using NDR to obtain visibility into the virtual systems and cloud properties, and then using EDR as soon as the attack moved across the network into managed endpoints.

One of the more infamous variants is what was used in the [Volt Typhoon attack](https://thehackernews.com/2024/08/chinese-volt-typhoon-exploits-versa.html) observed by Microsoft in 2023. It's attributed to Chinese state-sponsored actors using living off the land (LoTL) techniques that helped them avoid endpoint detection. Its targets were unmanaged network edge devices, such as SOHO routers and other Internet of Things (IoT) hardware. The actors were able to alter the originating packets to appear to be coming from a cable modem in Texas, rather than a direct link to...