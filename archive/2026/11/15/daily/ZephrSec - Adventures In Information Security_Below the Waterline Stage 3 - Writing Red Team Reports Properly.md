---
title: Below the Waterline Stage 3 - Writing Red Team Reports Properly
url: https://blog.zsec.uk/below-the-waterline-reporting/
source: ZephrSec - Adventures In Information Security
date: 2026-11-15
fetch_date: 2026-11-16T08:48:47.824806
---

# Below the Waterline Stage 3 - Writing Red Team Reports Properly

[Skip to content](#main)

[![ZephrSec - Adventures In Information Security](/content/images/size/w400/2025/05/YoutubeHeader-Recovered-1.png)](https://blog.zsec.uk)

* [About Andy Gill/ZephrFish](https://blog.zsec.uk/about/)
* [My Red Team Course](https://lms.zsec.red/courses/malwareless-adversarial-emulation)
* [ZephrSec](https://zephrsec.com)
* [My Books](https://leanpub.com/b/LearningTheRopes)
* [Photo Blog](https://photos.zsec.uk/)

[Buy me a coffee](https://blog.zsec.uk/support/)

Toggle colour scheme
[Buy me a coffee](https://blog.zsec.uk/support/)
[Subscribe](#/portal/signup)
Menu

[redteam](/tag/redteam/)

# Below the Waterline Stage 3 - Writing Red Team Reports Properly

How to write red team reports that get acted on: executive summaries, findings, severity ratings and turning technical work into business impact.

[Andy Gill](/author/andy/)
/
15 November 2026
/
10 min read
/

 views

![](/content/images/size/w30/2026/09/20221022_160704-1.jpg)
![Below the Waterline Stage 3 - Writing Red Team Reports Properly](/content/images/size/w1200/2026/09/20221022_160704-1.jpg)

Loch Lomond in on a Grey Autumnal Day

On this page

On this page

Welcome back to my Below the Waterline series. In this part I'm going to dive into reporting, and more specifically getting the right point across to the right audience, because finding something technically interesting is only half the job. You can find a brilliant attack path, prove it beyond any doubt, write it up, talk it through in a meeting and still change absolutely nothing if the report doesn't explain why it matters and what somebody should actually do about it. This is especially true in red teaming, where people tend to be technically strong but don't always have the knowledge to explain business impact.

Most red team courses and blog posts skip over reporting because it isn't seen as a technical skill, and to be honest, it's nowhere near as fun to demo as an exploit or a clever route to an objective.

In reality reporting is a lot closer to translation. You're pulling apart what happened during an engagement and explaining it to people who weren't sat next to the operator when it happened, and a fair few of those people control the remediation budget, sign off on business risk or decide what the security programme does next.

The report is the permanent record of the work. Once it's done the infrastructure gets torn down and everyone moves on to the next job, but people will still be reading the report, quoting it and arguing about it months or even years later. It has to make sense on its own without you in the room to explain what you meant, with enough context that a reader can follow what you did and why.

## What the Report Needs to Contain

At its core a report has three parts: the executive summary, the findings, and the operational narrative along with its appendices. They all describe the same engagement, but each one has a different job to do and serves a different audience, they shouldn't read as though somebody wrote one section and then copied it out three times at different lengths.

![](https://blog.zsec.uk/content/images/2026/11/image-9.png)

The executive summary is for people who don't have the technical detail (and often don't need to know the full technical ins and outs) often they may not have had anything to do with the engagement. It should cover why the exercise happened, when it happened, what was tested, what the red team achieved(and didn't achieve), what the organisation did well, where the real gaps are and what needs to happen next. An executive reader should be able to get through it without having to translate it in their head, but it still has to be specific enough that they can make a decision off the back of it. Where possible the Red Team Manager involved in the project should write it, or at the very least review it and own it. The whole engagement gets boiled down to a page or two in this section, so a sloppy sentence here does far more damage than one buried in a finding.

The findings carry the detail somebody needs to understand each weakness and fix it. For each one we want to know what was found and where, how it was demonstrated, what evidence backs it up, what it enabled the team do, how it affects the organisation, how it was rated and what should be done about it. Screenshots and command output are great when they prove the point, but pick the ones that do and label them properly. Dumping every screenshot from the engagement into a finding just makes it unreadable and equally repeating content from the narrative in the finding is no use either as it just makes the report untenably long when it often doesn't need to be.

The operational narrative is where the findings get tied together into the story of the engagement, and the appendices hold everything that would swamp the main report if you put it there. Depending on the job that could be the detailed timeline, ATT&CK mapping, scope and exclusions, methodology, detection results, the artefact register, the accelerator log (the record of any help the client gave the team to keep things moving, such as handing over credentials), evidence references and cleanup status. If a reader needs something to understand a finding, put it in the main report. Anything that ends up in an appendix because nobody knew where else to put it is something most readers will never see.

## Lead With the Adversary

In most cases a Red Team will be an Adversary Simulation (sometimes called an Adversary Emulation), therefore the order you put things in changes how the whole report gets read. If you lead with findings before you've set out who the adversary was, you lose the threat framing, and the reader is left judging each finding with no idea what the red team was trying to be.

Demonstrate early on which adversary you were playing and whether you were simulating or emulating them, and know the difference between the two, because people use them interchangeably and they shouldn't. Emulation means reproducing the known tradecraft of a specific, named threat actor as closely as you can. Simulation means behaving like a type of adversary, say a financially motivated ransomware crew, without following any one group's playbook step for step. Which one you did tells the reader how far they can generalise your results. Leave that out and you'll find remediation priorities getting challenged or quietly pushed down the list by people who never understood what was being tested in the first place.

## Documentation Throughout

A report gets built in stages, and each stage relies on the records kept in the one before it. Most of what decides whether a report is any good happens well before anyone opens the template.

![](https://blog.zsec.uk/content/images/2026/11/image-8.png)

A few basics will save you a lot of pain at reporting time:

* Agree on UTC before the engagement starts. When every operator logs in their own time zone, rebuilding the timeline afterwards is close to impossible.
* Log actions as you do them. Trying to remember at the end of the day what you ran at 10am never goes well.
* Keep an artefact register of every file dropped, account created and persistence mechanism installed. It doubles as your cleanup checklist at the end.

The wash-up and everything after it assume you've got these records. Without them you end up piecing the timeline back together from memory and chat history, and a finding you can't evidence is a hard one to defend when the client pushes back on it.

## The Wash-Up Meeting

Before anybody drafts a finding, the operator timeline needs lining up against the blue team's evidence so you know what the SOC saw(in a regulatory assessment at least, obviously some red team reports will vary and this isn't always the case), what they missed, what they spotted but never acted on and what they handled well.

Any disputed facts should get sorted out in the wash-up, before they get anywhere near the report. I...