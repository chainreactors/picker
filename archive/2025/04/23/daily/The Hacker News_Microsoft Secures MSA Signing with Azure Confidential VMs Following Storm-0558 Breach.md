---
title: Microsoft Secures MSA Signing with Azure Confidential VMs Following Storm-0558 Breach
url: https://thehackernews.com/2025/04/microsoft-secures-msa-signing-with.html
source: The Hacker News
date: 2025-04-23
fetch_date: 2025-10-06T22:09:33.151046
---

# Microsoft Secures MSA Signing with Azure Confidential VMs Following Storm-0558 Breach

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Microsoft Secures MSA Signing with Azure Confidential VMs Following Storm-0558 Breach](https://thehackernews.com/2025/04/microsoft-secures-msa-signing-with.html)

**Apr 22, 2025**Ravie LakshmananIdentity Management / Cloud Security

[![Microsoft Secures MSA Signing](data:image/png;base64... "Microsoft Secures MSA Signing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqE7AbDpfQhavgfDSZVtvme4uOW9Gj37qcxGqQfhp1wcmtDXh2bZMoGcHsoWPCxoCEIStIZWm8OsQFrGR9tg8w4rjDm3q_YohE8iC0ywYiNnu07ZvX8HtBszGBOH-Hh4lKl9-UI2FA9uXal_gCE6oS5YbTz18CCn_fHfAlZBz8YBGnidA44FLE6AAlSG9o/s790-rw-e365/ms-keys.jpg)

Microsoft on Monday announced that it has moved the Microsoft Account (MSA) signing service to Azure confidential virtual machines (VMs) and that it's also in the process of migrating the Entra ID signing service as well.

The disclosure comes about seven months after the tech giant [said](https://www.microsoft.com/en-us/security/blog/2024/09/23/securing-our-future-september-2024-progress-update-on-microsofts-secure-future-initiative-sfi/) it completed updates to Microsoft Entra ID and MS for both public and United States government clouds to generate, store, and automatically rotate access token signing keys using the Azure Managed Hardware Security Module (HSM) service.

"Each of these improvements helps mitigate the attack vectors that we suspect the actor used in the 2023 Storm-0558 attack on Microsoft," Charlie Bell, Executive Vice President for Microsoft Security, [said](https://www.microsoft.com/en-us/security/blog/2025/04/21/securing-our-future-april-2025-progress-report-on-microsofts-secure-future-initiative/) in a post shared with The Hacker News ahead of publication.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Microsoft also noted that 90% of identity tokens from Microsoft Entra ID for Microsoft apps are validated by a hardened identity Software Development Kit (SDK) and that 92% of employee productivity accounts are now using phishing-resistant multifactor authentication (MFA) to mitigate risk from advanced cyber attacks.

Besides isolating production systems and enforcing a two-year retention policy for security logs, the company also said it's protecting 81% of production code branches using MFA through proof-of-presence checks.

"To reduce the risk of lateral movement, we are piloting a project to move customer support workflows and scenarios into a dedicated tenant," it added. "Security baselines are enforced across all types of Microsoft tenants, and a new tenant provisioning system automatically registers new tenants in our security emergency response system."

The changes are part of its Secure Future Initiative ([SFI](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative)), which the company characterized as the "largest cybersecurity engineering project in history and most extensive effort of its kind at Microsoft."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1RUTicS-hciLlSx2eax4Qc_H3WAhWPM3HgNmPJIgsj8lMKVRpsOYJal8NCUsFcbJnpOR35PFiBnuuZjwBqbwvnjtVuuecgevrj5v9W4LHx-zFOGo4mB7ui8b7k-gEhyphenhyphenpy53aIckVUhUng5kKYRoFEpxeDrpcJRXZSbRM8-ASgE8BgNb-hg6xb8FCbJ0bS/s790-rw-e365/paved.jpg)

The SFI gained traction last year in response to a report from the U.S. Cyber Safety Review Board (CSRB), which [criticized](https://thehackernews.com/2024/04/us-cyber-safety-board-slams-microsoft.html) the tech giant for a series of avoidable errors that led to the breach of nearly two dozen companies across Europe and the U.S. by a China-based nation-state group called Storm-0558 in 2023.

Microsoft, in July 2023, revealed that a [validation error](https://thehackernews.com/2023/07/microsoft-bug-allowed-hackers-to-breach.html) in its source code allowed for Azure Active Directory (Azure AD) or Entra ID tokens to be forged by Storm-0558 using an MSA consumer signing key to infiltrate several organizations and gain unauthorized email access for subsequent exfiltration of mailbox data.

Late last year, the company also [launched](https://thehackernews.com/2024/11/microsoft-launches-windows-resiliency.html) a Windows Resiliency Initiative to improve security and reliability and avoid causing system disruptions like what happened during the infamous [CrowdStrike update incident](https://thehackernews.com/2024/08/crowdstrike-reveals-root-cause-of.html) in July 2024.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This includes a feature called Quick Machine Recovery, which enables IT administrators to run specific fixes on Windows PCs even in situations when the machines are unable to boot. It's built into the Windows Recovery Environment (WinRE).

"Unlike traditional repair options that rely on user intervention, it activates automatically when the system detects failure," Patch My PC's Rudy Ooms [said](https://patchmypc.com/quick-machine-recovery-cloud-based-remediation) late last month.

"The whole cloud remediation process is pretty straightforward: it checks if flags/settings like CloudRemediation, AutoRemediation, and optionally HeadlessMode are set. If the environment meets the conditions (such as an available network and required plugin), Windows silently initiates recovery."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on W...