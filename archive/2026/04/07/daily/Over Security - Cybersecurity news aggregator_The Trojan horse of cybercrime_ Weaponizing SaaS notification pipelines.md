---
title: The Trojan horse of cybercrime: Weaponizing SaaS notification pipelines
url: https://blog.talosintelligence.com/weaponizing-saas-notification-pipelines/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-07
fetch_date: 2026-04-08T04:38:54.748678
---

# The Trojan horse of cybercrime: Weaponizing SaaS notification pipelines

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/phishing-evergreen.jpg)

# The Trojan horse of cybercrime: Weaponizing SaaS notification pipelines

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Tuesday, April 7, 2026 06:00

[SecureX](/category/securex-3/)
[Threat Spotlight](/category/threat-spotlight/)

*By Diana Brown*

* Cisco Talos has recently observed an increase in activity that is leveraging notification pipelines in popular collaboration platforms to deliver spam and phishing emails.
* These emails are transmitted using the legitimate mail delivery infrastructure associated with GitHub and Jira, minimizing the likelihood that they will be blocked in transit to potential victims.
* By taking advantage of the built-in notification functionality available within these platforms, adversaries can more effectively circumvent email security and monitoring solutions and facilitate more effective delivery to potential victims.
* In most cases, these campaigns have been associated with phishing and credential harvesting activity, which is often a precursor to additional attacks once credentials have been compromised and/or initial access has been achieved.
* During one campaign conducted on Feb. 17, 2026, approximately 2.89% of the emails observed being sent from GitHub were likely associated with this abuse activity.

## Platform abuse, social engineering, and SaaS notification hijacking

Recent telemetry indicates an increase in threat actors leveraging the automated notification infrastructure of legitimate Software-as-a-Service (SaaS) platforms to facilitate social engineering campaigns. By embedding malicious lures within system-generated commit notifications, attackers bypass traditional reputation-based email security filters. This Platform-as-a-Proxy (PaaP) technique exploits the implicit trust organizations place in traffic originating from verified SaaS providers, effectively weaponizing legitimate infrastructure to bypass standard email authentication protocols. Talos' analysis explores how attackers abuse the notification pipelines of platforms like GitHub and Atlassian to facilitate credential harvesting and social engineering.

### The PaaP model

The core of this campaign relies on the abuse of SaaS features to generate emails. Because the emails are dispatched from the platform's own infrastructure, they satisfy all standard authentication requirements (SPF, DKIM, and DMARC), effectively neutralizing the primary gatekeepers of modern email security. By decoupling the malicious intent from the technical infrastructure, attackers successfully deliver phishing content with a "seal of approval" that few security gateways are configured to challenge.

### Anatomy of GitHub campaign: Abusing automated notification pipelines

The GitHub vector is a pure "notification pipeline" abuse mechanism. Attackers create repositories and push commits with payloads embedded in the commit messages. The User Interface Mechanism has two fields for text input: one is a mandatory summary, a single limited line, where the user provides a high-level overview of the change. Attackers weaponize this field to craft the initial social engineering hook, ensuring the malicious lure is the most prominent element of the resulting automated notification. The second field is an optional, extended description that allows for multi-line, detailed explanations. Attackers abuse this to place the primary scam content, such as fake billing details or fraudulent support numbers.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/image002.png)

Figure 1: Email header

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/image003.png)

Figure 2: The body of the message

By pushing a commit, the attacker triggers an automatic email notification. GitHub’s system is configured to notify collaborators of repository activity. Because the content is generated by the platform’s own system, it avoidssecurity flags. In this example, we can see the details of the commit followed by the scam message. At the bottom of the email, we have the mention of the subscription, buried at the very bottom of the page.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/image004.png)

Figure 3: List-Unsubscribe link

The chain of Received headers shows the message entering the system from “out-28[.]smtp[.]github[.]com” (IP “192[.]30[.]252[.]211”). This is a known legitimate and verified GitHub SMTP server.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/image005.png)

Figure 4: Raw headers

The email contains a DKIM-Signature with “d=github[.]com”. This signature was successfully verified by the receiving server (“esa1[.]hc6633-79[.]iphmx[.]com”), proving that the email was sent by an authorized GitHub system and was not tampered with in transit. Telemetry collected over a five-day observation period indicates that 1.20% of the total traffic originating from “noreply[@]github[.]com” contained the "invoice" lure in the subject line. On the peak day of Feb. 17, 2026, this volume spiked to approximately 2.89% of the daily sample set.

### Abusing workflow and invitation logic (Jira)

The Jira vector does not rely on a notification pipeline in the traditional sense. Jira notifications are expected in corporate environments. An email from Atlassian is rarely blocked, as it is often critical for internal project management and IT operations. The abuse here is not a "pipeline" of activity, but an abuse of the collaborative invitation feature.

Attackers do not have access to modify the underlying HTML/CSS templates of Atlassian’s emails. Instead, they ...