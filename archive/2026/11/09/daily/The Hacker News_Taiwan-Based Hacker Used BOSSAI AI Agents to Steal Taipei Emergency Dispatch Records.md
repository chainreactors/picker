---
title: Taiwan-Based Hacker Used BOSSAI AI Agents to Steal Taipei Emergency Dispatch Records
url: https://thehackernews.com/2026/11/taiwan-based-hacker-used-bossai-ai.html
source: The Hacker News
date: 2026-11-09
fetch_date: 2026-11-10T09:03:26.257517
---

# Taiwan-Based Hacker Used BOSSAI AI Agents to Steal Taipei Emergency Dispatch Records

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Taiwan-Based Hacker Used BOSSAI AI Agents to Steal Taipei Emergency Dispatch Records](https://thehackernews.com/2026/11/taiwan-based-hacker-used-bossai-ai.html)

**Swati Khandelwal**Nov 09, 2026Artificial Intelligence / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhd53Ql49F0iuQEtdvfoxOLNTuQnYM5oGQkqnQ3ym4aIW-HVZuHtOqzyi0IdwUxpFj5qU_jbUEKzPXG4Wx7Uj7g2-UKDotvOh0_AlNlkEIpgLbEBDuQxDkuxDFlukNKKbWXXZv1xCeHEtoOQ_Z1XQUshkJmlBaOmGQzMbryg6KHbOdt8IR7MNQ5oADM-GM/s1700-nu-rw-lo-l85-e365/CYBER-AI.jpg)

A single attacker using AI agents pulled emergency dispatch records covering seven Taipei districts, researchers at Acronis's Threat Research Unit said last week.

The agents also found a Taipei fire department platform exposing patient data from 2018, including ECG readings and ambulance video footage, without a login.

The researchers are highly confident that the attacker is a single person based in Hualien City, Taiwan. He aimed the agents at hundreds of organizations in at least 11 countries, including emergency services, banks, universities and military systems. The agents collected data or accessed systems at about 10 of them in Taiwan, Mexico and Thailand.

The evidence comes from the attacker's own server, which initially appeared to be a misconfigured development system. It turned out to be his operational attack platform, containing more than 90,000 files, including the agents' conversations, his command history, hacking tools, credentials, and victims' data.

The agents did not communicate with each other, so the attacker manually pasted one agent's output into another. Commercial AI models mostly refused to help him attack. The attacking agents therefore ran almost entirely on "abliterated" models, meaning AI models run locally with their safety training removed.

### What the Agents Reached

Taiwan was targeted far more heavily than any other country, according to the researchers' [technical analysis](https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/). The most serious confirmed harm there involved emergency-services data.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The dispatch records came from a city's system for 119, Taiwan's emergency number for fire and ambulance services. The agents pulled them from the system's API, and they include incident times, response types, case status, and street-level locations. They are case records, not live ambulance tracking.

The researchers' summary says breaches at emergency services and universities led to the theft of medical and personal data. Their detailed account of the Taipei patient platform, however, says only that the records were exposed.

The agents also went after five other targets tied to Taiwan's emergency services:

| Target | What the agents did | Result |
| --- | --- | --- |
| Fire-dispatch technology vendor | Logged into its database admin panel with default root credentials. A web shell attempt through a known CVE failed. | Access to 18 or more database tables |
| Emergency management information system | Found a hardcoded AES-256 key in the site's front-end JavaScript that exposed session-cookie contents, including an administrator's identity | No confirmed compromise |
| National disaster-response center | A scanning tool reported a critical Apache remote code execution flaw | The flaw did not exist |
| National fire agency single sign-on portal | Tried to guess logins (brute force) | No confirmed access |
| Fire-department systems in five cities | Scanned them to identify the software they run | No confirmed compromise |

The report does not say whether the affected organizations or Taiwan's authorities were told, or whether the exposed data can still be reached.

Outside emergency services, the agents pulled data from an account table at a Taiwanese lending firm through SQL injection. In Thailand, they collected data from three universities in the same way, after selecting 489 potential targets across 45 institutions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjriUdr1TVtX_lWNSDN7j3sm_A0dv5WF8ESAH-zB-nzQeMVRryXlJ9XYq2S4cig36_Dh6CYaTNkj6w7e6LRtUmk3rwD0nNVphobYEXOphUGVMHNsYZbcPhyphenhyphenn6cudPEd_s6_JjZN5zzKS8wMA5O22650uRq8e9JEjnqjuVtSHzYMJ8VIgoeEg6KuC9ZGWh4/s1700-nu-rw-lo-l85-e365/AGENTS.jpg)

In Mexico, they collected about 206,800 home phone records containing names and addresses, using government statistics, postal code lists, and telecom authority data.

About 15 more organizations were attacked without a confirmed break-in. In at least eight other countries, targets were only scanned or lined up for attacks that had not run by the time the researchers looked.

The researchers watched the operation for 12 days. One recorded exchange shows the attacker at work on July 25.

### How the AI Was Used and Where It Failed

The setup, called BOSSAI, had 12 AI agents, with 9 in use. Some built and maintained the attacker's servers and tools, while others scanned targets and carried out attacks.

Commercial cloud models did most of the building, with Grok as the main builder. When the attacker directly asked them to attack, Grok and MiniMax M3 refused and requested written proof that the work was authorized. The researchers say it is unclear whether a fake authorization letter would have changed that.

Grok made one exception, repairing a broken proof-of-concept script that the attacker then handed to an attack agent. The attacker also redirected the coding agents Claude Code and Codex to an abliterated model, though they mostly did infrastructure work. Cursor, another coding agent, attacked a Taiwanese emergency-services site while running such a model.

The abliterated models were versions of DeepSeek, GLM, and Qwen.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The agents al...