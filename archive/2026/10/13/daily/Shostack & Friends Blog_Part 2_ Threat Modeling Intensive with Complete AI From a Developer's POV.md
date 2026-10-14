---
title: Part 2: Threat Modeling Intensive with Complete AI From a Developer's POV
url: https://shostack.org/blog/threat-modeling-intensive-from-a-dev-pov-pt2/
source: Shostack & Friends Blog
date: 2026-10-13
fetch_date: 2026-10-14T06:52:14.892667
---

# Part 2: Threat Modeling Intensive with Complete AI From a Developer's POV

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about)
  + [Shostack + Associates](/about)
  + [Adam Shostack](/about/adam)
  + [Our Partners](/partners)
* [Services](/training)
  + [Training](/training)
  + [Accelerator](/secure-design-accelerator)
  + [Speaking Requests](/speaking)
  + [Consulting](/consulting)
* [Resources](/resources)
  + [Overview](/resources)
  + [Threat Modeling](/resources/threat-modeling)
  + [Books](/books)
  + [Games](/tm-games)
  + [Cyber Public Health](/resources/cyber-public-health)
  + [Lessons Learned](/resources/lessons)
  + [Videos](/resources/videos)
  + [Whitepapers](/resources/whitepapers)
* [Blog](/blog)
* [Contact](/contact)

1. [Shostack + Associates](/)
2. [Blog](/blog)
3. Part 2: Threat Modeling Intensive with Complete AI From a Developer's POV

Shostack + Friends Blog

# Part 2: Threat Modeling Intensive with Complete AI From a Developer's POV

Kris Yun, Software Engineer @ Shostack + Associates

Reflecting on AI in the Intensive
![A robot helpfully provides an overly verbose diagram on a scroll to a developer, who is noticing the flaming symbols that represent assumptions added by the AI model](/images/blog/img/2026/TM-developer-perspective-2-1000w.jpeg)

I promised a part 2 about my reflections of the Threat Modeling Intensive with Complete AI, and I'm here to deliver! Let's talk about AI. In the [first part of my reflections](https://shostack.org/blog/threat-modeling-from-a-software-pov/), I focused on the fundamentals of threat modeling: the Four Question Framework. With these four questions, I found myself repeatedly thinking, "Oh, this makes sense! Why haven't we been doing this from the start?" (especially in the context of AI-assisted software development).

Let's take the first question: "What are we working on?" This step is so obvious yet often forgotten. How can we build and secure services whose purpose we don't know? During the LLM portion of training, the importance multipled. In our discussions, one student noted the verbosity and low-level assumptions of LLM-generated data flow diagrams. The student prompted, "Generate a data flow diagram (DFD) based on these requirements," and pasted in our assignment. The output was too mammoth to follow, and even zooming out couldn't save us. Worse, the LLM-generated DFD added components, arrows, and trust boundaries where not specified.

As a result of this verbosity and the model's assumptions, we see how teams struggle with downstream complications. Initially, a verbose DFD seems better; after all, more the better... right? But in reality, is a verbose diagram always useful? Sometimes, yes. Analyzing a verbose LLM-generated DFD can serve security architects collaborating across teams. However, the class agreed that analysts may spend more time untangling an overly-complex DFD than performing meaningful work.

The instructors, Adam and Michael, stressed the impact of assumptions made by an LLM. An LLM is a mathematical model that predicts the next word by recognizing patterns. As a result, an LLM "assumes" by filling in missing gaps with statistical probability. However, we often forget these assumptions because of the LLM's confidence. When we read, "Component A talks to Component B" or "Passwords are stored here," we forget that these statements are unvalidated. And even if they are based on a conversation's context, what happens if these details are stale? The importance of doubting LLM-generated output multiplies in importance, especially when asking what we are doing. If practitioners use outdated (or incorrect) DFDs, they waste precious discussion time on a problem that doesn't actually exist.

But this is one example. What about the rest of the Four Question Framework? In the second question, we ask, "What can go wrong?" Prior to training, I assumed I knew the BARE minimum about LLMs (and therefore, AI threats). In the process, I unintentionally absolved myself from thinking about AI-specific threats. The realm of possibility just felt too foreign and vast! However, Michael Novack, an AI cybersecurity architect and Shostack + Associates trainer, helped me rethink my defeatist mindset. AI is not leaving our software processes anytime soon. This requires everyone--security analysts, software engineers, quality assurance engineers, managers, and more--to see data as an attack vector.

What does this mean? Let's remember how an LLM is trained across three phases: pre-training, fine-tuning, and post-training, [according to IBM](https://www.ibm.com/think/topics/llm-training). During pre-training, the model learns from massive text collections. Text are tokenized, or broken down, into fundamental units that are encoded into numerical representations for the model to understand. By the end of pre-training, the model broadly learns factual knowledge. Once achieving "base model" status, the LLM is fine-tuned for a specific use case with high-quality training datasets. Finally, the model undergoes post-training, where human feedback is taken into account. Across these three phases, we see how data (or datasets) are an implicit input. If an LLM is involved in the system design, data (whether in the form of a direct user query or a training set) can be exploited. As a result, Michael helped me see how data can then induce unintended or harmful model behavior.

So in the spirit of the Four Question Framework: What do we do about it? If you're a software developer who may be thinking, "AI threats aren't my problem... that's a security issue," I implore you to consider taking training that combines threat modeling with a focus on AI. As software developers, we are responsible for designing performant, scalable, and secure systems, and the Wild West of AI is not an excuse for ignoring evolving attack vectors. Even better: we highly encourage your TEAM to participate in a training. Software teams often create their own dictionary of workflow terminology, and I encourage the team of developers to build a common language when thinking about threat modeling AI systems.

I had a blast learning from Michael, Adam, and the students. If any of these ideas resonate with you, consider registering for the **Threat Modeling Intensive Using AI at OWASP Global AppSec USA from November 2 - 4, 2026**. This course will pair the fundamentals of the Threat Modeling Intensive with hands-on experience in using LLMs for threat modeling. [Register here](https://owaspglobalappsecusa2026.sched.com/event/2O5ER)!

Image by midjourney: "A watercolor painting of a friendly, simple robot at a table proudly presenting a very long scroll covered in boxes and arrows that unspools across the floor in loose curls. A bemused and mildly overwhelmed developer kneels beside it, tracing one small section of the scroll with a finger. A few of the shapes on the scroll glow bright orange. Deep indigo purple background, lime green and bright orange accents, red-orange highlights. Curious, good-humored mood, plenty of negative space."

Originally published by Kris Yun on 13 Oct 2026

Categories:
  [conferences](/blog/category/conferences)
  [training](/blog/category/training)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder)

[Other Star Wars blog posts](/blog/category/star-wars)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives)

[Doing science with near misses](/blog/doing-science-with-near-misses)

[Posts about “Threat Modeling 2nd Edition”](/blog/category/threat-modeling-2nd-edition)

[Posts about Adam’s “Threats” book](/blog/category/threats-book)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book)

[Posts about “The New School of Information Security” book](/blog/category/the...