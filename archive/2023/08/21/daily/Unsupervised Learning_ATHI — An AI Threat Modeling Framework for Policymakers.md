---
title: ATHI — An AI Threat Modeling Framework for Policymakers
url: https://danielmiessler.com/p/athi-an-ai-threat-modeling-framework-for-policymakers
source: Unsupervised Learning
date: 2023-08-21
fetch_date: 2025-10-04T12:01:13.370250
---

# ATHI — An AI Threat Modeling Framework for Policymakers

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# ATHI — An AI Threat Modeling Framework for Policymakers

A framework for thinking about harms and impacts that can come from AI systems

August 20, 2023

[#ai](/archives/?tag=ai) [#business](/archives/?tag=business) [#cybersecurity](/archives/?tag=cybersecurity) [#ethics](/archives/?tag=ethics) [#innovation](/archives/?tag=innovation) [#politics](/archives/?tag=politics) [#society](/archives/?tag=society) [#technology](/archives/?tag=technology) [#recommended](/archives/?tag=recommended) [#top](/archives/?tag=top)

![](/images/2f5f9188-f433-4982-abff-4b0e7db391f7-ATHI-miessler-2023.png)

My whole career has been in Information Security, and I began thinking a lot about AI in 2015. Since then I’ve done multiple deep dives on ML/Deep Learning, joined an AI team at Apple, and stayed extremely close to the field. Then late last year I left my main job to go full-time working for myself—largely with AI.

Most recently, my friend Jason Haddix and I joined the board of the [AI Village](https://aivillage.org?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=athi-an-ai-threat-modeling-framework-for-policymakers) > at DEFCON to help think about how to illustrate and prevent dangers from the technology.

❝

It’s hard to properly address concerns that can’t be clearly articulated.

Many are quite worried about AI. Some are worried it’ll take all the jobs. Others worry it’ll turn us Into paperclips, or worse. And others can’t shake the idea of Schwarzenegger robots with machine guns.

This worry is not without consequences. When people get worried they talk. They complain. They become agitated. And if it’s bad enough, government gets involved. And that’s what’s happening.

People are disturbed enough that the US Congress is looking at ways to protect people from harm. This is all good. They should be doing that.

**The problem is that we seem to lack a clear framework for discussing the problems we’re facing. And without such a framework we face the risk of laws being passed that either 1) won’t address the issues, 2) will cause their own separate harms, or both.**

## An AI Threat Modeling framework

What I propose here is that we find a way to speak about these problems in a clear, conversational way.

Threat Modeling is a great way to do this. It’s a way of taking many different attacks, and possibilities, and possible negative outcomes, and turning them into clear language that people understand.

"In our e-commerce website, 'BuyItAll', a potential threat model could be a scenario where hackers exploit a weak session management system to hijack user sessions, gaining unauthorized access to sensitive customer information such as credit card details and personal addresses, which could lead to massive financial losses for customers, reputational damage for the company, and potential legal consequences."

  A typical Threat Model approach for technical vulnerabilities

This type of approach works because people *think* in stories—a concept captured well in [*The Storytelling Animal: How Stories Make Us Human*](https://www.amazon.com/Storytelling-Animal-Stories-Make-Human/dp/0544002342?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=athi-an-ai-threat-modeling-framework-for-policymakers) >, and many other works in psychology and sociology.

A 20-page academic paper might have tons of data and support for an idea. A table of facts and figures might perfectly spell out a connection between X and Y. But what seems to resonate best is a basic structure of: **This** person did **this**, which resulted in **this**, which caused **this**, that had this **effect**.

### ATHI Structure = Actor, Technique, Harm, Impact

And so that is precisely the structure I propose we use for talking about AI harm. In fact we can use this for many different types of threats, including cyber, terrorism, etc. Many such schemas exist already in their own niches.

❝

It’s useful to think about the impact you’re worried about and work backwards.

I think we need one for AI because it’s so new and strange that people aren’t calmly using such schemas to think about the problem. And many of the systems are quite intricate, terminology-heavy, and specific to one particular niche.

#### Basic structure

This ATHI approach is designed to be extremely simple and clear. We just train ourselves to articulate our concerns in a structure like this one.

![](/images/b5da4234-e3c8-49e7-97cb-eef0a681cb61-Screenshot_2023-08-20_at_15.12.25.png)

#### Filled-in structure

So for poisoning of data that is used to train models it would look something like this in sentence form:

![](/images/05d6027b-a85c-471f-b67d-f4cbf8800ce8-Screenshot_2023-08-20_at_15.18.19.png)

Or like this in the chart form.

![](/images/1bfd3f7d-a074-49bb-98e3-8381edff061d-ATHI_example_miessler.png)

Note that the categories you see here in each section are just initial examples. Many more can/should/will be added to make the system more accurate. We could even add another step between Technique and Harm, or between Harm and Impact.

The point is to think and communicate our concerns in this logical and structured way.

## Recommendation

What I recommend is that we start trying to have these AI Risk conversations in a more structured way. And that we use something like ATHI to do that. If there’s something better, let’s use that. Just as long as it has the following characteristics:

1. It’s **Simple**
2. It’s **Easy to** **Use**
3. Easy to **Adjust** as needed while still maintaining #1 and #2.

So when you hear someone say, "AI is really scary!", try to steer them towards this type of thinking. Who would do that? How would they do it? What would happen as a result? And what would the be the effects of that happening?

Then you can perhaps make a list of their concerns—starting with the impacts—and look at which are worst in terms of danger to people and society.

I think this could be extraordinarily useful for thinking clearly during the creation of policy and laws.

## Summary

1. AI threats are both new and considerable, so it’s hard to think about them clearly.
2. Threat Modeling has been used to do this for other security arenas for decades, and we should use something similar for AI.
3. We can use a similar approach for AI, using something simple like ATHI.
4. Hopefully the ability to have clear conversations about the problems will help us create better solutions.

### Collaboration

Here is [the Github Repo for ATHI](https://github.com/danielmiessler/athi?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=athi-an-ai-threat-modeling-framework-for-policymakers) >, where the community can add Actors, Techniques, Harms, and Impacts.

 > > > > > > >[![](/images/ATHI_example_miessler.png)](https://github.com/danielmiessler/athi?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=athi-an-ai-threat-modeling-framework-for-policymakers)

GitHub - danielmiessler/ATHI — An AI Threat Modeling Framework for Policymakers

ATHI — An AI Threat Modeling Framework for Policymakers, Lawmakers, and the Public to better understand and discuss AI Threats.

github.com/danielmiessler/athi

![](/images/ATHI_example_miessler.png)

#### NOTES

1. Thanks to Joseph Thacker, Alexander Romero, and Saul Varish for feedback on the system.

Share

[Post](https://ul.live/share/x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fathi-an-ai-threat-modeling-framework-for-policymakers&title=ATHI%20%E2%80%94%20An%20AI%20Threat%20Modeling%20Framework%20for%20Policymakers "Share on X")  [LinkedIn](https://ul.live/share/linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fathi-an-ai-threat-modeling-framework-for-policymakers&title=ATHI%20%E2%80%94%20An%20AI%20Threat%20Modeling%20Framework%20for%20Policymake...