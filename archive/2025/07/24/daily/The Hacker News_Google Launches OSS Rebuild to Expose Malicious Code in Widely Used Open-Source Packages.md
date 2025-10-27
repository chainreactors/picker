---
title: Google Launches OSS Rebuild to Expose Malicious Code in Widely Used Open-Source Packages
url: https://thehackernews.com/2025/07/google-launches-oss-rebuild-to-expose.html
source: The Hacker News
date: 2025-07-24
fetch_date: 2025-10-06T23:56:04.963643
---

# Google Launches OSS Rebuild to Expose Malicious Code in Widely Used Open-Source Packages

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

# [Google Launches OSS Rebuild to Expose Malicious Code in Widely Used Open-Source Packages](https://thehackernews.com/2025/07/google-launches-oss-rebuild-to-expose.html)

**Jul 23, 2025**Ravie LakshmananSoftware Integrity / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVTbR6LJir_eI7N7gkOjMM6_7gbgGB2mlSN35MVS3dyyhxfdxlxJDA-l72RHV3JQkbQDI27mwgjsqhxeljRf_npW8U0kFfybyj9LwxpxxvEGPDWdyY_9fVZNabLzItXSUddM7NicNYPe8Z2hi_g3tNEelWKacPECSL-2rmzzirRBdJ8eCUXse7zPrF34KQ/s790-rw-e365/google.jpg)

Google has announced the launch of a new initiative called **OSS Rebuild** to bolster the security of the open-source package ecosystems and prevent software supply chain attacks.

"As supply chain attacks continue to target widely-used dependencies, OSS Rebuild gives security teams powerful data to avoid compromise without burden on upstream maintainers," Matthew Suozzo, Google Open Source Security Team (GOSST), [said](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html) in a blog post this week.

The project aims to provide build provenance for packages across the Python Package Index (Python), npm (JS/TS), and Crates.io (Rust) package registries, with plans to extend it to other open-source software development platforms.

With OSS Rebuild, the idea is to leverage a combination of declarative build definitions, build instrumentation, and network monitoring capabilities to produce trustworthy security metadata, which can then be used to validate the package's origin and ensure it has not been tampered with.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Through automation and heuristics, we determine a prospective build definition for a target package and rebuild it," Google said. "We semantically compare the result with the existing upstream artifact, normalizing each one to remove instabilities that cause bit-for-bit comparisons to fail (e.g., archive compression)."

Once the package is reproduced, the build definition and outcome is published via [SLSA Provenance](https://thehackernews.com/2022/10/google-launches-guac-open-source.html) as an attestation mechanism that allows users to reliably verify its origin, repeat the build process, and even customize the build from a known-functional baseline.

In scenarios where automation isn't able to fully reproduce the package, OSS Rebuild offers a manual build specification that can be used instead.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitnYiFmAA5C3XnJTik64rlFOc4tDfxtToK0-yk4LVKOUy-NDGm2bNcxfcMlrfSpcL-XvH4TsGoOyc4BGGz65B3SGUi9ef-Jx49ZyZbQI4wYvOo4jQlHHMYYTW88Is4MwcTTfGlVfl_cz4A7AtRc4nL5KH3uVUzErCnAOTf8pQoPuWK6_YyzvHmxS7SqwEd/s790-rw-e365/oss.png)

OSS Rebuild, the tech giant noted, can help detect different categories of supply chain compromises, including -

* Published packages that contain code not present in the public source repository (e.g., [@solana/web3.js](https://thehackernews.com/2024/12/researchers-uncover-backdoor-in-solanas.html))
* Suspicious build activity (e.g., [tj-actions/changed-files](https://thehackernews.com/2025/04/spotbugs-access-token-theft-identified.html))
* Unusual execution paths or suspicious operations embedded within a package that are challenging to identify through manual review (e.g., [XZ Utils](https://thehackernews.com/2024/04/malicious-code-in-xz-utils-for-linux.html))

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Besides securing the software supply chain, the solution can improve Software Bills of Materials (SBOMs), speed up vulnerability response, strengthen package trust, and eliminate the need for CI/CD platforms to be in charge of an organization's package security.

"Rebuilds are derived by analyzing the published metadata and artifacts and are evaluated against the upstream package versions," Google [said](https://github.com/google/oss-rebuild). "When successful, build attestations are published for the upstream artifacts, verifying the integrity of the upstream artifact and eliminating many possible sources of compromise."

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

[Automation](https://thehackernews.com/search/label/Automation)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DevSecOps](https://thehackernews.com/search/label/DevSecOps)[Google](https://thehackernews.com/search/label/Google)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Package Management](https://thehackernews.com/search/label/Package%20Management)[Python](https://thehackernews.com/search/label/Python)[Rust](https://thehackernews.com/search/label/Rust)[Software Integrity](https://thehackernews.com/search/label/Software%20Integrity)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)[vulnerability management](https://thehackernews.com/search/label/vulnerability%20management)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effect...