---
title: UK Cybercrime Journal: Inside the Cl0p attack on South Staffs Water
url: https://blog.bushidotoken.net/2026/05/uk-cybercrime-journal-inside-cl0p.html
source: Over Security
date: 2026-05-23
fetch_date: 2026-05-24T06:01:16.582409
---

# UK Cybercrime Journal: Inside the Cl0p attack on South Staffs Water

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### UK Cybercrime Journal: Inside the Cl0p attack on South Staffs Water

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[May 23, 2026](https://blog.bushidotoken.net/2026/05/uk-cybercrime-journal-inside-cl0p.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijcw80jUrnzMEfeZRdyl2kzD9NSXsR3QbuZNyylwUaSmCCudOL0mUHlDRTTchpECjKDuGgrItJg2otphI6GyGebjyvBuioT8CWf6ORS24HZ6Xvvj5Bx70rpZMA-5GdIRppQy52bJRl4m_rtci8IAtuG4U7B3bRuxmPj6NPst8HUX3Vf7OQJRhACnA2hjKA/w400-h266/IMG_4900.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijcw80jUrnzMEfeZRdyl2kzD9NSXsR3QbuZNyylwUaSmCCudOL0mUHlDRTTchpECjKDuGgrItJg2otphI6GyGebjyvBuioT8CWf6ORS24HZ6Xvvj5Bx70rpZMA-5GdIRppQy52bJRl4m_rtci8IAtuG4U7B3bRuxmPj6NPst8HUX3Vf7OQJRhACnA2hjKA/s1843/IMG_4900.jpeg)

What Happened:

On 11 May 2026, the UK Information Commissioner’s Office (ICO) fined South Staffordshire Water £963,900 after the Cl0p ransomware group lurked completely undetected in its network for nearly two years. Initial access reportedly occurred via a malicious phishing email in September 2020, which downloaded Cl0p’s Get2Loader malware and their SDBBOT backdoor to establish persistence. The breach itself, however, was only discovered two years later in July 2022 when staff began investigating IT performance slowdowns. South Staffs Water ultimately found out that 4.1 terabytes of data was exfiltrated and the personal data of 633,887 customers and employees being published in August 2022 on Cl0p’s Tor data leak site.

The ICO’s investigation also revealed a staggering list of systemic failures. The ICO exposed that South Staff’s outsourced Security Operations Center (SOC) was blind to 95% of the network and that they conducted zero internal or external vulnerability scans over an 18-month window. At the time of the attack they were still running Windows Server 2003 machines long after extended support ended. Further, two of their domain controllers were left completely unpatched against ZeroLogon (CVE-2020-1472), a critical, easily exploitable vulnerability published years before the intrusion.

Analyst Comment:

This case is a sobering look at the technical debt hiding inside the UK’s Critical National Infrastructure (CNI). A dwell time of nearly two years is practically unheard of in modern ransomware operations, and the TTPs used by the adversary points to a total breakdown of their defences. Cl0p didn’t need sophisticated, state-sponsored techniques or zero-days to pull this one off, they just walked back in through an infection that went undetected.

The ICO’s findings also reveal the reality that many UK organisations still treat cybersecurity as a set-and-forget compliance check rather than routine efforts to mature and upgrade systems or proactive measures to hunt and detect threats lurking inside the network.

Defensive Takeaways:

* Audit Your Outsourced SOC: As we learned from this incident, never assume the third-party security provider sees everything or is doing everything right. Establish audits to verify that endpoint telemetry and logs from your entire estate are actively ingested, retained, and monitored in the right platform.
* Harden Your Crown Jewels Against Old Flaws: Ensure that active directory and domain controllers are strictly monitored and prioritised for critical patches. Vulnerabilities like ZeroLogon remain a ransomware operator’s favourite tool for fast lateral movement and escalation to Domain Admin access. This is exactly what Cl0p and a dozen or so other groups use.

**Relevant Sources:**

1. <https://ico.org.uk/media2/xdrfahsw/south-staffordshire-plc-and-south-staffordshire-water-plc-monetary-penalty-notice.pdf>
2. <https://therecord.media/uk-water-company-had-hackers-lurking-for-years>
3. [https://www.bleepingcomputer.com/news/security/uk-fines-water-supplier-13m-for-exposing-data-of-664k-customers/](https://www.bleepingcomputer.com/news/security/uk-fines-water-supplier-13m-for-exposing-data-of-664k-customers/amp/)
4. <https://www.theregister.com/cyber-crime/2026/05/11/ico-fines-south-staffordshire-963k-over-2022-breach/5237875>
5. <https://www.theregister.com/security/2022/08/18/ransomware-attack-on-a-uk-water-company-clouded-by-confusion/1394557>

**Relevant CTI Resources**

1. <https://malpedia.caad.fkie.fraunhofer.de/details/win.clop>
2. <https://malpedia.caad.fkie.fraunhofer.de/details/win.get2>
3. <https://malpedia.caad.fkie.fraunhofer.de/details/win.sdbbot>
4. <https://www.crowdstrike.com/en-us/blog/cve-2020-1472-zerologon-security-advisory/>
5. <https://github.com/BushidoUK/Ransomware-Vulnerability-Matrix/blob/main/GroupProfiles/Clop.md>
6. <https://www.ransomware.live/group/clop>

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

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd_7gSbs89Orm2BQ22KJ76nRHlAoIyaj6Rph2DA0sQ2IaBIrPTmDZdn_9uHremHSL1vxAG9t1m-fg_Yqgova-eqexDrglh-rIRmXxXrvvmb0_h6dSJlqBsTRSCIhvTEweAprIcS8JYsBWdRni5xwMAG5SysOEnDAvzJwdRHZJVh0Jp2obgs43Ui4w7Yg/s16000/RRobin_April2023.png)](https://blog.bushidotoken.net/2023/05/raspberry-robin-global-usb-malware.html)

Logo credit: RedCanary Ever since it first appeared in late 2021, the Raspberry Robin malware campaign has been propagating globally. A number of threat intelligence reports by vendors such as RedCanary (who named it) and Microsoft (who track it as DEV-0856/Storm-0856) have covered the malware campaign in great detail.  In fact, the list of blogs I do recommend to read to catch up on this threat are as follows: https://redcanary.com/blog/raspberry-robin https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity https://blog.sekoia.io/raspberry-robins-botnet-second-life/ https://decoded.avast.i...