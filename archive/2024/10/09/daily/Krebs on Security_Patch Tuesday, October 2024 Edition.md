---
title: Patch Tuesday, October 2024 Edition
url: https://krebsonsecurity.com/2024/10/patch-tuesday-october-2024-edition/
source: Krebs on Security
date: 2024-10-09
fetch_date: 2025-10-06T19:10:35.333807
---

# Patch Tuesday, October 2024 Edition

Advertisement

[![](/b-knowbe4/40.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Patch Tuesday, October 2024 Edition

October 8, 2024

[9 Comments](https://krebsonsecurity.com/2024/10/patch-tuesday-october-2024-edition/#comments)

**Microsoft** today released security updates to fix at least 117 security holes in **Windows** computers and other software, including two vulnerabilities that are already seeing active attacks. Also, **Adobe** plugged 52 security holes across a range of products, and **Apple** has addressed a bug in its new **macOS 15** “**Sequoia**” update that broke many cybersecurity tools.

![](https://krebsonsecurity.com/wp-content/uploads/2020/08/windowsec.png)

One of the zero-day flaws — [CVE-2024-43573](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-43573) — stems from a security weakness in **MSHTML**, the proprietary engine of Microsoft’s **Internet Explorer** web browser. If that sounds familiar it’s because this is the fourth MSHTML vulnerability found to be exploited in the wild so far in 2024.

**Nikolas Cemerikic**, a cybersecurity engineer at **Immersive Labs**, said the vulnerability allows an attacker to trick users into viewing malicious web content, which could appear legitimate thanks to the way Windows handles certain web elements.

“Once a user is deceived into interacting with this content (typically through phishing attacks), the attacker can potentially gain unauthorized access to sensitive information or manipulate web-based services,” he said.

Cemerikic noted that while Internet Explorer is being retired on many platforms, its underlying MSHTML technology remains active and vulnerable.

“This creates a risk for employees using these older systems as part of their everyday work, especially if they are accessing sensitive data or performing financial transactions online,” he said.

Probably the more serious zero-day this month is [CVE-2024-43572](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-43572), a code execution bug in the [Microsoft Management Console](https://en.wikipedia.org/wiki/Microsoft_Management_Console), a component of Windows that gives system administrators a way to configure and monitor the system.

**Satnam Narang**, senior staff research engineer at **Tenable**, observed that the patch for CVE-2024-43572 arrived a few months after researchers at **Elastic Security Labs** disclosed an attack technique called [GrimResource](https://www.elastic.co/security-labs/grimresource) that leveraged an old cross-site scripting (XSS) vulnerability combined with a specially crafted Microsoft Saved Console (MSC) file to gain code execution privileges.

“Although Microsoft patched a different MMC vulnerability in September (CVE-2024-38259) that was neither exploited in the wild nor publicly disclosed,” Narang said. “Since the discovery of CVE-2024-43572, Microsoft now prevents untrusted MSC files from being opened on a system.”

Microsoft also patched **Office,** **Azure**, **.NET**, **OpenSSH for Windows**; **Power BI**; **Windows Hyper-V**; **Windows Mobile Broadband**, and **Visual Studio**. As usual, the **SANS Internet Storm Center** has [a list of all Microsoft patches released today](https://isc.sans.edu/diary/Microsoft%20Patch%20Tuesday%20-%20October%202024/31336), indexed by severity and exploitability.

Late last month, Apple rolled out macOS 15, an operating system update called Sequoia that broke the functionality of security tools made by a number of vendors, including CrowdStrike, SentinelOne and Microsoft. On Oct. 7, [Apple pushed an update to Sequoia users](https://techcrunch.com/2024/10/07/apple-fixes-bugs-in-macos-sequoia-that-broke-some-cybersecurity-tools/) that addresses these compatibility issues.

Finally, Adobe has released security updates to plug a total of 52 vulnerabilities in a range of software, including **Adobe Substance 3D Painter**, **Commerce**, **Dimension**, **Animate**, **Lightroom**, **InCopy**, **InDesign**, **Substance 3D Stager**, and **Adobe FrameMaker**.

Please consider backing up important data before applying any updates. Zero-days aside, there’s generally little harm in waiting a few days to apply any pending patches, because not infrequently a security update introduces stability or compatibility issues. **AskWoody.com** usually has the skinny on any problematic patches.

And as always, if you run into any glitches after installing patches, leave a note in the comments; chances are someone else is stuck with the same issue and may have even found a solution.

*This entry was posted on Tuesday 8th of October 2024 06:21 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Security Tools](https://krebsonsecurity.com/category/security-tools/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[.NET](https://krebsonsecurity.com/tag/net/) [adobe](https://krebsonsecurity.com/tag/adobe/) [Adobe Framemaker](https://krebsonsecurity.com/tag/adobe-framemaker/) [Adobe Substance 3D Painter](https://krebsonsecurity.com/tag/adobe-substance-3d-painter/) [Animate](https://krebsonsecurity.com/tag/animate/) [apple](https://krebsonsecurity.com/tag/apple/) [Azure](https://krebsonsecurity.com/tag/azure/) [Commerce](https://krebsonsecurity.com/tag/commerce/) [CVE-2024-43572](https://krebsonsecurity.com/tag/cve-2024-43572/) [CVE-2024-43573](https://krebsonsecurity.com/tag/cve-2024-43573/) [Dimension](https://krebsonsecurity.com/tag/dimension/) [Elastic Security Labs](https://krebsonsecurity.com/tag/elastic-security-labs/) [GrimResource](https://krebsonsecurity.com/tag/grimresource/) [Immersive Labs](https://krebsonsecurity.com/tag/immersive-labs/) [InCopy](https://krebsonsecurity.com/tag/incopy/) [InDesign](https://krebsonsecurity.com/tag/indesign/) [Lightroom](https://krebsonsecurity.com/tag/lightroom/) [macOS 15](https://krebsonsecurity.com/tag/macos-15/) [MSHTML](https://krebsonsecurity.com/tag/mshtml/) [Nikolas Cemerikic](https://krebsonsecurity.com/tag/nikolas-cemerikic/) [Office](https://krebsonsecurity.com/tag/office/) [OpenSSH for Windows; Power BI; Windows Hyper-V; Windows Mobile Broadband](https://krebsonsecurity.com/tag/openssh-for-windows-power-bi-windows-hyper-v-windows-mobile-broadband/) [Satnam Narang](https://krebsonsecurity.com/tag/satnam-narang/) [Sequoia](https://krebsonsecurity.com/tag/sequoia/) [Substance 3D Stager](https://krebsonsecurity.com/tag/substance-3d-stager/) [Tenable](https://krebsonsecurity.com/tag/tenable/) [Visual Studio](https://krebsonsecurity.com/tag/visual-studio/)

Post navigation

[← A Single Cloud Compromise Can Feed an Army of AI Sex Bots](https://krebsonsecurity.com/2024/10/a-single-cloud-compromise-can-feed-an-army-of-ai-sex-bots/)
[Lamborghini Carjackers Lured by $243M Cyberheist →](https://krebsonsecurity.com/2024/10/lamborghini-carjackers-lured-by-243m-cyberheist/)

## 9 thoughts on “Patch Tuesday, October 2024 Edition”

1. William Kemmler [October 9, 2024](https://krebsonsecurity.com/2024/10/patch-tuesday-october-2024-edition/#comment-616802)

   “. . . stems from a security weakness in MSHTML, the proprietary engine of Microsoft’s Internet Explorer web browser.”

   Once again Microsoft’s irrational obsession with backwards compatibility bites them in the hind end. I just don’t understand it. How long has it been since Microsoft announced they were deprecating and removin...