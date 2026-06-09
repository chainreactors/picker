---
title: SCANT: A (kind-of-decent) Framework for Ethical Deepfake Creation & Distribution
url: https://secjuice.com/scant-framework-for-ethical-deepfake-creation-distribution-2/
source: Over Security
date: 2026-06-08
fetch_date: 2026-06-09T06:03:26.302580
---

# SCANT: A (kind-of-decent) Framework for Ethical Deepfake Creation & Distribution

[![Secjuice](https://secjuice.com/content/images/2018/12/Logo-1.png)](https://secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

# SCANT: A (kind-of-decent) Framework for Ethical Deepfake Creation & Distribution

* [![Ross Moore](/content/images/size/w100/2025/01/Moore-Headshot-2024-1195C.jpg)](/author/rossamoore/)

#### [Ross Moore](/author/rossamoore/)

Jan 20, 2026
• 12 min read

![SCANT: A (kind-of-decent) Framework for Ethical Deepfake Creation & Distribution](/content/images/size/w2000/2026/01/crossrhythmcoffee_imagine_Scaffolding_around_a_giant_robot_th_2a9df0df-8973-4ae5-a4ed-df0a480d9ac5_2.png)

**Workers on a scaffold building a robot, with the tech blueprint in the background**

**Contents**

1. The Ethical Blueprint: Building Trust in Synthetic Media
   1. S - Social Benefit
   2. C - Consent
   3. A - Accountability
   4. N - Non-Deception
   5. T - Transparency
2. Putting SCANT into Practice
3. TL;DR Checklist
4. It takes work!
5. AI - Embracing the Human
6. Speaking of ISO 42001

## **The Ethical Blueprint: Building Trust in Synthetic Media**

Lots of damage has been done with AI, and to keep from deep-sixing the forward-leaning tone I want in this article, I’ll refrain from noting any details – the internet is available for you to search to your heart’s content. I want to start with that note because how we use AI is not just an option, like whether we want a cinnamon roll or a bagel at breakfast. AI use has meaning – whether it’s dark or not depends on each of us.

On the lighter side of negative consequences, more and more media influencers are posting AI videos claiming that those videos aren’t AI, just to increase their views and to increase interaction – drawing out those who claim, rightly, that the media truly is AI, and then arguing back and forth about its validity. Some influencers are abusing AI to waste peoples’ time for the sole benefit of the influencer; and those actions a) further erode viewers’ trust in media platforms and b) turn them against the hope of the real usefulness of AI. (plus, it wastes their time, and that time is part of life, so it really grinds on the nerves to realize that one has spent some of their life’s breath only to be been taken for a fool). So, even on the lighter side, those consequences are eroding trust in all-things-online. But with running with the concept of “learn to discern,” one can beat that fraud. [Mitch Clark](https://www.instagram.com/mitchckofficial/?ref=secjuice.com) does an excellent job at educating on this.

For a recent cybersecurity presentation, I worked with the bots to create an ethical AI framework to fit GenAI in general. The bots gave me some decent ideas, and I prompted back and forth with them, and then moved it into my own short set that I then made into an acronym. Mnemonic devices to the rescue! This is also an example of human-in-the-loop in AI – the robot gives some information, and there’s back-and-forth between me and the machines, but in the end it’s human creativity and alignment of the information presented that wins the day.

Are there other frameworks? Sure! Well-researched ones, official governmental ones, professional community-developed ones. But I wanted to make one that’s maybe more accessible to the general public. Will it fail to gain traction? Certainly! But I have today, and maybe someone will read this and either learn something, or think “I can do better” and I will have accomplished a goal of forcing others to write better things because I wrote a so-so thing. (I do this at home – I throw out weird, and even bad ideas, and that forces the kids to create better ideas 😊 )

**SCANT** is a concise and actionable set of principles designed to keep AI-generated media safe, respectful, and trustworthy.

Why SCANT? ***Scant*** [means](https://www.merriam-webster.com/dictionary/scant?ref=secjuice.com) “falling short of what is normal, necessary, or desirable.” I decided to keep it because it’s an insufficient approach, but may be simple enough to either work as-is or urge others on to make their own. AI is still a nascent field, and a good improvement would be for those involved in the field to either adopt or form their own workable models for evaluating how AI is developed in their org, even if it’s nothing fancy.

Yes, of course there’s [ISO 42001](https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html?ref=secjuice.com) ! There are great things happening around the world. Those can be expensive and cumbersome, though just knowing the principles and proceeding accordingly is a great way to show others how you align your AI practices with the international standard. SCANT is simply a “pet project,” if you will, so I thought I’d bring it in the open.

*NOTE: The term “deepfake” is often used to describe unethical use of high-quality GenAI, but the term is actually used for any of those high quality results. Throughout this article, deepfake is used for the final product, not simply for the deceptive kind.*

## SCANT

**S - Social Benefit**

**The Goal?** Deploy deepfake technology only when it creates a positive impact for individuals, communities, or society at large.

| Why it matters | How to achieve it | Examples |
| --- | --- | --- |
| Avoids harm Unchecked manipulation can erode trust, fuel harassment, or amplify misinformation. | **Purpose‑first assessment**   * Before any generation, ask: "What problem am I solving?" * Even simpler, answer "Why?" * Benefit‑impact analysis * Weigh expected social gains (*education, accessibility, art*) against possible negative externalities (*misrepresentation, emotional distress*).   **Stakeholder consultation**   * Involve affected groups (e.g., subjects of the synthetic video, target audiences) early in the design phase. | • Using a deepfake to recreate a historic figure for a museum exhibit that teaches history. • Generating realistic sign‑language avatars for deaf learners. • Avoiding deepfakes that glorify violent extremist propaganda. |
| Promotes public good  Aligns technology with broader societal goals (digital literacy, cultural preservation). | **Tie to measurable outcomes**   * Define KPIs (e.g., number of students reached, reduction in accessibility barriers).   **Iterative review**   * Reevaluate benefit after deployment; discontinue if harms emerge. | • A deepfake‑based language‑learning app that improves pronunciation for non‑native speakers. |

**C - Consent**

**Goal:** Secure explicit and informed permission from every person whose likeness, voice, or mannerisms are used.
*(Are voice trademarks the path forward? See this article re: Matthew McConaughey trademarking his voice* [*https://analystip.com/matthew-mcconaughey-trademark-himself-to-stop-ai-clones/*](https://analystip.com/matthew-mcconaughey-trademark-himself-to-stop-ai-clones/?ref=secjuice.com) *)*

| Core elements | Practical steps | Case handling |
| --- | --- | --- |
| Informed  Explain what the synthetic media will depict, where it will appear, and how long it will remain online. | • Provide a plain‑language consent form that includes:  ◦ Description of the generated content  ◦ Intended distribution channels  ◦ Rights to withdraw consent later | • If a celebrity's image is required for a parody, obtain a signed release from the talent agency or the individual's legal representative |
| Freely given  No coercion, undue pressure, or hidden incentives. | • Allow the subject to...