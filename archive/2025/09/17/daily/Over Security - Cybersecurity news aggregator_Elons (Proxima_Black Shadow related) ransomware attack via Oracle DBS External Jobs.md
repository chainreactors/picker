---
title: Elons (Proxima/Black Shadow related) ransomware attack via Oracle DBS External Jobs
url: https://labs.yarix.com/2025/09/elons-proxima-black-shadow-related-ransomware-attack-via-oracle-dbs-external-jobs/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-17
fetch_date: 2025-10-02T20:15:15.716413
---

# Elons (Proxima/Black Shadow related) ransomware attack via Oracle DBS External Jobs

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Elons (Proxima/Black Shadow related) ransomware attack via Oracle DBS External Jobs

* [Home](https://labs.yarix.com "Go to Home Page")
* Elons (Proxima/Black Shadow related) ransomware attack via Oracle DBS External Jobs

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2025/09/Gemini_Generated_Image_gjp8trgjp8trgjp8noconf.png)

16Sep16/09/2025

## Elons (Proxima/Black Shadow related) ransomware attack via Oracle DBS External Jobs

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2025-09-16T16:22:57+02:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   20 minutes

### Premise

As Yarix’s Incident Response Team, our responsibilities are to manage critical issues related to cyber-attacks carried out by cybercriminals, intervening promptly in order to guarantee security to victim companies and to minimize latent risks, analyzing the systems within their infrastructures and indicating precise remediation actions capable of re-establishing a state of security sufficient for normal operational recovery.

In the course of our activities, therefore, we are called upon to analyze the events that occurred on a case-by-case basis, reconstructing the attack chain used by the Threat Actor (TA: malicious actor, cybercriminal) to penetrate the implemented perimeter defenses and then, exploiting the foothold obtained in the corporate infrastructure, to extend its control within it for malicious purposes.

The first weaknesses to be exploited by attackers are those exposed by the infrastructure, which can be present within published portals, services exposed to the Internet and the public or even, in some cases, in appliances deployed on the perimeter to defend the infrastructure, such as Firewall devices, which can sometimes represent a weakness in the layered defense if not maintained and updated correctly or having vulnerable code. When the exploitation of a weak point occurs, it can allow cybercriminals to execute remote commands using specific techniques to exploit the technologies used in the infrastructure, bypassing defenses and allowing greater compromise of the same, up to, in the most disastrous cases, its total compromise and inoperability.

The aim of attackers is very often to profit through mechanisms such as blackmail. This is done by threatening the publication of company data exfiltrated from databases or servers during the perpetrated attack, within their own Data Leak Site (DLS: personal site of cybercriminals where the victims of attacks are announced to the public) and, in the case of encryption of systems through the use of ransomware files, by blocking victim’s business operativity.

To withdraw the threat of publication and regain access to company data by restoring the impacted systems, cybercriminals often demand the payment of a ransom in cryptocurrency, after which it would be possible to re-establish a situation of operational normality for the victim company.

In the specific case that will be dealt within this article, in anonymized form, we will illustrate a case in which the TA targeted an exposed service leveraging it to gain access to the infrastructure, creating an encrypted tunnel with a C2 server (Command&Control) and encrypting the only accessible server, thanks to the segmentation of the network implemented by the organization.

It should also be noted that some evidences, within the body of the article and in the images inserted, will be censored with “[redacted]” or asterisks and blurred, in order to avoid any traceability to the victim of the attack.

### The case analyzed

* **ENTRY POINT:** Oracle DBS Job Scheduler

The entry point detected was the use of a function of Oracle DBS, an exposed service active on their Database Server, which allowed the execution of commands remotely. The service was exploited to obtain abusive access to the infrastructure after several attempts to access it, evidenced by the numerous events related to logins, part of which we highlight for example in the following figure.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x49.jpg)

*Evidence of an attempt to log in to Oracle DBS*

The event logs of the attempts details the hostname of the TA machine, i.e. “WIN-2P3KK7923EM”, the user with whom the threat actor is logged on the attacking machine, i.e. “Administrator”, the action desired by the TA or “CONNECT”, the DBID which is an internal, unique identifier for an Oracle database, the user with whom the threat actor intended to access, i.e. “SYS” and the result of the operation or, in this case, “1017”, which corresponds to the failure of the attempt to access the database due to the use of incorrect credentials.

{“EventData”:{“Data”:”LENGTH: ‘184’ ACTION :[7] ‘CONNECT’ DATABASE USER:[3] ‘SYS’ PRIVILEGE :[4] ‘NONE’ CLIENT USER:[13] ‘Administrator’ CLIENT TERMINAL:[15] ‘WIN-2P3KK7923EM’ STATUS:[4] ‘1017’ DBID:[10] ‘1407890857’ “,”Binary”:””}}

It is also noted that no special privileges are requested within this access attempts, but the access attempts differed in terms of characteristics and results. In fact, shortly after, the attempt to access the Database evidenced that the result of the “CONNECT” action was the code “28009”, as presented in the raw log of the event below.

{“EventData”:{“Data”:”LENGTH: ‘185’ ACTION :[7] ‘CONNECT’ DATABASE USER:[3] ‘SYS’ PRIVILEGE :[4] ‘NONE’ CLIENT USER:[13] ‘Administrator’ CLIENT TERMINAL:[15] ‘WIN-2P3KK7923EM’ STATUS:[5] ‘28009’ DBID:[10] ‘1407890857’ “,”Binary”:””}}

The code “28009” corresponds to the failure of the connection because access with the user “SYS” is deprecated without specifying the database administrator clause, i.e. by requesting privileged access from “SYSDBA” or “SYSOPER”.

This evidence, which was no longer returning an error for using incorrect credentials, represented a symptom that the TA had plausibly obtained valid credentials for access to the database.

**SYSDBA and SYSOPER**“SYSDBA” and “SYSOPER” are administrative privileges that are required to perform administrative operations such as creating, starting, stopping, backing up, or restoring the database. These privileges allow access to a database instance even when the database is not open. Control of these privileges is then completely outside of the database itself, allowing an administrator who is granted one of these privileges to also connect to the database instance to launch it.

This code gave the TA the hint needed to access the database, in fact, the next login attempt was successful, as evidenced in the following raw log, in which the return action code is “STATUS:[1] ‘0’”, which in Oracle is a status of success:

{“EventData”:{“Data”:”LENGTH: ‘183’ ACTION :[7] ‘CONNECT’ DATABASE USER:[3] ‘SYS’ PRIVILEGE :[6]
‘SYSDBA’ CLIENT USER:[13] ‘Administrator’ CLIENT TERMINAL:[15] ‘WIN-2P3KK7923EM’ STATUS:[1] ‘0’
DBID:[10] ‘1407890857’ “,”Binary”:””}}

It is important to note that, the Oracle Database logs on the server were affected by the encryption activity performed by the TA, making it impossible to investigate them further.

After this successful attempt, the very next evidence revealed the creation of the file *“test3.bat”* as shown below.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x26.jpg)

*Evidence of the creation of the “test3.bat” file*

* **TECHNIQUES USED:** External Jobs Execution, WSMan, encoded Powershell commands, reverse shell

It should be noted that, although there are sev...