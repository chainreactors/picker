---
title: Researchers Uncover New Bugs in Popular ImageMagick Image Processing Utility
url: https://thehackernews.com/2023/02/researchers-uncover-new-bugs-in-popular.html
source: The Hacker News
date: 2023-02-02
fetch_date: 2025-10-04T05:32:03.546235
---

# Researchers Uncover New Bugs in Popular ImageMagick Image Processing Utility

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

# [Researchers Uncover New Bugs in Popular ImageMagick Image Processing Utility](https://thehackernews.com/2023/02/researchers-uncover-new-bugs-in-popular.html)

**Feb 01, 2023**Ravie LakshmananVulnerability

[![ImageMagick Image Processing](data:image/png;base64... "ImageMagick Image Processing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDmANjNdKMraBT1f4IA8KMB8DLu6siOgn5YDeGdES5bnrAscdIrj5zHhxp2E2tThaKb1Eq5eYX6FFlvsvh5s5u79uceZrjpRFufLwUJw-DlSmyjnO3vhipAXvWZKZCJUNFgNSdT1tGQaS90UP8yQTcB2zVAZF3nFuMFO88L1FIl7m44Ze1NnfvNH3C/s790-rw-e365/image.png)

Cybersecurity researchers have disclosed details of two security flaws in the open source [ImageMagick software](https://imagemagick.org/) that could potentially lead to a denial-of-service (DoS) and information disclosure.

The two issues, which were identified by Latin American cybersecurity firm Metabase Q in version 7.1.0-49, were [addressed](https://github.com/ImageMagick/ImageMagick/commit/05673e63c919e61ffa1107804d1138c46547a475) in ImageMagick [version 7.1.0-52](https://github.com/ImageMagick/ImageMagick/releases/tag/7.1.0-52), released in November 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A brief description of the flaws is as follows -

* **CVE-2022-44267** - A DoS vulnerability that arises when parsing a PNG image with a filename that's a single dash ("-")
* **CVE-2022-44268** - An information disclosure vulnerability that could be exploited to read arbitrary files from a server when parsing an image

That said, an attacker must be able to upload a malicious image to a website using ImageMagick so as to weaponize the flaws remotely. The specially crafted image, for its part, can be created by inserting a [text chunk](https://www.w3.org/TR/PNG-Chunks.html#:~:text=4.2.7.%20tEXt%20Textual%20data) that specifies some metadata of the attacker's choice (e.g., "-" for the filename).

[![ImageMagick Image Processing](data:image/png;base64... "ImageMagick Image Processing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEik8njbVX30vldmg3ovrTNEQPxZBuKaZqmj4fSoevi6Pwx0_HF90VhCjrUHq8TUF7cOY7iO4RFrkQXgTBNtm5LK39KWcvITxcc74wfKm9lbqgNR9DXxty33zuZSmjD_k5cYDrrzxdu7ycu4TS15li5C01A16wUY3zGDFgQUvYiQJZ2kwdNBtJ_6FkE9/s790-rw-e365/poc-1.png)

[![ImageMagick Image Processing](data:image/png;base64... "ImageMagick Image Processing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtekS6Pq1MtNAsWk937aPy2io7q9_5X53uwuLEnO4VrTM-PiIq-j0SLonEICBW76_EAWs9PmEsbZnYvkhedG3pd3E8sEuwTFItrAhyVUzxCEXX4Nqhc4ouHNe-Kmb_3PUsmZBqFnxS0efl17RF-gJAPbo24rFrQckoUY40txi6UWDN32WbAt-RqA67/s790-rw-e365/poc-2.png)

"If the specified filename is '-' (a single dash), ImageMagick will try to read the content from standard input potentially leaving the process waiting forever," the researchers said in a [report](https://www.metabaseq.com/imagemagick-zero-days/) shared with The Hacker News.

In the same manner, if the filename refers to an actual file located in the server (e.g., "/etc/passwd"), an image processing operation carried out on the input could potentially embed the contents of the remote file on the processed image after it's complete.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is not the first time security vulnerabilities have been discovered in ImageMagick. In May 2016, multiple flaws were disclosed in the software, one of which, dubbed [ImageTragick](https://imagetragick.com/), could have been abused to gain remote code execution when processing user-submitted images.

A [shell injection vulnerability](https://insert-script.blogspot.com/2020/11/imagemagick-shell-injection-via-pdf.html) was subsequently revealed in November 2020, wherein an attacker could insert arbitrary commands when converting encrypted PDFs to images via the "-authenticate" command line parameter.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ImageMagick](https://thehackernews.com/search/label/ImageMagick)[Metabase](https://thehackernews.com/search/label/Metabase)[Shell Injection](https://thehackernews.com/search/label/Shell%20Injection)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credent...