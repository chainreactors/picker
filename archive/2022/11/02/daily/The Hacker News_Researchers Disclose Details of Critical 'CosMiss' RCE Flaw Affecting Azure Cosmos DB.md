---
title: Researchers Disclose Details of Critical 'CosMiss' RCE Flaw Affecting Azure Cosmos DB
url: https://thehackernews.com/2022/11/researchers-disclose-details-of.html
source: The Hacker News
date: 2022-11-02
fetch_date: 2025-10-03T21:34:54.602670
---

# Researchers Disclose Details of Critical 'CosMiss' RCE Flaw Affecting Azure Cosmos DB

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

# [Researchers Disclose Details of Critical 'CosMiss' RCE Flaw Affecting Azure Cosmos DB](https://thehackernews.com/2022/11/researchers-disclose-details-of.html)

**Nov 01, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDBzNhfxCV9NX6g4d__6a-w2rkVtsicudwMFp5n2VhIZCO9Aa2WViNma8DbI9DOKNCwZgF5i-FSBxc_Ojed4kKklgKN6INB3e3rbhVx1hESImXDbi-G_22SSUoF-ZJKKZo6pccJOIF-zMWeYFDb5PVoPul7SdwRvaRWk8CfqrzdmGN08rCmkfeSOGM/s790-rw-e365/azure-hack.jpg)

Microsoft on Tuesday said it addressed an authentication bypass vulnerability in [Jupyter Notebooks](https://learn.microsoft.com/en-us/azure/cosmos-db/notebooks-overview) for Azure Cosmos DB that enabled full read and write access.

The tech giant said the problem was introduced on August 12, 2022, and rectified worldwide on October 6, 2022, two days after responsible disclosure from Orca Security, which dubbed the flaw [**CosMiss**](https://orca.security/resources/blog/cosmiss-vulnerability-azure-cosmos-db/).

"In short, if an attacker had knowledge of a Notebook's 'forwardingId,' which is the UUID of the Notebook Workspace, they would have had full permissions on the Notebook without having to authenticate, including read and write access, and the ability to modify the file system of the container running the notebook," researchers Lidor Ben Shitrit and Roee Sagi said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEii9GNCQ3_1OKtxK4WSFx4vqW-MCD9mIxDgF4z1ihM2O_0eTRlHaJ4IzVdd1hDyTf4kmrx6EnYpb9WCJuqNmO09z8KIGyEn0mL1-fG8ZipZ1UN6JuNptGdIY6-8Wn2Xo0A1Nl1Q1Bp5WpUmmiPMKTIIz9lMaHZg3bo6-kkvRkyGFwGIduzmqbKbJlnw/s790-rw-e365/orca.jpg)

This container modification could ultimately pave the way for obtaining remote code execution in the Notebook container by overwriting a Python file associated with the [Cosmos DB Explorer](https://learn.microsoft.com/en-us/azure/cosmos-db/data-explorer) to spawn a reverse shell.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Successful exploitation of the flaw, however, requires that the adversary is in possession of the unique 128-bit forwardingId and that it's put to use within a one-hour window, after which the temporary Notebook is automatically deleted.

"The vulnerability, even with knowledge of the forwardingId, did not give the ability to execute notebooks, automatically save notebooks in the victim's (optional) connected GitHub repository, or access to data in the Azure Cosmos DB account," Redmond [said](https://msrc-blog.microsoft.com/2022/11/01/microsoft-mitigates-vulnerability-in-jupyter-notebooks-for-azure-cosmos-db/).

Microsoft noted in its own advisory that it identified no evidence of malicious activity, adding no action is required from customers. It also described the issue as "difficult to exploit" owing to the randomness of the 128 bit forwadingID and its limited lifespan.

"Customers not using Jupyter Notebooks (99.8% of Azure Cosmos DB customers do NOT use Jupyter notebooks) were not susceptible to this vulnerability," it further said.

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
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Authentication bypass](https://thehackernews.com/search/label/Authentication%20bypass)[Azure](https://thehackernews.com/search/label/Azure)[Cosmos DB](https://thehackernews.com/search/label/Cosmos%20DB)[Jupyter](https://thehackernews.com/search/label/Jupyter)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64.....