---
title: New GootLoader Campaign Targets Users Searching for Bengal Cat Laws in Australia
url: https://thehackernews.com/2024/11/new-gootloader-campaign-targets-users.html
source: The Hacker News
date: 2024-11-12
fetch_date: 2025-10-06T19:23:33.545542
---

# New GootLoader Campaign Targets Users Searching for Bengal Cat Laws in Australia

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

# [New GootLoader Campaign Targets Users Searching for Bengal Cat Laws in Australia](https://thehackernews.com/2024/11/new-gootloader-campaign-targets-users.html)

**Nov 11, 2024**Ravie LakshmananMalware / SEO Poisoning

[![GootLoader Campaign](data:image/png;base64... "GootLoader Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhrS-fLloWm-F_Q0TakcWCqk5s3TjzZp_CYCtv6DfSaTWHypIZtMiamAos2nYnh4xAJ83BzLIV-CeO5v2DYjPeg-P9RQJFYaP-aodTqLresfJrm7EmDUgy0G6vQJYC-T83Qv3MYr8WrJacec_l-w0e9QHaE3rez3BLefqmSfd6OurMY3zG93RHzzMNXaLP/s790-rw-e365/aus.png)

In an unusually specific campaign, users searching about the legality of Bengal Cats in Australia are being targeted with the **GootLoader** malware.

"In this case, we found the GootLoader actors using search results for information about a particular cat and a particular geography being used to deliver the payload: 'Are Bengal Cats legal in Australia?,'" Sophos researchers Trang Tang, Hikaru Koike, Asha Castle, and Sean Gallagher [said](https://news.sophos.com/en-us/2024/11/06/bengal-cat-lovers-in-australia-get-psspsspssd-in-google-driven-gootloader-campaign/) in a report published last week.

[GootLoader](https://thehackernews.com/2024/07/gootloader-malware-delivers-new.html), as the name implies, is a malware loader that's typically distributed using search engine optimization (SEO) poisoning tactics for initial access.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Specifically, the malware is deployed onto victim machines when searching for certain terms like legal documents and agreements on search engines like Google surface booby-trapped links pointing to compromised websites that host a ZIP archive containing a JavaScript payload.

Once installed, it makes way for a second-stage malware, often an information stealer and remote access trojan dubbed [GootKit](https://thehackernews.com/2021/03/gootkit-rat-using-seo-to-distribute.html), although it has also been observed delivering other families such as Cobalt Strike, IcedID, Kronos, REvil, and SystemBC in the past for post-exploitation.

[![GootLoader Campaign](data:image/png;base64... "GootLoader Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK99Pre7WfanDDw0brJ73DFUCZlVh50n41m8Xt6TFlmlPSOI4dBRvtR44hTvGVXkFh_wnN0hURPreRqZpv-V4cscdCXfUQ6GzeVtDBMhBVvwK6Gbm1_uMuwduFaKzHRmJ3ahjLORCw5y8LDviv78wFCL9IYSFnwJbZ1LpI0OLphXtauSxVKRq7_utxs5fm/s790-rw-e365/alware.png)

The latest attack chain is no different in that searches for "Do you need a license to own a Bengal cat in Australia" surface results that include a link to a legitimate-but-infected website belonging to a Belgium-based LED display maker, from where victims are prompted to download a ZIP archive.

Present within the ZIP archive is a JavaScript file that's then responsible for kicking off a multi-stage attack chain that culminates in the execution of a PowerShell script capable of harvesting system information and fetching additional payloads. It's worth noting that an identical campaign was [documented](https://thehackernews.com/2024/07/gootloader-malware-delivers-new.html) by Cybereason earlier this July.

Sophos said it did not observe the deployment of GootKit in the case the company analyzed, thereby preventing the download of additional malware.

"GootLoader is one of a number of continuing malware-delivery-as-a-service operations that heavily leverage search results as a means to reach victims," the researchers said. "The use of search engine optimization, and abuse of search engine advertising to lure targets to download malware loaders and dropper, are not new—GootLoader has been doing this since at least 2020."

## Update

Google's Mandiant Managed Defense team, which is tracking GootLoader under the name SLOWPOUR, said it also discovered a similar campaign that leverages searches for "california law break room requirements" to deliver the malware.

"Victims perform a search, often for business-related documents such as legal requirements, agreements, or contracts, and navigate to a compromised site with information purportedly related to their search," it [said](https://www.googlecloudcommunity.com/gc/Community-Blog/Finding-Malware-Detecting-GOOTLOADER-with-Google-Security/ba-p/823766) in a technical report published late last month.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Both the archive and the JavaScript file have names that closely resemble the victim's search query. This naming scheme helps trick the user into extracting and executing the malware."

That having said, there are indications that the attack chains have shifted tactics for initial access as of early November 2024. A security researcher, who goes by the online alias [GootLoader](https://gootloader.wordpress.com/2024/11/07/gootloaders-pivot-from-seo-poisoning-pdf-converters-become-the-new-infection-vector/), has revealed that the threat actors behind the operation have pivoted from SEO poisoning tactics to fake PDF converters pushed via malvertising campaigns.

"This shift from SEO poisoning and legal terms — clearly aimed at corporations — could now target everyday users, including those looking to convert PDFs to DOCX," the researcher [noted](https://gootloader.wordpress.com/2024/11/07/gootloaders-pivot-from-seo-poisoning-pdf-converters-become-the-new-infection-vector/) in a brief published last week.

*(The story was updated after publication to include new information about the GootLoader campaigns.)*

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

*...