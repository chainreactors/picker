---
title: There is no real fix to the security issues recently found in GitHub and other similar software
url: https://blog.talosintelligence.com/threat-source-newsletter-aug-1-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-02
fetch_date: 2025-10-06T18:04:23.343187
---

# There is no real fix to the security issues recently found in GitHub and other similar software

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

# There is no real fix to the security issues recently found in GitHub and other similar software

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, August 1, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

A [recently discovered security issue in GitHub](https://www.thestack.technology/github-repo-deleted/) and other, similar, control system products seem to fit into the classic “it’s a feature, not a bug” category.

Security researchers last week published their findings into some research of how deleted forks in GitHub work, potentially leaving the door open for a malicious actor to steal a project key and then view deleted forks and versions of any project on GitHub.

This may not necessarily even be a \*new\* discovery, because users on social media were quick to point out that these products have always been designed this way, so it’s not like a new sort of exploit had just been published. But the publishing of these findings came after [Truffle Security says](https://trufflesecurity.com/blog/anyone-can-access-deleted-and-private-repo-data-github) a major tech company accidentally leaked a private key for an employee GitHub account, and despite totally deleting the repo thinking that would take care of the leak, it was still exposed and accessed by potentially malicious users.

This potential issue has not been tested in similar software like GitLab or Bitbucket, but conceivably, they’ve all been designed in the same way. The major difference for GitHub is that deleted or unpublished commits can be downloaded via a fork if the user has the correct identifying hash (or at least a portion of it).

The issue here is there is no real patch or fix to address this issue, and now it’s widely known and been publicized on the internet.

GitHub told The Register that this is part of how the software is designed, and there doesn’t appear any efforts underway to change that.

“GitHub is committed to investigating reported security issues. We are aware of this report and have validated that this is expected and documented behavior inherent to how fork networks work. You can read more about how deleting or changing visibility affects repository forks in our documentation,” the company said in a statement to online publication [The Register](https://www.theregister.com/2024/07/25/data_from_deleted_github_repos/).

The lesson for users, especially if you’re a private company that primarily uses GitHub, is just to understand the inherent dangers of using open-source software like those projects that are created and managed on GitHub. (Martin Lee and I will be discussing more in tomorrow morning’s episode of Talos Takes.)

The other option is that, if you’re a GitHub user and at some point, published a key, you should probably just assume someone has copied it by now. That means not only deleting references to that key but rotating the key and checking if it was used improperly.

## The one big thing

Cisco Talos recently [discovered a malicious campaign](https://blog.talosintelligence.com/chinese-hacking-group-apt41-compromised-taiwanese-government-affiliated-research-institute-with-shadowpad-and-cobaltstrike-2/) that compromised a Taiwanese Government Affiliated Research Institute that started as early as July 2023, delivering Shadowpad malware, Cobalt Strike and other customized tools for post-compromise activities. The activity conducted on the victim endpoint matches the Chinese hacking group APT41. The combined use of malware, open-source tools and projects procedures and post-compromise activity matches this group method of operation. ShadowPad, widely considered the successor of PlugX, is a modular remote-access-trojan (RAT) only seen sold to Chinese hacking groups.

### Why do I care?

APT41 is a prolific and dangerous threat actor that all users and cybersecurity practitioners should be keeping track of. The group, also known as Amoeba, Bronze Atlas, Wicked Spider, and more, is known for carrying out Chinese state-sponsored espionage activity and other financially motivated cybercrimes. We have also uncovered that APT41 created a tailored loader to inject a proof of concept for [CVE-2018-0824](https://nvd.nist.gov/vuln/detail/CVE-2018-0824), a remote code execution vulnerability in Microsoft COM for Windows, directly into memory to achieve local privilege escalation.

### So now what?

This threat actor commonly tries to exploit CVE-2018-0824, which Microsoft has long had a patch available for. Users should ensure all Windows systems are up to date to the latest version to protect against this vulnerability (and the hundreds of others that exist in Windows anyway!). Additionally, Talos has released new ClamAV signatures and Snort rules to detect the ShadowPad malware and Cobalt Strike beacons used by APT41.

# Top security headlines of the week

**Another Microsoft outage just days after the massive CrowdStrike-related incident was the result of a cyber attack, according to the company.** The outage Wednesday morning affected Microsoft Outlook and the video game “Minecraft” for almost 10 hours and forced thousands of users to report issues. The incident gained increased interest in the wake of a massive outage last weekend that resulted in international disruptions and tens of millions of dollars in damages. Microsoft stated after the outage was resolved that the initial issue was caused by a distributed denial-of-service attack, and additional mitigations to defend against that DDoS attack failed. A notification on Microsoft’s website said the outage affected Microsoft Azure, the cloud platform that powers many of its services, and Microsoft 365. It also said cloud systems Intune and Entra were affected. Even though Microsoft had no direct...