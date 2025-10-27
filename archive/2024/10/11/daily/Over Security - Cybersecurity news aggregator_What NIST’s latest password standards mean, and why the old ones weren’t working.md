---
title: What NIST’s latest password standards mean, and why the old ones weren’t working
url: https://blog.talosintelligence.com/threat-source-newsletter-oct-10-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-11
fetch_date: 2025-10-06T18:54:38.332808
---

# What NIST’s latest password standards mean, and why the old ones weren’t working

# Cisco Talos Blog

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

# What NIST’s latest password standards mean, and why the old ones weren’t working

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, October 10, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Say goodbye to the days of using the “@” symbol to mean “a” in your password or replacing an “S” with a “$.”

The U.S. National Institute of Standards and Technology (NIST) [recently announced](https://www.darkreading.com/identity-access-management-security/nist-drops-password-complexity-mandatory-reset-rules) new guidelines for the ways website and organizations should handle password creation and management that will do away with many of the “common sense” things we’ve thought about passwords for years now.

Here is a tl;dr version of what these proposed guidelines say:

* Passwords need to be at least eight characters long, and sites should have an additional recommendation to make them at least 15 characters long.
* Credential service providers (CSPs) should allow users to make their passwords as long as 64 characters.
* CSPs should allow ASCII and Unicode characters to be included in passwords.
* Rather than setting a regular cadence for changing passwords, users only need to change their passwords if there is evidence of a breach.
* There should not be requirements to implement a certain number of numbers or special characters into passwords. (Ex., “Password12345!”)
* Do away with knowledge-based authentication or security questions when selecting passwords. (Think: “What was the name of your college roommate?”)

Now, we should make a few things here clear. Just because NIST is proposing these doesn’t mean anyone \*has\* to abide by them, these are merely guidelines that some of the larger tech companies in the U.S. can choose to adopt. And these are proposed rules for the time being, meaning the public and tech companies have time to weigh in on the matter before they are codified in any way.

While these proposals may seem counterintuitive, it should make traditional text-based login credentials more manageable for users and admins. [Studies have shown](https://research.gatech.edu/largest-study-its-kind-shows-outdated-password-practices-are-widespread) that requiring a mixture of special characters and numbers has led users to create easier-to-guess passwords like “$ummer2024!” or “P@ssword”.

And policies that require users to change their passwords often have led them to create passwords that are neigh-impossible to remember, so users [end up storing these passwords](https://www.washingtonpost.com/technology/2024/09/27/how-often-reset-passwords/) in easy-to-locate places near their computers, like on a physical piece of paper or saved to a .txt file on their desktop.

The [hope from NIST](https://www.fastcompany.com/91200084/nist-password-guidelines-2024) is that enforcing longer passwords will make it harder for adversaries to guess and less intimidating for users to manage their passwords.

Of course, using a third-party password manager is usually the most secure option for anyone. But what NIST is proposing is still a step in the right direction, and if nothing else will make those of us who are more security-minded have a better time when creating a new account.

## The one big thing

The [largest Microsoft Patch Tuesday](https://blog.talosintelligence.com/microsoft-patch-tuesday-october-2024/) since July includes two vulnerabilities that have been exploited in the wild and three other critical issues across the company’s range of hardware and software offerings. October’s monthly security update from Microsoft includes fixes for 117 CVEs, the most in a month since July’s updates covered 142 vulnerabilities. The two vulnerabilities that Microsoft reports have been actively exploited in the wild and are publicly known are both rated as only being of “moderate” severity.

### Why do I care?

[CVE-2024-43572](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43572) is a remote code execution vulnerability in the Microsoft Management Console that could allow an attacker to execute arbitrary code on the targeted machine. Microsoft’s security update will prevent untrusted Microsoft Saved Console (MSC) files from being opened to protect users against adversaries trying to exploit this vulnerability. The other vulnerability that was exploited in the wild in this week’s security update is [CVE-2024-43573](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43573), a platform spoofing vulnerability in Windows MSHTML. Platform spoofing vulnerabilities usually allow an adversary to gain unauthorized access to an environment by disguising themselves as a trusted source.

### So now what?

Talos is releasing a new Snort rule set that detects attempts to exploit some of them. Please note that additional rules may be released at a future date and current rules are subject to change pending additional information. Cisco Security Firewall customers should use the latest update to their ruleset by updating their SRU. Open-source Snort Subscriber Rule Set customers can stay up to date by downloading the latest rule pack available for purchase on Snort.org. The rules included in this release that protect against the exploitation of many of these vulnerabilities are 64083 - 64086, 64089, 64090, 64111 and 64112. There are also Snort 3 rules 301034 - 301036 and 301041.

# Top security headlines of the week

**Chinese state-sponsored actors are suspected to have breached several U.S. telecommunications providers to spy on U.S. government phone calls.** AT&T, Verizon and Lumen may have all been victims of the alleged counter-spying operation from the newly named APT Salt Typhoon. The actor potentially accessed information from systems ...