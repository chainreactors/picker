---
title: Chainlit AI Framework Flaws Enable Data Theft via File Read and SSRF Bugs
url: https://thehackernews.com/2026/01/chainlit-ai-framework-flaws-enable-data.html
source: The Hacker News
date: 2026-01-21
fetch_date: 2026-01-22T03:36:33.898642
---

# Chainlit AI Framework Flaws Enable Data Theft via File Read and SSRF Bugs

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

# [Chainlit AI Framework Flaws Enable Data Theft via File Read and SSRF Bugs](https://thehackernews.com/2026/01/chainlit-ai-framework-flaws-enable-data.html)

**Ravie Lakshmanan**Jan 21, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOQfYQeWdwmviN0kYk0o1lwduXDGiv53wwizZeyajke-6SGNlGc1wdSk5yUWZ_Bt4-yQrihJrMohBqDcsqStLjmdJ_YfRZ2vM27oKy4LVviBgbJHP71E2MWRRf_d39VMy7BQ2WzIxl-s0ufscfKHo8AL9Dj0W77aRmVM_lNvGAeOwN1Xxf7IGoG7DwTbus/s1600-e365/exploit.jpg)

Security vulnerabilities were uncovered in the popular open-source artificial intelligence (AI) framework [Chainlit](https://pepy.tech/projects/chainlit) that could allow attackers to steal sensitive data, which may allow for lateral movement within a susceptible organization.

Zafran Security [said](https://www.zafran.io/resources/chainleak-critical-ai-framework-vulnerabilities-expose-data-enable-cloud-takeover) the high-severity flaws, collectively dubbed **ChainLeak**, could be abused to leak cloud environment API keys and steal sensitive files, or perform server-side request forgery (SSRF) attacks against servers hosting AI applications.

[Chainlit](https://docs.chainlit.io/get-started/overview) is a framework for creating conversational chatbots. According to statistics shared by the Python Software Foundation, the package has been downloaded over [220,000 times](https://pypistats.org/packages/chainlit) over the past week. It has attracted a total of 7.3 million downloads to date.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Details of the two vulnerabilities are as follows -

* **[CVE-2026-22218](https://nvd.nist.gov/vuln/detail/CVE-2026-22218)** (CVSS score: 7.1) - An arbitrary file read vulnerability in the "/project/element" update flow that allows an authenticated attacker to access the contents of any file readable by the service into their own session due to a lack of validation of user-controller fields
* **[CVE-2026-22219](https://nvd.nist.gov/vuln/detail/CVE-2026-22219)** (CVSS score: 8.3) - An SSRF vulnerability in the "/project/element" update flow when configured with the SQLAlchemy data layer backend that allows an attacker to make arbitrary HTTP requests to internal network services or cloud metadata endpoints from the Chainlit server and store the retrieved responses

"The two Chainlit vulnerabilities can be combined in multiple ways to leak sensitive data, escalate privileges, and move laterally within the system," Zafran researchers Gal Zaban and Ido Shani said. "Once an attacker gains arbitrary file read access on the server, the AI application's security quickly begins to collapse. What initially appears to be a contained flaw becomes direct access to the system's most sensitive secrets and internal state."

For instance, an attacker can weaponize CVE-2026-22218 to read "/proc/self/environ," allowing them to glean valuable information such as API keys, credentials, and internal file paths that could be used to burrow deeper into the compromised network and even gain access to the application source code. Alternatively, it can be used to leak database files if the setup uses SQLAlchemy with an SQLite backend as its data layer.

What's more, if Chainlit is deployed on an Amazon Web Services (AWS) EC2 instance with IMDSv1 enabled, the SSRF vulnerability can be abused to access the link-local address (169.254.169[.]254) and retrieve role endpoints, enabling opportunities for lateral movement within the cloud environment.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigOCtRlYmt68Q5dC5lNsNYLXw03qD9QsDiJzGOYfpH2VpmWWFXfkXZxy5KpkXt6HiPqz1Egmo_i9HQs2EevFMgh5HPTFhrlmcUISd-zIwoqADvyefq4MYISAY_BH-Q1VuPjF2tN5hr_hPq_HUGVifGNRnQjVvh8kFKZNKfH8rJxVDRSAVIrpGFekn4QVbW/s1600-e365/attacker.png)

Following responsible disclosure on November 23, 2025, both vulnerabilities were addressed by Chainlit in [version 2.9.4](https://github.com/Chainlit/chainlit/releases/tag/2.9.4) released on December 24, 2025.

"As organizations rapidly adopt AI frameworks and third-party components, long-standing classes of software vulnerabilities are being embedded directly into AI infrastructure," Zafran said. "These frameworks introduce new and often poorly understood attack surfaces, where well-known vulnerability classes can directly compromise AI-powered systems."

### Flaw in Microsoft MarkItDown MCP Server

The disclosure comes as BlueRock disclosed a similar SSRF vulnerability in Microsoft's MarkItDown Model Context Protocol (MCP) server dubbed MCP fURI that enables arbitrary calling of URI resources, exposing organizations to privilege escalation, SSRF, and data leakage attacks. The shortcoming affects the server when running in an Amazon Web Services (AWS) EC2 instance using [IDMSv1](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

"This vulnerability allows an attacker to execute the Markitdown MCP tool convert\_to\_markdown to call an arbitrary uniform resource identifier (URI)," BlueRock [said](https://www.bluerock.io/post/mcp-furi-microsoft-markitdown-vulnerabilities). "The lack of any boundaries on the URI allows any user, agent, or attacker calling the tool to access any HTTP or file resource."

"When providing a URI to the Markitdown MCP server, this can be used to query the instance metadata of the server. A user can then obtain credentials to the instance if there is a role associated, giving you access to the AWS account, including the access and secret keys."

The agentic AI security company said its analysis of more than 7,000 MCP servers found that over 36.7% of them are likely exposed to similar SSRF vulnerabilities. To mitigate the risk posed by the issue, it's advised to use IMDSv2 to secure against SSRF attacks, implement private IP blocking, restrict access to metadata services, and create an allowlist to prevent data exfiltration.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive conte...