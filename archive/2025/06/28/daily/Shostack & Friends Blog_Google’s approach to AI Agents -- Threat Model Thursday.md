---
title: Google’s approach to AI Agents -- Threat Model Thursday
url: https://shostack.org/blog/google-approach-to-ai-agents-threat-model-thursday/
source: Shostack & Friends Blog
date: 2025-06-28
fetch_date: 2025-10-06T22:55:55.456265
---

# Google’s approach to AI Agents -- Threat Model Thursday

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Google’s approach to AI Agents -- Threat Model Thursday

Shostack + Friends Blog

# Google’s approach to AI Agents -- Threat Model Thursday

What can we learn from Google’s approach to AI Agent Security
![A screencapture of the document title, An Introduction to Google’s Approach to AI Agent Security](/images/blog/img/2025/google-ai-sec@2x-1600w.png)

Last month, Google released [An Introduction to Google’s Approach to AI Agent Security](https://storage.googleapis.com/gweb-research2023-media/pubtools/1018686.pdf), a 17 page whitepaper by Santiago Díaz, Christoph Kern, and Kara Olive. As always with Threat Model Thursday, I want to look at this to see what we can learn and maybe offer up a little constructive criticism. And despite not being labeled a threat model, it has the main components of one, and it can be seen as a high level threat model that outlines dangers of agentic AI. It also serves as an interesting example of a “template,” where it outlines very generically the threats to an architecture like this, and allows someone building an agentic system to start from the template and provide more specific threats and mitigations. Lastly, it demonstrates some of the key values that Loren Kohnfelder and I are advocating in our call to [publish your threat models](https://docs.google.com/document/d/17bMzGYWbYxw_HFA1PyuYFLZXXhA4sVqQC2Daa6a1hUU/edit?usp=sharing)!1. The paper serves the needs of those who are considering using Google’s Agentic AI. As we discussed, publishing your threat model allows buyers to determine if something meets their security needs, and it lets them do that far better than most third party risk management programs. This threat model helps with:

![A slide image including the words ‘Analyze their security commitment + decisions. Do we need “compensating controls”? Can we skip extraneous controls because of provider choices?’](/images/blog/img/2025/publishing-serves-buyers@2x-400w.png)* Select the right providers
* Analyze their security commitment + decisions
* Do we need “compensating controls”?
* Can we skip extraneous controls because of provider choices?

Digging into how breaks a little from the ordering, but not the spirit, of the Four Question Framework.

The paper starts by layout out a tension for those building systems with agentic AI:

> Securing AI agents involves a challenging trade-off: enhancing an agent’s utility through greater autonomy and capability inherently increases the complexity of ensuring its safety and security. Traditional systems security approaches (such as restrictions on agent actions implemented through classical software) lack the contextual awareness needed for versatile agents and can overly restrict utility. Conversely, purely reasoning-based security (relying solely on the AI model’s judgment) is insufficient because current LLMs remain susceptible to manipulations like prompt injection and cannot yet offer sufficiently robust guarantees. Neither approach is sufficient in isolation to manage this delicate balance between utility and risk.”

This tradeoff ties to the questions of “what are we working on” and “what can go wrong” and explains the danger for those who are going to rely on it. Here, ignoring that model improves clarity of communication, but they return very crisply to both questions. For example, the very next paragraph says:

![A system model](/images/blog/img/2025/google-approach-to-ai-agents-system-model.png@2x-500w.png)
> The primary concerns demanding strategic focus are rogue actions (unintended, harmful, or policy-violating actions) and sensitive data disclosure (unauthorized revelation of private information).

The paper uses a set of clear diagrams to lay out the architecture of the system as they see it.

Lastly, it lays out three “Core principles for agent security:”

* Agents must have well-defined human controllers (incorporating both control and ‘identity’).
* Agent powers must have limitations.
* Agent actions and planning must be observable.

For illustrative purposes, I’ll give into the temptation to be snarky for a moment: “Agent powers must have limitations” Really? Thank you so much! But now that Google has said so, we can contrast with MCP, where no one seems to have said that. We can notice that MCP has all sorts of authentication and confused deputy problems, which are not quite built in, but the absence of strong authentication and authorization mean that developers will define those services themselves, and many of them will not do a good job.

What’s more, Google closes out with the sorts of additional controls they expect a developer to add, in a section on “Validating your agent security.” Frankly, I’d like this to be more clear about who has to do what, in the sense of a shared responsibility model. I think most of that paragraph is about things that Google’s customers need to do, and then at the end, there’s a phrase ‘external security researchers (engaged through programs like Google’s VRP...)’ which could be stated as “engaged through your bug bounties, programs like Google’s VRP.’

The one thing that I do want to call out is the confusing use of “alignment,” here defining it as “Ensuring alignment—that agent actions reasonably match **user intent**...” But alignment may also mean alignment with the intent of the people building the agentic AI, or the ones incorporating it into a product. For example, if Expedia uses Gemini to buy me a ticket, to whose interests are we “aligning?” I ask because elsewhere, [Google Deepmind defines alignment](https://deepmind.google/discover/blog/introducing-the-frontier-safety-framework/) as “act[ing] in accordance with human values and societal goals” while in a different forum [Google DeepMind defines mis-alignment](https://www.alignmentforum.org/posts/3ki4mt4BA6eTx56Tc/google-deepmind-an-approach-to-technical-agi-safety-and) as “The AI system knowingly causes harm against the intent of the developer.” So does “alignment” refer to the goals of the user, the developer or society?

But all up, this white paper is useful for anyone deploying agentic AI. It’s also helpful to those who are thinking about platforms and how to communicate so that their customers can deploy securely.

1. I haven’t discussed this post with Loren in advance, so this is my perspective on that work.

Originally published by Adam on 27 Jun 2025

Categories:
  [threat modeling](/blog/category/threat-modeling)
  [threat model thursday](/blog/category/threat-model-thursday)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/category/star-wars/)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives/)

[Doing science with near misses](/blog/doing-science-with-near-misses/)

[Posts about Adam’s “Threats” book](/blog/category/threats-book/)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book/)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school/)

...