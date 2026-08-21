---
title: UAT-10147: Chinese-speaking adversary integrates agentic AI into post-compromise operations
url: https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/
source: Over Security
date: 2026-08-20
fetch_date: 2026-08-21T03:04:57.532751
---

# UAT-10147: Chinese-speaking adversary integrates agentic AI into post-compromise operations

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-0.jpg)

# UAT-10147: Chinese-speaking adversary integrates agentic AI into post-compromise operations

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Thursday, August 20, 2026 06:00

[Threat Spotlight](/category/threat-spotlight/)
[AI](/category/ai/)

* Cisco Talos identified UAT-10147 targeting Windows and Linux web servers globally, impacting organizations in government, education, media, technology, and gaming sectors. The actor leveraged publicly disclosed vulnerabilities to gain initial access at scale.
* UAT-10147 integrated AI-driven tooling into exploitation, reconnaissance, payload generation, validation, and persistence workflows. Talos observed AI-generated operational playbooks, exploit automation scripts, and troubleshooting logic supporting real-world intrusions.
* The actor employed a mixture of open-source offensive frameworks, including Metasploit, ysoserial, PentestGPT, DeepAudit, and multiple privilege escalation exploits to automate intrusion operations and establish persistence.
* Talos assesses that integrating AI-generated exploitation guidance, automation, and validation workflows enables threat actors to scale complex attacks more efficiently while reducing the expertise traditionally required for advanced post-compromise operations.

---

In early 2026, Cisco Talos discovered a Chinese-speaking cybercrime group, tracked as UAT-10147, that targets a wide range of vulnerable web servers. The group engages in multiple criminal activities, including search engine optimization (SEO) fraud and data theft.

This blog post provides an overview of the campaign, examining the countries affected and the potential impact of BadIIS infections. It also outlines UAT-10147's attack chain and post-compromise tactics.

Talos assesses with moderate-to-high confidence that UAT-10147 is among an emerging class of financially motivated intrusion operators leveraging agentic AI systems to operationalize offensive tradecraft at scale. Unlike traditional use of generative AI for simple scripting assistance, the actor demonstrated:

* Iterative exploit refinement
* Adaptive troubleshooting
* Post-exploitation automation
* Exploit validation workflows
* Operational documentation generation

This indicates a transition from AI-assisted scripting toward semi-autonomous offensive orchestration.

## Victimology

UAT-10147 targeted high-value internet-exposed web servers across multiple regions. Talos’ investigation shows affected servers located in Brazil, Bolivia, China, Canada, and Vietnam. These systems belong to organizations in sectors including government, universities, media, technology, and gaming.

From the threat actor’s command-and-control (C2) server open directory, we also identified a target list containing approximately 170,000 URLs stored in a text file. The actor appears aware that scanning the entire list at once is inefficient and time consuming. To improve performance, they split the large list into 17 files, each containing about 10,000 URLs. Additionally, the threat actor uses the letter “w” as a reference to the Chinese character “萬,” which represents 10,000.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-1.png)

Figure 1. Commands to split the large list.

Figure 2 shows the distribution of the target list across countries based on the IP addresses resolved from the 170,000 URLs.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-2.jpg)

Figure 2. Distribution of target list across countries.

## UAT-10147 OPSEC failure

Talos identified this activity after observing a compromised machine communicating with a download server hosted at “139.180.197[.]150”. A review of this IP address revealed an open directory. Below provides a high-level view of this directory listing.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Untitled-1-3.png)

Figure 3. Open directory on download site.

## Attack summary

Talos observed that the threat actor uses multiple methods to gain initial access to a victim’s network. After successfully achieving remote code execution (RCE) on a website or otherwise gaining access to the server, the actor typically runs an automated script to install and deploy malware for SEO fraud or data stealing. In some cases, the attacker instead installs a web shell, which allows them to manually set up the BadIIS malware and establish persistence through additional backdoor deployment.

### Windows platform infection chain

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-4.jpg)

Figure 4. Windows infection chain.

The attack uses multiple Windows batch scripts to carry out its objectives. Although some versions of the scripts contain minor variations, these differences do not affect the overall purpose. The following section highlights the primary batch files observed during the attack.

The main script is executed after the threat actor obtains RCE or establishes an implant on the victim’s web server. It is commonly named “back.txt” or “back.bat”. This code represents a multi-stage malware deployment script that utilizes certutil to download a privilege escalation tool (EfsPotato, renamed as “prcc1.rar”), a secondary batch script (“bai.bat”), and the [QuasarRAT](https://github.com/quasar/Quasar) payload (disguised as “svchosts.exe”). Using the [EfsPotato](https://github.com/zcgonvh/EfsPotato) tool to gain elevated system privileges, the script modifies the Windows Registry and uses PowerShell to add specific directories to the Windows Defender exclusion list, effectively hiding the malware from an...