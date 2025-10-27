---
title: Windows Event Log Analysis – Complete Incident Response Guide
url: https://cybersecuritynews.com/windows-event-log-analysis/
source: Instapaper: Unread
date: 2022-10-20
fetch_date: 2025-10-03T20:25:43.109925
---

# Windows Event Log Analysis – Complete Incident Response Guide

[Linkedin](https://www.linkedin.com/company/cybersecurity-news/ "Linkedin")

[Naver](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en "Naver")

[RSS](https://cybersecuritynews.com/feed/ "RSS")

[Twitter](https://twitter.com/The_Cyber_News "Twitter")

* [Home](https://cybersecuritynews.com/)
* [Threats](https://cybersecuritynews.com/category/threats/)
* [Cyber Attacks](https://cybersecuritynews.com/category/cyber-attack/)
* [Vulnerabilities](https://cybersecuritynews.com/category/vulnerability/)
* [Breaches](https://cybersecuritynews.com/category/data-breaches/)
* [Top 10](https://cybersecuritynews.com/category/top-10/)

Search

[![Cyber Security News](https://cybersecuritynews.com/wp-content/uploads/2025/05/Cyber-Security-News-Logo.webp "Cyber Security News")Cyber Security NewsLatest Cyber Security News](https://cybersecuritynews.com/ "Cyber Security News")

Friday, October 3, 2025

[Linkedin](https://www.linkedin.com/company/cybersecurity-news/ "Linkedin")

[RSS](https://cybersecuritynews.com/feed/ "RSS")

[Twitter](https://x.com/The_Cyber_News "Twitter")

[Google News](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en "Google News")[Google News](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en)

[![Cyber Security News](https://cybersecuritynews.com/wp-content/uploads/2025/05/Cyber-Security-News-Logo.webp "Cyber Security News")Cyber Security NewsLatest Cyber Security News](https://cybersecuritynews.com/ "Cyber Security News")

* [Home](https://cybersecuritynews.com/)
* [Threats](https://cybersecuritynews.com/category/threats/)
* [Cyber Attacks](https://cybersecuritynews.com/category/cyber-attack/)
* [Vulnerabilities](https://cybersecuritynews.com/category/vulnerability/)
* [Breaches](https://cybersecuritynews.com/category/data-breaches/)
* [Top 10](https://cybersecuritynews.com/category/top-10/)

[Follow on LinkedIn](https://www.linkedin.com/company/cybersecurity-news/ "Follow on LinkedIn")

Search

[Home](https://cybersecuritynews.com/)  [CyberPedia](https://cybersecuritynews.com/category/cyberpedia/ "View all posts in CyberPedia")  Windows Event Log Analysis – Complete Incident Response Guide

* [CyberPedia](https://cybersecuritynews.com/category/cyberpedia/)
* [Top 10](https://cybersecuritynews.com/category/top-10/)

# Windows Event Log Analysis – Complete Incident Response Guide

By

[Balaji N](https://cybersecuritynews.com/author/balaji/)

-

October 19, 2022

[![Windows Event Log Analysis – Complete Incident Response Guide](https://i2.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuLZGTzVk9kgLC7_PS7l2OUm3fKDVTlc2i3EPxI703COmJOeO_btsxMI13GAHjaUYMJtg2csvPWIlgt7vpXoPwb7QRkdaQzmbFh4WRf-7FYfY01nOcH8RzXbVOuF_VdvhUfxQk1igH0_WbBhEq8buBJ1-KfW_-vFVpKKRYVweaKMD73We-VD-KqOt4A1k7/s16000/Windows%20Event%20Log%20Analysis%20(1).webp?w=1068&resize=1068,0&ssl=1 "Windows Event Log Analysis – Complete Incident Response Guide")](https://i2.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuLZGTzVk9kgLC7_PS7l2OUm3fKDVTlc2i3EPxI703COmJOeO_btsxMI13GAHjaUYMJtg2csvPWIlgt7vpXoPwb7QRkdaQzmbFh4WRf-7FYfY01nOcH8RzXbVOuF_VdvhUfxQk1igH0_WbBhEq8buBJ1-KfW_-vFVpKKRYVweaKMD73We-VD-KqOt4A1k7/s16000/Windows%20Event%20Log%20Analysis%20%281%29.webp?w=1600&resize=1600,900&ssl=1)

Windows event logging provides detailed information like source, username, computer, type of event, and level, and shows a log of application and system messages, including errors, information messages, and warnings.

Microsoft has to keep increasing the efficiency and effectiveness of its auditing facilities over the years. Modern Windows systems can log vast amounts of information with minimal system impact.

Configuring adequate logging on Windows systems, and ideally aggregating those logs into a SIEM or other log aggregator, is a critical step toward ensuring that your environment is able to support effective incident response using [**Incident response tools**](https://cybersecuritynews.com/incident-response-tools/).

**Also Read: [SIEM Better Visibility for SOC Analyst](https://gbhackers.com/siem-for-better-visibility-for-an-analyst-to-handle-an-incident/)**

## **Event Log Format**

Modern Windows systems store logs in the %SystemRoot%\System32\winevt\logs directory by default in the binary XML Windows Event Logging format, designated by the .evtx extension. Logs can also be stored remotely using log subscriptions.

Events can be logged in the Security, System and Application event logs or, on modern Windows systems, they may also appear in several other log files. The Setup event log records activities that occurred during the installation of Windows.

[![google](https://thecybernews.com/csngoogle.svg
)](https://www.google.com/preferences/source?q=cybersecuritynews.com)

The Forwarded Logs event log is the default location to record events received from other systems. But there are also many additional logs, listed under Applications and Services Logs in Event Viewer, that record details related to specific types of activities.

* **Log Name:** The name of the Event Log where the event is stored. Useful when processing numerous logs pulled from the same system.
* **Source:** The service, Microsoft component or application that generated the event.
* **Event ID:** A code assigned to each type of audited activity.
* **Level:** The severity assigned to the event in question.
* **User:** The user account involved in triggering the activity or the user context that the source was running as when it logged the event. Note that this field often indicates “System” or a user that is not the cause of the event being recorded.
* **OpCode:** Assigned by the source generating the log. It’s meaning is left to the source.
* **Logged:** The local system date and time when the event was logged.
* **Task Category:** Assigned by the source generating the log. It’s meaning is left to the source.
* **Keywords:** Assigned by the source and used to group or sort events.
* **Computer:** The computer on which the event was logged. This is useful when examining logs collected from multiple systems, but should not be considered to be the device that caused an event (such as when a remote logon is initiated, the Computer field will still show the name of the system logging the event, not the source of the connection).
* **Description:** A text block where additional information specific to the event being logged is recorded. This is often the most significant field for the analyst.

## **Types of Windows Event Log Analysis – Guide**

* **Account Management Events**
* **Account Logon and Logon Events**
* **Common Event ID 4768 result codes**
* **Logon event type code descriptions**
* **Common logon failure status codes**
* **Access to Shared Objects**
* **Scheduled Task Logging**
* **Object Access Auditing**
* **Audit Policy Changes**
* **Auditing Windows Services**
* **Wireless LAN Auditing**
* **Process Tracking**
* **Additional Program Execution Logging**
* **Auditing PowerShell Use**

## **Account Management Events**

The following events will be recorded on the system where the account was created or modified, which will be the local system for a local account or a domain controller for a domain account.

|  |  |
| --- | --- |
| **Event ID** | **Description** |
| 4720 | A user account was created. |
| 4722 | A user account was enabled. |
| 4723 | A user attempted to change an account’s password. |
| 4724 | An attempt was made to reset an account’s password. |
| 4725 | A user account was disabled. |
| 4726 | A user account was deleted. |
| 4727 | A security-enabled global group was created. |
| 4728 | A member was added to a security-enabled global group. |
| 4729 | A member was removed from a security-enabled global group. |
| 4730 | A security-e...