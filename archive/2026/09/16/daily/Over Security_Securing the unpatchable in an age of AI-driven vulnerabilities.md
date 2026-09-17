---
title: Securing the unpatchable in an age of AI-driven vulnerabilities
url: https://blog.talosintelligence.com/securing-the-unpatchable-in-an-age-of-ai-driven-vulnerabilities/
source: Over Security
date: 2026-09-16
fetch_date: 2026-09-17T07:00:01.738370
---

# Securing the unpatchable in an age of AI-driven vulnerabilities

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

# Securing the unpatchable in an age of AI-driven vulnerabilities

By
[Martin Lee](https://blog.talosintelligence.com/author/martin-lee/)

Wednesday, September 16, 2026 06:00

[On The Radar](https://blog.talosintelligence.com/category/on-the-radar/)

* AI is accelerating vulnerability discovery, leaving unpatchable operational technology (OT) systems at risk. Hoping for the best is not a viable anti-exploitation strategy.
* Deploying next-generation firewalls directly upstream allows for virtual patching through deep packet inspection. These systems scan incoming traffic to detect and block exploit attempts before they can impact the vulnerable device.
* The predictability of legitimate network connections to OT systems can be used to protect systems through micro-segmentation. This ensures that only a handful of authorized devices can communicate with the system, minimizing the attack surface.

---

AI-assisted code analysis is uncovering decades of technical debt. Every new patch removes a newly identified coding mistake. Little by little, we are improving the state of software engineering, but the price is a cadence of patching that organizations may struggle to implement.

These efforts leave unsupported systems, or systems that are not able to be patched for whatever reason, with unmitigated known vulnerabilities. How can such systems be secured in a world where AI is steadily improving its ability to identify new vulnerabilities?

Operational technology (OT) systems provide the services that support modern life (e.g., medical equipment, building management systems, and industrial critical systems within chemical plants). Often the systems are certified to operate only with a defined set of software that cannot easily be altered, or operate using systems that are no longer supported. In either case, if a vulnerability is discovered that affects the system, there is no easy way for it to be patched.

Ignoring the problem and hoping for the best is rarely an effective strategy. The U.K.’s NHS health system was significantly affected by the [WannaCry worm](https://www.england.nhs.uk/wp-content/uploads/2018/02/lessons-learned-review-wannacry-ransomware-cyber-attack-cio-review.pdf) in 2017, with a significant minority of systems running the end-of-life operating system Windows XP contributing to the problem. More recently, exploitation of end-of-life software was used to [gain access](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-339a) to governmental systems in 2023.

Even systems that are believed to run on a bespoke platform will almost certainly include common libraries and protocols in which vulnerabilities may be found. Vulnerable systems that are not publicly exposed can still be identified by threat actors who gain access to internal networks and pose a tempting target.

## Defending by predictability

Applying the approved patch remains the best option. If this is not possible, we can use the inherent predictability of OT systems to protect them.

**Visibility first:** You cannot protect what you cannot see. The characteristics of the network fingerprint presented by legacy systems allows them to be easily identified to build an inventory of systems requiring attention.

**Micro-segmentation:** Network architecture is an effective first line of defense. Frequently, OT only ever connects to a small number of systems. By using virtual local area networks (VLANs) coupled with access control lists (ACLs), we can place vulnerable systems on private networks where only authorized devices are permitted to connect to them. By shutting them off from the rest of the network, we make it incrementally more difficult for attackers to identify them and launch their attacks.

**NGFW and IPS:** Placing a next-generation firewall (NGFW) upstream allows for granular filtering. When equipped with an up-to-date intrusion prevention system (IPS), the firewall can inspect traffic to filter out any attempts at exploitation before it impacts the device. When coupled with network segmentation, we can ensure that not only are trusted systems solely communicating with the vulnerable system, but that the traffic is free from known malicious content.

## The myth of the air gap

In theory, it is possible to create an air-gapped system that is completely disconnected from wider systems, although in practice it is difficult to achieve. Without absolute operational discipline, air gaps are frequently breached by staff or contractors seeking shortcuts.

Temporary bridges installed to facilitate data transfer or short-term fixes involving a VPN and wireless connectivity have a habit of becoming semi-permanent features. Each shortcut provides a means by which attacks can impact the system.

Even data diodes, hardware that physically restricts data to one-way flow, may be circumvented by shortcuts when the inconvenience of maintaining security compliance clashes with operational expedience.

An air gap or data diode may be an appropriate solution, but defenders should understand that it is unlikely to permanently provide absolute separation, and should be vigilant for breaches of the gap.

## Conclusion

Advances in AI technology will continue to identify vulnerabilities that in some circumstances are difficult, or effectively impossible, to patch. In situations where fixing the software isn’t possible, appropriate network segmentation, rigorous visibility, and the deployment of NGFW/IPS combinations can provide a powerful compensatory layer.

We might not be able to prevent the discovery of vulnerabilities, but we can ensure that attackers do not have an easy path to exploit them in the field.

##### Share this post

#### Related Content

[### The safety penalty: Reclaiming operational sovereignty in the age of AI

August 25, 2026 06:00

As frontier AI ...