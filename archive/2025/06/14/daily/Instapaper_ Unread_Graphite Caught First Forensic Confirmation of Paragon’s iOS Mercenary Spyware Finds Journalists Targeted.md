---
title: Graphite Caught First Forensic Confirmation of Paragon’s iOS Mercenary Spyware Finds Journalists Targeted
url: https://citizenlab.ca/2025/06/first-forensic-confirmation-of-paragons-ios-mercenary-spyware-finds-journalists-targeted/
source: Instapaper: Unread
date: 2025-06-14
fetch_date: 2025-10-06T22:55:26.239537
---

# Graphite Caught First Forensic Confirmation of Paragon’s iOS Mercenary Spyware Finds Journalists Targeted

[![The Citizen Lab](https://citizenlab.ca/wp-content/themes/citizenlab-2.1.5/library/images/CL-logo-3-headed.png)](https://citizenlab.ca)
![Munk School of Global Affairs & Public Policy | University of Toronto](https://citizenlab.ca/wp-content/themes/citizenlab-2.1.5/library/images/MunkSchool-WHT.png)

[Open main menu](#main-menu)

[Skip to main content](#main)

[Close main menu](#homepage)

* [Research](https://citizenlab.ca/category/research/)
  + [Targeted Threats](https://citizenlab.ca/category/research/targeted-threats/)
  + [Free Expression Online](https://citizenlab.ca/category/research/free-expression-online/)
  + [Transparency and Accountability](https://citizenlab.ca/category/research/transparency/)
  + [App Privacy and Controls](https://citizenlab.ca/category/research/app-privacy-and-security/)
  + [Global Research Network](https://citizenlab.ca/category/research/global-research-network/)
  + [Tools & Resources](https://citizenlab.ca/category/research/tools-resources/)
  + [Publications](https://citizenlab.ca/publications/)
* [News](https://citizenlab.ca/category/lab-news/)
  + [In the Media](https://citizenlab.ca/category/lab-news/mentions/)
  + [Events](https://citizenlab.ca/category/lab-news/events/)
  + [Opportunities](https://citizenlab.ca/category/lab-news/opportunities/)
* [About](https://citizenlab.ca/about/)
  + [About The Citizen Lab](https://citizenlab.ca/about/)
  + [Media Resources](https://citizenlab.ca/media/)
  + [People](https://citizenlab.ca/people/)
  + [Teaching](https://citizenlab.ca/teaching/)
  + [Donate](https://engage.utoronto.ca/site/SPageServer?pagename=donate#/fund/847)
  + [Security Vulnerabilities](https://citizenlab.ca/disclosure-of-security-vulnerabilities/)

[[Research](https://citizenlab.ca/category/research/)](https://citizenlab.ca/category/research/)[Targeted Threats](https://citizenlab.ca/category/research/targeted-threats/)

# Graphite Caught First Forensic Confirmation of Paragon’s iOS Mercenary Spyware Finds Journalists Targeted

By
[Bill Marczak](https://citizenlab.ca/author/bmarczak/ "Posts by Bill Marczak") and [John Scott-Railton](https://citizenlab.ca/author/jsrailton/ "Posts by John Scott-Railton")

June 12, 2025

# Introduction

On April 29, 2025, a select group of iOS users were notified by Apple that they were targeted with advanced spyware. Among the group were two journalists that consented for the technical analysis of their cases. The key findings from our forensic analysis of their devices are summarized below:

* Our analysis finds forensic evidence confirming with high confidence that both a prominent European journalist (who requests anonymity), and Italian journalist Ciro Pellegrino, were targeted with Paragon’s Graphite mercenary spyware.
* We identify an indicator linking both cases to the same Paragon operator.
* Apple confirms to us that the zero-click attack deployed in these cases was mitigated as of iOS 18.3.1 and has assigned the vulnerability [CVE-2025-43200](https://support.apple.com/en-us/122174).

Our analysis is ongoing.

# Case 1: Prominent European Journalist

We analyzed Apple devices belonging to a prominent European journalist who has requested to remain anonymous. On April 29, 2025, this journalist received an Apple notification and sought technical assistance.

Our forensic analysis concluded that one of the journalist’s devices was compromised with Paragon’s Graphite spyware in January and early February 2025 while running iOS 18.2.1. We attribute the compromise to Graphite with high confidence because logs on the device indicated that it made a series of requests to a server that, during the same time period, matched our [published](https://citizenlab.ca/2025/03/a-first-look-at-paragons-proliferating-spyware-operations/) Fingerprint P1. We linked this fingerprint to Paragon’s Graphite spyware with high confidence.

**Graphite spyware server contacted by the journalist’s device:**

|  |
| --- |
| https://46.183.184[.]91/ |

The server appears to have been rented from VPS provider [EDIS Global](https://www.edisglobal.com/about). The server remained online and continued to match Fingerprint P1 until at least April 12, 2025.

![](https://citizenlab.ca/wp-content/uploads/2025/06/image2.png "Graphite Caught: First Forensic Confirmation of Paragon’s iOS Mercenary Spyware Finds Journalists Targeted 1")

**Figure 1.** Censys result for the IP address contacted by the journalist’s phone during the infection period.

We identified an iMessage account present in the device logs around the same time as the phone was communicating with the Paragon server `46.183.184[.]91`. We redact the account and refer to it as **ATTACKER1**. Based on our forensic analysis, we conclude that this account was used to deploy Paragon’s Graphite spyware using a sophisticated iMessage zero-click attack. We believe that this infection would not have been visible to the target. Apple confirms to us that the zero-click attack deployed here was mitigated as of iOS 18.3.1 and has assigned [CVE-2025-43200](https://support.apple.com/en-us/122174) to this zero-day vulnerability.

# **Case 2: Ciro Pellegrino**

Ciro Pellegrino is a journalist and head of the Naples newsroom at *Fanpage.it,* where he has reported on numerous high-profile cases. On April 29, 2025, Mr. Pellegrino received an Apple notification and sought our technical assistance.

We analyzed artifacts from Mr. Pellegrino’s iPhone and determined with high confidence that it was targeted with Paragon’s Graphite spyware. Our analysis of the device’s logs revealed the presence of the same **ATTACKER1** iMessage account used to target the journalist from **Case 1**, which we associate with a Graphite zero-click infection attempt.

![](https://citizenlab.ca/wp-content/uploads/2025/06/Paragonredux-1.png "Graphite Caught: First Forensic Confirmation of Paragon’s iOS Mercenary Spyware Finds Journalists Targeted 2")

**Figure 2**. Attribution to Paragon’s Graphite spyware via artifacts found on the devices of Ciro Pellegrino and the unnamed prominent European journalist.

It is standard for each customer of a mercenary spyware company to have its own dedicated infrastructure. Thus, we believe that the **ATTACKER1** account would be used exclusively by a single Graphite customer / operator, and we conclude that this customer targeted both individuals.

Our forensic analyses of these attacks, and Paragon’s iOS capabilities, are ongoing.

## **The Fanpage.it Paragon Cluster**

Mr. Pellegrino’s close colleague and *Fanpage.it* editor, Francesco Cancellato, was [notified](https://citizenlab.ca/2025/03/a-first-look-at-paragons-proliferating-spyware-operations/) in January 2025 by WhatsApp that he was targeted with Paragon’s Graphite spyware.

The Citizen Lab has been conducting forensic analysis of Mr. Cancellato’s Android device. However, as of our initial report, we were unable to obtain forensic confirmation of a successful infection of Mr. Cancellato’s Android. As we explained at the time: “Given the sporadic nature of Android logs, the absence of a finding of BIGPRETZEL on a particular device does not mean that the phone wasn’t successfully hacked, simply that relevant logs may not have been captured or may have been overwritten.”

Following Mr. Cancellato’s case, the identification of a second journalist at Fanpage.it targeted with Paragon suggests an effort to target this news organization This appears to be a distinct cluster of cases that warrants further scrutiny.

# **Statements by Paragon and the Italian Government**

On June 5, 2025, the Italian government’s parliamentary committee overseeing Italy’s intelligence services (COPASIR: Comitato Parlamentare per la Sicurezza della Repubblica) [published](https://documenti.camera.it/_dati/leg19/lavori/documentiparlamentari/IndiceETesti/034/004/INTERO.pdf) the report of their inquiry into the Paragon affair in Italy.

The report acknowledged that the Italian government had used Paragon’s Graphite ...