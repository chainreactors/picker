---
title: DevSecOps: Lessons from the ST:TNG Crew
url: https://shostack.org/blog/devsecops-lessons-from-st-tng-crew/
source: Shostack & Friends Blog
date: 2026-04-05
fetch_date: 2026-04-06T04:44:30.012195
---

# DevSecOps: Lessons from the ST:TNG Crew

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
  + [Our Partners](/partners/)
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
3. DevSecOps: Lessons from the ST:TNG Crew

Shostack + Friends Blog

# DevSecOps: Lessons from the ST:TNG Crew

Kymberlee Price, Shostack + Associates

On First Contact Day, we dive into the lessons that security engineers can learn from the crew.
![Security engineers on the deck of a Star Trek ship examining data on multiple screens.](/images/blog/img/2026/Gemini_Generated_Image_star-trek-crew-hoodies-1000w.png)

In the April 1 blog, we looked at how the *USS Enterprise*, a ship of exploration, diplomacy and science, is like your application portfolio, with its [need for layered defenses and threat modeling](/blog/devsecops-learn-from-star-trek/). Running that ship takes more than knowing the threat landscape. It takes knowing which crew member to deploy, and when.

## Picard and the Art of Stakeholder Diplomacy

Captain Jean-Luc Picard is one of the great fictional diplomats of all time. He quotes Shakespare. He drinks Earl Grey tea. He sits across from Romulans, Cardassians, and Q himself — and he talks. He builds trust. He understands that the best outcome is almost never achieved by force alone. [Darmok and Jalad at Tanagra](https://en.wikipedia.org/wiki/Darmok).

Security engineers need to be Picard.

Think about what Picard actually does when the *Enterprise* encounters a tense situation. He doesn't immediately arm photon torpedoes. He gathers context. He asks questions. He tries to understand the other party's motivations and constraints. And then he finds a path that, ideally, achieves the mission without unnecessary conflict.

Now think about the last time you engaged an application team on a secure design review. Did you lead with a list of everything they were doing wrong? Or did you start by understanding what they were trying to build, what pressure they were under, and what constraints shaped their current design choices?

Picard's diplomacy isn't weakness — it's strategic. He knows that the outcome he needs (a secure ship, a safe crew, a completed mission) is far more likely to be achieved through alignment than adversarialism. When you walk into a conversation with an application team as a partner rather than an auditor, you dramatically increase the probability that your security requirements will actually be implemented — not just checked off on a form and quietly ignored.

[Adam’s book](//threatsbook.com) teaches engineers to think about what could go wrong and what they can do about it. That's essential. But in DevSecOps, you also need to think like a diplomat. You need to understand the political landscape of your organization: who owns what, who's accountable for what timeline, where the budget pressure lives, and what the team actually cares about. Picard always did his homework before first contact. So should you.

## Worf: Knowing When to Lead With Risk

Lieutenant Commander Worf is the *Enterprise*'s Chief of Security and, later, Strategic Operations Officer. He is also, famously, always the first to recommend the most aggressive option.

> “Captain, I recommend we raise shields and arm weapons.”

Picard rarely takes this advice immediately — but he values it. Worf's job isn't just to fire the phasers. It's to make sure the captain always has a clear picture of the threat landscape, the defensive posture of the ship, and what offensive options are available if diplomacy fails.

In the DevSecOps context, Worf is your threat modeling posture. When you're working with an application team on a new feature or system design, there are moments when you need to be Worf. You need to put the threat model on the table and say, clearly and directly:

> “Here is the attack surface. Here is what an adversary can do. Here is the blast radius if this goes wrong.”

This isn't fear-mongering. This is giving the team (and leadership!) the information they need to make informed decisions. Worf never hides the danger to spare people's feelings. He gives an honest assessment so the captain can act with full situational awareness.

The key lesson from Worf isn't aggression, it's that security risk communication has to be clear, direct, and delivered at the right moment. When a team is designing a new authentication flow, that's when you deploy Worf. You bring the threat model. You walk through the STRIDE analysis. You show what broken authentication looks like in production, with real CVEs and real breach costs.

But — and this is critical — you do it *before* the code is written, not after. Worf doesn't raise shields after the Klingon Bird-of-Prey has already decloaked and fired. **Shifting left in DevSecOps means getting Worf into the conversation during architecture review, not during the penetration test.**

## Deanna Troi: Reading the Room, Building the Relationship

Counselor Deanna Troi is, to put it bluntly, the most underappreciated member of the *Enterprise* senior staff — and almost certainly the character whose function security engineers most need to internalize.

Troi is an empath. Her job is to understand what people are *actually* feeling versus what they're saying. She reads the subtext. She notices when someone is afraid, when someone is hiding something, when the stated position and the actual position are not the same.

Security engineers deal in subtext constantly.

When a developer says “we can add that security control in the next sprint,” what they sometimes mean is “I don't understand why this matters and I'm hoping you'll forget.” When a product manager says “we've assessed the risk,” what they sometimes mean is “we've decided to accept the risk without fully understanding it because we have a launch date.”

Deploying Troi means developing the soft-skills and interpersonal awareness to read these situations accurately. It means noticing when a team isn't pushing back on your recommendations because they agree with you — or because they've tuned you out. It means recognizing when resistance to a security control comes from a genuine technical constraint versus an organizational incentive problem that needs to be escalated differently.

Troi also plays a critical role in *de-escalation*. There are moments when Worf has the right tactical read but the wrong interpersonal approach. Picard frequently turns to Troi when a conversation needs to be navigated with care — when the other party is defensive, when trust has been damaged, when force (or the security equivalent: mandate and audit) will produce compliance without understanding.

If Worf is how you communicate risk, Troi is how you build the relationship that makes people want to act on it.

## Data: Consistency, Repeatability, and the Security Standard

No discussion of *TNG* and engineering would be complete without Commander Data.

Data is the *Enterprise*'s second officer and chief operations officer, and he is, above all else, consistent. He doesn't have bad days. He doesn't get tired and skip a step. He applies the same logic, the same thoroughness, the same process every single time.

In DevSecOps, Data represents your security standards, your automated controls, and your repeatable processes. Static analysis in the CI/CD pipeline? That's Data...