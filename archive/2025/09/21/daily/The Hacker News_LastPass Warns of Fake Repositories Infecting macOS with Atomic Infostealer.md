---
title: LastPass Warns of Fake Repositories Infecting macOS with Atomic Infostealer
url: https://thehackernews.com/2025/09/lastpass-warns-of-fake-repositories.html
source: The Hacker News
date: 2025-09-21
fetch_date: 2025-10-02T20:29:21.865920
---

# LastPass Warns of Fake Repositories Infecting macOS with Atomic Infostealer

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

# [LastPass Warns of Fake Repositories Infecting macOS with Atomic Infostealer](https://thehackernews.com/2025/09/lastpass-warns-of-fake-repositories.html)

**Sep 20, 2025**Ravie LakshmananSoftware Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTi6Dhy7nzXe67ma-c9btG81oYxzpSkP8uMuw_TPUNRLO2uSbZ4ML4n363q5U8Gi3zsxQ2LQSDrMSnwipWYtDsd02K3785fguCkDPLfN8JFw1FXtsXe-MoCwyRbbcYm7RLotDe_r2tUrt4NKF35cxs7VIFdI2s4rJRAvDsD6Ws6VuFqztH2-Ywm1Avw-cg/s790-rw-e365/1000021404.jpg)

LastPass is warning of an ongoing, widespread information stealer campaign targeting Apple macOS users through fake GitHub repositories that distribute malware-laced programs masquerading as legitimate tools.

"In the case of LastPass, the fraudulent repositories redirected potential victims to a repository that downloads the [Atomic](https://thehackernews.com/2025/07/fake-gaming-and-ai-firms-push-malware.html) infostealer malware," researchers Alex Cox, Mike Kosak, and Stephanie Schneider from the LastPass Threat Intelligence, Mitigation, and Escalation (TIME) team [said](https://blog.lastpass.com/posts/attack-targeting-macs-via-github-pages).

Beyond LastPass, some of the popular tools impersonated in the campaign include 1Password, Basecamp, Dropbox, Gemini, Hootsuite, Notion, Obsidian, Robinhood, Salesloft, SentinelOne, Shopify, Thunderbird, and TweetDeck, among others. All the GiHub repositories are designed to target macOS systems.

The attacks involve the use of Search Engine Optimization (SEO) poisoning to push links to malicious GitHub sites on top of search results on Bing and Google, which then instruct users to download the program by clicking the "Install LastPass on MacBook" button, redirecting them a GitHub page domain.

"The GitHub pages appear to be created by multiple GitHub usernames to get around takedowns," LastPass said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The GitHub page is designed to take the user to another domain that provides [ClickFix-style instructions](https://thehackernews.com/2025/06/new-atomic-macos-stealer-campaign.html) to copy and execute a command on the Terminal app, resulting in the deployment of the Atomic Stealer malware.

It's worth noting similar campaigns have been previously leveraged malicious sponsored Google Ads for Homebrew to distribute a multi-stage dropper through a bogus GitHub repository that can run detect virtual machines or analysis environments, and decode and execute system commands to establish connection with a remote server, per [security researcher Dhiraj Mishra](https://medium.com/deriv-tech/brewing-trouble-dissecting-a-macos-malware-campaign-90c2c24de5dc).

In recent weeks, threat actors have been spotted [leveraging](https://thehackernews.com/2025/07/hackers-use-github-repositories-to-host.html) public GitHub repositories to host malicious payloads and distribute them via Amadey, as well as [employ dangling commits](https://thehackernews.com/2025/09/gpugate-malware-uses-google-ads-and.html) corresponding to an official GitHub repository to redirect unwitting users to malicious programs.

### Update

Malwarebytes, in a follow-up report published on September 23, 2025, said the campaign has also employed GitHub repositories to host fake versions of its own software to target Mac users with the Atomic Stealer malware.

"Impersonating brands is sadly commonplace, as scammers take advantage of established brand names to target their victims," the company [said](https://www.malwarebytes.com/blog/news/2025/09/fake-malwarebytes-lastpass-and-others-on-github-serve-malware). "In this case, the cybercriminals' goal is to distribute information stealers."

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

[GitHub](https://thehackernews.com/search/label/GitHub)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[software security](https://thehackernews.com/search/label/software%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://th...