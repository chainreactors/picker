---
title: Extracting Account Connectivity Credentials (ACCs) from Symantec Management Agent (aka Altiris)
url: https://www.mdsec.co.uk/2024/12/extracting-account-connectivity-credentials-accs-from-symantec-management-agent-aka-altiris/
source: Penetration testing Archives - MDSec
date: 2024-12-04
fetch_date: 2025-10-06T19:44:10.047205
---

# Extracting Account Connectivity Credentials (ACCs) from Symantec Management Agent (aka Altiris)

* Our Services
* Knowledge Centre
* [About](https://www.mdsec.co.uk/about/)
* [Contact](https://www.mdsec.co.uk/contact/)

* Our Services
  + [Adversary Simulation](https://www.mdsec.co.uk/our-services/adversary-simulation/)
  + [Application Security](https://www.mdsec.co.uk/our-services/application-security/)
  + [Penetration Testing](https://www.mdsec.co.uk/our-services/penetration-testing/)
  + [Response](https://www.mdsec.co.uk/our-services/response/)
* Knowledge Centre
  + [Insights](https://www.mdsec.co.uk/knowledge-centre/insights/)
  + [Research](https://www.mdsec.co.uk/knowledge-centre/research/)
  + [Training](https://www.mdsec.co.uk/knowledge-centre/training/)
* [About](https://www.mdsec.co.uk/about/)
* [Contact](https://www.mdsec.co.uk/contact/)

* [![Adversary](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-adversary.svg)

  ## Adversary Simulation

  Our best in class red team can deliver a holistic cyber attack simulation to provide a true evaluation of your organisation’s cyber resilience.](https://www.mdsec.co.uk/our-services/adversary-simulation/)
* [![Application Security](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-application-security.svg)

  ## Application Security

  Leverage the team behind the industry-leading Web Application and Mobile Hacker’s Handbook series.](https://www.mdsec.co.uk/our-services/applicaton-security/)
* [![Penetration Testing](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-penetration-testing.svg)

  ## Penetration Testing

  MDSec’s penetration testing team is trusted by companies from the world’s leading technology firms to global financial institutions.](https://www.mdsec.co.uk/our-services/penetration-testing/)
* [![Response](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-response.svg)

  ## Response

  Our certified team work with customers at all stages of the Incident Response lifecycle through our range of proactive and reactive services.](https://www.mdsec.co.uk/our-services/response/)

* [## Research

  MDSec’s dedicated research team periodically releases white papers, blog posts, and tooling.](https://www.mdsec.co.uk/knowledge-centre/research/)
* [## Training

  MDSec’s training courses are informed by our security consultancy and research functions, ensuring you benefit from the latest and most applicable trends in the field.](https://www.mdsec.co.uk/knowledge-centre/training/)
* [## Insights

  View insights from MDSec’s consultancy and research teams.](https://www.mdsec.co.uk/knowledge-centre/insights/)

ActiveBreach

# Extracting Account Connectivity Credentials (ACCs) from Symantec Management Agent (aka Altiris)

[Home](https://www.mdsec.co.uk/) >
[Knowledge Centre](https://www.mdsec.co.uk/knowledge-centre/) >
[Insights](https://www.mdsec.co.uk/knowledge-centre/insights) >
Extracting Account Connectivity Credentials (ACCs) from Symantec Management Agent (aka Altiris)

# Introduction

On a recent Red Team for a particularly hardened client, we were looking to escalate our privileges in order to move off the endpoint and pivot into the server subnets. When none of the usual paths bore fruit, we began to look into the management software installed on the endpoint, specifically Symantec Management Agent (previously known as “Altiris”). Indeed this was something we had run into [before](https://www.mdsec.co.uk/2022/07/altiris-methods-for-lateral-movement/) and were keen to see what could be done from a privilege escalation perspective.

Reviewing the online [documentation](https://knowledge.broadcom.com/external/article/194234/how-to-setup-agent-connectivity-credenti.html) revealed the use of a “Account Connectivity Credential (ACC)”. This account is used to facilitate network access to the Symantec Site Server in order to download package, policy and task configuration data. This immediately reminded us of another three letter acronym used to perform an almost identical task within Microsoft SCCM, the Network Access Account (NAA).

Security risks associated with Network Access Accounts are well established, thanks to excellent [research](https://blog.xpnsec.com/unobfuscating-network-access-accounts/) by Adam Chester and C# tooling such as a [SharpSCCM](https://github.com/Mayyhem/SharpSCCM) by Chris Thompson.

Given the frequency with which we see overly privileged SCCM NAAs on engagements, we set off to identify how the Symantec Management Agent ACC was configured, how it was delivered to the endpoint and if it was possible to extract the credentials.

To skip straight to the tool, go [here](https://github.com/mdsecactivebreach/evilaltiris).

### Symantec Management Platform Infrastructure

The Symantec Management Platform has four main architectural components as detailed [here](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/it-management-suite/ITMS/Getting-Started/Understanding-the-components-of-IT-Management-Suite/core-architectural-components-of-symantec-manageme-v54482933-d780e968.html)

* Notification Server and its Web-based Symantec Management Console
* SQL Server
* Site servers (can include task servers, package servers, network boot servers, and monitor service).
* Managed computers

A high-level infrastructure diagram from Symantec can be seen below. For our purposes, we assume we have already compromised a managed computer with the Symantec Management Agent installed.

![](https://www.mdsec.co.uk/wp-content/uploads/2024/12/original-1.jpg)

### Symantec Management Agent ACC Account Configuration

During installation of our lab environment, we are prompted to enter the account credentials for the Notification Server account.

![](https://www.mdsec.co.uk/wp-content/uploads/2024/12/Screenshot_from_2024-03-29_18-22-37-1-960x527.jpg)

According to the [documentation](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/it-management-suite/ITMS/Administration/Configuring-Notification-Server/configuring-notification-server-settings-v15701619-d846e35732/notification-server-processing-settings-v11802974-d846e35883.html#v11802974), this account **must** have local administrator rights on the Notification Server.

![](https://www.mdsec.co.uk/wp-content/uploads/2024/12/image-1-960x347.jpg)

By default, these credentials will also be used as the ACC unless we explicitly configure one inside the web admin portal under `Settings → Agents/Plug-ins → Symantec Management Agent → Settings → Global Agent Settings`. This means that in a default configuration, the ACC will be set to an account with full administrative rights over the Notification Server. These credentials can also be used to access the admin console at URL `https://notification-server.local/Altiris/console` with full admin rights.

We can see here that Symantec warn us about the potential security risks associated with this and instead suggest we configure a low-privileged account. Problem solved! surely no-one would use the product in its default configuration?

![](https://www.mdsec.co.uk/wp-content/uploads/2024/12/Screenshot_from_2024-04-17_11-16-24-1-960x318.jpg)

With an understanding of how the ACC is configured, and the prospect of capturing credentials for a highly privileged account, we can move on to figuring out how the ACC is sent to the agents.

### Overview of the Agent Enrollment Process

To understand how the ACC is distributed, we must first understand a bit about how the agent enrollment process works.

As the agent communications occurs over HTTP(S), we can simply install the agent using the MSI installer and run Wireshark to observe the traffic. Although the agent installer does support HTTP proxies, running the agent traffic via Burp during installation created unexpected results. To view HTTPS communications, we can simply add the private key from the Notification Server SSL certificate to decrypt the traffic.

While installing the agent, we observe a HTTP r...