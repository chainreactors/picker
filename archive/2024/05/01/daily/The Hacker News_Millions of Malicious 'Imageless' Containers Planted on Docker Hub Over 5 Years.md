---
title: Millions of Malicious 'Imageless' Containers Planted on Docker Hub Over 5 Years
url: https://thehackernews.com/2024/04/millions-of-malicious-imageless.html
source: The Hacker News
date: 2024-05-01
fetch_date: 2025-10-06T17:27:23.027056
---

# Millions of Malicious 'Imageless' Containers Planted on Docker Hub Over 5 Years

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

# [Millions of Malicious 'Imageless' Containers Planted on Docker Hub Over 5 Years](https://thehackernews.com/2024/04/millions-of-malicious-imageless.html)

**Apr 30, 2024**Ravie LakshmananDocker Hub / Supply Chain Attack

[![Docker Hub](data:image/png;base64... "Docker Hub")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgV60ycag3gu19fGfBY_Q4zNcxY0p1dxw9j1AUl1ZjhUHOEj1jwT23M-UTQ_FR32i9FMaKoSE7POh9-eZ_U8a620DwdQtcHRvPSj5IUASrCgsOXV4b0TWPEWYWxW9AXJ167zMChZtkBNAdz8lMM-Azz2YO_WP0Qmj1MTI6kH1BHZ-kPQl_MvMGnl_zRuDjY/s790-rw-e365/docker-hub.png)

Cybersecurity researchers have discovered multiple campaigns targeting [Docker Hub](https://docs.docker.com/docker-hub/) by planting millions of malicious "imageless" containers over the past five years, once again underscoring how open-source registries could pave the way for supply chain attacks.

"Over four million of the repositories in Docker Hub are imageless and have no content except for the repository documentation," JFrog security researcher Andrey Polkovnichenko [said](https://jfrog.com/blog/attacks-on-docker-with-millions-of-malicious-repositories-spread-malware-and-phishing-scams/) in a report shared with The Hacker News.

What's more, the documentation has no connection whatsoever to the container. Instead, it's a web page that's designed to lure users into visiting phishing or malware-hosting websites.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Of the 4.6 million imageless Docker Hub repositories uncovered, 2.81 million of them are said to have been used as landing pages to redirect unsuspecting users to fraudulent sites as part of three broad campaigns -

* Downloader (repositories created in the first half of 2021 and September 2023), which advertises links to purported pirated content or cheats for video games but either directly links to malicious sources or a legitimate one that, in turn, contains JavaScript code that [redirects](https://isc.sans.edu/diary/How%2BMalware%2BCampaigns%2BEmploy%2BGoogle%2BRedirects%2Band%2BAnalytics/19843) to the malicious payload after 500 milliseconds.

* E-book phishing (repositories created in mid-2021), which redirects users searching for e-books to a website ("rd.lesac.ru") that, in turn, urges them to enter their financial information to download the e-book.

* Website (thousands of repositories created daily from April 2021 to October 2023), which contains a link to an online diary-hosting service called Penzu in some cases, or a harmless piece of text, suggesting that it could have been used during early testing phases.

The payload delivered as part of the downloader campaign is designed to contact a command-and-control (C2) server and transmit system metadata, following which the server responds with a link to cracked software.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEir15BATdfWuvJ-nw9BU2Ip9pPrhXA21BYxR7n8-kpcLfiZW3sXEE7uXgX3gyX_eKwJnUEe2n6KcgxazttrpGdayg-R3aLD2iqWjA-gGsH80dtrtzvt7nIQ1TUTFbBGmZ5ADIKxODW0QoKnWG_HZz8dnRbA_ViMgpMRUnqs-q3BEZSY1HVtujQdzjgJXjNQ/s790-rw-e365/Img1.png)

It's suspected that the attacks may be part of a larger malware operation, which could involve adware or monetization schemes that derive monetary benefit out of distributing third-party software.

On the other hand, the exact goal of the website cluster is currently unclear, with the campaign also propagated on sites that have a lax content moderation policy.

JFrog said it counted a total of 208,739 fake accounts that the threat actors used to create the malicious and unwanted repositories. Docker has since taken down all of them following responsible disclosure.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The most concerning aspect of these three campaigns is that there is not a lot that users can do to protect themselves at the outset, other than exercising caution," Shachar Menashe, senior director of security research at JFrog, said in a statement shared with The Hacker News.

"We're essentially looking at a malware playground that in some cases has been three years in the making. These threat actors are highly motivated and are hiding behind the credibility of the Docker Hub name to lure victims."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4KxJuo1o1ocJztVfvTM5Sa_nbou8UsUuJ3DHso2P0XBKQ4wUHy_ONM57UGRBEN2hrIHb4imVRxr9W_udUzqZF6MX5yR7vckexQxPms4jkjL2HPzdRzXjTJjzQjIxSM10Tkgwe7VsjzWnJW2z2dKf_-8SJmCWV-E9R_8XTKMuUXNriJZDxP1tTpJlmCkHo/s790-rw-e365/Img4.png)

With threat actors taking [painstaking efforts](https://thehackernews.com/2024/04/popular-rust-crate-liblzma-sys.html) to poison well known utilities, as evidenced in the case of the [XZ Utils compromise](https://securelist.com/xz-backdoor-story-part-2-social-engineering/112476/), it's imperative that developers exercise caution when it comes to downloading packages from open-source ecosystems.

"As Murphy's Law suggests, if something can be exploited by malware developers, it inevitably will be, so we expect that these campaigns can be found in more repositories than just Docker Hub," Menashe said.

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_sh...