---
title: Microsoft Identifies 3,000 Leaked ASP.NET Keys Enabling Code Injection Attacks
url: https://thehackernews.com/2025/02/microsoft-identifies-3000-publicly.html
source: The Hacker News
date: 2025-02-08
fetch_date: 2025-10-06T20:47:23.154952
---

# Microsoft Identifies 3,000 Leaked ASP.NET Keys Enabling Code Injection Attacks

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

# [Microsoft Identifies 3,000 Leaked ASP.NET Keys Enabling Code Injection Attacks](https://thehackernews.com/2025/02/microsoft-identifies-3000-publicly.html)

**Feb 07, 2025**Ravie LakshmananCloud Security / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVoW40-QIiQLq-Oev6SR4JOxqPvHz6kGrfaNIo8KNE2taMrVwHZ1Ax-KniVuTTjNBeEV93O66RKupYvMB1XRKzo_cstxNkORu7biO_U-Si6GiEyKeXa4dF4wuePLqQdOkz6TGheoQEERNuIp8SmsZKlFbKAPfMSqeQ01Oa6s95PPwbjUnmykx7ugHQCrL0/s790-rw-e365/ms.png)

Microsoft is warning of an insecure practice wherein software developers are incorporating publicly disclosed ASP.NET machine keys from publicly accessible resources, thereby putting their applications in attackers' pathway.

The tech giant's threat intelligence team said it observed limited activity in December 2024 that involved an unknown threat actor using a publicly available, static ASP.NET machine key to inject malicious code and deliver the [Godzilla](https://thehackernews.com/2024/01/apache-activemq-flaw-exploited-in-new.html) post-exploitation framework.

It also noted that it has identified over 3,000 publicly disclosed keys that could be used for these types of attacks, which it's calling [ViewState code injection attacks](https://www.zerodayinitiative.com/blog/2020/2/24/cve-2020-0688-remote-code-execution-on-microsoft-exchange-server-through-fixed-cryptographic-keys).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Whereas many previously known ViewState code injection attacks used compromised or stolen keys that are often sold on dark web forums, these publicly disclosed keys could pose a higher risk because they are available in multiple code repositories and could have been pushed into development code without modification," Microsoft [said](https://www.microsoft.com/en-us/security/blog/2025/02/06/code-injection-attacks-using-publicly-disclosed-asp-net-machine-keys/).

ViewState is a method used in the ASP.NET framework to preserve page and control values between postbacks. This can also include application data that is specific to a page.

"By default, view state data is stored in the page in a hidden field and is encoded using base64 encoding," Microsoft [notes](https://learn.microsoft.com/en-us/previous-versions/aspnet/bb386448%28v%3Dvs.100%29) in its documentation. "In addition, a hash of the view state data is created from the data by using a machine authentication code (MAC) key. The hash value is added to the encoded view state data and the resulting string is stored in the page."

In using a hash value, the idea is to ensure that the view state data has not been corrupted or tampered with by malicious actors. That said, if these keys are stolen or made accessible to unauthorized third-parties, it opens the door to a scenario where the threat actor can leverage the keys to send a malicious ViewState request and execute arbitrary code.

"When the request is processed by ASP.NET Runtime on the targeted server, the ViewState is decrypted and validated successfully because the right keys are used," Redmond noted. "The malicious code is then loaded into the worker process memory and executed, providing the threat actor remote code execution capabilities on the target IIS web server."

Microsoft has provided a [list of hash values](https://github.com/microsoft/mstic/blob/master/RapidReleaseTI/MachineKeys.csv) for the publicly disclosed machine keys, urging customers to [check](https://github.com/microsoft/mstic/blob/master/RapidReleaseTI/MachineKeyScan.ps1) them against the machine keys used in their environments. It has also warned that in the event of a successful exploitation of publicly disclosed keys, merely rotating the keys will not be sufficient as the threat actors may have already established persistence on the host.

To mitigate the risk posed by such attacks, it's advised to not copy keys from publicly available sources and to regularly rotate keys. As a further step to deter threat actors, Microsoft said it removed key artifacts from "limited instances" where they were included in its documentation.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as cloud security company Aqua revealed details of an [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper) bypass that could be exploited to conduct unauthorized actions in Kubernetes environments, including deploying unauthorized container images.

"In the k8sallowedrepos policy, a security risk arises from how the Rego logic is written in the ConstraintTemplate file," researchers Yakir Kadkoda and Assaf Morag [said](https://www.aquasec.com/blog/risks-misconfigured-kubernetes-policy-engines-opa-gatekeeper/) in an analysis shared with The Hacker News.

"This risk is further amplified when users define values in the Constraint YAML file that do not align with how the Rego logic processes them. This mismatch can result in policy bypasses, making the restrictions ineffective."

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

[ASP.NET](https://thehackernews.com/search/label/ASP.NET)[Cloud security](https://thehackernews...