---
title: Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git
url: https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html
source: The Hacker News
date: 2026-07-25
fetch_date: 2026-07-26T05:24:36.566221
---

# Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git](https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html)

**Swati Khandelwal**Jul 25, 2026Vulnerability / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRIN1sheAdScq7AX9pLc07esRzQ18-0vBJ7hz9DlVhggVAImXrhYM_zxN0N6hJ2inDkBCnzRCXHR3Kv3I0QwyiVWkAMu7p949JSjgK611r48deMbrSN8iDD78aJdfxEeO_Jy6JFwOfPL_8M0RKEBl1RFO7ufvop1XG9-tdms7VRyvONXoteuCYp9Rg-FM/s1700-e365/gitlab.gif)

Security researchers at [depthfirst](https://depthfirst.com/gitlab-rce-oj-spill) published [working exploit code](https://github.com/wupco/gitlab-rce-demo) on July 24 for a GitLab flaw that GitLab patched six weeks earlier, on June 10. It runs commands as `git` on any self-managed `18.11.3` server that has not taken the update.

Any authenticated user who can push to a project can run it. The attacker commits a crafted Jupyter notebook and opens its commit diff, which leaks a heap pointer. Enough of those and an automated probe can locate the libraries in memory. Two more notebooks then fire the payload. No administrator rights, no CI or runner access, no victim interaction, no access to anyone else's project.

GitLab did not file the fix as a security fix. A review by The Hacker News found the Oj `3.17.3` bump listed under bug fixes in the [June 10 patch release](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-0-2-released/), not in the security-fix table. There is no CVE, no CVSS score, and no mention of the notebook-diff chain. Operators who triaged that release against the security table had no reason to treat it as urgent.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Two memory corruption bugs in Oj, a Ruby JSON parser implemented largely in native C, make the chain work. [depthfirst](https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html) says its system flagged them autonomously, and researchers chained them by hand.

GitLab's notebook renderer, an in-tree gem called `ipynbdiff`, passes repository-controlled `.ipynb` JSON to `Oj::Parser.usual.parse` inside a long-lived Puma worker, so attacker-controlled bytes reach Oj's manually managed C memory inside the application process.

One bug writes past a fixed 1,024-byte nesting stack until it controls the parser's `start` callback. The other truncates a 65,565-byte object key to 29 in a signed 16-bit field and returns a live heap pointer, which GitLab renders into the diff. The leak locates libc, and the write points the callback at `system()`.

| Component | Affected | First fixed |
| --- | --- | --- |
| GitLab CE/EE | 15.2.0 to 18.10.7 | 18.10.8 |
| GitLab CE/EE | 18.11.0 to 18.11.4 | 18.11.5 |
| GitLab CE/EE | 19.0.0 to 19.0.1 | 19.0.2 |
| Oj gem | 3.13.0 to 3.17.1 | 3.17.3 |

All tiers are affected, CE and EE, Free through Ultimate. Ruby itself is not. Oj `3.17.2` carried other fixes from the same review but not these two.

Upgrade to `18.10.8`, `18.11.5`, or `19.0.2`. Neither GitLab nor depthfirst offers a workaround for anyone who cannot.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiKTyaaLkhwstQr3NKKNz65EvIXQgyvfFLQ-FJU7bXyQu8z40Wjm_CNFPnYSNqUOqYXgT0ClkMj-FG-E1KYhlD5y0NOUUTo8Z3s7YECp1045Gm3MqxsXVckEbtGCAw_94koZXNPhNmlz6aQ5VTTTxfpNMIai4APKbZNYUQrsQpXdLvdoosjhWRauoy1GQ/s1700-e365/git-exploited.png)

The trap is Helm and Operator: check the GitLab version inside the [Webservice image](https://docs.gitlab.com/charts/installation/version_mappings/) running Puma, not the chart or Operator version. Anything on 15.2 through 18.9 gets no backport, because those lines sit outside GitLab's [security-maintained patch trains](https://docs.gitlab.com/policy/maintenance/), so those installs have to move to a supported release instead.

Commands run as `git`, the account behind Puma. How far that goes depends on how the install is isolated. In reach: source code, Rails secrets, service credentials, CI/CD data, and internal services the application can talk to.

The public exploit is built for GitLab `18.11.3` on x86-64. Gadget offsets, register state, and jemalloc behavior all came from that image, and a recovered library base holds only until the Puma master restarts, so this is not drop-in against an arbitrary target.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrEy9jEFSadp95ztaH87-97Z_U9V94nUsE-BsrdwSR8ETPJDyCjy63vNxc-O26z6VhA3nDOrU24lJqNdy24bfNxGPxGxXNRvM_XCwnZ7ukY5wDnXKsvDZN42aCT1JFYXZZGoZFEtSQgbba742oPTEgEbtoa0GBYWWkkkU43P1wPq-LByZPJfbzwZsb1RiI/s728-e100/sygnia-d-1.png)](https://thn.news/sygnia-webinar)

The Oj bugs are general; porting the exploit is real work. depthfirst measured five to ten minutes for the memory search on a fresh two-worker install and projects one to two hours on longer-running ones. Its [writeup](https://depthfirst.com/research/going-depthfirst-achieving-gitlab-rce-via-two-ruby-memory-corruption-vulnerabilities) has the full chain.

depthfirst reported the Oj bugs on May 21, the maintainer [merged fixes](https://github.com/ohler55/oj/pull/1014) on May 27, and Oj [`3.17.3`](https://github.com/ohler55/oj/releases/tag/v3.17.3) shipped June 4. The GitLab chain went to GitLab on June 5, was confirmed on June 8, and was patched on June 10. depthfirst says it is not aware of in-the-wild exploitation, and that GitLab reproduced the RCE independently. Its wider Oj review produced nine more CVE advisories, none of them this chain.

The Hacker News has asked GitLab why the fix was not classified as a security issue and whether a CVE will be assigned, and asked depthfirst about exploit portability. Responses are pending.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn...