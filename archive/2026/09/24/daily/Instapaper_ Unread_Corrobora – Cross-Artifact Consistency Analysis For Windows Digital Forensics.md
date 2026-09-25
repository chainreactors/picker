---
title: Corrobora – Cross-Artifact Consistency Analysis For Windows Digital Forensics
url: https://www.forensicfocus.com/articles/corrobora-cross-artifact-consistency-analysis-for-windows-digital-forensics/
source: Instapaper: Unread
date: 2026-09-24
fetch_date: 2026-09-25T06:53:30.966397
---

# Corrobora – Cross-Artifact Consistency Analysis For Windows Digital Forensics

[Skip to content](#content "Skip to content")

* [Login/Register](https://www.forensicfocus.com/sign-in/?redirect_to=https%3A%2F%2Fwww.forensicfocus.com%2Farticles%2Fcorrobora-cross-artifact-consistency-analysis-for-windows-digital-forensics%2F)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/themes/generatepress_child/assets/images/logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

[Login](/sign-in/)
[Register](/sign-up/)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/uploads/2020/05/forensic-focus_logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

Menu

* News
  + [Headlines](/news/headlines/latest/)
  + [More News](/news/)
* Articles
  + [Articles](/articles/)
  + [Interviews](/interviews/)
  + [Case Studies](/case-studies/)
  + [Reviews](/reviews/)
  + [Guides](/guides/)
  + [Digital Forensics Timeline](/digital-forensics-timeline/)
  + [Tool & Vendor Directory](/dfir-tool-directory/)
  + [Tool Release Tracker](/dfir-tool-release-tracker/)
* Webinars/Videos
  + [Webinars](/webinars/)
  + [Videos](/videos/)
* Careers & Jobs
  + [Browse Jobs](/jobs/)
  + [How to Start a Career](/articles/how-to-start-a-career-in-digital-forensics/)
  + [Education & Training Guide](/articles/digital-forensics-education-certification-and-training-guide/)
  + [Training Finder](/dfir-training-finder/)
  + [Salary Explorer](/dfir-salary-explorer/)
  + [Skills in Demand](/dfir-skills-demand-explorer/)
  + [Practice & CTFs](/dfir-practice-directory/)
* [Well-Being](/well-being/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](/event-info/)

* [Forums](/forums/)
* [Discord](https://discord.gg/97zKvTXHeS)
* [Podcast](/podcast/)
* [Newsletter](/newsletter/)
* [Links](/useful-links/)
* [Advertise](/advertising/)
* [About](/about/)

Menu

* News
  + [Headlines](/news/headlines/latest/)
  + [More News](/news/)
* Articles
  + [Articles](/articles/)
  + [Interviews](/interviews/)
  + [Case Studies](/case-studies/)
  + [Reviews](/reviews/)
  + [Guides](/guides/)
  + [Digital Forensics Timeline](/digital-forensics-timeline/)
  + [Tool & Vendor Directory](/dfir-tool-directory/)
  + [Tool Release Tracker](/dfir-tool-release-tracker/)
* Webinars/Videos
  + [Webinars](/webinars/)
  + [Videos](/videos/)
* Careers & Jobs
  + [Browse Jobs](/jobs/)
  + [How to Start a Career](/articles/how-to-start-a-career-in-digital-forensics/)
  + [Education & Training Guide](/articles/digital-forensics-education-certification-and-training-guide/)
  + [Training Finder](/dfir-training-finder/)
  + [Salary Explorer](/dfir-salary-explorer/)
  + [Skills in Demand](/dfir-skills-demand-explorer/)
  + [Practice & CTFs](/dfir-practice-directory/)
* [Well-Being](/well-being/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](/event-info/)

[Home](https://www.forensicfocus.com/) » [Articles](https://www.forensicfocus.com/articles/) » Corrobora – Cross-Artifact Consistency Analysis For Windows Digital Forensics

# Corrobora – Cross-Artifact Consistency Analysis For Windows Digital Forensics

24th September 2026 by [Forensic Focus](https://www.forensicfocus.com/author/forensicfocus/ "View all posts by Forensic Focus")

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/09/ChatGPT-Image-Sep-24-2026-04_17_11-PM.png)

*by [Dielle De Noon](https://gear-i.github.io), M.S.*

## Abstract

This article presents the design and development of [Corrobora](https://github.com/Gear-I/Corrobora/tree/main), an open-source Windows digital forensics framework built as part of a Master of Science in Cybersecurity capstone at Western Governors University. Unlike tools that examine forensic artifacts in isolation, Corrobora is designed to compare evidence across multiple independent Windows artifact sources to identify inconsistencies that may warrant further investigation. This article covers the first two milestones of the project: the Windows Event Log (EVTX) parser and the Windows Registry parser. It discusses the motivation for each component, the shared design philosophy that guided their development, the technical challenges encountered, and how both parsers lay the groundwork for Corrobora’s planned cross-artifact correlation engine.

## Introduction

Every digital forensic investigation begins with a fundamental question: what happened on this system? Answering that question requires investigators to collect, analyze, and validate evidence from multiple sources while ensuring their conclusions are based on reliable and defensible data. Windows systems generate a vast amount of forensic evidence, and two of the most valuable sources available to investigators are the Windows Event Log (EVTX) and the Windows Registry.

Windows Event Logs provide a chronological record of operating system activity, authentication events, application behavior, security auditing, service execution, and countless other events that help investigators reconstruct system activity. The Windows Registry, by contrast, serves as the operating system’s central configuration database, preserving information about installed software, user preferences, hardware devices, startup locations, and other configuration details that often remain available long after an event occurs.

As part of my capstone research, I am developing Corrobora, an open-source Windows digital forensics framework focused on cross-artifact consistency analysis. Rather than examining forensic artifacts independently, Corrobora compares evidence across multiple Windows artifact sources to identify inconsistencies that may warrant further investigation. The EVTX parser and the Registry parser are the first two major milestones of the project, and together they establish the engineering patterns and forensic principles that will guide the rest of the framework’s development.

## Get The Latest DFIR News

### The monthly Forensic Focus newsletter, plus webinar invitations and occasional research surveys.

Unsubscribe or change what you receive at any time. We respect your privacy: read our [privacy policy](/privacy-policy).

Leave this field empty if you're human:

## Why Is This Important

Whether investigating ransomware, insider threats, unauthorized access, or policy violations, EVTX files frequently provide some of the earliest and most valuable evidence available in a Windows investigation. Event Logs exist on nearly every Windows installation, document activity across numerous Windows components, and provide chronological information that becomes valuable when constructing investigative timelines. Critically, Event Logs frequently contain evidence that can later be validated using independent artifacts, making them an ideal starting point for cross-artifact consistency analysis.

The Registry complements this record. From a digital forensics perspective, Registry artifacts can help answer questions such as what software is installed on a system, what programs are configured to start automatically, what user accounts have interacted with the computer, what system settings have changed, and which devices have previously been connected. Although the Registry rarely provides every answer by itself, it often provides valuable context when combined with other forensic artifacts, including Event Logs.

Most existing forensic tools already do an excellent job parsing either Event Logs or the Registry individually. What is largely missing is an open, transparent framework that treats these artifacts as pieces of a larger, correlated picture rather than as standalone evidence sources — which is the gap Corrobora is designed to address.

## What Is the Problem

Digital forensic investigations are built upon evidence, not individual artifacts. Yet many forensic workflows still treat artifacts such as Event Logs and the Registry as separate, independently analyzed sources of evidence, rather than as parts of a larger evidentiary picture. When artifacts are examined only in isolation, opportu...