---
title: VECT 2.0 Ransomware Irreversibly Destroys Files Over 131KB on Windows, Linux, ESXi
url: https://thehackernews.com/2026/04/vect-20-ransomware-irreversibly.html
source: The Hacker News
date: 2026-04-28
fetch_date: 2026-04-29T05:13:05.302974
---

# VECT 2.0 Ransomware Irreversibly Destroys Files Over 131KB on Windows, Linux, ESXi

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

# [VECT 2.0 Ransomware Irreversibly Destroys Files Over 131KB on Windows, Linux, ESXi](https://thehackernews.com/2026/04/vect-20-ransomware-irreversibly.html)

**Ravie Lakshmanan**Apr 28, 2026Malware / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEji1Auw0eR5oiVkEiB8JPzjSCaFsUUiAOfNHrcsOzO4DElBB4gbQ20uu3p69nojIkLsgxZOj81fa7fK_dchUAx0WINAGMq3X0VSA7LH_Isc1hPAvls76rdLeSYCn40zw8P2xAikVwxb_pclaNQXER8G7nzPO41LAl0-ELu-i60_RLl7CLCWcC9gGrEC8oXw/s1700-e365/vect.gif)

Threat hunters are warning that the cybercriminal operation known as **VECT 2.0** acts more like a wiper than a ransomware due to a critical flaw in its encryption implementation across Windows, Linux, and ESXi variants that renders recovery impossible even for the threat actors.

The fact that VECT's locker [permanently destroys large files](https://research.checkpoint.com/2026/vect-ransomware-by-design-wiper-by-accident/) rather than encrypting them means even victims who opt to pay the ransom cannot get their data back, as the decryption keys are discarded by the malware during the time encryption occurs.

"VECT is being marketed as ransomware, but for any file over 131KB – which is most of what enterprises actually care about – it functions as a data destruction tool," Eli Smadja, group manager at Check Point Research, said in a statement shared with The Hacker News.

"CISOs need to understand that in a VECT incident, paying is not a recovery strategy. There is no decrypter that can be handed over, not because the attackers are unwilling, but because the information required to build one was destroyed the moment their software ran. The focus has to be on resilience: offline backups, tested recovery procedures, and rapid containment – not negotiation."

[VECT](https://www.halcyon.ai/ransomware-alerts/emerging-ransomware-group-vect) (now rebranded as VECT 2.0) is a ransomware-as-a-service (RaaS) scheme that first [launched](https://www.cyfirma.com/news/weekly-intelligence-report-03-april-2026/) its affiliate program in December 2025. On its dark website, the group displays the message "Exfiltration / Encryption / Extortion," highlighting its triple-threat business model.

According to an analysis [published](https://www.dsci.in/files/content/advisory/2026/threat-report-feb-2026.pdf) by the Data Security Council of India (DSCI) last month, a $250 entry fee, payable in Monero (XMR), is required for new affiliates. The fee is waived for applicants from the Commonwealth of Independent States (CIS) countries, indicating an attempt to recruit individuals from the region.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agentic-guide-d-3)

In recent weeks, the group has established a formal partnership with the BreachForums cybercrime marketplace and the [TeamPCP](https://thehackernews.com/2026/03/teampcp-pushes-malicious-telnyx.html) hacking group, in a move aimed at further lowering the barrier to entry for ransomware operators and incentivizing affiliates to launch attacks by weaponizing previously stolen data.

"The convergence of large-scale supply chain credential theft, a maturing RaaS operation, and mass dark web forum mobilization represents an unprecedented model of industrialized ransomware deployment," Dataminr [noted](https://thehackernews.com/2026/04/weekly-recap-vercel-hack-push-fraud.html#:~:text=Vect%20Partners%20with%20BreachForums%20and%20TeamPCP) earlier this month.

While the collaboration may be a sign of what's to come, its data leak site currently lists only two victims, both of which are said to have been compromised via the TeamPCP supply chain attacks. What's more, contrary to the group's initial claims of using ChaCha20-Poly1305 [AEAD](https://developers.google.com/tink/aead) for encryption, Check Point's analysis has found that it uses a weaker, unauthenticated cipher with no integrity protection.

But it doesn't end there, for the C++-based lockers for all three platforms suffer from a fundamental design flaw that causes any file larger than 131,072 bytes to be permanently and irrecoverably destroyed, as opposed to being encrypted.

"The malware encrypts four independent chunks of each 'large file' using four freshly generated random 12-byte nonces, but appends only the final nonce to the specific encrypted file on disk," Check Point explained. "The first three nonces, each required to decrypt its respective chunk, are generated, used, and silently discarded. They are never stored on disk, in the registry, or transmitted to the operator."

"Because ChaCha20-IETF requires both the 32-byte key and the exact matching 12-byte nonce to reverse each chunk, the first three quarters of every large file are unrecoverable by anyone, including the ransomware operator, who cannot provide a working decryption tool even after ransom payment. Since the vast majority of operationally critical files exceed this 'large-size' threshold, VECT 2.0 functions in practice as a data wiper with a ransomware facade."

The Windows version of the ransomware, besides encrypting files across local, removable, and network-accessible storage, features a comprehensive anti-analysis suite targeting 44 specific security and debugging tools, alongside a safe-mode persistence mechanism and multiple remote-execution script templates for lateral spread.

When "--force-safemode" is active, the locker configures the next boot into Windows Safe Mode and writes its own executable path into the Windows Registry so that it's automatically run on the subsequent Safe Mode boot, where the operating system is launched in a basic state using a limited set of files and drivers.

On top of that, although the Windows variant implements environment detection mechanisms to fly under the radar, they are never invoked, allowing security teams running the artifacts to avoid triggering any evasive response. The ESXi variant, on the other hand, enforces geofencing and anti-debugging checks prior to commencing the encryption step. It also attempts to move laterally using SSH. The Linux version uses the same codebase as the ESXi flavor and implements a subset of its functionality.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

The geofencing step verifies if i...