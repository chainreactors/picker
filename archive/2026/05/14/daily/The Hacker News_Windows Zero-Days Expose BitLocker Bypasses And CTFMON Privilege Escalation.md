---
title: Windows Zero-Days Expose BitLocker Bypasses And CTFMON Privilege Escalation
url: https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html
source: The Hacker News
date: 2026-05-14
fetch_date: 2026-05-15T05:53:28.279155
---

# Windows Zero-Days Expose BitLocker Bypasses And CTFMON Privilege Escalation

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Windows Zero-Days Expose BitLocker Bypasses And CTFMON Privilege Escalation](https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html)

**Ravie Lakshmanan**May 14, 2026Zero-Day / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXt7ooDl2PwJY4nazAKdW9rmILsmosve2FZaO9usxTk_rkksEEvsLgY-uc_MErXvjvusuWjN7PWRM9KaRXB1OkL75gio7tcqpMsPZxaFNE9XDpYmARH3Dw_gGgddwWXHSt5VUJ-lb56F9bCVzTYghEo7qELWVv8K_W8V1BrWgssgqWkzPJxW6I31i_GyYf/s1700-e365/windowss.jpg)

An anonymous cybersecurity researcher who disclosed three Microsoft Defender vulnerabilities has returned with two more zero-days involving a BitLocker bypass and a privilege escalation impacting Windows Collaborative Translation Framework (CTFMON).

The [security defects](https://deadeclipse666.blogspot.com/2026/05/two-more-public-disclosures-it-will.html) have been codenamed **[YellowKey](https://github.com/Nightmare-Eclipse/YellowKey)** and **[GreenPlasma](https://github.com/Nightmare-Eclipse/GreenPlasma)**, respectively, by the researcher, who goes by the online aliases Chaotic Eclipse and Nightmare-Eclipse.

The researcher described [YellowKey](https://x.com/weezerOSINT/status/2054299771817660433) as "one of the most insane discoveries I ever found," likening the BitLocker bypass to functioning as a backdoor, as the bug is present only in the Windows Recovery Environment ([WinRE](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference)), a built-in framework designed to troubleshoot and repair common unbootable operating system issues.

YellowKey affects Windows 11 and Windows Server 2022/2025. At a high level, it involves copying specially crafted "FsTx" files on a USB drive or the EFI partition, plugging the USB drive into the target Windows computer with BitLocker protections turned on, rebooting into WinRE, and triggering a shell by holding down the CTRL key.

"I think it will take a while even for MSRC to find the real root cause of the issue. I just never managed to understand why this vulnerability is sooo well hidden," the researcher [explained](https://deadeclipse666.blogspot.com/2026/05/were-doing-silent-patches-now-huh-also.html). "Second thing is, no, TPM+PIN does not help, the issue is still exploitable regardless."

Security researcher Will Dormann, in a [post](https://infosec.exchange/%40wdormann/116565129854382214) shared on Mastodon, said, "I was able to reproduce [YellowKey] with a USB drive attached," adding, "it looks like Transactional NTFS bits on a USB Drive are able to delete the winpeshl.ini file on ANOTHER DRIVE (X:). And we get a cmd.exe prompt, with BitLocker unlocked instead of the expected Windows Recovery environment."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

"While the [TPM-only BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/countermeasures) bypass is indeed interesting, I think the buried lede here is that a \System Volume Information\FsTx directory on one volume has the ability to modify the contents of another volume when it is replayed," Dormann pointed out. "To me, this in and of itself sounds like a vulnerability."

The second vulnerability flagged by Chaotic Eclipse is a case of privilege escalation security that could be exploited to obtain a shell with SYSTEM permissions. It arises as a result of what has been described as Windows CTFMON arbitrary section creation.

The released proof-of-concept (PoC) is incomplete and lacks the necessary code to obtain a full SYSTEM shell. In its current form, the exploit can allow an unprivileged user to create arbitrary memory section objects within directory objects writable by SYSTEM, potentially enabling manipulation of privileged services or drivers that implicitly trust those paths, as a standard user does not have write access to the locations.

The development comes nearly a month after the researcher [published](https://thehackernews.com/2026/04/three-microsoft-defender-zero-days.html) three Defender zero-days dubbed BlueHammer, RedSun, and UnDefend after allegedly expressing dissatisfaction with Microsoft's handling of the vulnerability disclosure process. The shortcomings have since come under active exploitation in the wild.

While BlueHammer was officially assigned the identifier CVE-2026-33825 and patched by Microsoft last month, Chaotic Eclipse said the tech giant appears to have "silently" addressed RedSun without issuing any advisory.

"I hope you at least attempt to resolve the situation responsibly, I'm not sure what type of reaction you expected from me when you threw more gas on the fire after BlueHammer," the researcher said. "The fire will go as long as you want, unless you extinguish it or until there nothing left to burn."

Chaotic Eclipse also promised a "big surprise" for Microsoft, coinciding with the next Patch Tuesday release in June 2026.

When reached for comment, a Microsoft spokesperson had previously told The Hacker News that it "has a customer commitment to investigate reported security issues and update impacted devices to protect customers as soon as possible," and that it supports coordinated vulnerability disclosure, which the company said "helps ensure issues are carefully investigated and addressed before public disclosure."

### BitLocker Downgrade Attack Uncovered

The development comes as French cybersecurity company Intrinsec detailed an [attack chain](https://github.com/garatc/BitUnlocker) against BitLocker that leverages a boot manager downgrade by exploiting [CVE-2025-48804](https://thehackernews.com/2025/07/microsoft-patches-130-vulnerabilities.html) (CVSS score: 6.8) to bypass the encryption protection on fully patched Windows 11 systems in under five minutes.

"The principle is as follows: the boot manager loads the System Deployment Image (SDI) file and the WIM ref...