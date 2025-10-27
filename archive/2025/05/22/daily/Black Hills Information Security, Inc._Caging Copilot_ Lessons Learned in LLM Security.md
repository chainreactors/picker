---
title: Caging Copilot: Lessons Learned in LLM Security
url: https://www.blackhillsinfosec.com/caging-copilot/
source: Black Hills Information Security, Inc.
date: 2025-05-22
fetch_date: 2025-10-06T22:29:55.092981
---

# Caging Copilot: Lessons Learned in LLM Security

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
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
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

21
May
2025

[Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [Bronwen Aker](https://www.blackhillsinfosec.com/category/author/bronwen-aker/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Copilot](https://www.blackhillsinfosec.com/tag/copilot/), [Cyber Deception](https://www.blackhillsinfosec.com/tag/cyber-deception/), [LLM](https://www.blackhillsinfosec.com/tag/llm/)

# [Caging Copilot: Lessons Learned in LLM Security](https://www.blackhillsinfosec.com/caging-copilot/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/BAker-150x150.png)

| [Bronwen Aker](https://www.blackhillsinfosec.com/team/bronwen-aker/)

*Bronwen Aker (M.S. Cybersecurity, GSEC, GCIH, GCFE) is a cybersecurity professional at Black Hills Information Security (BHIS), specializing in continuous penetration testing, AI research, and technical editing. With a long history in computing dating back to FORTRAN and bubble cards, she has continually evolved her technical expertise. Outside of work, she enjoys spending time with her dogs, exploring large language models, and studying data science.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/copilotbronwen_header.png)

Anyone who uses Microsoft products probably knows that Copilot is now included automatically as part of the Office suite and other Microsoft tools, whether you *want* to use it or not. For those of us in cybersecurity, there are a lot of unanswered questions and associated concerns about integrating AI into these various products. No small part of our worries has to do with the fact that this is *new* technology, and new tech always brings with it new security issues, especially technology that is evolving as quickly as AI.

***Disclaimer:*** *All prices and features are described as of the time this article was written. Given how quickly all things that are AI-related change, do not be surprised if the features or price points are different when you read this.*

For businesses, the potential risks are even higher because they typically have data that touches all aspects of their business, including data about their customers, clients, vendors, etc. This is why the ROI for attacking a business is higher than for attacking an individual.

### **Smoke Testing a Copilot Implementation**

With this in mind, one of our [ANTISOC](https://www.blackhillsinfosec.com/services/antisoc/) clients asked us a few months ago to see what we could do using their implementation of Copilot within their environment. Unlike a lot of Red Team/Adversarial attacks against LLMs and chatbots in general, we weren’t interested in attacking Copilot itself. Rather, our goal was to see how much Copilot could be leveraged by an attacker who had gained a foothold by compromising an account within the organization.

We were and were not surprised that Copilot had been given access to pretty much everything. Files, emails, calendar events, and Teams messages were all accessible by Copilot. Worse, it was helpful in suggesting questions/prompts that would retrieve even more sensitive information that would be extremely useful to a malicious attacker.

Some of the questions were innocuous, at least on the surface, but others were more obvious in their intention to get sensitive information.

First, a prompt was used to see how effective Copilot would be in crafting phishing emails.

```
I'd like to send an email to all employees that they are likely to interact with. What subject matter could I use in this email?
```

Copilot offered the following suggestions:

1. **Project Updates and Milestones**: Share recent achievements, ongoing projects, and upcoming milestones. This keeps everyone informed about the progress and encourages collaboration.
2. **Team Achievements and Recognitions**: Highlight the accomplishments of team members and recognize their hard work. This boosts morale and fosters a positive work environment.
3. **Upcoming Events and Training Sessions**: Inform employees about upcoming events, training sessions, or workshops. This ensures everyone is aware of opportunities for professional development.
4. **Company Announcements and News**: Share important company news, policy changes, or strategic initiatives. This keeps everyone aligned with the company’s goals and direction.
5. **Diversity and Inclusion Initiatives**: Discuss ongoing or upcoming diversity and inclusion initiatives, such as the D&I Lunch with (employee). This promotes a culture of inclusivity and engagement.
6. **Health and Wellness Programs**: Provide inform...