---
title: UK Cybercrime Journal: Sustained DragonForce Campaign
url: https://blog.bushidotoken.net/2026/06/uk-cybercrime-journal-sustained.html
source: Over Security
date: 2026-06-17
fetch_date: 2026-06-18T06:51:41.415429
---

# UK Cybercrime Journal: Sustained DragonForce Campaign

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### UK Cybercrime Journal: Sustained DragonForce Campaign

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[June 17, 2026](https://blog.bushidotoken.net/2026/06/uk-cybercrime-journal-sustained.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZLDacO8tJifEdNGsyG0kBzeZFP1fC2rMPDuRs6KE4xdsOu5J76DHNHzvMD_PVbY5DJoBLFLedwC0Lb77F0kns5vAm1ivCOW0nYDqQmTbyUK1cb6U14gaK4cLrg69cRvWCoNVlZE_8v5aIEeEjeDl6Uy38sVHV6PsAxb47JSvAGDzUZz0w3xOpfHhWESsZ/w640-h304/IMG_4973.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZLDacO8tJifEdNGsyG0kBzeZFP1fC2rMPDuRs6KE4xdsOu5J76DHNHzvMD_PVbY5DJoBLFLedwC0Lb77F0kns5vAm1ivCOW0nYDqQmTbyUK1cb6U14gaK4cLrg69cRvWCoNVlZE_8v5aIEeEjeDl6Uy38sVHV6PsAxb47JSvAGDzUZz0w3xOpfHhWESsZ/s1280/IMG_4973.png)

 What Happened

* Throughout May 2026, affiliates of the DragonForce ransomware-as-a-service (RaaS) platform claimed seven UK-based companies as its victims by posting them on their Tor data leak site.
* On 27 May 2026 alone, DragonForce ended the month by posting 22 victims from around the world, four of which were UK-based firms.

DragonForce’s UK-based victims from May spanned a diverse range of industries:

* Professional Services & Talent: Practicus (interim management/executive search)
* Financial & Tax Services: WSM (UK tax advisory)
* Infrastructure & Logistics: ERH (traffic management solutions) and Refreshment Systems (vending/logistics)
* Heavy Industry/Construction: Arsenal Scaffold
* Technology & IT: Helix International (managed enterprise software)
* Luxury Retail/Finance: Cult Wines.

Analyst Comment

Active since late 2023, DragonForce remains a persistent cybercriminal threat particularly towards the UK. The recent flurry of disclosures on the DragonForce ransomware Tor data leak site in May highlights a highly active and accelerating threat campaign towards the UK. This diverse range of firms indicates that DragonForce affiliates are largely opportunistic rather than specific. They tend to exploit vulnerabilities or compromised credentials wherever they find them, rather than executing a highly tailored campaign against a single industry or target.

While these companies may not all be household names, some of them will be important suppliers and service providers for their local regions. Helix International in particular is a concern due to them being a managed service provider (MSP) that caters to medium, large, and Fortune 500 companies across various industries, including healthcare, finance, retail, and entertainment.

The Ransomware Vulnerability Matrix [Group Profile](https://github.com/BushidoUK/Ransomware-Vulnerability-Matrix/blob/main/GroupProfiles/DragonForce.md) for DragonForce shows that affiliates are highly adept at targeting edge devices and remote access points, such as Ivanti Connect Secure, Fortinet FortiOS, SonicWall SSL-VPN. A recurring theme across DragonForce's Ransomware Tool Matrix [Group Profile](https://github.com/BushidoUK/Ransomware-Tool-Matrix/blob/main/GroupProfiles/DragonForce.md) is their regular abuse of Bring Your Own Vulnerable Driver (BYOVD) tactics to bypass Endpoint Detection and Response (EDR) and Antivirus software.

In June 2025, DragonForce [made the news](https://www.securityweek.com/ransomware-group-claims-attacks-on-uk-retailers/) as it was used by affiliates, attributed to Scattered Spider, to attack the UK retailers M&S, Co-op, and Harrods in a string of high-profile attacks. More recently, DragonForce has [reportedly](https://x.com/falconfeedsio/status/2060220753400967490) been actively recruiting on English-speaking cybercrime forums.

Defensive Takeaways

* Attack Surface Monitoring: Based on DragonForce’s reported tactics, organisations must review their RDP (Port 3389) exposures as well as any unpatched SSL-VPNs. Prevent these exposures and apply updates as soon as possible. Any brief exposures or time when systems are left unpatched leaves an open window for the adversary to get inside.
* Rotate your credentials & implement MFA: It may sound simple, but a lot of these DragonForce incidents have been because of RDP and SSL-VPN account brute forcing. Therefore, the importance of using strong credentials, secure password managers, and multi-factor authentication (MFA) enabled cannot be overstated.
* Back Your Data Up: To increase your odds of recovering from a ransomware attack, it’s essential to maintain backups of your business critical data. However, as the DragonForce affiliates are known to target backup solutions like Veeam servers, it’s increasingly important to maintain regularly updated offline backups to be able to restore from.

**Relevant Sources**

1. <https://www.ransomware.live/group/dragonforce>
2. <https://www.ransomware.live/map/GB>
3. [https://x.com/falconfeedsio/status/2060220753400967490](https://x.com/falconfeedsio/status/2060220753400967490?s=46&t=-dkNDSDHEzyAagaVN0SDgA)

**Relevant CTI Resources**

1. <https://github.com/BushidoUK/Ransomware-Tool-Matrix/blob/main/GroupProfiles/DragonForce.md>
2. <https://github.com/BushidoUK/Ransomware-Vulnerability-Matrix/blob/main/GroupProfiles/DragonForce.md>
3. <https://github.com/BushidoUK/Ransomware-Tool-Matrix/blob/main/CommunityReports/CR-021-DRAGONFORCE-APR-2025.md>
4. <https://github.com/BushidoUK/Ransomware-Tool-Matrix/blob/main/CommunityReports/CR-022-DRAGONFORCE-FEB-2026.md>
5. <https://github.com/BushidoUK/Ransomware-Tool-Matrix/blob/main/CommunityReports/CR-023-DRAGONFORCE-AUG-2024.md>

[DragonForce](https://blog.bushidotoken.net/search/label/DragonForce)
[ransomware](https://blog.bushidotoken.net/search/label/ransomware)
[UK Cybercrime Journal](https://blog.bushidotoken.net/search/label/UK%20Cybercrime%20Journal)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Popular posts from this blog

### [Ransomware Tool Matrix Project Updates: May 2025](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html)

-
[May 05, 2025](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_BpTZksj9aZ67Y0MoiVTbyhuF2ZNK6mjoCeIlkF5MIjc7DlouoqPLYd-7XXsHgxT6Vytvvo-gY5b8JO3Ujab_8XLnSo1LbYrBUW78GrP2U8wx3ZT-B2ZwMGLO2aVCovVuIX3qZWYIN3X-GCw470E7tr2aiI0CPIgi9bkXbvDldhDL1hNZEc48rVTPyvxY/s320/OIG2.jpg)](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html)

Introduction This blog is a summary and analysis of recent additions to the Ransomware Tool Matrix (RTM) as well as the Ransomware Vulnerability Matrix (RVM) .  Feedback from the infosec community about these projects has been overwhelmingly positive and many researchers have contacted me to tell me how helpful they have found these to be.  It makes me happy to hear how doing something in my spare time can help stop ransomware attacks and cybercriminals from exploiting our society’s systems. And it is for that reason, I shall continue to maintain these projects as long as ransomware is still around.  For anyone new to these projects, please read the descriptions on GitHub or feel free to watch my talk explaining the project at BSides London . Background on the current ransomware ecosystem as of May 2025 Following the impact of Operation Cronos against LockBit and the exit scam by ALPHV/BlackCat, the ransomware ecosystem has been even more unstable than usual.  The e...

[Read more](https://blog.bushidotoken.net/2025/05/ransomware-tool-matrix-project-updates.html "Ransomware Tool Matrix Project Updates: May 2025")

### [Raspberry Robin: A global USB malware campaign providing access to ransomware operators](https://blog.bushidotoken.net/2023/05/raspberry-robin-global-usb-malware.html)

-
[May 02, 2023](https://blog.bushidotoken.net/2023/05/raspberry-robin-global-usb-malware.html "permanent link")

[![Image](https://blogg...