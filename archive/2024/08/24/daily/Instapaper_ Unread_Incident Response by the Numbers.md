---
title: Incident Response by the Numbers
url: https://www.paloaltonetworks.com/blog/?p=327482
source: Instapaper: Unread
date: 2024-08-24
fetch_date: 2025-10-06T18:07:08.193911
---

# Incident Response by the Numbers

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Announcement](https://www.paloaltonetworks.com/blog/category/announcement/)
* Incident Response by the ...

# Incident Response by the Numbers

Link copied

By [Michael J Graven](/blog/author/michael-j-graven/ "Posts by Michael J Graven")

Aug 22, 2024

8 minutes

[Announcement](/blog/category/announcement/)

[Unit 42](/blog/category/unit42/)

[incident response report](/blog/tag/incident-response-report/)

## Key Insights from Unit 42’s 2024 Incident Response Report

In the past year, we’ve seen threat actors making bigger moves faster to mount more sophisticated attacks against their targets.

As we helped hundreds of clients assess, respond and recover from attacks, we collected data about those attacks and compiled them into our [2024 Incident Response (IR) Report](/resources/research/unit-42-incident-response-report).

Here are the data points that tell the story of last year's attacks and the steps defenders can take to protect their organizations.

## To Block Attacks, Lock Down the Vectors

Attack vectors are the avenues by which attackers penetrate your organization’s defenses. Understanding how attackers get in can show you where to place controls to stop them.

The three most popular initial attack vectors we identified:

1. Software and API vulnerabilities: 38.6% of cases
2. Previously compromised credentials: 20.5% of cases
3. Social engineering and phishing: 17% of cases

Shoring up these weak points is no easy task, and it requires a combination of tools, expertise and routine processes.

### Exploiting Software and API Vulnerabilities

Last year, software and API vulnerabilities provided the initial access vectors for 38.6% of attacks we investigated – more than any other vector.

These attacks result from large-scale, automated intrusion campaigns. Often, attacks targeted key parts of the software supply chain, like Apache’s Log4j logging framework and Oracle’s WebLogic server, affecting governments, banks, shipping companies, airlines and others.

The IR Report demonstrates that these types of exploits are not anomalies. Instead, they represent an attack trend. [A proactive patch management program](/cyberpedia/vulnerability-management) is key to addressing realized vulnerabilities promptly and anticipating future vulnerabilities based on trends and threat intelligence.

The challenge lies in an uncomfortable truth – vulnerabilities are discovered at a far greater rate than teams’ ability to patch them. [Thousands of vulnerabilities are reported each year](https://www.ncsc.gov.uk/collection/vulnerability-management/understanding-vulnerabilities), and each patch should be tested before being deployed in your environment.

Two of the top five [Common Vulnerabilities and Exposures (CVEs)](/blog/security-operations/playbook-of-the-week-using-cves-in-incident-investigation/) exploited in 2023 were identified years before that (2020 and 2021), which illustrates a significant lag in patching known vulnerabilities.

##### **Detecting vulnerabilities isn’t enough. Teams must be able to prioritize the most critical vulnerabilities and implement defenses to mitigate lower-priority vulnerabilities.**

### Continued Use of Previously Compromised Credentials

Previously compromised credentials provided the initial access vector in 20.5% of cases we investigated – a 5x rise over the past two years.

Compromised credentials overtook phishing and social engineering as an attack vector, and there is a persistent and active black market for them.

Good hygiene can limit the damage potential of stolen credentials, but controls must go beyond strong passwords and multifactor authentication (MFA).

* **Secure Credential Storage**: Teams should store credentials using encryption and secret management solutions.
* **Credential Rotation**: Rotating credentials can help minimize the likelihood of an attacker having success using previously compromised ones.
* **Least-Privileged Access**: [The principle of least privilege](/cyberpedia/what-is-least-privilege-access) limits the damage incurred from compromised credentials by ensuring each staff member doesn’t have excessive access beyond what they need to do their jobs.
* **Audit Logging**: Audits of credential use can uncover potentially compromising activities and help comply with reporting standards.

As cybercriminal tactics evolve, teams must implement more dynamic and responsive security controls and policies. These include regular security audits, real-time threat detection and training programs aimed at credential-threat risk recognition and mitigation.

##### **It’s equally important to recognize the anomalous and suspicious behavior that follows the use of compromised credentials.**

As attackers act with greater sophistication and subtlety, AI and machine learning are becoming vital to detect attack patterns early and position defenders to respond with precision.

### Targeted Social Engineering and Phishing

Previously, social engineering and phishing were the top attack vectors, accounting for 17% of the attacks we investigated last year.

Our experience shows that [social engineering and phishing](/cybersecurity-perspectives/social-engineering-and-the-art-of-fishing) attacks are increasingly aimed at the IT help desk rather than employees themselves. Attackers will call the target’s help desk and impersonate a real employee, asking for help with resetting their password or with changing the phone number associated with an account.

Defending against human nature is still the hardest task. Often, admins prove just as susceptible to phishing attacks as other team members. That’s because high-performing organizations are built on people helping one another. We go against our own goals and self-interest when we ask people not to trust or help each other.

##### A multilayered defense slows attackers down, creates more opportunities for them to make mistakes, and gives your team the upper hand.

* Train IT and admin staff to recognize and respond to phishing attempts.
* Perform continuous authentication and monitoring of communication channels.
* Encourage employees to question anomalies and report suspicious behavior.

## Evolving Malware Capabilities

In 2023, malware was implicated in 56% of all documented security incidents, with ransomware accounting for 33% of these cases.

We found a few noteworthy shifts in the details:

* Attackers are more frequently using data destruction tactics with wipers and other tools and techniques.
* About 42% of our investigations involved a backdoor, while 32% of malware-related matters had some kind of interactive C2 software. In 12% of cases, attackers used web shells to use a compromised server as a beachhead into an environment. These tactics afford intruders a foothold from which they can covertly conduct a wide range of malicious activity.
* Reverse tunnels are a favored technique among attackers. These connections lead out of the target environment and terminate on a system under the attacker’s control. This allows attackers more freedom without needing to install malware on the target system.
* Many operating systems have built-in support for encrypted tunnels that hackers can exploit. For example, the vast majority (85%) of organizations still leave Microsoft Remote Desktop exposed to the internet for [at least 25% of the month](/resources/research/2023-unit-42-attack-surface-threat-report).

##### **Organizations need more** [**comprehensive monitoring systems**](/cyberpedia/siem-solutions-in-soc) **that detect and counteract stealthy infiltrations through backdoors and encrypted channels.**

Comprehensive monitoring includes advanced threat detection technologies that analyze behaviors and patterns, integrate endpoint protection, and employ decryption capabilities to identify hidden exploits.

## Speed Matters

One of the biggest ...