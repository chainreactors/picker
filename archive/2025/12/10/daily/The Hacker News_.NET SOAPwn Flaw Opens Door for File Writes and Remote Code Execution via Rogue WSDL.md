---
title: .NET SOAPwn Flaw Opens Door for File Writes and Remote Code Execution via Rogue WSDL
url: https://thehackernews.com/2025/12/net-soapwn-flaw-opens-door-for-file.html
source: The Hacker News
date: 2025-12-10
fetch_date: 2025-12-11T03:25:10.969805
---

# .NET SOAPwn Flaw Opens Door for File Writes and Remote Code Execution via Rogue WSDL

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [.NET SOAPwn Flaw Opens Door for File Writes and Remote Code Execution via Rogue WSDL](https://thehackernews.com/2025/12/net-soapwn-flaw-opens-door-for-file.html)

**Dec 10, 2025**Ravie LakshmananEnterprise Security / Web Services

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinnS9vb2LFKF6s5fAoVyttBrJ95yYGilrXcgWROlH3mnc3beTVNzu1Km1jBS92RliRTTah0jkHemQXiksFryQVbwuifWpzWqz1uN4JFrqiEEKM3_kB2xdKhRydMPYkn4lwrN9v2deQDGeM44_9B-2KMk1pvRHNA-PW7G7QoPYUzZDFmuNFW7lCEjJyyIUp/s790-rw-e365/ms.net.jpg)

New research has uncovered exploitation primitives in the .NET Framework that could be leveraged against enterprise-grade applications to achieve remote code execution.

WatchTowr Labs, which has codenamed the "invalid cast vulnerability" **SOAPwn**, [said](https://labs.watchtowr.com/soapwn-pwning-net-framework-applications-through-http-client-proxies-and-wsdl/) the issue impacts Barracuda Service Center RMM, Ivanti Endpoint Manager (EPM), and Umbraco 8. But the number of affected vendors is likely to be longer given the widespread use of .NET.

The findings were [presented today](https://blackhat.com/eu-25/briefings/schedule/#soapwn-pwning-net-framework-applications-through-http-client-proxies-and-wsdl-49018) by watchTowr security researcher Piotr Bazydlo at the Black Hat Europe security conference, which is being held in London.

SOAPwn essentially allows attackers to abuse Web Services Description Language (WSDL) imports and HTTP client proxies to execute arbitrary code in products built on the foundations of .NET due to errors in the way they handle Simple Object Access Protocol ([SOAP](https://blog.postman.com/soap-api-definition/)) messages.

"It is usually abusable through SOAP clients, especially if they are dynamically created from the attacker-controlled WSDL," Bazydlo said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

As a result, .NET Framework [HTTP client proxies](https://httpwebclientprotocol) can be manipulated into using file system handlers and achieve arbitrary file write by passing as URL something like "file://<attacker-controlled input>" into a SOAP client proxy, ultimately leading to code execution. To make matters worse, it can be used to overwrite existing files since the attacker controls the full write path.

In a hypothetical attack scenario, a threat actor could leverage this behavior to supply a Universal Naming Convention ([UNC](https://learn.microsoft.com/en-us/dotnet/standard/io/file-path-formats#unc-paths)) path (e.g., "file://attacker.server/poc/poc") and cause the SOAP request to be written to an SMB share under their control. This, in turn, can allow an attacker to capture the NTLM challenge and crack it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieQ3-_dVbUk2iEvyQzEGIRIqmBNqWR05hgOneb434b72hFAIgEpFJT65YRArG1W_zNO47R7O-zesR7_IDC_bYpobG-VAluLsuqwyivpedjKEtTZiBEWsIv48dxVOqHPOToiC8o7CL_ZEPhIKywnbJCPpaj2AfSsSPNHXE49-35bMh-vn71MHVEy9dntZ-h/s2600/flaw.png)

That's not all. The research also found that a more powerful exploitation vector can be weaponized in applications that generate HTTP client proxies from WSDL files using the [ServiceDescriptionImporter](https://learn.microsoft.com/en-us/dotnet/api/system.web.services.description.servicedescriptionimporter) class by taking advantage of the fact that it does not validate the URL used by the generated HTTP client proxy.

In this technique, an attacker can provide a URL that points to a WSDL file they control to vulnerable applications, and obtain remote code execution by dropping a fully functional ASPX web shell or additional payloads like CSHTML web shells or PowerShell scripts.

Following responsible disclosure in March 2024 and July 2025, Microsoft has opted not to fix the vulnerability, stating the issue stems from either an application issue or behavior, and that "users should not consume untrusted input that can generate and run code."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

The findings illustrate how expected behavior in a popular framework can become a potential exploit path that leads to NTLM relaying or arbitrary file writes. The issue has since been addressed in Barracuda Service Center RMM [version 2025.1.1](https://campus.barracuda.com/product/managedworkplace/doc/93200432/release-notes/) ([CVE-2025-34392](https://nvd.nist.gov/vuln/detail/CVE-2025-34392), CVSS score: 9.8) and Ivanti EPM [version 2024 SU4 SR1](https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html#ivanti-releases-fix-for-critical-epm-flaw) ([CVE-2025-13659](https://nvd.nist.gov/vuln/detail/cve-2025-13659), CVSS score: 8.8).

"It is possible to make SOAP proxies write SOAP requests into files rather than sending them over HTTP," Bazydlo said. "In many cases, this leads to remote code execution through webshell uploads or PowerShell script uploads. The exact impact depends on the application using the proxy classes."

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

[.NET framework](https://thehackernews.com/search/label/.NET%20framework)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[en...