---
title: Lessons From A Chatbot Incident
url: https://www.blackhillsinfosec.com/lessons-from-a-chatbot-incident/
source: Black Hills Information Security, Inc.
date: 2026-03-25
fetch_date: 2026-03-26T04:30:47.197982
---

# Lessons From A Chatbot Incident

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin Team](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [Active SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

25
Mar
2026

[Informational](https://www.blackhillsinfosec.com/category/informational/), [Jeremiah Fowler](https://www.blackhillsinfosec.com/category/author/jeremiah-fowler/)

# [Lessons From A Chatbot Incident](https://www.blackhillsinfosec.com/lessons-from-a-chatbot-incident/)

written by Jeremiah Fowler || Cybersecurity Researcher

![Lessons from a chatbot incident](https://www.blackhillsinfosec.com/wp-content/uploads/2026/03/lessons-from-a-chatbot-incident.png)

## When AI Chatbots Become a Data Liability

The adoption of AI chatbots across industries has transformed customer service, scheduling, and operational workflows, but it has also introduced a new and often overlooked risk of exposing customer data. Recently, I discovered three publicly accessible databases containing approximately 3.7 million records belonging to Sears Home Services, the beloved retailer founded in 1892. These files consisted of chat transcripts, audio recordings, and text transcriptions of customer interactions which included Personally Identifiable Information (PII) such as names, addresses, emails, and phone numbers, along with details about products and services.

The databases have since been secured, but the incident highlights a critical issue for businesses that think AI chatbots are a silver bullet or a turnkey replacement for humans. AI bots are not just operational tools, they are effectively data collection systems that can become significant liabilities if improperly managed or data storage is misconfigured. In the following screenshot, we see an example of a customer address (redacted) being transcribed from a service call into the database which was unprotected and unencrypted.

![Chatbot log reveals customer address](https://www.blackhillsinfosec.com/wp-content/uploads/2026/03/chatbot-log-reveals-address-1024x198.png)

Chatbot log reveals customer address

AI-driven assistants can aggregate numerous data types into a single ecosystem. Datasets that contain detailed logs, metadata, and voice recordings can be used by attackers for identity reconstruction, targeted social engineering, or even biometric misuse. There is also a growing risk of biometric voice data being used to synthesize realistic voice clones for social engineering and other forms of fraud.

![Chatbot log reveals customer call file](https://www.blackhillsinfosec.com/wp-content/uploads/2026/03/chatbot-log-reveals-audio-file-1024x740.png)

Chatbot log reveals customer call file

In addition to exposing user or customer PII, chatbot systems can also reveal internal logic, prompts, and other proprietary details.

![Chatbot log reveals chatbot logic](https://www.blackhillsinfosec.com/wp-content/uploads/2026/03/chatbot-log-reveals-chatbot-logic.png)

Chatbot log reveals chatbot logic

## Incident Insights

My [report](https://www.expressvpn.com/blog/searshomeservices-data-exposed/) was covered by [WIRED](https://www.wired.com/story/sears-exposed-ai-chatbot-phone-calls-and-text-chats-to-anyone-on-the-web/) and multiple other media outlets, but I wanted to summarize the findings here for the BHIS community with a security minded perspective to prepare for the future of AI risks. An important takeaway from this discovery is that these files were not exposed by a sophisticated cyberattack but from a basic security failure. In this case, the databases were neither password protected nor encrypted, making them accessible to anyone with a web browser.

![Files exposed in chatbot log](https://www.blackhillsinfosec.com/wp-content/uploads/2026/03/files-exposed-in-chatbot-log-1024x337.png)

Files exposed in chatbot log

Human error is still a serious issue in the world of data protection and security. The chances of a data incident only increase when third-party vendors are involved in developing or managing AI systems. This is why data governance and oversight should be a core part of your business. Even if a contractor or vendor has a breach at the end of the day, this is still your data or the data of your customers.

By now, we all know (or should know) the risks of improper AI data management, such as not encrypting files that contain sensitive information. Far too often I see plaintext data exposed, but when I find files that are encrypted, I move on because the files are unreadable, and I don’t have a supercomputer (yet). It is a good idea to follow a zero-trust model where access is explicitly granted, continuously verified, and need-based. Data minimization and giving data a lifespan can also mitigate risks, since reducing the volume of stored data can reduce the potential impact of any breach.

Organizations must now consider and plan for emerging AI specifi...