---
title: California Just Built a Data Deletion Tool That Actually Works (And Data Brokers Are Sweating)
url: https://secjuice.com/california-drop/
source: Over Security
date: 2026-06-27
fetch_date: 2026-06-28T06:14:08.407089
---

# California Just Built a Data Deletion Tool That Actually Works (And Data Brokers Are Sweating)

[![Secjuice](https://secjuice.com/content/images/2018/12/Logo-1.png)](https://secjuice.com)

* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/osint/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write](https://secjuice.com/join-secjuice-writing-team/)

[Sign in](#/portal/signin)
[Donate](/donate/)

[INFOSEC](/tag/infosec/)

# California Just Built a Data Deletion Tool That Actually Works (And Data Brokers Are Sweating)

California’s DROP lets consumers delete data from 1,600+ brokers in one click—but behind the scenes it raises serious security, compliance, and transparency risks.

* [![Deepak Gupta](/content/images/size/w100/2025/12/Gupta-Deepak-Studio-Session-2905.jpg)](/author/deepak-gupta/)

#### [Deepak Gupta](/author/deepak-gupta/)

Jan 10, 2026

[Tip Writer](https://ko-fi.com/secjuice)

![California Just Built a Data Deletion Tool That Actually Works (And Data Brokers Are Sweating)](https://images.unsplash.com/photo-1619083382085-9452906b7157?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMTc3M3wwfDF8c2VhcmNofDN8fGNhbGlmb3JuaWF8ZW58MHx8fHwxNzY3NTkyNjYxfDA&ixlib=rb-4.1.0&q=80&w=2000)

Photo by [Lala Miklós](https://unsplash.com/%40lalamiklos024?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit) / [Unsplash](https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)

I've been dealing with data privacy regulations for over 15 years. GDPR, CCPA, dozens of state laws—most of them great on paper, terrible in execution. But California just launched something different.

It's called [DROP (Delete Records Of Personal Data)](https://privacy.ca.gov/drop/about-drop-and-the-delete-act/?ref=secjuice.com), and it's the first government-run platform that lets you nuke your data from 1,600+ data brokers with a single request. No forms per broker. No endless verification emails. One click.

Sounds too good to be true, right? Let me tell you what's actually happening under the hood.

## The Problem DROP Actually Solves

Here's what data deletion looked like before DROP:

* You discover Acxiom has your data.
* You submit a deletion request.
* They have 45 days to respond.
* You verify your identity in three different ways.
* They finally delete it.
* Meanwhile, 83 other brokers still have it.

Want to clean them all? That's 84 separate requests, 84 verification processes, months of follow-up. Nobody does it. That's exactly why the system was broken.

The DELETE Act (AB 375) changed the game. Instead of putting the burden on consumers, it created a centralized deletion mechanism. And DROP is that mechanism.

## How DROP Actually Works (Technical Reality)

When you submit a [request through DROP](https://guptadeepak.com/californias-drop-the-first-of-its-kind-data-deletion-platform-that-could-reshape-global-privacy-standards/?ref=secjuice.com), here's what happens:

* **Identity Verification:** California uses Login.gov for authentication. This isn't just username/password—it's identity proofing that meets NIST 800-63-3 standards. They need to know you're actually you before they start deleting your data everywhere.
* **Broker Notification:** Your deletion request hits the California Privacy Protection Agency's system. They batch requests and distribute them to registered data brokers through their Data Broker Registry.
* **48-Hour Window:** Brokers have 48 hours to acknowledge receipt. Not 45 days to complete it—48 hours just to say "we got it."
* **Verification Requirements:** Here's where it gets interesting. Each broker has to verify it's actually your data before deletion. But they can't ask you to verify each request individually (that would defeat the purpose). So they're stuck implementing automated verification systems that work with DROP's authentication.
* **Deletion Execution:** Brokers must delete data from:
  + Active databases
  + Backup systems (this is the hard part)
  + Derived datasets
  + Third-party systems where they've shared your data

That last one is brutal. If Broker A sold your data to Broker B, Broker A has to track down Broker B and get them to delete it, too.

## The Security Nightmare Nobody's Talking About

DROP is brilliant from a consumer perspective. From a security perspective, it's terrifying. Here's why:

* **Mass Deletion Authority:** Think about what DROP represents—a single authentication that can delete data across 1,600+ organizations. That's an incredibly high-value target.
* **Identity Theft Paradise:** If someone compromises your Login.gov account, they can delete your data from every broker. Sounds good until you realize some of that data is used for fraud prevention. Suddenly, you can't open bank accounts, get credit, or verify your identity anywhere.
* **Broker Authentication Gaps:** Each broker needs to verify that the deletion request came from DROP and applies to real data. Most brokers aren't equipped for this. They're going to implement whatever's easiest, which means inconsistent security across the ecosystem.
* **No Audit Trail for Users:** You submit a request. You get confirmation that it was sent. But do you know which brokers actually deleted your data? Do you know what they deleted? Do you know if they missed anything in backup systems? Nope.

## What Data Brokers Are Actually Doing

I've talked to folks at several data brokers. Here's what's happening behind the scenes:

* Some are building compliant systems. Automated verification, proper deletion workflows, and audit logs. It's expensive and time-consuming, but they're doing it right.
* Others are taking shortcuts. "Soft deletes" where data gets flagged but not actually removed. Automated "we can't verify this" responses to slow things down. Creative interpretations of what counts as "derived data."
* And some are just confused. They don't have systems to track where they've shared data. They can't identify all instances of a person's information. They're going to miss stuff—not maliciously, just because their infrastructure can't handle it.

## The CCPA Compliance Trap

Here's the part that keeps me up at night: DROP is built on CCPA's deletion requirements. But CCPA has exceptions—lots of them.

Brokers can keep your data if they need it for:

* Completing transactions
* Detecting security incidents
* Complying with other legal obligations
* Internal uses "reasonably aligned" with consumer expectations

That last one is a loophole big enough to drive a truck through.

So you use DROP, you get confirmation, you think you're clean. But Broker X kept 40% of your data under "reasonable business purposes." You'd never know unless you submitted a CCPA data request separately to see what they still have.

## What Actually Needs to Happen

DROP is a good start, but here's what would make it actually work:

* **Verification Transparency:** Users need to see which brokers confirmed deletion and which ones claimed exceptions. Right now, it's a black box.
* **Automated Monitoring:** The system should periodically check if deleted data reappears. If Broker A deleted your data but Broker B (who bought it from A six months ago) still has it, you should know.
* **Penalty Enforcement:** CCPA violations can cost $7,500 per violation. But unless California actively audits brokers, there are no teeth. They need automated compliance checking, not an honor system.
* **Data Minimization Standards:** Instead of just enabling deletion, require brokers to justify why they're collecting data in the first place. Make them prove the business purpose before collection, not after.
* **Kill Switch Limits:** Right now, DROP can delete everything. There should be categories—delete marketing data but preserve fraud prevention data, for example.

## For Security Practitioners

If you're working on systems that might interact with DROP (or similar platforms that will inevitably follow), here's what you need to think about:...