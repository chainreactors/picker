---
title: Hackers Found a Way Around GitHub SHA Pinning. This Webinar Explains How to Close the Gap
url: https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html
source: The Hacker News
date: 2026-11-24
fetch_date: 2026-11-25T10:48:29.638445
---

# Hackers Found a Way Around GitHub SHA Pinning. This Webinar Explains How to Close the Gap

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Hackers Found a Way Around GitHub SHA Pinning. This Webinar Explains How to Close the Gap](https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html)

**The Hacker News**Nov 24, 2026Supply Chain Security / DevSecOps

[![](data:image/png;base64...)](https://thehacker.news/github-actions-security)

Pinning GitHub Actions to an exact version of their code, known as SHA pinning, has become the go-to defense against software supply chain attacks. Attackers have already found a way around it.

In March 2026, the hackers who hijacked Trivy, a widely used open-source security scanner, planted malicious code that looked like it came from GitHub's official checkout tool. They even labeled it a security fix. Teams pinned to it would have passed every check.

The trick works because GitHub lets copies of a project, called forks, share code with the original. In May, the same technique hit the popular actions-cool/issues-helper tool, stealing credentials from the pipelines that ran it.

The lesson: pinning guarantees the code won't change, but not who wrote it.

That gap is the focus of an upcoming webinar, [GitHub Actions Security Beyond SHA Pinning](https://thehacker.news/github-actions-security). If your team treats pinning as the finish line, **save your seat** to learn what it actually protects you from, and what it doesn't.

## Immutability Is Not Provenance

Pinning earned its reputation. When the tj-actions/changed-files compromise repointed tags to a malicious commit across more than 23,000 repositories in March 2025, teams that had pinned to SHAs were unaffected.

GitHub now lets administrators enforce pinning as an organization-wide policy, and few security teams argue against it.

📅 **Save Your Spot:** [Learn Why “Best Practice” Won’t Stop the Next GitHub Actions Attack](https://thehacker.news/github-actions-security)

But a pinned SHA leaves three questions unanswered:

* **Authorship:** A SHA doesn't tell you who wrote the commit. Any fork commit can be pinned.
* **Project membership:** Org-level enforcement checks that a reference is a 40-character SHA, not that the commit actually lives in the upstream project.
* **Runtime:** A Docker-based action pinned to a SHA can still build its image at runtime, pulling in dependencies that were never frozen.

With agentic development pushing more code through CI than ever, each of those gaps gets exercised more often and reviewed less closely.

## GitHub's Lockfiles Help. They Don't Finish the Job.

GitHub's 2026 Actions security roadmap, published March 26, put deterministic dependency locking front and center. Workflow lockfiles entered public preview on October 14 and became generally available on October 28, 2026. They tie every run to recorded commits for actions and their transitive dependencies, even if a tag moves later.

That's real progress. Locked commits must exist on a branch of the source repository, which blunts fork-only impostors. But GitHub's own changelog is clear that locking "does not determine whether the dependency itself is safe." Commit authorship and runtime builds remain open; immutable releases only help when maintainers opt in, and lockfiles aren't currently supported on GitHub Enterprise Server.

Not sure where your pipelines fall in that gap? **[Register for the webinar](https://thehacker.news/github-actions-security)** for a clear-eyed breakdown of what GitHub's roadmap fixes and what it still leaves to you.

## What You'll Learn

[![](data:image/png;base64...)](https://thehacker.news/github-actions-securityg)

Led by **Erika Heidi**, Staff Developer Relations Engineer at **Chainguard**, the session draws a hard line between immutability and provenance, and covers:

* What org-level pin enforcement actually verifies, and the false confidence it can create
* How impostor commits work, and why GitHub's repository network makes them possible
* What GitHub's Actions roadmap addresses, and what it doesn't
* Other ways to close the trust gap, including a curated catalog of vetted actions

## Who Should Attend

Platform and DevOps engineers who own CI/CD, AppSec and DevSecOps teams writing pipeline policy, and security leaders who signed off on SHA pinning as "done." If your workflows pull in third-party actions, this session is for you.

Attackers have already shown they can disguise a malicious commit as a hardening fix. The next one won't announce itself either.

**[Register now for GitHub Actions Security Beyond SHA Pinning](https://thehacker.news/github-actions-security)**, pick the session time that works for you, and find out what your pins aren't telling you.

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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

[CI/CD Security](https://thehackernews.com/search/label/CI/CD%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [DevSecOps](https://thehackernews.com/search/label/DevSecOps), [GitHub Actions](https://thehackernews.com/search/label/GitHub%20Actions), [Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain), [Supply Chain Security](https://thehackernews.com/search/label/...