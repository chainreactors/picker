---
title: Unmasking the new XorDDoS controller and infrastructure
url: https://blog.talosintelligence.com/unmasking-the-new-xorddos-controller-and-infrastructure/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-18
fetch_date: 2025-10-06T22:06:44.034435
---

# Unmasking the new XorDDoS controller and infrastructure

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

# Unmasking the new XorDDoS controller and infrastructure

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Thursday, April 17, 2025 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)

* Cisco Talos observed an existing distributed denial-of-service (DDoS) malware known as XorDDoS, continuing to spread globally between November 2023 and February 2025.
* A significant finding shows that over 70 percent of attacks using XorDDoS targeted the United States from Nov. 2023 to Feb. 2025.
* The language settings of the muti-layer controller, XorDDoS builder and controller binding tool strongly suggest that the operators are Chinese-speaking individuals.
* Talos discovered the latest version of the XorDDoS controller, called the “VIP version,” and its corresponding central controller were used to build the DDoS bot network for more sophisticated and widespread attacks.
* Talos' analysis exposes the network connection between central controller, sub-controller and XorDDoS malware in order to highlight the XorDDoS trojan network pattern. This may help victims identify when they are targeted by these trojans.

---

## Linux XorDDoS trojan trend and victimology

The XorDDoS trojan is a well-known DDoS malware that targets Linux machines, turning them into "zombie bots" that carry out attacks. First identified in [2014](https://blog.malwaremustdie.org/2014/09/mmd-0028-2014-fuzzy-reversing-new-china.html), its sub-controller was uncovered in [2015](https://www.virusbulletin.com/uploads/pdf/conference/vb2015/KalnaiHorejsi-VB2015.pdf). Based on the simplified Chinese user interface and instructions of the XorDDoS controllers and builder, Talos assess with high confidence that the operators are Chinese-speaking individuals.

From 2020 to 2023, the XorDDoS trojan has increased significantly in prevalence. This trend is not only due to the [widespread global distribution](https://www.microsoft.com/en-us/security/blog/2022/05/19/rise-in-xorddos-a-deeper-look-at-the-stealthy-ddos-malware-targeting-linux-devices/) of the XorDDoS trojan but also an uptick in [malicious DNS requests](https://unit42.paloaltonetworks.com/new-linux-xorddos-trojan-campaign-delivers-malware/) linked to its command-and-control (C2) infrastructure. In addition to targeting commonly exposed Linux machines, the trojan has expanded its reach to [Docker servers](https://www.trendmicro.com/en_us/research/20/f/xorddos-kaiji-botnet-malware-variants-target-exposed-docker-servers.html), converting infected hosts into bots. It employs a strategy of Secure Shell (SSH) brute-force attacks to gain remote access to target devices. Once it obtains valid SSH credentials, the attacker leverages root privileges to execute a script that downloads and installs XorDDoS on the compromised device.

Even though numerous security vendors have already provided solutions and detection methods to capture them, Talos continues to observe attempts to deliver XorDDoS malware.

![](https://blog.talosintelligence.com/content/images/2025/04/XorDDoS_detection-statistics.jpg)

**Figure 1. Cisco Secure Firewall’s monthly malware connection detection statistics.**

Between November 2023 and February 2025, Talos observed that the XorDDoS trojan continued to have a global impact, with nearly 50 percent of its successfully compromised victims located in the United States. Additionally, we noted that the compromised systems attempted to target and attack several countries, including Spain, the United States, Taiwan, Canada, Japan, Brazil, Paraguay, Argentina, the United Kingdom, the Netherlands, Italy, Ukraine, Germany, Thailand, China, India, Israel, Venezuela, Switzerland, Singapore, Finland, Australia, Saudi Arabia, France, Turkey, the United Arab Emirates and South Korea.

![](https://blog.talosintelligence.com/content/images/2025/04/XorDDoS_-XorDDoS-trojan-victim.jpg)

**Figure 2. Percentage of XorDDoS successfully-compromised machines across all regions.**

Talos also used our Cisco Secure Network/Cloud Analysis to observe actors using those compromised machines to launch DDoS attack and the attacks are globalized. Notably, we found that the United States accounted for over 70 percent of attempted attacks employing XorDDoS.

![](https://blog.talosintelligence.com/content/images/2025/04/XorDDoS-04.jpg)

**Figure 3. Percentage of XorDDoS attempted targets across all regions.**

## Infection chain

XorDDoS has long relied on SSH brute-force attacks to spread. It deploys a malicious shell script that attempts numerous root credential combinations across thousands of servers until it successfully accesses a target Linux device. Once inside the machine, XorDDoS implements persistence mechanisms to ensure it launches automatically at system startup, therefore evading detection and termination by security products. To maintain persistence, the malware installs an init script and a cron job script. These scripts are embedded within the malware and perform actions consistent with those outlined in [previous reports](https://www.microsoft.com/en-us/security/blog/2022/05/19/rise-in-xorddos-a-deeper-look-at-the-stealthy-ddos-malware-targeting-linux-devices/).

![](https://blog.talosintelligence.com/content/images/2025/04/Picture1.png)

**Figure 4. Inint script and cron script embedded in trojan.**

The latest version of XorDDoS malware continues to use the same decryption function and the XOR key "BB2FA36AAA9541F0" to decrypt its embedded configuration. Once the URLs or IPs are decrypted, they are added to a remote list. This list is then used to establish communication and retrieve commands from the C2 server. Talos used [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':'BB2FA36AAA9541F0'%7D,'Standard',false)&input=MzIgMzIgNDIg...