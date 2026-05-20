---
title: Popular GitHub Action Tags Redirected to Imposter Commit to Steal CI/CD Credentials
url: https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html
source: The Hacker News
date: 2026-05-19
fetch_date: 2026-05-20T06:05:28.572290
---

# Popular GitHub Action Tags Redirected to Imposter Commit to Steal CI/CD Credentials

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Popular GitHub Action Tags Redirected to Imposter Commit to Steal CI/CD Credentials](https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html)

**Ravie Lakshmanan**May 19, 2026Software Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgc7jpVO6HhBuEBTjkwmNjYhKlFmhhmytOqNZHYuGP-dNWrf3AoyE68yoKj77elddOX4Ps2x9jSuwhi5sE-QjK_oEjLXgQW9e6EHx6W0G7qTqYTM3fZh1AQTyrgm2o-PFBeD9ryHnC6fDmK5MYKUzBjU_pJibTilnm1d99WSQkJux6PXXRydkYW5d15Ada-/s1700-e365/step.jpg)

In yet another software supply chain attack, threat actors have compromised the popular GitHub Actions workflow, **actions-cool/issues-helper**, to run malicious code that harvests sensitive credentials and exfiltrates them to an attacker-controlled server.

"Every existing tag in the repository has been moved to point to an imposter commit that does not appear in the action's normal commit history," StepSecurity researcher Varun Sharma [said](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials). "That commit contains malicious code that exfiltrates credentials from CI/CD pipelines that run the action."

An [imposter commit](https://www.chainguard.dev/unchained/what-the-fork-imposter-commits-in-github-actions-and-ci-cd) refers to a deceptive software supply chain attack strategy in which malicious code is injected into a project by referencing a commit or tag that exists only in an adversary-controlled fork, rather than the original trusted repository. As a result, attackers can bypass standard Pull Request (PR) reviews and achieve arbitrary code execution.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The imposter commit, per the cybersecurity company, contains code that, upon being executed within a GitHub Actions runner, performs a series of actions -

* Downloads the Bun JavaScript runtime to the runner.
* Reads memory from the Runner.Worker process to extract credentials.
* Makes an outbound HTTPS call to an attacker-controlled domain ("t.m-kosche[.]com") to transmit the stolen data.

StepSecurity said 15 tags associated with a second GitHub action, "actions-cool/maintain-one-comment" have also been compromised with the same functionality.

GitHub has since [disabled access to the repository](https://github.com/actions-cool/maintain-one-comment/) due to a "violation of GitHub's terms of service." It's currently not known what led the Microsoft-owned subsidiary to this decision.

Interestingly, the exfiltration domain "t.m-kosche[.]com" has been [observed](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html) in the latest wave of the Mini Shai-Hulud campaign targeting npm packages from the @antv ecosystem, indicating the two clusters of activity could be related.

In a statement shared with The Hacker News, Philipp Burckhardt, head of threat intelligence at Socket, said the @antv npm compromise is likely linked to the actions-cool hack, citing overlaps in the exfiltration domain.

"That points to the same Mini Shai-Hulud activity cluster, not a separate npm-only incident," Burckhardt added. "We're still being careful about the exact initial access path, but the overlap is strong enough that we're treating them as related."

"Because every tag now resolves to malicious commits, any workflow that references the action by version pulls the malicious code on its next run," StepSecurity said. "Only workflows pinned to a known-good full commit SHA are unaffected."

*(The story was updated after publication to include a response from Socket.)*

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

[CI/CD](https://thehackernews.com/search/label/CI/CD), [Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [GitHub Actions](https://thehackernews.com/search/label/GitHub%20Actions), [Malware](https://thehackernews.com/search/label/Malware), [Mini Sha-Hulud](https://thehackernews.com/search/label/Mini%20Sha-Hulud), [NPM](https://thehackernews.com/search/label/NPM), [Software Security](https://thehackernews.com/search/label/Software%20Security), [StepSecurity](https://thehackernews.com/search/label/StepSecurity), [Supply Chain Attack](https://thehackernews.com/search/label/Supply%20Chain%20Attack)

⚡ Top Stories This Week

[![Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](data:image/svg+xml;base64... "Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak")

Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](https://thehackernews.com/2026/05/ollama-out-of-bounds-read-vulnerability.html)

[![Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](data:image/svg+xml;base64... "Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence")

Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html)

[![On-Prem Microsoft Exchange Server C...