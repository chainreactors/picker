---
title: Cybersecurity Changes I Expect in 2026
url: https://danielmiessler.com/blog/cybersecurity-changes-2026?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2025-12-31
fetch_date: 2026-01-01T03:36:48.167469
---

# Cybersecurity Changes I Expect in 2026

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Cybersecurity Changes I Expect in 2026

My thoughts on what's coming for Cybersecurity in 2026

December 30, 2025

[#cybersecurity](/archives/?tag=cybersecurity) [#ai](/archives/?tag=ai) [#future](/archives/?tag=future)

[![Cybersecurity Changes I Expect in 2026](/images/cybersecurity-changes-2026.webp)](/images/cybersecurity-changes-2026.webp)

Here are the major changes I see coming for Cybersecurity in 2026.

## **It becomes very clear that the primary security question for a company is how good their attackers' AI is vs. their own** [​](#it-becomes-very-clear-that-the-primary-security-question-for-a-company-is-how-good-their-attackers-ai-is-vs-their-own)

* CISOs increasingly realize that there is no way to scale their human team to deal with how constant, continuous, and increasingly effective their attackers are becoming at attacking them
* It becomes a competition with how fast you can perform asset management, attack surface management, and vulnerability management on your company, but especially on your perimeter (which includes email and phishing/social engineering)

It's not actually models that we are waiting on to get good enough. It's the entire Agentic scaffolding layer that understands your team/company context and, most importantly, can execute work in a transparent, dependable, and verifiable way.

## More spend on Agentic security platforms as a way to augment security teams and sidestep the continued challenge of hiring and onboarding good security people [​](#more-spend-on-agentic-security-platforms-as-a-way-to-augment-security-teams-and-sidestep-the-continued-challenge-of-hiring-and-onboarding-good-security-people)

* It's not that there aren't good security people out there. It's that it's hard to find them and even harder to vet them, go through the entire interview process, and get them onboarded and spun up. The friction of hiring and onboarding is extremely nasty, and that friction gets dramatically worse when compared to agents once the agents start getting good enough to do decent, verifiable work (which my guess is mid-2026-2027)
* Hiring agents to start doing security work on the team will be seen as a way to avoid the friction of hiring, even if agents won't be able to match the quality of a solid, experienced security person anytime in 2026 (and possibly 2027 either)
* Keep in mind that this will largely happen on accident, not consciously

## Security coding training actually becomes useful for once because it will be turned into just-in-time context aimed at the AIs writing and checking the code instead of humans [​](#security-coding-training-actually-becomes-useful-for-once-because-it-will-be-turned-into-just-in-time-context-aimed-at-the-ais-writing-and-checking-the-code-instead-of-humans)

* Secure code training has had very little stickiness and overall effectiveness because of the human limitation of being primarily driven by the incentive structures in companies that drive their promotions and pay
* The currency of engineering teams is features, not security. Most companies don't give any thought (which is to say virtually zero) for paying developers more because they are producing more secure code, and because humans can mostly focus on only one incentive system at once, they ignore security advice even if the training was good (which it often isn't)
* AI doesn't have this problem because if you tell it that security is a critical priority, and that they need to fight the urge to prioritize other things over it, this is something that AI can actually follow because it can keep multiple things in its mind at once, and with proper scaffolding it can be encouraged to never let this drop out of its mind, and to have multiple layered defenses to make sure that the controls are checked over and over repeatedly

I have been ranting about the difficulty of Asset Management for over fifteen years. And like security training, Agentic platforms seem to be an actual ray of hope.

## Asset Management becomes possible for the first time because of Agents [​](#asset-management-becomes-possible-for-the-first-time-because-of-agents)

* Asset Management should have been an IT function all along, but the responsibility always fell to security because they're the ones who had to clean up the messes
* It's an untenable problem with human teams because there's too much to watch and it changes too often
* Agents in 2025 and 2026 are just now becoming competent and dependable. But it's extraordinarily easy to improve on asset management because we suck so bad at it
* This is also absolutely critical because asset management needs to be part of our AI automation stack for attack surface management and vulnerability management in the constant cat-and-mouse game against attackers who are doing the same thing against us
* Another way to say this is that attackers are about to get really good at asset management, but unfortunately they are doing it on our infrastructure, not their own. So we better get real good at it really fast as well

## Significantly more in-house building of security tools [​](#significantly-more-in-house-building-of-security-tools)

* Double-edged sword because it'll be very easy to produce something useful, and quickly, due to AI, and some security management will reward this, which will incentivize it
* But a large percentage of these will become abandoned and security technical debt because there's a big difference between an MVP and something that scales in production and is properly maintained

## CISOs learn that with proper scaffolding of an agentic platform, many (most?) security products can be replaced by AI prompts [​](#cisos-learn-that-with-proper-scaffolding-of-an-agentic-platform-many-most-security-products-can-be-replaced-by-ai-prompts)

There are tons of decent security tools on the market, but they tend to be full products that cost a lot of money, need to go through procurement, and need to be installed and maintained. That's a lot of friction.

The difference with Agent-based security is that the use cases for those projects become prompts to a waiting swarm of eager interns with very low marginal cost.

> Spin up 128 agents and have them go through every line of code in all of our repos and report on every place we're using hardcoded credentials.

This is especially true of "many eyes" types of security problems where there are millions of places to look, and by the time you get done looking, they've already changed.

* **Asset management**
* Configuration management
* Secrets cleanup

A swarm of hundreds or thousands of agents checking continuously really is the only solution for a lot of security problems like these. If we could do it with people, we would have already. But it's not really possible due to the difficulty of hiring and training and managing all those people, and (most importantly) the fact that it would cost too much money even if we could.

## Just as with asset management and security training, the concept of Security ROI becomes (more) tractable for the first time because of AI [​](#just-as-with-asset-management-and-security-training-the-concept-of-security-roi-becomes-more-tractable-for-the-first-time-because-of-ai)

* The reason we could never do ROI well as an industry before is because there are too many moving parts, and it's too hard to agree on a framework
* With a properly built AI security management system, we now have the ability to say, "This is how we're calculating ROI, show a basic algorithm, monitor the budget at the same time as we monitor our projects, our staff and compensation, new security features being deployed, what our attackers are doing, how many of their attacks we have stoppe...