---
title: Researchers Find Over 22,000 Removed PyPI Packages at Risk of Revival Hijack
url: https://thehackernews.com/2024/09/hackers-hijack-22000-removed-pypi.html
source: The Hacker News
date: 2024-09-05
fetch_date: 2025-10-06T18:30:38.931089
---

# Researchers Find Over 22,000 Removed PyPI Packages at Risk of Revival Hijack

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

# [Researchers Find Over 22,000 Removed PyPI Packages at Risk of Revival Hijack](https://thehackernews.com/2024/09/hackers-hijack-22000-removed-pypi.html)

**Sep 04, 2024**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8Hel-8ANHTua9rNhRLRWwf_lWbIrRqnJICcLADWnyPcH-6Lt7nO_FLlyA3rv3jZJZNS-fwVLlVWBvJLEBursDobXtXZn9_YkCe8Sjy0z8hYWA4vS0Lu0CwHX7UlwSRaPqgjtJxUUshj2FwrbfXfiF7R4w2Q8iAwsHiKSuPwKpjxf3rJFfIqK2R-SPXIJR/s790-rw-e365/pipy.jpg)

A new supply chain attack technique targeting the Python Package Index (PyPI) registry has been exploited in the wild in an attempt to infiltrate downstream organizations.

It has been codenamed Revival Hijack by software supply chain security firm JFrog, which said the attack method could be used to hijack 22,000 existing PyPI packages and result in "hundreds of thousands" of malicious package downloads. These susceptible packages have more than 100,000 downloads or have been active for over six months.

"This attack technique involves hijacking PyPI software packages by manipulating the option to re-register them once they're removed from PyPI's index by the original owner," JFrog security researchers Andrey Polkovnychenko and Brian Moussalli said in a [report](https://jfrog.com/blog/revival-hijack-pypi-hijack-technique-exploited-22k-packages-at-risk/) shared with The Hacker News.

At its core, the attack hinges on the fact that Python packages published in the PyPI repository may get removed, making available the [names of those deleted projects](https://discuss.python.org/t/stop-allowing-deleting-things-from-pypi/17227) for registration to any other user.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Statistics shared by JFrog show that about 309 packages are removed each month on average. These could happen for any number of reasons: Lack of maintenance (i.e., abandonware), package getting re-published under a different name, or introducing the same functionality into official libraries or built-in APIs.

This also poses a lucrative attack surface that's more effective than typosquatting and which an attacker, using their own accounts, could exploit to publish malicious packages under the same name and a higher version to infect developer environments.

"The technique does not rely on the victim making a mistake when installing the package," the researchers said, pointing out how Revival Hijack can yield better results from the point of view of an adversary. "Updating a 'once safe' package to its latest version is viewed as a safe operation by many users."

While PyPI does have safeguards in place against author impersonation and typosquatting attempts, JFrog's analysis found that running the "[pip list --outdated](https://pip.pypa.io/en/stable/cli/pip_list/)" command lists the counterfeit package as a new version of the original package, wherein the former corresponds to a different package from an entirely different author.

Even more concerning, running the "[pip install –upgrade](https://pip.pypa.io/en/stable/cli/pip_install/)" command replaces the actual package with the phony one without not so much of a warning that the package's author has changed, potentially exposing unwitting developers to a huge software supply chain risk.

JFrog said it took the step of creating a new PyPI user account called "[security\_holding](https://pypi.org/user/security_holding/)" that it used to safely hijack the susceptible packages and replace them with empty placeholders so as to prevent malicious actors from capitalizing on the removed packages.

Additionally, each of these packages has been assigned the version number as 0.0.0.1 – the opposite of a [dependency confusion attack](https://thehackernews.com/2024/04/apache-cordova-app-harness-targeted-in.html) scenario – to avoid getting pulled by developers when running a pip upgrade command.

What's more disturbing is that Revival Hijack has already been exploited in the wild, with an unknown threat actor called Jinnis introducing a benign version of a package named "[pingdomv3](https://www.pepy.tech/projects/pingdomv3?versions=0.0.2&versions=1.0.0&versions=1.1.0)" on March 30, 2024, the same day the original owner (cheneyyan) removed the package from PyPI.

On April 12, 2024, the new developer is said to have released an update containing a Base64-encoded payload that checks for the presence of the "[JENKINS\_URL](https://www.jenkins.io/doc/book/managing/cli/)" environment variable, and if present, executes an unknown next-stage module retrieved from a remote server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This suggests that the attackers either delayed the delivery of the attack or designed it to be more targeted, possibly limiting it to a specific IP range," JFrog said.

The new attack is a sign that threat actors are eyeing supply chain attacks on a broader scale by targeting deleted PyPI packages in order to expand the reach of the campaigns. Organizations and developers are recommended to inspect their DevOps pipelines to ensure that they are not installing packages that have been already removed from the repository.

"Using a vulnerable behavior in the handling of removed packages allowed attackers to hijack existing packages, making it possible to install it to the target systems without any changes to the user's workflow," said Moussalli, JFrog Security Research Team Lead.

"The PyPI package attack surface is continually growing. Despite proactive intervention here, users should always stay vigilant and take the necessary precautions to protect themselves and the PyPI community from this hijack technique."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read...