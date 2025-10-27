---
title: ESXiArgs: The code behind the ransomware
url: https://www.trustedsec.com/blog/esxiargs-the-code-behind-the-ransomware/
source: TrustedSec
date: 2023-02-09
fetch_date: 2025-10-04T06:09:58.161944
---

# ESXiArgs: The code behind the ransomware

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [ESXiArgs: The code behind the ransomware](https://trustedsec.com/blog/esxiargs-the-code-behind-the-ransomware)

February 08, 2023

# ESXiArgs: The code behind the ransomware

Written by
Scott Nusbaum

Incident Response
Incident Response & Forensics

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ESXiArgsCode_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695565110&s=902bca2392c03303af5a2c3905de1c79)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#c3fcb0b6a1a9a6a0b7fe80aba6a0a8e6f1f3acb6b7e6f1f3b7abaab0e6f1f3a2b1b7aaa0afa6e6f1f3a5b1acaee6f1f397b1b6b0b7a6a790a6a0e6f1f2e5a2aeb3f8a1aca7bafe86909baa82b1a4b0e6f082e6f1f397aba6e6f1f3a0aca7a6e6f1f3a1a6abaaada7e6f1f3b7aba6e6f1f3b1a2adb0acaeb4a2b1a6e6f082e6f1f3abb7b7b3b0e6f082e6f185e6f185b7b1b6b0b7a6a7b0a6a0eda0acaee6f185a1afaca4e6f185a6b0bbaaa2b1a4b0eeb7aba6eea0aca7a6eea1a6abaaada7eeb7aba6eeb1a2adb0acaeb4a2b1a6 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fesxiargs-the-code-behind-the-ransomware "Share on Facebook")
* [Share on X](http://twitter.com/share?text=ESXiArgs%3A%20The%20code%20behind%20the%20ransomware%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fesxiargs-the-code-behind-the-ransomware "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fesxiargs-the-code-behind-the-ransomware&mini=true "Share on LinkedIn")

## 1 Deep Dive into an ESXi Ransomware

TrustedSec’s Nick Gilberti wrote a great blog covering the ESXi ransomware’s shell script [here](https://trustedsec.com/blog/esxiargs-what-you-need-to-know-and-how-to-protect-your-data). However, in this blog, we are going to dive a little deeper into the code behind this ransomware. The sample ransomware discussed was acquired from [VirusTotal and Bleeping Computers forum.](https://www.virustotal.com/gui/file/10c3b6b03a9bf105d264a8e7f30dcab0a6c59a414529b0af0a6bd9f1d2984459) The following is a list of the parts of the malware, and each part will be discussed in its own section.

* Initial Compromise
* Public PEM File
* Shell Script
* Executable
* Ransom Notes

### 1.1 Initial Compromise

Like most ransomware samples, the ESXi ransomware is basic. It contains multiple files, but none of them are obfuscated or contain much in the way of anti-forensics. In this case, there are no attempts to hide what the code does. The shell script is in plaintext and even contains comments. The malicious ELF file was not even stripped of its function names. The reason behind this is because at the point when the attackers are ready to launch the ransomware on the system, they already have complete control over that system; in this case, they are operating as the **root** user. This means that any protections that could have been enabled on the system have been removed. There are several different ways that attackers can gain access to the system, but the common theme is that they must obtain root or compromise a user who has access to the ESXi tools.

### 1.2 Public PEM file

Multiple files are dropped into the ***/tmp/*** directory during the initial compromise; the first among these is the ***public.pem*** file. The ***encrypt*** executable will read in this file and encrypt the target files based on the public key contained within. To decrypt the files, the attackers must be able to provide a private key that is paired to the public.

In most ransomware attacks, the attacker creates a key or multiple keys for each target organization. Some will use multiple keys and encrypt sensitive documents or systems with a different key in order to charge a higher price for the decryption key. In this case, the same key is used to encrypt each component of the ESXi system. This means that the same decryption key can be used to recover each of these components. It also means that if the attackers use the same key against multiple companies, the same decryption key should work.

#### 1.2.1 Analysis of the Shell Script

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Nusbaum_ESXI_1.png)

The second file of interest located in the ***/tmp/*** directory is encrypt.sh. This is a shell script file used to perform most of the work to identify what files to encrypt. See Nick’s blog for details about what this script does. We will focus on the encrypt section of the ***encrypt.sh file***, which searches for specific files to encrypt. This is done using a combination of ESXi tools and basic Linux commands. The ***esxcli*** is used to find the location of each volume.

The script starts of...