---
title: Using AI to defeat AI
url: https://blog.talosintelligence.com/using-ai-to-defeat-ai/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-19
fetch_date: 2026-02-20T04:07:33.376188
---

# Using AI to defeat AI

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

# Using AI to defeat AI

By
[Martin Lee](https://blog.talosintelligence.com/author/martin-lee/)

Thursday, February 19, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Generative AI and agentic AI are here to stay. Although I believe that the advantages that AI brings to bad guys may be overstated, these new technologies [allow threat actors](https://blog.talosintelligence.com/spy-vs-spy-how-genai-is-powering-defenders-and-attackers/) to conduct attacks at a faster rate than before.

One capability that AI improves for threat actors is the ability to reconnoitre employees, discover their interests, and craft social engineering lures specific to them. Being able to deliver tailored, targeted social engineering using the language and tone most likely to trick an individual is a useful tool for the bad guys.

However, if AI brings advantages to those who seek to attack us, we shouldn’t overlook the benefits that it brings to defenders and the new weaknesses it exposes in the bad guys. If AI agents are searching for employees who are vulnerable to social engineering; then let us serve them exactly what that are looking for.

AI tools can create a whole army of fictitious employees who can be a rich source of threat intelligence. With AI we can easily create social media profiles of fake employees to entice malicious profiling agents. These AI avatars can post social media content or upload AI generated CVs or other documents to AI systems, leaving a trail of breadcrumbs for malicious agents to discover and follow.

Clearly, any message sent to the email address of an AI-generated employee is certain to be spam. We can update our lists of potentially malicious IP addresses and URLs appropriately. Similarly, we can create accounts on messaging platforms for our fake employees and wait for the social engineering attempts to analyse and block

Any attempt to access services or log-in using the credentials of an AI employee can only be malicious. Again, defensive teams can quickly and easily block the connecting IP address to nip in the bud any malicious campaign.

Malicious use of AI doesn’t need to be thought of only as a threat. It can be a way to turn the tables on threat actors and use their own tools against them. By understanding how AI tools are profiling and collecting information about our users, we can flood these tools with disinformation and treat any resulting attacks as a rich source of threat intelligence rather than as a source of concern.

AI is changing things for both attackers and defenders. New tools and capabilities allow us to think differently about defense and how we can increasingly make life difficult for the bad guys.

## The one big thing

In our [latest Vulnerability Deep Dive](https://blog.talosintelligence.com/good-enough-emulation/), a Cisco Talos researcher discovered six vulnerabilities in the Socomec DIRIS M-70 industrial gateway by emulating just the Modbus protocol handling thread, rather than the whole system. Using tools like Unicorn Engine, AFL, and Qiling for fuzzing and debugging, this “good enough” approach made it possible to find and analyze weaknesses despite hardware protections. The vulnerabilities were responsibly disclosed and have been patched by the manufacturer.

### Why do I care?

Vulnerabilities in industrial gateways like the M-70 can cause major disruptions, especially in critical infrastructure, data centers, and health care. Attackers could exploit these flaws to stop operations or manipulate processes, leading to financial loss and equipment damage. The research highlights how even devices with strong hardware protections can still be vulnerable through their communication protocols.

### So now what?

Organizations using Socomec DIRIS M-70 gateways should apply the manufacturer’s patches to fix the vulnerabilities. To detect exploitation attempts, defenders should download and use the latest Snort rulesets from Snort.org, as recommended in the blog. Finally, regularly monitor industrial devices for unusual activity and review security controls around critical gateways.

## Top security headlines of the week

**CISA navigates DHS shutdown with reduced staff**
CISA is currently operating at roughly 38% capacity (888 out of 2,341 staff) due to the U.S. Department of Homeland Security shutdown that began February 14, 2026. KEV is one area that remains. ([SecurityWeek](https://www.securityweek.com/cisa-navigates-dhs-shutdown-with-reduced-staff/))

**EU Parliament blocks AI tools over cyber, privacy fears**
According to an internal email seen by POLITICO, EU Parliament had disabled "built-in artificial intelligence features" on corporate tablets after its IT department assessed it couldn't guarantee the security of the tools' data. ([POLITICO](https://www.politico.eu/article/eu-parliament-blocks-ai-features-over-cyber-privacy-fears/))

**Supply chain attack embeds malware in Android devices**
Researchers have spotted new malware embedded in the firmware of Android devices from multiple vendors that injects itself into every app on infected systems, giving attackers virtually unrestricted remote access to them. ([Dark Reading](https://www.darkreading.com/mobile-security/supply-chain-attack-embeds-malware-android-devices))

**Data breach at fintech giant Figure affects close to a million customers**
Troy Hunt, security researcher and creator of the site Have I Been Pwned, analyzed the data allegedly taken from Figure and found it contained 967,200 unique email addresses associated with Figure customers. ([TechCrunch](https://techcrunch.com/2026/02/18/data-breach-at-fintech-giant-figure-affects-close-to-a-million-customers/))

**Amnesty International:** **Intellexa’s** **Pr...