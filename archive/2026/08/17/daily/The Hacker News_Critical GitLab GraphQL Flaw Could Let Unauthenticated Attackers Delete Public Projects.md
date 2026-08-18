---
title: Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects
url: https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html
source: The Hacker News
date: 2026-08-17
fetch_date: 2026-08-18T02:54:01.562737
---

# Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects](https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html)

**Swati Khandelwal**Aug 17, 2026Vulnerability / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLiZpsYdSdkh6GE1rDDV3XVwWiGdjWBlx3B1irY9V5RtHt1cv7sQYPaa16y78EJdluo3FTMr5Wq0O2ZCWZjRMdrewgLrGJS3Ii_NLOQKQKN18PEGHhDiSyJtvf8TpdFrrIplaynGWNVmUxdAkyL7E8h_GtKfog8EE_TV25SySHFqbQgK3ChyphenhyphenKaKktnUic/s1700-e365/gitlab.jpg)

GitLab has released security updates to address a critical vulnerability impacting its Community Edition (CE) and Enterprise Edition (EE) software that, under certain conditions, could allow an unauthenticated attacker to remotely modify or delete public projects and user data.

The flaw, tracked as **CVE-2026-19478**, has been rated Critical by GitLab and assigned a CVSS score of 9.4.

Released on August 17, 2026, the [critical patch release](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/) arrived outside the company's usual schedule of twice-monthly updates on the second and fourth Wednesdays, five days after a routine patch release that carried no critical-rated issues.

Only self-managed installations need to act. The fixes are available in GitLab [19.2.4, 19.1.6, 19.0.8, and 18.11.11](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"GitLab.com and GitLab Dedicated are already running the patched version. GitLab.com and GitLab Dedicated customers do not need to take action," the company said.

The following versions are affected -

* All versions from 18.2 before 18.11.11
* 19.0 before 19.0.8
* 19.1 before 19.1.6
* 19.2 before 19.2.4

The fixes do not extend to the 18.2 through 18.10 branches, which fall inside the affected range.

"GitLab has remediated an issue that under certain conditions could allow an unauthenticated user to remotely modify or delete public projects and user data via a GraphQL directive," [GitLab said](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/).

The CVSS vector published for the flaw indicates that it can be exploited over a network by an attacker holding no credentials, and without any action on the part of a victim.

GitLab has not named the GraphQL directive involved or specified what the conditions necessary for exploitation are.

The advisory discloses no exploitation of either flaw, and no public exploit code for them has surfaced on GitHub as of August 18, 2026.

The second issue fixed in the release, **CVE-2026-19650**, has been rated High by GitLab with a CVSS score of 7.1, and concerns a cross-site request forgery (CSRF) weakness in the GraphQL multiplex query handler.

Unlike the critical flaw, it requires user interaction to work.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"GitLab has remediated an issue that under certain conditions could have allowed an unauthenticated user to execute mutations via GET requests due to improper request validation in GraphQL multiplex query handling," the company said.

The company said the update introduces no new migrations and is not expected to require downtime on multi-node deployments.

The disclosure follows a July 2026 report in which researchers [published working exploit code for a separate GitLab flaw](https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html) affecting self-managed servers.

GitLab did not immediately respond to a request for comment.

The company said it makes the issues detailing each vulnerability public on its issue tracker 90 days after the release that patched them. GitLab's June 10, 2026 patch release put that window at 30 days.

That places technical details of both flaws at around mid-November 2026.

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

[API Security](https://thehackernews.com/search/label/API%20Security), [Application Security](https://thehackernews.com/search/label/Application%20Security), [CSRF](https://thehackernews.com/search/label/CSRF), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DevOps Security](https://thehackernews.com/search/label/DevOps%20Security), [Gitlab](https://thehackernews.com/search/label/Gitlab), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](data:image/svg+xml;base64... "Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database")

Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html)

[![Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations]...