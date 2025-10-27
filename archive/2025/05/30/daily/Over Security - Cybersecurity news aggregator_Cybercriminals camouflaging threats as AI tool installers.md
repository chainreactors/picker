---
title: Cybercriminals camouflaging threats as AI tool installers
url: https://blog.talosintelligence.com/fake-ai-tool-installers/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-30
fetch_date: 2025-10-06T22:27:52.973966
---

# Cybercriminals camouflaging threats as AI tool installers

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

![](/content/images/2025/05/Cybercriminals-Camouflaging-1.jpg)

# Cybercriminals camouflaging threats as AI tool installers

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Thursday, May 29, 2025 06:00

[Threats](/category/threats/)
[ransomware](/category/ransomware/)

* Cisco Talos has discovered new threats, including the ransomware CyberLock, Lucky\_Gh0$t, and a newly-discovered malware we call “Numero,” all of which masquerade as legitimate AI tool installers.
* CyberLock ransomware, developed using PowerShell, primarily focuses on encrypting specific files on the victim's system. The threat actor deceitfully claims in the ransom note that the payments will be allocated for humanitarian aid in various regions, including Palestine, Ukraine, Africa and Asia.
* Lucky\_Gh0$t ransomware is yet another variant of the Yashma ransomware, which is the sixth iteration of the Chaos ransomware series, featuring only minor modifications to the ransomware binary.
* The newly-identified destructive malware, Numero, affects victims by manipulating the graphical user interface (GUI) components of their Windows OSs, rendering systems completely unusable.

---

AI has increasingly proliferated across various business verticals, leading to a transformation of industries through automation, data-driven decision-making and enhanced customer engagements. However, as AI continues to propel multiple industry sectors forward, malicious actors are exploiting its popularity by distributing a range of malware disguised as AI solutions’ installers and tools.

Threat actors are employing a variety of techniques and channels to distribute these fraudulent installers, including SEO-poisoning tactics to manipulate search engine rankings and cause their malicious websites or download links to appear at the top of search engine results, as well as platforms such as Telegram or social media messengers.

As a result, unsuspecting businesses in search of AI solutions may be deceived into downloading counterfeit tools in which malware is embedded. This practice poses a significant risk, as it not only compromises sensitive business data and financial assets but also undermines trust in legitimate AI market solutions. Therefore, organizations and users must exercise extreme caution, meticulously verify sources, and rely exclusively on reputable vendors to avoid falling prey to these threats.

Talos has recently uncovered multiple threats masquerading as AI solutions being circulated in the wild, including the CyberLock and Lucky\_Gh0$t ransomware families, along with a newly discovered destructive malware, dubbed “Numero.” The legitimate versions of these AI tools are particularly popular within the B2B sales domain and the technology and marketing sectors, indicating that individuals and organizations in these industries are particularly at risk of being targeted by these malicious threats.

## CyberLock ransomware

Talos observed a threat actor creating a lookalike fake AI solution website with the domain ‘novaleadsai[.]com’, likely masquerading as the original website domain ‘novaleads.app’, a lead monetization platform designed to help businesses maximize the value of their leads through various services and performance-based models.

![Inserting image..., Picture](https://blog.talosintelligence.com/content/images/2025/05/data-src-image-2f8ff667-a31c-4338-ae7f-b67d048f4c6c.png)

Figure 1. Fake website advertising the AI tool.

On the fake website, the actor persuades users to download the product with an offer of free access to the tool for the first 12 months, followed with a monthly subscription of $95. The threat actor also used an SEO manipulation technique that made their fake website appear in the top search results for online search engines.

When a user downloads the fake AI product as a ZIP archive, it contains a .NET executable with the file name ‘NovaLeadsAI.exe’. The executable was compiled on Feb. 2, 2025, which is on the same day the fake domain ‘novaleadsai[.]com’ was created.

The ‘NovaLeadsAI.exe’ file is the loader that has the CyberLock ransomware PowerShell script embedded as the resource file. When the victim runs the loader executable, it deploys the ransomware.

![Picture](https://blog.talosintelligence.com/content/images/2025/05/data-src-image-06d82260-725c-4659-8427-fcf8ae34b457.png)

Figure 2. Snippet of the CyberLock ransomware loader.

## CyberLock ransom note

The CyberLock ransomware appeared to be operating as early as Feb. 2025. The ransom note claims that the threat actor has obtained full access to sensitive business documents, personal files and confidential databases, demanding a hefty ransom in exchange for decryption keys. Victims are instructed to communicate with the threat actor by emailing ‘cyberspectreislocked@onionmail[.]org’.

The CyberLock threat actor demands that the USD $50,000 ransom be paid exclusively in Monero (XMR) cryptocurrency and employs psychological tactics by falsely claiming that the ransom payments will be used for humanitarian aid in regions like Palestine, Ukraine, Africa and Asia. The actor splits the payment into two separate wallets, complicating defenders' tracking efforts.

The ransom note is structured to intimidate and manipulate victims by threatening to expose stolen data if payment is not made within three days. However, Talos did not see any evidence of data exfiltration functionality within the ransomware code.

![](https://blog.talosintelligence.com/content/images/2025/05/Picture1.png)

Figure 3. CyberLock ransom note.

## CyberLock, the PowerShell ransomware

CyberLock ransomware is written in PowerShell, embedded with the CSharp code and delivered to the victims as an embedded resource of the .NET loader.

When CyberLock is executed, it initially uses the functi...