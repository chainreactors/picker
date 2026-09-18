---
title: Dfirai primer how to combat hallucinations
url: https://www.cybertriage.com/ai/dfirai-primer-how-to-combat-hallucinations/
source: Instapaper: Unread
date: 2026-09-17
fetch_date: 2026-09-18T06:53:40.803637
---

# Dfirai primer how to combat hallucinations

[Skip to content](#primary)

[cyber-triage-logo](https://www.cybertriage.com/)

Primary Menu

* [Platform](https://www.cybertriage.com/features/)
  + - * [Workflow](https://www.cybertriage.com/how-cyber-triage-works/)
      * [Benefits](https://www.cybertriage.com/benefits/)
      * [Why Cyber Triage](https://www.cybertriage.com/why-cyber-triage-digital-forensics-tool/)
      * [Cyber Triage for Teams](https://www.cybertriage.com/team-version/)
      * [Cyber Triage for Enterprise](https://www.cybertriage.com/enterprise/)
    - * #### Key Features
      * [Compare Versions](https://www.cybertriage.com/pricing/)
      * [The Collector](https://www.cybertriage.com/cyber-triage-dfir-collector/)
      * [Guided Analysis](https://www.cybertriage.com/guided-analysis/)
      * [Malware Detection](https://www.cybertriage.com/malware-forensics-tool/)
      * [How Cyber Triage Uses AI](https://www.cybertriage.com/how-we-use-ai-in-cyber-triage/)
    - * #### EDR
      * [EDR + Cyber Triage](https://www.cybertriage.com/edr/)
      * [EDR Evasion 101](https://www.cybertriage.com/blog/how-edr-evasion-works-attacker-tactics/)
    - * #### Integrations
      * [EDR Powershell Script](https://www.cybertriage.com/deployer-script/)
      * [Integrated Capabilities](https://www.cybertriage.com/features/integrations/)
      * [Malware Scanner for Autopsy](https://www.cybertriage.com/autopsy-malware-module/)
* Use Cases
  + [SOC Endpoint Investigation](https://www.cybertriage.com/soc-alert-investigation/)
  + [Consultants](https://www.cybertriage.com/consultants/)
  + [SOC DFIR Teams](https://www.cybertriage.com/internal-incident-responders/)
  + [Law Enforcement - Intrusions](https://www.cybertriage.com/law-enforcement/)
  + [Law Enforcement - ICAC (Trojan Defense)](https://www.cybertriage.com/detect-remote-access-for-icac-and-trojan-defense/)
* [Pricing](https://www.cybertriage.com/pricing/)
  + [Buy Cyber Triage](https://www.cybertriage.com/pricing/)
  + [Buy Malware Scanning Boosts](https://www.cybertriage.com/boost-checkout/)
  + [Buy Autopsy Malware Scanner Module](https://www.cybertriage.com/autopsy-checkout/)
  + [Buy Rapid Endpoint Triage Service](https://www.sleuthkitlabs.com/rapid_checkout/)
* [Resources](https://www.cybertriage.com/online-response-training/)
  + - * #### DFIR Education
      * [Blog](https://www.cybertriage.com/blog/)
      * [Training](https://www.cybertriage.com/training/)
      * [Webinars](https://www.cybertriage.com/events/)
      * [Product Videos](https://www.cybertriage.com/videos/)
      * [Intro to DFIR Blog Series](https://www.cybertriage.com/intro-to-cyber-incident-response/)
    - * #### Case Studies
      * [How to Bridge the EDR/Forensics Gap](https://www.cybertriage.com/blog/how-an-industrial-manufacturer-accelerated-investigations-with-cyber-triage/)
      * [How to Scale IR Collaboration](https://www.cybertriage.com/blog/how-a-fortune-100s-ir-team-accelerated-client-investigations/)
      * [How to Escalate to IR with Confidence](https://www.cybertriage.com/blog/how-a-major-german-bank-reduced-risk-saved-money-with-cyber-triage/)
      * [How to Speed Up Client Investigations](https://www.cybertriage.com/blog/how-cy4-cut-analysis-time-75/)
    - * #### Recent Releases
      * [3.18 (More MCP & Cloud Functions)](https://www.cybertriage.com/blog/cyber-triage-3-18-new-ai-cloud-automation-capabilities/)
      * [3.17 (MCP & GenAI)](https://www.cybertriage.com/blog/cyber-triage-3-17-use-cyber-triage-with-ai/)
      * [3.16 (Enterprise Tier)](https://www.cybertriage.com/blog/cyber-triage-3-16-investigate-faster-with-cyber-triage-enterprise/)
      * [3.15 (Defender Telemetry, Access Control, IRIS)](https://www.cybertriage.com/blog/cyber-triage-3-15-import-defender-telemetry-more-soc-features/)
* [About](https://www.cybertriage.com/about/)
  + [About](https://www.cybertriage.com/about/)
  + [Team](https://www.cybertriage.com/team/)
  + [Contact](https://www.cybertriage.com/contact/)
* [Start Free Trial](https://www.cybertriage.com/download-eval/)

Close signup

![](https://www.cybertriage.com/wp-content/uploads/2021/04/cyber-triage-logo-color-1.png)
Stay up to date on our **technology, training, events,** and more.

By submitting this form, you agree that Sleuth Kit Labs may process your information in accordance with our [Privacy Policy](https://sleuthkitlabs.com/privacy-policy/). We’ll use your information to send educational and marketing communications.

You can unsubscribe at any time using the link in our emails.

Not now >

Sleuth Kit Labs | 1070 Broadway, Somerville, MA 02144-2078 | info@sleuthkitlabs.com

# DFIR + AI Primer: How to Combat Hallucinations

* May 28, 2026
* **[Dr. Brian Carrier](https://www.cybertriage.com/team/dr-brian-carrier/)**

[All Blogs](https://www.cybertriage.com/blog/)

GenAI outputs require verification because of hallucinations. As you integrate AI into your investigations, it is important to understand why hallucinations happen and how to address them based on your risk thresholds.

GenAI can provide value to an investigation, but it’s not for free.

## **Why does GenAI Hallucinate?**

GenAI algorithms use probabilities to generate sequences of words. It can ultimately generate a sequence of words that are probable, but not accurate.

This most often comes into play when you ask GenAI to enrich and reason about your data when it doesn’t actually know much about it. It can generate false information about an artifact and come to conclusions it can’t actually justify.

Here is a recent DFIR example I had (paraphrasing for brevity):

> **Claude**: ‘co1bld’ is a standard hostname that appears in the LNK files created on Microsoft’s internal build infrastructure during the Windows build process. These LNK files are not suspicious even though they were created on a different machine.
>
> **Me**: Do you have a reference for that hostname?
>
> **Claude**: Honestly, no — I don’t have a reliable citation for that. When I said it, I was drawing on what seems like plausible pattern-matching (the naming convention, the context), but I can’t point you to a public source that definitively documents co1bld as a Microsoft internal build hostname.

We ultimately decided not to take Claude’s advice and could not find any Internet references to it. Cyber Triage will still flag LNK files that have ‘co1bld’ as their hostname.

## **Combating Hallucinations**

There are several ways to verify data is not a hallucination:

* **Query for item existence**: You can automatically confirm that items referred to by AI are actually in the original data set with a simple deterministic query by their path, time, etc.
* **Manual:** Confirm enrichment with other deterministic data sources, such as threat intelligence feeds or websites that were cited for the conclusion. This often requires a human to reason that the data source and the AI conclusion are equivalent.
* **Judging LLM**: Have an independent LLM review the enrichment and storyline to confirm that it agrees (i.e., Claude vs ChatGPT). This can still have errors, but it can increase your overall confidence.

The Judging LLM approach can help with reasoning errors, and one model could identify a logical mistake made by another. But it may not catch knowledge errors because they may both have the same knowledge gaps or wrong data (i.e., the internet is wrong about something).

## **Know Your Investigation and AI Risk Levels**

Not every investigation has the same impact, and therefore each can have different risk thresholds for how much to verify the results.

**Examples:**

* A low-severity EDR alert investigation could have a high-risk threshold and be OK with little human verification or with a judging LLM.
* A medium-severity EDR alert may want a human to review the timeline and double-check that nothing else was missed.
* A criminal case where someone could go to jail should have a low-risk threshold, and a human verifies every item in the final result.

Know your inv...