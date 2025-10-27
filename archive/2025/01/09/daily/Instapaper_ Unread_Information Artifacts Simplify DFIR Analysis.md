---
title: Information Artifacts Simplify DFIR Analysis
url: https://www.cybertriage.com/blog/how-to-simplify-dfir-artifacts/
source: Instapaper: Unread
date: 2025-01-09
fetch_date: 2025-10-06T20:14:17.052845
---

# Information Artifacts Simplify DFIR Analysis

[Skip to content](#primary)

[cyber-triage-logo](https://www.cybertriage.com/)

Primary Menu

* [Platform](https://www.cybertriage.com/features/)
  + - * [Workflow](https://www.cybertriage.com/how-cyber-triage-works/)
      * [Benefits](https://www.cybertriage.com/benefits/)
      * [Why Cyber Triage](https://www.cybertriage.com/why-cyber-triage-digital-forensics-tool/)
      * [Compare Versions](https://www.cybertriage.com/features/versions/)
      * [Cyber Triage for Teams](https://www.cybertriage.com/team-version/)
    - * #### Key Features
      * [The Collector](https://www.cybertriage.com/cyber-triage-dfir-collector/)
      * [Artifact Scoring](https://www.cybertriage.com/features/prioritize-with-cyber-triage/)
      * [Malware Detection](https://www.cybertriage.com/malware-forensics-tool/)
      * [Ransomware Detection](https://www.cybertriage.com/features/ransomware/)
      * [Server API](https://www.cybertriage.com/team-rest-api/)
    - * #### EDR
      * [EDR + Cyber Triage](https://www.cybertriage.com/edr/)
      * [EDR Evasion 101](https://www.cybertriage.com/blog/how-edr-evasion-works-attacker-tactics/)
    - * #### Integrations
      * [EDR Powershell Script](https://www.cybertriage.com/deployer-script/)
      * [Integrated Capabilities](https://www.cybertriage.com/features/integrations/)
      * [Malware Scanner for Autopsy](https://www.cybertriage.com/autopsy-malware-module/)
* [Use Cases](https://www.cybertriage.com/benefits/)
  + [SOC Endpoint Investigation](https://www.cybertriage.com/soc-alert-investigation/)
  + [Consultants](https://www.cybertriage.com/benefits/consultants/)
  + [SOC DFIR Teams](https://www.cybertriage.com/benefits/internal-incident-responders/)
  + [Law Enforcement - Intrusions](https://www.cybertriage.com/benefits/law-enforcement/)
  + [Law Enforcement - ICAC (Trojan Defense)](https://www.cybertriage.com/detect-remote-access-for-icac-and-trojan-defense/)
* [Pricing](https://www.cybertriage.com/pricing/)
  + [Buy Cyber Triage](https://www.cybertriage.com/pricing/)
  + [Buy Malware Scanning Boosts](https://www.cybertriage.com/boost-checkout/)
  + [Buy Autopsy Malware Scanner Module](https://www.cybertriage.com/autopsy-checkout/)
  + [Buy Rapid Endpoint Triage Service](https://www.sleuthkitlabs.com/rapid_checkout/)
* [Resources](https://www.cybertriage.com/online-response-training/)
  + - * [Blog](https://www.cybertriage.com/blog/)
      * [Webinars](https://www.cybertriage.com/events/)
      * [Videos](https://www.cybertriage.com/videos/)
      * [Intro to DFIR Blog Series](https://www.cybertriage.com/intro-to-cyber-incident-response/)
      * [Cyber RespondIR Newsletter](https://www.cybertriage.com/sign-up-for-the-cyber-respondir/)
    - * [Rapid Endpoint Triage Service](https://www.cybertriage.com/services/#rapid)
      * [Training](https://www.cybertriage.com/training/)
    - * #### Recent Releases
      * [3.15 (Defender Telemetry, Access Control, IRIS)](https://www.cybertriage.com/blog/cyber-triage-3-15-import-defender-telemetry-more-soc-features/)
      * [3.14 (Tactics, Hayabusa, Baselining)](https://www.cybertriage.com/blog/3-14-release-brings-new-uis-hayabusa-baselining-and-much-more/)
      * [3.13 (MemProcFS, S3 Reading)](https://www.cybertriage.com/blog/releases/3-13-adds-memprocfs-and-extends-the-s3-and-recorded-future-sandbox-integrations/)
      * [3.12 (Data Exfil, USB, Validation)](https://www.cybertriage.com/blog/releases/3-12-adds-data-exfiltration-detection-usb-devices-and-easier-validation/)
* [About](https://www.cybertriage.com/about/)
  + [About](https://www.cybertriage.com/about/)
  + [Team](https://www.cybertriage.com/team/)
  + [Contact](https://www.cybertriage.com/contact/)
* [Start Free Trial](https://www.cybertriage.com/download-eval/)

# Information Artifacts: Simplify DFIR Analysis

* January 7, 2025
* **[Dr. Brian Carrier](https://www.cybertriage.com/team/dr-brian-carrier/)**

Do you know the differences between [MUICache](https://www.cybertriage.com/blog/muicache-2025-guide/), [ShimCache](https://www.cybertriage.com/blog/shimcache-and-amcache-forensic-analysis-2025/), [AMCache](https://www.cybertriage.com/blog/shimcache-and-amcache-forensic-analysis-2025/), and PMCache without the help of Google?

Did you know that one of them is made up?

You’re not alone if you didn’t. It’s hard to keep track of all of the artifact types that can be relevant for a forensics investigation.

As part of our efforts to make investigations easier, we avoid the above terms as much as possible. We instead use more simple terms, such as “Process” and “[Inbound Logons](https://www.cybertriage.com/blog/inbound-logon-artifact-deep-dive-series/)”.

We call these higher-level concepts “information artifacts.” This post maps out why we did this and how you can use them too in your work.

At a high level:

* **Data artifacts** represent data stored by an application on disk or in memory, such as Prefetch or MUICache.
* **Information artifacts** represent one or more data artifacts that have the same meaning and are for the same event, such as a “Process.”

## First Principles: Basic Computing Concepts

At the end of the day, all of us are investigating what happened on various types of computers, such as laptops, servers, or cell phones. To make investigations easier, it can help to focus on the core computing concepts.

There is no single list of core computing concepts, but I think of them as concepts that:

* Can be found in a computer science textbook or an operating system user manual.
* Are not unique to any single operating system or application.
* Answer a digital investigative question.

This list will evolve, but here are a few examples:

* **Operating System Configuration**: All computers have an operating system with various settings, some of which are relevant during an investigation.
* **Users**: Nearly all operating systems have a concept of user accounts, which define who can access the system and what permissions they have.
* **Processes**: All computers run processes with the permissions of a given user.
* **Network Connections**: Process can connect to other hosts by making network connections.
* **Messages:** Users can send messages to each other’s user protocols and applications.

The benefit of using these simple concepts is that:

* They are similar across all computers (Windows, Linux, MacOS, etc.).
* There are less than 20 of them (versus hundreds of other artifact types).
* We use them during our normal daily lives, and they become natural. We login, launch processes, connect to servers, etc.

You should be thinking about investigations with these high-level concepts in mind and not always worrying about Prefetch and Event ID 4688.

## Data Artifacts Are About Observations

Artifact is a word frequently used in the DFIR space to represent data from a system being investigated. We use the term “data artifact” to refer to these items.

Data artifacts are data stored by the operating system or other process for its own purposes. The application observed something and recorded it. Digital investigators leverage that data for our own purposes. We call these data artifacts because it’s data that was written by some application.

For example, [Prefetch](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/prefetch) exists because Microsoft wanted to track which processes recently ran so that it can preload data into memory. [Event ID 4688](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4688) exists because audit settings cause Windows to record when a process launches.

When a process launches, there are other applications besides Prefetch that also record that launch. Each application may record its data at a slightly different time and use a different format. They are all ultimately different observations of the same event and mean the same thing: a process launched.

We define a data artifact based on two c...