---
title: Crafting the Perfect Prompt: Getting the Most Out of ChatGPT and Other LLMs
url: https://www.blackhillsinfosec.com/crafting-the-perfect-prompt/
source: Black Hills Information Security
date: 2024-08-30
fetch_date: 2025-10-06T18:05:14.137992
---

# Crafting the Perfect Prompt: Getting the Most Out of ChatGPT and Other LLMs

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

29
Aug
2024

[Bronwen Aker](https://www.blackhillsinfosec.com/category/author/bronwen-aker/), [Fun & Games](https://www.blackhillsinfosec.com/category/fun-games/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[AI](https://www.blackhillsinfosec.com/tag/ai/), [Chatbots](https://www.blackhillsinfosec.com/tag/chatbots/), [ChatGPT](https://www.blackhillsinfosec.com/tag/chatgpt/), [LLM](https://www.blackhillsinfosec.com/tag/llm/)

# [Crafting the Perfect Prompt: Getting the Most Out of ChatGPT and Other LLMs](https://www.blackhillsinfosec.com/crafting-the-perfect-prompt/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/BAker-150x150.png)

| [Bronwen Aker](https://www.blackhillsinfosec.com/team/bronwen-aker/) //

*Sr. Technical Editor, M.S. Cybersecurity, GSEC, GCIH, GCFE*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/BLOG_chalkboard_00685.jpg)

Go online these days and you will see tons of articles, posts, Tweets, TikToks, and videos about how AI and AI-driven tools will revolutionize your life and the world. While a lot of the hype isn’t realistic, it is true that LLMs (large language models) like ChatGPT, Copilot, and Claude can make boring and difficult tasks easier. The trick is in knowing how to talk to them.

LLMs like ChatGPT, Copilot, and Claude are text-based tools, so it should be no surprise that they are very good at analyzing, summarizing, and generating text that you can use for various projects. Like any other tool, however, knowing how to use them well is critical for getting the positive results you want. In a recent webcast (<https://www.youtube.com/watch?v=D1pIfpcEBtI>), I shared some tips and tricks for using LLMs more effectively, and I’m including them here again for your use.

First, some definitions:

* Artificial Intelligence (AI): “Artificial intelligence” refers to the discipline of computer science dedicated to making computer systems that can think like a human.
* Large Language Models (LLMs): A type of AI model that can process and generate natural language text
* Models: A “model” refers to a mathematical framework or algorithm trained on vast datasets to recognize patterns, understand language, and generate human-like text based on the input it receives. These models use neural networks to process and predict information, enabling them to perform tasks such as text completion, translation, and question-answering.
* Prompt: A prompt is the input text or query given to the model to elicit a response. It guides the model’s output by providing context, instructions, or questions for the model to process and generate relevant text.

So, to summarize: LLMs are a form of AI. We use prompts to give LLMs instructions or commands. They reply with responses and/or output that resembles text that would be generated by a human. The challenge, however, is that not all prompts are created equal.

I tend to classify prompts using the following categories:

* Simple Query: A lot like a search engine query, but will usually give you more relevant results. Good for “quick and dirty” questions or tasks.
* Detailed Instruction: Includes some specifics about the task to be performed and may include some direction regarding how to render or organize the resultant output.
* Contextual Prompt: A structured prompt that includes several layers of instruction and very specific directions on how to format and organize the output.
* Conversational Prompt: Less of a single prompt and more like a conversation with another person. Great for brainstorming and/or refining ideas in an iterative manner.

### **Simple Query**

This prompt is easy and is the format used by most people most of the time. All it involves is asking a simple question like, “What is the airspeed velocity of an unladen swallow?” or, “What is the ultimate answer to the ultimate question of Life, the Universe, and Everything?”

Usually, the response is more useful than what you might get from a search engine because it answers the question rather than giving you links to millions of web pages that might have the answer you are looking for.

### **Detailed Instruction**

This is a medium complexity prompt where you give the LLM more detail about what you want it to do. For example:

```
I need a Python script that will sort internet domains, first by TLD, then by domain, then by subdomains. The script needs to be able to deal with multiple subdomains. e.g., www.jpl.nasa.gov.
```

In this example, I’ve told the LLM that I want a Python script, a...