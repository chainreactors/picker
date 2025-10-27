---
title: Augmenting Penetration Testing Methodology with Artificial Intelligence – Part 3: Arcanum Cyber Security Bot
url: https://www.blackhillsinfosec.com/penetration-testing-with-ai-part-3/
source: Black Hills Information Security, Inc.
date: 2025-06-26
fetch_date: 2025-10-06T22:53:49.030287
---

# Augmenting Penetration Testing Methodology with Artificial Intelligence – Part 3: Arcanum Cyber Security Bot

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

25
Jun
2025

[Craig Vincent](https://www.blackhillsinfosec.com/category/author/craig-vincent/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[AI](https://www.blackhillsinfosec.com/tag/ai/), [Arcanum Cyber Security Bot](https://www.blackhillsinfosec.com/tag/arcanum-cyber-security-bot/), [artifical intelligence](https://www.blackhillsinfosec.com/tag/artifical-intelligence/), [penetration testing](https://www.blackhillsinfosec.com/tag/penetration-testing/), [Pentesting](https://www.blackhillsinfosec.com/tag/pentesting/)

# [Augmenting Penetration Testing Methodology with Artificial Intelligence – Part 3: Arcanum Cyber Security Bot](https://www.blackhillsinfosec.com/penetration-testing-with-ai-part-3/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/CVincent-150x150.png)

| [Craig Vincent](https://www.blackhillsinfosec.com/team/craig-vincent/)

*Craig is a former software developer and red teamer. He has been pentesting at Black Hills Infosec since 2018.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/06/arcanum_header.png)

*Read more of this series here:*
*[**Part 1 – Burpference**](https://www.blackhillsinfosec.com/penetration-testing-with-ai-part-1/)*
[***Part 2 – Copilot***](https://www.blackhillsinfosec.com/penetration-testing-with-ai-part-2/)

In my journey to explore how I can use artificial intelligence to assist in penetration testing, I experimented with a security-focused chat bot created by [Jason Haddix](https://x.com/Jhaddix) called Arcanum Cyber Security Bot (available on <https://chatgpt.com/gpts>). Jason engineered this bot to leverage up-to-date technical information related to application security and penetration testing. One of the example prompts is to supply the chatbot with JavaScript source and have it analyze the code from a security perspective.

As with previous blogs in this series, I used OWASP’s intentionally vulnerable Juice Shop web application for this experimentation. Again, it is important to consider client confidentiality when performing penetration tests. So, take care not to send customer information to remote LLMs, and use local on-premises models instead for real penetration tests. At first, I tried to paste Juice Shop’s entire main.js file into the Arcanum chat bot’s prompt form. This resulted in a response indicating that the prompt was too large. I used [parallel-prettier](https://github.com/microsoft/parallel-prettier) to make the file more readable so I could break it up and submit it to the chatbot in chunks.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture1-2.png)

**Submitting Beginning of JavaScript File to Arcanum Cyber Security Bot**

The chatbot returned a list of API endpoints it discovered in the source code. It’s always a good idea to look for additional attack surface in JavaScript files, so it was really helpful for the chatbot to pull those out of the source code. It even attempted to provide some documentation for the API calls!

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture2-2.png)

**API Calls Identified in Source Code**

The chatbot continued with its security analysis of the file. Interestingly, it identified hacking tutorial content in the source code and deduced that the code was part of an intentionally vulnerable web application, even calling out the application I was using by name.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture3-2.png)

**Additional Chatbot Source Code Analysis**

The response continued with ideas for possible attack paths.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture4-2.png)

**Chatbot Suggested Attack Paths**

The chatbot response concluded with defensive recommendations and an overall summary of its findings. At this point, I’m already impressed. The speed at which the chatbot extracted API endpoints from the source code alone is a huge value in terms of time savings. But wait! There’s more! The bot asked if I wanted to provide proof-of-concept exploits for the potential vulnerabilities it identified. I told it “yes,” and it provided the PoCs.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture10-2.png)

**Chatbot Generated Proof of Concept Exploit**

Again, this is where I would likely depart the AI and begin trying to exploit these things, but the chatbot was offering me more, and I wanted to see what else it had.

The chatbot next walked me through how to use Intruder to perform attacks against the different reported vulnerab...