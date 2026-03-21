---
title: Magento PolyShell Flaw Enables Unauthenticated Uploads, RCE and Account Takeover
url: https://thehackernews.com/2026/03/magento-polyshell-flaw-enables.html
source: The Hacker News
date: 2026-03-20
fetch_date: 2026-03-21T04:08:41.369160
---

# Magento PolyShell Flaw Enables Unauthenticated Uploads, RCE and Account Takeover

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Magento PolyShell Flaw Enables Unauthenticated Uploads, RCE and Account Takeover](https://thehackernews.com/2026/03/magento-polyshell-flaw-enables.html)

**Ravie Lakshmanan**Mar 20, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmvoo5bgNhw6SuInM6rRH_pdtYFmiDdMlG7hS2GdUJfwhXoOClt29lEpxaqI27b6XOOfX3eO8eHlUM0LA55P9U_HfWgVPyqDWMO01Chkp6aC-is0292EqVXPRjwesdZl9igZ0iD7NdoW8rQhKRVfF7s_I98a8r2YOk3-vjDMEz4eGGVXjmt-nUJpLpM4OL/s1700-e365/mag.jpg)

Sansec is warning of a critical security flaw in Magento's REST API that could allow unauthenticated attackers to upload arbitrary executables and achieve code execution and account takeover.

The vulnerability has been codenamed **PolyShell** by Sansec owing to the fact that the attack hinges on disguising malicious code as an image. There is no evidence that the shortcoming has been exploited in the wild. The unrestricted file upload flaw affects all Magento Open Source and Adobe Commerce versions up to 2.4.9-alpha2.

The Dutch security firm said the problem stems from the fact that Magento's REST API accepts file uploads as part of the custom options for the cart item.

"When a product option has type 'file,' Magento processes an embedded file\_info object containing base64-encoded file data, a MIME type, and a filename," it [said](https://sansec.io/research/magento-polyshell). "The file is written to pub/media/custom\_options/quote/ on the server."

Depending on the web server configuration, the flaw can enable remote code execution via PHP upload or account takeover via stored XSS.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fs-report-d)

Sansec also noted that Adobe fixed the issue in the 2.4.9 pre-release branch as part of [APSB25-94](https://helpx.adobe.com/in/security/products/magento/apsb25-94.html), but leaves current production versions without an isolated patch.

"While Adobe provides a sample web server configuration that would largely limit the fallout, the majority of stores use a custom configuration from their hosting provider," it added.

To mitigate any potential risk, e-commerce storefronts are advised to perform the following steps -

* Restrict access to the upload directory ("pub/media/custom\_options/").
* Verify that nginx or Apache rules prevent access to the directory.
* Scan the stores for web shells, backdoors, and other malware.

"Blocking access does not block uploads, so people will still be able to upload malicious code if you aren't using a specialized WAF [Web Application Firewall]," Sansec said.

The development comes as Netcraft flagged an ongoing campaign involving the compromise and defacement of thousands of Magento e-commerce sites across multiple sectors and geographies. The activity, which commenced on February 27, 2026, involves the threat actor uploading plaintext files to publicly accessible web directories.

"Attackers have deployed defacement txt files across approximately 15,000 hostnames spanning 7,500 domains, including infrastructure associated with prominent global brands, e-commerce platforms, and government services," security researcher Gina Chow [said](https://www.netcraft.com/blog/large-scale-magento-defacement-campaign).

It's currently not clear if the attacks are exploiting a specific Magento vulnerability or misconfiguration, and it's the work of a single threat actor. The campaign has impacted infrastructure belonging to several globally recognized brands, including Asus, FedEx, Fiat, Lindt, Toyota, and Yamaha, among others.

The Hacker News has also reached out to Netcraft to understand if this activity has a connection to PolyShell, and we will update the story if we hear back.

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

[Adobe Commerce](https://thehackernews.com/search/label/Adobe%20Commerce), [API Security](https://thehackernews.com/search/label/API%20Security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Magento](https://thehackernews.com/search/label/Magento), [Malware](https://thehackernews.com/search/label/Malware), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [web security](https://thehackernews.com/search/label/web%20security), [xss](https://thehackernews.com/search/label/xss)

Trending News

[![FortiGate Devices Exploited to Breach Networks and Steal Service Account Credentials](data:image/svg+xml;base64... "FortiGate Devices Exploited to Breach Networks and Steal Service Account Credentials")

FortiGate Devices Exploited to Breach Networks and Steal Service Account Credentials](https://thehackernews.com/2026/03/fortigate-devices-exploited-to-breach.html)

[![Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days](data:image/svg+xml;base64... "Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days")

Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days](https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html)

[![Researche...