---
title: Learning From the Past — Ten 2022 Cybersecurity Events to Know
url: https://www.paloaltonetworks.com/blog/2022/12/unit42-cybersecurity-events-2022/
source: Palo Alto Networks Blog
date: 2022-12-30
fetch_date: 2025-10-04T02:46:30.375205
---

# Learning From the Past — Ten 2022 Cybersecurity Events to Know

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Must-Read Articles](https://www.paloaltonetworks.com/blog/security-operations/category/must-read-articles/)
* Learning From the Past — ...

# Learning From the Past — Ten 2022 Cybersecurity Events to Know

Link copied

By [Unit 42](/blog/author/unit-42/ "Posts by Unit 42")

Dec 29, 2022

7 minutes

[Must-Read Articles](/blog/security-operations/category/must-read-articles/)

[Points of View](/blog/category/points-of-view/)

[Container Security](/blog/tag/container-security/)

[cybersecurity](/blog/tag/cybersecurity/)

[malware](/blog/tag/malware/)

[ransomware](/blog/tag/ransomware/)

[Russia](/blog/tag/russia/)

[trends](/blog/tag/trends/)

[Ukraine](/blog/tag/ukraine/)

[Unit 42](/blog/tag/unit-42/)

This post is also available in:
[日本語 (Japanese)](https://www.paloaltonetworks.com/blog/2023/01/unit42-cybersecurity-events-2022/?lang=ja)

While it might seem counterintuitive to revisit last week’s newspaper for valuable information, “Those who cannot remember the past are condemned to repeat it.” Stepping back to recollect the security events from the recent past is particularly important, as the risk of repeating past mistakes is particularly high. Last year’s most popular posts on the [Unit 42 Threat Research blog](https://unit42.paloaltonetworks.com/) let us examine what the events of 2022 can tell us about the year to come.

Threat actors are tremendously fond of recycling and reusing old techniques, as long as they continue to have a high rate of return. And as past incidents have shown us, these tricks can be useful for years, if people don’t apply appropriate patches and mitigations.

## All Eyes on Eastern Europe

![](/blog/wp-content/uploads/2022/12/word-image-177517-1.jpeg)

### Threat Brief: Ongoing Russia and Ukraine Cyber Activity

Even before the beginning of the recent events starting in February 2022, there was significant cybersecurity activity in Eastern Europe. Beginning on Jan. 14, 2022, reports began emerging about a series of [**attacks targeting Ukrainian government websites**](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/). As a result of these attacks, numerous government websites were either defaced or inaccessible. As a result, the government of Ukraine [formally accused Russia](https://thehackernews.com/2022/01/ukrainian-government-officially-accuses.html) of masterminding these attacks.

### Russia-Ukraine Cyberattacks: How to Protect Against Related Cyberthreats Including DDoS, HermeticWiper, Gamaredon, Website Defacement, Phishing and Scams

Over the next several weeks, [**Russia-Ukraine cyber activity escalated substantially**](https://unit42.paloaltonetworks.com/preparing-for-cyber-impact-russia-ukraine-crisis/). Beginning on Feb. 15, a series of distributed denial of service (DDoS) attacks commenced. These attacks continued, impacting both the Ukrainian government and banking institutions. On Feb. 23, a new variant of wiper malware, named HermeticWiper, was discovered in Ukraine. Shortly after, a new round of website defacement attacks were also observed impacting Ukrainian government organizations.

### Russia’s Gamaredon aka Primitive Bear APT Group Actively Targeting Ukraine

The [**Gamaredon group**](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/) (aka Trident Ursa, Primitive Bear) is one of the most active, advanced and persistent threats (APT) targeting Ukraine. Given the current geopolitical situation and their specific target focus, Unit 42 continues to actively monitor for indicators of their operations.

In January 2022, Unit 42 researchers were able to map out three large clusters of Gamaredon’s infrastructure used to support different phishing and malware purposes. In further updates in February and June, these clusters were found to link to over 700 malicious domains, 215 IP addresses and over 100 samples of malware. We will continue to provide updates as needed.

### Russian APT29 Hackers Use Online Storage Services, Dropbox and Google Drive

The cybersecurity industry has also long considered [**Cloaked Ursa**](https://unit42.paloaltonetworks.com/cloaked-ursa-online-storage-services-campaigns/) to be affiliated with the Russian government. This aligns with the group’s historic targeting focus, dating back to malware campaigns against Chechnya and other former Soviet bloc countries in 2008.

Campaigns in May 2022 by Cloaked Ursa were initiated with a lure of an agenda for an upcoming meeting with an ambassador. These campaigns are believed to have targeted several Western diplomatic missions between May and June 2022. The lures included in these campaigns suggest targeting a foreign embassy in Portugal, as well as a foreign embassy in Brazil. In both cases, the phishing documents contained a link to a malicious HTML file – [EnvyScout](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/) – that served as a dropper for additional malicious files in the target network, including a Cobalt Strike payload.

## Top Vulnerabilities

![](/blog/wp-content/uploads/2022/12/word-image-177517-2.png)

### New Linux Vulnerability CVE-2022-0492 Affecting Cgroups: Can Containers Escape?

In February, 2022, Linux announced [CVE-2022-0492](https://access.redhat.com/security/cve/cve-2022-0492), a [**new privilege escalation vulnerability in the kernel**](https://unit42.paloaltonetworks.com/cve-2022-0492-cgroups/). CVE-2022-0492 marks a logical bug in control groups ([cgroups](https://man7.org/linux/man-pages/man7/cgroups.7.html)), a Linux feature that is a fundamental building block of containers.

The issue stands out as one of the simplest Linux privilege escalations discovered in recent times. The Linux kernel mistakenly exposed a privileged operation to unprivileged users. Fortunately, the default security hardenings in most container environments are enough to prevent container escape.

### CVE-2022-22965: Spring Core Remote Code Execution Vulnerability Exploited In the Wild (SpringShell)

In March 2022, two vulnerabilities were [**announced within the Spring Framework**](https://unit42.paloaltonetworks.com/cve-2022-22965-springshell/) – an open-source framework for building enterprise Java applications. These vulnerabilities were assigned [CVE-2022-22963](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22963) and [CVE-2022-22965](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22965). The vendor patched these with the release of Spring Cloud Function 3.1.7 and 3.2.3, as well as version 5.3.18 and 5.2.20 of Spring Framework respectively.

The CVE-2022-22965 vulnerability was particularly notable because it allowed an attacker unauthenticated remote code execution (RCE), which Unit 42 had observed being exploited in the wild. The exploitation of this vulnerability could result in a webshell being installed onto the compromised server that would allow further command execution.

### Threat Brief: CVE-2022-30190 – MSDT Code Execution Vulnerability

In May 2022, details began to emerge of malicious **Word documents leveraging remote templates to** [**execute PowerShell**](https://unit42.paloaltonetworks.com/cve-2022-30190-msdt-code-execution-vulnerability/) via the ms-msdt Office URL protocol. The use of this technique appeared to allow attackers to bypass local Office macro policies. It executed code within the context of Word. Microsoft has since released [protection guidance](https://msrc-blog.microsoft.com/2022/05/30/guidance-for-cve-2022-30190-microsoft-support-diagnostic-tool-vulnerability/) and assigned [CVE-2022-30190](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30190) to this vulnerability.

## Top Malware

![](/blog/wp-content/uploads/2022/12/word-image-177517-3.png)

### Threat Assessment: BlackCat Ransomware

[BlackCat (aka ALPHV)](http...