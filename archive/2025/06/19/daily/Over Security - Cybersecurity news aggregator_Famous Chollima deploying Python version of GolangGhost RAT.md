---
title: Famous Chollima deploying Python version of GolangGhost RAT
url: https://blog.talosintelligence.com/python-version-of-golangghost-rat/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-19
fetch_date: 2025-10-06T22:55:48.680463
---

# Famous Chollima deploying Python version of GolangGhost RAT

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

![](/content/images/2025/06/image-2.jpeg)

# Famous Chollima deploying Python version of GolangGhost RAT

By
[Vanja Svajcer](https://blog.talosintelligence.com/author/vanja-svajcer/)

Wednesday, June 18, 2025 06:00

[Threats](/category/threats/)
[SecureX](/category/securex-3/)
[APT](/category/apt/)
[DPRK](/category/dprk/)

* In May 2025, Cisco Talos identified a Python-based remote access trojan (RAT) we call “PylangGhost,” used exclusively by a North Korean-aligned threat actor. PylangGhost is functionally similar to the previously documented GolangGhost RAT, sharing many of the same capabilities.
* In recent campaigns, the threat actor [Famous Chollima](https://malpedia.caad.fkie.fraunhofer.de/actor/wagemole) — potentially made up of multiple groups — has been using a Python-based version of their trojan to target Windows systems, while continuing to deploy a Golang-based version for MacOS users. Linux users are not targeted in these latest campaigns.
* The attacks are targeting employees with experience in cryptocurrency and blockchain technologies.
* Based on open-source intelligence, only a small number of users, predominantly in India, are affected. Cisco product telemetry does not indicate that there are any affected Cisco users.

---

Since mid-2024, the threat actor group [Famous Chollima (aka Wagemole)](https://malpedia.caad.fkie.fraunhofer.de/actor/wagemole), a North Korean-aligned threat actor, has been very active through several well-documented campaigns. These campaigns include using variants of Contagious Interview (aka DeceptiveDevelopment) and creating fake job advertisements and skill-testing pages. In the latter, users are instructed to copy and paste (ClickFix) a malicious command line in order to install drivers necessary to conduct the final skill-testing stage.

Toward the end of the year, researchers [documented Famous Chollima’s remote access trojan](https://dmpdump.github.io/posts/NorthKorea_Backdoor_Stealer/) (RAT) called “GolangGhost” in its source code format, which was frequently used as the final payload in the threat actor’s ClickFix campaigns.

In May 2025, Cisco Talos discovered threat actors starting to deploy a functionally equivalent Python variant of GolangGhost trojan, which we call “PylangGhost.”

## Fake job interview sites mislead users to PylangGhost infection

Famous Chollima seek financial benefit using a two-pronged approach: first, by creating fake employers for the purpose of jobseekers exposing their personal information, and second by deploying fake employees as workers in targeted victim companies.

This blog focuses on the first method, where real software engineers, marketing employees, designers and other workers are targeted by fake recruiters and instructed to visit skill-testing pages in order to move forward with their application.

Based on the advertised positions, it is clear that the Famous Chollima is broadly targeting individuals with previous experience in cryptocurrency and blockchain technologies. The skill-testing sites attempt to impersonate real companies such as Coinbase, Archblock, Robinhood, Parallel Studios, Uniswap and others, which helps with the targeting.

![](https://blog.talosintelligence.com/content/images/2025/06/ChollimaFigure1-01-1.png)

Figure 1. Examples of initial fake job sites.

Each target is sent an invite code to visit a testing website where, depending on the position, they are instructed to enter their details and answer several questions to test their experience and skills. The sites are created using the React framework and have very similar visual designs, no matter the type of position.

![Picture 1112995568, Picture](https://blog.talosintelligence.com/content/images/2025/06/data-src-image-a17be5ae-26e9-417a-9fef-bfc518153aac.png)

**Figure 2. Example of questions asked for an illegitimate Business Development Manager position at Robinhood.**

Once the user answers all the questions and provides personal details, the site displays an invitation to record a video for the interviewer, recommending that the user request camera access by pressing a button.

![Picture 836890465, Picture](https://blog.talosintelligence.com/content/images/2025/06/data-src-image-7e93dffd-d191-4d84-abea-0fe861b1dcf0.png)

**Figure 3. A camera setup page displayed once questions are answered.**

Finally, when the user requests camera, the site displays the instructions for the user to copy, paste and execute a command to allegedly install the required video drivers, if the OS is supported. When Talos used Windows and MacOS test systems, the instructions were shown as seen in Figure 4 and 5. The Linux test system led to another error message, without any instructions to download and install the payload.

![Picture 708346057, Picture](https://blog.talosintelligence.com/content/images/2025/06/data-src-image-628846bb-0b5d-4677-9edb-0cf83cd30d9e.png)

Figure 4. Windows instructions to copy, paste and execute a malicious command.

![Picture 1300516178, Picture](https://blog.talosintelligence.com/content/images/2025/06/data-src-image-b690f129-55cf-4328-b08d-107a3dbd05d4.jpeg)

Figure 5. MacOS instructions to copy, paste and execute a malicious command.

Instructions for downloading the alleged fix are different based on the browser fingerprinting, and also given in appropriate shell language for the OS: PowerShell or Command Shell for Windows, and Bash for MacOS.

![](https://blog.talosintelligence.com/content/images/2025/06/ChollimaFigure1-02.png)

**Figure 6. Command Shell, PowerShell or Bash instructions to download a payload.**

## PylangGhost - Python variant of GolangGhost

As the Golang variant of the RAT is already well-documented, this blog focuses on the Python version and the similarities between the two. The initial stage consists of a command line which the f...