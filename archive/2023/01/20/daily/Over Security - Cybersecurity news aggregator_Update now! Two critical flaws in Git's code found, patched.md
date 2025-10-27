---
title: Update now! Two critical flaws in Git's code found, patched
url: https://www.malwarebytes.com/blog/news/2023/01/update-now-two-critical-flaws-in-gits-code-found-patched
source: Over Security - Cybersecurity news aggregator
date: 2023-01-20
fetch_date: 2025-10-04T04:23:53.651962
---

# Update now! Two critical flaws in Git's code found, patched

[Skip to content](#primary)

Search

Search Malwarebytes.com

Search for:

* [Sign In](https://my.malwarebytes.com/en/login)

  [Sign in](https://my.malwarebytes.com/overview)

  [Activate subscription >](https://my.malwarebytes.com/landing/activate)

  [Add devices or upgrade >](https://my.malwarebytes.com/landing/upgrade)

  [Renew subscription >](https://my.malwarebytes.com/landing/manual-renewal)

  [Secure Hub >](https://my.malwarebytes.com/secure-hub)

  [Don’t have an account?
  **Sign up >**](https://my.malwarebytes.com/overview?flow=signup)

  Sign In

[Malwarebytes logo](https://www.malwarebytes.com/blog)

* Personal

  < Products

  **Device Protection & Antivirus**

  + [Premium Security Antivirus](https://www.malwarebytes.com/premium)
  + [Mobile Security for Android & iOS](https://www.malwarebytes.com/mobile)

  **Identity Protection**

  + [Identity Theft Protection](https://www.malwarebytes.com/identity-theft-protection)
  + [Personal Data Remover](https://www.malwarebytes.com/personal-data-remover)
  + [Digital Footprint Scanner](https://www.malwarebytes.com/digital-footprint)

  **Privacy Protection**

  + [Privacy VPN](https://www.malwarebytes.com/vpn)
  + [Browser Guard](https://www.malwarebytes.com/browserguard)
  + [AdwCleaner](https://www.malwarebytes.com/adwcleaner)

  Have a current computer infection?

  [**Free Virus Scan**](https://www.malwarebytes.com/solutions/virus-scanner)

  Worried it’s a scam?

  [**Free Scam Guard tool**](https://www.malwarebytes.com/solutions/scam-guard)

  Try our antivirus with a free, full-featured 14-day trial

  [**Free Antivirus**](https://www.malwarebytes.com/mwb-download)

  Get your free digital security toolkit

  [**Explore all free tools**](https://www.malwarebytes.com/free-tools)

  Find the right cyberprotection for you

  [**Compare plans and pricing**](https://www.malwarebytes.com/pricing)
* Business

  < Business

  **[Teams](https://www.malwarebytes.com/teams)**

  Protect small & home offices – no IT expertise needed

  **[ThreatDown](https://www.threatdown.com/?utm_campaign=mwb-referral&utm_source=malwarebytes.com&utm_medium=referral&utm_content=cta-mb-nav-threatdown)**

  Award-winning endpoint security for small and medium businesses
* Pricing

  < Pricing

  [Personal pricing](https://www.malwarebytes.com/pricing)

  Protect your personal devices and data

  [Small or home office pricing](https://www.malwarebytes.com/pricing/teams)

  Protect your team’s devices and data – no IT skills needed

  [Corporate pricing](https://www.threatdown.com/pricing/?utm_campaign=mwb-referral&utm_source=malwarebytes.com&utm_medium=referral&utm_content=cat-en-us-navbar-pricing-business-pricing-click)

  Explore award-winning endpoint security for your business
* [Partners](https://www.malwarebytes.com/partners)
* Resources

  < Resources

  [![Malwarebytes Labs](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/07/mwb-labs-159px.svg)](https://www.malwarebytes.com/blog)

  + [Security terms glossary](https://www.malwarebytes.com/glossary)
  + [Threat Center](https://www.malwarebytes.com/blog/threats)
  + [Cybersecurity News](https://www.malwarebytes.com/blog)

  + [About Malwarebytes](https://www.malwarebytes.com/company)
  + [Press](https://www.malwarebytes.com/press/)
  + [Careers](https://www.malwarebytes.com/jobs)

  [Cybersecurity Resource Center](https://www.malwarebytes.com/cybersecurity)

  + [Antivirus](https://www.malwarebytes.com/cybersecurity/basics/antivirus)
  + [Malware](https://www.malwarebytes.com/malware)
  + [Phishing](https://www.malwarebytes.com/phishing)
  + [Ransomware](https://www.malwarebytes.com/ransomware)
  + [Small business hub](https://www.malwarebytes.com/small-business)
  + [See all articles](https://www.malwarebytes.com/cybersecurity)
* Help

  < Support

  [Malwarebytes Help Center](https://help.malwarebytes.com/hc/en-us)

  Malwarebytes and Teams Customers

  [ThreatDown Business Support](https://support.threatdown.com/hc/en-us/?utm_campaign=mwb-referral&utm_source=malwarebytes.com&utm_medium=referral&utm_content=cta-navbar-support-Threatdown-business-click)

  Nebula and Oneview Customers

  [Community Forums](https://forums.malwarebytes.com/)

Free Download

Search
Search

Search Malwarebytes.com

Search for:

![git logo](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/01/asset_upload_file97293_255583.jpg?w=736)

[News](https://www.malwarebytes.com/blog/category/news)

# Update now! Two critical flaws in Git’s code found, patched

Posted: January 19, 2023
 by [Jovi Umawing](https://www.malwarebytes.com/blog/authors/jumawing)

In a sponsored security source code audit, security experts from X41 D-SEC GmbH (Eric Sesterhenn and Markus Vervier) and GitLab (Joern Schneeweisz) found two notable critical flaws in Git’s code. A vulnerability on Git could generally compromise source code repositories and developer systems, but “wormable” ones could result in large-scale breaches, according to the high-level [audit report](https://x41-dsec.de/security/research/news/2023/01/17/git-security-audit-ostif/). Microsoft [defines](https://msrc-blog.microsoft.com/2020/07/14/july-2020-security-update-cve-2020-1350-vulnerability-in-windows-domain-name-system-dns-server/) a flaw as “wormable” if it doesn’t rely on human interaction, instead it allows [malware](https://www.malwarebytes.com/malware) to spread from one vulnerable system to another.

The two critical flaws, tracked as **[CVE-2022-23521](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23521)** and **[CVE-2022-41903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41903)**, could allow threat actors to potentially run malware after taking advantage of overflow weaknesses in a system’s memory.

A total of eight vulnerabilities were found in Git’s code. On top of the critical ones we mentioned, the experts also found one rated medium, one high, and four rated low severity. 27 other issues found don’t have a direct security impact.

A copy of the full audit report from X41 and GitLab can be found [here](https://www.x41-dsec.de/static/reports/X41-OSTIF-Gitlab-Git-Security-Audit-20230117-public.pdf).

## Recommendation and workaround

The easiest way to protect against [exploits](https://www.malwarebytes.com/exploits) of these critical vulnerabilities is to upgrade to the latest Git release, which is version **[2.39.1](https://git-scm.com/downloads)**, as well as [update your GitLab instance](https://about.gitlab.com/releases/2023/01/17/critical-security-release-gitlab-15-7-5-released/) to one of these versions: **15.7.5**, **15.6.6**, and **15.5.9**.

* [How to update GitLab](https://about.gitlab.com/update/)
* [How to update GitLab Runner](https://docs.gitlab.com/runner/install/linux-repository.html#updating-the-runner)

Version 2.39.1 of Git for Windows also addresses the flaw tracked as [CVE-2022-41953](https://github.com/git-for-windows/git/security/advisories/GHSA-v4px-mx59-w99c).

The researchers recommend those using Git continue to use safe wrappers and develop strategies to mitigate common memory safety issues. They also discouraged storing length values to signed integer typed variables.

> “Introducing generic hardenings such as sanity checks on data input length, and the use of safe wrappers can improve the security of the software in the short term. The usage of signed integer typed variables to store length values should be banned. Additionally, the software could benefit from compiler level checks regarding the use of integer and long variable types for length and size values. Enabling the related compiler warnings during the build process can help identify the issues early in the development process.”

Per [BleepingComputer](https://www.bleepingcomputer.com/news/security/git-patches-two-critical-remote-code-execution-security-flaws/), users who cannot upgrade to address CVE-2022-41903 may want to apply this workaround instead:

* Disable ‘git archive’ in untrusted ...