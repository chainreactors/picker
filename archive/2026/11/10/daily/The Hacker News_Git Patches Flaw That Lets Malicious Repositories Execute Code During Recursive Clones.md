---
title: Git Patches Flaw That Lets Malicious Repositories Execute Code During Recursive Clones
url: https://thehackernews.com/2026/11/git-patches-flaw-that-lets-malicious.html
source: The Hacker News
date: 2026-11-10
fetch_date: 2026-11-11T08:35:39.284583
---

# Git Patches Flaw That Lets Malicious Repositories Execute Code During Recursive Clones

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

# [Git Patches Flaw That Lets Malicious Repositories Execute Code During Recursive Clones](https://thehackernews.com/2026/11/git-patches-flaw-that-lets-malicious.html)

**Swati Khandelwal**Nov 10, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoPlLYj_xfJ8bsfRTONwa3estE9I2un_9OBx2fVuxEp-zoiADgipn-gGOeU4TqqyjqjrCpoGXC4jmuF7o1e_PUMbr-QoHDdPZEDWavb4VbjtWbOxMfmz-E9fIPT2DHEXYCN53l2jtiJGVfEFjHsR8gaHeyF59Yii0oTnP73vaslLWPzuideEGxTy6S9U/s1700-nu-rw-lo-l85-e365/gits.jpg)

A flaw in Git can let a malicious repository run an attacker's code on a computer that clones it recursively, together with its submodules. The Git project fixed it this week in Git 2.56.1, with matching fixes for the 2.50 through 2.55 series in 2.50.2, 2.51.3, 2.52.1, 2.53.1, 2.54.1 and 2.55.1.

The flaw, tracked as **CVE-2026-111760**, is an integer truncation in how Git handles its index. An extremely long path in a repository can pass Git's safety check, but Git then writes it to disk under a shorter name that an attacker can set to .git.

This lets an attacker replace a submodule's .git file with a symbolic link to a folder holding malicious hooks or configuration. Hooks are programs Git runs at set points, so once Git uses that folder, the attacker's code can run.

Submodules matter here because Git refuses to replace a .git folder with a symbolic link, but in a freshly cloned submodule, .git is a file.

The fixed versions, listed in the Git project's [release announcement](https://lore.kernel.org/git/xmqqh5hosgw5.fsf%40gitster.g/), refuse such extremely long paths before their length can be cut short.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

GitHub, which ships Git in its own tools, explained the fixes in a [detailed write-up](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/). It advises installing a fixed version from your operating system or Git distributor, and updating any app that ships its own copy of Git.

The company has already applied the fixes to github.com and GitHub Enterprise Cloud. For GitHub Enterprise Server, they are in versions 3.19.15, 3.20.11, 3.21.9 and 3.22.4.

Fixed versions of GitHub Desktop and the GitHub Copilot app are being prepared. GitHub Codespaces and GitHub Actions will also get the fixed Git.

Git for Windows had not released a version based on Git 2.56.1 as of Tuesday at 19:09 UTC, a check of its release tags by The Hacker News found.

Until a fixed version is installed, GitHub suggests these steps, which do not replace the fixes:

* Clone only from servers you trust.
* Do not recursively clone repositories you do not trust.
* Do not merge content or tags you do not trust.
* Do not process binary patches or fast-import streams from sources you do not trust.

The Git releases also fix five other flaws:

* **CVE-2026-113408:** When someone clones an empty repository over Git protocol v2, a malicious server can send a branch name that contains path traversal. With the files reference backend, a later update to that branch can then write outside Git's reference folder.
* **CVE-2026-114467:** Merging a tag that carries more than two GPG signatures corrupts Git's stack memory and can cause a denial of service. Hosting services that run such merges for users may also be affected.
* **CVE-2026-114469:** A binary patch that expands to a very large size can get past Git's patch size limit of about 1 GiB and crash Git with an out-of-bounds read.
* **CVE-2026-105437:** A very large merge, with many conflicts and a large conflict-marker-size attribute, can make Git write past the end of a buffer that is too small, corrupting heap memory.
* **CVE-2026-114466:** Three git fast-import features, rewrite-submodules-from, rewrite-submodules-to and export-pack-edges, could be used to read arbitrary files or to create files and add data to them. Git now rejects them in an input stream unless --allow-unsafe-features is set.

GitLab, which assigned CVE-2026-105437, said code-hosting servers are most likely to be targeted through git merge-tree. A server may run that command to check whether a pull or merge request can be merged.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The conflict-marker-size attribute can be set in a .gitattributes file committed to a repository. If a server reads attributes from the repository, any user who can push branches and open a pull or merge request can trigger the flaw.

As a workaround for this flaw, servers that cannot upgrade yet can add conflict-marker-size=7 to each repository's info/attributes file, or turn off those merge checks for untrusted repositories.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

...