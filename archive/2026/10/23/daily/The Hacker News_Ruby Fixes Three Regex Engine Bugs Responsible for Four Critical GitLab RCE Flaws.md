---
title: Ruby Fixes Three Regex Engine Bugs Responsible for Four Critical GitLab RCE Flaws
url: https://thehackernews.com/2026/10/ruby-fixes-three-regex-engine-bugs.html
source: The Hacker News
date: 2026-10-23
fetch_date: 2026-10-24T06:48:21.463086
---

# Ruby Fixes Three Regex Engine Bugs Responsible for Four Critical GitLab RCE Flaws

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Ruby Fixes Three Regex Engine Bugs Responsible for Four Critical GitLab RCE Flaws](https://thehackernews.com/2026/10/ruby-fixes-three-regex-engine-bugs.html)

**Swati Khandelwal**Oct 23, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjA5n8ST_yuElQgTwbfq1oFnVAoiTvZCW_Ct1b8lT_OQ9dnyeXfocrqzTUJJ1t920YaEa-7Sonxl9KlthV4x7lXI3dmJxc9_S11NjWRJ6dcgfsX4UGhv0KFWZsZrzXKpjh92JPyDdHPlCPQh1AHd0YKM44sVcc9d-57r8_BdrIb3V06MWfk8bRAy4kDU6I/s1700-nu-rw-lo-l85-e365/ruby-rce.jpg)

Ruby has released versions 4.0.9, 3.4.12, and 3.3.13 to fix three bugs in Onigmo, the regular expression engine built into the language. The bugs lie behind four critical security flaws that GitLab patched over the past month.

GitLab found that a specially crafted pattern could corrupt memory while Ruby compiles it, potentially leading to code execution on its own servers.

Ruby says any application that builds a regular expression from text an attacker controls is affected, not just GitLab.

### Which Applications Are Affected

In [its advisory](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves/), Ruby said an application is affected only if it compiles a regular expression from a string an attacker controls. That happens when a program passes such a string to Regexp.new, Regexp.union or Regexp.compile, or places it inside a pattern through interpolation, as in /#{input}/.

Applications that only use regular expressions written by their own developers are not affected.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Ruby fixed the bugs in 4.0.9, 3.4.12, and 3.3.13. The 3.4.12 and 3.3.13 releases are the first in their series to carry any of the three fixes.

* Ruby 4.0: upgrade to [4.0.9](https://www.ruby-lang.org/en/news/2026/10/23/ruby-4-0-9-released/)
* Ruby 3.4: upgrade to [3.4.12](https://www.ruby-lang.org/en/news/2026/10/23/ruby-3-4-12-released/)
* Ruby 3.3: upgrade to [3.3.13](https://www.ruby-lang.org/en/news/2026/10/23/ruby-3-3-13-released/)

An earlier release from the same week, 4.0.8, does not include the fix for one of the flaws, [CVE-2026-110264](https://www.cve.org/CVERecord?id=CVE-2026-110264), so 4.0 users should install 4.0.9.

Ruby 3.2 and earlier will not get a fix. Ruby 3.2 [reached end of life](https://www.ruby-lang.org/en/downloads/branches/) on April 1, 2026, and 3.2.11 was its final release. Ruby recommends moving to 3.4 or 4.0.

If you cannot upgrade yet, the advisory says to stop compiling regular expressions from untrusted input.

Two defenses that look like they would help do not. Setting Regexp.timeout does not stop these bugs. Capping the length of a pattern is also unreliable because short patterns can trigger bugs.

### How the Bugs Reached GitLab

GitLab compiles regular expressions supplied by its users, such as the patterns in a CI/CD configuration. It found that crafted patterns could corrupt memory as Ruby compiled them, and it issued four CVEs between [September 23](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-1-released/) and [October 21](https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html), fixing each by shipping a patched Ruby.

The first two, disclosed on September 23, each need a logged-in account and were rated 9.9 out of 10. The two from [October](https://thehackernews.com/2026/10/gitlab-patches-cvss-100-flaw-that-could.html), [CVE-2026-97229](https://www.cve.org/CVERecord?id=CVE-2026-97229) on the 12th and CVE-2026-110264 on the 21st, need no account and were rated 10.0, the maximum. CVE-2026-110264 reaches every GitLab version from 7.0 onward.

A researcher using the handle joaxcar reported all four through GitLab's bug bounty program. As of October 23, none of the four was listed in CISA's Known Exploited Vulnerabilities catalog.

### No Ruby CVE, for Now

Ruby has not requested CVE identifiers of its own for these fixes, "at least for now," it said, and told users to track the issues by GitLab's four CVE numbers instead.

That leaves a gap for anyone who scans by CVE. GitLab's CVE records name only GitLab as the affected product, so a scanner that checks those records against installed Ruby versions has nothing to match.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Ruby has treated this kind of bug as a vulnerability before, assigning CVE numbers to fixes in [2022](https://www.ruby-lang.org/en/news/2022/04/12/double-free-in-regexp-compilation-cve-2022-28738/) and [2024](https://www.ruby-lang.org/en/news/2024/04/23/arbitrary-memory-address-read-regexp-cve-2024-27282/), even though it has long been unsafe to build a regular expression from untrusted input.

Its [documentation](https://docs.ruby-lang.org/en/master/Regexp.html#class-regexp-timeouts) still describes untrusted patterns only as a denial-of-service risk. Ruby said it will update its advisory if it requests any CVE identifiers.

### For GitLab Administrators

Self-managed GitLab instances need the release that fixes CVE-2026-110264. GitLab [shipped it](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/) on October 21 and backported it as far as version 18.11.13.

* 19.5.1
* 19.4.3
* 19.3.6
* 19.2.9
* 19.1.9
* 19.0.10
* 18.11.13

GitLab.com already runs the patched version, and GitLab Dedicated tenants on recent internal releases need no action, GitLab said. Because GitLab bundles its own copy of Ruby and patched it there, installing one of these fixed versions applies the fix.

GitLab also published [detection rules](https://gitlab.com/gitlab-security-oss/tldr/-/blob/main/Detections/platforms/GitLab/Vulnerability%20Detections/onigmo_native_worker_crash.md) that self-managed administrators can use to look for signs of exploitation attempts.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndn...