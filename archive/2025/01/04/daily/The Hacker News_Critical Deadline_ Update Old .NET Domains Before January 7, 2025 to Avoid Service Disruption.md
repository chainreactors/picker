---
title: Critical Deadline: Update Old .NET Domains Before January 7, 2025 to Avoid Service Disruption
url: https://thehackernews.com/2025/01/critical-deadline-update-old-net.html
source: The Hacker News
date: 2025-01-04
fetch_date: 2025-10-06T20:13:24.471941
---

# Critical Deadline: Update Old .NET Domains Before January 7, 2025 to Avoid Service Disruption

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

# [Critical Deadline: Update Old .NET Domains Before January 7, 2025 to Avoid Service Disruption](https://thehackernews.com/2025/01/critical-deadline-update-old-net.html)

**Jan 03, 2025**Ravie LakshmananDevOps / Software Development

[![.NET Domains](data:image/png;base64... ".NET Domains")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiI6_S3vqEiLs-QJcbQfgqYygCdle3V7kFbtvebhtLOVL_9n6MFMEXbxvT0uMsNKU83NrYsO9YGPY1ojIgy4B_ZNRSGK8dVqp6CxXASbVWOu5ykJivSVzs0ApHCMgbrlnGH_Ddw_K1qdTWCA2_dif0-PgN-V-0Vgh_7bCcCGWEWuMZ8lVp9ODazd5-wuR1a/s790-rw-e365/NET.png)

Microsoft has announced that it's making an "unexpected change" to the way .NET installers and archives are distributed, requiring developers to update their production and DevOps infrastructure.

"We expect that most users will not be directly affected, however, it is critical that you validate if you are affected and to watch for downtime or other kinds of breakage," Richard Lander, a program manager on the .NET team, [said](https://devblogs.microsoft.com/dotnet/critical-dotnet-install-links-are-changing/) in a statement last week.

The move is the result of the fact that some .NET binaries and installers are hosted on Azure Content Delivery Network (CDN) domains that end in .azureedge[.]net -- dotnetcli.azureedge.net and dotnetbuilds.azureedge.net -- which are hosted on Edgio.

Last month, web infrastructure and security company Akamai acquired select assets from Edgio following its bankruptcy. As part of this transition, the Edgio platform is scheduled to end service on January 15, 2025.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Given that the .azureedge[.]net domains could cease to become unavailable in the future, Microsoft [said](https://learn.microsoft.com/en-us/azure/cdn/edgio-retirement-faq) it's migrating to [Azure Front Door CDNs](https://learn.microsoft.com/en-us/azure/frontdoor/migrate-cdn-to-front-door). The Windows maker said it will automatically migrate customers' workloads by January 7, 2025, if no action is taken.

However, it's worth noting that automatic migration will not be possible for endpoints with \*.vo.msecnd.net domains. Users who plan to migrate to Akamai or another CDN provider are also required to set the Feature Flag DoNotForceMigrateEdgioCDNProfiles before January 7, 2025, so as to prevent automatic migration to Azure Front Door.

"Note you will have until January 14, 2025 to complete your migration to another CDN, but again Microsoft cannot guarantee your services will be available on the Edgio platform before this date," Microsoft said.

"Please be advised we will need to halt all configuration changes to Azure CDN by Edgio profiles starting on January 3, 2025. This means you will not be able to update your CDN profile configuration, but your services on Azure CDN from Edgio will still operate until you are migrated or the Edgio platform is shut down on January 15, 2025. If you apply the DoNotForceMigrateEdgioCDNProfiles feature flag before January 3, your configuration will not be frozen for changes."

While relying on \*.azureedge[.]net and \*.azurefd[.]net isn't recommended due to availability risks, users have the temporary option of migrating to Azure Front Door while retaining the domains.

"To ensure greater flexibility and avoid a single point of failure, it's advisable to adopt a custom domain as soon as possible," Microsoft warns.

Furthermore, to avoid security concerns with a bad actor acquiring the azureedge[.]net domain for malware distribution or poisoning the software supply chain, the tech giant said it has taken control of it. But as for why the old domain names could not be used to resolve to the new servers, it's being [said](https://github.com/dotnet/core/issues/9671) that "this option wasn't being made available."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Users are recommended to scan their codebases for references to azureedge[.]net and update them to the following -

* Update dotnetcli.azureedge.net to builds.dotnet.microsoft.com
* Update dotnetcli.blob.core.windows.net to builds.dotnet.microsoft.com

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

[.NET](https://thehackernews.com/search/label/.NET)[Akamai](https://thehackernews.com/search/label/Akamai)[Azure](https://thehackernews.com/search/label/Azure)[Cloud Migration](https://thehackernews.com/search/label/Cloud%20Migration)[Content Delivery Network](https://thehackernews.com/search/label/Content%20Delivery%20Network)[DevOps](https://thehackernews.com/search/label/DevOps)[Microsoft](https://thehackernews.com/search/label/Microsoft)[security](https://thehackernews.com/search/label/security)[software development](https://thehackernews.com/search/label/software%20development)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-cont...