---
title: Making sure the checks get printed
url: https://blog.talosintelligence.com/making-sure-the-checks-get-printed/
source: Over Security
date: 2026-10-08
fetch_date: 2026-10-09T08:12:02.597345
---

# Making sure the checks get printed

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

# Making sure the checks get printed

By
[Pierre Cadieux](https://blog.talosintelligence.com/author/pierre/)

Thursday, October 8, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

My name is Pierre Cadieux, and I’ll be helping contribute to these newsletters. A little about me: I’ve been working in the cybersecurity industry in many roles over the past 20+ years, first focusing on endpoint security, policies, and firewalls, then moving to risk management and compliance, disaster recovery, and investigations. I spent about 15 years as a consultant working across many well-known consultancy firms and eventually moved to Cisco where I spent time doing security operations center (SOC) design and assessments as well as segmentation before moving to the Talos IR team. I spent many years there, first as an Incident Commander and then a manager of our excellent team of global IR consultants and investigators. My current role is with the Talos Threat Intelligence and Interdiction team, where I’m focused on intelligence efficacy — how we can do better with the data we have, how we can get more data, and what our customers want from our intelligence products.

Since it’s Cybersecurity Awareness Month, I wanted to take a few minutes to collectively thank all of the defenders out there for the hard work you do each day. The work you do may not always be visible, but it matters.

I remember one job I had many years ago when I was in charge of security for a financial institution. I spent time learning each of the business processes that we had so I could understand each of the moving parts, what was essential, and what was on the horizon for change. I even spent a couple days meeting with the folks who handled printing. Yeah, printing — but not reports or internal documents. These were the people that created the checks that our institution used to pay other institutions, and more importantly (to me) our customers.

I recall there being many out-of-patch compliance boxes in this area of the company, so I, being the diligent Director, decided to find out why. It turns out the software being used to print these business essential checks would not run on the current operating systems, and the physical printer cards used to connect to these non-network printers also required older hardware ports. As one of the people I interviewed said, “We don’t want to be the reason someone’s grandma doesn’t get her check and can’t go to the grocery store.”

There were (at the time) no other alternatives that we could deploy, and the environment had zero tolerance for downtime. The solution I proposed was to isolate these devices into their own network, which blocked access to and from the internet for these devices, and also reduced the likelihood that these devices would be identified during an adversary’s internal reconnaissance or mapping. It didn’t patch the vulnerable devices, but it went a long way to reducing the likelihood of a bad thing happening to these devices due to their out-of-date OS and software.

This story is especially appropriate today, as we face ever-increasing numbers of vulnerabilities announced by software vendors, and can only expect this volume to continue to increase. Do what you can to make sure the checks still get printed, while managing your risks intentionally.

## The one big thing

Cisco Talos is disclosing [new findings from our CAIRN research](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware) that show malware authors are embedding natural-language instructions into their code to evade AI-assisted analysis. We classify this growing trend as "A3: AI-Analysis Evasion." Over the past 18 months, we've tracked techniques ranging from simple comments telling an AI to ignore a file, to advanced "template spraying" designed to trick specific large language models (LLMs).

### Why do I care?

Attackers expect AI to be in your analysis pipeline, and they’re developing cheap methods to manipulate those systems. While we found these prompt-injection techniques only steer the AI's verdict in the attacker's favor about 35 percent of the time, they are being adopted across all levels of malware sophistication. A3 families like MANTLEMAZE also pair these AI deceptions with serious underlying threats, such as abusing vulnerable drivers to disable EDR from kernel space.

### So now what?

Because these evasion instructions must be written in plaintext, defenders have a highly stable detection surface to monitor. Security teams should flag imperative language addressed to analysis systems within binaries as a suspicious signal. Most importantly, anyone building or using AI-assisted pipelines must ensure that text extracted from a sample is strictly treated as evidence, never as a system directive. [Read the full blog](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware) for more information on these techniques and a list of sample hashes.

## Top security headlines of the week

**Citrix NetScaler security snafus get even worse amid more zero-day reports**
This latest vulnerability, tracked as CVE-2026-88779, is a memory overflow bug that leads to denial of service attacks. ([The Register](https://www.theregister.com/security/2026/10/05/citrix-netscaler-security-snafus-get-even-worse-amid-more-0-day-reports/5301232?utm_source=tldrinfosec))

**Hackers steal 8 million citizens’ records from Danish government database**
The Danish government would not say who is behind the breach, which happened in September but was discovered on October 2. However, it said the unauthorized access was obtained by...