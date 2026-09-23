---
title: My Favorite Findings From the AI Security Decisions Report
url: https://zeltser.com/ai-security-decisions-report
source: Lenny Zeltser
date: 2026-09-22
fetch_date: 2026-09-23T06:53:34.548574
---

# My Favorite Findings From the AI Security Decisions Report

[Skip to main content](#main-content)

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# My Favorite Findings From the AI Security Decisions Report

Over 300 security professionals told Sounil Yu and me how their organizations secure AI. We published what we learned as the AI Security Decisions Report, so you can compare your AI security decisions with your peers'. Several of the findings were surprising, and each one is worth checking against your own program.

![Seen from behind, a person holds orange chalk beside an empty cell in a grid drawn on a chalkboard.](/assets/ai-security-decisions-report.CyIfktOH_Z1Cflcu.webp)

[Sounil Yu](https://www.linkedin.com/in/sounil) and I asked security professionals how their organizations secure AI. Over 300 people completed the survey (thank you!). We published the findings as the [AI Security Decisions Report](https://reports.aidefensematrix.com/ai-security-decisions/2026-wave-1), the peer benchmark we promised when we [launched the survey](/ai-security-survey) in July.

Here are some of my favorite findings from the report, each with an action you can take for your own program.

## Existing security measures are the most common way to secure AI.

Given the many products that aim to defend AI, I was surprised to see that respondents most often secured AI using general-purpose security tools and processes they already have. Security features that AI and cloud providers build into their offerings came next, then controls built in-house, and AI-security-specific products last.

It makes sense to first turn to our existing capabilities for AI security. However, be sure to check whether the tools cover all the different types of AI assets that are relevant to your organization. The [AI Defense Matrix](https://aidefensematrix.com) offers a list of the AI asset types to consider.

As you review your AI assets and the existing measures, you’ll likely find gaps that will benefit from a dedicated security tool. The [AI Defense Matrix Catalog](https://catalog.aidefensematrix.com) offers a starting point for mapping such tools to the different types of AI assets you might need to protect. If you sell such a product, be ready to explain what it adds to what the buyer already has.

## The assets that make agents work are the least protected by dedicated controls.

AI agents use AI models to make decisions as they pursue their goals, choosing their steps and tools along the way. Three types of AI assets make this possible:

* An orchestration layer connects the model to tools and data.
* Runtime AI data (prompts, retrieved content, and memory flowing through the agent) is what the agent works from.
* An agent identity (credentials the agent acts with) grants it access to tools and data.

According to the survey, these AI assets—the ones that make AI agents possible—were the least likely to have dedicated security controls, meaning controls set up for that asset in particular. This is in line with the first finding. Many organizations eager to experiment with and deploy AI agents turned to their existing security tools, perhaps extending them to protect AI assets that resemble what they already protect, such as code, data, and infrastructure.

Yet, there’s reason to think that existing controls haven’t caught up with these three assets. When asked what worries them most, respondents most often named two of them: runtime AI data and agent identities. Under pressure to support the rollout of AI agents, defenders may still need to extend existing controls to these assets or add new ones.

As you work to secure AI agents in your organization, understand what aspects of their operation are similar to the traditional assets you’ve been defending even during the pre-AI era. Then, determine which aspects of AI agents require dedicated security controls; for these, check whether a tool you already run covers them before looking for a new one. Which controls an agent needs also depends on how much autonomy you grant it. The [Security Autonomy Matrix](/security-autonomy-matrix) can help you decide.

## Accountability for AI security decisions is unsettled.

Among the respondents, the CISO or central security leadership was primarily accountable for AI security decisions. Yet, this was the case at fewer than half of the organizations. One in eight respondents described accountability as shared across several leaders with no primary owner, and as many said their organization hadn’t established it yet.

Respondents whose organizations hadn’t yet established accountability more often reported no dedicated control for any AI asset. In this small group, respondents were about twice as likely to say so as those whose CISO was accountable. To me this indicates that many of these organizations haven’t yet made a deliberate decision about how to secure AI, and that the ones that have decided are the ones with controls in place.

If your organization hasn’t decided who should have the primary responsibility for deciding how to secure AI, start there. If you’re already set on a general direction of AI governance, review each cell in the AI Defense Matrix, each a defensive activity for one type of AI asset, pick the ones most relevant to your organization, then assign an owner to each. If distributing AI ownership, make sure that “it’s everyone’s responsibility” [doesn’t turn into it being no one’s responsibility](/distribute-cybersecurity-tasks).

## AI-generated code is the most widespread AI asset, and the one respondents worry about least.

AI-generated code was the AI asset respondents most often reported having. Fewer than half of those organizations have a dedicated control for it. When asked what worries them most, almost no one mentioned AI-generated code. This suggests that respondents are comfortable with their existing code security tooling securing AI-generated code, or that they haven’t given the question much thought.

It’s true that code is code, whether it was generated by AI or a human developer. Yet, in the vibe coding era, non-developer employees are using AI to generate code and are often doing this outside the usual pipeline where traditional code security tools have been deployed. Securing code developed by non-engineers [requires special considerations](/security-governance-vibe-coding).

When securing AI-generated code, find out how much of it comes from people outside engineering and where it runs. Consider what safeguards such code needs beyond your usual pipeline. For example, you may need to extend discovery to those apps and build dependency scanning and secret detection into the platforms employees already use to create them.

## Explore the report.

Read the [full report](https://reports.aidefensematrix.com/ai-security-decisions/2026-wave-1) for additional findings. For those who want to dig deeper, it makes available the numbers behind every finding, the charts, the survey questions, and the data as CSV files.

The report is designed with human and AI readers in mind. For example, to extract your own insights and apply them to your organization, simply give your AI agent the report’s URL and start asking questions. The site publishes the underlying data in formats an agent can read, so the agent can answer with your own context in mind.

Receive my blog posts by email.

Email address   Subscribe

### Related Articles

[![](/assets/security-autonomy-matrix.DYA60hX6_Z1HmNzo.webp) The Security Autonomy Matrix: Deciding AI Authority](/security-autonomy-matrix)  [![](/assets/ai-security-buying-questions.D4MeVkxw_Zfc3qV.webp) Five Questions to Answer Before Buying an AI Security Product](/ai-security-buying-questions)

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Facu...