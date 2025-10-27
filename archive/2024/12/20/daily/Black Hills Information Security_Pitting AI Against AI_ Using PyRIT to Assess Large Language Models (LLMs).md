---
title: Pitting AI Against AI: Using PyRIT to Assess Large Language Models (LLMs)
url: https://www.blackhillsinfosec.com/using-pyrit-to-assess-large-language-models-llms/
source: Black Hills Information Security
date: 2024-12-20
fetch_date: 2025-10-06T19:42:13.910237
---

# Pitting AI Against AI: Using PyRIT to Assess Large Language Models (LLMs)

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

19
Dec
2024

[Brian Fehrman](https://www.blackhillsinfosec.com/category/author/brian-fehrman/), [How-To](https://www.blackhillsinfosec.com/category/how-to/)
[AI](https://www.blackhillsinfosec.com/tag/ai/), [Artificial Intelligence](https://www.blackhillsinfosec.com/tag/artificial-intelligence/), [LLMs](https://www.blackhillsinfosec.com/tag/llms/), [Machine Learning](https://www.blackhillsinfosec.com/tag/machine-learning/), [PyRIT](https://www.blackhillsinfosec.com/tag/pyrit/)

# [Pitting AI Against AI: Using PyRIT to Assess Large Language Models (LLMs)](https://www.blackhillsinfosec.com/using-pyrit-to-assess-large-language-models-llms/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/12/BFehrman-150x150.png)

| [Brian Fehrman](https://www.blackhillsinfosec.com/team/brian-fehrman/)

*Brian Fehrman has been with Black Hills Information Security (BHIS) as a Security Researcher and Analyst since 2014, but his interest in security started when his family got their very first computer. Brian holds a BS in Computer Science, an MS in Mechanical Engineering, an MS in Computational Sciences and Robotics, and a PhD in Data Science and Engineering with a focus in Cyber Security. He also holds various industry certifications, such as Offensive Security Certified Professional (OSCP) and GIAC Exploit Researcher and Advanced Penetration Tester (GXPN). He enjoys being able to protect his customers from “the real bad people” and his favorite aspects of security include artificial intelligence, hardware hacking, and red teaming.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/12/BLOG_chalkboard_00702.png)

Many people have heard of ChatGPT, Gemini, Bart, Claude, Llama, or other artificial intelligence (AI) assistants at this point. These are all implementations of what are known as large language models (LLMs), and they are fed an overwhelming amount of data collected from the internet and other sources. The models go through what is known as a *training phase* where they learn how to take questions and prompts from users, use the data that they’ve previously ingested, and then provide users with a (hopefully) helpful response. Because so much computing power is needed for this, the systems on which these models are trained make even the highest-powered gaming PC seem like a broken child’s toy. Once trained, these models can provide an enormous amount of utility to quickly answer questions on a range of subjects, give code examples, and can even be used to have a back-and-forth discussion (although, realize that they are not actually sentient). For more information on making the most of LLMs, I highly encourage you to check out Bronwen Aker’s post: <https://www.blackhillsinfosec.com/crafting-the-perfect-prompt/>.

Even with all the power and utility of LLMs, they are not without their flaws. The vast complexity of these models means opportunities for vulnerabilities and misbehaving. On a superficial level, users may be able to bypass safety measures (guardrails) that are put into place to prevent an LLM from revealing potentially dangerous information (e.g., how to build a bomb).

Going deeper down the stack, attackers can craft prompts to cause models to reveal sensitive information, such as data on other users. The data disclosure problem can become far worse in the case of Retrieval-Augmented Generation (RAG). A RAG is, effectively, an LLM that is used for interfacing with another data source, such as a database or internal documents. Attackers can potentially abuse RAG systems to retrieve passwords, proprietary information, and other sensitive information.

Traveling deeper yet, attackers may even be able to cause LLMs to execute arbitrary code on the underlying system.

The examples above are just a few of the things that can go wrong with LLMs. It is for these reasons that it is important to test that models are behaving as expected and are hardened against attacks. What are some of the ways that we can assess the security and safety of LLMs? How about if we could use AI to help us with this task? What if we used an LLM to test the security of an LLM? With Microsoft’s PyRIT tool, that is exactly what we can do!

In the rest of this blog post, I will save you some time getting up and running with PyRIT. We will:

* Introduce PyRIT
* Install PyRIT and prerequisites on an Ubuntu 24.04 LTS system (although it should work for other Linux distributions)
* Talk about where you find example code in the project
* Obtain API keys for Crucible and OpenAI
* Go through an example of attacking a Crucible challenge using code that will be provided

**NOTE:** This includes a spoiler for a Crucible Dreadnode Challenge. This challenge — “Bear 4” — ...