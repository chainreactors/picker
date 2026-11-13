---
title: Attacker Used 4,837 Hijacked GitHub Accounts to Run a CI Secret Stealer in 1,806+ Repositories
url: https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html
source: The Hacker News
date: 2026-11-12
fetch_date: 2026-11-13T09:07:46.214313
---

# Attacker Used 4,837 Hijacked GitHub Accounts to Run a CI Secret Stealer in 1,806+ Repositories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Attacker Used 4,837 Hijacked GitHub Accounts to Run a CI Secret Stealer in 1,806+ Repositories](https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html)

**Swati Khandelwal**Nov 12, 2026Supply Chain / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1-4OiOkGLcK3fAr2HdhALOfc_BqR21440TsjUIuCNzv4YL0lWRC3lvUjE1vu2RdVfjunxi80gMQyGpjvUdWzMRtthW8_-hFOJ79YhFzJrNGgoKDPYXm2OaWOsN8kgBELqOPs5s9QKL4qzQzu_3NEEqHygpfQzKYxDRIQeFgMHj24oyPyaslUemke-loU/s1700-nu-rw-lo-l85-e365/github.jpg)

Starting Tuesday, an attacker used stolen credentials for 4,837 GitHub accounts to plant a secret stealer in repositories those accounts could write to, according to Aikido Security, a security software company.

The stealer is built to take the secrets and cloud credentials that a repository's CI workflows can reach. It ran in at least 1,806 repositories, where the attacker has likely collected those credentials, the company says.

Each attack started with a pull request titled docs: dependency audit notes, opened from a branch named **wfx-docs** to test whether the account could write to the repository. These test pull requests were opened in 61,764 repositories, and the stealer followed in some of them.

In a [separate analysis](https://safedep.io/blog/github-actions-wfx-credential-stealer), researchers at SafeDep, which sells software supply chain security tools, counted 8,093 repositories that received malicious commits between 12:46 UTC on Tuesday and 04:36 UTC today. That count covers every repository that received malicious commits, not only those where the stealer ran. Their search covered only the default branches of public repositories, so the true total is higher, the researchers say.

In 7,309 of those repositories, the stealer was added to an existing workflow. In 771, it came as an npm postinstall hook, which also runs on a developer's machine during npm install.

After pushing the stealer, the attacker usually reverted the change within minutes. Where the stealer ran, its logs were deleted, usually along with the run itself. In those repositories, every secret and cloud role available to the workflows should be treated as compromised.

More pull requests with the same title were opened early today, after the company's own GitHub search ended on Wednesday, a check by The Hacker News found. Three that were checked, opened between 05:04 and 05:38 UTC, came from wfx-docs branches. It is not clear whether the stealer followed.

Any account that opened one of the attacker's test pull requests is compromised, even if the stealer never ran, Aikido said in its [technical analysis](https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories). The analysis does not explain how the attacker obtained the credentials.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

SafeDep's researchers advise owners of affected repositories to revoke the commit author's tokens, OAuth app grants, SSH keys, and sessions, and to turn on 2FA. Owners should also rotate every secret and variable the repository can read. Anyone who ran npm install on an affected commit should treat that machine as compromised and rotate its keys.

In most other repositories that received a test, nothing was pushed afterward, or the stealer did not run due to the repository's settings or the account's permissions. The figures cover only the public repositories the company could see.

The tests also reached repositories that the compromised accounts did not own. Of the test pull requests, 10,431 were submitted via collaborator or organization access, and 92% of those were still open when the company checked.

### Signs a Repository Was Hit

Check for these signs, from Tuesday onward, in any repository you can write to:

* **Branch:** `wfx-docs`
* **Branch:** `chore/[a-z0-9]{8}`, short-lived
* **Branch:** `ci-check-[0-9]{4}`
* **Pull request title:** `docs: dependency audit notes`
* **Commit message:** `ci: refresh build cache`, which adds about 1,500 lines to an existing workflow
* **Commit message:** `chore: add ci helper`, which adds a `.ci-xxxxxx.sh` script and a `postinstall` hook in `package.json` that runs it on any npm install
* **Commit message:** `chore: add dependency audit workflow`, which adds `.github/workflows/build-audit-xxxxxx.yml` on a `chore/` branch
* **Commit message:** `chore: initial commit`, pushed before a new workflow file in an empty repository
* **Commit message:** `ci: restore`
* **Commit message:** `ci: cleanup`
* **SHA-256 (stealer script):** `89695abb392d5cfd4972672961e644bb46baa98aa1ed7173c2a2816c762735cf`
* **IP:** `194.150.166[.]244:8080/exfil`
* **IP:** `18.143.168[.]96:8080/exfil`
* **IP:** `153.75.82[.]159:8080`

A repository can show no **wfx-loot** artifacts, **wfx- cache** entries, or **WFX-BEGIN** step summaries and still have lost data. A missing run number on the attacker's commit is the more reliable sign that the stealer ran.

The stealer sends data by HTTP POST to the addresses above or to a Telegram chat, the SafeDep researchers found. In a sample of 200 payload commits, about a fifth used Telegram only.

The stealer is built to collect credentials from every source on the runner, according to the company. They include GitHub Actions secrets and variables, the workflow's GITHUB\_TOKEN, OIDC and Actions runtime tokens, keys for AI services, and secrets in the memory of the runner's own processes. It reads credential files for AWS, Azure, GCP, Kubernetes, npm, PyPI, SSH, and other tools from their usual locations.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtSga7KnuQEVNRq8P0ipc-BpahQII_9sitqTPWaJCTeBzd-RM6vhmdtvdYwUFCOW_4uHZMeWasFS3FjiegphcFoKKN96nl_BXvSlg6Jx3tUnNiUdgFIOl_ILO63QpjgEnPBXgzyefhyHL2h04sNUzP2AUdV_MZ9bjklxoloNbPUn1sXRkFTepkON8fwSrd/s1700-nu-rw-lo-l85-e365/github-actions.jpg)

It also copie...