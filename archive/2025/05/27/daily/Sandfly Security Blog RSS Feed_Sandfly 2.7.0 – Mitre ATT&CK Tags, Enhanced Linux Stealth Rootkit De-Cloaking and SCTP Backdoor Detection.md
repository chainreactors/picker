---
title: Sandfly 2.7.0 – Mitre ATT&CK Tags, Enhanced Linux Stealth Rootkit De-Cloaking and SCTP Backdoor Detection
url: https://sandflysecurity.com/blog/sandfly-2-7-0-mitre-attck-tags-enhanced-linux-stealth-rootkit-de-cloaking-and-sctp-backdoor-detection
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:28:01.511732
---

# Sandfly 2.7.0 – Mitre ATT&CK Tags, Enhanced Linux Stealth Rootkit De-Cloaking and SCTP Backdoor Detection

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 2.7.0 – Mitre ATT&CK Tags, Enhanced Linux Stealth Rootkit De-Cloaking and SCTP Backdoor Detection

04 August 2020

Product Update

Sandfly 2.7.0 is now out and features some significant upgrades.

* Sandfly modules now are tagged with Mitre ATT&CK categories and tactics.
* We are able to completely decloak even more hidden processes with Linux Loadable Kernel Module (LKM) rootkits.
* We are able to detect and report on SCTP backdoors and variants.
* Other Sandfly modules added to search for suspicious file permissions, malicious history file usage, SSH misconfiguration and more.

## Mitre ATT&CK Tags

All Sandfly modules now have tagging which includes [Mitre ATT&CK](https://attack.mitre.org/) categorizations and tactics. The tagging is also customizable by users that are creating their own Sandfly checks. Sandfly tags follow the data when alerts are reported so they are visible and searchable inside tools like Kibana and Splunk. Below is a Kibana tag cloud tied into history file tampering with Mitre ATT&CK tags.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Mitre ATT&CK Tags and Sandfly](https://www.datocms-assets.com/56687/1635216291-attack-history-alert.png?auto=format&dpr=2&q=60&w=920 "Mitre ATT&CK Tags and Sandfly")

All tactic areas are covered where appropriate along with tactic ID if applicable such as:

* Initial Access
* Defense Evasion
* Execution
* Credential Access
* Discovery
* Persistence
* Privilege Execution
* etc.

Each Sandfly module will have both the high-level category and Mitre ATT&CK ID in their tagging which can be searched and reported on inside Kibana and Splunk.

## Decloaking Diamorphine and Reptile Stealth Rootkits

Sandfly has had mechanisms to detect Loadable Kernel Module (LKM) rootkits on Linux since version 1.x. In particular we are able to spot file system inconsistencies which show an LKM rootkit is active. With version 2.7.0 we have taken this a step further by enhancing our decloaking to completely reveal any process that is being hidden by the Diamorphine or Reptile rootkits.

The Diamorphine and Reptile rootkits are the most easily used and deployed LKM style rootkits on Linux and share a lot of similarities in how they hide on a host system. Sandfly can find any process hidden with them or their derivatives. On top of this, we are also able to run these decloaked processes through other signatures to enhance detection and reveal more about what may be going on with the system. Below is one example of decloaking the Reptile rootkit backdoor process:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Decloaked Reptile Rootkit Process on Linux](https://www.datocms-assets.com/56687/1635216299-reptile-hidden-shell.png?auto=format&dpr=2&q=60&w=920 "Decloaked Reptile Rootkit Process on Linux")

## SCTP Network Protocol Checks

SCTP is protocol that provides reliable transport like TCP. However, it is rarely used except in some specialized telecom applications. Yet for attackers, it can be used to hop over poorly configured firewalls or bypass network monitoring systems that are not enabled to look for it. As a result, the SCTP protocol can be a favorite backdoor method for attackers and Red Teams looking to quietly slip around unnoticed.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SCTP Backdoor Running from Linux /tmp Directory](https://www.datocms-assets.com/56687/1635216310-sctp-running-from-tmp.png?auto=format&dpr=2&q=60&w=920 "SCTP Backdoor Running from Linux /tmp Directory")

Sandfly has now added full SCTP socket decoding to spot not just programs using the SCTP protocol (which is in itself suspicious), but also identical attack types that are done with TCP/UDP protocols such as backdoors, suspicious server locations and so on. These new checks essentially duplicate the standard checks we’ve been doing for TCP/UDP/ICMP and Raw network sockets from the very beginning.

## Malicious or Suspicious Linux User Command History

Sandfly will now look inside user history files for commands that are suspicious or malicious in nature. If we find anything that needs attention, we will capture the offending entries and present them to you for analysis and review. This feature can catch a lot of attackers off-guard if they do not clean their history files correctly.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Detecting Malicious Commands in User History on Linux](https://www.datocms-assets.com/56687/1635216317-sandfly-user-history-malicious.png?auto=format&dpr=2&q=60&w=920 "Sandfly Detecting Malicious Commands in User History on Linux")

## File Permission Risk Checks Expanded

We have expanded the files and directories we investigate for file permission risks that can compromise a system’s security. We will for instance investigate the */etc* directory system configuration and boot scripts to be sure they are secure and not modified with permissions that can allow an intruder to easily escalate privileges or embed backdoors.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Risky File Permission Detected in /etc on Linux](https://www.datocms-assets.com/56687/1635216325-sandfly-file-permissions-risk-etc-dir.png?auto=format&dpr=2&q=60&w=920 "Risky File Permission Detected in /etc on Linux")

## Socat Backdoor Checks Expanded

We have expanded and improved the number and types of backdoors detected using the socat network socket utility. *Socat* is a powerful network utility that can be legitimate, but can also be used to bypass network controls and setup backdoors to allow remote exploitation. We have enhanced the varieties of backdoors we are detecting and also general flagging of *socat* processes that may be running.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Detecting socat Reverse Bindshell Backdoor on Linux](https://www.datocms-assets.com/56687/1635216332-process-backdoor-bindshell-revserse-socat.png?auto=format&dpr=2&q=60&w=920 "Sandfly Detecting socat Reverse Bindshell Backdoor on Linux")

## User History File Grabbing for Incident Response

We now have an Incident Response (IR) module that will specifically grab a user’s history file from a remote system. This module can also be used as a *Recon* Sandfly to grab user history files for storage in a central Elasticsearch or Splunk database for searching and historical review. The module is able to grab all user history files on the remote system without any other input from the operator. This module is excellent for performing a manual IR review of users to see if they were doing anything suspicious or unusual that left behind commands in their history.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Grabbing Linux User History Files for Incident Response](https://www.datocms-assets.com/56687/1635216340-sandfly-user-history-data.png?auto=format&dpr=2&q=60&w=920 "Grabbing Linux User History Files for Incident Response")

## Suspicious or Risky SSH Server Features Enabled

We have new modules to help search for SSH servers that have unusual or risky features enabled such as:

* root login enabled
* TCP port forwarding enabled
* Tunneling enabled
* Gateway ports enabled
* Agent forwarding enabled

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH TCP Port Forwarding Enabled Security Risk Detected](https://www.datocms-assets.com/56687/1635216347-ssh-enabled-tcp-forwarding-1.png?auto=format&dpr=2&q=60&w=920 "SSH TCP Port Forwarding Enabled Security Risk Detected")

These checks will vary by enterprise depending on what you consider a risk so these modules have been made *Incident Response* types. However, you can qu...