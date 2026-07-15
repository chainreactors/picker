---
title: Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack
url: https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:49:58.898265
---

# Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack](https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html)

**Swati Khandelwal**Jul 14, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi34s_9ywUXjSc5OtF7-fDiAqSa3H-UHpJfACXyULY5ziUlM67mCJHWee9tluTiGm7ZRhMy36SLal2CUjqwJHZ8vdHuFstRwJhPGLAXe49as-o3nRE-QAyRs2mx3og8eVdWdnzzr9LwGMXckMix80XOQPsWiE30xqqYGG3PNjjpVTCpLsnW77pCk_3MyKQ/s1700-e365/ms%3Dpatch.jpg)

Microsoft shipped its largest **Patch Tuesday** on record today, and two of the fixes close holes that attackers are already exploiting. The release covers 622 of Microsoft's own CVEs by its [Security Update Guide](https://msrc.microsoft.com/update-guide/releaseNote/2026-Jul) count, more than triple [June's previous high of around 200](https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html).

Those two live bugs are the ones to grab first. Microsoft credits incident responders for both. Both are elevation-of-privilege flaws in identity and collaboration infrastructure: CVE-2026-56164 in on-premises SharePoint Server and CVE-2026-56155 in Active Directory Federation Services.

Neither is one of the splashy remote code execution criticals. They are privilege bugs in two systems that matter more than their scores suggest: the company document store, and the box that signs its logins.

## The two zero-days to patch first

[CVE-2026-56164](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56164), a SharePoint Server flaw Microsoft says is being exploited in attacks, lets an unauthenticated attacker escalate privileges over the network. No credentials, no user interaction, remote. Microsoft credited it to Mandiant's incident responders and Google's FLARE team, which points to discovery inside active attacks, though Microsoft has not said how it was exploited or by whom.

If you run self-hosted SharePoint, this is the one to grab first, and there is a second clock on it: today is also the day SharePoint Server 2016 and 2019 reach the end of extended support. Unlike Windows Server or SQL Server, neither has a paid ESU program to fall back on.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Beyond patching, Microsoft's advisory notes that enabling AMSI in Full Mode on the server blunts the attack. SharePoint has been an attacker magnet since the [ToolShell chain](https://thehackernews.com/2025/07/critical-microsoft-sharepoint-flaw.html) tore through unpatched servers in 2025, and it has not stopped being one.

[CVE-2026-56155](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56155), an Active Directory Federation Services flaw Microsoft also flags as exploited, lets an already-authenticated attacker elevate privileges locally through weak access controls. Microsoft's own DART incident-response unit gets the credit.

AD FS is the box that signs the tokens for the rest of the estate trusts, which is why a flaw labeled "local" on that host is worth more attention than the label suggests. Microsoft has not said what privileges it grants, or how attackers used it.

Worth knowing for anyone tracking remediation deadlines: neither CVE is on [CISA's Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) as of this writing. Microsoft's own exploitability rating already marks both as exploited. Do not wait for a KEV listing to make it official.

Microsoft also rates the SharePoint bug fairly low on severity, which is a good reminder that the severity label is not the thing to sort by this month.

## A third bug, and a SharePoint chain landing in August

The third zero-day was publicly disclosed but is not under attack: CVE-2026-50661, another [BitLocker bypass](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50661). It needs physical access to the device, so it is not a remote emergency. Patch it, but it does not jump the queue. It continues a run of BitLocker bypasses stretching back through bitskrieg and [YellowKey](https://thehackernews.com/2026/05/microsoft-releases-mitigation-for.html) earlier this year.

SharePoint drew a second notable fix. Rapid7 Labs disclosed [CVE-2026-55040](https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed/), a JWT authentication bypass they built for their Pwn2Own Berlin entry. The score depends on who you ask: Rapid7 puts it at 5.3 and says Microsoft assigned it medium severity, while ZDI [reads](https://www.zerodayinitiative.com/blog/2026/7/14/the-july-2026-security-update-review) the release as Critical at 9.1.

What it does is not in dispute. Rapid7 chained it to a separate remote code execution bug to reach unauthenticated RCE against a vulnerable server, and the RCE half is not patched yet; Microsoft is slated to fix it in August.

That makes July bypass the fix that breaks the chain. A four-point spread on one bug also tells you what a severity number is worth this month.

## The RC4 cleanup that can break logins

This update also finishes Microsoft's multi-year Kerberos RC4 hardening. The July rollout removes the RC4DefaultDisablementPhase rollback switch, the escape hatch admins have leaned on since Microsoft began the crackdown in January.

After this, RC4 works only for accounts explicitly configured to allow it. If any service account in your environment still requests RC4 Kerberos tickets, it can fail authentication the moment the update lands.

The order matters: audit first, using the RC4 audit events Microsoft added in January, then rotate the passwords on flagged service accounts, so Windows generates AES keys for them, then patch. Rotation only fixes accounts missing AES keys.

Anything pinned to RC4 by configuration, or a legacy client that speaks nothing else, needs its own fix before the update lands. This one does not get you...