---
title: Daily Blog #706: Using AI to help create better test evidence
url: https://www.hecfblog.com/2025/01/daily-blog-706-using-ai-to-help-create.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-03
fetch_date: 2025-10-06T20:14:33.642432
---

# Daily Blog #706: Using AI to help create better test evidence

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[evidence generation](https://www.hecfblog.com/search/label/evidence%20generation)

Daily Blog #706: Using AI to help create better test evidence

# Daily Blog #706: Using AI to help create better test evidence

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 02, 2025
•

[AI](https://www.hecfblog.com/search/label/AI?&max-results=8)
[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[evidence generation](https://www.hecfblog.com/search/label/evidence%20generation?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiEki65mAY7MgyH_QsQPQtLqDPmZrmBzdHtXfPD4kMb9-lO0vPoKZy6adMCM9pKqujt1LsNcMSQkKLa7bCirH9PBYaUz7IbnuuAmQe0L2iUSz1wYxFs2sOFt5kMlaNoFBKYmjYekphh1D1RaKLfpUezfKO9is704dhWjdoz0IAq5cKm8s5M3-zS1YiTj5Qi=w512-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEiEki65mAY7MgyH_QsQPQtLqDPmZrmBzdHtXfPD4kMb9-lO0vPoKZy6adMCM9pKqujt1LsNcMSQkKLa7bCirH9PBYaUz7IbnuuAmQe0L2iUSz1wYxFs2sOFt5kMlaNoFBKYmjYekphh1D1RaKLfpUezfKO9is704dhWjdoz0IAq5cKm8s5M3-zS1YiTj5Qi)

**Hello Reader,**

Two AI-related posts in a row might seem like a lot, but I’ve been incorporating AI into my research for the past couple of years, so it naturally comes up in my work. While I’m not quite ready to share what I’ve been doing recently with Cursor, an AI IDE, I do want to showcase how I’ve used AI to create better datasets for forensic testing.

Creating engaging datasets for others to learn from can be a challenge, particularly when it comes to adding interesting elements for people to discover. In the past, I relied on downloading random free ebooks or generating large files with random data. However, I wondered if AI could improve this process. So, I tried this prompt:

> “Create a PowerShell script that will generate a series of files with names related to AI technologies and themed around projects called ‘AI Tacos’ and ‘AI Burritos.’ The script should create 100 files with random data to vary their sizes. The files should use popular extensions and avoid numbers in the names. Instead, include at least 30 unique terms commonly used in research and development.”

The AI-generated script worked perfectly. When executed, it created 100 files in my specified directory, each with randomized content and varied file extensions. The result, as shown in the screenshot below, added depth and realism to my sample datasets.

![](data:image/png;base64...)

This kind of themed, random data is incredibly useful for making datasets feel more authentic. For example, I can create a new virtual hard drive (VHD), populate it with these files, and then focus on generating interactions that leave digital artifacts for forensic analysis.

If you’re looking to populate other types of content, AI can help there too. For instance, this prompt:

> “Write 5 text messages between two friends named David Cowen and Matthew Seyer discussing what kind of tacos to have for lunch.”

Produced the following conversation:

David Cowen: Hey Matt, I'm thinking tacos for lunch today. You up for it?
Matthew Seyer: Absolutely, dude! I could eat tacos every day. Any idea what kind?
David Cowen: I'm torn between fish tacos and something spicy, like chipotle chicken. What do you think?
Matthew Seyer: Fish tacos would be great, but I’m kind of craving some good old barbacoa. How about we do both?
David Cowen: Perfect idea! Let’s split an order of each so we can try everything. I’ll meet you in 20.

I even took it a step further and used AI to craft detailed fictional personas. For example, I used this prompt:

> “Create a background story for a fictional employee at a company called TacoCorp who has worked there for 10 years as an IT administrator. This person has been recruited by BurritoTown to steal secrets from TacoCorp. Provide motivations, names, and profiles for their boss, coworker, new boss at BurritoTown, and best friend who’s a local police officer. Include a CV, LinkedIn bio, and 10 social media posts detailing their life.”

The AI generated a detailed persona, including:

* **Name:** Oliver Delgado
* **Email:** [email protected]
* **Social Media Handle:** @OllieTacoTech

**Motivations for Betrayal:**
Oliver felt undervalued and underpaid after a decade at TacoCorp. Financial pressure and resentment toward his boss pushed him to accept BurritoTown’s lucrative offer to steal TacoCorp’s secrets.

**Supporting Characters:**

* Franklin Hoyt, a strict and demanding boss at TacoCorp.
* Samantha Mills, a friendly coworker unaware of Oliver’s frustrations.
* Grace Li, the ambitious new boss at BurritoTown.
* Daniel Morales, Oliver’s loyal best friend and a local detective.

The AI even provided Oliver’s CV, LinkedIn bio, social media posts, and a detailed headshot description for his persona.

This ability to quickly generate characters, scenarios, and realistic data allows me to focus on ensuring the technical accuracy of my work. AI tools are invaluable for filling in creative gaps and enhancing the realism of forensic datasets. Don’t underestimate how much they can help!

Also Read:  [AI Prompts that help me](https://www.hecfblog.com/2025/01/daily-blog-705-ai-prompts-that-help-me.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/01/daily-blog-707-surviving-breach-podcast.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/01/daily-blog-705-ai-prompts-that-help-me.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/2242396732782374724/comments/default)

## Top Posts/Right Now

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R76fsdeVWnJb-lPNFnJnif0HpOq-5yuADLWqHUQjQG4zpbLb46P0PM-dvHaM9rsb-D39qs/s72-c/sundayfunday.png)](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)

  [Daily Blog #814: Sunday Funday 4/20/25](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72JbkCoEID0IEVH-rls7Q1LRd_0awNugK97uT7EDxugHyuXvFM/s72-c/forgive.png)](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)

  [Daily Blog #815: I missed a day](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi60iLy5WiSNWWSyeIoM9JsOK9Xwv5L7GT5g4NxBmdQwyQNbbHzgWoiG4FbwefVVrqg1yDaz0ripRAlyXSWNX4xJ3tACOcH7a0_YyoPVT2XMPnI2-0aE3gKc9hJWhMWYqDWlTUDM2XM3DEHiJB5Z1iSrtjQeP0qG5xKxmt4RewUfbqA0FR7cw1DXPwxYNM/s72-c/solutionsaturday.png)](https://www.hecfblog.com/2025/04/daily-blog-813-solu...